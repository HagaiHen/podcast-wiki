---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# AI-SDLC (agents across the dev lifecycle)

**Summary:** Running the software lifecycle with agent teams, from product idea to PRD, task breakdown, implementation, review, and QA, with existing artifacts (Jira tickets, PRDs, PRs, tests) as the source of truth and humans placed deliberately at feedback points. Two automation types: *passive* flows triggered by events (errors in logs, Zendesk tickets, code review) and the *core* flow of team requirements moving to remote execution. Most orgs are at "level 1"; start small at the edges and fix dev infrastructure first.

## Key ideas
- First questions: what's the source of truth, and where and how do humans give feedback ([[episodes/langtalks--68-ai-sdlc]], [[people/yonatan-maor]])?
- PRD stage: an agent takes a terse problem description, researches, asks product questions asynchronously, and drafts the PRD; mocks become live demos in staging using the org's design system ([[episodes/langtalks--68-ai-sdlc]]).
- Breakdown: an agent session reads the PRD against the codebase, routes technical gaps to a tech lead (e.g. via Slack), and produces subtasks with definitions of done and files to touch, written back to Jira ([[episodes/langtalks--68-ai-sdlc]]).
- Ownership creates healthy tension: product owns the PRD skill, the engineering lead owns breakdown and can push back on the product agent ([[episodes/langtalks--68-ai-sdlc]]).
- Routing by blast radius: one line in auth may need human eyes, while 100 low-risk lines may not. Complexity also decides whether a plan is required. SRE-type fixes such as reverts can ship without human review ([[episodes/langtalks--68-ai-sdlc]]).
- Adoption friction: making developers decide upfront between remote and local execution failed; mid-flow gates where they can steer, and easy handoff to local work, help ([[episodes/langtalks--68-ai-sdlc]]).
- Start at the edges: bug triage, on-call investigation and routing; the core flow is mentally harder because developers sign off on that work ([[episodes/langtalks--68-ai-sdlc]]).

## Disagreements & open questions
- Org knowledge and skill sharing remain unsolved; every team does it differently ([[episodes/langtalks--68-ai-sdlc]]).

## Takeaways
- [ ] Define your SDLC source of truth and human feedback points before automating ([[episodes/langtalks--68-ai-sdlc]])
- [ ] Start with peripheral flows: bug triage, on-call investigation ([[episodes/langtalks--68-ai-sdlc]])
- [ ] Route agent tasks to human review by blast radius, not line count ([[episodes/langtalks--68-ai-sdlc]])

## Related
[[concepts/harness-engineering]] · [[concepts/ai-verification]] · [[concepts/skill-engineering]] · [[concepts/agent-ready-codebase]]
