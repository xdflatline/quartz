---
title: "Fireworks AI"
detail: "Open-source model inference platform with FireAttention (custom kernels), per-token serverless, and per-second on-demand GPU deployments."
details: "Fireworks AI hosts 200+ open-source models (text, vision, audio, image, embeddings) on optimized inference infrastructure. The platform pairs a serverless per-token API with on-demand GPU deployments, plus the FireOptimizer stack for SFT, LoRA, RFT, and RL fine-tuning. Known for low latency via custom FireAttention kernels."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://fireworks.ai/pricing"
---
# Fireworks AI

**Category:** Platform (inference + fine-tuning)

**Website:** [fireworks.ai](https://fireworks.ai/)
**Pricing page:** [fireworks.ai/pricing](https://fireworks.ai/pricing)
**Docs:** [docs.fireworks.ai](https://docs.fireworks.ai/)

---

## Overview

Fireworks AI is a production inference and adaptation platform built by former Meta PyTorch team members. It hosts 200+ open-source models (text, vision, audio, image, embeddings) and ships a custom inference engine (FireAttention) plus a full post-training stack (FireOptimizer: SFT, LoRA, RFT, RL). Three deployment tiers: per-token Serverless, per-GPU-second On-Demand, and Enterprise Reserved with custom SLAs and BYOC.

## Key Details

### Pricing (Serverless, per-token, July 2026)

| Tier | Rate | Source |
|---|---|---|
| Text/vision <4B parameters | from $0.10/1M tokens | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| 70B-class | from $0.90/1M tokens (Standard) | third-party aggregator |
| Cached tokens | 50% off cached input | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| Batch | 50% off input and output | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| Image generation (non-FLUX) | from $0.00013/step | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| FLUX.1 image generation | from $0.00035/step | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| Embeddings | from $0.008/1M input tokens | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| Speech-to-text (Whisper) | from $0.0009/audio minute | [fireworks.ai/pricing](https://fireworks.ai/pricing) |

### On-Demand (per-second GPU, no startup charge)

| GPU | Rate | Source |
|---|---|---|
| H100 80GB | $7.00/hr | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| H200 141GB | $7.00/hr | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| B200 180GB | $10.00/hr | [fireworks.ai/pricing](https://fireworks.ai/pricing) |
| B300 288GB | $12.00/hr | [fireworks.ai/pricing](https://fireworks.ai/pricing) |

### Fine-tuning

From $0.50 per 1M training tokens, LoRA or full-param. Billed per GPU-second at the same rate as On-Demand deployments.

### API and SDK

- OpenAI-compatible HTTP API.
- Function calling, vision, audio endpoints share one schema.
- Streaming and structured outputs.
- Python and JavaScript SDKs.

### Cold starts

Serverless tier claims no cold boots. On-Demand deployments have brief container spin-up.

### Data privacy

- 99.9% uptime SLA.
- SOC 2 Type II compliant.
- Enterprise Reserved offers bring-your-own-cloud and custom SLAs.
- Self-serve tiers do not offer data-residency guarantees.

### Storage

No native persistent storage beyond model weights; weights uploaded at deployment time. S3/GCS are accessible via standard clients from the runtime.

### Free tier

$1 in free credits on sign-up. No permanent free tier.

## Strengths

- FireAttention engine claims 3-12x lower latency and up to 5.6x higher throughput than self-hosted vLLM.
- Inference and fine-tuning are exposed under the same API.
- 200+ open models with new weights typically available within 24 hours of public release.

## Limitations

- On-Demand GPU pricing starts at $7/hr for H100, which is higher than bare-metal providers.
- Some specialized providers (DeepInfra, Fireworks' own serverless for some models) can undercut Fireworks on raw per-token cost.
- Not the lowest per-token price in every model category.
