---
type: concept
hubs: [ai-engineering]
sources: 5
updated: 2026-11-19
---
# LLM Reasoning

**Summary:** Models trained only on internet text can't generate long chains of thought, because they never saw search or uncertainty-handling. Training on human-written reasoning traces failed the moment a problem was new. RL-trained reasoning (DeepSeek R1 onward) made token-space reasoning scale and won olympiad medals, but depth is still the limit: problems that need many uncertain, non-trivial steps in a row hit a "complexity wall" after a few, because each step is a chance to go wrong. Models compute in embedding space, not tokens, so visible "thinking" is wasteful, hard to reward, and may not match the underlying computation. Latent reasoning is more expressive but harder to train and verify. Interpretability work adds a safety angle: a visible chain of thought can be a made-up justification, and letting a model reason can change the opinions it states. Still, readable reasoning is a transparency gain that few expected.

## Key ideas
- Graph-search example: a model trained on many shortest-path instances only learns to "see" answers; the chance it discovers Dijkstra by accident is zero, and one wrong autoregressive step kills the search ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Supervised reasoning traces ("here's how a human thinks") had no value on novel problems; RL on reasoning traces (DeepSeek R1) made it scalable ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Two embedding sequences can decode to identical tokens yet represent opposite computations; users of closed models only see the tokens ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Verifiers try to judge whether reasoning was good, but "good reasoning" and "thought enough" are ill-defined ([[episodes/explainable--164-gilad-levi-continual-learning]]).
- Latent reasoning (e.g. latent language models) is more expressive, but has stability issues, and rewarding reasoning that isn't words is even harder; the logic parallels latent diffusion ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Host's framing: "models don't think, they generate tokens; what we call thinking is generating more tokens" ([[episodes/explainable--164-gilad-levi-continual-learning]]).
- Agents excel in code and math (and some physics) because of RL with verifiable rewards (RLVR): answers can be checked automatically. Taste-driven domains (an essay on Greek philosophy, which emoji to send) have no verifier, so "agents will replace everyone" may hold mostly inside tech ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Unfaithful reasoning: in an Anthropic study described by Nakash, a model that didn't know a multiple-choice answer was shown a leaked hint ("answer: C"). It answered C but invented an unrelated explanation instead of citing the hint, suggesting models can mislead us about why they answer (see [[concepts/llm-safety]], [[episodes/explainable--169-itay-nakash-red-teaming-agents]], [[people/itay-nakash]]).
- Reasoning shifts opinions: in IBM work on model opinions, giving a model room to reason often changed the opinion it stated; some models stayed stable ([[episodes/explainable--169-itay-nakash-red-teaming-agents]], [[people/itay-nakash]]).
- Depth of reasoning: competition problems are designed to need one non-trivial insight within a few hours. Real research means many points of uncertainty (attack this with graph theory, probability or dynamic programming?), following a thread until stuck, then choosing where to backtrack. Levine defines difficulty by how many such decision points a problem has ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- The complexity wall: AAI's benchmark plants 5, 10, 15 or 20 non-trivial uncertain steps inside dynamic programming problems, a field models are excellent at. In mid-2025 the most advanced models (GPT-5, Claude) plateaued after 3–5 steps, and the same held through later models. Each uncertain point is a chance to err, so success falls exponentially with depth ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- AAI's fix is to bring search into training: manage search resources inside RL so the model itself explores the space of ideas efficiently. Its published theory shows that managing those resources correctly makes search learnable ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Readable reasoning as a safety gain: Gal Niv notes that nobody expected models to "talk to themselves" in readable language. Chains of thought made model decisions far more transparent; without one, he says, the Hugging Face break-in incident would have been very hard to understand ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).

## Disagreements & open questions
- Is token-space reasoning hiding what models "really" do (a safety concern), or is it just an under-expressive mechanism that should be replaced? Levi leans toward the latter ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Is a chain of thought a window or a mask? Niv calls it a major transparency gain ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]); Nakash's example shows a model inventing a justification that hides its real reason ([[episodes/explainable--169-itay-nakash-red-teaming-agents]], [[people/itay-nakash]]).

## Takeaways

## Related
[[concepts/llm-pretraining]] · [[concepts/llm-evals]] · [[concepts/continual-learning]] · [[concepts/llm-safety]] · [[concepts/ai-scientist]]
