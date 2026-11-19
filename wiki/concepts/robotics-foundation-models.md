---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-11-19
---
# Robotics Foundation Models (physical AI)

**Summary:** Language models output text, images and audio, artifacts that stay in software. Robots need actions in the physical world, and robotics is still before its "ChatGPT moment": there's no general solution, and the field mixes AI with hardware and physics. Robot software comes in three kinds: classical robotics (deterministic code for one machine in one place), task-specific learned policies or "skills" (often trained from teleoperation demos), and general foundation models meant to run on any robot. In practice today you fine-tune a generic model on the customer's task, and companies like Enigma try to shrink that step by building models that generalize to new environments and tasks. Most deployments are robot arms and four-legged robots, not humanoids. Large enterprises with labor shortages (retail, logistics, factories) are the first buyers, and real deployments teach what lab demos can't.

## Key ideas
- Why not GPT? It's a great product, but it emits artifacts that stay in software; robots need actions with motion in the real world. Language models are only starting to enter that space ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- An open field for founders: unlike coding agents, where strong players already exist, robotics is unsolved, and it's multidisciplinary, so you have to understand AI, hardware and physics together ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Three categories of robot software: classical robotics (code written to solve one concrete problem with specific hardware, which already works in factories); policies or skills (a model trained to do one task robustly, e.g. pick up this bottle anywhere on the table, often from teleoperation data); and foundation models that can "do everything" ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Today's practice is to take a generic model and fine-tune it on the specific use case. Enigma works to shrink that gap and already handles some use cases without task-specific data ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Possible specializations: soft objects; a fixed site you scan once with many sensors (a fast-food kitchen barely changes); or unseen environments, such as disaster rescue, where generalization is everything. Enigma bets on adaptability to new environments and tasks over intricate manipulation ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- The stack: the model; a hardware abstraction layer so the software is plug-and-play across many robot types; and interfaces, because nobody yet knows how billions of people want to experience a robot ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Customers: large enterprises with severe labor shortages that need robots fast and at scale, such as retailers, logistics warehouses, factories and stores. Enigma explains what models can and can't do, then deliberately picks use cases a little beyond what it can do today ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Deployment friction is the teacher: a pot steaming in a kitchen burns out motors, distorts sound and fogs the camera lens, producing images unlike anything from training. Like SpaceX selling to NASA and Starlink early, contact with customers shapes how models are built ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Horizontal vs vertical: Unitree deliberately ships an SDK for others to put any brain on its robots, like Android on many phone makers' devices. Vertical integration allows optimization and avoids drivers, but locks you into the use cases of the hardware you build ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Humanoids vs the rest: the world is built for humans, which is the case for humanoids (Figure, Tesla, Boston Dynamics), but standing stably on two legs is hard mechanically, and so is opening a door by leaning your weight on it. Most deployments are arms and quadrupeds; many "humanoids" are a human-like torso on wheels. Arms are the most common robot: engineers kept the minimum degrees of freedom needed ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Dexterous hands with the human hand's ~21 degrees of freedom exist, but they're expensive and not production-ready, though prices fall and reliability improves ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- In three years Niv expects major breakthroughs, robots in stores and workplaces rather than humanoids in homes, and companies that become the base layer running them ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- Room at every layer: infrastructure, cyber, hardware, software, brains and applications, such as a robot cleaning service that comes while you're out, or Israel's Bellboy, which builds robots for hotel tasks such as room inspection ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).
- "Everyone does everything all the time" (Palo Alto Networks in cyber, Google in its cloud), so a big player in a space isn't a reason to stay out. Startups win by speed and by having no big organization or prior commitments to protect ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).

## Disagreements & open questions
- Humanoids or specialized robots? The host argues the world is built for humans, so humanoids are the natural form. Niv agrees in principle, but says that when you look at each use case separately you can usually solve it more easily with other hardware, and many jobs (climbing power lines, deep diving) are ones you don't want a human-shaped body doing ([[episodes/ignore-instructions--30-enigma-gal-niv]], [[people/gal-niv]]).

## Takeaways
- [ ] Before picking a robotics niche, run and fine-tune an open robot model yourself to see what it can actually do ([[episodes/ignore-instructions--30-enigma-gal-niv]])

## Related
[[concepts/world-models]] · [[concepts/continual-learning]] · [[concepts/llm-safety]] · [[concepts/ai-moats]] · [[concepts/multimodal-llms]]
