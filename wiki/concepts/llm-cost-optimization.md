---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# LLM Cost Optimization

**Summary:** Engineering habits that cut token spend without hurting quality. Put stable content first so prompt caching works (cached tokens cost roughly a tenth); remember output tokens cost more than input, so ask for short, structured answers; and split planning (strong model) from execution (cheaper model). Measure before optimizing: a gateway gives the visibility.

## Key ideas
- Caching works from the top down until the first change. Put the system prompt (generic, repeated) first and per-user and per-task data after ([[people/dor-cohen]], [[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Anti-pattern: a timestamp at the start of every prompt broke the cache before it began ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- In chat, every turn resends the whole history (N+1), so good caching of the prefix matters a lot ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Personalization context that rarely changes (who the user is, their boards) belongs in the stable prefix ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Output tokens cost more than input. Chatty, over-explaining answers cost you and the user, so constrain structure and length ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Plan vs execute: plan with Opus, execute with Sonnet, Haiku, or another model, in products as in your own dev workflow ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Prompt routing mid-session breaks the model's cache. A gateway-level cache can add consistency ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- For pure classification at scale, a dedicated classifier can be ~30–100× cheaper and far faster than a small LLM with thinking (see [[concepts/decision-classifiers]], [[episodes/langtalks--74-jev]]).

## Disagreements & open questions

## Takeaways
- [ ] Order prompts stable-first (system prompt, then user/task data); no timestamps up front ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Constrain output length and structure to cut output-token cost ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Plan with a strong model, execute with a cheaper one ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])

## Related
[[concepts/ai-gateway]] · [[concepts/llm-inference]] · [[concepts/model-selection]]
