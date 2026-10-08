---
type: concept
hubs: [ai-engineering]
sources: 10
updated: 2026-10-08
---
# LLM Cost Optimization

**Summary:** Managing LLM spend has two halves: measuring it and reducing it. **Measuring (AI FinOps)** treats AI like any cloud cost. Provider bills lump calls together, so tag every call at a gateway or internal proxy, log the telemetry, and compute full unit economics per use case: tokens plus observability, subscriptions, databases and infrastructure. **Reducing** comes down to engineering habits. Put stable content first so prompt caching works (cached tokens cost roughly a tenth). Output costs more than input, so ask for short, structured answers. Plan with a strong model and execute with a cheap one, and trim whole traces, not single prompts. For coding agents, spend per developer is rising; the goal is value per dollar, not cutting to zero.

## Key ideas

### Measuring: attribution and unit economics (AI FinOps)
- Bedrock's cost report can't tell which of many systems made a call. Inference profiles (logical model IDs per team) helped but don't scale; the shift is to gateway tagging and call logs exported (e.g. to S3) ([[episodes/langtalks--67-finops-for-ai]], [[people/yizhar-gilboa]]).
- Simplest implementation: an internal proxy exposing the same model API but requiring metadata (repo, use case) on each call ([[episodes/langtalks--67-finops-for-ai]]).
- Holistic unit economics: customer-support cost equals agent tokens plus its database, backend, and tooling, the same way you'd break down storage per GB or DB queries ([[episodes/langtalks--67-finops-for-ai]]).
- Coding spend per developer: ~65% of companies $100–300/month, ~30% $300–600, ~5% under $100 ([[episodes/langtalks--67-finops-for-ai]]).
- It must not be zero: every developer can benefit; the best treat themselves as leads of small agent teams ([[episodes/langtalks--67-finops-for-ai]]).
- Analyze the extremes: non-users need adoption help (education, guilds, peer review); heavy spenders' sessions reveal infrastructure fixes (e.g. if code exploration eats 30% of tokens, maintain docs/indexes to cut it) and good practices to spread via skills ([[episodes/langtalks--67-finops-for-ai]]).
- AI in production costs much more than AI for coding; companies still happily open the tap for coding when it boosts productivity ([[episodes/langtalks--67-finops-for-ai]]).
- Prediction: the theoretical $1–2k/month per-developer ceiling will break; money becomes tokens, intelligence, energy ([[episodes/langtalks--67-finops-for-ai]]).
- Mandatory project tags on an internal LLM API answer whether, say, the back office is half the Bedrock bill or negligible ([[episodes/langtalks--66-scaling-llmops]]).
- Spend should be read alongside productivity metrics: productivity per dollar ([[episodes/langtalks--64-ai-coding-metrics]]).
- Hidden production costs demos skip: calling a model on another cloud (e.g. Gemini from AWS infrastructure) adds data egress fees; EU customers may forbid data leaving Europe, so global routing for capacity overflow is off-limits; you must verify the vendor isn't logging or retaining data ([[episodes/osim-tochna--ai-in-production-reality-vs-imagination]]).

### Reducing: engineering habits
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
- Tool overload (100+ tools) hurts, but swapping tool subsets per step breaks the KV cache. Manus masks token logits to restrict tool choice while keeping the prefix stable ([[episodes/langtalks--55-context-engineering]]).
- Agents are expensive at scale: the OpenClaw creator reportedly ran 100 Codex agents nonstop for a month for ~$1M in tokens. An agency estimates ~$500k just to build a working multi-agent system (team, architecture, memory, RAG), before infra and tokens ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Subscriptions are subsidized: a heavy Claude Max $200 user would cost ~$1.5–2k at API prices (~1:10). If vendors switch to AWS-style metered billing, economics change ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Every skill, hook, and plugin loaded into context costs tokens on each send; a big context window fills fast and burns the weekly quota ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Inference optimization is a growing role: minimize $/1M tokens while meeting the SLA, since every token costs GPU time and electricity ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Kubernetes FinOps beyond tokens: Riskified combined spot instances with reserved instances and savings plans, and built a controller that steers Karpenter's spot/on-demand mix by how well the org's commitments are being used. Almost no servers run at full price (all >50% off), saving 30–40% on Kubernetes. Installing a tool by its quick-start isn't enough; value comes from understanding your environment ([[episodes/osim-tochna--running-llms-at-scale]], [[people/kfir-schneider]]).
- Margins differ by feature: agent features run close to raw LLM cost, especially when users can pick the priciest model, while non-AI automations keep software margins, so a product's blended margin depends on its usage mix ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]])

## Disagreements & open questions
- Is cost even the issue? One host argues flat $200 subscriptions make it moot and the real question is business impact ([[episodes/langtalks--67-finops-for-ai]]).
- Flat subscriptions as the answer vs a temporary subsidy: a heavy Claude Max $200 user would cost ~$1.5–2k at API prices, and metered billing would change the economics ([[episodes/explainable--163-hidden-cost-of-agents]], [[episodes/langtalks--67-finops-for-ai]]).
- How long will the subsidy last? Inference optimizer Mike Erlihson says LLM vendors lose huge sums (perhaps ~$1B a month) and expects $100–200 subscriptions could become ~$1,000 when the party ends; host Amit Bendor notes competition is still holding prices down ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]], [[people/amit-bendor]]).

## Takeaways
- [ ] Require use-case/repo metadata on every LLM call via an internal proxy or gateway ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Review the sessions of your heaviest and lightest AI spenders for fixes and practices to spread ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Compute full unit economics per AI feature (tokens + infra + tools) ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Order prompts stable-first (system prompt, then user/task data); no timestamps up front ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Constrain output length and structure to cut output-token cost ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Plan with a strong model, execute with a cheaper one ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Trim and reformat tool responses (drop unused fields; JSON → YAML) before they reach the model ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Use cross-region inference (where compliant) to raise rate limits before buying capacity ([[episodes/langtalks--66-scaling-llmops]])
- [ ] Keep the tool list stable and restrict choices via logit masking/constrained decoding rather than swapping tools mid-session ([[episodes/langtalks--55-context-engineering]])
- [ ] Audit which skills, hooks, and plugins load into every agent session; drop the unused ones ([[episodes/explainable--163-hidden-cost-of-agents]])
- [ ] Match cloud commitments (reserved instances, savings plans) to actual usage, and steer the autoscaler's spot/on-demand mix by commitment utilization ([[episodes/osim-tochna--running-llms-at-scale]])

## Related
[[concepts/ai-gateway]] · [[concepts/llm-inference]] · [[concepts/model-selection]] · [[concepts/harness-engineering]] · [[concepts/ai-engineering-metrics]] · [[concepts/decision-classifiers]] · [[concepts/ai-pricing]]
