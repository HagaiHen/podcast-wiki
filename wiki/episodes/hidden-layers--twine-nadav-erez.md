---
type: episode
show: Hidden Layers
date: 2026-05-03
guests: ["[[people/nadav-erez]]"]
spotify_url: https://open.spotify.com/episode/50hedszyjEXCucmdoNLi0j
source: whisper
raw: raw/hidden-layers/2026-05-03-twine.md
---
# Digital Employees in Cybersecurity — with Nadav Erez (Twine)

[[people/uri-eliabayev]] talks with [[people/nadav-erez]], CTO and co-founder of Twine, which builds "digital employees" for security, starting with "Alex" for identity and access management.
Not a copilot: Alex owns a KPI (everyone has exactly the access they need, when they need it) and works continuously, replacing quarterly review cycles with daily ones. It runs on off-the-shelf LLMs, with the value in a rich, constantly enriched data layer and a knowledge layer of org policies and exceptions. Where no written policy exists, it infers practice from a year of tickets.
Scoped per-page agents didn't survive real users, so they moved to one agent loading skills, including awareness of what's on the user's screen; evals improved immediately.
Trust is earned gradually: first read-only data gathering on escalated tickets (e.g. why a user keeps getting locked out), then a "control membrane" mapping each action and context to an approval level. A deterministic plan is executed with no AI between approval and execution, alongside audit logs, undo, an honest "I don't know", and a "raise issue" tool for async tasks.
Vision: sibling agents (vulnerabilities, network) sharing one data fabric, and a CISO who sets objectives that cascade into KPIs and tasks.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/agent-workspaces]] · [[concepts/ai-guardrails]] · [[concepts/skill-engineering]] · [[concepts/agent-memory]]
