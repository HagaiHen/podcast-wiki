---
type: concept
hubs: [ai-engineering]
sources: 3
updated: 2026-10-07
---
# Agent-Ready Products (marketing to agents)

**Summary:** Agents are becoming customers: they research, choose, and integrate tools on users' behalf, and consumers increasingly decide inside ChatGPT. Products that expose themselves to agents (skills or CLI for personal agents, MCP for remote ones) and get listed where agents look capture demand that most SaaS still ignores. Postiz jumped from $21k to $103k MRR in two months this way. Developers and early adopters here pay fast for things that solve problems.

## Key ideas
- Two surfaces: a *skill* (just an MD file, e.g. built from your public API docs, the most popular endpoints first) for personal agents like OpenClaw and Claude Code; an *MCP server* for remote agents like ChatGPT and Claude ([[episodes/langtalks--69-marketing-for-agents]], [[people/nevo-david]]).
- Discovery: (1) GitHub "awesome-skills/awesome-mcp" lists, a strong source of truth for LLM search (AEO); (2) marketplaces like ClawHub, whose virus scans randomly flag CLI-containing skills (re-uploading helps); (3) official ChatGPT (connectors) and Claude (connector, plugin marketplace, skill) submissions. High Claude installs lead to Claude citing you unprompted ([[episodes/langtalks--69-marketing-for-agents]]).
- CLI versus MCP: MCP sends big JSON payloads (slower, more context rot) and suits stateful or remote use; CLIs are one-liners the agent iterates on fast, with agent-friendly errors and workflow-shaped commands. Build both ([[episodes/langtalks--69-marketing-for-agents]]).
- CLI design: rich `--help` at root and per command, gradual exposure; OpenAI publishes a "CLI Creator" skill (it falls back to whatever runtime is installed if Rust isn't) ([[episodes/langtalks--69-marketing-for-agents]]).
- Auth: CLIs keep tokens out of the LLM context (env var, or `login` OAuth stored by the CLI). MCP options are a key in the URL, dynamic OAuth (give ChatGPT client ID and secret so it runs the flow and refreshes tokens), or an auth header ([[episodes/langtalks--69-marketing-for-agents]]).
- Agent-driven purchasing: an agent picked and integrated a platform on the free tier; by the time a credit card was needed, switching was "too late" ([[episodes/langtalks--69-marketing-for-agents]]).
- Big companies are moving too: Stripe's CLI, a bank (Mercury), Salesforce going "headless" for agents ([[episodes/langtalks--69-marketing-for-agents]]).
- Consumers: with ~1B ChatGPT monthly users asking it which insurance to buy, providers it can't quote get skipped ([[episodes/langtalks--69-marketing-for-agents]]).
- SaaS isn't dead: old users keep using classic SaaS; agents open *additional* demand few serve yet ([[episodes/langtalks--69-marketing-for-agents]]).
- An ecosystem is rebuilding the internet for agents: AgentMail (inboxes), Resend (email), Browser Use and similar (web UI), agent phone services, Tavily (search). Most software was built for eyes and clicks ([[episodes/ignore-instructions--28-ai-marketing-enso]]).
- WebMCP (experimental in Chrome, from Google and Microsoft): a site exposes a concise tool list (search, compare, add to cart, apply coupon) that the user's *own* agent calls in the browser, manipulating the visible UI ([[episodes/startup-ideas--webmcp-clearly-explained]]).
- Spectrum of agent access, from headless to UI-bound: raw API → MCP server → computer use (screenshots, slow) → browser MCP (DOM parsing, fragile) → WebMCP → in-app agent. WebMCP inherits the logged-in session, so there are no API keys or OAuth, and tools can be conditional on login state ([[episodes/startup-ideas--webmcp-clearly-explained]]).
- Users want their one agent, carrying their context, to use your product, rather than your in-app agent (whose tokens you pay for) ([[episodes/startup-ideas--webmcp-clearly-explained]]).
- SEO (can Google understand it?) → AEO (can AI cite it?) → agent readiness (can the agent finish the job?) ([[episodes/startup-ideas--webmcp-clearly-explained]], [[people/greg-isenberg]]).
- Best early fits: compatibility-heavy commerce (espresso gear, camera systems, car parts), SaaS admin consoles, read-only self-service in banking and insurance, and internal tools ([[episodes/startup-ideas--webmcp-clearly-explained]]).

## Disagreements & open questions

## Takeaways
- [ ] Publish a skill (MD from your API docs) and an MCP server for your product ([[episodes/langtalks--69-marketing-for-agents]])
- [ ] Submit to GitHub awesome lists, ClawHub, and the ChatGPT/Claude marketplaces ([[episodes/langtalks--69-marketing-for-agents]])
- [ ] Ship a CLI with OAuth login so tokens never enter the agent's context ([[episodes/langtalks--69-marketing-for-agents]])
- [ ] Pick your product's top 3 user journeys and test whether an agent can complete them end to end ([[episodes/startup-ideas--webmcp-clearly-explained]])

## Related
[[concepts/skill-engineering]] · [[concepts/agent-security]] · [[concepts/agent-workspaces]] · [[concepts/ai-growth-marketing]]
