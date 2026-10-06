---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# Open-Weight Models

**Summary:** Open-weight models, notably Chinese ones like GLM, Kimi, and Qwen, now compete strongly at a fraction of the price (estimates range from ~20–30% cheaper to a fifth or tenth of the cost; GLM 5.2 is said to approach Opus), pushing proprietary providers to cut prices. Enterprise fear has faded since open weights are not code and can run inside trusted clouds (AWS, Google, NVIDIA) in your own VPC rather than via Chinese APIs. Choose use cases carefully: fine for coding, but conversational answers can reflect different training values. Give customers transparency and the choice to opt in.

## Key ideas
- Chinese models (GLM, Kimi) "give a phenomenal fight"; proprietary prices are starting to drop ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]).
- Banks once panicked at anything Chinese; now they're open to it because open weights aren't executable code ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Remaining reluctance is either not enough cost pain or unreasonable fear (e.g. political) ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Treat any model, Chinese or not, with the same care: assume it can act wrongly, as security teams assume of humans ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- monday.com doesn't call Chinese vendors' APIs; it runs models via sub-processors (AWS, Google, NVIDIA) under existing security and data-residency contracts, inside its VPC ([[episodes/ai-engineering-podcast--ai-infra-at-scale]], [[people/dor-cohen]]).
- Use-case fit: coding output is largely value-neutral; conversation differs (e.g. answers about Taiwan) ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- US enterprise customers may not want Chinese models, so model choice must stay with the customer, with transparency ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).

## Disagreements & open questions

## Takeaways
- [ ] Benchmark an open-weight model (e.g. GLM, Kimi, Qwen) on your workload for cost savings ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/model-selection]] · [[concepts/llm-inference]] · [[concepts/ai-guardrails]] · [[concepts/ai-gateway]]
