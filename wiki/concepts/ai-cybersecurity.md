---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# AI and Cybersecurity

**Summary:** Frontier models are getting much better at finding vulnerabilities, which erodes cybersecurity's old premise that scarce expert knowledge can be packaged into products that protect people who lack it. Code is now written faster by agents, legacy is vast, and attackers use LLMs too, so periodic manual testing no longer keeps up. The response is continuous, automated testing plus fast remediation. How labs should release cyber-capable models is contested: restricted access versus broad access with identity verification. Demand for security is expected to *rise*, since organizational risk is growing, not shrinking.

## Key ideas
- Traditional pentesting comes in two forms: external audits for compliance (a two-week engagement ending in a PDF; expensive, infrequent, and dependent on the team's day) or scarce internal red teams. Neither scales to agent-speed code ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Model capability in finding vulnerabilities rose faster than the Tenzai team expected; the same evolution was visible before Mythos ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Two things can be true at once: models are genuinely improving at offense, *and* Anthropic's restricted Mythos rollout (Project Glasswing, select US companies) is a marketing masterstroke built on scarcity ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Gurevich's view on access: restricting defenders while capable models leak or exist elsewhere hurts safety. Prefer KYC-style identity verification and accountability (OpenAI's trusted-access program) and broad access for defenders. Security-through-obscurity has failed repeatedly ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Model differences plateau: vulnerability-finding curves level off at similar heights. Harness and token budget matter as much as the model, and he rated GPT-5.5 under trusted access above Opus 4.8 at finding vulnerabilities in code ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- A coming cleanup era, similar to the early Windows worm era: many critical bugs found, then the internet gets cleaner. What matters is time to find *and* time to fix (in code or at an intermediate layer) ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Host's analogy: a good lock used to stop opportunistic burglars; now opportunists may get professional-grade tools ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]]).
- Many real findings are business-logic and integration gaps (microservices wired wrongly, infrastructure config, double-spend style flows), not classic coding mistakes ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Security demand grows while the case for buying generic SaaS weakens: companies can build more themselves, but cyber risk only rises ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Open-weight models are what matter about "Chinese models": US companies are also working on strong open models, and broad openness with incremental capability helps defenders keep up ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).

## Disagreements & open questions
- Restricted release vs broad verified access: the host argues that with very high-stakes capabilities (state actors), caution and responsible-disclosure-style delays make sense; Gurevich counters that selective early access isn't disclosure and leaves most defenders blind ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]]).

## Takeaways
- [ ] Add automated security testing to the release process for agent-written code ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]])
- [ ] Raise human pentest frequency from yearly to quarterly or monthly, and test integrated staging, not just code ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]])

## Related
[[concepts/agent-security]] · [[concepts/harness-engineering]] · [[concepts/open-weight-models]] · [[concepts/ai-verification]]
