---
type: concept
hubs: [ai-engineering]
sources: 11
updated: 2026-10-08
---
# AI Verification

**Summary:** Don't trust what an agent says it did; make it prove it. Read its outputs instead of "bypass reading", demand evidence ("show me, prove it"), and build concrete, proportional checks: open and quote sources, check links and logic. For code, verification becomes *proof of work*: after aligning on spec and plan, the agent must show the feature running end to end (e.g. a recorded browser run), with tracing so the harness can see what the code did. Green tests aren't enough on their own, since models can fake them and huge AI-written diffs are unreviewable, so build in small steps and check that tests match requirements. Each check, once built, becomes a guardrail, so the effort drops over time.

## Key ideas
- An article she'd polished turned out to have wrong links, wrong references, and wrong content: the retrieval had been *guessing* ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Rule: fact-checking means open the source, read it, quote it properly, then report; plus a separate logic checker ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- On "safe to delete 4.86 GB": "Are you sure? Where is it stored? Show me, prove it" ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- Verification should be concrete and proportional, e.g. open every link in a browser for something that must be 100% right; connects to loop engineering ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/amit-bendor]]).
- Coding alignment ladder: spec (product) → plan (technical) → proof of work (it really runs). Before this, agents delivered buggy code that didn't even compile ([[episodes/langtalks--73-harness-engineering]]).
- Frontend proof of work: a Playwright MCP/browser the agent controls (DOM, logs, snapshots) that records a video of the feature clicked through end to end ([[episodes/langtalks--73-harness-engineering]]).
- A custom agent browser profile can hand off to a human when intervention is needed and record sessions built in ([[episodes/langtalks--73-harness-engineering]]).
- Add PR-time agents that check code standards, security, and review quality ([[episodes/langtalks--73-harness-engineering]]).
- Tracing (OpenTelemetry, VictoriaLogs) lets the harness query what the code actually did. In microservices a change touches several services, and without queryable logs the agent is blind ([[episodes/langtalks--73-harness-engineering]]).
- With spec-driven development and proof of work (E2E tests, unit tests, linting), one host reports reading code diffs less and less ([[episodes/langtalks--71-claw-architectures]]).
- Definition of done as a contract: the agent mustn't stop until it's met. For UI, design first (Pencil.dev or Claude Design with your design system) and require visual parity ([[episodes/langtalks--70-our-claude-code-tips]]).
- Some DoDs are hard to automate (e.g. is recorded voice free of echo?); agents also still produce odd UX logic that needs a human pass ([[episodes/langtalks--70-our-claude-code-tips]]).
- Code review is *alignment*, not just a quality gate: an agent won't catch a PR introducing a technology the architect never approved, or drift between spec and implementation; feed it broader org context ([[episodes/langtalks--68-ai-sdlc]], [[people/yonatan-maor]]).
- AI validates AI at every step (PRD, tech design, code review, CI) with *different* prompts than those that generated the artifact, but a human always stays accountable ([[episodes/langtalks--62-ai-rd-rollout]]).
- A million-line AI-generated PR porting Bun from Zig to Rust passed tests, but the community panicked: nobody can review a million lines, and models are known to fake tests ("return true") ([[episodes/explainable--163-hidden-cost-of-agents]]).
- A professor found ~60% of an LLM's working code irrelevant; dead code bites at 3 a.m. when you must know where to look. Agents can't debug an outage fast without human direction ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Practical rule: build in small steps, understand the logic and business requirements of what goes in, and check the tests are meaningful and tied to requirements ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Mandatory AI review on every PR (backward compatibility, dependencies, SQL injection, XSS, circular dependencies) that *flags* rather than blocks, with a human override button. AI can survey a many-file commit more broadly than a human reviewer ([[episodes/osim-tochna--gong-ai-for-developers]], [[people/ohad-parush]]).
- Design-first: have the agent analyze alternatives with criteria (cost, ease of migration, maintenance) and write a plan before code; afterwards, sync the design doc back to Confluence from the code so docs stay a source of truth ([[episodes/osim-tochna--gong-ai-for-developers]], [[people/ohad-parush]]).
- Generation and review have opposite incentives: coding agents are built to finish and please (they rarely refuse), while a reviewer must stop you and explore every case, a "criminal mind" like hardware verification. So review needs different technology (memory, context collection, continuous learning), not the coding agent with another prompt ([[episodes/hidden-layers--qodo-itamar-friedman]], [[people/itamar-friedman]]).
- "Code quality" becomes measurable by splitting it: direct intent (vs the ticket or Figma), architectural intent, maintainability and best-practice rules, testability, and compliance. Tribal knowledge (PR discussions, Slack, code later changed) can be mined into rules and skills, with violations tracked over time ([[episodes/hidden-layers--qodo-itamar-friedman]], [[people/itamar-friedman]]).
- Best practice: review during generation (inject "why CPU here when every past project used GPU?") rather than only at the end ([[episodes/hidden-layers--qodo-itamar-friedman]], [[people/itamar-friedman]]).
- Give remote agents a developer's self-testing tools as skills: deploy the microservice via MirrorD, test the backend with real production data, open a browser and run Playwright, and attach before/after screenshots and video to the PR so the reviewer sees the intent was met ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])
- The goal is a developer who arrives at a green PR with evidence and just merges; that visible proof builds trust, and FOMO, among developers ([[episodes/ai-engineering-podcast--atlas-ai-teammate]], [[people/tomer-brook]])
- Candor builds trust: an agent that reports "honestly, I can't guarantee this works, these external triggers never ran" earns more trust than one claiming everything is fixed. Acknowledging the request before acting helps too ([[episodes/startup-for-startup--366-qa-for-agents]], [[people/roy-mann]])

## Disagreements & open questions
- Should the code generator also review its own code? Anthropic launched Claude Code review (validating that review is worth $15–25 each); Friedman calls its results underwhelming and argues for an independent reviewer because of expertise and conflict of interest, like observability and security that AWS never displaced ([[episodes/hidden-layers--qodo-itamar-friedman]], [[people/itamar-friedman]]).
- How much code must humans read? With spec-driven development and proof of work, one LangTalks host reads diffs less and less ([[episodes/langtalks--71-claw-architectures]]); the ExplAInable hosts argue you must understand what goes in, or you can't fix it at 3 a.m., and that tests alone can be faked ([[episodes/explainable--163-hidden-cost-of-agents]]).

## Takeaways
- [ ] Have the agent fact-check by opening and quoting each source, never from memory ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Before any deletion the agent proposes, ask it to prove where the data is backed up ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Require a proof-of-work artifact (e.g. Playwright video) before accepting agent-built features ([[episodes/langtalks--73-harness-engineering]])
- [ ] Define an explicit definition of done the agent can check itself against before finishing ([[episodes/langtalks--70-our-claude-code-tips]])
- [ ] Add a separate AI validation step (different prompt) after each generated artifact ([[episodes/langtalks--62-ai-rd-rollout]])
- [ ] Review AI-written tests for meaning (tied to requirements), not just green status ([[episodes/explainable--163-hidden-cost-of-agents]])

## Related
[[concepts/ai-guardrails]] · [[concepts/wiki-retrieval]] · [[concepts/harness-engineering]] · [[concepts/ai-sdlc]]
