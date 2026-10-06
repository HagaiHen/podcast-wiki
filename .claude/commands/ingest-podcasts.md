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
