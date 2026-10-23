---
type: concept
hubs: [ai-engineering]
sources: 10
updated: 2026-10-23
---
# Open-Weight Models

**Summary:** Open-weight models, notably Chinese ones like GLM, Kimi, and Qwen, trail the frontier by a gap estimated at four to six months and shrinking, at a fraction of the price, pushing proprietary providers to cut prices. Enterprise fear has faded since weights can run inside trusted clouds or your own VPC; monday already routes ~10% of its internal traffic to untuned open models via Bedrock, starting internally and keeping them opt-in for customers, though worries about Chinese backdoors and malicious generated code persist, and one view is that frontier labs amplify that fear to win regulation. NVIDIA's Nemotron is a non-Chinese alternative. A GPU-cloud view sums up three reasons companies move from closed frontier APIs to open models they deploy themselves: cost, model-level differentiation (if everyone calls the same Anthropic model, only your own data-tuned model sets you apart), and sovereignty over data and region. They win where you need real fine-tuning or LoRA on domain data, privacy (local subtasks routed from a main agent), or edge deployment. "Open" varies (weights only vs data and recipes too). Self-hosting isn't automatically cheaper than a cheap hosted model. They are also the basis of "sovereign AI": governments running adapted open models in their own isolated data centers. Choose use cases carefully: conversational answers can reflect different training values.

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
- Open-weight models now reach frontier size: Kimi at ~1T parameters, DeepSeek V3/V3.2 at ~670B, and DeepSeek V4 at reportedly ~1.4T with notable architectural changes. At that size you have to split them across GPUs ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Sovereign AI for defense: build national data centers, install open-source models, and adapt them under your own control, isolated from the internet. Open source is ~6 months behind the frontier, "good enough for 99% of use cases" ([[episodes/micha-stocks--naftali-bennett-economic-interview]], [[people/naftali-bennett]]).

- Three reasons companies move from proprietary frontier models to self-deployed open ones: cost; differentiation at the model level, since with closed APIs you can't fine-tune or post-train and "the whole world uses the same model"; and sovereignty, both regional (European and UAE firms reluctant to send data to US servers) and control over what happens to the data ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Common pattern: keep your stack on AWS, and deploy your own open model on GPU infrastructure in the same region instead of sending inference calls to Anthropic ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Differentiation requires maturity: startups start on closed APIs, but once a company collects its own data it can tune an open model to its needs ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- ~10% of monday's internal traffic already goes to open-source models with good results, generic and not fine-tuned (though they could be); Chinese models and NVIDIA's Nemotron do well on its internal benchmark ([[episodes/ai-engineering-podcast--choosing-the-right-model]], [[people/keren-kushman]]).
- Safe adoption path: consume them through a known provider (AWS Bedrock, not the Chinese vendor directly), start with internal use, and make customer use opt-in after security and legal review. If worried, use Nemotron or keep them to tasks without customer or business data ([[episodes/ai-engineering-podcast--choosing-the-right-model]], [[people/keren-kushman]]).
- How they got so good is debated; there are many suspicions they copy (distill) frontier models ([[episodes/ai-engineering-podcast--choosing-the-right-model]]).

## Disagreements & open questions
- Are open weights safe? Sharon Dahan argues weights aren't executable code, so the old panic is misplaced ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]); Keren Kushman cites fears of backdoors in Chinese weights that leak data, and a host worries such a model could write code that runs through a local coding agent while nobody reviews every PR. Kushman also thinks frontier labs sow these fears to win regulation ([[episodes/ai-engineering-podcast--choosing-the-right-model]], [[people/keren-kushman]]).
- How far behind is open source? Earlier guests put it at ~6 months ([[episodes/hidden-layers--nexar-roni-goldshmidt]], [[episodes/micha-stocks--naftali-bennett-economic-interview]]); a Nebius guest says estimates fell from a year to seven months to ~four months recently ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).

## Takeaways
- [ ] Benchmark an open-weight model (e.g. GLM, Kimi, Qwen) on your workload for cost savings ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Route privacy-sensitive subtasks (e.g. bank statements) to a local open model from your main agent via a skill ([[episodes/hidden-layers--nexar-roni-goldshmidt]])
- [ ] Introduce open models through a trusted provider, internal traffic first, opt-in for customers ([[episodes/ai-engineering-podcast--choosing-the-right-model]])

## Related
[[concepts/model-selection]] · [[concepts/llm-inference]] · [[concepts/ai-guardrails]] · [[concepts/ai-gateway]] · [[concepts/hebrew-llms]] · [[concepts/neoclouds]]
