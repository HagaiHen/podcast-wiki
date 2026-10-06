---
type: episode
show: ExplAInable
date: 2026-09-13
guests: []
spotify_url: https://open.spotify.com/episode/1F2wrHMORXbT5U3zEEl9nu
source: whisper
raw: raw/explainable/2026-09-13-163.md
---
# #163 — A Million Dollars a Month: The Dark (and Expensive) Secret of AI Agents

The two hosts (Mike and a co-host who works on LLM inference cost optimization) debate whether agents will replace developers, starting from economics. Running 100 Codex agents nonstop for a month reportedly costs ~$1M in tokens. One agency estimates ~$500k just to build a working multi-agent system. Subscriptions are subsidized roughly 1:10 (a heavy $200 plan is ~$1.5–2k at API prices).
Risks: vendor lock-in, silent model downgrades under load, outages ("Claude is down, go home"), and account bans. Agents need real-time supervision (a vending-machine agent was talked into giving products away), and probabilistic agents add entropy to complex systems, which only humans can order.
Examples: a million-line AI-written PR porting Bun from Zig to Rust alarmed the community; a professor found 60% of working LLM-written code irrelevant.
Agents excel in code and math because of RL with verifiable rewards. Taste-driven domains lag, so "agents replace everyone" may be a tech bubble.
Advice: learn what surrounds the LLM (ops, cost, verification), agent infrastructure (protocols, runtimes, memory), and the hardware layer. Humans become agent orchestrators.

**Show:** [[shows/explainable]]

**Concepts:** [[concepts/llm-cost-optimization]] · [[concepts/ai-gateway]] · [[concepts/ai-verification]] · [[concepts/ai-guardrails]] · [[concepts/future-of-software-engineering]] · [[concepts/llm-reasoning]]
