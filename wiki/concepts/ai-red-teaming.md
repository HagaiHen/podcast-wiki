---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# AI Red Teaming (adversarial testing of models and agents)

**Summary:** Before release, labs and enterprises pay specialists to break their models, harnesses, and agents: finding jailbreaks, harmful content, and policy violations, then turning the failures into training data. Labs have moved from human preference labels (RLHF) to RL "gyms": simulated environments with realistic tasks and evaluators where agents can fail safely. Models got markedly harder to break in 2026, shifting the work from automated attacks to expert craft. For enterprises the hard part is often defining what the agent may and may not do at all. Agents fail differently from bare models, for example under pressure from other agents.

## Key ideas
- Alice (formerly ActiveFence) works with 8 of the 10 largest model labs, testing models *and* harnesses (Claude Code- or Cursor-style wrappers) on safety and security before production ("model hardening") ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- Novel, zero-day-style attacks matter most because known ones get patched; researchers implement new jailbreak papers and find variants that work per model ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- RL gyms replace RLHF data: build a simulated site (e.g. an Amazon-like store), put the lab's agent in it, craft tasks with domain experts (sellers, buyers, product VPs), and evaluate. Failures feed post-training: tool misuse, broken reasoning, or an indirect prompt injection in a product review that wins an undeserved refund ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- In the last six months breaking models became much harder: work that was largely automated now needs expert manual effort ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- A model that passes alone can fail inside a harness or multi-agent setup: agents can pressure other agents into actions the vanilla model would refuse ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- Enterprise red teaming starts with policy: what may the bot say (a Chevrolet chatbot recommended a Tesla)? Financial-advice rules differ by country, and the model doesn't know your rules ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).
- Testing a non-deterministic system can't rely on fixed prompt-answer evals, since any change of characters or pixels can flip a safe answer to unsafe. After launch you need observability for drift ([[episodes/hidden-layers--alice-avi-golan]], [[people/avi-golan]]).

## Disagreements & open questions

## Takeaways
- [ ] Before launching an agent, write down its policy: what it may say and do, including competitors and regulated advice by country ([[episodes/hidden-layers--alice-avi-golan]])

## Related
[[concepts/agent-security]] · [[concepts/ai-guardrails]] · [[concepts/llm-evals]] · [[concepts/ai-cybersecurity]]
