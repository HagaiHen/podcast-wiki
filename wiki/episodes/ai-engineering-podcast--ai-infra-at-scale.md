---
type: episode
show: AI Engineering (AI אנג׳נירינג)
date: 2026-08-17
guests: ["[[people/dor-cohen]]"]
spotify_url: https://open.spotify.com/episode/66gS88BZmsw3oI49hpOr3m
source: whisper
raw: raw/ai/2026-08-17-ai-infra-at-scale.md
---
# AI Infra at Scale — with Dor Cohen (monday.com)

[[people/dor-cohen]], who leads AI infrastructure at monday.com (tens of thousands of customer agents), explains why API keys in code break at scale. An experimental lab product once burned $50k in a day.
The AI gateway routes traffic across models and vendors, meters and limits cost per feature and customer, strips PII, and blocks prompt injection and policy abuse, all invisibly.
Evals come in two kinds: offline (curated datasets in CI, code checks plus LLM-as-judge) and online (scoring production sessions continuously), with models A/B tested by gradual rollout.
Cost levers: prompt caching (stable prefix first), concise structured outputs, and planning with a strong model while executing with a cheaper one. Chinese open-weight models run via AWS/Google with customer opt-in.
Takeaways: use a gateway, treat prompts like code, and never lock into one vendor.

**Show:** [[shows/ai-engineering-podcast]]

**Concepts:** [[concepts/ai-gateway]] · [[concepts/llm-evals]] · [[concepts/llm-cost-optimization]] · [[concepts/model-selection]] · [[concepts/open-weight-models]] · [[concepts/ai-guardrails]]
