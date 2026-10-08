---
type: episode
show: Startup for Startup
date: 2026-09-08
guests: ["[[people/roy-mann]]", "[[people/matan-lach]]"]
spotify_url: https://open.spotify.com/episode/7dPDL5oP5JyxP8hvixlooC
source: whisper
raw: raw/startup-for-startup/2026-09-08-366-qa.md
---
# #366 — How Do You QA the Agents We Build?

> Host: Daria Wertheim. Part of the "time capsule" series on current thinking about agents.

[[people/roy-mann]] and [[people/matan-lach]] (who leads Taka, an AI social media manager from monday's Agent Labs) discuss measuring agent quality when the same input never gives the same output.
Agents range from "pass the butter" task bots to personal assistants that must remember you; Taka went vertical because general agents lacked social-media expertise.
Testing has three levels: deterministic tool checks in CI, LLM-judged scenarios run many times, and production failures replayed until the judge catches them. Plus trait tests (honesty), a nightly "monkey farm" of LLM user personas, and frustration-triggered feedback.
Pitfalls: Sonnet "beat" Opus on short transactional tests, and tool loading breaks agents silently. Pass-rate trends across models show real prompt gains.
Advice: start quality work early. The experience is the product, and candor about what the agent couldn't verify builds trust.

**Show:** [[shows/startup-for-startup]]

**Concepts:** [[concepts/llm-evals]] · [[concepts/agent-architectures]] · [[concepts/context-engineering]] · [[concepts/ai-verification]]
