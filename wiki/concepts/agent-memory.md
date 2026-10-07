---
type: concept
hubs: [ai-engineering, knowledge-management]
sources: 4
updated: 2026-10-07
---
# Agent Memory (short- and long-term, governed)

**Summary:** Memory is a frontier problem for agents, especially coding agents, which must follow a team's practices consistently. *Short-term* memory keeps a long session faithful to its early instructions; *long-term* memory holds personal preferences, repo conventions, org practices, and non-technical context (Slack, PRDs). Natural-language files keep it inspectable, but you need a lifecycle: creation, retrieval at the right moment, and *evidence of value*. Governance (usage and acceptance stats, whose feedback counts) is what tools lack most.

## Key ideas
- Memory dimensions: short vs long term; personal, team, company; updating vs static; transparent vs opaque ([[episodes/langtalks--57-memory]], [[people/itamar-friedman]]).
- Hierarchy: personal memory → repo memory (CLAUDE.md/AGENTS.md, committed) → org practices (architecture, testing; often in Notion) → non-technical context (Slack threads, PRDs via MCP) ([[episodes/langtalks--57-memory]]).
- Natural-language memory is preferable for now because it's controllable; you can see and veto what was learned ([[episodes/langtalks--57-memory]]).
- Three-part framework: how a rule is created (human, machine, or both), when it's retrieved, and whether it's valuable. If a rule fired 100 times and developers accepted the result 80 times, keep it; otherwise change or delete it ([[episodes/langtalks--57-memory]]).
- Ingestion design: avoid both extremes ("encode everything into one format" and "only index where things live"). Ingest and encode per media type (logs, PR discussions, diagrams) with references back to sources, give agents memory tools per type, and route between them ([[episodes/langtalks--57-memory]]).
- Learning governance: should one senior's repeated comment become a rule? Juniors versus seniors, outliers, positive and negative learning ([[episodes/langtalks--57-memory]]).
- Mem0's MCP gives add, search, update, delete; plus multimodal memories (UI screenshots, architecture diagrams), graph modeling, timestamps with expiry, and usefulness feedback. That's ~80% of the plumbing, not the intelligence ([[episodes/langtalks--57-memory]]).
- Merging parallel agent sessions needs their *intent* (in the sessions), not just their code ([[episodes/langtalks--57-memory]]).
- Cold start: backfill (e.g. 12 months of GitHub discussions) rather than only learning going forward ([[episodes/langtalks--57-memory]]).
- Good memory also cuts tokens and cost; it's context engineering of the future ([[episodes/langtalks--57-memory]]).
- Start with the file system before a vector DB: most agent work is episodic, so files for PRDs, plans, and to-dos give persistence, git history, and human review; semantic memory retrieval is rarely the first or second thing you need ([[episodes/langtalks--55-context-engineering]]).
- Claude Code memory levels: project, user, enterprise ([[episodes/langtalks--55-context-engineering]]).
- Critique of memory systems: retrieval, memory graphs, and summarization only choose which notes to re-read from an ever-growing stack, like an employee rereading all their notes each morning. The problem is ill-posed because data isn't distilled as it arrives. Humans change a little with every input ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Two layers for a domain agent: a constantly enriched data layer (what permissions actually allow) and a knowledge layer of org policies and exceptions ("never auto-disable the CEO"), learned from every interaction so customers needn't repeat themselves ([[episodes/hidden-layers--twine-nadav-erez]], [[people/nadav-erez]]).

## Disagreements & open questions
- Bitter lesson (scale data and compute) versus algorithmic innovation: Friedman expects new memory architectures; the hosts sense today's memory is feature engineering awaiting a learned solution ([[episodes/langtalks--57-memory]]).

## Takeaways
- [ ] Track each rule's usage and acceptance rate and prune rules that don't earn their place ([[episodes/langtalks--57-memory]])
- [ ] Ingest memory per source type with links back to originals instead of one giant encoding ([[episodes/langtalks--57-memory]])
- [ ] Backfill memory from historical PR discussions to avoid cold start ([[episodes/langtalks--57-memory]])
- [ ] Use files (PRD, plan, to-do) as the agent's working memory before building a vector memory ([[episodes/langtalks--55-context-engineering]])

## Related
[[concepts/memory-consolidation]] · [[concepts/human-vs-ai-memory]] · [[concepts/context-engineering]] · [[concepts/company-brain]] · [[concepts/continual-learning]]
