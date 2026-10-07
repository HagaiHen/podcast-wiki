---
type: concept
hubs: [ai-engineering]
sources: 6
updated: 2026-10-07
---
# Open-Weight Models

**Summary:** Open-weight models, notably Chinese ones like GLM, Kimi, and Qwen, trail the frontier by roughly six months at a fraction of the price, pushing proprietary providers to cut prices. Enterprise fear has faded since weights can run inside trusted clouds or your own VPC. They win where you need real fine-tuning or LoRA on domain data, privacy (local subtasks routed from a main agent), or edge deployment. "Open" varies (weights only vs data and recipes too). Self-hosting isn't automatically cheaper than a cheap hosted model. Choose use cases carefully: conversational answers can reflect different training values.

## Key ideas
- Chinese models (GLM, Kimi) "give a phenomenal fight"; proprietary prices are starting to drop ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]).
- Banks once panicked at anything Chinese; now they're open to it because open weights aren't executable code ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Remaining reluctance is either not enough cost pain or unreasonable fear (e.g. political) ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Treat any model, Chinese or not, with the same care: assume it can act wrongly, as security teams assume of humans ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- monday.com doesn't call Chinese vendors' APIs; it runs models via sub-processors (AWS, Google, NVIDIA) under existing security and data-residency contracts, inside its VPC ([[episodes/ai-engineering-podcast--ai-infra-at-scale]], [[people/dor-cohen]]).
- Use-case fit: coding output is largely value-neutral; conversation differs (e.g. answers about Taiwan) ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- US enterprise customers may not want Chinese models, so model choice must stay with the customer, with transparency ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- "Open" varies: NVIDIA Nemotron released weights, training data, and SFT data, which made continued pre-training reproducible. Licenses ruled out some candidates (commercial use) ([[episodes/explainable--157-training-hebatron]]).
- Prediction: within 6–12 months more enterprises will fine-tune open-weight models on their own agents' failure cases ("shift left" into the weights), especially where data is rare (cyber, medical, drug research) ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- Bria ships its image foundation models with weights, so enterprises can keep training on proprietary data, run on-prem at a capped license cost, and avoid generic outputs ([[episodes/hidden-layers--bria-misha-feinstein]], [[people/misha-feinstein]]).
- Open models trail the frontier by roughly six months (with Chinese labs leading open benchmarks); you pick the model size yourself, unlike closed products with routers and system prompts. Kimi K2.5 comes close to Claude Code for coding ([[episodes/hidden-layers--nexar-roni-goldshmidt]], [[people/roni-goldshmidt]]).
- Local isn't automatically cheaper: in Nexar's video-classification benchmark, Gemini Flash beat a strong Qwen *and* cost less than the A100 hour needed to host it ([[episodes/hidden-layers--nexar-roni-goldshmidt]], [[people/roni-goldshmidt]]).
- Where open wins: real fine-tuning or LoRA on domain data (closed-model tuning barely changes behavior), privacy-sensitive subtasks routed from a main agent via a skill, and possibly future personal agents fine-tuned per user and run locally ([[episodes/hidden-layers--nexar-roni-goldshmidt]], [[people/roni-goldshmidt]]).

## Disagreements & open questions

## Takeaways
- [ ] Benchmark an open-weight model (e.g. GLM, Kimi, Qwen) on your workload for cost savings ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Route privacy-sensitive subtasks (e.g. bank statements) to a local open model from your main agent via a skill ([[episodes/hidden-layers--nexar-roni-goldshmidt]])

## Related
[[concepts/model-selection]] · [[concepts/llm-inference]] · [[concepts/ai-guardrails]] · [[concepts/ai-gateway]] · [[concepts/hebrew-llms]]
