---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# Agent Architectures (fitting structure to the job)

**Summary:** "Agent" is as broad as "software", and the right architecture depends on the job. A single personal agent can live on its own machine (OpenClaw-style). Many agents serving many people need agents *assembled on demand* from shared memory, skills, and knowledge, so one improvement reaches all of them. Roy Mann splits the space into agents working *with* people (in code, where tests and deploys already impose order, or in general work, where processes must be built and audited) and agents *doing the work* (close to AI-infused automation, likely spawning many vertical architectures). Mixing problem types, such as a personal companion that must also run reliable task loops, makes both worse.

## Key ideas
- One machine per agent breaks at scale: rolling a good skill out to hundreds of agents means patching every machine. monday's internal agents have no machine; they assemble from shared stores and run, so changing one skill file updates everyone ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]], [[people/netanel-abergel]]).
- Agents working with people in code is the easier case: code is the truth, and review, tests, and deploys were already orderly before agents ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- Agents working with people in general work (sales, travel or vacation requests) is harder: the organization needs audit trails and processes that stay dynamic for the agent, not hard-coded ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- Agents doing the work (checking an insurance-claim form, calling a customer when a delivery arrives, an SDR): no complex collaboration, but accountability, history, and the ability to ask "why did that fail?" and improve. Expect both generic platforms and vertical startups ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- First questions for builders: what job should the agent do, which category is it, and does the product really need to solve two problem types at once ([[episodes/startup-for-startup--362-agent-architecture-fit]])?
- Personality and memory slow and confuse task agents: Mann's personal agent brought its whole persona into a bug-fixing loop that didn't need it ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- Agent sessions repeatedly asked to open pull requests, which needs no AI, so they made a deterministic skill with a script. The next generation of agents should detect this and write the script themselves ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/netanel-abergel]], [[people/roy-mann]]).

## Disagreements & open questions
- Will one generic agent platform serve all "doing the work" jobs, or will verticals (SDR, voice) win with specialized architectures? Mann expects both ([[episodes/startup-for-startup--362-agent-architecture-fit]]).

## Takeaways
- [ ] Before building an agent, classify the job (with people in code, with people in general work, or doing the work) and solve only that problem ([[episodes/startup-for-startup--362-agent-architecture-fit]])

## Related
[[concepts/agent-workspaces]] · [[concepts/multi-agent-orchestration]] · [[concepts/personal-ai-assistants]] · [[concepts/harness-engineering]] · [[concepts/workflow-automation]]
