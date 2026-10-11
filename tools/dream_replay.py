"""Replay recent Claude Code sessions for the /dream skill.

Prints each human prompt since the last dream, paired with the tail of the assistant text
that preceded it, so corrections ("no, too heavy") read in context. Then lists outcomes nobody
typed out: commits in the window that look like fixes or reverts, and failures logged by the
scheduled ingest job.

  uv run tools/dream_replay.py            # sessions since memory/.last-dream (default: 7 days)
  uv run tools/dream_replay.py --since 2026-10-01
  uv run tools/dream_replay.py --stamp    # record now as the last dream
  uv run tools/dream_replay.py --selftest
"""
import argparse, json, os, re, subprocess, sys, tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"
JOB_LOG = Path.home() / "Library" / "Logs" / "podcast-wiki.log"  # tools/scheduled_ingest.sh
CTX = 300  # chars of preceding assistant text to show
# ponytail: keyword heuristic on commit subjects; misses silent fixes, read `git show` for the why
# ponytail: keyword heuristic on log lines; the full run is in the log if a line needs context
FAILURE = re.compile(r"\w+(Error|Exception):|refused|not allowed|permission|incomplete|failed|blocked|stopped|didn't ingest", re.I)
OUTCOME = re.compile(r"\b(fix\w*|revert\w*|broke\w*|break|breaks|repair\w*|undo|regress\w*|wrong)\b", re.I)


def project_dir(cwd=None):
    return PROJECTS / str(Path(cwd or os.getcwd()).resolve()).replace("/", "-")


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def human_text(d):
    """Text of a typed human prompt, or None for tool results, hooks, notifications."""
    if d.get("type") != "user" or (d.get("origin") or {}).get("kind") != "human":
        return None
    c = (d.get("message") or {}).get("content")
    if isinstance(c, list):
        c = " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    if not isinstance(c, str) or not c.strip() or c.lstrip().startswith("<"):
        return None
    return c.strip()


def assistant_text(d):
    if d.get("type") != "assistant":
        return None
    c = (d.get("message") or {}).get("content")
    if not isinstance(c, list):
        return None
    t = " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text").strip()
    return t or None


def replay(pdir, since):
    """[(session_id, title, [(ts, prev_assistant_tail, prompt)])] for sessions touched since `since`."""
    out = []
    for f in sorted(pdir.glob("*.jsonl"), key=os.path.getmtime):
        if datetime.fromtimestamp(f.stat().st_mtime, timezone.utc) < since:
            continue
        title, last, turns = f.stem, "", []
        for line in f.open(encoding="utf-8", errors="replace"):
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if d.get("type") == "ai-title":
                title = d.get("aiTitle") or title
            elif (a := assistant_text(d)):
                last = a
            elif (h := human_text(d)) and d.get("timestamp") and parse_ts(d["timestamp"]) >= since:
                turns.append((d["timestamp"][:16].replace("T", " "), last[-CTX:], h))
        if turns:
            out.append((f.stem, title, turns))
    return out


def outcomes(since, log=None):
    """Commit lines (hash date subject) since `since` whose subject reads like a fix or revert."""
    if log is None:
        log = subprocess.run(["git", "log", f"--since={since.isoformat()}", "--date=short", "--format=%h %ad %s"],
                             capture_output=True, text=True).stdout
    return [l for l in log.splitlines()
            if OUTCOME.search(s := l.split(" ", 2)[-1]) and not s.startswith("dream:")]


def run_start(header):
    """Datetime of a `=== <date> ===` job-log header: ISO, or the old `date` default format."""
    d = header.strip("= \n")
    try:
        return datetime.fromisoformat(d)
    except ValueError:
        parts = d.split()  # Tue Oct  6 22:02:04 IDT 2026: drop the zone name, read as local time
        return datetime.strptime(" ".join(parts[:4] + parts[5:]), "%a %b %d %H:%M:%S %Y").astimezone()


def failures(since, text=None):
    """[(run header, [failure lines])] for scheduled-ingest runs since `since`."""
    if text is None:
        text = JOB_LOG.read_text(errors="replace") if JOB_LOG.exists() else ""
    out, cur = [], None
    for line in text.splitlines():
        if line.startswith("=== "):
            cur = (line.strip("= "), []) if run_start(line) >= since else None
            if cur:
                out.append(cur)
        elif cur and FAILURE.search(line) and line.strip()[:200] not in cur[1]:
            cur[1].append(line.strip()[:200])
    return [r for r in out if r[1]]


