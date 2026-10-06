"""Fetch podcast episode text into raw/: published transcript -> Whisper -> Spotify description.

  uv run tools/fetch_transcript.py <episodes.json>   # fetch new episodes, print new raw paths
  uv run tools/fetch_transcript.py --pending         # raw files with no wiki episode page yet
  uv run tools/fetch_transcript.py --selftest
"""
import json
import re
import shutil
import sys
import tempfile
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMESTAMP = re.compile(r"\d{1,2}:\d{2}[:.,\d]*\s*-->")
RAW = ROOT / "raw"
EPISODES = ROOT / "wiki" / "episodes"
PODCAST_NS = "{https://podcastindex.org/namespace/1.0}"
TRANSCRIPT_PREFERENCE = ("text/vtt", "application/x-subrip", "application/srt",
                         "application/json", "text/html", "text/plain")
WHISPER_MODEL = "mlx-community/whisper-large-v3-mlx"
UA = {"User-Agent": "podcast-wiki/0.1"}


def normalize(title):
    title = unicodedata.normalize("NFKC", unescape(title)).casefold()
    return " ".join(re.sub(r"[^\w\s]", " ", title).split())


def slugify(text, fallback):
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")[:60].strip("-") or fallback


def parse_date(s):
    """Spotify 'YYYY-MM-DD' or RSS RFC-2822 -> date; None if missing or imprecise."""
    if not s:
        return None
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
            return date.fromisoformat(s)
        return parsedate_to_datetime(s).date()
    except (TypeError, ValueError):
        return None


def match_episode(items, title, release_date, max_days=2):
    """items: [(rss_title, pubDate, payload)]. Exact normalized title wins (closest date breaks
    ties); otherwise one title containing the other, but only within max_days of release_date."""
    want, want_date = normalize(title), parse_date(release_date)

    def days(pub):
        d = parse_date(pub)
        return abs((d - want_date).days) if d and want_date else None

    exact = [(days(pub), payload) for t, pub, payload in items if normalize(t) == want]
    if exact:
        return min(exact, key=lambda e: 10**6 if e[0] is None else e[0])[1]
    loose = []
    for t, pub, payload in items:
        n, d = normalize(t), days(pub)
        if want and n and (want in n or n in want) and d is not None and d <= max_days:
            loose.append((d, payload))
    return min(loose, key=lambda e: e[0])[1] if loose else None


def to_text(body, kind):
    """podcast:transcript body (vtt / srt / json / html / plain) -> plain text."""
    if "json" in kind:
        return " ".join(seg.get("body", "") for seg in json.loads(body).get("segments", []))
    if "html" in kind:
        return " ".join(unescape(re.sub(r"<[^>]+>", " ", body)).split())
    lines, prev = [], None
    for line in body.splitlines():
        line = re.sub(r"<[^>]+>", "", line).strip()  # VTT voice tags like <v Alice>
        if not line or line == "WEBVTT" or line.startswith("NOTE") or line.isdigit() or TIMESTAMP.search(line):
            continue
        if line != prev:  # captions often repeat across cues
            lines.append(line)
        prev = line
    return "\n".join(lines)


def get(url, timeout=60):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def find_item(show_name, title, release_date):
    """RSS <item> for the episode, or None if no feed/episode matches. Network errors raise."""
    query = urllib.parse.urlencode({"media": "podcast", "entity": "podcast", "term": show_name, "limit": 5})
    results = json.loads(get(f"https://itunes.apple.com/search?{query}"))["results"]
    results.sort(key=lambda r: normalize(r.get("collectionName", "")) != normalize(show_name))  # exact name first
    for result in results[:3]:
        if not result.get("feedUrl"):
            continue
        try:
            root = ET.fromstring(get(result["feedUrl"]))
        except ET.ParseError as e:
            print(f"bad feed {result['feedUrl']}: {e}", file=sys.stderr)
            continue
        items = [(i.findtext("title", ""), i.findtext("pubDate"), i) for i in root.iter("item")]
        item = match_episode(items, title, release_date)
        if item is not None:
            return item
    return None


