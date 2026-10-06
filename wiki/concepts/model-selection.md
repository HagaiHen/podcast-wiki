---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# Model Selection

**Summary:** Bigger isn't automatically better: there's no bad model, only a model that hasn't been taught the task. Before upgrading, narrow the task's scope, reframe the question, and manage context aggressively, which often lets a small, cheap, fast model do the job. Big reasoning models are convenient because you can say little, but you pay in money and latency, which B2C margins and customer-facing agents can't afford.

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

## Disagreements & open questions

## Takeaways
- [ ] Before upgrading a model, narrow the task and rephrase the question; retest on the small model ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Split complex tasks so each small-model call has ≤2–3 logic steps ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Set reasoning-token budgets instead of default effort levels where available ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/context-engineering]] · [[concepts/llm-inference]] · [[concepts/open-weight-models]]
