---
title: "Serverless / On-Demand GPU Inference Providers"
detail: "Comparison of ten serverless and on-demand GPU providers for ML inference, including Akash Network, covering pricing, API, data privacy, and storage."
details: "Comparison of ten serverless and on-demand GPU providers used for ML inference as of July 2026. Covers pricing models (per-token, per-GPU-second, per-replica-hour, per-output), API design, data privacy and compliance, storage options, cold-start behavior, and provider strengths/limitations. Includes Akash Network, Replicate, Modal, RunPod, Together AI, Fireworks AI, Hugging Face Inference Endpoints, Fal.ai, Baseten, and Beam Cloud."
tags:
  - research
created: 2026-07-24
updated: 2026-07-24
type: research
sources:
  - .Concepts/serverless-gpu-pricing-models
  - .Concepts/serverless-gpu-data-privacy
  - .Entities/akash-network
  - .Entities/replicate
  - .Entities/modal
  - .Entities/runpod
  - .Entities/together-ai
  - .Entities/fireworks-ai
  - .Entities/lambda
  - .Entities/huggingface-inference-endpoints
  - .Entities/fal-ai
  - .Entities/baseten
  - .Entities/beam-cloud
  - .Entities/cerebrium
  - .Entities/anyscale
  - .Entities/deepinfra
---
# Serverless / On-Demand GPU Inference Providers

**Updated:** 2026-07-24
**Scope:** Ten providers covering serverless and on-demand GPU inference, including the decentralized Akash Network. Pricing data captured July 2026 from each provider's published pricing page; third-party aggregators cited where the provider does not publish a list price (e.g., reverse auction).

---

## Provider List (with Direct Product-Page URLs)

