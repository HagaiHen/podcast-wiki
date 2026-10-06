---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# AI SRE (agents for production reliability)

**Summary:** An AI site-reliability engineer detects production problems, investigates root causes, and increasingly remediates them. Investigation is the hard core: production data is huge and noisy, so a naive agent with log access quickly floods its context and hallucinates. Good AI SREs reuse existing detection, query a normalized backend instead of raw sources, investigate like a human ("hops and signals" into a tree of hypotheses), and inject environment topology as context. Self-healing is the 2026 frontier; prevention comes next.

## Key ideas
- Stages: detection → investigation → remediation / self-healing. Remediation is easy for AI but most sensitive for humans, who need the *why* ([[episodes/langtalks--65-ai-sre]], [[people/asaf-savich]]).
- Naive approach (agent SDK + Datadog MCP + kubectl) fails on noise filtering and context exhaustion except for narrow, small problems ([[episodes/langtalks--65-ai-sre]]).
- Hops and signals: high memory in service A → logs show service B flooding it → B fell back because DB calls fail → check the DB. Each step picks the next lead ([[episodes/langtalks--65-ai-sre]]).
- Hypotheses form a tree. A dead branch at level six doesn't invalidate the proven levels above; branches can run in parallel in separate contexts, which takes workflow engineering ([[episodes/langtalks--65-ai-sre]]).
- Data layer: a daemon in each customer cluster feeds a normalized backend mapped to Kubernetes' hierarchy (namespaces, deployments, CRDs, plus Argo and Helm); the agent queries the backend, not the daemon. Pre-built tools like "all unhealthy workloads" save hops ([[episodes/langtalks--65-ai-sre]]).
- Topology as context: for a customer with very complex CRD relationships, a validated map of their environment in the preprompt (as YAML, easier for LLMs than graphs) raised investigation quality several levels ([[episodes/langtalks--65-ai-sre]]).
- Customers want the full cycle: why wait for a human on call while the service is down? Prevention (spotting services heading for trouble, restructuring hotspots) comes next ([[episodes/langtalks--65-ai-sre]]).
- Bringing in third-party data (APMs, Grafana, cloud providers) makes evaluation harder, since the inputs are outside your control ([[episodes/langtalks--65-ai-sre]]).

## Disagreements & open questions
- Is the goal just restoring production, or a deeper root-cause fix ([[episodes/langtalks--65-ai-sre]])?

## Takeaways
- [ ] Give investigation agents normalized, pre-filtered data and purpose-built query tools, not raw log firehoses ([[episodes/langtalks--65-ai-sre]])
- [ ] Inject a validated map of the system's topology into the agent's context ([[episodes/langtalks--65-ai-sre]])

## Related
[[concepts/llm-evals]] · [[concepts/context-engineering]] · [[concepts/knowledge-graphs]] · [[concepts/llm-pipelines]]