def render(sessions):
    lines = []
    for sid, title, turns in sessions:
        lines.append(f"## {title} ({sid[:8]})")
        for ts, prev, prompt in turns:
            if prev:
                lines.append(f"  claude: …{' '.join(prev.split())}")
            lines.append(f"[{ts}] user: {prompt}")
        lines.append("")
    return "\n".join(lines) or "no human prompts since last dream"


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        rows = [
            {"type": "ai-title", "aiTitle": "Promo video"},
            {"type": "assistant", "message": {"content": [{"type": "text", "text": "Here is a synth track."}]}},
            {"type": "user", "origin": {"kind": "human"}, "timestamp": "2026-10-07T10:00:00Z", "message": {"content": "too heavy, lighter"}},
            {"type": "user", "origin": {"kind": "human"}, "timestamp": "2026-10-07T10:01:00Z", "message": {"content": "<task-notification>x"}},
            {"type": "user", "timestamp": "2026-10-07T10:02:00Z", "message": {"content": [{"type": "tool_result", "content": "ok"}]}},
            {"type": "user", "origin": {"kind": "human"}, "timestamp": "2026-09-01T10:00:00Z", "message": {"content": "old"}},
        ]
        (p / "s1.jsonl").write_text("\n".join(map(json.dumps, rows)) + "\nnot json\n")
        got = replay(p, parse_ts("2026-10-01T00:00:00Z"))
        assert [t[2] for t in got[0][2]] == ["too heavy, lighter"], got
        assert got[0][1] == "Promo video" and got[0][2][0][1] == "Here is a synth track."
        assert "claude: …Here is a synth track." in render(got)
        assert replay(p, datetime.now(timezone.utc) + timedelta(days=1)) == []
        assert project_dir("/a/b") == PROJECTS / "-a-b"
        log = "b0be0ce 2026-10-10 scheduled ingest: absolute Edit rule so a cd doesn't break write\n705daae 2026-10-10 ingest: 1 episodes\nabc1234 2026-10-09 Revert \"promo: x\""
        log += "\ne6cb107 2026-10-11 dream: learn from fix commits"
        assert [l[:7] for l in outcomes(None, log)] == ["b0be0ce", "abc1234"]
        joblog = ("=== Thu Oct  8 10:15:05 IDT 2026 ===\nThe run stopped: no permission\nok line\n"
                  "=== 2026-10-11T10:15:01+03:00 ===\nTraceback (most recent call last):\n"
                  "requests.exceptions.ConnectionError: aborted\nrequests.exceptions.ConnectionError: aborted\n"
                  "=== 2026-10-12T10:15:01+03:00 ===\nall good\n")
        got = failures(parse_ts("2026-10-09T00:00:00Z"), joblog)
        assert got == [("2026-10-11T10:15:01+03:00", ["requests.exceptions.ConnectionError: aborted"])], got
        assert len(failures(parse_ts("2026-10-01T00:00:00Z"), joblog)) == 2
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    pdir = project_dir()
    stamp = pdir / "memory" / ".last-dream"
    if a.stamp:
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text(datetime.now(timezone.utc).isoformat())
        return print(f"stamped {stamp}")
    if a.since:
        since = parse_ts(a.since if "T" in a.since else a.since + "T00:00:00+00:00")
    elif stamp.exists():
        since = parse_ts(stamp.read_text().strip())
    else:
        since = datetime.now(timezone.utc) - timedelta(days=7)
    print(f"# replay since {since.isoformat()[:16]} · memory dir: {pdir / 'memory'}\n")
    print(render(replay(pdir, since)))
    print("\n# outcomes: fix/revert commits since then (`git show <hash>` for the why)")
    print("\n".join(outcomes(since)) or "none")
    print(f"\n# outcomes: scheduled-ingest failures since then ({JOB_LOG})")
    print("\n".join(f"{h}\n  " + "\n  ".join(ls) for h, ls in failures(since)) or "none")


if __name__ == "__main__":
    sys.exit(main())
