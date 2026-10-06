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

Tools: `uv run tools/fetch_transcript.py --pending` lists raw files not yet in the wiki. `/ingest-podcasts` runs the whole pipeline.

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
