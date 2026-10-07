---
type: episode
show: Startup for Startup
date: 2026-06-09
guests: []
spotify_url: https://open.spotify.com/episode/4sDL5aKls9Y2BYd36jC8vM
source: whisper
raw: raw/startup-for-startup/2026-06-09-353.md
---
# #353 — How We Built a Self-Updating "Team Brain"

> Guest named Sar in the transcript (software engineering group lead at monday.com); surname unclear. Host: Roni.

The team building Harmony, a new go-to-market product at monday.com (the same team that built monday's AI note-taker), wanted to capture early "shadow data": meetings, Slack, WhatsApp, late-night architecture debates, and hallway talks.
v1 was one person's n8n flow updating three files (decisions, action items, open questions). The files bloated and hallucinated, and per-person workflows wouldn't scale to 20 people.
After Karpathy's LLM Wiki post, they built a persistent, interlinked wiki in a git repo: concepts, domains, entities (companies and roles), decisions, action items. A Claude skill on each person's machine runs every ~30 minutes, pulls new data through their personal MCPs (note-taker, Slack, WhatsApp, docs), skips already-ingested raw items, updates many pages per meeting, and pushes. Answers worth keeping get saved back.
Access: a Wikipedia-style site, and a WhatsApp agent ("Siena", on OpenClaw) that answers anyone 24/7.
Impact: an executive vision deck in hours instead of weeks, Google Ads messaging written from the brain with good leads, and cross-team alignment without syncs. Next: autonomous discipline agents built on the brain.
Costs: private conversations leaked into git history (repo wiped more than once), and nothing is private anymore. Advice: start simple and local before automating at scale.

**Show:** [[shows/startup-for-startup]]

**Concepts:** [[concepts/company-brain]] · [[concepts/llm-wiki]] · [[concepts/ai-guardrails]]
