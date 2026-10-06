---
type: episode
show: ExplAInable
date: 2026-06-16
guests: []
spotify_url: https://open.spotify.com/episode/4usi3lrCnaKAD5yDYyOlPt
source: whisper
raw: raw/explainable/2026-06-16-157.md
---
# #157 — Cracking Hebrew: Behind the Scenes of Training Hebatron

> Guest names were unclear in the transcript: the AI development lead at PwC Next (Sar) and the team member who led evaluation and data collection (Noam). Host: Mike.

Hebatron is an open Hebrew LLM built by PwC Next with Israel's national AI program, on AWS compute, via continued pre-training of NVIDIA's Nemotron (a Mamba mixture-of-experts model). It hit ~30k downloads and four community quantizations in its first week.
Hebrew is morphologically rich: prefixes fuse into words, which strains BPE tokenization. Tokenizer compression ratio was the key base-model criterion (~2.5 tokens per word vs ~5 for Granite or Llama).
Instruct-tuned bases with heavily engineered post-training (Cohere's Aya, Command R) wouldn't improve. Fully open Nemotron (data and recipes released) did. Lesson: pick the most *trainable* base, not the strongest on benchmarks.
In ~200 experiments, falling train and validation loss never predicted benchmark gains, and benchmarks didn't predict arena preference. The breakthrough came from raising the batch size to ~16.5M tokens and scaling the learning rate by √(batch). Data *order*, not just mix, changed results.
Infra: AWS HyperPod with 64 GPUs. Moving from DeepSpeed to NVIDIA NeMo/Megatron Bridge halved cost, and H200 → B300 was ~7× faster at 2× the price. A full continued pre-training (CPT) run fell from a projected ~$200k to tens of thousands of dollars.

**Show:** [[shows/explainable]]

**Concepts:** [[concepts/hebrew-llms]] · [[concepts/llm-pretraining]] · [[concepts/llm-evals]] · [[concepts/open-weight-models]]
