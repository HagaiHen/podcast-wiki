# Podcast Wiki — Design

Date: 2026-10-06

## Goal

Every podcast episode the user finishes (or plays ≥50% of) on Spotify, from shows they follow, is ingested into a Karpathy-style LLM wiki: interlinked markdown pages maintained by Claude. The wiki's primary purpose is **learning topics across episodes** (concept-centric synthesis), secondarily **actionable takeaways** (things to try, recommendations).

### Decisions made

| Topic | Decision |
|---|---|
| Content source | Hybrid: published transcript → local Whisper → Spotify description |
| Detection | Followed shows only; episode `resume_point` (fully played or ≥50%) |
| Trigger | Manual `/ingest-podcasts` command first; launchd schedule in phase 2 |
| Languages | Hebrew + English sources; wiki written in English |
| Primary page type | Concept pages; takeaways as secondary layer |
| Topic organization | Flat concepts + emergent hub pages (created at ~5 concepts per domain) |

### Assumptions

- User has Spotify Premium (required to create a Spotify developer app).
- Apple Silicon Mac (for `mlx-whisper`).
- Plain local markdown files; no database. Viewable in Obsidian or any editor.

## Repository layout

```
knowledgebase/
  CLAUDE.md                          # wiki schema + ingest rules
  raw/<show-slug>/<YYYY-MM-DD>-<episode-slug>.md   # immutable source text
  wiki/
    index.md
    log.md
    concepts/<slug>.md
    hubs/<domain>.md
    episodes/<show-slug>--<episode-slug>.md
    people/<slug>.md
    shows/<slug>.md
    takeaways/to-try.md
    takeaways/recommendations.md
  tools/
    spotify_mcp.py
    fetch_transcript.py
  .claude/commands/ingest-podcasts.md
  .mcp.json                          # registers spotify_mcp.py
```

## Components

### 1. `tools/spotify_mcp.py` — Spotify MCP server

A minimal MCP server (Python, FastMCP + spotipy) exposing one tool:

- `list_heard_episodes(min_progress: float = 0.5) -> list[Episode]`
  - Fetches followed shows (`GET /me/shows`), then each show's recent episodes (`GET /shows/{id}/episodes`), which include `resume_point`.
  - Returns episodes where `resume_point.fully_played` is true, or `resume_position_ms / duration_ms >= min_progress`.
  - Each `Episode`: `id`, `show_name`, `show_id`, `title`, `release_date`, `description`, `duration_ms`, `progress`, `spotify_url`, `language`.
- Auth: Spotify OAuth (Authorization Code) via spotipy with scopes `user-library-read user-read-playback-position`; token cached locally in `.spotify_cache` (gitignored). Client ID/secret from env vars `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, redirect `http://127.0.0.1:8888/callback`.
- Per-show episode lookup limited to the 20 most recent episodes (heard back-catalog beyond that is out of scope).

During planning, check whether an existing community Spotify MCP already returns `resume_point`; if one does, use it instead of writing this file.

### 2. `tools/fetch_transcript.py` — episode → raw file

CLI: `fetch_transcript.py <episode-json>` (the Episode object from the MCP). Writes one file to `raw/` and prints its path.

Fallback chain:

1. **Find RSS feed:** iTunes Search API (`https://itunes.apple.com/search?media=podcast&term=<show_name>`) → `feedUrl`. Match the episode in the feed by normalized title (case/punctuation-insensitive), with release date (±2 days) as tiebreaker.
2. **Published transcript:** if the feed item has `<podcast:transcript>` (VTT/SRT/text/HTML), download and convert to plain text. `source: transcript`.
3. **Whisper:** download the item's `<enclosure>` MP3 to a temp dir, transcribe with `mlx-whisper` model `large-v3` (auto language detection), delete the audio. `source: whisper`.
4. **Description:** if no feed/episode match or transcription fails, use the Spotify description. `source: description`.

Raw file format:

```markdown
---
spotify_id: ...
show: ...
title: ...
release_date: YYYY-MM-DD
spotify_url: ...
language: he|en
source: transcript|whisper|description
fetched: YYYY-MM-DD
---
<full text>
```

The existence of a raw file for a `spotify_id` is the "already ingested" record. No separate state store.

### 3. `.claude/commands/ingest-podcasts.md` — the ingest command

Instructions for Claude:

