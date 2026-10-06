---
type: concept
hubs: [ai-engineering]
sources: 5
updated: 2026-10-06
---
# AI Verification

**Summary:** Don't trust what an agent says it did; make it prove it. Read its outputs instead of "bypass reading", demand evidence ("show me, prove it"), and build concrete, proportional checks: open and quote sources, check links and logic. For code, verification becomes *proof of work*: after aligning on spec and plan, the agent must show the feature running end to end, e.g. driving a browser via Playwright and recording a video. Each check, once built, becomes a guardrail, so the effort drops over time.

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

## Disagreements & open questions

## Takeaways
- [ ] Have the agent fact-check by opening and quoting each source, never from memory ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Before any deletion the agent proposes, ask it to prove where the data is backed up ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Require a proof-of-work artifact (e.g. Playwright video) before accepting agent-built features ([[episodes/langtalks--73-harness-engineering]])
- [ ] Define an explicit definition of done the agent can check itself against before finishing ([[episodes/langtalks--70-our-claude-code-tips]])

## Related
[[concepts/ai-guardrails]] · [[concepts/wiki-retrieval]] · [[concepts/harness-engineering]] · [[concepts/ai-sdlc]]
