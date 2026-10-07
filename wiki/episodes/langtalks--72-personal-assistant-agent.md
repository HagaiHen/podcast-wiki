---
type: episode
show: LangTalks
date: 2026-08-16
guests: []
spotify_url: https://open.spotify.com/episode/3OfxFANlEKTiiNmWiY9UQp
source: whisper
raw: raw/langtalks/2026-08-16-72-personal-assistant-agent.md
---
# #72 — Personal Assistant Agent

> Transcript note: one short passage (on the GitHub-issues MCP) came out garbled; the surrounding context is intact.

The hosts walk through a personal-assistant agent (an OpenClaw-style "claw") built around meetings. It tags calendar events by type, writes per-type morning briefings (with past action items and enrichment on external guests), records every meeting to Notion, writes templated summaries, files action items, drafts follow-up emails in the user's style, and learns nightly from the user's corrections.
They compare it with n8n/Zapier (deterministic and cheap, but unnatural to build) and Anthropic's dynamic workflows (converse first, then generate deterministic code).
Team pain points: agents acting under the user's identity flood shared tools with noise; skills shared by forking diverge; skills need versioning like libraries.
A self-healing loop: users' complaints become GitHub issues, an agent SDK proposes fixes, small ones auto-merge, and the user gets told to retry.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/personal-ai-assistants]] · [[concepts/skill-engineering]] · [[concepts/memory-consolidation]] · [[concepts/agent-workspaces]] · [[concepts/second-brain]]
