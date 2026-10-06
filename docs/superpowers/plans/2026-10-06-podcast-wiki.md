# Podcast Wiki Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ingest every podcast episode the user has heard (followed shows, ≥50% played) on Spotify into a concept-centric, Karpathy-style markdown wiki maintained by Claude.

**Architecture:** A tiny Spotify MCP server lists heard episodes. A Python script turns each new episode into an immutable `raw/` text file (published transcript → mlx-whisper → Spotify description). Claude then updates `wiki/` following rules in `CLAUDE.md`, driven by the `/ingest-podcasts` command (manual) or a launchd job (scheduled).

**Tech Stack:** Python ≥3.11 via `uv`, `mcp` (FastMCP), `spotipy`, `mlx-whisper` (`mlx-community/whisper-large-v3-mlx`), stdlib `urllib`/`xml.etree` for iTunes + RSS, Claude Code slash command, launchd.

**Spec:** `docs/superpowers/specs/2026-10-06-podcast-wiki-design.md`

**Deliberate refinements vs. spec** (same behavior, fewer moving parts):
- `fetch_transcript.py` takes a JSON *list* of episodes (`raw/.heard.json`) and skips already-ingested ones itself, instead of one episode per call — avoids shell-quoting episode JSON and makes dedupe deterministic.
- `fetch_transcript.py --pending` lists raw files that have no wiki episode page yet. The wiki step works off this list, so a run interrupted after fetching heals on the next run.
- `spotify_mcp.py` also has `--auth` (one-time OAuth) and `--list` (prints the same data as the MCP tool). The scheduled job uses `--list` because headless Claude can't wait out long Whisper runs inside its 10-minute tool timeout.
- Fetch errors that might be temporary (network, download) skip the episode so it's retried. Only "no feed/episode match" or "no audio enclosure" falls back to the description.
- Each ingest ends with a git commit of `raw/` and `wiki/`, so a bad concept-page rewrite can be reverted.

## Global Constraints

- Python `>=3.11`, run everything through `uv run` (system python is 3.9).
- Spotify scopes: `user-library-read user-read-playback-position`; redirect URI `http://127.0.0.1:8888/callback`; credentials from `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` (read from gitignored `.env`); token cache `.spotify_cache` (gitignored).
- Heard = `resume_point.fully_played` OR `resume_position_ms / duration_ms >= 0.5`. Only the 20 most recent episodes per followed show.
- Whisper model: `mlx-community/whisper-large-v3-mlx`, auto language detection.
- Raw file path: `raw/<show-slug>/<release_date>-<episode-slug>.md`; frontmatter keys exactly `spotify_id, show, title, release_date, spotify_url, language, source, fetched`; `source` ∈ `transcript|whisper|description`.
- Wiki written in English; Obsidian `[[folder/slug]]` links; slugs lowercase-kebab-case.
- Absolute paths in launchd/MCP config: repo `/Users/hagaihen/projects/knowledgebase`, `uv` at `/Users/hagaihen/.local/bin/uv`, `claude` at `/Users/hagaihen/.local/bin/claude`.

## Review Focus

1. **Hebrew-only show/episode titles**: the ASCII slug comes out empty, so the path must fall back to Spotify IDs, never `raw//-.md` or colliding files. → Task 2 test (`slugify`).
2. **Temporary network failure** (iTunes, feed, transcript, or MP3 download): the episode is skipped and retried next run, never permanently downgraded to description-only. → Task 3 test (`fetch` returns `None`).
3. **Re-running ingest**: no duplicate raw files, and no re-synthesis of episodes that already have wiki pages. → Task 3 test (`ingested_ids`, `pending`).
4. **Missing `resume_point` / `duration_ms` of 0 / null episode entries** from Spotify: no crash, and the episode counts as unheard unless `fully_played`. → Task 1 test.
5. **Spotify title differs from RSS title** (episode-number prefix, `&amp;`, punctuation): still matched via containment within ±2 days, while a same-titled episode from a different year is *not* loosely matched. Titles with quotes/colons survive frontmatter. → Task 2 test (`match_episode`) + Task 3 test (`render` roundtrip).

---

### Task 1: Project scaffold + Spotify MCP server

