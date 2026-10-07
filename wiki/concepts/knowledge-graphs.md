---
type: concept
hubs: [knowledge-management, ai-engineering]
sources: 4
updated: 2026-10-07
---
# Knowledge Graphs & Ontology

**Summary:** Representing knowledge as entities and relationships (an ontology) rather than documents. Hard for humans to read, but valuable to agents for understanding how an organization works: who, what, when, why, and what depends on what. A graph gives agents a map instead of a flashlight, so they don't exhaust themselves querying one spot at a time or misread an empty result from a slightly wrong filter as "nothing happened". Popularized in enterprises by Palantir; GraphRAG and Databricks' Genie Ontology bring it to AI stacks, and security platforms build hybrid graphs (batch-built, plus live queries for freshness).

## Key ideas
- Ontologies help agents grasp an org's relationships, metrics, and mechanics ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Palantir deploys engineers to build company-level ontologies for defense, logistics, and more ([[episodes/ai-engineering-podcast--company-brain]]).
- Databricks Genie Ontology ranks "snippets" (docs, tables, dashboards, markdown, *people*) with a relevance model (OntoRank) and can tell an agent "this only lives with this person; go ask him" ([[episodes/ai-engineering-podcast--company-brain]]).
- Key elements to extract: actors, interactions, time (relative urgency), rationales, dependencies ([[episodes/ai-engineering-podcast--company-brain]]).
- Maintenance options include keeping only metadata/references plus cleanup jobs ([[episodes/ai-engineering-podcast--company-brain]]).
- Topology maps help agents: a customer-validated map of Kubernetes resource relationships, serialized as YAML in the prompt, beat letting the agent rediscover them ([[episodes/langtalks--65-ai-sre]]).
- Humans organize knowledge into schemas that speed encoding and retrieval. Agent memory stores facts independently, and it's unclear that GraphRAG matches how the brain does this ([[episodes/langtalks--60-brain-memory]]).
- Give agents a map, not a flashlight: query tools let an agent illuminate one spot at a time, and it exhausts itself or stops at the first hit. A context graph of resolved entities and relationships (an ontology over normalized data) answers in one place. Build it in batches, and combine it with live queries for freshness ([[episodes/hidden-layers--vega-gili-kanfo]], [[people/gili-kanfo]]).
- Silent failures motivate it: a query filtering on a slightly wrong value ("uri" vs "Uri") runs fine and returns nothing, which an agent reads as "no activity", whereas a human would sense something off ([[episodes/hidden-layers--vega-gili-kanfo]], [[people/gili-kanfo]]).

## Disagreements & open questions

## Takeaways

## Related
[[concepts/second-brain]] · [[concepts/rag]] · [[concepts/ai-sre]]
