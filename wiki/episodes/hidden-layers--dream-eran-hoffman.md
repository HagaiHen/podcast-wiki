---
type: episode
show: Hidden Layers
date: 2026-06-18
guests: ["[[people/eran-hoffman]]"]
spotify_url: https://open.spotify.com/episode/0VuXESLXcr8dtYQVHp2ogQ
source: whisper
raw: raw/hidden-layers/2026-06-18-ai-dream.md
---
# How Is AI Used to Defend Countries From Cyberattacks? — with Eran Hoffman (Dream)

[[people/uri-eliabayev]] talks with [[people/eran-hoffman]], Chief R&D Officer at Dream, an AI company providing cyber defense (and now intelligence and other products) to governments and critical infrastructure.
Government customers demand top quality and explainability, and often air-gapped on-prem deployment where fixing a bug can mean flying in. So research POCs built on big models must be re-engineered for production.
Example: a model that predicts an attacker's next steps took three days instead of five hours once moved to large customer networks. They fixed it by splitting tasks across small fine-tuned models under an orchestrator with an expert-knowledge base ("the sous-chef"), then optimized inference from drivers to model configuration.
Every component must pass an eval built on a 500–1,000-item expert ground truth expanded with Claude. Skills hit a ceiling, after which they fine-tune, sometimes automatically at the customer site.
On threats: AI makes attacks a commodity and zero-days a matter of hours, so defense must be faster and increasingly autonomous ("don't bring a knife to a gunfight"), with fine-grained containment recommendations rather than "disconnect everything".

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/ai-cybersecurity]] · [[concepts/multi-agent-orchestration]] · [[concepts/small-language-models]] · [[concepts/llm-evals]] · [[concepts/skill-engineering]]
