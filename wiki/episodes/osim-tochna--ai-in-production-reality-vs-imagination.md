---
type: episode
show: Osim Tochna (עושים תוכנה)
date: 2026-02-23
guests: []
spotify_url: https://open.spotify.com/episode/6FijPoTGlL8ZtYNAqME0K9
source: whisper
raw: raw/osim-tochna/2026-02-23-6FijPoTGlL8ZtYNAqME0K9.md
---
# AI in Production: Reality vs Imagination

> Guest named Ran in the transcript (AI engineer at CyberArk); surname unclear. Host: [[people/amit-bendor]].

Ran tells the "front-line" story of taking a multimodal LLM feature to general availability: extracting insights from RDP session recordings of sensitive machines where nothing can be installed. Text extraction plus one-shot prompting failed. Multimodal models hallucinated (a single black pixel became "Mike Tyson vs Muhammad Ali"), strong models cost too much, and three-image demos fell apart on 500 images.
Fixes: a simple in-house eval harness, LLM-as-judge on a coarse 0/50/100 scale (whose own mistakes required manual review), cheaper models enriched with metadata, deterministic routing between two models, and a patented visual hint (marking the click point on the screenshot). An agent optimizing prompts with Opus 4.5 raised accuracy from 76% to the 80s overnight.
New problems on top of old ones: prompt and typographic injection via on-screen text, guardrail cost at a million operations a day, cross-cloud egress costs, EU data residency, and vendor logging. Plus the old problems: CI, networking, VPCs.
Asides: an exposed OpenClaw instance reported at 4 a.m.; "the end of programmers" doesn't match reality; buying SaaS offloads liability.
Advice: wait two weeks before chasing a trend, remember the 80/20 gap after the POC, and take a breath.

**Show:** [[shows/osim-tochna]]

**Concepts:** [[concepts/multimodal-llms]] · [[concepts/llm-evals]] · [[concepts/agent-security]] · [[concepts/ai-finops]] · [[concepts/future-of-software-engineering]] · [[concepts/ai-hype]]
