---
type: concept
hubs: [ai-engineering]
sources: 7
updated: 2026-10-06
---
# Context Engineering

**Summary:** What separates generic AI output from "gold" is context: deciding what goes into it, keeping it lean and current, and surfacing the right thing at the right moment. It's also the lever behind cost: aggressive context management (splitting tasks, slimming what each agent sees) lets smaller, cheaper models succeed, and unmanaged context makes any model "dumb". Watch what always loads (keep CLAUDE.md small), prefer discoverable files over tools, and capture off-repo context (meetings, Slack) with the reasons behind decisions.

## Key ideas
- Context is the difference between generic and excellent output; the craft is what to include without bloating it ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Ask your system to diagram what happens when a request arrives (what loads, when). Dana keeps her CLAUDE.md very small because it loads every time ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Garbage in, garbage out: the AI may treat irrelevant sources as relevant, so you must draw the line ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Files beat MCPs for discoverability: an agent often won't call a Jira/Linear MCP because it doesn't know what's there ([[episodes/langtalks--73-harness-engineering]]).
- Much context lives in Slack, Zoom, and hallway talks. Record and transcribe meetings, then have a scheduled job reconcile Slack threads with specs (newest wins; flag oddities) ([[episodes/langtalks--73-harness-engineering]]).
- Telling the agent "use component B, not A" without saying *why* doesn't persist; it repeats the mistake tomorrow ([[episodes/langtalks--73-harness-engineering]]).
- "Context management is the king" of model selection: how much you invest in it decides how small a model you can use ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- A ship-ERP troubleshooting agent with many subagents failed because one middle agent's context was too big; it "choked". Splitting the context raised eval success from 85% to 97%, with no fine-tuning ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- When a long Claude Code session degrades after compaction, have it write what it knows to an MD file and start fresh ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Context is king for personalization: decompose it into personal, team, group, and org layers, with permissions so nothing leaks ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]], [[people/matan-cohen]]).
- Skill descriptions consume context: with 100+ skills the listing gets truncated, silently hiding skills ([[episodes/langtalks--70-our-claude-code-tips]]).
- Global and repo instruction files fill context fast and aren't relevant to every task. Keep them focused, and retrieve decisions made *in the area you're touching* dynamically ([[episodes/langtalks--68-ai-sdlc]]).
- Agent-loop best practices: dump large intermediate data to files instead of keeping it in state; keep the prompt prefix stable for caching (manual on Claude/Bedrock, automatic on OpenAI). Manus's context-engineering blog post is recommended ([[episodes/langtalks--65-ai-sre]]).

## Disagreements & open questions

## Takeaways
- [ ] Ask your agent to diagram what it loads on each request; keep always-loaded files (CLAUDE.md) small ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] When correcting an agent, state the reason so it can be saved as a rule ([[episodes/langtalks--73-harness-engineering]])
- [ ] When a session degrades after compaction, dump state to an MD file and restart ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/wiki-retrieval]] · [[concepts/llm-wiki]] · [[concepts/agent-ready-codebase]] · [[concepts/model-selection]]
