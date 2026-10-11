---
type: concept
hubs: [ai-engineering]
sources: 5
updated: 2026-10-11
---
# Agent-Ready Codebase

**Summary:** Converting a project or team so an agent can understand and operate it like a human developer: product and organizational knowledge available as files, documented interfaces and testing methods, and infrastructure the agent can spin up by itself. The knowledge base is seeded from everything the org already has (infra code, Confluence, old docs) into a shared repo, so every new hire's agent starts with years of context, and it grows as agents record what they learn in sessions. Breadth of context beats perfect accuracy: wrong entries can be fixed like any documentation. Greenfield projects can be built this way from day one; existing ones must be migrated.

## Key ideas
- Give the agent the project's *why*: PRDs, roadmap, plans, even before any code exists ([[episodes/langtalks--73-harness-engineering]]).
- Files beat an MCP to Jira/Linear: with an MCP the agent must guess when to look and often won't; a folder of docs plus a prompt explaining each file is far more natural ([[episodes/langtalks--73-harness-engineering]]).
- Option: a docs/ folder (PRDs, product concepts, security concepts, DB schema), or skills (how to test, end-to-end testing, system interfaces, product-design concepts) ([[episodes/langtalks--73-harness-engineering]]).
- Put *when to update* in each skill's description, since descriptions always sit in context. The agent then proposes updates, e.g. after a test failure or a newly found interface ([[episodes/langtalks--73-harness-engineering]]).
- Shared staging breaks constantly in growing orgs. Give each developer, and each agent, an isolated environment it can launch via CLI, decoupled from the machine it codes on ([[episodes/langtalks--73-harness-engineering]]).
- Pitfall: grabbing a popular skill (e.g. a code-reviewer with 100k GitHub stars) is a fine start, but the value is in custom skills encoding *your* deployment, design principles, tests, and team review norms ([[episodes/langtalks--73-harness-engineering]]).
- The host adapted Superpowers' visual planning: deep, comprehensive HTML plans (even if they take 30 min) reviewed via a custom Chrome extension for in-browser comments, fed back as Markdown, to batch decisions and cut context switching across 6–7 parallel sessions ([[episodes/langtalks--73-harness-engineering]]).
- Keep a docs folder of markdown inside the repo maintained by workflows. A one-off generator (e.g. DeepWiki) only describes current code, while decisions made in sessions need capturing; Claude Code memory scatters them ([[episodes/langtalks--68-ai-sdlc]]).
- Make the repo AI-ready for review: have an agent describe the existing architecture, agree on it once, and from then on get alerts when a change breaks it ([[episodes/hidden-layers--qodo-itamar-friedman]], [[people/itamar-friedman]]).
- Seed it from every source: Cato's team let an agent read the infrastructure code and all their knowledge bases (Confluence, old-school docs) and pushed the result as rules and skills into a shared repo. Every new employee's agent now has the org's accumulated knowledge built in, and guides its operator back: which checks to run after a push, which environments exist ([[episodes/hidden-layers--cato-networks-avishai-zvinsky]], [[people/avishai-zvinsky]]).
- The wider *why* matters more than syntax the agent can infer itself: why we write protections, the deployment cycle, when a change reaches production, who to ask when stuck ([[episodes/hidden-layers--cato-networks-avishai-zvinsky]], [[people/avishai-zvinsky]]).
- Let the agent write its own skills: after a conversation that reached conclusions it hadn't inferred, say "document everything new to you in skills and rules" and commit it. Zvinsky urges his team to do this freely, preferring plenty of context over worrying it might be wrong; like old docs, anyone can edit and fix it. The host likens this to evolution or human memory: what's useful survives, the rest fades out ([[episodes/hidden-layers--cato-networks-avishai-zvinsky]], [[people/avishai-zvinsky]]).

## Disagreements & open questions
- How much context to give: Zvinsky prefers a large, freely agent-written body of skills and rules, fixing errors as they appear ([[episodes/hidden-layers--cato-networks-avishai-zvinsky]]); Bleiberg argues every context item costs tokens and attention, so inject only what evals show the model gets wrong and load the rest progressively ([[episodes/startup-for-startup--354-reliable-agents-lean-context]]). Progressive skill loading may reconcile the two.

## Takeaways
- [ ] Put product docs (PRDs, roadmap, concepts) as files in the repo, with an index prompt explaining each ([[episodes/langtalks--73-harness-engineering]])
- [ ] Add "when to update this skill" to every skill description ([[episodes/langtalks--73-harness-engineering]])
- [ ] Let agents launch isolated per-branch environments with one CLI command ([[episodes/langtalks--73-harness-engineering]])
- [ ] Write custom skills for your org's deploy, design, test, and review norms instead of relying on popular generic ones ([[episodes/langtalks--73-harness-engineering]])
- [ ] After a session that taught the agent something new, ask it to record the lessons as skills or rules and commit them ([[episodes/hidden-layers--cato-networks-avishai-zvinsky]])

## Related
[[concepts/harness-engineering]] · [[concepts/context-engineering]] · [[concepts/ai-guardrails]] · [[concepts/ai-sdlc]] · [[concepts/agentic-vulnerability-response]]
