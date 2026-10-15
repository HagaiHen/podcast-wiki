---
type: episode
show: "Startup for Startup"
date: 2026-10-13
guests: ["[[people/raz-diskin]]", "[[people/moshe-krispin]]"]
spotify_url: https://open.spotify.com/episode/1hP8dGqKBFQpTAPFVCAdrs
source: whisper
raw: raw/startup-for-startup/2026-10-13-370.md
---
# #370 — How We Cut Agent Building From a Month to a Day

> Host: Yael Avdi (product lead, Startup for Startup).

[[people/raz-diskin]] (go-to-market engineer) and [[people/moshe-krispin]] (tech lead) of monday.com's RevAI team describe AgentOS, the internal platform behind their sales agents Amanda (inbound leads who asked for sales) and Jax (new signups).
Agents moved "from rails to a cage": maximum freedom, with business rules (no 2 a.m. calls) enforced as system policies that block the action and explain why, which also lets prompts get shorter.
An Agent Definition Language compiled into a runtime on LangChain's Deep Agents lets GTM engineers change or build agents without developers, while engineers harden the platform.
Results: a 35–45% meeting rate, thousands of meetings a month, and sourced pipeline rising from $3–4M to $8.5M a month, with individual-level personalization and long-term memory per lead.
Current problems are cost (~$1.50 per run; a model router is on the way) and deciding which new tech to adopt; the next step is self-improving agents. Closing advice: don't be afraid, build a small POC.

**Show:** [[shows/startup-for-startup]]

**Concepts:** [[concepts/ai-guardrails]] · [[concepts/harness-engineering]] · [[concepts/ai-growth-marketing]] · [[concepts/agent-memory]] · [[concepts/llm-cost-optimization]] · [[concepts/ai-hype]]
