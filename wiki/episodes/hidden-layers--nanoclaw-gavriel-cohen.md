---
type: episode
show: Hidden Layers
date: 2026-05-21
guests: ["[[people/gavriel-cohen]]"]
spotify_url: https://open.spotify.com/episode/6GnM3IfX26smvdFedJUreq
source: whisper
raw: raw/hidden-layers/2026-05-21-ai-nanoclaw.md
---
# Building Secure AI Agents for Organizations — with Gavriel Cohen (NanoClaw)

[[people/uri-eliabayev]] talks with [[people/gavriel-cohen]] (ex-Wix developer, then PR, now founder of NanoCo) about how NanoClaw came about.
Running an AI-native marketing agency with his brother, he tried OpenClaw in a WhatsApp group; within a day it was running their sales pipeline with morning task assignments. His thesis on why it works: a coding agent plus a *persistent* environment plus messaging apps plus internet access yields memory, self-built tools, scheduled jobs, and autonomy (an agent that set itself a daily cron job to watch stroller prices for his wife).
But he saw problems: plaintext logs of every WhatsApp chat, app-level rather than OS-level sandboxing, and unvetted dependencies. So in two days he built NanoClaw: a small codebase anyone can audit in an hour, each agent in its own container, and capabilities hard-wired outside the model.
After a Hacker News launch and a Karpathy thread praising its lean, customizable approach, it grew past 28k GitHub stars; Singapore's foreign minister published his own fork with an LLM-wiki memory. New versions add multiple channels per agent, a credential vault behind a proxy, and human-in-the-loop approvals frozen in flight.
Vision: every employee delegates to their own agent, then teams run dozens or hundreds. Isolate agents and enforce the perimeter rather than policing every tool call.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/personal-ai-assistants]] · [[concepts/agent-security]] · [[concepts/llm-wiki]]
