---
type: episode
show: LangTalks
date: 2026-11-23
guests: ["[[people/gabi-balko]]"]
spotify_url: https://open.spotify.com/episode/1HNvk16SMpBbZ3TEgtzDF2
source: whisper
raw: raw/langtalks/2026-11-23-76-agents-that-win-bug-bounties-gabriel-balko-kritt.md
---
# #76 Agents That Win Bug Bounties, With Gabi Balko of Kritt

Vulnerability researcher [[people/gabi-balko]] made over $1M in bug bounties last year with Kritt, his AI agent for finding vulnerabilities. One bug paid over $500K.
A plain "find vulnerabilities" prompt fails: the context is too big and the task too vague. Splitting the work into narrow subtasks ("find a buffer overflow in this function") raises the odds sharply.
Bug bounties reward an edge. Baseline model findings are duplicates someone else found first, so the domain expertise has to go into the workflows.
OpenKritt, the open-source orchestrator, has three parts: workflows (a directed graph of prompts that fans out per result), post-scripts (judge, report, PoC) and rankers. Kritt keeps its best workflows private.
Model spend is about $2K a month. The hosts conclude that opinionated workflows buy stability at the cost of full agency.

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/ai-cybersecurity]] · [[concepts/multi-agent-orchestration]] · [[concepts/skill-engineering]] · [[concepts/context-engineering]] · [[concepts/llm-cost-optimization]] · [[concepts/harness-engineering]]
