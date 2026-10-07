---
type: episode
show: Hidden Layers
date: 2026-07-01
guests: ["[[people/avi-golan]]"]
spotify_url: https://open.spotify.com/episode/6xX2AqmL4x7TZKNFtXEthy
source: whisper
raw: raw/hidden-layers/2026-07-01-ai-alice.md
---
# How Do You Keep the World's Strongest AI Models From Going Rogue? — with Avi Golan (Alice)

[[people/uri-eliabayev]] talks with [[people/avi-golan]] of Alice (formerly ActiveFence, founded 2018; it began by finding ISIS videos and child-safety content for big platforms).
Alice now red-teams models and harnesses for 8 of the 10 largest foundation-model labs before release. Close to 100 security researchers and PhD-level experts (child safety, terror, misinformation) hunt novel jailbreaks, backed by an internal attack database ("Rabbit Hole").
Training data has shifted from RLHF preference labels to RL "gyms": simulated environments (e.g. a fake e-commerce site with seller agents) with expert-built tasks and evaluators, whose failures feed post-training. In the past six months models got much harder to break, so the work shifted from automated to expert-manual.
For enterprises: defining policies is half the work (may a chatbot recommend a competitor? give financial advice per country?). Defense is layered; observe for drift; and beware the "lethal trifecta": untrusted input, sensitive data, and the ability to act.
Prediction: enterprises will fine-tune open-weight models on their own failure cases, because 1-in-100 errors are catastrophic at scale.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/ai-red-teaming]] · [[concepts/agent-security]] · [[concepts/ai-guardrails]] · [[concepts/llm-evals]] · [[concepts/open-weight-models]]
