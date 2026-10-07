---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-07
---
# Agent-Ready Codebase

**Summary:** Converting a project so an agent can understand and operate it like a human developer: product knowledge available as files, documented interfaces and testing methods, and infrastructure the agent can spin up by itself. Greenfield projects can be built this way from day one; existing ones must be migrated.

## Key ideas
- Give the agent the project's *why*: PRDs, roadmap, plans, even before any code exists ([[episodes/langtalks--73-harness-engineering]]).
- Files beat an MCP to Jira/Linear: with an MCP the agent must guess when to look and often won't; a folder of docs plus a prompt explaining each file is far more natural ([[episodes/langtalks--73-harness-engineering]]).
- Option: a docs/ folder (PRDs, product concepts, security concepts, DB schema), or skills (how to test, end-to-end testing, system interfaces, product-design concepts) ([[episodes/langtalks--73-harness-engineering]]).
- Put *when to update* in each skill's description, since descriptions always sit in context. The agent then proposes updates, e.g. after a test failure or a newly found interface ([[episodes/langtalks--73-harness-engineering]]).
- Shared staging breaks constantly in growing orgs. Give each developer, and each agent, an isolated environment it can launch via CLI, decoupled from the machine it codes on ([[episodes/langtalks--73-harness-engineering]]).
- Pitfall: grabbing a popular skill (e.g. a code-reviewer with 100k GitHub stars) is a fine start, but the value is in custom skills encoding *your* deployment, design principles, tests, and team review norms ([[episodes/langtalks--73-harness-engineering]]).
- The host adapted Superpowers' visual planning: deep, comprehensive HTML plans (even if they take 30 min) reviewed via a custom Chrome extension for in-browser comments, fed back as Markdown, to batch decisions and cut context switching across 6–7 parallel sessions ([[episodes/langtalks--73-harness-engineering]]).
- Keep a docs folder of markdown inside the repo maintained by workflows. A one-off generator (e.g. DeepWiki) only describes current code, while decisions made in sessions need capturing; Claude Code memory scatters them ([[episodes/langtalks--68-ai-sdlc]]).

## Disagreements & open questions

## Takeaways
- [ ] Put product docs (PRDs, roadmap, concepts) as files in the repo, with an index prompt explaining each ([[episodes/langtalks--73-harness-engineering]])
- [ ] Add "when to update this skill" to every skill description ([[episodes/langtalks--73-harness-engineering]])
- [ ] Let agents launch isolated per-branch environments with one CLI command ([[episodes/langtalks--73-harness-engineering]])
- [ ] Write custom skills for your org's deploy, design, test, and review norms instead of relying on popular generic ones ([[episodes/langtalks--73-harness-engineering]])

## Related
[[concepts/harness-engineering]] · [[concepts/context-engineering]] · [[concepts/ai-guardrails]] · [[concepts/ai-sdlc]]
