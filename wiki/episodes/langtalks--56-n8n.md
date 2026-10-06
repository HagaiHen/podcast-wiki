---
type: episode
show: LangTalks
date: 2025-10-25
guests: ["[[people/shay-shitrit]]"]
spotify_url: https://open.spotify.com/episode/303oTqwfjLnzDuTDr4NJ1N
source: whisper
raw: raw/langtalks/2025-10-25-56-n8n-shay-shitrit.md
---
# #56 — n8n — with Shay Shitrit

[[people/shay-shitrit]] (Lab17, product background) helps companies adopt AI through n8n automations and agents.
Start with n8n Cloud (~€20–25/month, integrations with minimal friction); self-host later for privacy and cost.
Worked example: an email labeler where an LLM classifies new Gmail messages into fixed categories. It grows into a receipts agent that logs each receipt to Google Sheets, extracts PDF text, flags unusual charges against the vendor's history, and files attachments in Drive.
No-code removes the coding "plumbing" but not the other half of technical work: prompts, tool wiring, and system design.
Developers use it for fast MVPs and internal tools, and a dedicated automation owner can serve non-technical teams instead of pulling R&D in. Versus Make, Zapier, Flowise, and Langflow: n8n spans simple to complex flows, has strong LangChain-based agent nodes, and prices per workflow run, not per step. It also offers execution history for debugging, built-in evals, and fast releases (native Anthropic, Firecrawl scraping).

**Show:** [[shows/langtalks]]

**Concepts:** [[concepts/workflow-automation]] · [[concepts/personal-ai-assistants]] · [[concepts/ai-sdlc]] · [[concepts/llm-evals]]
