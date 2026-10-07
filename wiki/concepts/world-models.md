---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# World Models (beyond next-token prediction)

**Summary:** A push to move AI from predicting the next text token toward models that understand the physical world, for robotics, autonomous driving, and long-term planning. "World model" is overloaded: it covers video generators that predict frames (Decart, Genie), 3D scene builders (Fei-Fei Li's Gaussian splats), and Yann LeCun's JEPA family, which predicts abstract latent representations instead of pixels. Critics of frame prediction argue it's wasteful and weakly tied to intelligence. Latent approaches can represent uncertainty properly but are not yet proven at scale.

## Key ideas
- Plato's cave: LLMs learn from a text projection of the world, like prisoners seeing shadows. They don't know what a person is, or how beer tastes ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- Next-frame prediction over all of YouTube is infeasible and no human does it; it has a weak link to intelligence ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- JEPA (Joint Embedding Predictive Architecture, from LeCun's AMI lab): encode two frames and minimize the distance between their latents. A car approaching a three-way split is predicted as a one-third chance for each branch, where a video model must pick one path and is wrong two-thirds of the time ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- Collapse problem: both encoders could output the zero vector. Fix: regularize the distribution of embeddings (VICReg: variance, invariance, covariance; then SIGReg: just an isotropic Gaussian) ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- JEPA limits: it's non-generative, so it can't produce text, and it's unproven at scale; one paper shows it needs data with particular distributional properties ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- Gaussian splats represent images as sums of Gaussians, which have no order, so transformers drop positional encoding to become set-invariant ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- New paradigms start as underdogs (LeCun and Bengio struggled to publish on neural nets), but with AI money even a $1B+ lab is an underdog bet ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).

## Disagreements & open questions
- More compute vs new architectures: Levi grants that "add compute and data" keeps working for many cases (ViT, AlphaFold 3) but argues diminishing returns (10× compute for 99% → 99.9%) open the door to cheaper approaches ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).

## Takeaways

## Related
[[concepts/continual-learning]] · [[concepts/llm-pretraining]] · [[concepts/multimodal-llms]]
