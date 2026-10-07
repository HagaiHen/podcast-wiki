---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-07
---
# AI Engineering Metrics (measuring coding-agent impact)

**Summary:** If you can't measure it, you can't improve it. Classic engineering metrics (PR cycle time, review time, DORA) are built on metadata and blind to context and complexity: a frontend team shipping five features a week can't be compared with a backend team shipping two a month. With GenAI, the content itself (code, git blame, tickets, agent events) is analyzable, enabling per-commit attribution of AI use. A three-layer framework: **adoption**, **productivity** (with versus without AI), and **quality** (does AI-assisted code survive in production?).

## Key ideas
- Stage zero: measure baseline engineering productivity regardless of AI (e.g. DORA) ([[episodes/langtalks--64-ai-coding-metrics]], [[people/liad-elidan]]).
- Attribution: know which commit or PR used Cursor, Copilot, or Claude Code (autonomously or not), via a data lake aggregating Git, Jira, CI/CD, and agent telemetry ([[episodes/langtalks--64-ai-coding-metrics]]).
- Adoption: who uses which tools and features (autocomplete, chat, agentic chat), and how often. Productivity gains only mean something with real adoption ([[episodes/langtalks--64-ai-coding-metrics]]).
- Productivity: compare a developer's PRs with and without AI on cycle, coding, and review time ([[episodes/langtalks--64-ai-coding-metrics]]).
- Quality: *code survival / longevity*. Trace bug-fix PRs via git blame to the lines they changed, then check whether those were AI-assisted, to see whether AI correlates with more bugs ([[episodes/langtalks--64-ai-coding-metrics]]).
- Usage versus utilization: logging in daily differs from *how* it's used. Go deeper with the percent of PR code AI-generated, PRs reviewed by custom agents, and whether buggy lines came from planned, spec-driven sessions or a quick phone session ([[episodes/langtalks--64-ai-coding-metrics]]).
- If a developer's agents rarely use the internal MCP and their bug rate is high, that's concrete coaching feedback ([[episodes/langtalks--64-ai-coding-metrics]]).
- "Cursor vs Claude Code?" is answerable per org only with these metrics ([[episodes/langtalks--64-ai-coding-metrics]]).
- Token usage per developer as an adoption metric: it shows usage, not quality, and can reward junk code or wasted context. Gong is still deciding between time-to-maturity of features, bug counts, and refactoring capability ([[episodes/osim-tochna--gong-ai-for-developers]], [[people/ohad-parush]]).

## Disagreements & open questions

## Takeaways
- [ ] Measure baseline engineering productivity before attributing changes to AI ([[episodes/langtalks--64-ai-coding-metrics]])
- [ ] Track code survival of AI-assisted vs human code via git blame and bug-fix PRs ([[episodes/langtalks--64-ai-coding-metrics]])
- [ ] Check whether bug-prone code came from spec-driven sessions and used internal tools ([[episodes/langtalks--64-ai-coding-metrics]])

## Related
[[concepts/ai-sdlc]] · [[concepts/llm-cost-optimization]] · [[concepts/llm-evals]]
