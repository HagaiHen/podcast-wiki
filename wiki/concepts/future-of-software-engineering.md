---
type: concept
hubs: [ai-engineering]
sources: 7
updated: 2026-10-07
---
# Future of Software Engineering

**Summary:** AI replaces coding, not engineering. The value of AI arrives *with* an engineering layer around it: memory, context, evals, harnesses. As with past shifts (network engineers became DevOps, platform engineers, and SREs when virtualization arrived), roles move one level of abstraction up. Developers may absorb product and UX work, but security, legal, and real product depth keep engineering essential.

## Key ideas
- "Coding is dead, but engineering definitely isn't" ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]], [[people/netanel-abergel]]).
- Historical analogy: virtualization didn't eliminate network engineers; they became DevOps, platform engineers, and SREs ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]], [[people/matan-cohen]]).
- AI has limits: the math of capability vs cost vs output, and how much harness work it takes to truly finish a task ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- You can't vibe-code a product like monday.com: security, legal, and countless details ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- The guest is openly bullish on developers, skeptical of apocalyptic predictions ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Customer success became "forward-deployed engineering": new, more abstract role names ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Medium term: developers become orchestrators ("agent team leads") and environment engineers, building internal CLIs, dev platforms, and environments agents can run in ([[episodes/langtalks--63-wake-up]]).
- Longer term: agents may write everything; human value shifts to creativity. Analyst, QA, and design roles get folded into agents a developer directs ([[episodes/langtalks--63-wake-up]]).
- One host's productivity estimate: ~5× today, ~20× by end of 2026, ~100× in 2027, driven by overnight background agents ([[episodes/langtalks--63-wake-up]]).
- Two possible paths: smaller R&D orgs, or the same headcount shipping far more (raising the question of whether customers can absorb it) ([[episodes/langtalks--63-wake-up]]).
- Entry-level jobs get much harder; deep fundamentals (logic, architecture, distributed systems) are needed to handle the last 5% where agents get stuck. Seniors who "were in the trenches" have an edge ([[episodes/langtalks--63-wake-up]]).
- Companies whose moat was the software itself face commoditization ([[episodes/langtalks--63-wake-up]]).
- Wonderful "officially stopped writing code" ~6 months before the episode; developers aren't attached to code, so libraries get replaced via "Codex, please implement" overnight ([[episodes/ignore-instructions--24-wonderful-road-to-100m]]).
- Entropy argument: complex systems drift toward disorder, and probabilistic agents add small errors that compound. Humans, wired to seek order and causes, remain needed to control the chaos, e.g. as reviewers of *why* an agent chose a fix ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Roles will shift as mobile and full-stack once appeared: pure "code monkeys" may go, while architecture, design, cost, and ops roles grow. Agents act as force multipliers that raise expectations and make you always-available (remote agent control) ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Advice: learn what surrounds the LLM (ops, cost, verification), agent infrastructure (protocols, runtimes, memory; e.g. Anthropic buying Bun, OpenAI buying uv/ruff), and the hardware layer, which brings strong job security. Humans become agent orchestrators ([[episodes/explainable--163-hidden-cost-of-agents]]).
- Paradox: if agents replace most workers, who buys the products (Jira, Slack, Office) built for them? Alternatively, a Star Trek future where people pursue hobbies ([[episodes/explainable--163-hidden-cost-of-agents]]).
- "The end of programmers" vs the front line: building one multimodal feature to GA took 1.5 years of evals, cost, security, compliance, and plain old CI and networking work. Easy POCs, like website builders before them, raise the bar for what's expected rather than ending the job ([[episodes/osim-tochna--ai-in-production-reality-vs-imagination]], [[people/amit-bendor]]).
- Build vs buy: buying SaaS offloads liability (security, compliance such as data-access requests under EU or Israeli law, with fines on revenue). Saving a few million by vibe-coding your own system exposes you to far larger risks ([[episodes/osim-tochna--ai-in-production-reality-vs-imagination]]).
- AI as pair programmer brings back XP's pair programming, but you're only as good as your pair: seniors can hold a deeper dialogue with it. Gong keeps hiring aggressively ("hire 200, get the impact of 300") and calls fears of no more juniors "fake" ([[episodes/osim-tochna--gong-ai-for-developers]], [[people/ohad-parush]]).
- Learning a language still matters: "vibe coding will bridge it" is shallow and fails in practice ([[episodes/osim-tochna--gong-ai-for-developers]], [[people/ohad-parush]]).
- Inference optimization as job security: everyone builds agents, and they all have to run somewhere. Training is concentrated in few companies, but every company does inference, and low-level work (kernels, distributed serving) is still where coding agents are least autonomous ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- The new bottleneck is imagination, not coding skill: a mathematician who says he can't write code builds with Claude and Codex, and advises everyone to dream big because tools now realize much of it ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).

## Disagreements & open questions
- How far will it go? Matan Cohen is bullish that developers stay essential, moving up a level of abstraction ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]); the LangTalks hosts expect agents to eventually write everything, with even product decisions automatable ([[episodes/langtalks--63-wake-up]]).
- Optimistic take (Matan Cohen) versus the widespread view that AI will sharply reduce developer jobs ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).

## Takeaways

## Related
[[concepts/harness-engineering]] · [[concepts/agent-workspaces]] · [[concepts/autonomous-agents-outlook]] · [[concepts/llm-inference]]
