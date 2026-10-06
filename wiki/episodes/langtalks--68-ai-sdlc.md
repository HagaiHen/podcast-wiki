---
type: episode
show: LangTalks
date: 2026-05-24
guests: ["[[people/yonatan-maor]]"]
spotify_url: https://open.spotify.com/episode/44cnbIkDvinaZpgfdoPZlY
source: whisper
raw: raw/langtalks/2026-05-24-68-ai-sdlc-yonatan-maor-clears-ai.md
---
# #68 — AI-SDLC — with Yonatan Maor (Clears.ai)

[[people/yonatan-maor]] and the hosts sketch an AI-native development lifecycle with agent teams. Ask two questions first: what is your source of truth (Jira, PRDs, PRs, tests), and where do humans give feedback?
Happy path: an agent turns a terse idea into a researched PRD (with a live mock in your design system), then breaks it into subtasks with definitions of done and files to touch, asking the tech lead about gaps. It writes everything back to Jira.
Blast radius and complexity decide whether a task needs a plan and human code review; code review is really *alignment* (architecture standards, spec drift), not just a quality gate.
Knowledge: keep global and repo instructions focused, retrieve area-specific decisions dynamically, and run an org-wide skills marketplace with an owner.
Getting started: begin at the edges (bug triage, on-call investigation, Zendesk/log-driven tasks), cut friction, and fix the DevOps basics first (per-developer environments and log access), because agents can't close loops built on copy-paste.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/ai-sdlc]] · [[concepts/harness-engineering]] · [[concepts/ai-verification]] · [[concepts/skill-engineering]] · [[concepts/context-engineering]]
