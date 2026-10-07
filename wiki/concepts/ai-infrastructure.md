---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-07
---
# AI Infrastructure (AI factories, compute, and networking)

**Summary:** Training and serving frontier models is distributed computing across hundreds of thousands to a million GPUs that must behave as one computer. That makes an "AI factory" fundamentally different from a server farm, where each app runs on one server and the network barely matters. Performance hinges on networking at three tiers: scale-up (GPUs within a rack act as one), scale-out (racks across a data center), and scale-across (data centers linked across distance). The main enemy is jitter, variance in latency that idles every other GPU. Power, not floor space, caps how many GPUs fit in one place, which drives energy-saving choices from copper cabling to co-packaged optics.

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

## Disagreements & open questions

## Takeaways

## Related
[[concepts/llm-inference]] · [[concepts/llm-pretraining]] · [[concepts/ai-finops]]
