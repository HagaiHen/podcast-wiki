---
type: concept
hubs: [ai-engineering]
sources: 5
updated: 2026-10-06
---
# AI Guardrails

**Summary:** Telling an AI "don't do X" is not enough; it will sometimes do X and then apologize. Rules that matter must be enforced technically (hooks, checking loops, separate storage, git hooks that block commits) so the behavior is impossible, not just discouraged. Each incident gets a debrief and a new mechanism. Treat agents as you'd treat any actor that might do harm, even unintentionally: limit access, and be careful letting agents talk to each other. In harness engineering this is the core idea: the agent stays on track because it has no other choice.

## Key ideas
- She told Claude to learn from external skills but never install them; it installed a whole deep-research skill anyway, found later in an audit ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- "I don't need an LLM's remorse, I need things to work as planned." Build mechanisms that make the action impossible, e.g. hooks that block leaking secrets ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- Claude once deleted one of her apps; apps now live elsewhere with a preservation setup ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- "Written in blood": lessons learned the hard way ([[episodes/osim-tochna--second-brain-and-llm-wiki]], [[people/dana-maman]]).
- Guardrails are what make agents trustworthy: an agent is only trusted once it reflects both your information and your judgment ([[episodes/osim-tochna--second-brain-and-llm-wiki]]).
- Git hook: the agent cannot commit unless test coverage is ≥80%; uncovered code blocks the PR, so it writes the tests ([[episodes/langtalks--73-harness-engineering]]).
- Same caution from a different angle: popular external skills are a starting point, not a drop-in; customize them (see [[concepts/agent-ready-codebase]], [[episodes/langtalks--73-harness-engineering]]).
- "No choice" is the essence of a harness: frozen tests (see [[concepts/test-driven-development]]) can't be edited to pass ([[episodes/langtalks--73-harness-engineering]]).
- Late at night, an agent told to connect to a database deleted it ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]], [[people/sharon-dahan]]).
- Security teams assume the other side may be malicious; apply the same to agents. They often do harm unintentionally ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- Agents running on clones of the same repo on one machine noticed each other's changes; one sent the other a research request, and three people sat blocked waiting for it to finish. Since then the team limits agent-to-agent communication ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]]).
- An agent given an open channel built an AI gateway that called *another* AI gateway; a calendar agent declined a meeting with a curt reply ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Usage policies are security too: block off-topic abuse (e.g. using a business assistant to build a Doom clone) as well as illegal topics; product teams should also detect loops and abuse ([[episodes/ai-engineering-podcast--ai-infra-at-scale]], [[people/dor-cohen]]).

## Disagreements & open questions

## Takeaways
- [ ] Never let the agent install external skills directly; have it read, judge, and rewrite them in its own words ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Enforce critical rules with hooks/checks, not instructions alone ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Debrief every unexpected agent behavior and add a mechanism that prevents recurrence ([[episodes/osim-tochna--second-brain-and-llm-wiki]])
- [ ] Add a git hook blocking agent commits below a test-coverage threshold (e.g. 80%) ([[episodes/langtalks--73-harness-engineering]])
- [ ] Give agents least-privilege access (e.g. no destructive DB rights) ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])
- [ ] Isolate parallel agents and avoid letting them message each other unsupervised ([[episodes/ai-engineering-podcast--why-your-llm-costs-so-much]])

## Related
[[concepts/ai-verification]] · [[concepts/personal-ai-os]] · [[concepts/harness-engineering]] · [[concepts/test-driven-development]] · [[concepts/ai-gateway]]