def transcript_text(item):
    """(text, None) from the feed's <podcast:transcript>, or (None, None) if it has none."""
    tags = item.findall(f"{PODCAST_NS}transcript")
    rank = {t: i for i, t in enumerate(TRANSCRIPT_PREFERENCE)}
    for tag in sorted(tags, key=lambda t: rank.get(t.get("type"), len(rank))):
        if tag.get("url"):
            text = to_text(get(tag.get("url")).decode("utf-8", "replace"), tag.get("type", ""))
            if text.strip():
                return text, None
    return None, None


def whisper_text(item):
    """(text, language) by transcribing the <enclosure> audio, or (None, None) if there's no audio."""
    enclosure = item.find("enclosure")
    if enclosure is None or not enclosure.get("url"):
        return None, None
    import mlx_whisper

    with tempfile.TemporaryDirectory() as tmp:
        audio = Path(tmp) / "episode-audio"
        req = urllib.request.Request(enclosure.get("url"), headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r, open(audio, "wb") as f:
            shutil.copyfileobj(r, f)
        print(f"transcribing {item.findtext('title', '')[:60]}", file=sys.stderr, flush=True)
        result = mlx_whisper.transcribe(str(audio), path_or_hf_repo=WHISPER_MODEL, verbose=False)  # verbose=False = tqdm progress bar on stderr
    text = "\n".join(seg["text"].strip() for seg in result.get("segments", [])) or result["text"].strip()
    return text, result.get("language")


def fetch(ep):
    """(text, source, language), or None to skip this run (transient error; retried next run)."""
    try:
        item = find_item(ep["show_name"], ep["title"], ep["release_date"])
        if item is not None:
            for source, fn in (("transcript", transcript_text), ("whisper", whisper_text)):
                text, language = fn(item)
                if text:
                    return text, source, language
    except Exception as e:  # ponytail: any failure = retry next run; a permanently broken step shows up as repeated skips in log.md
        print(f"skip {ep['id']} ({ep['title']}): {e}", file=sys.stderr)
        return None
    return ep.get("description") or "", "description", None


def raw_path(ep):
    show = slugify(ep["show_name"], ep["show_id"])
    return RAW / show / f"{ep['release_date']}-{slugify(ep['title'], ep['id'])}.md"


def render(ep, text, source, language):
    meta = {
        "spotify_id": ep["id"], "show": ep["show_name"], "title": ep["title"],
        "release_date": ep["release_date"], "spotify_url": ep["spotify_url"],
        "language": (language or ep.get("language") or "")[:2], "source": source,
        "fetched": date.today().isoformat(),
    }
    front = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
    return f"---\n{front}\n---\n{text.strip()}\n"


def ingested_ids(raw=RAW):
    ids = set()
    for p in raw.rglob("*.md"):
        with open(p, encoding="utf-8") as f:
            m = re.search(r'^spotify_id: "([^"]+)"', f.read(1000), re.M)
        if m:
            ids.add(m.group(1))
    return ids


def pending(raw=RAW, episodes_dir=EPISODES, root=ROOT):
    pages = " ".join(p.read_text(encoding="utf-8") for p in episodes_dir.glob("*.md")) if episodes_dir.exists() else ""
    rels = (str(p.relative_to(root)) for p in sorted(raw.rglob("*.md")))
    return [rel for rel in rels if rel not in pages]


def process(episodes):
    done = ingested_ids()
    for ep in episodes:
        if ep["id"] in done:
            continue
        fetched = fetch(ep)
        if fetched is None:
            continue
        text, source, language = fetched
        path = raw_path(ep)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(ep, text, source, language), encoding="utf-8")
        done.add(ep["id"])
        print(path.relative_to(ROOT), source, flush=True)


