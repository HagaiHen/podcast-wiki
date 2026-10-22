---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-10-22
---
# Neoclouds (GPU clouds)

**Summary:** Neoclouds are clouds built for GPU workloads, ranging from ex-crypto miners renting bare-metal GPUs to full "hyperscalers of AI" like Nebius that offer the familiar cloud stack (VMs, managed Kubernetes, S3-style storage, managed inference) tuned for GPUs. Their reason to exist: an on-prem GPU data center is hard on money, Nvidia delivery times, and expertise, and the big clouds don't always have GPUs to give. Few companies move their whole platform; the multi-cloud pattern is to keep microservices on AWS/Azure/GCP and send training, fine-tuning, and inference to a GPU specialist. Capacity, not price, is the scarce resource, which is why Israel's Innovation Authority subsidized *reserved* GPU capacity for local startups and academia rather than paying to build a data center.

## Key ideas
- Spectrum: bare-metal GPU resellers (often former crypto miners) at one end; full, GPU-dedicated cloud ecosystems at the other ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Vertical integration as the moat: Nebius builds data centers (mostly greenfield), designs its own servers, and writes its own virtualization layer, which passes GPUs through when it matters; NCCL and MLPerf tests often beat bare-metal providers despite the extra layer ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Self-service like AWS: a researcher can rent one GPU with a credit card; labs rent clusters of thousands with solution architects ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Multi-cloud: "use each cloud for what it's good at". Nobody moves their microservices and databases to a neocloud; they send GPU workloads there, ideally in the same region as their main cloud ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Build ahead of demand: Nebius buys GPUs and builds before customers sign, betting the market is there ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Origin story: Nebius started in Israel as a generic cloud that couldn't differentiate, then pivoted right after the GPT moment using cash, data-center engineers, and its Nvidia relationship; four years later it's valued at ~$70B with ~$3–4B annual run-rate revenue (guest's figures) ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Moving up the stack through acquisitions such as Tavily (agentic search) after customers kept asking for it: knowing when to build and when to buy ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Israel Innovation Authority model: subsidize usage, not construction. It reserved 1,000 H200 GPUs at Nebius's 4,200-GPU Modiin site, split ~70% industry and startups (30% discount) and ~30% academia (80% discount), with a monthly committee approving requests; Nebius must bring the customers itself ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- The real value is the reservation: the site's other GPUs are sold out and cloud GPU requests are often rejected worldwide, so without it Israeli researchers might get nothing. Nebius now recommends the model to other governments ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).
- Demand outlook: he sees no cooling. Every API call becomes GPU work, and agents and harnesses have caused a token explosion; training's share shrinks while inference is "only at its beginning" ([[episodes/tsarot-baheitek--88-neoclouds-nebius]], [[people/ido]]).

## Disagreements & open questions
- Building ahead of demand assumes it keeps growing; the audience asked what happens if GPU demand cools, given convertible bonds and Nvidia as both supplier and investor. The guest's answer is that he doesn't see it falling ([[episodes/tsarot-baheitek--88-neoclouds-nebius]]).

## Takeaways
- [ ] Keep your platform on your main cloud and send GPU workloads (training, fine-tuning, inference) to a GPU cloud in the same region ([[episodes/tsarot-baheitek--88-neoclouds-nebius]])
- [ ] Israeli startup or researcher? Apply for Innovation Authority subsidized GPU capacity (30% off industry, 80% academia) ([[episodes/tsarot-baheitek--88-neoclouds-nebius]])

## Related
[[concepts/ai-infrastructure]] · [[concepts/llm-inference]] · [[concepts/open-weight-models]] · [[concepts/ai-moats]]
