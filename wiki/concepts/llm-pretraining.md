---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# LLM Pre-training

**Summary:** Pre-training is the stage where a model compresses a massive, unlabeled, scraped dataset. Because the data can't fit perfectly into the weights, the model is forced to learn regularities (ideally "expected value", not memorized labels). Generalization sometimes appears suddenly (grokking), and no one knows exactly why. Much of the craft is unpublished folklore passed between labs by word of mouth. Small academic experiments rarely transfer to scale, so only organizations that have actually trained large models hold the know-how. Few in Israel do (AI21, Lightricks for diffusion, a few others).

## Key ideas
- Recipe: scrape the biggest dataset possible, pick a model size by a rough ratio (Chinchilla-style, ~1:20 tokens per parameter as a "good enough" rule of thumb), and train it to reproduce the data ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Grokking: models sometimes suddenly learn the general form of a problem; inducing it relies on heuristics and regularization tricks mostly absent from the literature ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- The transformer came from engineering pressure, not a theory of learning: RNNs weren't parallelizable, so researchers tried convolutions plus attention and ablated everything except attention, hence "Attention Is All You Need" ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Context-length curriculum: train at 16k first (8× shorter sequences, ~64× cheaper attention), then extend to 128k. The model may then fail at untrained lengths like 30k even with relative position encodings. Context windows seem stuck around 1M tokens ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Folklore: multi-head latent attention (low-rank shared embeddings saving ~90% compute) existed quietly before DeepSeek published it. If you don't know such tricks, you won't invent them ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Academic papers now test on 1–7B models without money for scale, so results are "vibe papers": recommendations, not validation. The best evaluation is whether users use it ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Storage and interconnect, not just GPUs, are major unspoken bottlenecks ([[episodes/explainable--164-gilad-levi-continual-learning]]).

## Disagreements & open questions
- Can transformers be understood from inside? Interpretability researchers (e.g. at Anthropic) try to localize facts in MLPs; Levi thinks the general problem is like predicting a three-body system: sub-problems yes, the whole no ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).

## Takeaways

## Related
[[concepts/continual-learning]] · [[concepts/llm-reasoning]] · [[concepts/small-language-models]] · [[concepts/open-weight-models]]
