---
spotify_id: "demo-1"
show: "The Build Log (demo)"
title: "Ep. 12: Write the tests before the agent writes the code"
release_date: "2026-09-02"
spotify_url: "https://example.com/podcast-wiki-demo/build-log-12"
language: "en"
source: "transcript"
fetched: "2026-10-08"
---
[Fictional demo transcript written for the Podcast Wiki demo. The show and the people in it are made up.]

MAYA (host): Welcome back to The Build Log. Today's guest runs a small team that ships most of its code with AI coding agents. Sam, what changed when you went agent-first?

SAM (guest): The bottleneck moved. Writing code got cheap, and knowing whether the code is right got expensive. So we flipped the order: a human writes the failing tests first, then the agent writes code until they pass.

MAYA: Why not let the agent write the tests too?

SAM: Because it grades its own homework. If the agent writes both, it will happily write a test that matches its bug. We freeze the tests: the agent may not edit files under tests/ during a task. That one rule cut our "it passed but it's wrong" incidents to almost zero.

MAYA: Does that slow you down?

SAM: The first week, yes. After that it's faster, because review gets short. The reviewer reads the tests, which are small, instead of reading 600 lines of generated code.

MAYA: What about code review in general? Do you still do it?

SAM: We do, but differently. An AI reviewer does the first pass on every pull request: style, obvious bugs, missing error handling. Humans only review two things: the tests, and anything touching money or user data.

MAYA: Any advice for teams starting out?

SAM: Start with one repo and one rule: tests first, tests frozen. Measure how often agent pull requests get reverted. If that number drops, you've earned the right to expand.

MAYA: And if it doesn't drop?

SAM: Then your tests are too weak. That's the real lesson. The agent is only as good as the definition of done you give it.
