---
spotify_id: "demo-2"
show: "Signal & Noise (demo)"
title: "AI code review in practice: what to automate, what to keep"
release_date: "2026-09-16"
spotify_url: "https://example.com/podcast-wiki-demo/signal-noise-31"
language: "en"
source: "transcript"
fetched: "2026-10-08"
---
[Fictional demo transcript written for the Podcast Wiki demo. The show and the people in it are made up.]

LEO (host): On Signal & Noise today: AI code review. My guest leads a platform team of forty engineers. Priya, where does AI review actually help?

PRIYA (guest): Consistency. A human reviewer is great at 10am and terrible at 6pm. The AI reviewer is the same on every pull request. We use it for the boring, important stuff: unhandled errors, missing input validation, secrets in code, inconsistent naming.

LEO: And where does it fail?

PRIYA: Intent. It can tell you the code is clean; it can't tell you it's the wrong feature. So humans own design review. We also noticed reviewers got lazy when the AI said "looks good", so the AI is not allowed to approve. It can only comment.

LEO: Let's talk tests. A lot of people now say: write tests first, freeze them, let the agent code. Do you do that?

PRIYA: Honestly, no, and I think it's overrated for most teams. Writing good tests up front is slow, and for UI or exploratory work you don't know the right behavior yet. We let the agent write code and tests together, and we review the tests carefully afterwards. Mutation testing tells us if the tests are weak.

LEO: Isn't that the agent grading its own homework?

PRIYA: A bit. But a human reading the tests closes most of that gap, and we keep our speed. Tests-first works best for well-specified backend logic, not everywhere.

LEO: What do you measure?

PRIYA: Two numbers: how many review comments the AI makes that humans accept, and how many bugs reach production per hundred pull requests. If acceptance is below about half, the reviewer prompt is noisy and people start ignoring it.

LEO: One thing listeners should try this week?

PRIYA: Turn off AI approvals. Comments only. Then track which comments people accept.