1. Call `list_heard_episodes`.
2. Drop episodes whose `spotify_id` already appears in a `raw/` file's frontmatter (grep).
3. For each remaining episode, run `fetch_transcript.py`. On failure, append the error to `wiki/log.md` and continue.
4. For each newly written raw file, update the wiki following `CLAUDE.md` rules.
5. Print a summary: episodes ingested, sources used, concept pages created/updated.

### 4. `CLAUDE.md` — wiki schema and rules

Contains the page templates and ingest rules below.

## Wiki design

### Page types

- **Concept** (`concepts/`) — primary. Synthesized understanding of one topic across all episodes.
- **Hub** (`hubs/`) — a domain (e.g. health, investing). Lists its concepts with one-line descriptions and a short domain overview.
- **Episode** (`episodes/`) — short source note.
- **Person** (`people/`) — lightweight: who they are, which episodes, linked concepts.
- **Show** (`shows/`) — show description + list of ingested episodes.
- **Takeaways** — `takeaways/to-try.md` (checklist) and `takeaways/recommendations.md` (books/tools/people, grouped by type).
- **index.md** — every page, one line each, grouped by hub (ungrouped concepts under "Unsorted").
- **log.md** — append-only; one entry per ingest: date, episode, source type, pages created/updated, errors.

### Concept page template

```markdown
---
type: concept
hubs: [health]
sources: 4
updated: YYYY-MM-DD
---
# Zone 2 Training

**Summary:** 3–5 sentence synthesis.

## Key ideas
- Claim … ([[episodes/huberman--endurance]], [[people/peter-attia]])

## Disagreements & open questions
- Attia says 3–4h/week; Galpin argues 2h is enough … (sources)

## Takeaways
- [ ] Try 4×45min zone-2 sessions/week

## Related
[[concepts/vo2-max]] · [[concepts/mitochondria]]
```

### Episode page template

```markdown
---
type: episode
show: ...
date: YYYY-MM-DD
guests: [[[people/...]]]
spotify_url: ...
source: transcript|whisper|description
raw: raw/<show>/<file>.md
---
# <Episode title>

5-line summary.

**Concepts:** [[concepts/a]] · [[concepts/b]]
```

### Ingest rules

1. Extract 3–10 concepts per episode. Before creating a concept page, check `index.md` and grep `concepts/` for an existing page that fits; prefer extending existing pages over near-duplicates.
2. When a concept page gains material, **rewrite** its Summary to integrate it (don't append). Add new claims to Key ideas.
3. Conflicting claims go under "Disagreements & open questions" with both sources; never silently overwrite an existing claim.
4. Every claim links its episode, and the person who made it when identifiable.
5. Actionable items go to the concept page's Takeaways section **and** `takeaways/to-try.md` (linking concept + episode). Books/tools/people recommended go to `takeaways/recommendations.md`.
6. Assign each concept 1–2 hub domains in frontmatter. When a domain reaches ~5 concepts and has no hub page, create it; otherwise update the existing hub's list.
7. Create/update episode, show, and person pages; update `index.md`; append to `log.md`.
8. Write everything in English; translate Hebrew sources during synthesis. Keep proper names in their common English spelling.
9. Episodes with `source: description` are flagged in the log and episode page as thin; extract fewer concepts (1–3) from them.
10. Links use Obsidian-style `[[folder/slug]]` wikilinks; slugs are lowercase-kebab-case English.

## Error handling

- Per-episode failures (feed not found, download/transcription error) degrade down the fallback chain; only a total failure skips the episode.
- A skipped episode writes no raw file, so the next run retries it automatically.
- Spotify auth failure aborts the run with a clear message (re-run OAuth).

## Testing

- `fetch_transcript.py` includes an `assert`-based self-check (`python fetch_transcript.py --selftest`) for the episode-matching logic: title normalization, date tiebreak, no-match case.
- End-to-end: one real `/ingest-podcasts` run against the user's account, verified by inspecting raw files and wiki pages.

## Phase 2 — scheduling

A launchd agent (`~/Library/LaunchAgents/com.user.podcast-wiki.plist`) runs every 6 hours:
`claude -p "/ingest-podcasts" --allowedTools <MCP tool, Bash(python tools/fetch_transcript.py:*), Read, Write, Edit, Grep>` with working directory set to the repo. Logs to `~/Library/Logs/podcast-wiki.log`. The Mac must be on.

## Out of scope

- Search/embeddings/UI (use Obsidian or grep; revisit when `index.md` stops being enough).
- `/lint` command for orphans/duplicates (add when the wiki drifts).
- Non-followed shows / "currently playing" polling.
- Episodes beyond the 20 most recent per show.
