---
type: episode
show: LangTalks
date: 2026-04-12
guests: ["[[people/avi-lumelsky]]"]
spotify_url: https://open.spotify.com/episode/0AJxSFwUFThUqVZJpHEve9
source: whisper
raw: raw/langtalks/2026-04-12-66-scaling-llmops-avi-lumelsky-oligo.md
---
# #66 — Scaling LLMOps — with Avi Lumelsky (Oligo)

[[people/avi-lumelsky]], who leads production LLM work at the cybersecurity company Oligo, describes two features running at gigabyte-to-terabyte scale.
First, offline CVE enrichment: find which functions a vulnerability actually affects. The model gets a minimal context (the fix's diff plus public CVE references, not whole codebases), returns reasoning and a confidence score, and every claim is checked against real customer environments. Coverage grew from a paid feed's 4% (now the eval set) to ~60%.
Second, real-time malicious-command detection: small models (~70B) and Bedrock prompt caching over iterative event context, with cross-region inference to escape rate limits.
Lessons: define KPIs before experimenting; prefer deterministic *pipelines* over agents where accuracy, speed, and explainability matter; pick the smallest model that meets the KPI (NVIDIA Nemotron matched Sonnet 4.5 on one task at a fraction of the cost); use an internal OpenAI-compatible API with mandatory project tags and a prompt-versioning client SDK.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/llm-pipelines]] · [[concepts/model-selection]] · [[concepts/llm-cost-optimization]] · [[concepts/llm-evals]] · [[concepts/ai-gateway]] · [[concepts/ai-finops]]
