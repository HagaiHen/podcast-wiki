#!/bin/bash
# Scheduled ingest: list heard episodes, fetch their text (outside Claude, Whisper is slow),
# then have headless Claude update the wiki for pending raw files.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "=== $(date) ==="
mkdir -p raw
uv run tools/spotify_mcp.py --list > raw/.heard.json
uv run tools/fetch_transcript.py raw/.heard.json  # also appends skipped episodes to wiki/log.md
if [ -n "$(uv run tools/fetch_transcript.py --pending)" ]; then
  # Claude reads untrusted transcripts, so it may only write inside wiki/ and run no git itself.
  # Edit(wiki/**) also covers creating files; a Write(...) rule is ignored by Claude Code.
  claude -p "Follow the Wiki update procedure in CLAUDE.md for every file listed by \`uv run tools/fetch_transcript.py --pending\`. You run unattended: never ask questions or offer options; if a step is blocked, skip that episode and say why in one line." \
    --permission-mode default --allowedTools "Read,Glob,Grep,Edit(wiki/**),Bash(uv run tools/fetch_transcript.py --pending)"
fi
# A half-done ingest stays local (uncommitted) so it never reaches GitHub or the site; the next run finishes it.
if [ -n "$(uv run tools/fetch_transcript.py --pending)" ]; then
  echo "ingest incomplete, not committing; still pending:"; uv run tools/fetch_transcript.py --pending
  osascript -e 'display notification "Scheduled ingest incomplete, see ~/Library/Logs/podcast-wiki.log" with title "Podcast Wiki"' || true
  exit 1
fi
git add wiki
# "-- wiki" commits only wiki/, even if something else is staged.
git diff --cached --quiet -- wiki || git commit -q -m "ingest: scheduled" -- wiki
git push -q || echo "push failed; commits stay local until the next run"
