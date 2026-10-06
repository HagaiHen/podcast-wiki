---
type: episode
show: LangTalks
date: 2026-07-26
guests: ["[[people/gavriel-cohen]]"]
spotify_url: https://open.spotify.com/episode/2CPkGP3492fqgihOY0oNKA
source: whisper
raw: raw/langtalks/2026-07-26-71-claw-architectures-gavriel-cohen-nanoclaw.md
---
# #71 — Claw Architectures — with Gavriel Cohen (NanoClaw)

[[people/gavriel-cohen]] built NanoClaw after OpenClaw quickly ran his AI-native agency's sales funnel but proved too insecure to trust with customer data.
His threat model assumes any agent can be prompt-injected through email, PRs, or websites, so the architecture must not rely on the agent behaving. Each agent runs in its own container; an orchestrator routes messages; credentials live in an external vault-proxy (OneCLI) that injects them per host; and sensitive actions (sending email, rewiring agents) need human approval executed outside the container.
He chose the Claude Agent SDK as the harness: the subscription covers it, the ecosystem is shared, and Anthropic optimizes it. His view is that models aren't portable.
"AI-native open source": contributions come as *skills* that teach your agent to customize your fork, keeping the core lean and enabling bespoke software. Co-host Gal says he barely reads diffs now, relying on proof of work.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/agent-security]] · [[concepts/personal-ai-assistants]] · [[concepts/skill-engineering]] · [[concepts/model-selection]] · [[concepts/ai-verification]]
