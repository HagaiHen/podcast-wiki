---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-07
---
# Continual Learning

**Summary:** Today's LLMs are trained once on a frozen dataset and then shipped as a fixed point. Afterwards they "learn" only through the context window, like an employee who must reread a growing stack of notes every morning. Humans update continuously from sparse signals: one fact or one scare can change behavior for life. Continual learning aims at models that absorb a constantly changing world (enterprise data, conversations, facts that drift) into their weights, without catastrophic forgetting, and that memorize only what they need for planning while retrieving the rest. Frontier labs mostly don't pursue it: they're busy with benchmark fire-fighting, and it would need a huge bet on a new architecture.

## Key ideas
- Human learning runs on sparse, rare signals (a life-threatening situation, a PhD), yet people build around them for life; models need enormous data and can't learn from a few examples ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- The world changes subtly (a salary that was 40k is now 35k). Steering a pre-trained model in conversation fails: as the conversation goes on it drifts back to what's in its weights ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Fine-tuning gives you two points (the released weights and your tuned weights) with no idea what happened between them. Labs release weights without optimizer (Adam momentum) state, which makes careful continuation hard ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Memorization is a spectrum: you don't memorize page 140 of a book (retrieve it), but you memorize your room's layout perfectly, along with faces, songs, and how physical objects interact. Models should memorize what planning needs ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Industry split: ~85–90% only retrieve over a frozen model, ~9% fine-tune, ~1% do broad training on company data ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Why big labs don't do it: an arms race of fire-fighting (Gemini vs Anthropic vs OpenAI benchmarks). Continual learning needs a big architectural bet tested at scale and rolled out to every customer, which would cost competitiveness meanwhile ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Interpretability comes from engineering the system (e.g. a sniffer for when the model reads a database), not from opening the weights; whether a transformer's knowledge can be localized is likely unsolvable ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Manifold's framing: humans live one endless stream of experience, not millions of small contexts. They learn as *explorers* who act (drop a ball to learn physics), whereas LLMs are observers ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- No model learns as fast as a three-year-old, from either data volume or compute; robots can't tell when breaking a door is justified (a book behind it vs an EpiPen) ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).

## Disagreements & open questions
- Can a model update its weights continuously without forgetting? The host's intuition says fixing one thing breaks another; Levi argues it's solvable with the right definition of what to memorize ([[episodes/explainable--164-gilad-levi-continual-learning]]).

## Takeaways
- [ ] Before fine-tuning on company data, decide what must be memorized (needed for planning) vs retrieved ([[episodes/explainable--164-gilad-levi-continual-learning]])

## Related
[[concepts/agent-memory]] · [[concepts/rag]] · [[concepts/llm-pretraining]] · [[concepts/memory-consolidation]] · [[concepts/human-vs-ai-memory]] · [[concepts/world-models]]
