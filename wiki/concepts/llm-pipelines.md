---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# LLM Pipelines (vs agents) in production

**Summary:** For high-volume production features with strict accuracy, latency, cost, and explainability needs, a mostly deterministic pipeline with LLM steps beats an autonomous agent: no tool-choice mistakes or back-and-forth, and every output can be explained to a customer. Start by defining KPIs, give each LLM step the *minimal* context it needs, ask for reasoning plus confidence, validate claims against ground truth, and route the cases the pipeline can't handle to fallback strategies.

## Key ideas
- Define KPIs before experimentation, not after a naive proof of concept ([[episodes/langtalks--66-scaling-llmops]], [[people/avi-lumelsky]]).
- Minimal context: for CVE enrichment, not the whole codebase (unscalable) but the patch diff plus all public references, just as a security researcher reads the fix ([[episodes/langtalks--66-scaling-llmops]]).
- Ask for reasoning and a 0–1 confidence; tune the threshold on larger experiments; never present LLM output as gospel. Check that the claimed function exists in the customer's environment and version to cut false positives ([[episodes/langtalks--66-scaling-llmops]]).
- Explainability matters for customers: "the diff changed authenticate_user and the CVE describes an auth bypass" ([[episodes/langtalks--66-scaling-llmops]]).
- Funnel of strategies: the pipeline handles X%, and the rest goes to a fallback (skip for now, run an agent and tell the user it'll take longer, or a stronger model on the same pipeline) ([[episodes/langtalks--66-scaling-llmops]]).
- Rule-based pre-filters (regex, graphs) can come from domain experts or from Claude Code mining labeled data ([[episodes/langtalks--66-scaling-llmops]]).
- Language-agnostic tooling: an OpenAI-compatible internal endpoint (AWS Bedrock Access Gateway) let Go, TypeScript, and Python teams use any SDK; LLM calls live inline in existing services, not separate "AI microservices" ([[episodes/langtalks--66-scaling-llmops]]).
- A client SDK wraps prompts with their context-building logic and versions them, so swapping a prompt version is a one-line change and the prompt has one source of truth ([[episodes/langtalks--66-scaling-llmops]]).
- Strategy flavors on one engine ("accurate" vs "fast" via config, e.g. skipping extra validation and using faster models) let a new channel (voice) reuse the same evals and feedback loop instead of forking the system ([[episodes/langtalks--61-voice-agents]]).

## Disagreements & open questions
- Use an off-the-shelf proxy (features, but a dependency) or build a lean internal one (now easy with Claude Code)? ([[episodes/langtalks--66-scaling-llmops]])

## Takeaways
- [ ] Define KPIs for an AI feature before the first experiment ([[episodes/langtalks--66-scaling-llmops]])
- [ ] Prefer a pipeline with reasoning + confidence + ground-truth validation over an agent for high-volume features ([[episodes/langtalks--66-scaling-llmops]])
- [ ] Version prompts together with their context-building code in a shared client SDK ([[episodes/langtalks--66-scaling-llmops]])

## Related
[[concepts/llm-evals]] · [[concepts/model-selection]] · [[concepts/decision-classifiers]] · [[concepts/ai-gateway]] · [[concepts/voice-agents]]
