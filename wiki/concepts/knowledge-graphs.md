---
type: concept
hubs: [knowledge-management, ai-engineering]
sources: 1
updated: 2026-10-06
---
# Knowledge Graphs & Ontology

**Summary:** Representing knowledge as entities and relationships (an ontology) rather than documents. Hard for humans to read, but valuable to agents for understanding how an organization works: who, what, when, why, and what depends on what. Popularized in enterprises by Palantir; tools like Microsoft's GraphRAG and Databricks' Genie Ontology bring it to AI stacks.

## Key ideas
- Ontologies help agents grasp an org's relationships, metrics, and mechanics ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Palantir deploys engineers to build company-level ontologies for defense, logistics, and more ([[episodes/ai-engineering-podcast--company-brain]]).
- Databricks Genie Ontology ranks "snippets" (docs, tables, dashboards, markdown, *people*) with a relevance model (OntoRank) and can tell an agent "this only lives with this person; go ask him" ([[episodes/ai-engineering-podcast--company-brain]]).
- Key elements to extract: actors, interactions, time (relative urgency), rationales, dependencies ([[episodes/ai-engineering-podcast--company-brain]]).
- Maintenance options include keeping only metadata/references plus cleanup jobs ([[episodes/ai-engineering-podcast--company-brain]]).

## Disagreements & open questions

## Takeaways

## Related
[[concepts/company-brain]] · [[concepts/rag]]
