---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-08
---
# Agent Architectures (fitting structure to the job)

**Summary:** "Agent" is as broad as "software", and the right architecture depends on the job. At one end are "pass the butter" agents with a narrow task that must be stable and give clear feedback, with no need to remember you; at the other, personal assistants that must know and remember you and act proactively in the background, which makes them less predictable. A single personal agent can live on its own machine (OpenClaw-style). Many agents serving many people need agents *assembled on demand* from shared memory, skills, and knowledge, so one improvement reaches all of them. Roy Mann splits the space into agents working *with* people and agents *doing the work*, which likely spawn many vertical architectures; domain-expert work pushes general agents into niches. Sub-agents with bounded tasks keep context clean and outcomes predictable. Mixing problem types, such as a personal companion that must also run reliable task loops, makes both worse.

## Key ideas
- One machine per agent breaks at scale: rolling a good skill out to hundreds of agents means patching every machine. monday's internal agents have no machine; they assemble from shared stores and run, so changing one skill file updates everyone ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]], [[people/netanel-abergel]]).
- Agents working with people in code is the easier case: code is the truth, and review, tests, and deploys were already orderly before agents ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- Agents working with people in general work (sales, travel or vacation requests) is harder: the organization needs audit trails and processes that stay dynamic for the agent, not hard-coded ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- Agents doing the work (checking an insurance-claim form, calling a customer when a delivery arrives, an SDR): no complex collaboration, but accountability, history, and the ability to ask "why did that fail?" and improve. Expect both generic platforms and vertical startups ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- First questions for builders: what job should the agent do, which category is it, and does the product really need to solve two problem types at once ([[episodes/startup-for-startup--362-agent-architecture-fit]])?
- Personality and memory slow and confuse task agents: Mann's personal agent brought its whole persona into a bug-fixing loop that didn't need it ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- Agent sessions repeatedly asked to open pull requests, which needs no AI, so they made a deterministic skill with a script. The next generation of agents should detect this and write the script themselves ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/netanel-abergel]], [[people/roy-mann]]).
- The spectrum: a "pass the butter" agent (check a submitted document, reply, store it) needs stability and clear feedback, not your life story; a personal assistant must know and remember you and be proactive and ambient, so it's more general and less predictable ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/roy-mann]])
- monday runs both kinds: job agents (scan your field daily for relevant RFPs, fill them in, and ask for what's missing) where memory barely matters, and Sidekick, a general assistant where remembering the user is critical ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/roy-mann]])
- Vertical beats general for expert work: Taka started as general agents (Claude or OpenClaw managing social media), but on-brand images, carousels, and video needed domain expertise, so it narrowed into an AI social media manager ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/matan-lach]])
- Sub-agents with specific, bounded tasks don't pollute the main agent's context and can run on a known model; the clearer a task's start and end, the more certain the result ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/roy-mann]])

## Disagreements & open questions
- Will one generic agent platform serve all "doing the work" jobs, or will verticals (SDR, voice) win with specialized architectures? Mann expects both ([[episodes/startup-for-startup--362-agent-architecture-fit]]).

## Takeaways
- [ ] Before building an agent, classify the job (with people in code, with people in general work, or doing the work) and solve only that problem ([[episodes/startup-for-startup--362-agent-architecture-fit]])

## Related
[[concepts/agent-workspaces]] · [[concepts/multi-agent-orchestration]] · [[concepts/personal-ai-assistants]] · [[concepts/harness-engineering]] · [[concepts/workflow-automation]] · [[concepts/llm-evals]]
