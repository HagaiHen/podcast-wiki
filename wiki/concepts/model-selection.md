---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# Model Selection

**Summary:** Bigger isn't automatically better: there's no bad model, only a model that hasn't been taught the task. Before upgrading, narrow the task, reframe the question, and manage context, which often lets a small, cheap, fast model do the job. Choose on *your* evals, not public benchmarks. Plan with a strong model and execute with a cheaper one, keep prompts tuned per model version, and always have a tested fallback model so an outage or regression doesn't reach customers.

## Key ideas
- A ~35B Qwen model insisted a car in a video wasn't changing lanes; a big model got it right but at negative ROI. Asking instead "does the line move from the left of the frame to the right?" made the small model correct ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]).
- Scheduling PDFs failed even on Opus; a small model found cut points, the PDF was sliced, and the slices worked "phenomenally" ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- For ~30B models, target an "attention-deficit" level of focus: no more than 2–3 logic steps per call ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Newer models need less role-setting preamble, and preamble eats context in small models ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Reasoning budgets: many inference stacks let you cap thinking tokens; budget them so reasoning doesn't consume the whole context ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Batch ("take one") jobs of ~1.8M prompts must work the first time, so prompt engineering matters even more ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- B2C: one conversation can't cost the user's lifetime value, so stay on small models ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Consumer apps still make users choose models: partly marketing and psychology (launches like "Fable 5"); automatic routing via classifiers is coming ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- His coding defaults: Sonnet/Opus; Fable only for specific, patience-worthy cases; reasoning-heavy expensive models can over-research simple asks ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Every product should have a primary and a pre-tested fallback model (downgrade a version, or switch to another vendor's family) ([[episodes/ai-engineering-podcast--ai-infra-at-scale]], [[people/dor-cohen]]).
- Developers must know their models well enough to tune prompts per model version ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Public benchmarks often don't match your environment; test on your own evals ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).

## Disagreements & open questions

## Takeaways
- [ ] Before upgrading a model, narrow the task and rephrase the question; retest on the small model ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Split complex tasks so each small-model call has ≤2–3 logic steps ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Set reasoning-token budgets instead of default effort levels where available ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/context-engineering]] · [[concepts/llm-inference]] · [[concepts/open-weight-models]] · [[concepts/llm-evals]] · [[concepts/ai-gateway]]
