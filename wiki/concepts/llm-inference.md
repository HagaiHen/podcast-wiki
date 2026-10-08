---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-07
---
# LLM Inference

**Summary:** Training is expensive, but inference (actually serving models) is where most cost now lives, and where most companies work: few train, everyone serves. A model's memory need is roughly parameters × bits per parameter. Frontier open models now reach 1T+ parameters, so they're split across GPUs and even across 8-GPU machines (tensor parallelism), small ones are replicated (data parallelism), and mixture-of-experts models route each token to a few experts that must be placed across GPUs. The KV cache, which trades memory for recomputation, can reach terabytes with long contexts and many users, so it's managed in a hierarchy (GPU → host DRAM → SSD) and shared across users for common prefixes like system prompts. The job reduces to one number: minimize $ per million tokens while meeting a latency SLA (e.g. time to first token). Price comes down to utilization, and a rich, fast-growing framework stack (vLLM, SGLang, Mooncake, LMCache, llm-d) is itself an optimization dimension.

## Key ideas
- "120B", "30B" means parameter count; × quantization (4- or 8-bit) gives the memory required ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]).
- Tensor parallelism slices the model ("the loaf of bread") across GPUs that must communicate; that's why bigger models cost more: more hardware, more compute time ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Data parallelism: if the model fits one GPU, replicate it across the server's 8 GPUs ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Mixture-of-experts (e.g. "350B, 20B active"): only some experts fire per token; experts can be distributed and even swapped at runtime to maximize utilization ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- The KV cache stores attention computations; a high hit rate frees GPUs to do more work. Cache efficiency changes price by orders of magnitude ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- "A taxi that isn't driving loses money": keep GPUs busy and price per million tokens drops ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Generic APIs price for everyone, are optimized for time-to-first-token, and carry big margins. Latency-insensitive (async/batch) workloads tailored to the use case can cost ~20–30% of that ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- GPU supply is ~20% of real demand (claim attributed to an NVIDIA conference) ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Splitting a model across machines is a logic problem, not just engineering: you can shard by layers or within each layer, and the many ways to exchange partial results between machines (RDMA etc.) make finding the optimal plan non-trivial ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Memory per GPU sets the split: AMD's MI355 has 288 GB per GPU vs NVIDIA B200's 192 GB, so an 8-GPU machine holds ~2.3 TB vs ~1.5 TB. A ~3 TB model needs at least ~12 GPUs ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Why not fill GPU memory with weights alone? Serving many users at once needs room for each one's KV cache ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- KV cache = save computation at the expense of memory: partial attention results for earlier tokens are stored instead of recomputed for every new token. With contexts of hundreds of thousands of tokens it can reach terabytes ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- KV-cache hierarchy: an idle user's cache (gone for coffee) is moved from GPU memory to host DRAM, and to SSD if they stay away. Hundreds of papers cover compressing, chunking and transferring it ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Cross-user cache reuse: a popular agent's fixed system prompt should keep its KV cache close to the GPU so it's never recomputed, but GPU memory is limited across hundreds of agents, so it's a balancing act. Chunking the cache (e.g. LMCache) lets users reuse others' prefixes ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Mixture of experts in practice: a model may have ~256 experts but activate one always-on shared expert plus ~8 chosen per token by a learned router, using ~5% of parameters. Placing experts across machines interacts with the KV cache. Mistral popularized the architecture before today's 0.5T+ models all adopted it ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Hybrid architectures: Mamba/state-space layers mixed with transformer layers run faster and handle much longer contexts. AI21 was early (Jamba); IBM Granite, Qwen and MiniMax (linear attention) followed ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Continuous batching: hand-rolled batching ran ~5× slower than vLLM, whose continuous batching gave an immediate ~5× throughput gain ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Frameworks are an optimization axis too: vLLM, SGLang and AMD's ATOM for serving, Mooncake and LMCache for KV caching, llm-d for cluster-level scheduling (which users to admit). Pick per model type; the stack grows fast because vibe coding makes new ideas cheap to implement ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Where the headroom is: large models at huge scale still have lots of room. Small, popular models are already heavily tuned; an attempt to speed up an image diffusion model with Claude and Codex only made it slower ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Kernel work becomes accessible: someone who understands low-level GPU behavior can now use coding agents to tune AMD or NVIDIA kernels for a specific model, even selecting or generating kernels on the fly ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Learning path: understand transformers enough to see why a KV cache exists, then MoE, then systems concerns like scheduling, where backend engineers have an edge over algorithm people. Start by running small models locally (Ollama, then vLLM) and push on what's slow ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).

## Disagreements & open questions

## Takeaways
- [ ] For latency-insensitive bulk workloads, use batch/async inference rather than real-time APIs ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Learn inference by running a small model locally (Ollama, then vLLM) and comparing throughput with and without continuous batching ([[episodes/osim-tochna--running-llms-at-scale]])
- [ ] Keep fixed system prompts identical across requests so their KV cache can be shared and kept near the GPU ([[episodes/osim-tochna--running-llms-at-scale]])

## Related
[[concepts/model-selection]] · [[concepts/open-weight-models]] · [[concepts/ai-infrastructure]] · [[concepts/llm-cost-optimization]] · [[concepts/small-language-models]] · [[concepts/future-of-software-engineering]]