**Files:**
- Create: `pyproject.toml`, `.gitignore`, `.env.example`, `tools/spotify_mcp.py`, `.mcp.json`, `.claude/settings.json`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - MCP tool `mcp__spotify__list_heard_episodes(min_progress: float = 0.5) -> list[dict]`
  - CLI `uv run tools/spotify_mcp.py --list` → same list as JSON on stdout; `--auth`; `--selftest`
  - Episode dict keys: `id, show_name, show_id, title, release_date, description, duration_ms, progress, spotify_url, language` (all str except `duration_ms: int`, `progress: float`)

- [ ] **Step 1: Create scaffold files**

`pyproject.toml`:
```toml
[project]
name = "podcast-wiki"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["mcp>=1.2", "spotipy>=2.24", "mlx-whisper>=0.4"]

[tool.uv]
package = false
```

`.gitignore`:
```
.env
.spotify_cache
.venv/
__pycache__/
raw/.heard.json
```

`.env.example`:
```
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```

Run: `uv sync`
Expected: creates `.venv` and `uv.lock`, no errors.

- [ ] **Step 2: Write the failing self-check**

Create `tools/spotify_mcp.py` with only the self-check and entry point:
```python
"""Spotify MCP server: podcast episodes the user has heard from followed shows.

  uv run tools/spotify_mcp.py             # MCP server over stdio
  uv run tools/spotify_mcp.py --auth      # one-time interactive OAuth login
  uv run tools/spotify_mcp.py --list      # print heard episodes as JSON (scheduled job)
  uv run tools/spotify_mcp.py --selftest
"""
import json
import os
import sys
from pathlib import Path


def selftest():
    assert progress({"resume_point": {"fully_played": True}, "duration_ms": 0}) == 1.0
    assert progress({"resume_point": {"resume_position_ms": 30_000}, "duration_ms": 60_000}) == 0.5
    assert progress({"resume_point": {"resume_position_ms": 10}, "duration_ms": 0}) == 0.0
    assert progress({"duration_ms": 60_000}) == 0.0
    assert progress({"resume_point": None}) == 0.0

    def ep(id_, pos, dur=100):
        return {"id": id_, "name": f"T{id_}", "release_date": "2026-01-01", "description": "d",
                "duration_ms": dur, "resume_point": {"resume_position_ms": pos},
                "external_urls": {"spotify": f"https://open.spotify.com/episode/{id_}"}, "language": "he"}

    class FakeSpotify:
        def current_user_saved_shows(self, limit):
            return {"items": [{"show": {"id": "s1", "name": "Show"}}], "next": "page2"}

        def next(self, page):
            return {"items": [{"show": {"id": "s2", "name": "Other"}}], "next": None}

        def show_episodes(self, show_id, limit, market):
            return {"items": [None, ep(show_id + "a", 60), ep(show_id + "b", 10)]}

    got = heard_episodes(FakeSpotify(), 0.5)
    assert [e["id"] for e in got] == ["s1a", "s2a"], got
    assert got[0]["show_name"] == "Show" and got[0]["progress"] == 0.6
    assert set(got[0]) == {"id", "show_name", "show_id", "title", "release_date", "description",
                           "duration_ms", "progress", "spotify_url", "language"}
    print("selftest ok")


if __name__ == "__main__":
    selftest()
```

- [ ] **Step 3: Run it to verify it fails**

Run: `uv run tools/spotify_mcp.py --selftest`
Expected: FAIL with `NameError: name 'progress' is not defined`

- [ ] **Step 4: Implement the server**

