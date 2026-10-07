---
type: episode
show: Hidden Layers
date: 2026-09-27
guests: ["[[people/gilad-shainer]]"]
spotify_url: https://open.spotify.com/episode/5DxLYH5Tpvsk73lqqelJzQ
source: whisper
raw: raw/hidden-layers/2026-09-27-nvidia.md
---
# Making Sense of Nvidia's Technology — with Gilad Shainer

[[people/uri-eliabayev]] opens a series on data centers and compute with [[people/gilad-shainer]] (Nvidia SVP who came from Mellanox, now running networking products).
An "AI factory" isn't a server farm: AI is distributed computing across up to a million GPUs that must act as one computer, so how GPUs connect decides everything.
Three network tiers: scale-up (NVLink makes a rack of 72, then 576, then 1,152 GPUs act as one GPU, with ~10× the traffic of scale-out and compute inside the switches); scale-out (InfiniBand, or Spectrum-X Ethernet for teams that know Ethernet, where switches spray packets and the NIC restores order); and scale-across (linking distant AI factories with distance-aware congestion control instead of deep buffers).
The enemy is jitter: one late GPU idles 100,000 others. Power, not space, limits how many GPUs fit in one site.
Copper wins inside the rack (cheap, reliable, nearly zero power). Optics cost ~10% of compute power, so co-packaged optics (micro-ring modulators, with TSMC) cut that ~5× and failures ~10×.
Moore's law is over; new generations ship yearly. Four of the seven chips in a system are networking, built in Israel.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/ai-infrastructure]]
