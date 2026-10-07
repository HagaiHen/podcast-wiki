---
type: concept
hubs: [ai-engineering]
sources: 3
updated: 2026-10-07
---
# Multi-Agent Orchestration

**Summary:** An orchestrator agent breaks a complex task into sub-tasks and routes each to a specialized agent that executes with its own tools. Its sole job is decomposition and delegation, so it's trained and tuned differently. Benefits: context isolation and focus, with promising quality gains in domains like healthcare. Pitfalls: agents whose scopes overlap in unforeseen ways, and capability descriptions that go stale as agents gain tools. Expect models to be trained to delegate, as they're now trained to use CLIs.

## Key ideas
- "Orchestrator" barely came up for a year, then returned at re:Invent 2025 ([[episodes/langtalks--58-reinvent-predictions]], [[people/shuki-cohen]]).
- Overlap between agents confuses routing; descriptions of what each agent can do drift out of date as tools are added ([[episodes/langtalks--58-reinvent-predictions]]).
- Context isolation per agent improves accuracy ([[episodes/langtalks--58-reinvent-predictions]]).
- Coding leads: structure plus existing reliability tools (compilers, linters). Claude Code lets users define subagents rather than shipping opinionated built-ins; consolidation and built-in agents may follow ([[episodes/langtalks--58-reinvent-predictions]]).
- Autonomous agents are moving from broad "AI teammate" ambitions (the Devin wave) to narrow niches, with an orchestrator over many specialists, possibly the path to AGI ([[episodes/langtalks--58-reinvent-predictions]]).
- Chief-of-staff pattern: start with one manager agent that audits the business and proposes the first three agents. Have it do each task once, review, then spin it out into a dedicated agent with a goal. Add agents only when mission-critical ([[episodes/startup-ideas--grok-bot-one-person-company]], [[people/billy-howell]]).
- Routines: each agent sends a five-line end-of-day brief (done, blocked, needs you) to the chief of staff, which summarizes for the human ([[episodes/startup-ideas--grok-bot-one-person-company]]).
- Adversarial review panel: have sub-agents critique a work product in three rounds, taking output from ~50% to ~90% done; turn your own feedback into a review skill ([[episodes/startup-ideas--grok-bot-one-person-company]]).
- Four-week ramp: build the team → execute with no tinkering → hire and fire agents → automate ([[episodes/startup-ideas--grok-bot-one-person-company]]).

## Disagreements & open questions
- Hosts' caution: most successful agents in practice are *single* agents with narrow helper sub-agents (e.g. answer a question from one document), not full multi-agent systems ([[episodes/langtalks--55-context-engineering]]).

## Takeaways
- [ ] Keep each sub-agent's capability description auto-generated from its actual tools so the orchestrator stays current ([[episodes/langtalks--58-reinvent-predictions]])
- [ ] Add a five-line daily brief (done / blocked / needs me) to each recurring agent ([[episodes/startup-ideas--grok-bot-one-person-company]])

## Related
[[concepts/harness-engineering]] · [[concepts/small-language-models]] · [[concepts/autonomous-agents-outlook]]
