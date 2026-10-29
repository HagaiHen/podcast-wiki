---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-29
---
# Synthetic Data

**Summary:** Generated training and test data, used where real data is too rare (edge cases you'd wait years to see), too sensitive to train on (customer data in regulated enterprises), or stale because the world changed. Done naively it fails in two ways. Asking an LLM for "ten examples" yields one narrow cluster, and training on it collapses the model onto a subset of the problem. Letting a single LLM label the data adds noise and inconsistency. Plurai addresses diversity by decomposing the task into dimensions and covering combinations, and accuracy by a multi-agent debate that keeps a label only on full consensus. Done right, around a thousand examples can train a small model that beats frontier LLMs on its task, and the data is regenerated whenever production drifts. A cheaper variant stitches real documents into synthetic composites that come with free labels.

## Key ideas
- Synthetic-but-real composites: stitch real filings and invoices into bundles for free labels; for conversational data, real user messages beat synthetic ones ([[episodes/langtalks--59-slms]], [[people/elad-granot]]).
- Three motivations: simulating edge cases (as with car crashes, you can't wait to meet every one); training when customer data is too sensitive, as even the largest enterprises can't train on it; and avoiding "dogfooding" bias, where a model trained on your own company's usage surprises you at customers, because every domain differs ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/ilan-kedar]]).
- Challenge 1, diversity: an LLM asked for examples produces one cluster, and training or testing on it leads to model collapse. Plurai's task-dimension decomposition splits the problem into dimensions; more dimensions gave better generalization and coverage of the real-world test distribution (their ICML paper) ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/ilan-kedar]]).
- Challenge 2, faithfulness: a single LLM labeler is noisy, which leaves the dataset "worth nothing" and convinces teams synthetic data doesn't work. Instead, several agents each argue a thesis for a label over multiple rounds, and a label enters the dataset only on full consensus ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/ilan-kedar]]).
- Results: small models trained this way were more accurate than GPT-5 while much cheaper and faster, across finance, health care, customer support and security benchmarks ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/ilan-kedar]]).
- Ongoing, not one-off: monitor production, and on drift or a new use case (e.g. a pandemic bringing new support complaints) generate fresh examples tuned to that moment ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/ilan-kedar]], [[people/uri-eliabayev]]).
- For agents, synthetic data isn't only text: it includes which tool was called and which process was chosen across multi-step trajectories ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/uri-eliabayev]]).

## Disagreements & open questions
- Does synthetic data work? Opinions in industry and research are split; Ilan Kedar argues failures come from naive generation and single-LLM labeling, not the idea ([[episodes/hidden-layers--plurai-ilan-kedar]]).

## Takeaways
- [ ] When generating synthetic data, list the task's dimensions first and generate across their combinations, not "give me ten examples" ([[episodes/hidden-layers--plurai-ilan-kedar]])
- [ ] Label synthetic data with several models and keep only examples they agree on ([[episodes/hidden-layers--plurai-ilan-kedar]])

## Related
[[concepts/small-language-models]] · [[concepts/llm-evals]] · [[concepts/model-selection]]
