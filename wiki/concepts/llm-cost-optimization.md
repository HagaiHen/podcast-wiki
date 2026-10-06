---
type: concept
hubs: [ai-engineering]
sources: 4
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
- Optimize whole traces, not single prompts: fewer tool calls, and smaller tool responses that keep the needed context (strip headers, reformat JSON to YAML) ([[episodes/langtalks--67-finops-for-ai]]).
- Prompt compression is back: a community repo reportedly raised GPT 5.2 quality ~30% without extra cost or latency; startups mine traces for cheaper call patterns and caching ([[episodes/langtalks--67-finops-for-ai]]).
- Iterative real-time analysis (re-asking with all prior events each time) benefits hugely from Bedrock prompt caching, since most input repeats ([[episodes/langtalks--66-scaling-llmops]]).
- Rate limits: cross-region inference profiles gave ~5× the throughput of a region-pinned model (e.g. EU Sonnet → global), while staying compliant; some companies also spread load across multiple accounts ([[episodes/langtalks--66-scaling-llmops]]).

## Disagreements & open questions

## Takeaways
- [ ] Order prompts stable-first (system prompt, then user/task data); no timestamps up front ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Constrain output length and structure to cut output-token cost ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Plan with a strong model, execute with a cheaper one ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Trim and reformat tool responses (drop unused fields; JSON → YAML) before they reach the model ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Use cross-region inference (where compliant) to raise rate limits before buying capacity ([[episodes/langtalks--66-scaling-llmops]])

## Related
[[concepts/ai-gateway]] · [[concepts/llm-inference]] · [[concepts/model-selection]] · [[concepts/ai-finops]]
