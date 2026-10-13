---
type: concept
hubs: [ai-engineering]
sources: 8
updated: 2026-10-13
---
# Multi-Agent Orchestration

**Summary:** An orchestrator agent breaks a complex task into sub-tasks and routes each to a specialized agent that executes with its own tools. Its sole job is decomposition and delegation, so it's trained and tuned differently. The simplest form is a builder/checker pair, which tools like OpenRig wire up so you stop copying results between chat windows by hand. Benefits: context isolation and focus, with promising quality gains in domains like healthcare. Pitfalls: agents whose scopes overlap in unforeseen ways, and capability descriptions that go stale as agents gain tools. Expect models to be trained to delegate, as they're now trained to use CLIs.

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
- "Sous-chef" decomposition: an orchestrator draws on a company knowledge base of how expert researchers approach a task, breaks it into steps, dispatches them to specialized agents, and an aggregator draws the conclusion. Dream reuses this pattern well beyond cyber ([[episodes/hidden-layers--dream-eran-hoffman]], [[people/eran-hoffman]]).
- Risk moves to the connections: in orchestrated multi-agent workflows each agent may be safe and correctly permissioned alone, while the links between them open new paths ([[episodes/hidden-layers--tenable-tom-barnea]], [[people/tom-barnea]]).
- Builder + checker: OpenRig organizes Claude Code and Codex agents into a team, one making a change and another checking it, with a way to pass work between them. It pays off once you're the one copying output into a second chat for review and carrying feedback back. Its two-agent starter needs Mac or Linux with Node and tmux ([[episodes/startup-ideas--8-github-repos-viral-money]], [[people/greg-isenberg]]).

## Disagreements & open questions
- Hosts' caution: most successful agents in practice are *single* agents with narrow helper sub-agents (e.g. answer a question from one document), not full multi-agent systems ([[episodes/langtalks--55-context-engineering]]).
- One agent with skills, or a team of specialist agents? Billy Howell builds a chief-of-staff agent that spins out dedicated agents per task, and the LangTalks hosts see orchestrators over many specialists as the direction ([[episodes/startup-ideas--grok-bot-one-person-company]], [[people/billy-howell]], [[episodes/langtalks--58-reinvent-predictions]]). Vega and Twine went the other way: per-alert workflows and per-page agents broke, and a single agent selecting skills improved evals ([[episodes/hidden-layers--vega-gili-kanfo]], [[people/gili-kanfo]], [[episodes/hidden-layers--twine-nadav-erez]], [[people/nadav-erez]]).

## Takeaways
- [ ] Keep each sub-agent's capability description auto-generated from its actual tools so the orchestrator stays current ([[episodes/langtalks--58-reinvent-predictions]])
- [ ] Add a five-line daily brief (done / blocked / needs me) to each recurring agent ([[episodes/startup-ideas--grok-bot-one-person-company]])
- [ ] Try a builder + checker agent pair on a small job (e.g. a quote calculator checked against real pricing) in a test project ([[episodes/startup-ideas--8-github-repos-viral-money]])

## Related
[[concepts/harness-engineering]] · [[concepts/small-language-models]] · [[concepts/autonomous-agents-outlook]]
