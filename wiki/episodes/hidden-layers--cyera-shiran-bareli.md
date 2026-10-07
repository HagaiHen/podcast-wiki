---
type: episode
show: Hidden Layers
date: 2026-05-31
guests: ["[[people/shiran-bareli]]"]
spotify_url: https://open.spotify.com/episode/48P7NYRYFxKRYrrPrARj72
source: whisper
raw: raw/hidden-layers/2026-05-31-ai-cyera.md
---
# Advanced AI Research at a Cyber Company — with Shiran Bareli (Cyera)

[[people/uri-eliabayev]] talks with [[people/shiran-bareli]], VP Research at Cyera (founded 2021; data security posture management, DLP, and now AI security).
Classifying sensitive data across hundreds of millions of files a day rules out frontier LLMs on cost. Cyera splits the task into entity-level detection (credit cards, names) and document-level sensitivity (an M&A memo is sensitive even with no personal data), uses big LLMs plus a cross-functional committee and judges to build ground truth, then trains its own encoder-decoder models, self-hosted and GPU-optimized. The result is cheaper, faster, and more accurate, because context matters (a lawyer's brochure phone number isn't sensitive).
AI assistants plugged into Drive, M365, and Notion made the old access-governance problem far harder: over-permissioned users can now simply ask. Agents add intent problems: inventory every agent, check what data it can reach, detect out-of-scope actions, and watch for injected or insider prompts.
Also: match architecture to the problem (encoders for extraction, fine-tuned open decoders for explained risk scoring); a dedicated team drives safe AI adoption for non-technical staff; vulnerability research is their biggest token user ("a giant magnet for the needle in the haystack").

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/small-language-models]] · [[concepts/agent-security]] · [[concepts/model-selection]] · [[concepts/llm-evals]]
