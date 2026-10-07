---
type: concept
hubs: [ai-engineering]
sources: 4
updated: 2026-10-07
---
# AI R&D Rollout (adopting AI across an engineering org)

**Summary:** Rolling AI out to an R&D org is mostly change management. Start with education and licenses, let people try the main tools (Copilot, Cursor, Claude Code), converge on what works without locking in, and drive the mindset shift from "AI as a chat helper" to delegating whole features. A guild of early adopters spreads success stories and workshops; deliberate challenges (a sprint with no hand-written code) force the shift. Keep humans accountable throughout.

## Key ideas
- Path at Salt Security: Copilot licenses → everyone tries all tools → three-month accelerator → mainly Claude Code (codebase understanding, plan mode), with Copilot kept for tab completion ([[episodes/langtalks--62-ai-rd-rollout]], [[people/iko-azoulay]]).
- Avoid lock-in: tools leapfrog each other; don't build anything that ties you to one forever ([[episodes/langtalks--62-ai-rd-rollout]]).
- Tab completion is a "safety belt" for people not yet through the mindset shift. Choosing Claude Code (no tab completion) can push the shift; compliance reasons include Bedrock models and Cursor's server-side indexing ([[episodes/langtalks--62-ai-rd-rollout]]).
- Prediction: model labs will build the best coding agents because they fine-tune on their own tools ([[episodes/langtalks--62-ai-rd-rollout]]).
- GenAI guild: early adopters share success stories in wider forums, run internal workshops, and generate ideas, pulling laggards forward ([[episodes/langtalks--62-ai-rd-rollout]]).
- The "no-code sprint": he suggested a sprint of writing no code by hand. Harder at first, and people sometimes take pushback hard, but those who push through make the shift ([[episodes/langtalks--62-ai-rd-rollout]]).
- Give product people access too (Cursor plus repos) so they can ask the code instead of asking engineers ([[episodes/langtalks--62-ai-rd-rollout]]).
- A dedicated AI-enablement person can find internal "customers" and build Slack-channel agents for them (e.g. an analyst agent answering a GM's data questions, with a human analyst verifying SQL; a marketing copywriter agent) ([[episodes/ignore-instructions--24-wonderful-road-to-100m]]).
- Measured acceleration is modest overall: the host estimates 10–20% at Mixtiles (a few × in places, none in others). Gurevich sees ~3× on new products, where a founder can clear old processes. A flatter org with far more seniors than juniors; dashboards give way to asking Claude to investigate ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Little acceleration in sales and G&A. Gurevich argues automated outbound is a step backward and pushes enterprise sales back to in-person meetings, since buyers stake their careers on vendors ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- More than 20% of monday's code is written by agents ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/netanel-abergel]]).
- The main blocker is mindset: people micro-manage agents with 100 small tasks instead of stating the goal and reviewing the agent's plan; when something breaks, connect tools (e.g. a browser) and tell it to check itself rather than dictating fixes ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/netanel-abergel]]).
- Separate fundamentals (model and infra progress, which is steady and logical) from product hype ("the movie app doesn't actually work"); try things hands-on, since month-old verdicts are already history ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).

## Disagreements & open questions
- Copilot-style tab completion versus Claude Code: one host notes Cursor's cheap Composer model and agent editor are compelling, and that picking the right model per task is itself a skill ([[episodes/langtalks--62-ai-rd-rollout]]).

## Takeaways
- [ ] Start a GenAI guild of early adopters to share success stories and run workshops ([[episodes/langtalks--62-ai-rd-rollout]])
- [ ] Try a "no hand-written code" sprint to force the workflow shift ([[episodes/langtalks--62-ai-rd-rollout]])
- [ ] Give product managers read access to the codebase via an AI tool ([[episodes/langtalks--62-ai-rd-rollout]])
- [ ] Give agents the goal and review their plan, instead of dictating micro-tasks ([[episodes/startup-for-startup--362-agent-architecture-fit]])

## Related
[[concepts/ai-sdlc]] · [[concepts/ai-engineering-metrics]] · [[concepts/coding-agent-workflow]]
