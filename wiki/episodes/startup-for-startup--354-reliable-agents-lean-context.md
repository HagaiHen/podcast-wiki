---
type: episode
show: Startup for Startup
date: 2026-06-16
guests: ["[[people/doron-bleiberg]]"]
spotify_url: https://open.spotify.com/episode/55SDECEOJj6p99WtVqkdKj
source: whisper
raw: raw/startup-for-startup/2026-06-16-354.md
---
# #354 — Building Reliable Agents Without Overloading Context

A ten-minute conference talk by [[people/doron-bleiberg]] (AWS solutions architect, and bootstrapped co-founder of a coding agent for Minecraft plugins).
Common mistakes: prohibitions ("don't", "never"), which put attention on the unwanted thing; corrective if-this-then-that patches added after failures; context rot in long-running agents; and re-teaching the model knowledge it already has.
The paradox: we want to give the agent everything, but every token competes for attention, costs money, and slows it down.
Four principles: evaluate what the model already knows (run several times; include only what it gets wrong); attention pull (say what to do, e.g. "output Markdown", "answer from the user's point of view"; avoid implicit hints in eval questions); prefer prevention over correction; and progressive disclosure (minimal system prompt; load task instructions, skills, knowledge, and tool details only when needed, even via hooks at tool invocation).

**Show:** [[shows/startup-for-startup]]

**Concepts:** [[concepts/context-engineering]] · [[concepts/skill-engineering]] · [[concepts/llm-evals]]
