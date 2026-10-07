---
type: concept
hubs: [ai-engineering]
sources: 7
updated: 2026-10-07
---
# Harness Engineering

**Summary:** Designing the environment around a coding agent, or any task agent, so it can work autonomously for long sessions and converge on correct, production-ready results. The agent must understand the project, act like a practitioner (run code, tests, environments, browsers), and get reward signals telling it whether it's on track. Guardrails are *enforced* in the flow rather than requested. A harness is built and torn down at once: add scaffolding where the model falls short, and remove it as new models make it redundant. Purpose-built harnesses beat generic ones, measuring where you stand matters as much as the harness, and infrastructure (durable objects, sandboxes) is catching up for long-running agents.

## Key ideas
- Terminology: the harness is Claude Code, Codex, Cursor agent; tools like NanoClaw/OpenClaw are orchestrators that *use* a harness ([[episodes/langtalks--73-harness-engineering]]).
- In a plain chat session the only "reward" is your one prompt; the agent doesn't know if its code works or fits the product ([[episodes/langtalks--73-harness-engineering]]).
- OpenAI started a fresh repo in Aug 2025 with 3 engineers; it passed 1M lines within months and average productivity grew as engineers were added ([[episodes/langtalks--73-harness-engineering]]).
- Key pattern: instead of "try harder / check yourself 10 times", ask the agent *what capability it's missing* to verify its work, build that tool, and make it part of the enforced flow ([[episodes/langtalks--73-harness-engineering]]).
- Three alignments before trusting output: spec (product), plan (technical), proof of work (it actually runs). See [[concepts/ai-verification]] ([[episodes/langtalks--73-harness-engineering]]).
- Prediction (hosts): within months to a year, most code will be written autonomously by background agents. The bottleneck shifts to human code review ([[episodes/langtalks--73-harness-engineering]]).
- Success metric: productivity per token, rising over time not only with smarter models but with each internal tool you add ([[episodes/langtalks--73-harness-engineering]]).
- Choose stacks for agent autonomy: TypeScript and cloud-first (React Native even for a mobile app) so agents can run and verify in the cloud with your laptop closed ([[episodes/langtalks--70-our-claude-code-tips]]).
- Every agent PR spins up a full preview environment (DB, services, load balancers) via Pulumi/Kubernetes, or MirrorD mirrors only the changed container into a shared dev cluster ([[episodes/langtalks--70-our-claude-code-tips]]).
- Prefer CLIs over MCPs where possible; they're simpler for agents ([[episodes/langtalks--70-our-claude-code-tips]]).
- The biggest blocker is often plain DevOps: no per-developer environment, shared broken staging, no log access. Map where developers copy-paste between systems and wire those gaps (MCP, tokens, CLI, environment infra) ([[episodes/langtalks--68-ai-sdlc]]).
- The single most valuable investment for R&D orgs now: an internal platform for agents (environments, docs for internal tools, dev setups) ([[episodes/langtalks--63-wake-up]]).
- Infra is catching up for long-running agents: Vercel and Cloudflare (Durable Objects) make stateless serverless functions stateful, replacing a 4–5-piece stack (queues, Redis memory). Sandboxes (Cloudflare, Vercel, Daytona, E2B) run agent code without risk ([[episodes/ignore-instructions--20-idan-benyon-build-ship-grow]], [[people/idan-benyon]]).
- A harness is two opposite processes at once: *building* scaffolding where the model's freestyle intuition falls short (tools, memory, execution environment, what not to do) and *removing* it as new models make steps redundant or bloat the prompt, "like a startup" ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- A purpose-built harness beats generic ones; agent companies with enough traction and data eventually train their own model on open weights for cost and speed (as Cursor did with Composer) ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Long tasks (8–12 hours) need a cloud environment, memory across runs, and coverage reporting: the agent should show where it looked, not just "found nothing" ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Measuring where you stand can matter as much as the harness itself ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- "Harness" is overloaded: Mann reserves it for the loop that runs skills and tools, with an OS-like layer, applications, and plugins built above it, like CPU → OS → apps ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).
- 3D-printer analogy: early printers needed constant fixing; modern ones add a hundred engineering layers (laser bed scans) so a 40-hour print just works. Agents "don't fully work yet", and roughly a decade of engineering above the LLM is the opportunity (and why forward-deployed engineers exist) ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).

## Disagreements & open questions
- Cost: providers moved from flat ~$200/month plans to token billing, and companies push to cut spend (cheaper models, open source). The hosts argue against blind token minimization, but warn against "token-maxing" too: use harness hooks and OpenTelemetry to evaluate what's actually happening ([[episodes/langtalks--73-harness-engineering]]).

## Takeaways
- [ ] When an agent fails, ask it which capability/tool it lacks to verify itself, and build that ([[episodes/langtalks--73-harness-engineering]])
- [ ] Track productivity per token over time as the harness KPI ([[episodes/langtalks--73-harness-engineering]])
- [ ] Give each agent PR its own preview environment (IaC or container mirroring) ([[episodes/langtalks--70-our-claude-code-tips]])
- [ ] Map every copy-paste step in your dev loop and replace it with agent-accessible tooling ([[episodes/langtalks--68-ai-sdlc]])

## Related
[[concepts/agent-ready-codebase]] · [[concepts/test-driven-development]] · [[concepts/ai-guardrails]] · [[concepts/ai-verification]] · [[concepts/coding-agent-workflow]] · [[concepts/ai-sdlc]] · [[concepts/ai-cybersecurity]] · [[concepts/agent-architectures]]
