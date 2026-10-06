---
type: episode
show: LangTalks
date: 2026-03-08
guests: ["[[people/liad-elidan]]"]
spotify_url: https://open.spotify.com/episode/78OR0ST5r2DrNtYBerul5p
source: whisper
raw: raw/langtalks/2026-03-08-64-ai-coding-metrics-liad-elidan-milestone.md
---
# #64 — AI Coding Metrics — with Liad Elidan (Milestone)

[[people/liad-elidan]] (CEO of Milestone, engineering productivity) explains how to measure whether coding agents actually help.
Pre-GenAI productivity relied on *metadata* (PR cycle, coding, and review time; DORA metrics), which ignored context and complexity. GenAI made the *data* itself readable: code lines, git blame, ticket content, and agent events from Copilot, Cursor, and Claude Code. That makes attribution possible: which commit or PR used which tool.
Milestone's framework has three layers. **Adoption** asks who uses which tools and features. **Productivity** compares cycle and review times with and without AI per developer. **Quality** measures code survival and longevity, tracing bugs back via git blame to whether the offending lines were AI-assisted.
Hosts add: separate usage from utilization, check whether buggy code was spec-driven and used the internal MCP, and give custom agents success baselines that improve per version.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/ai-engineering-metrics]] · [[concepts/ai-sdlc]] · [[concepts/llm-evals]] · [[concepts/ai-finops]]
