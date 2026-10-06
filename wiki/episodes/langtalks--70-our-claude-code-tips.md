---
type: episode
show: LangTalks
date: 2026-06-28
guests: []
spotify_url: https://open.spotify.com/episode/307nmdS3Y26L0jGIjslSDk
source: whisper
raw: raw/langtalks/2026-06-28-70-our-claude-code-tips.md
---
# #70 — Our Claude Code Tips

The hosts share their personal coding-agent setups. One moved to Codex (GPT 5.5) over cost and found it stronger for long autonomous runs. Both use the Superpowers plugin (spec → plan → implement), which keeps their workflow portable across Claude Code, Codex, and Cursor.
Planning: verbose technical plans blur what the human asked for with the agent's assumptions, so keep them high-level and visual (HTML), with an in-browser feedback extension. For UI work, design first in Pencil.dev and make visual parity the definition of done.
Concrete Claude Code settings (no-flicker, no default worktrees, custom git instructions, larger skill-listing budget, keep sessions longer, remote control on startup), custom skills ("ask good questions", "linear ops"), a "context recap" output style, and a lid-closed keep-awake tool.
Autonomy comes from cloud-first stacks with per-PR ephemeral environments (Pulumi/Kubernetes, MirrorD), a dedicated Chrome profile for the agent (Agent Browser CLI), CLI over MCP, nightly routines, and a secrets vault.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/coding-agent-workflow]] · [[concepts/harness-engineering]] · [[concepts/ai-verification]] · [[concepts/skill-engineering]] · [[concepts/agent-security]] · [[concepts/context-engineering]]
