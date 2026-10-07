---
type: concept
hubs: [ai-engineering]
sources: 6
updated: 2026-10-07
---
# Small Language Models (SLMs)

**Summary:** Models from a few million to a few billion parameters (BERT/RoBERTa up to Qwen, Gemma, Phi, Llama sizes), fine-tuned for one task. Against general LLMs they trade breadth for speed, cost, privacy, and often *higher* accuracy on the target task, because the loss measures exactly that task. They also enable non-generative heads (segmentation, classification) that generative LLMs only imitate. The price is classic data-science work: datasets, training, evaluation, and serving. Lessons from the LLM era (distillation, chain-of-thought, RLHF, LLM-labeled data) make today's SLMs far stronger than same-size models of five years ago.

## Key ideas
- Latency, cost, and accuracy triangle: SLMs usually win latency and cost, and can win accuracy on a narrow task ([[episodes/langtalks--59-slms]], [[people/elad-granot]]).
- Generative LLMs need hacks for non-generative tasks, e.g. segmentation via chunk IDs; a purpose-built segmentation model just does it ([[episodes/langtalks--59-slms]]).
- Trullion's results versus Gemini 2.5 Flash: ~230× faster pre-batching; F1 ~80% → 90%+ ([[episodes/langtalks--59-slms]]).
- Data: synthetic-but-real composites (stitch real filings and invoices into bundles) give free labels; for conversational data, real user messages beat synthetic ones ([[episodes/langtalks--59-slms]]).
- Other labeling routes: existing similar datasets, domain experts with labeling tools, teacher-student (distillation) from a large model, which caps you near the teacher. Many model licenses forbid using outputs to train other models ([[episodes/langtalks--59-slms]]).
- Training pitfalls: hyperparameter tuning, exploding or vanishing gradients; tools include SageMaker for GPU training and Weights & Biases or TensorBoard for experiments. Fine-tuning a pretrained model can take just hours ([[episodes/langtalks--59-slms]]).
- Serving: self-hosted GPU servers with request batching, or managed and on-demand GPU platforms. Cost beats per-token APIs only above some request volume ([[episodes/langtalks--59-slms]]).
- Architecture: LLM orchestrator plus SLM specialist agents ([[episodes/langtalks--59-slms]]).
- Privacy: small models can run on-device, opening AI to banks and healthcare ([[episodes/langtalks--59-slms]]).
- Samsung's Tiny Recursive Model (~7M parameters) beat much larger models on some reasoning benchmarks ([[episodes/langtalks--59-slms]]).
- Custom training is opening up: AWS Nova Forge continues training from early foundation checkpoints on your data mix (more data than fine-tuning, but escaping local minima and catastrophic forgetting); Thinking Machines' Tinker is similar ([[episodes/langtalks--58-reinvent-predictions]], [[people/shuki-cohen]]).
- Encoder-only small models for classification are very fast and reliable ([[episodes/langtalks--58-reinvent-predictions]]).
- From POC to production: a big-model agent workflow that took three days on large customer networks (vs five hours expected) was fixed by splitting tasks across small fine-tuned models with an orchestrator, then optimizing inference from driver to model configuration ([[episodes/hidden-layers--dream-eran-hoffman]], [[people/eran-hoffman]]).
- At hundreds of millions of files a day, frontier LLMs are ~100× too expensive for classification. Cyera trains its own encoder-decoder models, self-hosted with GPU-optimized inference, which are cheaper, faster, and more accurate because guardrails and context are built in (a lawyer's brochure phone number isn't sensitive) ([[episodes/hidden-layers--cyera-shiran-bareli]], [[people/shiran-bareli]]).
- Logs too big for context: have a model write code (e.g. pandas over the logs) in a self-hosted sandbox instead of reading raw logs. Vega is distilling this from strong-model runs into small Qwen models (4B, 30B-A3B), possibly split into a coder and a summarizer ([[episodes/hidden-layers--vega-gili-kanfo]], [[people/gili-kanfo]]).
- Edge recipe: train the best model without constraints, then distill. Nexar's 300M V-JEPA teacher taught 86M and 22M ViT students to match its internal features, nearly matching it. Latency fell from ~2.5 s per window to ~30 ms end to end on a Jetson Thor after moving preprocessing from CPU to GPU, fp16, and torch.compile kernel fusion ([[episodes/hidden-layers--nexar-roni-goldshmidt]], [[people/roni-goldshmidt]]).
- Small vision-language models can reason: a fine-tuned 2B Qwen handles video Q&A and textual explanations of alerts ([[episodes/hidden-layers--nexar-roni-goldshmidt]], [[people/roni-goldshmidt]]).

## Disagreements & open questions
- Regression or evolution? Granot argues returning to small models is evolution, built on what LLMs taught us ([[episodes/langtalks--59-slms]]).

## Takeaways
- [ ] For segmentation or classification inside a pipeline, benchmark a fine-tuned small model against your LLM call ([[episodes/langtalks--59-slms]])
- [ ] Generate labeled training data by composing real documents synthetically ([[episodes/langtalks--59-slms]])
- [ ] Check model licenses before using an LLM to label training data ([[episodes/langtalks--59-slms]])

## Related
[[concepts/model-selection]] · [[concepts/decision-classifiers]] · [[concepts/llm-pipelines]] · [[concepts/open-weight-models]] · [[concepts/multi-agent-orchestration]] · [[concepts/hebrew-llms]]
