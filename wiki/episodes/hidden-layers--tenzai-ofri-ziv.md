---
type: episode
show: Hidden Layers
date: 2026-06-07
guests: ["[[people/ofri-ziv]]"]
spotify_url: https://open.spotify.com/episode/46ZZgyKwzQSJmIWsJb9Wre
source: whisper
raw: raw/hidden-layers/2026-06-07-ai-hacker-tenzai.md
---
# Building an AI Security Tester — with Ofri Ziv (Tenzai)

> Summarized at a high level (business, evaluation, safety); no technical attack detail.

[[people/uri-eliabayev]] talks with [[people/ofri-ziv]], co-founder of Tenzai (and previously of Guardicore, acquired by Akamai), which builds an AI agent that tests the security of organizations' own applications.
The business case: skilled security testers are scarce, regulation requires testing, and coding agents now ship far more code than periodic human tests can cover. Organizations can't fully adopt AI coding without testing at the same speed.
Customers value reports that prioritize what matters and explain business impact, which helps security teams get fixes made quickly.
Evaluation: internally built enterprise-style apps with known issues, run continuously; in customer comparisons, agent and human findings overlap only partly, which shows where each needs to improve.
Safety: an agent pushed to be thorough can also do damage in a live system, so they add checkpoints and deterministic guardrails, a delicate balance between thoroughness and restraint.
After Mythos, the debate shifted from "can AI find issues" to "can we fix them fast": giving coding agents full context for remediation, plus temporary mitigations through existing security tools until the real fix ships.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/ai-cybersecurity]] · [[concepts/ai-guardrails]] · [[concepts/llm-evals]]
