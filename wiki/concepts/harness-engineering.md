---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# Harness Engineering

**Summary:** Designing the environment around a coding agent so it can work autonomously for long sessions (40–50 minutes, not 5) and converge on correct, production-ready code. The agent must be able to understand the project, act like a developer (run code, tests, environments), and get reward signals telling it whether it's on track. Guardrails are *enforced* in the flow rather than requested. Gains compound: each internal tool lets agents run longer and better.

## Key ideas
- Terminology: the harness is Claude Code, Codex, Cursor agent; tools like NanoClaw/OpenClaw are orchestrators that *use* a harness ([[episodes/langtalks--73-harness-engineering]]).
- In a plain chat session the only "reward" is your one prompt; the agent doesn't know if its code works or fits the product ([[episodes/langtalks--73-harness-engineering]]).
- OpenAI started a fresh repo in Aug 2025 with 3 engineers; it passed 1M lines within months and average productivity grew as engineers were added ([[episodes/langtalks--73-harness-engineering]]).
- Key pattern: instead of "try harder / check yourself 10 times", ask the agent *what capability it's missing* to verify its work, build that tool, and make it part of the enforced flow ([[episodes/langtalks--73-harness-engineering]]).
- Three alignments before trusting output: spec (product), plan (technical), proof of work (it actually runs). See [[concepts/ai-verification]] ([[episodes/langtalks--73-harness-engineering]]).
- Prediction (hosts): within months to a year, most code will be written autonomously by background agents. The bottleneck shifts to human code review ([[episodes/langtalks--73-harness-engineering]]).
- Success metric: productivity per token, rising over time not only with smarter models but with each internal tool you add ([[episodes/langtalks--73-harness-engineering]]).

## Disagreements & open questions
- Cost: providers moved from flat ~$200/month plans to token billing, and companies push to cut spend (cheaper models, open source). The hosts argue against blind token minimization, but warn against "token-maxing" too: use harness hooks and OpenTelemetry to evaluate what's actually happening ([[episodes/langtalks--73-harness-engineering]]).

## Takeaways
- [ ] When an agent fails, ask it which capability/tool it lacks to verify itself, and build that ([[episodes/langtalks--73-harness-engineering]])
- [ ] Track productivity per token over time as the harness KPI ([[episodes/langtalks--73-harness-engineering]])

## Related
[[concepts/agent-ready-codebase]] · [[concepts/test-driven-development]] · [[concepts/ai-guardrails]] · [[concepts/ai-verification]]
