---
type: concept
hubs: [ai-engineering]
sources: 8
updated: 2026-10-29
---
# AI Moats (beyond the model)

**Summary:** A technical edge in AI is a "business card", not a moat: once users touch it, competitors have about six months to catch up, in the good case. Selling tokens with public benchmarks invites endless one-upping and one-click switching (OpenRouter is the worst case). The durable path is a "good enough" product whose value lives beyond the specific model, like Spotify knowing your music. For an AI application that means adapting the system to your own data and customers faster than anyone else, ideally in models you own; otherwise a competitor takes a slightly better model, adds a prompt, and copies you. Agents add a new kind of network effect: letting your agent coordinate with the agents of people you trust. The frontier labs themselves are in a money-losing arms race. Anthropic's S-1 shows revenue up ~15× year over year alongside losses, ~$270B of committed cloud contracts, and an IPO target of $1.5–2T, which strains growth math.

## Key ideas
- "Good enough" wins: nobody switches between Waze and Google Maps for five seconds, or buys a car for its 240 km/h top speed ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Benchmarks as a product are the worst business: like Spotify publishing evals against Apple Music. Spotify instead says "we already learned you" ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Model one-upmanship is tiny and weekly (Codex vs Claude Code flip-flopping), and AI products are technology-based, not market-based, so few last more than a week ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Founders: if you don't know your moat yet, say so and name it as a core problem; "everything's fine" lowers credibility ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Labs fight fires (Gemini, Anthropic, OpenAI, DeepSeek releases) and cut product lines. OpenAI said in 2023 it would try many lines and see what sticks; Anthropic cut far fewer ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Lose-now-earn-later works (Lime, Sequoia-style) but has never been tried past a trillion dollars. Google IPO'd at ~$20B and grew ~100×; a $2T IPO in a market roughly 4× that can't. Public pension money then carries the bet ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Big incumbents aren't dying: Microsoft has compliance, Apple has MacBooks (~$4–5T) and stays out of models, Amazon dominates the layer below, and Nvidia (~$5.5T) is the backbone ([[episodes/explainable--164-gilad-levi-continual-learning]], [[people/gilad-levi]]).
- Building on model vendors means competing with them: vendors move into every vertical (code, legal, design). The test is whether you create enough alpha to justify your margin on tokens ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Agent companies reaching escape velocity (coding, voice) train a fallback model of their own: better economics they can pass to customers, which frontier labs can't match at ~$1 per million tokens ([[episodes/ignore-instructions--26-ai-cyber-pavel-gurevich]], [[people/pavel-gurevich]]).
- Frontier LLMs have "zero distribution moat": no migration cost and precise benchmarks mean users switch weekly, so labs fight brutally; even toilet paper has more stickiness. Technology that learns its user continually is sticky by design ([[episodes/hidden-layers--manifold-gilad-levi]], [[people/gilad-levi]]).
- Frontier models commoditize their users: everyone using the same model gets the same results as their competitors. Differentiation needs access to the model's guts (inject your data, fine-tune) ([[episodes/hidden-layers--bria-misha-feinstein]], [[people/misha-feinstein]]).
- Anthropic's S-1 (ticker ANT): H1 2026 revenue of $16.3B against $1.1B a year earlier and $4.59B for all of 2025; 1,900+ customers paying over $1M a year and ~250 over $10M; ~5,300 employees. Losses, mostly compute, are huge ([[episodes/micha-stocks--anthropic-s1-numbers]], [[people/micha-stocks]]).
- At a $1.5T valuation that is ~327× 2025 revenue, or ~50× an annualized H1. It also owes long-term infrastructure contracts of ~$114B to Google, ~$110B to Amazon and ~$44B to Microsoft, so future revenue is already spoken for. Cash comes from heavy fundraising, with Google and Amazon as investors ([[episodes/micha-stocks--anthropic-s1-numbers]], [[people/micha-stocks]]).
- Anthropic's own pitch: commercial success and humanity's survival are "the same product", and a closed loop (train the model, sell it to enterprises, buy more compute, build the next apps) is the reason to invest ([[episodes/micha-stocks--anthropic-s1-numbers]], [[people/micha-stocks]]).
- Before the S-1, labs published only growth and funding rounds, not financials. By the guest's back-of-envelope math, OpenAI spends ~$40B a year to keep the lights on and loses money on every $20 subscriber, betting on pricier tiers and API work. Profitability forecasts have slipped from 2027 to 2029, and the whole AI bubble rests on them ([[episodes/explainable--167-yuval-avidani-agent-harness]], [[people/yuval-avidani]]).
- SpaceX is profitable on Starlink but loss-making overall because of xAI and Grok's infrastructure, which scares investors ([[episodes/explainable--167-yuval-avidani-agent-harness]], [[people/yuval-avidani]]).
- The real moat for an AI application is how fast it adapts the system to its own world. Fine-tuning your own models on your data and customers builds accumulated IP; staying on the same frontier APIs as everyone means paying the premium and the latency while keeping no knowledge in-house ([[episodes/hidden-layers--plurai-ilan-kedar]], [[people/ilan-kedar]], [[people/uri-eliabayev]]).

- Network effects for the agentic era: Instinct AI's trusted-person network lets users allow-list other people's agents so agents talk to each other; capturing the market early could become the moat many people ask about. Open question: will it interoperate with other agents or stay closed ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/greg-isenberg]], [[people/remy]])?

## Disagreements & open questions
- Is Instinct AI (rumored to be raising at a $10B valuation) a Clubhouse moment? Clubhouse raised at about $4B on invite-only hype and never lived up to it ([[episodes/startup-ideas--instinct-ai-assistant-for-normal-people]], [[people/greg-isenberg]]).
- Will one frontier lab collapse? The host expects one to; Levi doubts the causality but agrees the market is moving in an unhealthy direction ([[episodes/explainable--164-gilad-levi-continual-learning]]).
- Are lab losses temporary? Anthropic projects customer commitments reaching trillions of dollars; Micha calls much of it fantasy and asks whether spending that buys customers is sustainable ([[episodes/micha-stocks--anthropic-s1-numbers]], [[people/micha-stocks]]). Yuval Avidani had heard rumors Anthropic was profitable but assumed it loses money too ([[episodes/explainable--167-yuval-avidani-agent-harness]]).

## Takeaways
- [ ] When building on AI, write down what value remains if a competitor swaps in a better model tomorrow ([[episodes/explainable--164-gilad-levi-continual-learning]])

## Related
[[concepts/market-bubbles]] · [[concepts/small-language-models]] · [[concepts/ai-hype]] · [[concepts/enterprise-ai-adoption]] · [[concepts/model-selection]] · [[concepts/ai-cybersecurity]] · [[concepts/solo-builders]] · [[concepts/image-generation]]
