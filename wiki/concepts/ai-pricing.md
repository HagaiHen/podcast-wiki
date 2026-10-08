---
type: concept
hubs: [ai-engineering]
sources: 2
updated: 2026-10-08
---
# AI Pricing

**Summary:** AI breaks the SaaS business model: software used to keep 75–90% gross margins, but model inference is now a large, growing share of cost, so per-seat subscriptions alone no longer add up. The options run from value-based deals where the vendor owns the outcome, to pay-per-use, which enterprises find hard to budget for, to credits: one consumption unit across every product and tier, with a different margin behind each service. The emerging pattern, borrowed from the AI labs, is committed per-user credit buckets at a deep discount, paid for by unused credits that expire, with overflow into uncapped pools at list price for production work. Lab subscriptions are heavily subsidized, and charging a percentage on top of LLM cost is a mistake. Nobody has settled it yet; monday.com is still exploring these models.

## Key ideas
- Business model vs pricing: the business model is whether the product makes money at all (airlines ~5% margins, software historically 75–90% gross); pricing is how that is presented to the customer. AI costs grow and aren't negligible like web servers, so the SaaS model has to change ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Value-based (FDE-style, as at Wonderful): the vendor takes a fee and full responsibility for the outcome, and must make sure each deal pays ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Pay-per-use (e.g. paying per generated video, keep or not): it says "I don't know what it will cost or what you want", which large customers who plan budgets find hard, like asking a car dealer what next year's fuel will cost ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Credits decouple spend from dollars ("spend 300 credits" lands better than "spend $300"). At monday 1 credit is fixed at 1 cent; discounts mean more credits per dollar, never a cheaper credit ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- A credit system fits anyone with more than one product or tier, which will be nearly everyone: AWS, Datadog, Anthropic, OpenAI, and ElevenLabs all meter many services through one unit. monday wants boards, automations (not AI, but costly), the Sidekick assistant, task agents, and Vibe apps under one credit pool ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Margin differs by service: agent features pass most spend straight to the LLM (and users may pick the priciest model), so margins are thin; board automations keep software margins. Pricing must model the expected usage mix ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Buckets: a committed monthly plan ($100–300) gives far more credits than list price, up to ~20×, capped per user, with list price beyond. Unused credits vanish at month end as 100% margin. On average users consume about half a bucket, because those who hit the cap upgrade ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Subscriptions are subsidized: a heavy $200 Claude Max user would cost ~$1.5–2k at API prices ([[episodes/explainable--163-hidden-cost-of-agents]]).
- One shared account pool lets a single power user drain it and leaves little room for discounts. Per-user buckets plus pools fix both: every employee gets a discounted bucket, and anyone who runs out, or builds a production agent that can't stop, connects to a pool at list price, as the labs move you from a plan to an API key ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Pools carry the controls: per-department pools with their own budget and card, recurring purchases (discountable), top-ups and automatic top-ups, enterprise pay-as-you-go invoicing, and spending limits ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Agents bill to their human owner rather than holding budgets of their own: budgets are still allocated to people, and keeping that complexity in the product keeps billing simple ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).
- Taking a fixed percentage on top of LLM cost as the business model is a mistake for everyone, though many companies do it ([[episodes/startup-for-startup--369-ai-pricing]], [[people/roy-mann]]).

## Disagreements & open questions
- Should per-user buckets be upgradable one user at a time? Mann leans toward requiring org-wide upgrades in exchange for the deep discount ([[episodes/startup-for-startup--369-ai-pricing]]).

## Takeaways
- [ ] Model margin per service and the expected usage mix before choosing a pricing model ([[episodes/startup-for-startup--369-ai-pricing]])
- [ ] Consider committed per-user credit buckets with expiring credits to fund deep discounts, plus list-price pools for production use ([[episodes/startup-for-startup--369-ai-pricing]])

## Related
[[concepts/llm-cost-optimization]] · [[concepts/enterprise-ai-adoption]] · [[concepts/ai-moats]] · [[concepts/ai-hype]]
