---
type: concept
hubs: [knowledge-management, ai-engineering]
sources: 2
updated: 2026-10-07
---
# LLM Wiki (Karpathy pattern)

**Summary:** A knowledge-base pattern published by [[people/andrej-karpathy]] (in April, reaching ~20M views) in which an LLM, not the human, maintains the knowledge: it stores, connects, updates, and checks for contradictions, so the value compounds the more you use it. Three layers: **raw** sources kept unchanged as the source of truth, a **wiki** of digested concepts and links, and a **schema** (often just a CLAUDE.md/AGENTS.md) with the rules for ingesting, using, and maintaining it. Karpathy suggested it fits up to ~100 sources; beyond that, retrieval needs more care.

## Key ideas
- Raw is "the dump": transcripts and clippings, rarely accessed directly; the wiki is the clean, digested layer ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Its biggest value is the connections between pieces of information ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Your own outputs count as sources too: notes, summaries, conversation logs, articles you wrote. Otherwise the AI won't cite them ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Start simple per Karpathy (sources / wiki / schema) and restructure freely as needs emerge; Dana restarted several times ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- Rated suitable for ~100 sources; past that, see [[concepts/wiki-retrieval]] ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- Team adoption: monday's Harmony team applied the pattern to a 20-person org. The key difference from RAG is persistence: a librarian who remembers yesterday's question. Useful answers (e.g. a competitor pricing table a PM researched) are written back, so the next question needs no re-research ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Their schema: concepts, domains, entities (companies, people by role), decisions, and action items, all interlinked; one meeting can update 15 pages. Raw items are stored so nothing is re-processed (saves tokens) ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Advice: start with basic, manual, local versions to prove value, before cloud CI and scale ("bicycle before car") ([[episodes/startup-for-startup--353-self-updating-team-brain]]).

## Disagreements & open questions
- File layout: Dana keeps Karpathy's flat three layers; Amit experimented with a tree by domain (research, engineering…) aimed at fast, correct lookup. Both agree it keeps getting reorganized ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).

## Takeaways
- [ ] After any restructure, ask the AI to verify system integrity: links and routines still work ([[episodes/osim-tochna--second-brain-and-llm-wiki]])

## Related
[[concepts/second-brain]] · [[concepts/wiki-retrieval]] · [[concepts/open-knowledge-format]] · [[concepts/knowledge-rot]] · [[concepts/company-brain]]
