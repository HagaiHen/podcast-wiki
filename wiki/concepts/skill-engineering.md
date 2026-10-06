---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# Skill Engineering

**Summary:** Agent skills are mini software: a prompt describing a workflow (what, how, when) plus resources such as scripts, CLIs, or MCP calls. They replace functions and modules, or n8n graphs, combining deterministic code with LLM flexibility, and they let non-developers "contribute code". Sharing them is the hard part: forks diverge, external APIs change under them, and there's no good versioning or dependency management yet.

## Key ideas
- Even "complex" capabilities, like letting an agent message you, can be a few lines of skill plus an API or CLI and token setup ([[episodes/langtalks--72-personal-assistant-agent]]).
- Scripts in skills are Lego pieces the agent runs and may tweak per configuration ([[episodes/langtalks--72-personal-assistant-agent]]).
- Sharing by copy and fork was a mistake in hindsight: bug fixes and features don't propagate, and one user's feature is another's annoyance ([[episodes/langtalks--72-personal-assistant-agent]]).
- Better: a marketplace of composable pieces, plus each user's own workflow layered on top ("tag with meeting-tagger, but don't change my titles") ([[episodes/langtalks--72-personal-assistant-agent]]).
- Org practice: require every developer to contribute to a central skills repo periodically, so the shared catalog stays the source of truth ([[episodes/langtalks--72-personal-assistant-agent]]).
- Skills rot: a NanoClaw skill for a third-party API broke when the API changed, while old installs kept the stale skill. Skills need version control and dependency management like libraries ([[episodes/langtalks--72-personal-assistant-agent]]).
- Managing prompts well is an unsolved challenge: in code versus a platform, with no single source of truth and syncing issues ([[episodes/langtalks--72-personal-assistant-agent]]).
- AI-native open source: NanoClaw rejects PRs that change core code. Contributors submit *skills* that teach your coding agent how to modify your fork (e.g. swap WhatsApp for Telegram), so the core stays lean ([[episodes/langtalks--71-claw-architectures]], [[people/gavriel-cohen]]).
- This enables Karpathy's "bespoke software": everyone runs a customized version on a stable, secure base ([[episodes/langtalks--71-claw-architectures]]).
- Agent-operable projects: a CLAUDE.md for context plus a CLI usable by the operator, by Claude in the repo, and (with approvals) by agents in containers. Setup is a script that offers to run Claude on failures ([[episodes/langtalks--71-claw-architectures]]).

## Disagreements & open questions

## Takeaways
- [ ] Build skills as composable pieces and keep personal preferences in a separate per-user workflow layer ([[episodes/langtalks--72-personal-assistant-agent]])
- [ ] Keep shared skills in one versioned repo with a contribution norm, not personal forks ([[episodes/langtalks--72-personal-assistant-agent]])
- [ ] Make your project agent-operable: CLAUDE.md for context + a CLI agents can call ([[episodes/langtalks--71-claw-architectures]])

## Related
[[concepts/personal-ai-assistants]] · [[concepts/agent-ready-codebase]] · [[concepts/ai-guardrails]] · [[concepts/agent-security]]
