---
type: concept
hubs: [knowledge-management]
sources: 1
updated: 2026-10-06
---
# Memory Consolidation ("Dreaming")

**Summary:** Like the brain clearing and organizing memories during sleep, agent memory systems run nightly jobs that review the day's information: merge related memories, update stale facts, and delete what's no longer worth keeping, so the system "wakes up fresh". Open-source agents (e.g. Hermes) implemented it and it's spreading.

## Key ideas
- Humans absorb lots of junk daily yet function, thanks to sleep and dreaming. Agents need the equivalent "cron jobs" ([[episodes/ai-engineering-podcast--company-brain]], [[people/roi-zalta]]).
- Nightly job: take everything discussed today, clean it, connect memories, update information, and decide what not to keep ([[episodes/ai-engineering-podcast--company-brain]]).
- Outcome evidence: feed back which agent tasks passed CI, failed, reached production, or were rolled back, as team-level context for agents and humans ([[episodes/ai-engineering-podcast--company-brain]]).

## Disagreements & open questions

## Takeaways
- [ ] Add a nightly consolidation job to your agent memory or wiki: merge, update, prune ([[episodes/ai-engineering-podcast--company-brain]])
- [ ] Feed agent task outcomes (CI results, rollbacks) back as context ([[episodes/ai-engineering-podcast--company-brain]])

## Related
[[concepts/company-brain]] · [[concepts/knowledge-rot]]
