---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-11-19
---
# AI Scientist (AI at the research frontier)

**Summary:** An AI scientist would work at the level of the people who push human knowledge forward, not just help a strong researcher who guides it. Yoav Levine of AAI argues that scaling compute, data, RL and agent scaffolds won't get there by itself. He names four obstacles. Frontier problems have almost no training data by definition. Many answers are hard to verify, and without a precise correctness signal agents drift to the easy wrong answer. Real research needs deep reasoning, many uncertain decisions with backtracking, and models hit a wall after a few such steps. And the intelligence a model builds up during a long session is thrown away when the session ends. AAI's response is a model and harness co-designed for a few very hard problems, with verification built into every stage. Its first product applies this to performance engineering (see [[concepts/ai-performance-engineering]]).

## Key ideas
- The goal: "take Einstein, put him on a GPU and multiply it by millions". Today AI is a force multiplier with a strong researcher hand-holding it, not a scientist that breaks through on its own ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Obstacle 1, data: AI thrives on internet-scale data, but there is no internet-scale record of Newton under the apple tree or Einstein's 1905 papers. Hard engineering feats such as Flash Attention, which take the world's best engineers a quarter, are rare too ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Obstacle 2, correctness: for many hard problems, even checking an answer (hundreds of lines of code, a long proof) is non-trivial. AI improves from correctness signals; when they're imprecise, masses of agents searching in parallel often go "to the easier, wrong place" ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Obstacle 3, reasoning depth: olympiad and Codeforces problems are built to need one non-trivial insight in a few hours, since 17 insights in a row would take a year of research. Open problems need many (see [[concepts/llm-reasoning]]) ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Search data is missing too: people publish the "golden path", not the failed attempts, so models never see how to explore and backtrack ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Obstacle 4, "vaporizing intelligence": over a million-token session a model gets very good at the user's problem, and when the session closes that state is lost. A skill file keeps a summary, like reading a scientist's paper instead of talking to the scientist (see [[concepts/continual-learning]]) ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- The Navier–Stokes result was reportedly reached by a swarm of ~10,000 agents running for 88 hours, about a century of research time. Levine asks what happens to all that intelligence afterwards ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Why math advances fastest: in Lean, a formal proof language, a proof is checked mechanically with 100% certainty. That filter throws out the agents' rubbish and reward hacks and keeps the right answer. Few STEM problems can be formalized that way ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Brain power in watts: roughly 10B human brains at ~20 W each is 100–200 GW of human intelligence. Data centers have about a tenth of that today and will have a third in four years; Levine expects AI to pass humanity in the 2030s. AI can also collaborate without the bottleneck of turning ideas into papers ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- A different design point from frontier labs: AAI owns its compute, models and harness and co-designs them. Labs build for a billion users at a certain difficulty level; AAI builds a system that can spend a week on one hard problem, keeps successful sessions, and can later "bring that expert into the room" ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Domains beyond the team's expertise: the system first builds verification scaffolding for a new field and then explores it, applied so far to chip design and quantum circuits. The team verifies results before publishing ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- Building in Israel: talent moves around less than in the Bay Area bubble, and compensation doesn't turn into the same bidding race ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).

## Disagreements & open questions
- Will current methods get there anyway? The host points to models solving Navier–Stokes and olympiad problems and asks whether they're on the same path. Levine says scale, RL and scaffolds won't reach scientist level, and that those wins came where verification was easy (Lean) ([[episodes/ignore-instructions--29-aai-yoav-levine]], [[people/yoav-levine]]).
- AI scientists are also the missing piece of recursive self-improvement; see [[concepts/llm-safety]] ([[episodes/ignore-instructions--29-aai-yoav-levine]]).

## Takeaways
- [ ] When judging a model on a hard problem, count how many uncertain, non-trivial steps it needs, and expect reliability to drop sharply after 3–5 ([[episodes/ignore-instructions--29-aai-yoav-levine]])

## Related
[[concepts/llm-reasoning]] · [[concepts/ai-verification]] · [[concepts/continual-learning]] · [[concepts/llm-post-training]] · [[concepts/ai-performance-engineering]] · [[concepts/llm-safety]]
