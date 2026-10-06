---
type: episode
show: LangTalks
date: 2026-09-22
guests: []
spotify_url: https://open.spotify.com/episode/3ANjh65zIFIAMAWJGwR0N6
source: whisper
raw: raw/langtalks/2026-09-22-74-jev.md
---
# #74 — Jev

The hosts deflate the hype around Jev, a new *classification* model (not an LLM): you give it a state (like a system prompt) and typed questions (boolean or labels, each with an instruction), and it returns calibrated confidences for many questions in one non-autoregressive pass.
What's new: free-text labels, calibration (a 20% means 20%), batching, and RL training on *decision points* in conversations. A cheap LLM such as Gemini Flash could do similar work, at roughly 30–100× the cost and 2–9 s versus about 0.25 s.
Good fits: bulk filtering (RAG and repo selection, Slack events), PR risk scoring, ranking DOM elements for browser agents, judging tool calls or AGENTS.md compliance in a harness hook.
Bad fits: anything needing reasoning or text generation after the decision. It's a black box when wrong. Don't break agents into decision trees. Benchmark it, and keep an LLM fallback.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/decision-classifiers]] · [[concepts/rag]] · [[concepts/llm-cost-optimization]] · [[concepts/ai-hype]] · [[concepts/ai-guardrails]]
