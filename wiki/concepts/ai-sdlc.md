---
type: concept
hubs: [ai-engineering]
sources: 6
updated: 2026-10-08
---
# AI-SDLC (agents across the dev lifecycle)

**Summary:** Running the software lifecycle with agent teams, from product idea to PRD, task breakdown, implementation, review, and QA, with existing artifacts (Jira tickets, PRDs, PRs, tests) as the source of truth and humans placed deliberately at feedback points. Two automation types: *passive* flows triggered by events (errors in logs, support tickets, code review) and the *core* flow of team requirements moving to remote execution. Fire-and-forget remote agents fail; they need evals, self-testing tools, guardrails, and memory. When they work (~15% of monday's PRs come from remote agents), the bottleneck moves from writing code to reviewing it, and fixed two-week sprints stop fitting. Most orgs are at "level 1"; start with one concrete problem at the edges and fix dev infrastructure first.

## Key ideas
- First questions: what's the source of truth, and where and how do humans give feedback ([[episodes/langtalks--68-ai-sdlc]], [[people/yonatan-maor]])?
- PRD stage: an agent takes a terse problem description, researches, asks product questions asynchronously, and drafts the PRD; mocks become live demos in staging using the org's design system ([[episodes/langtalks--68-ai-sdlc]]).
- Breakdown: an agent session reads the PRD against the codebase, routes technical gaps to a tech lead (e.g. via Slack), and produces subtasks with definitions of done and files to touch, written back to Jira ([[episodes/langtalks--68-ai-sdlc]]).
- Ownership creates healthy tension: product owns the PRD skill, the engineering lead owns breakdown and can push back on the product agent ([[episodes/langtalks--68-ai-sdlc]]).
- Routing by blast radius: one line in auth may need human eyes, while 100 low-risk lines may not. Complexity also decides whether a plan is required. SRE-type fixes such as reverts can ship without human review ([[episodes/langtalks--68-ai-sdlc]]).
- Adoption friction: making developers decide upfront between remote and local execution failed; mid-flow gates where they can steer, and easy handoff to local work, help ([[episodes/langtalks--68-ai-sdlc]]).
- Start at the edges: bug triage, on-call investigation and routing; the core flow is mentally harder because developers sign off on that work ([[episodes/langtalks--68-ai-sdlc]]).
- Measuring the AI-SDLC needs a data lake joining Git, Jira, CI/CD, and agent telemetry; see [[concepts/ai-engineering-metrics]] ([[episodes/langtalks--64-ai-coding-metrics]]).
- A detailed spec is a *contract* between developer, machine, and product. Then a tech design grounded in repo context, then task breakdown. Don't jump from PRD to implementation ([[episodes/langtalks--62-ai-rd-rollout]], [[people/iko-azoulay]]).
- Spec review as a ritual: engineers bring an AI-refined spec back to product, mixing technical decisions into requirements early ([[episodes/langtalks--62-ai-rd-rollout]]).
- Next: product creates working-mock PRs on real data (tools like Autonomy AI); hierarchical, cross-repo context, since most features span 3–4 repos; less rigid, more interactive artifacts, because huge generated specs go unread ([[episodes/langtalks--62-ai-rd-rollout]]).
- Scrum rituals (dailies, retros, sprints) will change when agents do most of an epic ([[episodes/langtalks--62-ai-rd-rollout]]).
- Personas outside R&D can now skip lifecycle stages (product prototyping, ops building their own automations): great for prototypes and internal tools, risky for production ([[episodes/langtalks--56-n8n]]).
- For complex software, more AI-written code brings more production bugs and less shared understanding, so leading companies apply AI across the whole SDLC (review, testing, governance) rather than celebrating generation alone ([[episodes/hidden-layers--qodo-itamar-friedman]], [[people/itamar-friedman]]).
- Putting Claude Code in the cloud and throwing tasks at it failed: coding is never one-shot, and the agent produced thousands of terrible PRs nobody wanted to review ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])
- ~15% of monday's PRs are written and merged by *remote* agents (not local Claude Code or Cursor), and ~50% of agent PRs reach production with no human commit ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])
- The bottleneck moved from writing code to reviewing it: "we started working for the agents", which doesn't scale without trusted automated checks ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])
- Sprints are obsolete when execution time collapses and agents share the board: Brook's team dropped two-week sprints for kanban while still committing to deadlines and deliverables ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])
- Next steps: auto-merge with no human in the loop, then "agentic release", where agents run feature-flag rollouts and rollbacks up to the customer ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/netanel-abergel]])
- Where to start: one concrete, simple problem such as the bug-duty rotation; add control mechanisms and guardrails, prove it works, then deepen each part and expand to harder problems ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])

## Disagreements & open questions
- Org knowledge and skill sharing remain unsolved; every team does it differently ([[episodes/langtalks--68-ai-sdlc]]).

## Takeaways
- [ ] Define your SDLC source of truth and human feedback points before automating ([[episodes/langtalks--68-ai-sdlc]])
- [ ] Start with peripheral flows: bug triage, on-call investigation ([[episodes/langtalks--68-ai-sdlc]])
- [ ] Route agent tasks to human review by blast radius, not line count ([[episodes/langtalks--68-ai-sdlc]])
- [ ] Start agent adoption with one concrete problem (e.g. bug duty) and its guardrails before expanding ([[episodes/ai-engineering-podcast--atlas-ai-teammate]])

## Related
[[concepts/harness-engineering]] · [[concepts/ai-verification]] · [[concepts/skill-engineering]] · [[concepts/agent-ready-codebase]] · [[concepts/ai-engineering-metrics]] · [[concepts/ai-rd-rollout]] · [[concepts/workflow-automation]] · [[concepts/agent-workspaces]] · [[concepts/ai-guardrails]]
