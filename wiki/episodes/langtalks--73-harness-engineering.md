---
type: episode
show: LangTalks
date: 2026-09-15
guests: []
spotify_url: https://open.spotify.com/episode/24OoSYQv8SmkY6YjQNho87
source: whisper
raw: raw/langtalks/2026-09-15-73-harness-engineering.md
---
# #73 — Harness Engineering

> Transcript gap: Whisper got stuck in a repetition loop mid-episode (around tracing/observability), and part of the discussion is missing.

The hosts explain harness engineering: making coding agents run autonomously for 40–50 minutes, writing, testing, and proving code production-ready, by giving them the right environment, signals, and enforced guardrails.
OpenAI's case: a repo started in August 2025 by three engineers grew past a million lines in months, with productivity *rising* as the team grew, because instead of telling the agent to "try harder" they asked what capability it was missing and built it into the enforced flow.
Practical recipe: product docs as files in the repo, skills that say when to update themselves, git hooks enforcing 80% test coverage, TDD so agents can't cheat, agent-launchable isolated environments, and alignment in three steps (spec → plan → proof of work, e.g. a Playwright video of the feature working).
Closing take: harness gains compound; measure productivity per token over time.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/harness-engineering]] · [[concepts/agent-ready-codebase]] · [[concepts/test-driven-development]] · [[concepts/ai-verification]] · [[concepts/ai-guardrails]] · [[concepts/context-engineering]]
