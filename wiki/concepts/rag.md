---
type: concept
hubs: [ai-engineering]
sources: 4
updated: 2026-10-07
---
# RAG (Retrieval-Augmented Generation)

**Summary:** Retrieving relevant documents and feeding them to the model to generate the answer. It became a commodity in 2023, evolved into agentic RAG (the agent chooses to call retrieval as a tool), and is comparatively easy to evaluate because domain experts can judge answers on your own data. Per Roi Zalta it covers ~99% of real needs; you move beyond it when knowledge keeps accumulating across documents, tables, and people.

## Key ideas
- Classic RAG: you choose and ingest documents (later tables), then maintain them ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Agentic RAG: the agent decides when to retrieve, distills, and generates the final answer ([[episodes/ai-engineering-podcast--company-brain]]).
- Evaluation is relatively easy: domain experts from the org can grade answers ([[episodes/ai-engineering-podcast--company-brain]]).
- Early RAG targeted humans (onboarding, internal Google); autonomous agents made context sharing a much bigger problem ([[episodes/ai-engineering-podcast--company-brain]]).
- GraphRAG (Microsoft open source) extracted entities and relations, but context limits two years ago meant it couldn't handle a whole book ([[episodes/ai-engineering-podcast--company-brain]]).
- RAG is fundamentally *filtering*: give the LLM only what it needs, avoiding lost-in-the-middle. Options: vector DB pipelines (heavy engineering), agentic search over titles (slow, expensive), or a fast classifier pre-filter ([[episodes/langtalks--74-jev]]).
- Retrieval dominates: ~85–90% of industry uses a frozen pre-trained model with retrieval, ~9% fine-tune, ~1% train broadly on company data. Retrieval suits details you'd re-read (page 140 of a book); knowledge needed for planning arguably belongs in weights ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).

## Disagreements & open questions
- History suggests heavily engineered retrieval pipelines become "clunky boxes" once agents catch up ([[episodes/langtalks--74-jev]]).
- Roi: RAG is what you need in 99% of cases. Dana Maman: RAG makes its own mistakes, and she's trying to stay with a wiki past ~100 sources ([[episodes/osim-tochna--second-brain-and-llm-wiki]]). See [[concepts/wiki-retrieval]].

## Takeaways
- [ ] Start with (agentic) RAG and expert-graded evals before building anything more complex ([[episodes/ai-engineering-podcast--company-brain]])

## Related
[[concepts/wiki-retrieval]] · [[concepts/second-brain]] · [[concepts/knowledge-graphs]] · [[concepts/decision-classifiers]] · [[concepts/continual-learning]]
