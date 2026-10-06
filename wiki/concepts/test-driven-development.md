---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# Test-Driven Development (for agents)

**Summary:** Red-green testing (write failing tests first, then the code that makes them pass) was hard for humans to sustain but is ideal for agents. When an agent writes code first and tests after, it "cheats" by testing its own implementation. With tests written up front and frozen, it can only change the code, so the signal is black-and-white.

## Key ideas
- Red: tests fail because the feature doesn't exist; green: the same tests pass after implementation ([[episodes/langtalks--73-harness-engineering]]).
- The agent may not modify tests to make them pass, only code. "No choice" is the essence of a harness ([[episodes/langtalks--73-harness-engineering]]).
- Good engineering practices humans found too costly to maintain become cheap with agents ([[episodes/langtalks--73-harness-engineering]]).

## Disagreements & open questions

## Takeaways
- [ ] Have agents write and freeze failing tests before implementing ([[episodes/langtalks--73-harness-engineering]])

## Related
[[concepts/harness-engineering]] · [[concepts/ai-guardrails]]
