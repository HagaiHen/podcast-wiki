---
type: concept
hubs: [ai-engineering]
sources: 9
updated: 2026-10-07
---
# LLM Evals

**Summary:** How you know an AI feature works and keeps working, instead of "trust me bro" vibes after an hour of chatting. **Offline evals** run a curated dataset of representative cases before production: a lean set on every PR in CI, fuller runs on big changes, against a score threshold. **Online evals** continuously score real production sessions. Checks are code where the answer is deterministic (~80%) and LLM-as-judge where it isn't. A typical maturity path: manual conversation review → intent clustering → automated evals in CI ("eval-driven design", like TDD) → discovering *unknown* intents. New models get A/B tested by gradual rollout. Prompts are code: version, test, and observe them.

## Key ideas
- Offline evals guard against regressions from code, prompt, or ecosystem changes, and let you compare models on *your* use case ([[episodes/ai-engineering-podcast--ai-infra-at-scale]], [[people/dor-cohen]]).
- monday.com built an "offline eval skill" that scans a repo and generates a starter dataset for the team to refine ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Code checks for 0/1 facts (right tool used, right output structure): cheaper, faster, more precise. LLM-as-judge for the ~20% non-deterministic checks ("tomorrow morning" equals "morning tomorrow") ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Online evals: every few minutes, score production agent sessions; track whether quality holds, improves, or drops ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Model A/B tests: after offline validation, release a new model to a percentage of traffic and compare quality *and* cost before full switch ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Users of agent builders are often non-technical and won't notice a model change, but they'll feel worse results ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Prompts need per-model versions: Opus 5 self-checks sources on its own, so "verify your sources" instructions that helped Opus 4.8 now just waste tokens ([[episodes/ai-engineering-podcast--ai-infra-at-scale]]).
- Non-determinism compounds: one non-deterministic step is hard to bound; multi-step agents multiply it, and models keep changing ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]], [[people/matan-cohen]]).
- Dotti's path: manually review conversations (with customer consent), cluster intents by hand, discover unsupported query types (e.g. "my last conversation with X" is metadata, not semantic), then encode known intents as offline evals in CI ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- "Eval-driven design": treat evals as tests, written first, like TDD ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Known vs unknown: first seal what you know; then detect new intents users have that get bad answers, and add golden sets for them ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Privacy constraint: at Slack you can't read user data unless a user explicitly gives feedback, so you need clustering and topic-level signals without storing content ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Orchestrator/entry-point agents are far harder to evaluate than leaf agents with defined input/output ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Live demos expose non-determinism: a senior exec asked for an unrehearsed prompt mid-acquisition demo (it happened to answer even better) ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- An existing paid data feed can serve as the eval set: Oligo's pipeline had to match the feed's 4% coverage, then grew to ~60% ([[episodes/langtalks--66-scaling-llmops]], [[people/avi-lumelsky]]).
- Shadow runs: release v1.1 (and variants) silently beside v1.0 in production; an LLM judge scores each run and another compares pairs across thousands of real cases, on accuracy, tokens, and latency. New models get verdicts within hours or days on real traffic ([[episodes/langtalks--65-ai-sre]], [[people/asaf-savich]]).
- Custom agents (testing agents, review agents, auto-merge) need a success baseline that rises per version: v0 writes tests at all, v1 at least one passes the build, v2 all pass. Label agent-authored PRs so you can join them with CI outcomes ([[episodes/langtalks--64-ai-coding-metrics]], [[people/liad-elidan]]).
- Voice: feed the recorded *audio* to an audio-capable LLM judge (GPT-4 audio) to catch interruptions, noise, and bad audio that transcripts hide; post every call recording to Slack for team listening ([[episodes/langtalks--61-voice-agents]], [[people/shay-davidson]]).
- Simulated callers ("avatars") with personas (chatty, angry, accented, other languages) per popular intent stress-test robustness; third-party services offer the same ([[episodes/langtalks--61-voice-agents]]).
- Defining what makes output good is becoming a core PM skill. Expect simulated business environments for RL and reward/feedback endpoints from model providers in 2026 ([[episodes/langtalks--58-reinvent-predictions]]).
- Loss, benchmarks, and arena preference decouple: across ~200 Hebatron runs, train and validation loss fell while benchmarks got worse, and benchmarks didn't predict arena preference. Use loss and benchmarks only as negative signals (a big drop means trouble) ([[episodes/explainable--157-training-hebatron]]).
- The team released the version that scored ~3 points lower on benchmarks because users preferred it in the arena: users use models, they don't run benchmarks ([[episodes/explainable--157-training-hebatron]]).
- Arenas can be gamed too (the Meta Llama arena controversy) ([[episodes/explainable--157-training-hebatron]]).
- End-to-end agent evals as nightly labs: build realistic apps across stacks, plant known issues to form ground truth, run the full agent several times per lab, and track recall, precision (false positives), runtime, cost, and unsafe actions. At Tenzai this costs hundreds of thousands of dollars a month in tokens, before production ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Results pick the model per sub-agent, and the best choice changes daily as models ship (e.g. Claude better at one sub-task, GPT-5.5 at another) ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).

## Disagreements & open questions

## Takeaways
- [ ] Build a small offline eval set and run it in CI on every PR ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Use code checks for deterministic criteria; reserve LLM-as-judge for subjective ones ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Score a sample of production sessions continuously (online evals) ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Roll out new models gradually as an A/B test, comparing quality and cost ([[episodes/ai-engineering-podcast--ai-infra-at-scale]])
- [ ] Cluster real user intents (manually at first) and turn known ones into eval sets before scaling ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]])
- [ ] Shadow-run candidate versions beside production and compare pairwise with an LLM judge ([[episodes/langtalks--65-ai-sre]])
- [ ] Version custom agents against an explicit, rising success baseline ([[episodes/langtalks--64-ai-coding-metrics]])
- [ ] Treat loss and benchmark drops as alarms, but pick releases by user or arena preference ([[episodes/explainable--157-training-hebatron]])

## Related
[[concepts/ai-gateway]] · [[concepts/ai-verification]] · [[concepts/model-selection]] · [[concepts/proactive-ai]] · [[concepts/llm-pipelines]] · [[concepts/ai-sre]] · [[concepts/ai-engineering-metrics]] · [[concepts/voice-agents]]
