---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# Wiki Retrieval

**Summary:** Finding the right page in a growing LLM wiki is the weak point: stored text is phrased as answers, while questions use different words, so the agent bridges the gap by guessing search terms, searching the index, and falling back to grep. A single guess and the first hit often fail. Widening the search (several guesses, ranking several candidates) improves accuracy dramatically at modest token cost. RAG is the usual next step past ~100 sources but has its own errors; hybrids (core in the wiki, long tail in RAG) and topic clustering are emerging.

## Key ideas
- Observed flow: guess → search the index with the guess's words → open the hit, else grep the whole wiki (imprecise) ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Fix: generate 3 guesses instead of 1, then rank 3–4 index candidates before opening any ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- "What's the point of a huge wiki if I can't get to it?" ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Hybrid approaches: most important knowledge in the wiki, the rest in RAG; also clustering by topic ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Counterpoint: Roi Zalta argues plain or agentic RAG covers ~99% of needs and is easy to evaluate with domain experts ([[episodes/ai-engineering-podcast--company-brain]]).

## Disagreements & open questions
- Roi Zalta sees RAG as sufficient in ~99% of cases ([[episodes/ai-engineering-podcast--company-brain]]), versus Dana Maman's effort to avoid RAG entirely.
- Whether to move to RAG past ~100 sources: recommended by some, but RAG makes mistakes too; Dana is trying to avoid it ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).

## Takeaways
- [ ] Make your agent generate 3 query guesses and rank 3–4 candidates before answering from the wiki ([[episodes/osim-tochna--second-brain-and-llm-wiki]])

## Related
[[concepts/llm-wiki]] · [[concepts/context-engineering]] · [[concepts/rag]]