Replace `tools/spotify_mcp.py` with the full file (selftest body unchanged from Step 2):
```python
"""Spotify MCP server: podcast episodes the user has heard from followed shows.

  uv run tools/spotify_mcp.py             # MCP server over stdio
  uv run tools/spotify_mcp.py --auth      # one-time interactive OAuth login
  uv run tools/spotify_mcp.py --list      # print heard episodes as JSON (scheduled job)
  uv run tools/spotify_mcp.py --selftest
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE = "user-library-read user-read-playback-position"
EPISODES_PER_SHOW = 20  # ponytail: older heard episodes are ignored; paginate show_episodes if that matters


def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def client():
    import spotipy
    from spotipy.cache_handler import CacheFileHandler
    from spotipy.oauth2 import SpotifyOAuth

    load_env()
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://127.0.0.1:8888/callback",
        scope=SCOPE,
        cache_handler=CacheFileHandler(cache_path=str(ROOT / ".spotify_cache")),
    ))


def progress(ep):
    rp = ep.get("resume_point") or {}
    if rp.get("fully_played"):
        return 1.0
    duration = ep.get("duration_ms") or 0
    return rp.get("resume_position_ms", 0) / duration if duration else 0.0


def heard_episodes(sp, min_progress=0.5):
    shows, page = [], sp.current_user_saved_shows(limit=50)
    while page:
        shows += [item["show"] for item in page["items"]]
        page = sp.next(page) if page["next"] else None
    out = []
    for show in shows:
        for ep in sp.show_episodes(show["id"], limit=EPISODES_PER_SHOW, market="from_token")["items"]:
            if not ep:  # Spotify returns null for unavailable episodes
                continue
            p = progress(ep)
            if p < min_progress:
                continue
            out.append({
                "id": ep["id"],
                "show_name": show["name"],
                "show_id": show["id"],
                "title": ep["name"],
                "release_date": ep["release_date"],
                "description": ep.get("description", ""),
                "duration_ms": ep.get("duration_ms") or 0,
                "progress": round(p, 2),
                "spotify_url": ep["external_urls"]["spotify"],
                "language": ep.get("language") or (ep.get("languages") or [""])[0],
            })
    return out


def selftest():
    ...  # exactly the body from Step 2


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--selftest":
        selftest()
    elif arg == "--auth":
        print("Logged in as", client().current_user()["display_name"])
    elif arg == "--list":
        print(json.dumps(heard_episodes(client()), ensure_ascii=False, indent=1))
    else:
        from mcp.server.fastmcp import FastMCP

        mcp = FastMCP("spotify")

        @mcp.tool()
        def list_heard_episodes(min_progress: float = 0.5) -> list[dict]:
            """Podcast episodes from the user's followed Spotify shows that are fully played
            or at least `min_progress` (0-1) played. Checks each show's 20 most recent episodes."""
            return heard_episodes(client(), min_progress)

        mcp.run()
```

- [ ] **Step 5: Run the self-check to verify it passes**

Run: `uv run tools/spotify_mcp.py --selftest`
Expected: `selftest ok`

- [ ] **Step 6: Register the MCP server with Claude Code**

`.mcp.json`:
```json
{
  "mcpServers": {
    "spotify": {
      "command": "/Users/hagaihen/.local/bin/uv",
      "args": ["run", "--project", "/Users/hagaihen/projects/knowledgebase",
               "/Users/hagaihen/projects/knowledgebase/tools/spotify_mcp.py"]
    }
  }
}
```

`.claude/settings.json` (pre-approves the project server so headless runs can use it):
```json
{
  "enabledMcpjsonServers": ["spotify"]
}
```

- [ ] **Step 7: USER ACTION — create the Spotify app and log in**

Ask the user to:
1. Go to https://developer.spotify.com/dashboard → Create app. Redirect URI: `http://127.0.0.1:8888/callback`. API: Web API.
2. `cp .env.example .env` and fill in the Client ID and Client Secret.
3. Run `! uv run tools/spotify_mcp.py --auth`, approve in the browser, and check that it prints `Logged in as <name>`.

- [ ] **Step 8: Live probe — verify `resume_point` is trustworthy**

Run: `uv run tools/spotify_mcp.py --list | head -40`
Expected: a JSON array of episodes. Ask the user to confirm that one or two listed episodes really were finished or mostly played in the Spotify app, and that one episode they're sure they finished appears in the list. If `resume_point` looks wrong (there's a known community report about it on `/shows/{id}/episodes`), stop and report back before going on. The fix would be to re-fetch candidates individually with `sp.episode(id, market="from_token")`.

- [ ] **Step 9: Verify Claude sees the MCP**

Restart Claude Code in the repo, run `/mcp`, and check that `spotify` is connected and lists `list_heard_episodes`.

- [ ] **Step 10: Commit**

```bash
git add pyproject.toml uv.lock .gitignore .env.example tools/spotify_mcp.py .mcp.json .claude/settings.json
git commit -m "feat: Spotify MCP listing heard podcast episodes"
```

