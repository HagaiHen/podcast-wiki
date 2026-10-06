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
