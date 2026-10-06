---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-07
---
# LLM Reasoning

**Summary:** Models trained only on internet text can't generate long chains of thought, because they never saw search or uncertainty-handling. Training on human-written reasoning traces failed the moment a problem was new. RL-trained reasoning (DeepSeek R1 onward) made token-space reasoning scale. But models compute in embedding space, not tokens, so visible "thinking" is wasteful, hard to reward, and may not match the underlying computation. Latent reasoning is more expressive but harder to train and verify.

## Key ideas
- Graph-search example: a model trained on many shortest-path instances only learns to "see" answers; the chance it discovers Dijkstra by accident is zero, and one wrong autoregressive step kills the search ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Supervised reasoning traces ("here's how a human thinks") had no value on novel problems; RL on reasoning traces (DeepSeek R1) made it scalable ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Two embedding sequences can decode to identical tokens yet represent opposite computations; users of closed models only see the tokens ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Verifiers try to judge whether reasoning was good, but "good reasoning" and "thought enough" are ill-defined ([[episodes/explainable--164-gilad-levi-continual-learning]]).
- Latent reasoning (e.g. latent language models) is more expressive, but has stability issues, and rewarding reasoning that isn't words is even harder; the logic parallels latent diffusion ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Host's framing: "models don't think, they generate tokens; what we call thinking is generating more tokens" ([[episodes/explainable--164-gilad-levi-continual-learning]]).
- Agents excel in code and math (and some physics) because of RL with verifiable rewards (RLVR): answers can be checked automatically. Taste-driven domains (an essay on Greek philosophy, which emoji to send) have no verifier, so "agents will replace everyone" may hold mostly inside tech ([[episodes/explainable--163-hidden-cost-of-agents]]).

## Disagreements & open questions
- Is token-space reasoning hiding what models "really" do (a safety concern), or is it just an under-expressive mechanism that should be replaced? Levi leans toward the latter ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).

## Takeaways

## Related
[[concepts/llm-pretraining]] · [[concepts/llm-evals]] · [[concepts/continual-learning]]
