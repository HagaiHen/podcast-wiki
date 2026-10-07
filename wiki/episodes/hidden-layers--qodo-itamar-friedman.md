---
type: episode
show: Hidden Layers
date: 2026-03-31
guests: ["[[people/itamar-friedman]]"]
spotify_url: https://open.spotify.com/episode/3RvGgsQ8VbKorXXOVcE7Wa
source: whisper
raw: raw/hidden-layers/2026-03-31-qodo.md
---
# How Do You Review AI-Written Code? — with Itamar Friedman (Qodo)

[[people/uri-eliabayev]] talks with [[people/itamar-friedman]], co-founder and CEO of Qodo ("quality of code"), a multi-agent system for code review and code governance.
Simple greenfield apps are now one prompt away, but for complex software, more AI code also means more production bugs and less understanding, so leading companies put AI across the whole SDLC, not just generation.
Generation and review have opposite incentives: coding agents are rewarded for finishing and pleasing, while review must stop you and explore every case. Like hardware verification (Friedman's start at Mellanox, using ML 20 years ago), a reviewer needs a "criminal mind", systematically checking setups such as accessibility across resolutions. More context or thinking can hurt; for workflows, a smaller budget per node is often better.
"Code quality" splits into categories (intent, architecture, maintainability, testability, compliance), much of it measurable once tribal knowledge is digitized into rules and skills mined from PR history and Slack. He predicts reviews reaching about level 3.9 of autonomy by end of 2026.
Anthropic's launch of its own code review validated paying more for review (5–25 each), but he calls its results underwhelming and argues for an independent reviewer, as with observability and security on AWS.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/ai-verification]] · [[concepts/agent-ready-codebase]] · [[concepts/model-selection]] · [[concepts/ai-sdlc]]
