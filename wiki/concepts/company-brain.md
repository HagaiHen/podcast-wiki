---
type: concept
hubs: [knowledge-management, ai-engineering]
sources: 2
updated: 2026-10-07
---
# Company Brain

**Summary:** A shared organizational knowledge layer (a Y Combinator "call for startups" idea) that every agent connects to, reads, and writes memory into, while humans share context through it. Agents are its main consumers; its value is measured in money, through the loops it makes possible. As of the episode it isn't a solved problem even at team level. The technology mostly exists, but continuously syncing sources and resolving contradictions is expensive. A practical stack has four layers: factual memory, human communication (the "missing why"), a context-graph ontology, and governed actions.

## Key ideas
- Definition: the org's shared knowledge in one place, accessible to agents (often via MCP/API); success = how well agents get context ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Example: Cerebras built an organizational "knowledge layer" every employee's agent reaches via MCP, doing agentic RAG over all sources and even routing to human SPOCs ([[episodes/ai-engineering-podcast--company-brain]]).
- Teams that indexed *everything* (all sources, code as source of truth) found it too general. Moving to team-level context, then to layers, made the big jump ([[episodes/ai-engineering-podcast--company-brain]]).
- Layer 1, factual memory: meetings, Slack/Teams, email (more formal, so more trusted), docs (official > personal) ([[episodes/ai-engineering-podcast--company-brain]]).
- Layer 2, the "missing why": decisions, commitments, and reasons, often made in hallways and meetings, rarely recorded. Capturing them is the context-building agent's job ([[episodes/ai-engineering-podcast--company-brain]]).
- Layer 3, context-graph reasoning: an ontology of actors, interactions, time, rationales, and dependencies (see [[concepts/knowledge-graphs]]) ([[episodes/ai-engineering-podcast--company-brain]]).
- Layer 4, governed actions: loops that create value, e.g. onboarding a new C-level in weeks, not six months, or telling each customer which shipped feature they asked for two years ago ([[episodes/ai-engineering-podcast--company-brain]]).
- Ontology lenses: the same event means a feature gap to a PM and a churn signal to finance; the brain should inject role context into each agent's queries ([[episodes/ai-engineering-podcast--company-brain]]).
- Humans are knowledge nodes: the brain should know that some knowledge only lives with "the IT guy" and route the agent to ask him ([[episodes/ai-engineering-podcast--company-brain]]).
- Authority weighting: naive approaches trust C-level over junior employees; better to weight by information type (a developer outranks the CEO on code) and by usage ([[episodes/ai-engineering-podcast--company-brain]]).
- Maybe the center shouldn't be the company but its customers ([[episodes/ai-engineering-podcast--company-brain]]).
- Domain-expert knowledge, not frontier models, is the durable edge (Satya Nadella, as cited) ([[episodes/ai-engineering-podcast--company-brain]]).
- Wonderful's internal "Wonder" agent connects to Drive, calendars, public Slack, Salesforce, the product, and Snowflake so nobody asks colleagues factual questions. It ranges from "why is prod broken?" to cross-data research (e.g. FDE background vs delivery speed); next step: taking actions ([[episodes/ignore-instructions--24-wonderful-road-to-100m]], [[people/roy-lazar]]).

## Disagreements & open questions
- Who builds it? Agents will build the brain that gives agents context, so whose context builds it? Humans may lose the ability to read or audit the org's context ([[episodes/ai-engineering-podcast--company-brain]]).

## Takeaways
- [ ] Start from a concrete business use case and map its data sources before building a company brain ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Build team-level context before attempting company-wide ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Capture the "missing why": record decisions with their reasons ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Weight sources by type and authority (email > chat; official docs > personal notes) ([[episodes/ai-engineering-podcast--company-brain]])

## Related
[[concepts/rag]] · [[concepts/memory-consolidation]] · [[concepts/knowledge-graphs]] · [[concepts/personal-ai-os]] · [[concepts/llm-wiki]] · [[concepts/enterprise-ai-adoption]]
