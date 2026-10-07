---
type: episode
show: Hidden Layers
date: 2026-06-24
guests: ["[[people/misha-feinstein]]"]
spotify_url: https://open.spotify.com/episode/19qfdsCuYKsvf9pOjQV4Mb
source: whisper
raw: raw/hidden-layers/2026-06-24-bria.md
---
# How Do You Train an Image "Foundation Model" From Scratch? — with Misha Feinstein (Bria)

[[people/uri-eliabayev]] talks with [[people/misha-feinstein]], CTO of Bria, an Israeli company training visual foundation models from scratch for "professional pixels" (enterprise marketing and media).
Three pillars: fully licensed training data (no scraping, with indemnity and IP ownership for customers); fine-grained control; and open weights that enterprises can keep training on their own data.
Training needs data diversity, a large interconnected cluster (one failing machine can sink a run), and architecture. Instead of buying catalogs up front, Bria pays data owners revenue share by attribution: each generated image is decomposed (color, composition, semantics) into embeddings matched to training images, capped at ~200 owners per image, which steers contributors toward under-covered concepts.
Control: training on images paired with long structured JSON (objects, attributes, relations, lighting) instead of short captions. A reasoner turns a prompt into JSON, and users edit one field (chair color) without other things drifting. Customers can fine-tune the JSON vocabulary itself (a studio's "eyebrow shape").
Frontier models wow in demos but commoditize everyone's output and often fail production on cost and latency ("a 5-kilo hammer for snowflakes"). Next: cost, on-prem, and from pretty images to production-ready assets.

**Show:** [[shows/hidden-layers]]

**Concepts:** [[concepts/image-generation]] · [[concepts/ai-moats]] · [[concepts/open-weight-models]] · [[concepts/model-selection]]
