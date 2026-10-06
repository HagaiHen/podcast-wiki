---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# RAG (Retrieval-Augmented Generation)

**Summary:** Retrieving relevant documents and feeding them to the model to generate the answer. It became a commodity in 2023, evolved into agentic RAG (the agent chooses to call retrieval as a tool), and is comparatively easy to evaluate because domain experts can judge answers on your own data. Per Roi Zalta it covers ~99% of real needs; you move beyond it when knowledge keeps accumulating across documents, tables, and people.

## Key ideas
- Classic RAG: you choose and ingest documents (later tables), then maintain them ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Agentic RAG: the agent decides when to retrieve, distills, and generates the final answer ([[episodes/ai-engineering-podcast--company-brain]]).
- Evaluation is relatively easy: domain experts from the org can grade answers ([[episodes/ai-engineering-podcast--company-brain]]).
- Early RAG targeted humans (onboarding, internal Google); autonomous agents made context sharing a much bigger problem ([[episodes/ai-engineering-podcast--company-brain]]).
- GraphRAG (Microsoft open source) extracted entities and relations, but context limits two years ago meant it couldn't handle a whole book ([[episodes/ai-engineering-podcast--company-brain]]).

## Disagreements & open questions
- Roi: RAG is what you need in 99% of cases. Dana Maman: RAG makes its own mistakes, and she's trying to stay with a wiki past ~100 sources ([[episodes/osim-tochna--second-brain-and-llm-wiki]]). See [[concepts/wiki-retrieval]].

## Takeaways
- [ ] Start with (agentic) RAG and expert-graded evals before building anything more complex ([[episodes/ai-engineering-podcast--company-brain]])

## Related
[[concepts/wiki-retrieval]] · [[concepts/company-brain]] · [[concepts/knowledge-graphs]]
