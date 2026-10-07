---
type: episode
show: Hidden Layers
date: 2026-05-26
guests: ["[[people/tom-barnea]]"]
spotify_url: https://open.spotify.com/episode/0b4RGLT8X5Oe7eyvvj1st4
source: whisper
raw: raw/hidden-layers/2026-05-26-ai-tenable.md
---
# How Do You Secure AI Tool Use in the Organization? — with Tom Barnea (Tenable)

[[people/uri-eliabayev]] talks with [[people/tom-barnea]], who leads AI-security detections at Tenable (exposure management; it acquired the AI-security startup Apex).
AI risk differs from classic attacks. Instead of moving from a weak user to a big server, someone with one user's access can simply ask a connected assistant for exactly the sensitive data they want. Because everyone can now build agents, many incidents involve HR, finance, or the business rather than the security team. Example: employees asking the company copilot about quarterly results right before publication, hinting at insider trading.
Other risks: over-reliance (asking AI about chemical mixtures, medical questions, or student grades), self-promotional indirect prompt injection (hidden instructions in sites or résumés), and agents shared with too-broad permissions (one opened a user's org chat history to the internet by misconfiguration). Vendor admin consoles offer far fewer controls for AI than for cloud, and none are aligned across vendors.
Detection needs AI: semantic classifiers trained on labeled data, plus tightly scoped judge agents in production, built by security researchers paired with data scientists.
Next: orchestrated multi-agent workflows, where each agent may be safe alone but the connections between them open new risk.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/agent-security]] · [[concepts/ai-guardrails]] · [[concepts/multi-agent-orchestration]]