---

### Task 2: Episode matching + transcript text conversion (pure functions)

**Files:**
- Create: `tools/fetch_transcript.py`

**Interfaces:**
- Consumes: nothing (pure functions).
- Produces (used by Task 3, same file):
  - `normalize(title: str) -> str`
  - `slugify(text: str, fallback: str) -> str`
  - `parse_date(s: str | None) -> datetime.date | None`
  - `match_episode(items: list[tuple[str, str | None, Any]], title: str, release_date: str, max_days: int = 2) -> Any | None` — returns the matched item's payload (3rd tuple element)
  - `to_text(body: str, kind: str) -> str`

- [ ] **Step 1: Write the failing self-check**

Create `tools/fetch_transcript.py`:
```python
"""Fetch podcast episode text into raw/: published transcript -> Whisper -> Spotify description.

  uv run tools/fetch_transcript.py <episodes.json>   # fetch new episodes, print new raw paths
  uv run tools/fetch_transcript.py --pending         # raw files with no wiki episode page yet
  uv run tools/fetch_transcript.py --selftest
"""
import json
import re
import sys
import unicodedata
from datetime import date
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path


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
    print("selftest ok")


if __name__ == "__main__":
    selftest()
```

- [ ] **Step 2: Run it to verify it fails**

Run: `uv run tools/fetch_transcript.py --selftest`
Expected: FAIL with `NameError: name 'normalize' is not defined`

- [ ] **Step 3: Implement the pure functions**

Insert above `def selftest():`:
```python
ROOT = Path(__file__).resolve().parent.parent
TIMESTAMP = re.compile(r"\d{1,2}:\d{2}[:.,\d]*\s*-->")


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
```

- [ ] **Step 4: Run the self-check to verify it passes**

Run: `uv run tools/fetch_transcript.py --selftest`
Expected: `selftest ok`

- [ ] **Step 5: Commit**

```bash
git add tools/fetch_transcript.py
git commit -m "feat: episode matching and transcript text conversion"
```

---

### Task 3: Fetch chain, raw files, dedupe, pending list

**Files:**
- Modify: `tools/fetch_transcript.py`

**Interfaces:**
- Consumes: Task 2 functions; Task 1 episode dict keys.
- Produces:
  - CLI `uv run tools/fetch_transcript.py <episodes.json>` → writes new raw files, prints `raw/<...>.md <source>` per new file on stdout, `skip <id> (<title>): <error>` on stderr
  - CLI `uv run tools/fetch_transcript.py --pending` → prints one repo-relative raw path per line, for raw files not referenced in any `wiki/episodes/*.md`
  - `fetch(ep) -> tuple[str, str, str | None] | None` (text, source, language) or `None` = skip and retry later
  - `render(ep, text, source, language) -> str`, `raw_path(ep) -> Path`, `ingested_ids(raw: Path) -> set[str]`, `pending(raw: Path, episodes_dir: Path) -> list[str]`

- [ ] **Step 1: Add failing checks to the self-check**

Insert these lines in `selftest()` just before `print("selftest ok")`:
```python
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
```

- [ ] **Step 2: Run it to verify it fails**

Run: `uv run tools/fetch_transcript.py --selftest`
Expected: FAIL with `NameError: name 'raw_path' is not defined`

- [ ] **Step 3: Implement the fetch chain and CLI**

Add to the imports at the top:
```python
import shutil
import tempfile
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
```

Add below the existing `TIMESTAMP = ...` line:
```python
RAW = ROOT / "raw"
EPISODES = ROOT / "wiki" / "episodes"
PODCAST_NS = "{https://podcastindex.org/namespace/1.0}"
TRANSCRIPT_PREFERENCE = ("text/vtt", "application/x-subrip", "application/srt",
                         "application/json", "text/html", "text/plain")
WHISPER_MODEL = "mlx-community/whisper-large-v3-mlx"
UA = {"User-Agent": "podcast-wiki/0.1"}
```

Add below `to_text`, above `selftest`:
```python
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
        result = mlx_whisper.transcribe(str(audio), path_or_hf_repo=WHISPER_MODEL)
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
```

