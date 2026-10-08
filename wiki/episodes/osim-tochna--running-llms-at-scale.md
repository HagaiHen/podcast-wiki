---
type: episode
show: Osim Tochna (עושים תוכנה)
date: 2026-05-18
guests: ["[[people/mike-erlihson]]", "[[people/kfir-schneider]]"]
spotify_url: https://open.spotify.com/episode/5Aa8rBfo18NePbniYs685D
source: whisper
raw: raw/osim-tochna/2026-05-18-running-llms-at-scale.md
---
# How Do You Really Run LLMs at Huge Scale?

[[people/amit-bendor]] talks with [[people/mike-erlihson]] (math PhD, ExplAInable co-host, 600+ paper reviews, now optimizing LLM inference on AMD GPUs) about what happens behind every API call.
Splitting 1T+ parameter open models (Kimi, DeepSeek) across GPUs and machines; why GPU memory is reserved for the KV cache, which can reach terabytes and is managed across GPU, DRAM and SSD and shared across users for common prefixes.
Mixture of experts (~256 experts, ~8 active per token), hybrid Mamba/transformer models, continuous batching (~5× over hand-rolled), and the framework stack (vLLM, SGLang, Mooncake, LMCache, llm-d). The goal: minimum $/1M tokens within a latency SLA.
Mike expects subsidized subscriptions to get much pricier, sees inference optimization as a durable job, and urges listeners to "dream big" since coding is now a commodity.
Sponsor segment: [[people/kfir-schneider]] (Riskified) on steering Karpenter's spot/on-demand mix by commitment utilization, saving 30–40% on Kubernetes.

**Show:** [[shows/osim-tochna]]

**Concepts:** [[concepts/llm-inference]] · [[concepts/ai-infrastructure]] · [[concepts/open-weight-models]] · [[concepts/llm-cost-optimization]] · [[concepts/future-of-software-engineering]]
