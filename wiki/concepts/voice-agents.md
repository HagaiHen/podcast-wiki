---
type: concept
hubs: [ai-engineering]
sources: 3
updated: 2026-10-06
---
# Voice Agents

**Summary:** Two architectures. **Speech-to-speech** (OpenAI Realtime, Gemini Live): audio in, audio out, low latency, preserves tone and intonation, but today's models follow instructions roughly at a GPT-3.5 level and degrade with long contexts. **Chained** (STT → LLM → TTS): reuses your whole chat stack (graphs, evals), is more robust with swappable providers, but adds latency and points of failure and loses emotion. Either way, natural conversation needs deterministic scaffolding around the model, latency tricks, and audio-aware evaluation.

## Key ideas
- Trade-offs: latency versus instruction following, tool calling, accuracy, and robustness. A 911 admin line can't afford dropped calls, which pushed one host to the chained approach ([[episodes/langtalks--61-voice-agents]], [[people/shay-davidson]]).
- LLMs are driven by input tokens and silence isn't a token. Behaviors like "still there?" after N seconds of silence, escalation to a human, or ending the call need a state machine around the websocket (e.g. XState) ([[episodes/langtalks--61-voice-agents]]).
- Delegate hard intents: the realtime agent handles chit-chat plus a customer record in context, and routes real requests through a single "answer" tool to Lemonade's existing text support engine (200+ intents) ([[episodes/langtalks--61-voice-agents]]).
- Latency budget: email support tolerates minutes, phone about 10 seconds. A "fast" strategy (cheaper models, skipped validation and composition steps) on the same engine, plus filler phrases and hold music ([[episodes/langtalks--61-voice-agents]]).
- Semantic VAD (voice activity detection) waits longer when a sentence sounds unfinished, and can be tuned by prompt ("be more patient") ([[episodes/langtalks--61-voice-agents]]).
- Telephony adds latency (jitter buffers); network is no longer negligible ([[episodes/langtalks--61-voice-agents]]).
- OpenAI's Responses API and managed RAG (e.g. AWS Knowledge Bases) cut round-trips by running tools and retrieval server-side ([[episodes/langtalks--61-voice-agents]]).
- Fine-tuning the voice on about a minute of well-recorded speech improved tone more than prompting ([[episodes/langtalks--61-voice-agents]]).
- Quirks: speech-to-speech models sometimes laugh, change pitch, play "hold music", or answer in the user's own voice ([[episodes/langtalks--61-voice-agents]]).
- Disclosure that it's an AI makes ~30% of callers start with one word; a short, refined reply ("I can help with a lot, tell me more, or I'll transfer you") builds trust ([[episodes/langtalks--61-voice-agents]]).
- Infra gap: delegating reasoning asynchronously so the speech model can start talking and weave in the answer later; async tool calling (Nova Sonic 2 keeps speaking while tools run). Voice evals are far less deterministic than text, and replaying or editing parts of a conversation is hard ([[episodes/langtalks--58-reinvent-predictions]]).
- Early builders had to write their own voice orchestration (interruptions, end-of-turn, language switching, slower speech for elderly callers) before libraries like LiveKit/Pipecat existed ([[episodes/ignore-instructions--24-wonderful-road-to-100m]]).

## Disagreements & open questions
- Speech-to-speech versus chained: Lemonade chose realtime for naturalness; the host's 911 product chose chained for robustness, now reconsidering as multimodal improves ([[episodes/langtalks--61-voice-agents]]).

## Takeaways
- [ ] Wrap realtime voice models in a state machine for silence, escalation, and call-ending behaviors ([[episodes/langtalks--61-voice-agents]])
- [ ] Route complex voice intents to an existing text engine via one tool, with a latency-optimized strategy ([[episodes/langtalks--61-voice-agents]])
- [ ] Evaluate calls by feeding the *audio* (not just transcripts) to an LLM judge ([[episodes/langtalks--61-voice-agents]])

## Related
[[concepts/llm-evals]] · [[concepts/llm-pipelines]] · [[concepts/model-selection]]