| # | Provider | Product type | Pricing page | Product page |
|---|---|---|---|---|
| 1 | [[Entities/akash-network]] | Decentralized marketplace (reverse auction) | [akash.network/docs/learn/core-concepts/gpu-deployments](https://akash.network/docs/learn/core-concepts/gpu-deployments/) | [akash.network](https://akash.network/) |
| 2 | [[Entities/replicate]] | Serverless model registry + Cog private deploys | [replicate.com/pricing](https://replicate.com/pricing) | [replicate.com](https://replicate.com/) |
| 3 | [[Entities/modal]] | Python-native serverless GPU | [modal.com/pricing](https://modal.com/pricing) | [modal.com](https://modal.com/) |
| 4 | [[Entities/runpod]] | GPU cloud (Pods + Serverless) | [runpod.io/pricing](https://www.runpod.io/pricing) | [runpod.io/product/serverless](https://www.runpod.io/product/serverless) |
| 5 | [[Entities/together-ai]] | Open-model inference API + GPU clusters | [together.ai/pricing](https://www.together.ai/pricing) | [together.ai/serverless-inference](https://www.together.ai/serverless-inference) |
| 6 | [[Entities/fireworks-ai]] | Open-model inference + fine-tuning | [fireworks.ai/pricing](https://fireworks.ai/pricing) | [fireworks.ai](https://fireworks.ai/) |
| 7 | [[Entities/lambda]] | GPU cloud (H100, H200, B200 + 1-Click Clusters) | [lambda.ai/pricing](https://lambda.ai/pricing) | [lambda.ai/instances](https://lambda.ai/instances) |
| 8 | [[Entities/huggingface-inference-endpoints]] | Dedicated model deployment | [huggingface.co/pricing](https://huggingface.co/pricing) | [endpoints.huggingface.co](https://endpoints.huggingface.co/) |
| 9 | [[Entities/fal-ai]] | Generative-media serverless + Compute | [fal.ai/pricing](https://fal.ai/pricing) | [fal.ai/serverless](https://fal.ai/serverless) |
| 10 | [[Entities/baseten]] | Managed inference (Truss + Model API) | [baseten.co/pricing](https://www.baseten.co/pricing/) | [baseten.co](https://www.baseten.co/) |
| 11 | [[Entities/beam-cloud]] | Serverless GPU + Sandboxes + BYOC | [beam.cloud/pricing](https://www.beam.cloud/pricing) | [beam.cloud](https://www.beam.cloud/) |

The comparison below adds Cerebrium, Anyscale, and DeepInfra as honorable mentions because they were strong candidates for the list and are commonly seen in the same conversations.

---

## Master Comparison Table

| Provider | Primary pricing model | H100 effective rate | Cold start | BYOC | SOC 2 | HIPAA | Free tier |
|---|---|---|---|---|---|---|---|
| [[Entities/akash-network]] | Per-block (reverse auction) | $2.50-$4.00/hr | 5-30 min (lease) | No | No | No | Limited (testnet) |
| [[Entities/replicate]] | Per-second GPU + per-output | $5.49/hr (H100 list) | Free on popular public models | No | Yes | No (no BAA) | Limited free predictions |
| [[Entities/modal]] | Per-second GPU (active only) | ~$3.95/hr sustained | <1 sec | No | Yes (Type II) | Yes (enterprise) | $30/mo |
| [[Entities/runpod]] | Per-second GPU (Pods + Serverless) | $2.89/hr (Secure) / $1.39/hr (Community) | <200ms (FlashBoot) | No | Yes (Type II) | Yes (enterprise) | $25 sign-up credit |
| [[Entities/together-ai]] | Per-token serverless + per-GPU-hour dedicated | $5.49/hr dedicated; per-token serverless | Cold starts on serverless | No | Yes (Type II) | Yes (enterprise) | $5 sign-up credit |
| [[Entities/fireworks-ai]] | Per-token serverless + per-GPU-second on-demand | $7.00/hr (H100 On-Demand) | No cold boots on serverless | Yes (Reserved) | Yes (Type II) | Yes (enterprise) | $1 sign-up credit |
| [[Entities/lambda]] | Per-GPU-hour (on-demand + reserved) | from ~$2.49/hr reserved | 1-3 min (VM boot) | No | Yes (Type II) | Yes (enterprise) | No |
| [[Entities/huggingface-inference-endpoints]] | Per-replica-hour | $5.00/hr (H100) | None (warm replicas) | Yes (Enterprise Hub) | Yes (Type II) | Yes (enterprise) | Free Inference API (rate-limited) |
| [[Entities/fal-ai]] | Per-output (per-image, per-MP, per-second video) | $1.89-$3.99/hr Compute | None on Model API | No | Yes (SOC 2) | No (no BAA) | Limited free credits |
| [[Entities/baseten]] | Per-replica-minute (Dedicated) + per-token (Model API) | $6.50/hr (H100 Dedicated) | Sub-300ms (some workloads) | Yes (self-hosted) | Yes (Type II) | Yes | $30 sign-up credit |
| [[Entities/beam-cloud]] | Per-millisecond GPU (active only) | $3.55/hr (H100 PCIe serverless) | Low-hundreds-ms (memory snapshot) | Yes (BYOC) | Yes (enterprise) | Yes (enterprise) | $30/mo refreshed |

Honorable mentions: Cerebrium (multi-region real-time AI), Anyscale (Ray-native with mature BYOC), DeepInfra (lowest per-token on open models).

---

## Pricing Models (deep dive)

See [[Concepts/serverless-gpu-pricing-models]] for the full breakdown. The four primary models are:

1. **Per-output** (per-image, per-MP, per-second of video) — Fal.ai Model API.
2. **Per-token** (per-1M input/output tokens) — DeepInfra, Together, Fireworks, Baseten Model API.
3. **Per-GPU-second** (active only) — Modal, RunPod Serverless, Beam, Cerebrium, Replicate private, Akash.
4. **Per-replica-hour** (with optional scale-to-zero) — HF Endpoints, Baseten Dedicated, Together Dedicated, Lambda Instances, Anyscale Services.

Per-replica-hour is the most expensive at low utilization; per-GPU-second is the most flexible; per-token is the easiest to forecast against revenue; per-output is the most predictable for content-generation use cases.

---

## H100 Rate Comparison (effective $/hr, July 2026)

| Provider | H100 effective rate | Pricing model | Notes |
|---|---|---|---|
| RunPod (Community) | $1.39/hr | per-second | Preemptible; reliability varies |
| Beam On-Demand | $1.74/hr | per-hour | Bare-metal or VM |
| Fal.ai (Reserved) | $1.89/hr | per-second | Reserved-spend required for discount |
| Lambda (reserved) | ~$2.49/hr | per-hour | Reserved only; on-demand quoted on request |
| Akash (auction) | $2.50-$4.00/hr | per-block | Reverse auction; varies by provider bid |
| RunPod (Secure) | $2.89/hr | per-second | Reliable tier |
| Modal (sustained) | ~$3.95/hr | per-second | Idle is free; effective rate depends on utilization |
| Beam (serverless) | $3.55/hr | per-millisecond | Per-ms billing while active |
| Replicate (private) | $5.49/hr | per-second | Bills boot + idle + active on private deploys |
| Together (Dedicated) | $5.49/hr | per-hour | No scale-to-zero; reserved from $3.99/hr |
| HF Endpoints | $5.00/hr | per-replica-hour | Per-replica, no scale-to-zero unless configured |
| Baseten (Dedicated) | $6.50/hr | per-replica-minute | Includes Baseten Inference Stack |
| Fireworks (On-Demand) | $7.00/hr | per-GPU-second | No startup charge |

**Cross-check:** the [2026 GPU Buyer's Guide](https://cerebrium.ai/blog/2026-gpu-buyers-guide) and [Northflank serverless GPU comparison](https://northflank.com/blog/the-best-serverless-gpu-cloud-providers) publish similar H100 effective rates and converge on the same ordering. Northflank's own H100 rate of $2.74/hr is the lowest published non-Akash H100 rate in the market but is a single-provider outlier and was not included in this list because Northflank is positioned as a multi-service orchestration platform, not a pure inference API.

---

## API Compatibility

| Provider | OpenAI-compatible | Custom SDK | Bring your own model | Bring your own Dockerfile |
|---|---|---|---|---|
| Replicate | No (custom HTTP) | Python, JS, Cog | Yes (Cog) | No (Cog wraps Dockerfile) |
| Modal | No (Python decorator) | Python | Yes | No (Modal images) |
| RunPod | Partial (OpenAI-compatible endpoints for some models) | runpodctl, Python, JS | Yes | Yes |
| Together AI | Yes | Python, TS | Yes | No |
| Fireworks AI | Yes | Python, TS | Yes | No |
| Lambda | No (raw SSH) | Lambda Cloud API | Yes | Yes |
| HF Endpoints | Yes (router) | Python, JS | Yes (any Hub model) | Yes (custom handler) |
| Fal.ai | No (custom HTTP) | Python, TS, fal-client | Limited (per-output only on Model API; Docker on Compute) | Yes (Compute) |
| Baseten | Yes (Model API) | Python, Truss | Yes | Yes (Truss) |
| Beam | No (Python SDK) | Python | Yes | Yes |
| Cerebrium | No (custom HTTP) | Python | Yes | Yes (no SDK) |
| Anyscale | No (Ray API) | Ray Python | Yes | Yes |
| DeepInfra | Yes | Python, JS | Yes | Limited |
| Akash | No (akash CLI) | akash CLI | Yes (any Docker image) | Yes |

OpenAI-compatible providers are easiest to integrate with for LLM workloads (Together, Fireworks, HF Endpoints, DeepInfra, Baseten Model API). For non-LLM workloads (image, video, audio, custom code), the proprietary SDKs (Modal, Replicate, Fal.ai, Beam) are often more ergonomic.

---

## Data Privacy and Compliance (Summary)

See [[Concepts/serverless-gpu-data-privacy]] for the full pattern reference. The four patterns are:

1. **Public multi-tenant** — Replicate, DeepInfra, Together serverless, Fireworks serverless, Fal.ai Model API.
2. **Public single-tenant (dedicated)** — HF Endpoints, Baseten Dedicated, Together Dedicated, Fireworks On-Demand, RunPod Serverless, Modal, Beam, Cerebrium, Replicate private.
3. **BYOC (compute in customer's cloud)** — Beam BYOC, Baseten self-hosted, Anyscale BYOC, HF Enterprise Hub, Fireworks Reserved, Modal Reserved.
4. **Decentralized / permissionless** — Akash.

For HIPAA / healthcare workloads, the practical path is HF Endpoints (Enterprise), Baseten (self-hosted), or Anyscale BYOC. For financial services with strict data-residency, the same providers are the leading options. For censorship resistance and cost-first, Akash is unmatched.

---

## Storage Options

| Provider | Model registry | Persistent volumes | S3-compatible blob | BYO storage |
|---|---|---|---|---|
| Replicate | Yes (50,000+ models) | No | No | No |
| Modal | No native registry | Yes (Modal Volumes) | No (use S3/GCS via client) | Yes |
| RunPod | Yes (Hub + Public Endpoints catalog) | Yes (Network Volumes) | No (use S3 via client) | Yes |
| Together | Yes (model registry) | No | No | No |
| Fireworks | Yes (200+ models) | No | No | No |
| Lambda | No | Yes (Lambda Stack) | No | No |
| HF Endpoints | Yes (Hub, 1M+ models) | No (use Hub) | No | Yes (use Hub repos) |
| Fal.ai | Yes (Model API gallery) | No | Fal-managed with TTL | Yes (enterprise) |
| Baseten | No native registry (Truss) | No | No | No |
| Beam | No | Yes (first-class) | No | Yes |
| Cerebrium | No | Yes (volumes) | No | Yes |
| Anyscale | No (Ray-native) | Yes (Ray object store, S3-compatible) | Yes (Ray object store) | Yes |
| DeepInfra | Yes (model catalog) | No | No | No |
| Akash | No | Yes (persistent volumes, IPFS) | No | Yes (attach any) |

**Persistent volume mounts are rare in the category.** Beam and Modal both treat this as a first-class concept, which matters for model weights that cannot be re-downloaded on every cold start. HF Endpoints re-uses the Hub as a registry, which functionally serves the same purpose. Anyscale uses Ray's object store, which is S3-compatible.

---

## Cold Start Behavior

| Provider | Cold start latency | Cold start billed? |
|---|---|---|
| Modal | <1 sec (sub-second) | Only active compute billed |
| RunPod Serverless | <200ms (FlashBoot) | Only active compute billed |
| Beam | Low-hundreds-ms (memory snapshot) | Only active compute billed |
| Cerebrium | <1 sec (memory snapshot) | No (cold-start container spin-up is not billed) |
| HF Endpoints | None (warm replicas by default) | Always (replica-hour) |
| Baseten (Inference Stack) | Sub-300ms on some workloads | Only active compute billed |
| Fireworks (Serverless) | None (no cold boots) | Only active compute billed |
| Replicate (public models) | None (kept warm by other users) | Free |
| Replicate (private) | 1-2 min | Yes (bills for full online time) |
| Together (serverless) | Cold start on less-trafficked models | Yes (idle replicas) |
| Fal.ai (Model API) | None (Fal maintains warm capacity) | Per-output |
| Anyscale (Services) | None (replicas stay warm) | Always (replica-hour) |
| DeepInfra (popular) | None | Per-token |
| Akash | 5-30 min (lease) | N/A (per-block) |
| Lambda (instances) | 1-3 min (VM boot) | Always (instance-hour) |

---

## Provider Strengths and Limitations (Quick Reference)

### Akash Network
- **Strengths:** Lowest published GPU rates; censorship resistance; no KYC.
- **Limitations:** Reverse auction is operationally heavy; slow lease creation; no managed SOC 2/HIPAA.

### Replicate
- **Strengths:** Largest model registry (50,000+); free idle on public models; simple HTTP API.
- **Limitations:** Private deployments pay for boot+idle; no BYOC; H100 rate is high.

### Modal
- **Strengths:** Best Python DX; sub-second cold starts; full ML lifecycle.
- **Limitations:** Python-only SDK; decorator lock-in; sustained H100 rate above bare-metal.

### RunPod
- **Strengths:** Broadest GPU catalog (consumer to B300); Community Cloud is cheap; Pods + Serverless.
- **Limitations:** Community Cloud can preempt; weaker orchestration tooling than Modal or Baseten.

### Together AI
- **Strengths:** Strong on Qwen/DeepSeek/Llama; automatic prompt caching; batch 50% off.
- **Limitations:** No BYOC; H100 on-demand rate is high; serverless rate limits.

### Fireworks AI
- **Strengths:** FireAttention engine; inference + fine-tuning under one API; no cold boots.
- **Limitations:** On-Demand H100 is $7/hr (high); not always the cheapest per-token.

### Lambda
- **Strengths:** No egress fees; mature 1-Click Clusters; simple per-minute pricing.
- **Limitations:** No per-token serverless API; on-demand supply can be tight; no BYOC.

### Hugging Face Inference Endpoints
- **Strengths:** Tight Hub integration; multi-cloud (AWS/GCP/Azure); no cold starts.
- **Limitations:** Per-replica-hour pricing; scale-to-zero cold starts unpredictable; not the cheapest.

### Fal.ai
- **Strengths:** Best-in-class for generative media; per-output pricing; large model gallery.
- **Limitations:** API-bounded inference parameters; no custom checkpoints; high-volume costs grow linearly.

### Baseten
- **Strengths:** Baseten Inference Stack performance; Truss open-source; self-hosted option.
- **Limitations:** H100 Dedicated is $6.50/hr (high); per-replica-hour costs for idle replicas.

### Beam Cloud
- **Strengths:** Memory snapshot cold starts; persistent volumes; BYOC mature; Sandboxes product.
- **Limitations:** Smaller GPU catalog than RunPod; Python-only SDK; lower brand awareness.

---

## Decision Tree

```
Need censorship resistance / cost-first?
  -> Akash

Need per-token billing for LLM with prompt caching?
  -> DeepInfra (cheapest), Together (great DX), Fireworks (best cache + batch)

Need to deploy a custom model with low ops overhead?
  -> Modal (Python), Replicate (Cog), Beam (Python + volumes), Cerebrium (Dockerfile)

Need dedicated GPU for high-throughput, latency-sensitive?
  -> HF Endpoints (multi-cloud, no cold start), Baseten Dedicated (best perf), RunPod Serverless (cheapest), Together Dedicated (open model focus)

Need image / video generation at scale?
  -> Fal.ai (Model API, per-output), RunPod Serverless (per-second), self-host on Lambda/RunPod Pods

Need regulated workload (HIPAA, SOC 2, data residency)?
  -> HF Endpoints Enterprise, Baseten self-hosted, Anyscale BYOC, Fireworks Reserved, Modal enterprise

Need raw GPU rental for training / fine-tuning?
  -> Lambda (no egress), RunPod Pods (broad catalog), Modal (per-second), Akash (auction)

Need sandbox / untrusted code execution?
  -> Beam Sandboxes, Modal Sandboxes
```

---

## Cross-Cutting Themes

1. **Pricing is converging on per-GPU-second for the "infrastructure" tier and per-token for the "API" tier.** Most providers offer both. The decision is workload-dependent, not provider-dependent.

2. **Cold starts are no longer the differentiator they were in 2022.** Modal, RunPod, Beam, and Cerebrium all have sub-second cold starts via memory snapshotting. The remaining cold-start tax is on private deployments and on less-trafficked models in the per-token tier.

3. **BYOC is the moat for regulated workloads.** Of the ten providers, only Beam, Baseten, Anyscale, HF Enterprise Hub, and Fireworks Reserved have a mature BYOC product. For most regulated workloads, the choice is among these five.

4. **OpenAI-compatible APIs are the table stakes for LLM serving.** All per-token providers (DeepInfra, Together, Fireworks, HF Endpoints via Router, Baseten Model API) expose OpenAI-compatible endpoints. For non-LLM workloads, proprietary SDKs remain the norm.

5. **Decentralized compute (Akash) is structurally different.** It is the only provider without SOC 2, HIPAA, or BYOC. It is also the cheapest published rate for many GPU types and the only one with no KYC. The trade-off is operational complexity (reverse auction) and slow lease creation.

6. **The "Banana.dev pattern" is real.** Serverless GPU is a capital-intensive business; the pioneer (Banana) was unable to sustain it against better-capitalized competitors. Expect continued consolidation.

---

## Related Concepts

- [[Concepts/serverless-gpu-pricing-models]] — the four pricing primitives and crossover math.
- [[Concepts/serverless-gpu-data-privacy]] — privacy patterns, compliance matrix, BYOC options.

---

## Open Questions / Next Research Directions

- [ ] **Benchmark latency and throughput head-to-head on a real workload.** This comparison is on price and features only. Real throughput on a specific model (e.g., Llama 3.3 70B at 1500 tok/s) varies by provider's serving engine. Build a benchmark with vLLM-equivalent and measure tokens/sec/$.
- [ ] **Quantify egress cost impact.** Lambda is zero-egress; HF Endpoints inherits AWS egress. For a high-traffic public inference API, the egress cost can rival GPU cost. Measure against a realistic traffic shape.
- [ ] **Test BYOC ease-of-setup on Anyscale, Beam, Baseten, HF.** All claim BYOC; the actual setup time and operational cost is not comparable without hands-on testing.
- [ ] **Track Akash's GPU availability over time.** Reverse auction rates depend on provider supply. The published range is a typical, not a guarantee. Track the live H100 bid distribution.
- [ ] **Investigate prompt-cache hit rates on Together and Fireworks.** The published cache discount is large; the actual hit rate on a realistic workload is workload-dependent.