Note on the `pending` selftest: the raw files under the temp dir are referenced in the episode page by absolute path, while `pending` compares paths relative to `root`. The test passes `root=Path(tmp).parent`, so the relative path `tmpXXXX/raw/show1/a.md` is a substring of the absolute path written in `e.md`. In production, episode pages store `raw: raw/<show>/<file>.md`, which matches the relative path exactly.

Replace the `if __name__ == "__main__":` block:
```python
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
```

- [ ] **Step 4: Run the self-check to verify it passes**

Run: `uv run tools/fetch_transcript.py --selftest`
Expected: `selftest ok`

- [ ] **Step 5: Live run on one episode**

```bash
uv run tools/spotify_mcp.py --list > raw/.heard.json
uv run python -c "import json; d=json.load(open('raw/.heard.json')); json.dump(d[:1], open('raw/.one.json','w'), ensure_ascii=False)"
uv run tools/fetch_transcript.py raw/.one.json
```
Expected: one line like `raw/<show>/<date>-<slug>.md whisper` (or `transcript`/`description`). The first Whisper run downloads the model (~3 GB). Open the file and check that the frontmatter is valid and the text is real transcript content in the episode's language. Run the same command again and expect no output, since the episode is deduped. Then `uv run tools/fetch_transcript.py --pending` should list that file.

Clean up: `rm raw/.one.json`. Keep the raw file; Task 4 ingests it.

- [ ] **Step 6: Commit**

```bash
git add tools/fetch_transcript.py
git commit -m "feat: fetch episode text into raw/ with transcript/whisper/description fallback"
```

---

### Task 4: Wiki schema (`CLAUDE.md`), skeleton, `/ingest-podcasts` command

**Files:**
- Create: `CLAUDE.md`, `wiki/index.md`, `wiki/log.md`, `wiki/takeaways/to-try.md`, `wiki/takeaways/recommendations.md`, `.claude/commands/ingest-podcasts.md`

