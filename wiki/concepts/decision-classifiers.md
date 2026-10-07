---
type: concept
hubs: [ai-engineering]
sources: 4
updated: 2026-10-07
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
- Fine-tuned small models (segmentation and classification heads) are the in-house alternative to hosted classifiers, with task-specific losses ([[episodes/langtalks--59-slms]]).
- Mental model: not "ask Jev" but a typed API. Input object plus output schema in, probabilities out in ~200 ms regardless of size. 1,700 emails scored on four fields cost 18 cents ([[episodes/startup-ideas--jev-is-here]], [[people/ryan-vogel]]).
- Startup lens: find a business with an expensive queue of incoming information (leads, support tickets, quote requests) and put a decision model at the front to route each item to a human, an LLM, or the bin by confidence ([[episodes/startup-ideas--jev-is-here]], [[people/greg-isenberg]]).
- More uses: lead scoring on a contact form, picking short-form clips from a word-level transcript, and fast browser control (Browser Use booked a flight in 7.1 s). Poor where real judgment is needed: a minute-by-minute Bitcoin buy/sell signal flopped ([[episodes/startup-ideas--jev-is-here]]).
- Hack: making each next letter a decision lets it "generate" text slowly, showing it's not built for conversation ([[episodes/startup-ideas--jev-is-here]]).
- Real-world classification resists clean hierarchies: in device identification an Xbox and a surgical robot can look alike until one late feature, so you can't simply split "animals → mammals → dogs" ([[episodes/hidden-layers--claroty-ben-mashiach]], [[people/ben-mashiach]]).
- Domain experts and data scientists must co-build features (e.g. an expert's fingerprint-then-hash idea handed to a model); a latent-space map of unclassified items turns expert labeling into "quests" ([[episodes/hidden-layers--claroty-ben-mashiach]], [[people/ben-mashiach]]).
- Beyond classification, named-entity extraction pulls model, serial number, and OS version from raw text blobs; LLM embeddings place items semantically for grouping and policy ([[episodes/hidden-layers--claroty-ben-mashiach]], [[people/ben-mashiach]]).

## Disagreements & open questions
- Is it the start of a new model family? Possibly, but like RAG it may not be worth the engineering once agents get fast and cheap enough ([[episodes/langtalks--74-jev]]).

## Takeaways
- [ ] Use a cheap classifier (or cached cheap LLM) to pre-filter large candidate sets before an agent reasons over them ([[episodes/langtalks--74-jev]])
- [ ] Don't decompose conversational agents into decision trees of classifier calls; they break as LLMs improve ([[episodes/langtalks--74-jev]])
- [ ] If adopting a new model provider, keep a fallback to your existing LLM path ([[episodes/langtalks--74-jev]])
- [ ] List the decision points in your daily workflow (triage, lead quality, routing) and try a decision model on one ([[episodes/startup-ideas--jev-is-here]])

## Related
[[concepts/rag]] · [[concepts/llm-cost-optimization]] · [[concepts/model-selection]] · [[concepts/ai-guardrails]] · [[concepts/small-language-models]]
