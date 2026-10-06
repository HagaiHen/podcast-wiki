---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-06
---
# Context Engineering

**Summary:** What separates generic AI output from "gold" is context: deciding what goes into it, keeping it lean and current, and surfacing the right thing at the right moment. Watch what always loads (keep CLAUDE.md small) versus on demand. Prefer discoverable files over tools the agent must remember to call. Capture context that lives outside the repo (meetings, Slack), including the *reason* behind decisions, or the agent will repeat mistakes.

## Key ideas
- Context is the difference between generic and excellent output; the craft is what to include without bloating it ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Ask your system to diagram what happens when a request arrives (what loads, when). Dana keeps her CLAUDE.md very small because it loads every time ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Garbage in, garbage out: the AI may treat irrelevant sources as relevant, so you must draw the line ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Files beat MCPs for discoverability: an agent often won't call a Jira/Linear MCP because it doesn't know what's there ([[episodes/langtalks--73-harness-engineering]]).
- Much context lives in Slack, Zoom, and hallway talks. Record and transcribe meetings, then have a scheduled job reconcile Slack threads with specs (newest wins; flag oddities) ([[episodes/langtalks--73-harness-engineering]]).
- Telling the agent "use component B, not A" without saying *why* doesn't persist; it repeats the mistake tomorrow ([[episodes/langtalks--73-harness-engineering]]).

## Disagreements & open questions

## Takeaways
- [ ] Ask your agent to diagram what it loads on each request; keep always-loaded files (CLAUDE.md) small ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] When correcting an agent, state the reason so it can be saved as a rule ([[episodes/langtalks--73-harness-engineering]])

## Related
[[concepts/wiki-retrieval]] · [[concepts/llm-wiki]] · [[concepts/agent-ready-codebase]]