**Interfaces:**
- Consumes: MCP tool `mcp__spotify__list_heard_episodes`; CLIs `tools/fetch_transcript.py <file>` and `--pending`; raw frontmatter keys.
- Produces: the "Wiki update procedure" section in `CLAUDE.md` (Task 5's headless run invokes it by that name); `/ingest-podcasts`.

- [ ] **Step 1: Write `CLAUDE.md`**

````markdown
# Podcast Wiki

A Karpathy-style LLM wiki built from podcasts the user listens to on Spotify. Claude maintains `wiki/`; `raw/` is immutable source text. Primary purpose: **learning topics across episodes** (concept pages). Secondary: **actionable takeaways**.

## Layout

- `raw/<show>/<date>-<slug>.md` — source text with frontmatter (`spotify_id, show, title, release_date, spotify_url, language, source, fetched`). Never edit.
- `wiki/concepts/<slug>.md` — PRIMARY. One topic, synthesized across all episodes.
- `wiki/hubs/<domain>.md` — a domain (health, investing, …): overview + its concepts.
- `wiki/episodes/<show-slug>--<episode-slug>.md` — short source note per episode.
- `wiki/people/<slug>.md` — who they are, episodes, linked concepts.
- `wiki/shows/<slug>.md` — show description + ingested episodes.
- `wiki/takeaways/to-try.md` — checklist of actionable items.
- `wiki/takeaways/recommendations.md` — books / tools / people, grouped by type.
- `wiki/index.md` — every page, one line each, grouped by hub ("Unsorted" for concepts with no hub page yet).
- `wiki/log.md` — append-only ingest log.

Tools: `uv run tools/fetch_transcript.py --pending` lists raw files not yet in the wiki.

## Conventions

- Write everything in **English**. Translate Hebrew sources during synthesis; proper names in common English spelling.
- Links: Obsidian wikilinks `[[concepts/zone-2-training]]`. Slugs: lowercase-kebab-case English.
- Every claim links its episode, and the person who made it when identifiable.

## Page templates

Concept:
```markdown
---
type: concept
hubs: [health]
sources: 4
updated: YYYY-MM-DD
---
# Zone 2 Training

**Summary:** 3–5 sentence synthesis of everything known so far.

## Key ideas
- Claim … ([[episodes/huberman--endurance]], [[people/peter-attia]])

## Disagreements & open questions
- Attia says 3–4h/week; Galpin argues 2h is enough … ([[episodes/...]], [[episodes/...]])

## Takeaways
- [ ] Try 4×45min zone-2 sessions/week ([[episodes/...]])

## Related
[[concepts/vo2-max]] · [[concepts/mitochondria]]
```

Episode:
```markdown
---
type: episode
show: <show name>
date: YYYY-MM-DD
guests: ["[[people/...]]"]
spotify_url: <url>
source: transcript|whisper|description
raw: raw/<show>/<file>.md
---
# <Episode title (English)>

5-line summary.

**Concepts:** [[concepts/a]] · [[concepts/b]]
```

Person: frontmatter `type: person`; one-line bio; `## Appearances` (episode links); `## Concepts` (links).
Show: frontmatter `type: show`; short description; `## Episodes` (links, newest first).
Hub: frontmatter `type: hub`; 2–4 sentence domain overview; `## Concepts` (link + one line each).

## Wiki update procedure

For each raw file from `uv run tools/fetch_transcript.py --pending`, one at a time:

1. Read the raw file.
2. Pick 3–10 concepts (1–3 if `source: description` — thin source). For each, check `wiki/index.md` and grep `wiki/concepts/` for an existing page that fits; **extend existing pages rather than creating near-duplicates**.
3. For each concept page (new or existing):
   - **Rewrite** the Summary to integrate the new material (don't append).
   - Add new claims to Key ideas with episode + person links.
   - A claim that conflicts with an existing one goes under Disagreements & open questions with both sources. **Never silently overwrite an existing claim.**
   - Actionable items go in Takeaways.
   - Set `hubs` (1–2 domains), bump `sources`, set `updated`.
4. Append each actionable item to `wiki/takeaways/to-try.md` as `- [ ] item — [[concepts/x]] · [[episodes/y]]`. Add recommended books/tools/people to `wiki/takeaways/recommendations.md` under the right heading, with the episode link.
5. Write the episode page (its `raw:` field must be the exact repo-relative raw path; this marks the raw file as done). If `source: description`, add a line `> Thin source: based on the episode description only.`
6. Create or update the show page and the people pages.
7. Hubs: for each domain with ≥5 concepts and no `wiki/hubs/<domain>.md`, create it; otherwise update the existing hub's concept list.
8. Update `wiki/index.md` for every page created.
9. Append to `wiki/log.md`: `## YYYY-MM-DD — <show>: <episode title>` then `source: …`, `created: …`, `updated: …`.
````

- [ ] **Step 2: Create the wiki skeleton**

`wiki/index.md`:
```markdown
# Index

## Unsorted
```

`wiki/log.md`:
```markdown
# Ingest log
```

`wiki/takeaways/to-try.md`:
```markdown
# To try
```

`wiki/takeaways/recommendations.md`:
```markdown
# Recommendations

## Books

## Tools

## People
```

- [ ] **Step 3: Write the command**

`.claude/commands/ingest-podcasts.md`:
```markdown
---
description: Ingest newly heard Spotify podcast episodes into the wiki
allowed-tools: mcp__spotify__list_heard_episodes, Bash(uv run tools/fetch_transcript.py:*), Bash(git add:*), Bash(git commit:*), Read, Write, Edit, Glob, Grep
---
1. Call `mcp__spotify__list_heard_episodes`. Write its result, unchanged, as a JSON array to `raw/.heard.json`.
2. Run `uv run tools/fetch_transcript.py raw/.heard.json` with `run_in_background: true` (Whisper can take many minutes per episode) and wait for it to finish. Stdout has one `raw/... <source>` line per new episode; stderr has `skip ...` lines.
3. Run `uv run tools/fetch_transcript.py --pending` and follow the **Wiki update procedure** in `CLAUDE.md` for each listed file.
4. For each `skip` line from step 2, append to `wiki/log.md`: `## YYYY-MM-DD — skipped: <title>` with the error.
5. If anything changed: `git add raw wiki && git commit -m "ingest: <N> episodes"`.
6. Reply with: episodes ingested (with source type), concept pages created/updated, skipped episodes.
```

- [ ] **Step 4: End-to-end run**

Restart Claude Code in the repo, run `/ingest-podcasts`, and verify:
- the raw file from Task 3 now has `wiki/episodes/<...>.md` with a matching `raw:` field, and `--pending` no longer lists it;
- concept pages follow the template, are in English, and every claim links an episode;
- `index.md`, `log.md`, and `to-try.md` were updated, and a git commit `ingest: …` exists;
- running `/ingest-podcasts` a second time with nothing new heard ingests 0 episodes and makes no wiki changes.

Ask the user to read two concept pages and confirm the quality before moving on. Tune the rules in `CLAUDE.md` if needed.

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md .claude/commands/ingest-podcasts.md
git commit -m "feat: wiki schema and /ingest-podcasts command"
```
(The skeleton files and first ingest were already committed by the command in Step 4.)

---

### Task 5: Scheduled ingest (launchd)

**Files:**
- Create: `tools/scheduled_ingest.sh`, `tools/com.user.podcast-wiki.plist`

**Interfaces:**
- Consumes: `spotify_mcp.py --list`, `fetch_transcript.py <file>` / `--pending`, the "Wiki update procedure" in `CLAUDE.md`.
- Produces: a launchd agent `com.user.podcast-wiki` that runs every 6 hours.

- [ ] **Step 1: Write the job script**

`tools/scheduled_ingest.sh`:
```bash
#!/bin/bash
# Scheduled ingest: list heard episodes, fetch their text (outside Claude, Whisper is slow),
# then have headless Claude update the wiki for pending raw files.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "=== $(date) ==="
uv run tools/spotify_mcp.py --list > raw/.heard.json
uv run tools/fetch_transcript.py raw/.heard.json
if [ -n "$(uv run tools/fetch_transcript.py --pending)" ]; then
  claude -p "Follow the Wiki update procedure in CLAUDE.md for every file listed by \`uv run tools/fetch_transcript.py --pending\`. Then, if anything changed, run: git add raw wiki && git commit -m \"ingest: scheduled\"" \
    --allowedTools "Read,Write,Edit,Glob,Grep,Bash(uv run tools/fetch_transcript.py --pending),Bash(git add:*),Bash(git commit:*)"
fi
```

Run: `chmod +x tools/scheduled_ingest.sh`

- [ ] **Step 2: Run it manually**

Run: `PATH=/Users/hagaihen/.local/bin:/opt/homebrew/bin:/usr/bin:/bin tools/scheduled_ingest.sh`
Expected: exits 0. If nothing new was heard, there's no `claude` call. To exercise the Claude step, ask the user to listen to most of an episode first, or temporarily move one episode page out of `wiki/episodes/` so its raw file shows up as pending, then put it back.

- [ ] **Step 3: Write and load the launchd agent**

`tools/com.user.podcast-wiki.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.user.podcast-wiki</string>
  <key>ProgramArguments</key>
  <array><string>/Users/hagaihen/projects/knowledgebase/tools/scheduled_ingest.sh</string></array>
  <key>StartInterval</key><integer>21600</integer>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>/Users/hagaihen/.local/bin:/opt/homebrew/bin:/usr/bin:/bin</string></dict>
  <key>StandardOutPath</key><string>/Users/hagaihen/Library/Logs/podcast-wiki.log</string>
  <key>StandardErrorPath</key><string>/Users/hagaihen/Library/Logs/podcast-wiki.log</string>
</dict>
</plist>
```

```bash
cp tools/com.user.podcast-wiki.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.user.podcast-wiki.plist
launchctl kickstart gui/$(id -u)/com.user.podcast-wiki
```

- [ ] **Step 4: Verify the launchd run**

Run: `tail -30 ~/Library/Logs/podcast-wiki.log`
Expected: a fresh `=== <date> ===` header and no errors. Watch in particular for `claude` auth/keychain errors, `uv` not found, or a Spotify token prompt. A token prompt means `.spotify_cache` is missing, so re-run `--auth`. Run `launchctl print gui/$(id -u)/com.user.podcast-wiki | grep "last exit code"` and expect `0`.

- [ ] **Step 5: Commit**

```bash
git add tools/scheduled_ingest.sh tools/com.user.podcast-wiki.plist
git commit -m "feat: scheduled podcast ingest via launchd"
```
