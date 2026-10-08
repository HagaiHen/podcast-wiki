---
type: concept
hubs: [ai-engineering]
sources: 11
updated: 2026-10-08
---
# Context Engineering

**Summary:** Getting all and *only* the relevant context into each model call: prompts, retrieved knowledge, memory, conversation history, tool results, and output schemas. Context is what separates generic output from "gold". It's also the lever on cost (lean context lets small models succeed) and on reliability (irrelevant tokens measurably lower task success, and unmanaged context makes any model dumb). Treat the context window like RAM: *write* (what enters state, scratchpads, long-term memory), *select* (retrieve the right thing at the right moment), *compress* (offload to files, summarize with intent), and isolate work in sub-agents. Keep always-loaded files small, prefer discoverable files over tools the agent must remember, keep prompt prefixes stable for caching, and capture off-repo context (meetings, Slack) with the reasons behind decisions.

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
- Short-term memory problem: in long sessions, an instruction from the start may be lost or buried in context ([[episodes/langtalks--57-memory]]).
- Prompt engineering is only a slice; context engineering includes RAG, memory, history, and structured output. Even when needle-in-a-haystack is solved, irrelevant input tokens lower task success ([[episodes/langtalks--55-context-engineering]]).
- Karpathy's framing: LLM = CPU, context window = RAM to be managed ([[episodes/langtalks--55-context-engineering]]).
- Don't dump a whole file into the main conversation: a sub-agent reads it and returns a concise answer, or just the relevant line numbers or snippet ([[episodes/langtalks--55-context-engineering]]).
- Recitation: writing plans and to-do lists to files (and re-reading them) steers attention. Plans are verbose partly to bias the model, not for humans. Split big PRDs into done vs to-do files so the agent sees only what's relevant ([[episodes/langtalks--55-context-engineering]]).
- Prefer manual context injection when possible: e.g. a hook that injects testing guidelines when the agent starts writing tests ([[episodes/langtalks--55-context-engineering]]).
- Keep tool errors in context; make APIs used as agent tools return *specific* errors (bad secret vs no permission) so the agent can recover ([[episodes/langtalks--55-context-engineering]]).
- Compaction is a fallback; if used, tell it what to focus on. Alternatively, dump state to files at ~100k tokens, reset, and continue ([[episodes/langtalks--55-context-engineering]]).
- Health check: open your traces (LangSmith, Langfuse). The more you scroll past irrelevant content, the worse your context engineering ([[episodes/langtalks--55-context-engineering]]).
- As a *user* of coding agents you also do context engineering, e.g. @-mentioning the right files ([[episodes/langtalks--55-context-engineering]]).
- Prohibitions backfire: "don't", "never", "avoid" draw attention to the unwanted behavior. Say what you want instead ("output Markdown" rather than "not JSON"; "answer from the user's point of view" rather than "don't leak internals") ([[episodes/startup-for-startup--354-reliable-agents-lean-context]], [[people/doron-bleiberg]]).
- Prevention over correction: if-this-then-that patches added after failures fight attention already pointed the wrong way; shape the initial context instead ([[episodes/startup-for-startup--354-reliable-agents-lean-context]], [[people/doron-bleiberg]]).
- Don't re-teach what the model knows: benchmark it several times and inject only what it gets wrong; known knowledge costs tokens, latency, and attention ([[episodes/startup-for-startup--354-reliable-agents-lean-context]], [[people/doron-bleiberg]]).
- Every prompt part has a cost: the system prompt rides on every request with high attention, so keep it minimal; load task instructions, skills, domain knowledge, and tool details only when needed, even injecting tool-specific knowledge via hooks at invocation ([[episodes/startup-for-startup--354-reliable-agents-lean-context]], [[people/doron-bleiberg]]).
- Prompt tactics: keep hard "don'ts" to a few key ones (around four), repeat key instructions at both the start and end of the context, and watch the tool count, since piling on MCP tools overflows the context ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/roy-mann]])
- Mann had an agent gather strong public agent prompts into a library and compare his prompt against them; the report taught him a lot, but without a working test framework he couldn't tell whether the changes helped ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/roy-mann]])

## Disagreements & open questions

## Takeaways
- [ ] Ask your agent to diagram what it loads on each request; keep always-loaded files (CLAUDE.md) small ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] When correcting an agent, state the reason so it can be saved as a rule ([[episodes/langtalks--73-harness-engineering]])
- [ ] When a session degrades after compaction, dump state to an MD file and restart ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Have sub-agents read large files and return only answers or snippets to the main agent ([[episodes/langtalks--55-context-engineering]])
- [ ] Return specific, actionable errors from APIs that agents call, and keep errors in context ([[episodes/langtalks--55-context-engineering]])
- [ ] Audit a trace: if you scroll past lots of irrelevant content, trim the context ([[episodes/langtalks--55-context-engineering]])
- [ ] Rewrite "don't" rules in agent prompts as positive instructions ([[episodes/startup-for-startup--354-reliable-agents-lean-context]])

## Related
[[concepts/wiki-retrieval]] · [[concepts/llm-wiki]] · [[concepts/agent-ready-codebase]] · [[concepts/model-selection]] · [[concepts/agent-memory]]
