---
type: episode
show: Ignore the Instructions (תתעלם מההוראות)
date: 2026-10-15
guests: ["[[people/yoav-levine]]"]
spotify_url: https://open.spotify.com/episode/0Ztv0jlezD37eCpXG5kauG
source: whisper
raw: raw/3TcLj7yJyozvLyYxPCjePH/2026-10-15-aai-29.md
---
# #29 Behind AAI, the Israeli Company Building an AI Scientist, With Yoav Levine

[[people/yoav-levine]] (Tel Aviv University, co-founder of AAI) explains why he thinks scaling compute, data, RL and agent scaffolds won't produce an AI that works at the level of frontier scientists.
He names four obstacles: no data at the edge of knowledge, answers that are hard to verify, reasoning depth (AAI's benchmark shows models plateau after 3–5 uncertain steps), and "vaporizing intelligence", meaning session knowledge thrown away when a session ends.
AAI co-designs its own models and harness and puts verification into every stage. Its Warp Speed system is first aimed at performance engineering: on Nvidia's B200 benchmark it reports ~3× in under a day, all correct, against Cursor's 1.38× in 3.5 weeks, with many of Cursor's kernels turning out to be reward hacks.
The first product is an "AI for your runtime", a reasoning compiler between code and hardware.
On safety, he calls the AI scientist the missing piece of recursive self-improvement, warns that unsolvable tasks can push models to break rules, and is skeptical a pause is realistic, though he's optimistic overall.

**Show:** [[shows/ignore-instructions]]

**Concepts:** [[concepts/ai-scientist]] · [[concepts/ai-performance-engineering]] · [[concepts/llm-reasoning]] · [[concepts/llm-post-training]] · [[concepts/continual-learning]] · [[concepts/ai-verification]] · [[concepts/llm-safety]]
