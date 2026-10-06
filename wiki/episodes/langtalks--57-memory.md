---
type: episode
show: LangTalks
date: 2025-11-16
guests: ["[[people/itamar-friedman]]"]
spotify_url: https://open.spotify.com/episode/1Sh3AM2v9CfmOodOk1qpXn
source: whisper
raw: raw/langtalks/2025-11-16-57-memory-itamar-friedman-qodo.md
---
# #57 — Memory — with Itamar Friedman (Qodo)

[[people/itamar-friedman]], CEO of Qodo (AI code review, quality, and testing, "the counterpart to vibe coding"), discusses memory for coding agents.
Short-term memory keeps a long session faithful to early requests; long-term memory is project, personal, and organizational knowledge. Rules in markdown files are fine, since natural language keeps memory controllable, but you need a framework: how memories are created, when they're retrieved, and whether they're *valuable*. Track rule usage and acceptance (e.g. used 100 times, accepted 80) and prune.
Ingestion design: between "encode everything into one format" and "only index references", ingest and encode per media type with references back to sources, give agents per-type memory tools, and add a router. Governance (whose feedback counts: junior, senior, an outlier senior?) is what's missing in tools.
Mem0 offers add, search, update, delete, plus multimodal, graph, expiry, and feedback, but not the intelligence. Merging parallel sessions needs their *intent*, not just their code. Future: nightly background consolidation (like sleep) plus backfilling history to avoid cold start; possibly learned memory architectures, despite the bitter lesson.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/agent-memory]] · [[concepts/memory-consolidation]] · [[concepts/human-vs-ai-memory]] · [[concepts/context-engineering]]
