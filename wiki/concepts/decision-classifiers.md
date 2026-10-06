---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# Decision Classifiers (e.g. Jev)

**Summary:** Non-generative models that answer typed questions about a context with calibrated confidences, in a single fast pass. Jev is the hyped example: trained with reinforcement learning on decision points in conversations, it suits bulk, cheap, low-latency decisions (filtering, routing, risk scores, guardrail checks) where an LLM would be overkill. It can't reason, use tools, or explain itself, so it complements agents rather than replacing them.

## Key ideas
- Interface: a *state* (context) plus *questions* with types (boolean or free-text labels) and instructions, e.g. "is this PR safe to merge?" returns true/false with a confidence ([[episodes/langtalks--74-jev]]).
- Differences from older zero-shot classifiers: labels aren't baked into the model, confidences are calibrated, many questions run in one pass with shared context, and it's trained on conversational decisions ([[episodes/langtalks--74-jev]]).
- Cost and latency: about $0.04 per million input tokens and free output (one token) versus Gemini 3.8 Flash at $0.75/$3.75. With no thinking tokens it's ~30–100× cheaper in practice, ~0.25 s versus 2–9 s ([[episodes/langtalks--74-jev]]).
- Alternative: cache a system prompt on a cheap LLM and fan out parallel calls; zero-shot classifiers on Hugging Face do similar things ([[episodes/langtalks--74-jev]]).
- Use cases: pre-filter 1,000 repos or 10,000 Notion pages down to 20–50 before an agent looks; decide which Slack events an agent should react to; PR risk low/medium/high; rank DOM elements for browser agents; judge risky tool calls; check whether an agent ignored AGENTS.md (as a hook) ([[episodes/langtalks--74-jev]]).
- Failure mode: when wrong, there's no signal or way to steer. It denied that 19 Sep 2026 was a Saturday even though the state said so ([[episodes/langtalks--74-jev]]).

## Disagreements & open questions
- Is it the start of a new model family? Possibly, but like RAG it may not be worth the engineering once agents get fast and cheap enough ([[episodes/langtalks--74-jev]]).

## Takeaways
- [ ] Use a cheap classifier (or cached cheap LLM) to pre-filter large candidate sets before an agent reasons over them ([[episodes/langtalks--74-jev]])
- [ ] Don't decompose conversational agents into decision trees of classifier calls; they break as LLMs improve ([[episodes/langtalks--74-jev]])
- [ ] If adopting a new model provider, keep a fallback to your existing LLM path ([[episodes/langtalks--74-jev]])

## Related
[[concepts/rag]] · [[concepts/llm-cost-optimization]] · [[concepts/model-selection]] · [[concepts/ai-guardrails]]
