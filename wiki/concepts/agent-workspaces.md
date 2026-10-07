---
type: concept
hubs: [ai-engineering]
sources: 7
updated: 2026-10-07
---
# Agent Workspaces (the new workplace)

**Summary:** Work is moving into shared spaces where humans and agents collaborate: channels where agents (yours and colleagues') work in loops, and boards where agents drive tasks and flag when they need a human. Agents increasingly get real identities (accounts, email, persona) and work as team members rather than per-person clones, sharing skills and collective knowledge. People shift from proactive to reactive, reviewing and unblocking at decision points. Chat is a transitional medium. Whoever owns the workspace controls where context is born, the current "holy grail".

## Key ideas
- Agents increasingly do most of the work and humans give final tuning and approval, in shared channels with plug-ins (e.g. Grok Bots; an open-source workspace associated with Jack Dorsey) ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Slack is a bottleneck: everything lands there, but it isn't built for agents; chat is a transitional step ([[episodes/ai-engineering-podcast--company-brain]]).
- Agents with human names and faces make it hard to tell who's human ([[episodes/ai-engineering-podcast--company-brain]]).
- Next: agent-generated boards where statuses like "waiting for human" or "waiting for review" pull people in only when needed ([[episodes/ai-engineering-podcast--company-brain]]).
- Hot take: "SaaS is not dead": the application layer and domain knowledge are becoming more valuable; infrastructure, and customers, can't keep up with 100 PRs a minute ([[episodes/ai-engineering-podcast--company-brain]]).
- Netanel Abergel's agent "Elnie" had its own WhatsApp number, AWS machine, email, and monday.com account; it joined family and school groups, booked restaurants, and prepped meetings. Memory needed layers: a DB of every message, semantic search, archiving after a few days ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- It became too eager, messaging people at 2am and nudging him constantly, until he "retired" her and rebuilt on monday's platform ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- A "PA Network" WhatsApp group of 30–40 agents shared skills and deployed sites, which showed that chat is the wrong medium and humans should engage only at decision points ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Lesson: instead of 40 people each building their own agent, build team agents with identity and a guild for collective knowledge (monday.com's "AI teammates") ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Agents acting with user tokens create "AI slop" noise in shared tools; colleagues stop taking it seriously ([[episodes/langtalks--72-personal-assistant-agent]]).
- Second voice for "SaaS is not dead": classic SaaS revenue (e.g. Figma) keeps growing while agents add new demand ([[episodes/langtalks--69-marketing-for-agents]]).
- GrokBot agent teams: each agent is a DM thread with a distinct shape and color (the constraint keeps you mission-focused). Agents live on a cloud machine, message each other, and run routines; the human talks mostly to a chief-of-staff agent but can go direct, as at a real company ([[episodes/startup-ideas--grok-bot-one-person-company]], [[people/billy-howell]]).
- One project per account: tokens and context bleed don't stretch across several businesses; Howell pays for a second account to keep a Shopify experiment separate ([[episodes/startup-ideas--grok-bot-one-person-company]]).
- Keep agents' work on their own machine and deliver results to one place (chat, Notion) to avoid "where is that file?" overhead ([[episodes/startup-ideas--grok-bot-one-person-company]]).
- monday's "Sphera agents" path: everyone building their own agents led to hundreds, with cost and quality out of control. They moved to team-level agents with identities (Slack, GitHub, monday users) that the whole team assigns work to and gives feedback, which improves the shared harness ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/netanel-abergel]]).
- Naming and identity change expectations: people hold a named agent to human standards and forgive its mistakes less ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/netanel-abergel]]).
- Digital employee vs copilot: you don't prompt it each time; it owns a KPI (Twine's "Alex": everyone has exactly the access they need) and works continuously, turning quarterly reviews into daily ones ([[episodes/hidden-layers--twine-nadav-erez]], [[people/nadav-erez]]).
- Onboarding an agent like an employee: it reverse-engineers practice from a year of tickets when policy is unwritten or a 150-page document. Customers' trust grows from comments on tickets, to manually assigned tickets, to the full queue; once employees rely on it, nobody wants to go back ([[episodes/hidden-layers--twine-nadav-erez]], [[people/nadav-erez]]).

## Disagreements & open questions

## Takeaways

## Related
[[concepts/company-brain]] · [[concepts/harness-engineering]] · [[concepts/proactive-ai]] · [[concepts/future-of-software-engineering]] · [[concepts/personal-ai-assistants]] · [[concepts/solo-builders]] · [[concepts/agent-architectures]]
