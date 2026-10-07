---
type: episode
show: Hidden Layers
date: 2026-04-23
guests: ["[[people/roni-goldshmidt]]"]
spotify_url: https://open.spotify.com/episode/5cXDvrMjSojz1vbdbovBGP
source: whisper
raw: raw/hidden-layers/2026-04-23-ai-nexar.md
---
# AI Models That Understand the World — with Roni Goldshmidt (Nexar)

[[people/uri-eliabayev]] talks with [[people/roni-goldshmidt]], AI researcher at Nexar (dashcams and collision prediction), about local models and world models.
Open models (half a million on Hugging Face; the Chinese labs lead) trail the frontier by roughly six months, and you choose and manage the model yourself, unlike a closed product with routers and system prompts. Local isn't automatically cheaper: Gemini Flash beat a strong Qwen on video classification *and* cost less than the A100 hour needed to host it. Open models win on domain fine-tuning (real fine-tuning and LoRA vs weak closed-model tuning), privacy-sensitive subtasks routed from a main agent, and possibly per-user fine-tuned personal agents.
World models: LeCun argues next-token prediction lacks common sense, while V-JEPA learns by predicting masked latents rather than pixels. Nexar fine-tuned V-JEPA 2 and autoregressive video models (Cosmos) on about 2M clips ending in crashes or near misses vs normal driving. V-JEPA led by about 7 points, generalized to other customers' cameras, and even flagged imminent collisions in generated videos of dinosaurs and spaceships (a "BADAS moment").
Engineering: moving preprocessing to the GPU took per-window latency from ~2.5 s to under 1 s, and with fp16 and compilation it runs end to end in ~30 ms on a Jetson Thor. Distillation into 86M and 22M students nearly matched the 300M teacher. Attention maps show the model looking ahead along an object's path.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/world-models]] · [[concepts/open-weight-models]] · [[concepts/small-language-models]] · [[concepts/model-selection]]
