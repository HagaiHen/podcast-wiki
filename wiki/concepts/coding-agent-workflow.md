---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-06
---
# Coding-Agent Workflow (practical setup)

**Summary:** Day-to-day practices for working with coding agents (Claude Code, Codex, Cursor, Pi). Keep the workflow harness-agnostic with a plugin like Superpowers (spec → plan → implement), so you can hop between tools as models and pricing change. Plan visually and at the right altitude. Tune harness settings, and build small personal tools and skills for the friction you hit: losing track across many terminals, vague agent questions, the laptop sleeping mid-run.

## Key ideas
- Harness hopping: one host moved to Codex after an enterprise pricing change and found GPT 5.5 stronger than Opus for long autonomous tasks, though slower ([[episodes/langtalks--70-our-claude-code-tips]]).
- Superpowers' spec/plan/implement flow with review subagents makes switching between Cursor, Claude Code, and Codex nearly free ([[episodes/langtalks--70-our-claude-code-tips]]).
- Plan altitude: overly verbose technical plans blend the human's requirements with the agent's assumptions, so implementation treats them all as equal. Keep technical plans high-level and render them as HTML ([[episodes/langtalks--70-our-claude-code-tips]]).
- Feedback tooling: a small server plus a Chrome extension let him highlight and comment on HTML plans, turning comments into live tasks. Feedback is often a *principle* ("never more than two buttons per page"), not a one-off edit ([[episodes/langtalks--70-our-claude-code-tips]]).
- Claude Code settings he uses: no-flicker mode; background isolation off (no auto worktrees when supervising); his own git instructions instead of the default; skill-listing budget 0.02 → 0.03 (truncated descriptions hurt); cleanup period 9999 days (keep sessions); remote control on startup; knowledge-work plugins marketplace ([[episodes/langtalks--70-our-claude-code-tips]]).
- Output style "context recap": every reply ends with task (one line), what's done, numbered next steps (reply "1" to continue), and open threads, so you never scroll back across parallel terminals ([[episodes/langtalks--70-our-claude-code-tips]]).
- Skills: "ask good questions" (product-level questions, not obscure specifics); team "linear ops" (ticket ↔ session ↔ branch ↔ PR conventions) ([[episodes/langtalks--70-our-claude-code-tips]]).
- Terminal: Warp with a tab per project and a pane per task, so context switches happen per project ([[episodes/langtalks--70-our-claude-code-tips]]).
- Use idle subscription windows at night for routines: deep code and security reviews, Linear ticket dedupe ([[episodes/langtalks--70-our-claude-code-tips]]).
- A keep-awake tool lets Claude Code keep running with the MacBook lid closed (handling heat and hotspot) ([[episodes/langtalks--70-our-claude-code-tips]]).

## Disagreements & open questions

## Takeaways
- [ ] Use a harness-agnostic workflow plugin (e.g. Superpowers) so switching tools is cheap ([[episodes/langtalks--70-our-claude-code-tips]])
- [ ] Keep technical plans high-level; render plans as HTML for review ([[episodes/langtalks--70-our-claude-code-tips]])
- [ ] Add a "context recap" output style: task, done, numbered next steps, open threads ([[episodes/langtalks--70-our-claude-code-tips]])
- [ ] Raise Claude Code's skill-listing budget if you have many skills; extend session cleanup period ([[episodes/langtalks--70-our-claude-code-tips]])
- [ ] Schedule heavy reviews and maintenance as nightly routines ([[episodes/langtalks--70-our-claude-code-tips]])

## Related
[[concepts/harness-engineering]] · [[concepts/skill-engineering]] · [[concepts/ai-verification]]
