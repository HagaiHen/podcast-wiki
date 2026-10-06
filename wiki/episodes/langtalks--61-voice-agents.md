---
type: episode
show: LangTalks
date: 2026-01-24
guests: ["[[people/shay-davidson]]"]
spotify_url: https://open.spotify.com/episode/07PvAbAQ5dN7HTMP9Jienp
source: whisper
raw: raw/langtalks/2026-01-24-61-voice-agents-shay-davidson-lemonade.md
---
# #61 — Voice Agents — with Shay Davidson (Lemonade)

[[people/shay-davidson]], principal engineer at Lemonade, built "Maya", a phone support agent on OpenAI's Realtime API that OpenAI later showcased. A host who builds 911 admin-call agents compares it with the *chained* approach (speech-to-text → LLM → text-to-speech).
Speech-to-speech keeps tone and intonation and is fast, but the models are weaker at instruction following. Chained is more robust (swap providers per component) and reuses your chat stack, but adds latency and loses emotion.
Lemonade wraps the realtime model in a state machine (XState) for deterministic behaviors such as silence prompts and escalation, and delegates complex intents to its existing 200-intent text support engine via one "answer" tool, using a "fast" strategy, filler phrases, and hold music.
Also covered: semantic voice-activity detection, telephony latency (jitter buffers), a back office with live browser simulations, LLM-as-judge on raw *audio*, persona "avatars" for testing, and voice fine-tuning from about a minute of recorded speech.
Production surprise: ~30% of callers start with one word ("human", "cancel"), handled with a trust-building prompt.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/voice-agents]] · [[concepts/llm-evals]] · [[concepts/llm-pipelines]]