def selftest():
    # normalize: case, punctuation, entities, Hebrew kept
    assert normalize("#12: Sleep &amp; Dopamine!") == "12 sleep dopamine"
    assert normalize("שינה ודופמין?") == "שינה ודופמין"
    # slugify: Hebrew-only text falls back
    assert slugify("Zone 2: Training!", "x") == "zone-2-training"
    assert slugify("עושים היסטוריה", "show123") == "show123"
    assert len(slugify("a" * 100, "x")) == 60
    # parse_date
    assert parse_date("2026-03-05") == date(2026, 3, 5)
    assert parse_date("Thu, 05 Mar 2026 08:00:00 +0000") == date(2026, 3, 5)
    assert parse_date("2026") is None and parse_date(None) is None and parse_date("garbage") is None
    # match_episode
    items = [
        ("Sleep & Dopamine", "Thu, 05 Mar 2026 08:00:00 +0000", "exact-2026"),
        ("Sleep & Dopamine", "Mon, 05 Mar 2018 08:00:00 +0000", "exact-2018"),
        ("#45 - Zone 2 Training with Peter", "Fri, 06 Mar 2026 08:00:00 +0000", "loose"),
        ("Intro", "Sat, 01 Jan 2000 08:00:00 +0000", "old-intro"),
    ]
    assert match_episode(items, "Sleep &amp; Dopamine", "2026-03-05") == "exact-2026"
    assert match_episode(items, "sleep and dopamine", "2026-03-05") is None
    assert match_episode(items, "Zone 2 Training with Peter", "2026-03-05") == "loose"
    assert match_episode(items, "Zone 2 Training with Peter", "2025-03-05") is None  # loose needs date
    assert match_episode(items, "Intro to habits", "2026-03-05") is None  # "intro" is old
    assert match_episode([], "anything", "2026-03-05") is None
    # to_text
    vtt = "WEBVTT\n\n1\n00:00:01.000 --> 00:00:03.000\n<v Alice>Hello there</v>\n\n2\n00:00:03.000 --> 00:00:05.000\nHello there\nGeneral idea\n"
    assert to_text(vtt, "text/vtt") == "Hello there\nGeneral idea"
    srt = "1\n00:00:01,000 --> 00:00:03,000\nFirst line\n\n2\n00:00:03,000 --> 00:00:05,000\nSecond line\n"
    assert to_text(srt, "application/x-subrip") == "First line\nSecond line"
    assert to_text('{"segments": [{"body": "a"}, {"body": "b"}]}', "application/json") == "a b"
    assert to_text("<p>Hi &amp; bye</p>\n<p>next</p>", "text/html") == "Hi & bye next"
    # render + ingested_ids roundtrip (quotes/colons/Hebrew in title survive frontmatter)
    import tempfile
    ep = {"id": "ep1", "show_name": "עושים היסטוריה", "show_id": "show1", "title": 'Part 2: "Rome"',
          "release_date": "2026-03-05", "description": "desc text", "spotify_url": "https://x/ep1",
          "language": "he"}
    assert raw_path(ep).relative_to(ROOT).as_posix() == "raw/show1/2026-03-05-part-2-rome.md"
    with tempfile.TemporaryDirectory() as tmp:
        raw, episodes_dir = Path(tmp) / "raw", Path(tmp) / "episodes"
        (raw / "show1").mkdir(parents=True)
        episodes_dir.mkdir()
        doc = render(ep, "body", "whisper", "he")
        assert '\ntitle: "Part 2: \\"Rome\\""\n' in doc and "\nsource: \"whisper\"\n" in doc
        (raw / "show1" / "a.md").write_text(doc, encoding="utf-8")
        (raw / "show1" / "b.md").write_text(render(dict(ep, id="ep2"), "x", "description", None), encoding="utf-8")
        assert ingested_ids(raw) == {"ep1", "ep2"}
        (episodes_dir / "e.md").write_text(f"raw: {raw / 'show1' / 'a.md'}", encoding="utf-8")
        assert pending(raw, episodes_dir, root=Path(tmp).parent) == [str((raw / "show1" / "b.md").relative_to(Path(tmp).parent))]
    # fetch: transient error -> None (retry later); no match -> description
    real_find_item = globals()["find_item"]
    try:
        def network_down(*_):
            raise OSError("network down")
        globals()["find_item"] = network_down
        assert fetch(ep) is None
        globals()["find_item"] = lambda *_: None
        assert fetch(ep) == ("desc text", "description", None)
    finally:
        globals()["find_item"] = real_find_item
    print("selftest ok")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--selftest":
        selftest()
    elif arg == "--pending":
        print("\n".join(pending()))
    elif arg:
        process(json.loads(Path(arg).read_text(encoding="utf-8")))
    else:
        sys.exit(__doc__)
