---
type: episode
show: AI Engineering (AI אנג׳נירינג)
date: 2026-09-30
guests: ["[[people/sharon-dahan]]"]
spotify_url: https://open.spotify.com/episode/05bl2sW0hcP4Kgt8wCRCMN
source: whisper
raw: raw/ai/2026-09-30-why-your-llm-costs-so-much.md
---
# Why Your LLM Costs So Much — with Sharon Dahan (Impala)

[[people/sharon-dahan]], an architect at the inference company Impala, explains what happens behind a chat-completion call: model size × quantization = memory; tensor and data parallelism; mixture-of-experts; the KV cache; and why idle GPUs, like idle taxis, lose money.
Generic API pricing carries big margins, so latency-insensitive workloads can run for a fraction of the price.
On model choice: size isn't everything. Narrow the task, reframe the question, and manage context aggressively. A ship-ERP agent went from 85% to 97% on evals through context management alone.
Also covered: Chinese open-weight models (open weights aren't code), agents that interrupted each other and blocked a workday, an agent deleting a DB, and why to ignore any AI hype that hasn't survived a month.

**Show:** [[shows/ai-engineering-podcast]]

**Concepts:** [[concepts/llm-inference]] · [[concepts/model-selection]] · [[concepts/open-weight-models]] · [[concepts/context-engineering]] · [[concepts/ai-guardrails]] · [[concepts/ai-hype]]
