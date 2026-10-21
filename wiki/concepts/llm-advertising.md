---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-21
---
# Advertising in ChatGPT (LLM ads)

**Summary:** Chat assistants are becoming a paid marketing channel with no playbook yet. ChatGPT shows a small sponsored banner under an answer the advertiser can't influence, and it sits between push and pull: users search, but they also work and ask for advice, so the ad catches them earlier in the journey than Google Search does. monday.com has advertised there since the first day of ads (February 2026) and found that most Google habits fail. Targeting comes mostly from the ad's content, so they run many varied ads split by user intent (tool seekers, chat actions, solution seekers). Action-verb, high-contrast ads and content-heavy landing pages win. Bidding on a conversion event (OCPC) made the channel work. Measurement is the big gap: OpenAI shares almost nothing about what users asked, so click-based attribution undercounts and view-through and geo tests are needed. Competition is low and CPC is about a quarter of Google's, so early entrants learn cheaply before prices rise. Sponsored in-chat agents may replace landing pages.

## Key ideas
- Old split: *push* channels create intent (YouTube, LinkedIn, Facebook); *pull* channels catch existing intent (Google Search, SEO, affiliates, partnerships). ChatGPT is a hybrid: most users who clicked were seeing a monday ad for the first time, which reads like push ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]], [[people/tamar-hazoli]]).
- Getting in early: monday saw rising ad prices and new search behaviour about two years ago, pitched every AI engine it could, and nudged its ChatGPT Enterprise customer-success contact monthly. It ran ads from day one, among the first ~100 advertisers ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]]).
- Targeting: OpenAI asks for *context hints* per ad group (keywords, persona, which conversations to appear in), up to about 10 words each since prompts are paragraphs rather than "best CRM software". In practice the ad's own content drives who sees it, and OpenAI keeps changing the algorithm ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/tamar-hazoli]], [[people/yoav-rubin]]).
- Campaigns by intent: *Tool Seekers* (classic search for the best tool), *Chat Actions* (people asking it to do work, e.g. build a quarterly plan) and *Solution Seekers* (advice, e.g. how to manage a team). Each gets its own copy and landing page; solution seekers go to blog-style content pages ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]]).
- Tooling grew fast: weekly Excel reports in the pilot, then an Ads Manager, then pay-per-click instead of only impressions, then OCPC (bid on an event such as signup, like Google's tCPA). OpenAI has an MCP for ads too ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]], [[people/tamar-hazoli]]).
- What works: OCPC (CPC/CPM bidding converted poorly and cost nearly as much as Google); ads that lead with an action verb ("Plan this project with monday") over "best software" copy; high colour contrast against ChatGPT's black-or-white UI; zoomed-in product feature shots; landing pages *full* of content, which convert better and make the ad show more ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/tamar-hazoli]], [[people/yoav-rubin]]).
- Volume: Google allows three ads per ad group; advertisers on OpenAI upload about 100. Over 90% of large advertisers' ChatGPT ads differ from their Google ads and point to different landing pages. Hyper-local copy ("best sushi in Florentin") works since the prompt is that specific ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]], [[people/tamar-hazoli]]).
- Measurement: impressions → CTR (lower than Google, higher than push) → landing-page conversion (lower than Google Ads) → in-product retention (day 2, week 1, paid). Click-through alone is wrong here; they also count view-through and run a geo test of the lift across all of monday's channels ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]], [[people/tamar-hazoli]]).
- Visibility is the top pain, both ways: you don't know which users or prompts you paid for, nor what demand you're missing (Google publishes top searches). OpenAI guards the data because people share more sensitive things in chat than in search. Brand risk follows: an ad could appear under "what's the worst CRM?" with no way to monitor it ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/tamar-hazoli]], [[people/yoav-rubin]]).
- Cheap for now: CPC is about a quarter of Google's because there are many more searches (follow-up prompts count) and far fewer advertisers, and prompts don't all compete for the same two keywords. Expect prices and competition to rise within a year or two ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]], [[people/tamar-hazoli]]).
- Budget: monday carved a share out of other channels for Q4. On some metrics ChatGPT is its best channel, on others among its worst ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]]).
- Next: *sponsored agents* (alpha). The ad's call to action opens a company agent inside ChatGPT, briefed on pros, cons and pricing, so the user arrives at signup with clearer intent. It also eases privacy, since users know they're talking to the advertiser ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/tamar-hazoli]], [[people/yoav-rubin]]).

## Disagreements & open questions
- Who sees ads: only logged-out, free and lowest-tier users (about 50% of US users). Hazoli sees this as B2B's big fear, because monday's most valuable users work in enterprise accounts that never see ads. Rubin counters that small firms use free or cheap tiers, and that people research on a personal phone account and then sign up from work ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/tamar-hazoli]], [[people/yoav-rubin]]).
- Lead quality is unresolved: retention and conversion swing month to month, and low signup rates may mean irrelevant users or users who aren't ready yet ([[episodes/startup-for-startup--371-chatgpt-ads]], [[people/yoav-rubin]], [[people/tamar-hazoli]]).

## Takeaways
- [ ] Before advertising in ChatGPT, list what your users *do* in chat (searches, work tasks, advice) and build one campaign per intent ([[episodes/startup-for-startup--371-chatgpt-ads]])
- [ ] Send conversion events to OpenAI and bid with OCPC rather than CPC/CPM ([[episodes/startup-for-startup--371-chatgpt-ads]])
- [ ] Write many chat-specific ads that lead with an action verb; don't copy your Google ads ([[episodes/startup-for-startup--371-chatgpt-ads]])
- [ ] Measure view-through and cross-channel lift (e.g. a geo test), not just last click ([[episodes/startup-for-startup--371-chatgpt-ads]])

## Related
[[concepts/ai-growth-marketing]] · [[concepts/agent-ready-products]]
