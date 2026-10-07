---
type: concept
hubs: [knowledge-management, ai-engineering]
sources: 4
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
- Early-stage teams generate "shadow data" (customer meetings, Slack and WhatsApp threads, hallway and late-night architecture debates) that matters most precisely when there's no product yet ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- monday's Harmony team brain: every member's machine runs a Claude skill every ~30 minutes that pulls new items via their own MCPs (note-taker, Slack, WhatsApp, docs), updates a shared git wiki, and pushes, so each person is a node and the brain stays alive without per-person workflows ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Delivery surfaces: a Wikipedia-style site for morning reading, the repo inside Cursor or Claude for builders, Figma MCP plus the brain for designers, and a WhatsApp agent for anyone, including people on vacation or reserve duty ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Results: a vision deck for the CEO in hours instead of weeks; Google Ads messaging written by Claude from the brain, which knows more than any single member; alignment across product and go-to-market without extra syncs. Next: autonomous per-discipline agents built on top of the brain ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Culture shift: meetings without the note-taker became "unheard of", and the team even records in-person conversations ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Claroty's agentic assistant "Clar" was built after an internal tour collecting best practices from different departments, so the model reflects the company's cumulative expertise and can take operational actions, not just report ([[episodes/hidden-layers--claroty-ben-mashiach]], [[people/ben-mashiach]]).

## Disagreements & open questions
- Total transparency, bug or feature? Everything recorded or written becomes visible to the whole team; the guest now sees it as a feature ("everyone knows everything"), while acknowledging people still want to gossip in meetings and must switch the note-taker off to do so ([[episodes/startup-for-startup--353-self-updating-team-brain]]).
- Who builds it? Agents will build the brain that gives agents context, so whose context builds it? Humans may lose the ability to read or audit the org's context ([[episodes/ai-engineering-podcast--company-brain]]).

## Takeaways
- [ ] Start from a concrete business use case and map its data sources before building a company brain ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Build team-level context before attempting company-wide ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Capture the "missing why": record decisions with their reasons ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Weight sources by type and authority (email > chat; official docs > personal notes) ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Prototype a team brain locally (note-taker + Slack MCPs into a small git wiki) before automating it ([[episodes/startup-for-startup--353-self-updating-team-brain]])

## Related
[[concepts/rag]] · [[concepts/memory-consolidation]] · [[concepts/knowledge-graphs]] · [[concepts/personal-ai-os]] · [[concepts/llm-wiki]] · [[concepts/enterprise-ai-adoption]] · [[concepts/llm-wiki]]
