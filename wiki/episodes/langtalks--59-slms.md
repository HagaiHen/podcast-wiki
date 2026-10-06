---
type: episode
show: LangTalks
date: 2025-12-28
guests: ["[[people/elad-granot]]"]
spotify_url: https://open.spotify.com/episode/7a5a2Qu9ymY2tqBE83GGMF
source: whisper
raw: raw/langtalks/2025-12-28-59-slms-dr-elad-granot-trullion.md
---
# #59 — SLMs (Small Language Models) — with Dr. Elad Granot (Trullion)

[[people/elad-granot]] (AI researcher at Trullion, an AI finance platform for accountants and auditors) explains when to train small language models instead of calling a big LLM.
Use case: auditors receive one PDF bundling invoices, bank transfers, contracts, and inventory lists. It must be *segmented* into sub-documents and each one *classified*. Forcing a generative LLM to do segmentation (chunk IDs, "from ID x to y") is awkward; a fine-tuned segmentation model is natural.
Results versus Gemini 2.5 Flash: ~230× faster (before batching) and F1 rising from ~80% to over 90%, because the loss targets the task. Training data was synthetic but realistic: real public filings and invoices stitched together, giving labels for free.
Costs: datasets, tuning, training instabilities, serving (GPU servers, batching), and cost that only wins above some volume. Distillation from big models helps, but check the model license.
Bigger picture: LLM orchestrators with SLM specialists, privacy via on-device models, and tiny recursive models beating big ones on narrow benchmarks.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/small-language-models]] · [[concepts/model-selection]] · [[concepts/decision-classifiers]] · [[concepts/llm-pipelines]]
