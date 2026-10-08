---
spotify_id: "demo-3"
show: "The Build Log (demo)"
title: "Ep. 14: What AI agents really cost a small team"
release_date: "2026-09-30"
spotify_url: "https://example.com/podcast-wiki-demo/build-log-14"
language: "en"
source: "transcript"
fetched: "2026-10-08"
---
[Fictional demo transcript written for the Podcast Wiki demo. The show and the people in it are made up.]

MAYA (host): Back on The Build Log, and Sam is back too. Last time we talked about tests. Today: money. What do agents actually cost?

SAM (guest): More than people budget for, and mostly in places they don't look. Tokens are the visible part. The hidden part is rework: an agent that goes in the wrong direction for twenty minutes burns tokens and a human's time to undo it.

MAYA: How do you control that?

SAM: Small tasks. We cap an agent task at one pull request and ask for a plan first. A human approves the plan in thirty seconds; that kills most wrong directions before they cost anything. And frozen tests again: the agent stops when the tests pass, instead of polishing forever.

MAYA: Do you track cost per task?

SAM: Per merged pull request. Tokens plus review minutes. When a type of task costs more than a human doing it, we stop giving it to the agent. Migrations and test writing are cheap for us; vague product work is expensive.

MAYA: Some teams say just use the biggest model for everything.

SAM: We route. Small model for review comments and summaries, big model for planning and hard bugs. It cut our bill by about a third without a quality drop we could measure.

MAYA: Last question. Is code review going away?

SAM: No. It's moving. Humans review plans and tests; machines review lines. If you only remember one thing: review the definition of done, not the diff.
