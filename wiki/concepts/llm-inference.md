---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# LLM Inference

**Summary:** Training is expensive, but inference (actually serving models) is where most cost now lives. A model's memory need is roughly parameters × bits per parameter (quantization). Large models are split across GPUs (tensor parallelism), small ones are replicated to fill a server (data parallelism), mixture-of-experts models spread experts across GPUs, and every GPU reserves room for the KV cache. Price per token comes down to utilization: a busy GPU is cheap per token, an idle one loses money.

## Key ideas
- "120B", "30B" means parameter count; × quantization (4- or 8-bit) gives the memory required ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]).
- Tensor parallelism slices the model ("the loaf of bread") across GPUs that must communicate; that's why bigger models cost more: more hardware, more compute time ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Data parallelism: if the model fits one GPU, replicate it across the server's 8 GPUs ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Mixture-of-experts (e.g. "350B, 20B active"): only some experts fire per token; experts can be distributed and even swapped at runtime to maximize utilization ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- The KV cache stores attention computations; a high hit rate frees GPUs to do more work. Cache efficiency changes price by orders of magnitude ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- "A taxi that isn't driving loses money": keep GPUs busy and price per million tokens drops ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Generic APIs price for everyone, are optimized for time-to-first-token, and carry big margins. Latency-insensitive (async/batch) workloads tailored to the use case can cost ~20–30% of that ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- GPU supply is ~20% of real demand (claim attributed to an NVIDIA conference) ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).

## Disagreements & open questions

## Takeaways
- [ ] For latency-insensitive bulk workloads, use batch/async inference rather than real-time APIs ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/model-selection]] · [[concepts/open-weight-models]] · [[concepts/ai-infrastructure]] · [[concepts/llm-cost-optimization]]
