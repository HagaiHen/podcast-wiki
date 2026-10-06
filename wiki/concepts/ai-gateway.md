---
type: concept
hubs: [ai-engineering]
sources: 3
updated: 2026-10-06
---
# AI Gateway

**Summary:** A central layer every product calls instead of holding vendor API keys. It routes each request to the right model and vendor (by availability, cost, limits, real-time vs async), meters and caps spend per feature and per customer, and adds security (PII stripping, prompt-injection defense, usage policies) plus trust features (audit logs, data residency). Good AI infra is the kind you don't notice. A key in code is fastest, until it breaks.

## Key ideas
- An experimental product in a monday.com lab environment burned **$50k in one day** through a loop, with no visibility. That's the case for a gateway ([[episodes/ai-engineering-podcast--ai-infra-at-scale]], [[people/dor-cohen]]).
- Dynamic routing: check each vendor's availability, cost, and limits; switch models or vendors (e.g. AWS, Google) transparently when one fails ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Metering and limits per feature, with alerts; per-customer token attribution for credits and limits ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Products state their needs (specific model, real-time vs async); if they don't choose, the gateway picks the best fit for the intent ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Real-time paths optimize for speed; async/batch paths (e.g. daily email summaries) can afford heavier security and cheaper processing ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Security layer: strip PII (emails, credit cards) before it reaches models or logs; use specialist vendors for prompt-injection defense rather than reinventing it ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Trust: audit logs, data residency (EU data stays in EU), retention. When a model required 30-day data retention, it became customer opt-in ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Avoid vendor lock-in: always have a tested plan B model or vendor ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Not magic: product teams still own knowing their prompts and detecting loops and abuse; the gateway supplies visibility ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Gateways are also the FinOps backbone: tagging calls and emitting telemetry is what makes accurate cost attribution possible ([[episodes/langtalks--67-finops-for-ai]]).
- An OpenAI-compatible internal API with a mandatory project field shows per-feature production cost; a raw cloud bill for "Sonnet on Bedrock" doesn't ([[episodes/langtalks--66-scaling-llmops]]).

## Disagreements & open questions

## Takeaways
- [ ] Route all LLM calls through a gateway with per-feature spend limits and alerts ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Strip PII before prompts leave your system ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Keep a pre-tested fallback model/vendor for every AI feature ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])

## Related
[[concepts/llm-evals]] · [[concepts/llm-cost-optimization]] · [[concepts/model-selection]] · [[concepts/ai-guardrails]] · [[concepts/ai-finops]]
