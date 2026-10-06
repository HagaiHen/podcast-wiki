#!/bin/bash
# Scheduled ingest: list heard episodes, fetch their text (outside Claude, Whisper is slow),
# then have headless Claude update the wiki for pending raw files.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "=== $(date) ==="
mkdir -p raw
uv run tools/spotify_mcp.py --list > raw/.heard.json
uv run tools/fetch_transcript.py raw/.heard.json
if [ -n "$(uv run tools/fetch_transcript.py --pending)" ]; then
  claude -p "Follow the Wiki update procedure in CLAUDE.md for every file listed by \`uv run tools/fetch_transcript.py --pending\`. Then, if anything changed, run: git add raw wiki && git commit -m \"ingest: scheduled\"" \
    --allowedTools "Read,Write,Edit,Glob,Grep,Bash(uv run tools/fetch_transcript.py --pending),Bash(git add:*),Bash(git commit:*)"
fi
