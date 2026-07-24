---
title: "Serverless GPU pricing models"
detail: "Comparison of the four pricing models used by serverless and on-demand GPU providers: per-output, per-token, per-GPU-second, and per-replica-hour."
details: "The serverless GPU market has converged on four primary billing primitives. Each maps to a different cost structure and a different set of workload patterns. Understanding the tradeoffs is the single highest-leverage decision when picking a provider."
tags:
  - concepts
created: 2026-07-24
updated: 2026-07-24
type: concept
source: "https://www.spheron.network/blog/serverless-gpu-vs-on-demand-vs-reserved/"
---
# Serverless GPU Pricing Models

The serverless and on-demand GPU market has converged on four primary billing primitives. Each maps to a different cost structure and a different set of workload patterns. Picking the right model (and the right provider within each model) is the single highest-leverage cost decision for an ML team.

## 1. Per-Output (Per-Image, Per-Second-of-Video)

**Examples:** Fal.ai (FLUX, Wan video)

The provider charges for the artifact produced, not the GPU time consumed. A FLUX image at 1024x1024 and 28 steps is a fixed cost regardless of whether the model is fast or slow on the chosen hardware.

| Strength | Weakness |
|---|---|
| Predictable cost per unit of business value | Cost scales linearly with volume; no economy of scale |
| Zero infrastructure thinking | Hard to estimate GPU cost for cost-per-revenue analysis |
| Good for prototyping and low-volume | High-volume workloads can be 2-3x more expensive than self-hosted |

**Best for:** Low-to-medium-volume image/video generation where the per-unit cost is offset by zero ops overhead.

## 2. Per-Token (Per-1M Input/Output Tokens)

**Examples:** DeepInfra, Together AI (serverless tier), Fireworks AI (serverless tier), OpenAI, Groq, Baseten (Model API)

The provider charges by token, split between input and output (sometimes with a cache discount on warmed prefixes). This is the OpenAI-compatible billing model.

| Strength | Weakness |
|---|---|
| Maps to revenue (you charge per token, you pay per token) | Prompt-cache discount adds accounting complexity |
| OpenAI-compatible APIs enable drop-in replacement | Cold starts on less-trafficked models can hurt latency |
| Strong unit economics for popular open models | Vendor lock-in per token; some models cost 3-5x more on different providers |

**Best for:** LLM serving with variable traffic, especially when prompt caching helps and per-request latency is acceptable.

## 3. Per-GPU-Second (Billed by the Second While Active)

**Examples:** Modal, RunPod Serverless, Beam, Cerebrium, Akash (per-block), Replicate (private deployments), Baseten Dedicated, Fireworks On-Demand, Anyscale, Lambda

The provider charges for the actual time a GPU is allocated. Most providers additionally offer per-minute or per-hour billing for always-on machines. Cold starts may or may not be billed.

| Strength | Weakness |
|---|---|
| Fine-grained control over cost vs utilization | Cost variance based on workload burstiness |
| Good fit for high-utilization workloads | Idle replicas still cost (unless scale-to-zero) |
| Maps directly to GPU inventory cost | Hard to forecast without historical data |

**Best for:** Variable workloads, bursty inference, training, fine-tuning. The dominant model in the category.

## 4. Per-Replica-Hour (Always-On, Often With Scale-to-Zero)

**Examples:** Hugging Face Inference Endpoints, Baseten Dedicated, Together Dedicated, Lambda Instances, Anyscale Services, RunPod Pods (also per-second), Hugging Face Dedicated

The provider charges per replica, billed per hour (or per minute), regardless of whether requests are running. Scale-to-zero endpoints pause the replica during idle periods and resume on traffic.

| Strength | Weakness |
|---|---|
| Predictable monthly cost | Idle replicas waste money |
| No cold starts on warm replicas | Scale-to-zero cold starts can be 1-2 minutes |
| Easy to reason about capacity | Higher baseline cost than per-GPU-second for low-traffic workloads |

**Best for:** Steady traffic, latency-sensitive workloads where cold starts are unacceptable, compliance/regulated workloads on dedicated infrastructure.

## Crossover Points

The break-even between per-token and per-GPU-second is workload-dependent. A common heuristic: a single H100 running vLLM at ~1,500 tok/s produces ~130M tokens/day. At $0.90/1M output tokens (Fireworks Standard tier), the per-token cost is ~$117/day. The same H100 on Fireworks On-Demand costs $7.00/hr x 24 = $168/day. Below 70% utilization, per-token is cheaper; above, dedicated GPU wins. The crossover shifts based on model, GPU, and prompt structure.

For per-output vs self-hosted: a FLUX.2-dev image on Fal.ai costs ~$0.012. The same image on a self-hosted H100 PCIe at $2.01/hr producing ~7 images/min takes 8.5 minutes and costs ~$0.29. The crossover is around 168 images per hour of active generation ([source](https://www.spheron.network/blog/fal-ai-alternatives/)).

## Hidden Costs to Watch

- **Cold start charges**: some providers bill boot time, others don't. Replicate bills cold start on private deployments; Cerebrium does not.
- **Idle replica billing**: per-replica-hour models charge 24/7 for any deployed replica.
- **Egress fees**: most providers are zero-egress, but AWS-based options (Hugging Face Endpoints on AWS, Anyscale BYOC) can carry AWS egress fees.
- **Cache hit-rate accounting**: Together and Fireworks both offer cache discounts, but the accounting can make per-token forecasts noisy.
- **Startup/idle on dedicated deployments**: Replicate private deployments bill for the full online time including startup and idle, not just active inference.

## Choosing a Model

| Workload pattern | Recommended model |
|---|---|
| Sporadic LLM serving, prompt-cache friendly | Per-token (DeepInfra, Together, Fireworks) |
| Bursty multimodal / image generation | Per-output (Fal.ai) or per-GPU-second (Modal, RunPod) |
| Steady-state LLM at >50% utilization | Per-GPU-second dedicated (Baseten, Fireworks On-Demand) |
| Latency-critical real-time | Per-replica-hour with no scale-to-zero (HF Endpoints, Baseten Dedicated) |
| Training / fine-tuning | Per-GPU-second (Lambda, RunPod Pods) |
| Censorship-resistant / cost-first | Per-block (Akash) |

## References

- [Replicate pricing](https://replicate.com/pricing)
- [Modal pricing](https://modal.com/pricing)
- [RunPod pricing](https://www.runpod.io/pricing)
- [Together AI pricing](https://www.together.ai/pricing)
- [Fireworks pricing](https://fireworks.ai/pricing)
- [Hugging Face pricing](https://huggingface.co/pricing)
- [Fal.ai pricing](https://fal.ai/pricing)
- [Baseten pricing](https://www.baseten.co/pricing/)
- [Beam pricing](https://www.beam.cloud/pricing)
- [Cerebrium pricing](https://cerebrium.ai/pricing)
- [Anyscale pricing](https://www.anyscale.com/pricing)
- [DeepInfra pricing](https://deepinfra.com/pricing)
- [Lambda pricing](https://lambda.ai/pricing)
- [Akash GPU deployments](https://akash.network/docs/learn/core-concepts/gpu-deployments/)
