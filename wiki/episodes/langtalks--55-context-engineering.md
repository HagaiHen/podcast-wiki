---
type: episode
show: LangTalks
date: 2025-10-11
guests: []
spotify_url: https://open.spotify.com/episode/7c5mk0yzyPMD1wXAgJzb8U
source: whisper
raw: raw/langtalks/2025-10-11-55-context-engineering.md
---
# #55 — Context Engineering

The hosts define context engineering as getting *all and only* the relevant context into each LLM call. That spans prompt engineering, RAG, memory, conversation history, and structured output. Irrelevant tokens measurably lower task success, even where needle-in-a-haystack retrieval is "solved".
Following Karpathy's "LLM as OS" (context window = RAM), the pillars are write, select, and compress. Practices drawn from Manus's and LangChain's blog posts:
- sub-agents that read big files and return only an answer or snippet;
- a stable prompt prefix for KV caching;
- logit masking instead of swapping tool sets;
- the file system as memory before any vector DB;
- "recitation" via to-do files and plans;
- manual hooks that inject guidelines;
- keeping tool errors in context, and richer API errors for agents;
- focused compaction, or dump-to-files then reset.
Pitfall: jumping to multi-agent systems; most successful agents are a single agent plus narrow helpers. Check: if reading your traces means lots of scrolling past noise, your context engineering needs work.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/context-engineering]] · [[concepts/agent-memory]] · [[concepts/multi-agent-orchestration]] · [[concepts/llm-cost-optimization]]
