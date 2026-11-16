---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-11-16
---
# Natural-Language Data Access ("talk to your data")

**Summary:** The first building block for AI-native work on company data is letting anyone ask questions in plain language instead of writing SQL or waiting for an analyst. At monday.com, the Kramer agent knows the large data schema, writes the query, and returns an answer, while the existing permissions and governance flow through to each question, so a user only sees tables they're allowed to see. It plugs into Claude, Cursor or internal agents, which turns every employee into a kind of data analyst and keeps the developer's experiment feedback loop with the developer. The catch is that answers stay governed only while they live inside the system: a static HTML artifact built from them strips the permissions, which pushed the team toward live, permission-aware apps (see [[concepts/citizen-developers]]). Business questions often need heavy data manipulation, so the hosts left the accuracy side for a separate episode.

## Key ideas
- Layer one: expose data in a "human-native" way. The agent knows the schema and generates the query each role needs from free text ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]], [[people/oded]]).
- Kramer: any employee can ask about structured and BI data and get a free-text answer, with permissions and governance applied per question, whether asked from Claude, Cursor, or other agents connected to it ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]], [[people/doron]]).
- Developers used to depend on a BI analyst to monitor an experiment and report whether it worked; now getting the insight is part of the developer's own loop ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]], [[people/oded]]).
- Use cases by role: HR querying employee and recruiting data, salespeople tracking their pipeline, product managers checking a feature they just shipped ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]], [[people/doron]]).
- Shared static output loses permissions: someone who can see all salaries builds an HTML dashboard and shares it, and the recipient's rights are no longer checked. Usually not malicious, just easy; it's like emailing an Excel file in 2022, but far easier, and with agents in the loop the trust problem grows ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]], [[people/doron]], [[people/oded]]).
- The fix is infrastructure, not policy: live apps that refresh data and check each viewer's access to the underlying data, so a link can be shared and stays secure. An app over Salesforce asks each viewer for their own Salesforce credentials ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]], [[people/doron]], [[people/oded]]).

## Disagreements & open questions
- Accuracy of business answers: questions often need heavy data manipulation, so is a natural-language answer the single source of truth? Raised and deferred to a future episode ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]]).

## Takeaways
- [ ] Put a natural-language data agent in front of your warehouse that enforces each user's existing table permissions per question ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]])
- [ ] Discourage static HTML exports of internal data; offer live apps that re-check each viewer's access ([[episodes/ai-engineering-podcast--big-brain-studio-non-developers]])

## Related
[[concepts/citizen-developers]] · [[concepts/agent-security]] · [[concepts/rag]] · [[concepts/knowledge-graphs]]
