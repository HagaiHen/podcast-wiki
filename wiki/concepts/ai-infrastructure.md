---
type: concept
hubs: [ai-engineering]
sources: 3
updated: 2026-10-22
---
# AI Infrastructure (AI factories, compute, and networking)

**Summary:** Training and serving frontier models is distributed computing across hundreds of thousands to a million GPUs that must behave as one computer. That makes an "AI factory" fundamentally different from a server farm, where each app runs on one server and the network barely matters. Performance hinges on networking at three tiers: scale-up (GPUs within a rack act as one), scale-out (racks across a data center), and scale-across (data centers linked across distance). The main enemy is jitter, variance in latency that idles every other GPU. Power, not floor space, is the binding constraint: a modern GPU rack draws 55–140+ kW, so GPU data centers can't simply be converted CPU ones, land next to the electric grid is bought up as future data-center reserve, and energy shapes choices from copper cabling to co-packaged optics. The industry is also splitting giant training sites from smaller inference sites near customers.

## Key ideas
- Server farm vs AI factory: a farm serves single-server apps; an AI factory runs one job across many GPUs and "produces tokens, i.e. money", so idle GPUs are wasted capital ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Distributed computing alternates compute and data exchange; every GPU must finish and exchange data in lockstep. If one of 100,000 GPUs is late, all wait ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Scale-up (NVLink): 72 GPUs act as one unit (576 next, then 1,152), behaving as if on one giant wafer. It carries ~10× the traffic of scale-out, and part of the computation runs inside the switches during transfer ("put the oven in the delivery car") ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Scale-out: traditional Ethernet was built for single-server workloads and ignores jitter. InfiniBand (from 1999, connecting 300+ of the Top500 supercomputers) and Spectrum-X Ethernet target AI. Spectrum-X claims ~1.6× bandwidth, 3–4× lower latency, ~10× message rate, and 1.5–3× app performance; the network costs less than the value it unlocks ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- The network is switch *plus* NIC: switches spray each packet to the emptiest port (like Waze), and the receiving NIC restores order straight into GPU memory ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Congestion: many-to-one traffic jams spread backward through the network. Detect it fast and throttle senders (four senders drop to 25% each) instead of dropping packets or using deep buffers, since big buffers create jitter ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Scale-across: past a site's power limit, link AI factories (e.g. Haifa, Tel Aviv, Beersheba) to train one model. Light costs ~5 ns per meter; distance-aware congestion control avoids deep-buffer switches that could multiply latency ~5× ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Copper vs optics: copper is ~10× cheaper, nearly power-free, and robust, but only reaches ~2 m at these rates (inside the rack). Optics beyond that consume ~10% of compute power. Co-packaged optics put the optical engine next to the switch chip (micro-ring modulators, built with TSMC), cutting optical power ~5× and failures ~10×. Human touch causes ~3–4% of data-center downtime ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Moore's law no longer delivers. New generations ship yearly, and Nvidia's Israel team works on two generations in parallel ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- A Vera Rubin system has seven chip types: three compute (CPU, GPU, LPU) and four networking (BlueField DPU, NIC, Spectrum switch, NVLink switch). The networking silicon is built in Israel ([[episodes/hidden-layers--nvidia-gilad-shainer]], [[people/gilad-shainer]]).
- Cost of a serving node: an 8-GPU machine with ~200–300 GB per GPU runs from many tens to hundreds of thousands of dollars a month in the cloud, so it's mostly companies, not individuals, who work at this level ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).
- Scale is unprecedented: 1B+ people use LLMs, served by hundreds of thousands of GPUs across data centers, a scale that didn't exist five years ago ([[episodes/osim-tochna--running-llms-at-scale]], [[people/mike-erlihson]]).

- GPU racks need far more power than CPU racks: an H200 rack at Nebius's Modiin site draws ~55 kW, NVL72 racks 140+ kW. A GPU data center therefore differs from a converted CPU one in power, cooling, and redundant networking, before any servers arrive ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Grid access is the land rush: giant companies buy empty land whose only feature is proximity to the power grid, as future data-center reserves, like algo-trading firms placing servers next to the exchange ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Site selection weighs where customers are, access to power, and regional deployment. Solar alone doesn't fit; Israeli operator MegaDC builds power plants alongside its data centers ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Speed: Nebius's smallest site (4,200 GPUs, 8.5 MW, in a former synthetic-diamond factory) went up in five months, in colocation with MegaDC ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Sustainability efforts exist, e.g. Nebius's first data center in Finland pipes waste heat into a nearby village ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Trend: separate data centers for training (huge clusters of the latest GPUs) and inference (smaller sites with GPUs a generation or two older, close to customers), plus modular data centers you expand building by building ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Space and underwater data centers (Microsoft tried underwater) are limited by maintenance and construction; hard to see them going mainstream ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Careers: GPU data centers turned "low-tech" electrical, power, and networking engineering into sought-after jobs. The skill is learned only by working at one of the few companies that build them; low-level GPU work (CUDA, cold start, squeezing more from the GPU) is also in high demand ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
## Disagreements & open questions

## Takeaways

## Related
[[concepts/llm-inference]] · [[concepts/llm-pretraining]] · [[concepts/llm-cost-optimization]] · [[concepts/neoclouds]]
