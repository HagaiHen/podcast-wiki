---
type: episode
show: LangTalks
date: 2026-03-21
guests: ["[[people/asaf-savich]]"]
spotify_url: https://open.spotify.com/episode/4SiTQfJjlcfSaCC8lfbPD7
source: whisper
raw: raw/langtalks/2026-03-21-65-ai-sre-asaf-savich-komodor.md
---
# #65 — AI SRE — with Asaf Savich (Komodor)

[[people/asaf-savich]], who leads AI development at Komodor, explains Klaudia, an AI site-reliability engineer for Kubernetes environments.
A naive version (agent SDK plus a Datadog MCP) drowns in noise and fills its context window. Komodor already had detection (an in-cluster daemon feeding a normalized backend), so the work was investigation: following "hops and signals" like a human SRE builds a hypothesis tree, which needs workflow engineering and parallelism across context windows.
For one complex customer, pre-mapping their environment's resource relationships (validated by the customer and injected as YAML in the preprompt) lifted investigation quality several levels.
Evaluation: golden datasets, LLM-as-judge, and *shadow runs*, where new versions run silently beside production on real cases and are judged pairwise on accuracy, tokens, and latency.
Next: self-healing remediation in 2026, then prevention.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/ai-sre]] · [[concepts/llm-evals]] · [[concepts/context-engineering]] · [[concepts/knowledge-graphs]]
