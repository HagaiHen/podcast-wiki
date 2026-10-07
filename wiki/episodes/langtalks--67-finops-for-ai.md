---
type: episode
show: LangTalks
date: 2026-04-27
guests: ["[[people/yizhar-gilboa]]"]
spotify_url: https://open.spotify.com/episode/0YbHVJv5QRtXOh3wf3kOjc
source: whisper
raw: raw/langtalks/2026-04-27-67-finops-for-ai-yizhar-gilboa-finout.md
---
# #67 — FinOps for AI — with Yizhar Gilboa (Finout)

[[people/yizhar-gilboa]] (co-founder and CTO of Finout) explains how to attribute and manage AI spend now that budgets aren't unlimited.
The hard part is attribution: cloud bills (e.g. Bedrock) don't say which of your 50 systems made a call. It evolved from per-model inference profiles to tagging every call at a gateway and logging rich telemetry. Full unit economics joins AI token cost with each system's databases and storage.
Benchmarks for coding-agent spend per developer: ~65% of companies at $100–300/month, ~30% at $300–600, ~5% under $100. It must never be zero. Analyze heavy spenders' sessions for infrastructure savings (e.g. better docs to cut costly code exploration) and practices worth spreading. AI in production costs far more than AI for coding.
Optimization ideas: prompt and trace compression, slimmer tool responses (e.g. JSON → YAML, dropped headers). The hosts predict the per-developer spend ceiling will fall away as money becomes tokens, then intelligence.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/llm-cost-optimization]] · [[concepts/ai-gateway]]
