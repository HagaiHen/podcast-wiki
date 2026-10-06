---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# Multi-Agent Orchestration

**Summary:** An orchestrator agent breaks a complex task into sub-tasks and routes each to a specialized agent that executes with its own tools. Its sole job is decomposition and delegation, so it's trained and tuned differently. Benefits: context isolation and focus, with promising quality gains in domains like healthcare. Pitfalls: agents whose scopes overlap in unforeseen ways, and capability descriptions that go stale as agents gain tools. Expect models to be trained to delegate, as they're now trained to use CLIs.

## Key ideas
- "Orchestrator" barely came up for a year, then returned at re:Invent 2025 ([[episodes/langtalks--58-reinvent-predictions]], [[people/shuki-cohen]]).
- Overlap between agents confuses routing; descriptions of what each agent can do drift out of date as tools are added ([[episodes/langtalks--58-reinvent-predictions]]).
- Context isolation per agent improves accuracy ([[episodes/langtalks--58-reinvent-predictions]]).
- Coding leads: structure plus existing reliability tools (compilers, linters). Claude Code lets users define subagents rather than shipping opinionated built-ins; consolidation and built-in agents may follow ([[episodes/langtalks--58-reinvent-predictions]]).
- Autonomous agents are moving from broad "AI teammate" ambitions (the Devin wave) to narrow niches, with an orchestrator over many specialists, possibly the path to AGI ([[episodes/langtalks--58-reinvent-predictions]]).

## Disagreements & open questions

## Takeaways
- [ ] Keep each sub-agent's capability description auto-generated from its actual tools so the orchestrator stays current ([[episodes/langtalks--58-reinvent-predictions]])

## Related
[[concepts/harness-engineering]] · [[concepts/small-language-models]] · [[concepts/autonomous-agents-outlook]]
