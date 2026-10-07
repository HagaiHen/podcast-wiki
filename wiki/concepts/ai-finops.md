---
type: concept
hubs: [ai-engineering]
sources: 4
updated: 2026-10-07
---
# AI FinOps (attributing and managing AI spend)

**Summary:** Managing AI costs like any cloud cost: attribute spend to the systems, teams, and use cases that generate it, then optimize per unit. The crux is attribution. Provider bills lump calls together, so tag every call (usually at a gateway) and log telemetry (prompt, response, tokens, metadata). A use case's true cost combines tokens, observability, subscriptions, *and* its databases and infrastructure. For coding agents, spend per developer is rising; the question is value per dollar, not cutting to zero.

## Key ideas
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

## Disagreements & open questions
- Is cost even the issue? One host argues flat $200 subscriptions make it moot and the real question is business impact ([[episodes/langtalks--67-finops-for-ai]]).

## Takeaways
- [ ] Require use-case/repo metadata on every LLM call via an internal proxy or gateway ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Review the sessions of your heaviest and lightest AI spenders for fixes and practices to spread ([[episodes/langtalks--67-finops-for-ai]])
- [ ] Compute full unit economics per AI feature (tokens + infra + tools) ([[episodes/langtalks--67-finops-for-ai]])

## Related
[[concepts/ai-gateway]] · [[concepts/llm-cost-optimization]] · [[concepts/harness-engineering]] · [[concepts/ai-engineering-metrics]]
