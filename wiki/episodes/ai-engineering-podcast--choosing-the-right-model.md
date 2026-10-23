---
type: episode
show: AI Engineering (AI אנג׳נירינג)
date: 2026-10-22
guests: ["[[people/keren-kushman]]"]
spotify_url: https://open.spotify.com/episode/0OYm15HIzzPibbGxmsfZa9
source: whisper
raw: raw/ai/2026-10-22-0OYm15HIzzPibbGxmsfZa9.md
---
# How Do You Choose the Right Model? — with Keren Kushman (monday.com)

[[people/keren-kushman]], Head of Applied AI at monday.com, describes MondayBench: a private benchmark of ~20 golden-set prompts built from real company requests, run against raw model APIs (no harness) and scored by a three-lab judge panel, because models favor their own family.
Key lessons: compare cost per completed task, not per token; raising a cheap model's effort level doesn't make it smarter; knowledge work no longer needs frontier models, but hard engineering does.
monday routes by intent with a small model and picks once per session to keep prompt caching intact, and already sends ~10% of internal traffic to open models via Bedrock.
After a Silicon Valley trip she relays Anthropic's prediction that the harness will move into the model: "build harnesses, don't fall in love with them", and keep investing in context and memory.
Also: use automation, not AI, for deterministic processes; a "be positive" budget-approval agent that approved everything; and FinOps advice (attribution down to agent and person, then your own evals).

**Show:** [[shows/ai-engineering-podcast]]

**Concepts:** [[concepts/model-selection]] · [[concepts/llm-evals]] · [[concepts/harness-engineering]] · [[concepts/llm-cost-optimization]] · [[concepts/ai-gateway]] · [[concepts/open-weight-models]] · [[concepts/workflow-automation]] · [[concepts/ai-guardrails]]
