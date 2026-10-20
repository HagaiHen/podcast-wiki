---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-20
---
# Proactive AI (the AI UX paradox)

**Summary:** A chat box looks simple but is a hard interface: users can ask anything and expect anything, yet nothing in the UI shows what the AI can actually do, and backend upgrades (new tools, skills, reasoning) are invisible. Unlike deterministic products, there's no clear funnel. "Proactive AI" closes the gap by designing features that tell users what's possible, inside and outside the text box, and by bringing AI answers to people where they already work, avoiding cognitive leaps that lose users. Consumer agents push this furthest: Instinct AI onboards with a phone number inside iMessage, immediately demos what it can do, uses native reactions and effects, keeps replies short, and reaches out on its own when a deadline matters, so it feels like a human assistant. Hiding the work has a cost: users can't see progress and mistake silence for failure.

## Key ideas
- The paradox: the text box allows anything, so users can't know what they can or can't get ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]], [[people/matan-cohen]]).
- Early ChatGPT couldn't make images; once it could, nothing in the interface said so. Surfacing new capabilities is a product job ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Capability-surfacing features: Slack's "prepare me for a meeting" button on the Today screen; a question typed into search pops an AI answer that continues in Slackbot; suggesting an image or deck when intent fits ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Bring answers to users instead of making them find the AI: Dotti auto-answered questions in channels (e.g. IT/VPN), first visible only to the asker, who could then publish to the channel. Adoption spread "like wildfire" in 2,000-person channels ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Avoid cognitive leaps: in 2024 people searched for documents, not answers. Even writing a three-line prompt was a leap that needed hand-holding ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Personalization goes beyond "who asked": decompose context into personal, team, group, and org layers, with permissions as a huge, startup-killing problem ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).
- Mass-market onboarding: no MCPs, CLIs, or markdown files; log in with a phone number and land in iMessage, where the agent sends example use cases (flights, food, cancelling subscriptions, calendar) and shows that voice notes work ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/remy]]).
- Native channel features make an agent feel human: thumbs-up reactions read as approval, confetti and "loud" message effects for important news, voice notes, even playing iMessage Game Pigeon games ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/remy]]).
- Knowing when to react instead of reply avoids the verbosity of most models; "so human it's scary" is the aha moment ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/remy]], [[people/greg-isenberg]]).
- Proactivity: after a desk-rental search, the agent messaged the next morning that same-day delivery required ordering before noon ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/remy]]).
- Products moved from top-down, high-touch rollout to bottom-up and self-serve as users matured ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]]).

## Disagreements & open questions
- Invisible execution keeps the product simple, but when Instinct went silent for five minutes the user kept checking whether it was broken; trust came only with experience ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/remy]]).

## Takeaways
- [ ] For each new AI capability, add a visible entry point (button, suggestion) instead of relying on users to discover it in chat ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]])
- [ ] Deliver AI answers where users already ask (channels, search), privately first ([[episodes/ai-engineering-podcast--the-ai-ux-paradox]])

## Related
[[concepts/personal-ai-assistants]] · [[concepts/agent-workspaces]] · [[concepts/llm-evals]] · [[concepts/context-engineering]]
