---
type: episode
show: Osim Tochna (עושים תוכנה)
date: 2025-11-03
guests: ["[[people/ohad-parush]]"]
spotify_url: https://open.spotify.com/episode/1ose26CGIIVVaayyMMe6HU
source: whisper
raw: raw/osim-tochna/2025-11-03-gong-ai-for-developers.md
---
# Gong Rolls Out AI for Developers

[[people/amit-bendor]] talks with [[people/ohad-parush]], Chief R&D Officer at Gong, about deliberately embedding AI into development.
Copilot drew lukewarm reactions ("autocomplete on steroids"); Claude Code was the revolution, run in a Docker container per Anthropic's security guidance, with no token or session caps.
Practices: the Developer Experience (DX) team owns AI adoption (environments, manifests, practices); mandatory AI review prompts on every PR, always with a human override ("AI for Quality"); hands-on training on developers' own code; and a top-down mandate on one new product where an all-senior team had to use Claude Code, and got hooked.
Results: unfamiliar tech (Apache Iceberg, WebSockets) in two days instead of two months; tests first, so TDD gets a revival; design docs synced back to Confluence from code. Gong still hires aggressively: "200 developers with the impact of 300."
New role "DS2" (data scientist 2.0): prompt templates (machines write the prompts), evals, judges, gold sets, and continuous calibration (CI/CC/CD). Token usage as a metric is interesting but shallow.

**Show:** [[shows/osim-tochna]]

**Concepts:** [[concepts/ai-rd-rollout]] · [[concepts/ai-engineering-metrics]] · [[concepts/test-driven-development]] · [[concepts/llm-evals]] · [[concepts/ai-verification]] · [[concepts/future-of-software-engineering]]
