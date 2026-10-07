---
type: concept
hubs: [ai-engineering]
sources: 10
updated: 2026-10-07
---
# Model Selection

**Summary:** Bigger isn't automatically better: there's no bad model, only a model that hasn't been taught the task. Before upgrading, narrow the task, reframe the question, and manage context, which often lets a small, cheap, fast model do the job. Choose on *your* evals, not public benchmarks: start with the biggest model, then find the smallest that meets the KPI. Plan with a strong model and execute with a cheaper one, and keep prompts tuned per model version. Whether to build model-agnostic (swap per component, keep a tested fallback) or commit to one lab's models is contested.

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
- Gavriel Cohen follows Anthropic's view that agents aren't portable across providers: each lab's models behave differently, so he didn't build model-switching ([[episodes/langtalks--71-claw-architectures]]).
- Start with the biggest model, then find the smallest that meets the KPI: NVIDIA's open Nemotron (~33B active) matched Claude Sonnet 4.5 on CVE enrichment at a fraction of the cost; ~70B models suffice to flag crypto miners ([[episodes/langtalks--66-scaling-llmops]], [[people/avi-lumelsky]]).
- Small models sometimes grasp a narrow task *better* (e.g. spotting repeated base64 encoding as suspicious) ([[episodes/langtalks--66-scaling-llmops]]).
- Beyond picking among API models: training a small task-specific model can beat a general LLM on accuracy and speed; see [[concepts/small-language-models]] ([[episodes/langtalks--59-slms]]).
- Niche models: some aim to be best under real-time latency, others at long context or specific tasks. Per-intent compute (as GPT-5 varies thinking) may come to inference stacks. Smaller models gain ground as ROI starts to matter ([[episodes/langtalks--58-reinvent-predictions]]).
- For copywriting (incl. Hebrew), the host finds GPT 5.6 the best; Fable is "genius but hard to talk to" ([[episodes/ignore-instructions--28-ai-marketing-enso]]).
- Model-agnostic by design: every component (builders, runners) can use Gemini, OpenAI, Anthropic, or xAI behind a generic interface; an ML team keeps benchmarking and swapping per component. A better open-source voice-activity model was adopted within two days ([[episodes/ignore-instructions--24-wonderful-road-to-100m]]).
- Frontier models pass POCs easily but often fail production on unit economics and latency: re-touching a whole retail catalog for Christmas with a giant model is "a 5-kilo hammer for adding snowflakes". Smaller, controllable models win such jobs ([[episodes/hidden-layers--bria-misha-feinstein]], [[people/misha-feinstein]]).
- Match architecture to the problem: encoders for extraction (business-context NER), fine-tuned open decoders where an explanation is needed (risk scoring people can trust, since a bare "88" means nothing), and frontier models mainly for prototyping and ground truth ([[episodes/hidden-layers--cyera-shiran-bareli]], [[people/shiran-bareli]]).

## Disagreements & open questions
- Portability: Dor Cohen urges avoiding vendor lock-in with tested fallbacks ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]); Wonderful builds every component model-agnostic and swaps per component ([[episodes/ignore-instructions--24-wonderful-road-to-100m]]); Gavriel Cohen argues agents can't simply swap models ([[episodes/langtalks--71-claw-architectures]]).

## Takeaways
- [ ] Before upgrading a model, narrow the task and rephrase the question; retest on the small model ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Split complex tasks so each small-model call has ≤2–3 logic steps ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Set reasoning-token budgets instead of default effort levels where available ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/context-engineering]] · [[concepts/llm-inference]] · [[concepts/open-weight-models]] · [[concepts/llm-evals]] · [[concepts/ai-gateway]] · [[concepts/llm-pipelines]] · [[concepts/small-language-models]]
