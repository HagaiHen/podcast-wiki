---
type: episode
show: AI Engineering (AI אנג׳נירינג)
date: 2026-08-27
guests: ["[[people/tomer-brook]]"]
spotify_url: https://open.spotify.com/episode/0zUJmUhJD4O42NeqvMCcld
source: whisper
raw: raw/ai/2026-08-27-atlas-from-agent-to-ai-teammate.md
---
# Atlas: From Agent to AI Teammate — with Tomer Brook (monday.com)

[[people/netanel-abergel]] and [[people/tomer-brook]] (engineering manager, agentic developer platform) tell how monday.com took one coding agent, Atlas, from cloud Claude Code that produced thousands of unwanted PRs to a teammate whose PRs ship.
What it took: an eval "council of the wise" (LLM judges plus CI signals), CI failures fed back into the same session and memory, self-testing skills (MirrorD deploys, Playwright, screenshots and video on the PR), and PR guardrails shifted left to spec and pre-commit.
Agents are teammates with identities in Slack, monday, and GitHub, an LLM wiki of team context, session retros, and a shared base agent that collects everyone's lessons.
Results: ~15% of PRs come from remote agents and ~50% of those ship untouched. The bottleneck is now review; next are auto-merge and agentic releases.
Advice: start with one concrete problem such as bug duty. Brook also dropped sprints for kanban.

**Show:** [[shows/ai-engineering-podcast]]

**Concepts:** [[concepts/agent-workspaces]] · [[concepts/ai-sdlc]] · [[concepts/ai-guardrails]] · [[concepts/ai-verification]] · [[concepts/llm-evals]] · [[concepts/memory-consolidation]] · [[concepts/llm-wiki]] · [[concepts/future-of-software-engineering]]
