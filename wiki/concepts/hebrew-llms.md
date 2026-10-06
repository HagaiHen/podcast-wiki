---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# Hebrew LLMs (adapting models to a low-resource language)

**Summary:** Hebrew is a morphologically rich language: prefixes and suffixes fuse into words ("the computer", "to the computer"), so statistical BPE tokenization splits it poorly and models see little Hebrew in training. Building a Hebrew model means continued pre-training (CPT) of an open base model. The base choice is decided less by benchmark strength than by tokenizer efficiency, openness of data and recipes, licensing, and whether the model is still *trainable*. Hebatron, built on NVIDIA Nemotron by PwC Next with Israel's national AI program, is the main worked example.

## Key ideas
- Tokenizer compression ratio largely predicts success: Mistral's tokenizer (used by Nemotron) gives ~2.5–2.6 tokens per Hebrew word, while Granite or Llama are ~5. More tokens per word means harder next-token prediction and a shorter effective context ([[episodes/explainable--157-training-hebatron]]).
- Base vs instruct: literature and experience favor base models. Heavily engineered instruct models (Cohere's Aya, with iterative preference-optimization data and model merging) resisted improvement even though Aya led Hebrew leaderboards ([[episodes/explainable--157-training-hebatron]]).
- Pick the most trainable base, not the strongest: a model stacked with undocumented tricks is "mumbo jumbo that works" and can't be improved further ([[episodes/explainable--157-training-hebatron]]).
- Nemotron (released around December, Mamba + mixture-of-experts) ran ~7× faster than alternatives and released all its data, including SFT data, so you can restart from zero ([[episodes/explainable--157-training-hebatron]]).
- Mixture-of-experts in a new language: expert-routing entropy collapses in late layers for Hebrew (most experts go unused). An auxiliary load-balancing loss spreads experts, temporarily hurting reasoning while adding knowledge ([[episodes/explainable--157-training-hebatron]]).
- Data mixing by *content* (TF-IDF clustering into topics), not source, beats source-based mixing in theory (UtilityMax-style). In practice, frequent base-model switches and order effects made it unusable ([[episodes/explainable--157-training-hebatron]]).
- Benchmarks translated and localized into Hebrew (GSM8K, HellaSwag, Winograd) plus psychometric tests; trivia and reasoning can move in opposite directions ([[episodes/explainable--157-training-hebatron]]).

## Disagreements & open questions
- The national AI program recommended starting from Aya as the strongest Hebrew model; the team found it untrainable and switched to Nemotron ([[episodes/explainable--157-training-hebatron]]).

## Takeaways
- [ ] When adapting a model to a new language, compare tokenizer tokens-per-word before anything else ([[episodes/explainable--157-training-hebatron]])

## Related
[[concepts/llm-pretraining]] · [[concepts/open-weight-models]] · [[concepts/llm-evals]] · [[concepts/small-language-models]]
