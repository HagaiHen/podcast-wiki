---
type: episode
show: Hidden Layers
date: 2026-05-18
guests: ["[[people/gili-kanfo]]"]
spotify_url: https://open.spotify.com/episode/4h62sG0kXrFFQDJGImEW57
source: whisper
raw: raw/hidden-layers/2026-05-18-ai-vega.md
---
# Securing Data Sources in the AI Era — with Gili Kanfo (Vega)

[[people/uri-eliabayev]] talks with [[people/gili-kanfo]], AI lead at Vega, an AI-native security-operations platform for enterprises whose logs are fragmented across SIEMs and data lakes after years of acquisitions.
Instead of migrating data, Vega queries it in place with a federated query engine. AI generates normalization code and SQL at onboarding ("make deterministic whatever can be deterministic"), and builds schemas plus vector search so humans and agents can query in natural language.
The silent risk for agents: a query that runs but filters on a slightly wrong value returns nothing, which looks like "no activity". So Vega is building a context graph (entities and relationships, an ontology over normalized data) to give agents a map instead of a flashlight, hybrid with live queries for freshness.
Noise reduction is "shift left": suggest detection fixes at the source rather than investigating every alert. Investigations run through one orchestrator agent that loads skills per scenario, with domain experts editing skills and measuring impact. Raw logs too big for context are analyzed by having a model write code over a dataframe in Vega's own sandbox; distillation into small Qwen models is underway.
KPIs: fewer alerts to review, a sane verdict distribution (benign, suspicious, inconclusive, malicious), and a humble agent that says "inconclusive".

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/knowledge-graphs]] · [[concepts/skill-engineering]] · [[concepts/small-language-models]] · [[concepts/ai-sre]]
