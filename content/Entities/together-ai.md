---
title: "Together AI"
detail: "Open-model focused inference API with per-token serverless, single-tenant Dedicated Endpoints, and GPU Clusters for fine-tuning."
details: "Together AI runs an OpenAI-compatible serverless API for 100+ open models, plus single-tenant GPU instances and multi-GPU clusters. Known for low per-token rates, optimized inference (ATLAS speculative decoding on dedicated endpoints), and competitive fine-tuning pricing."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://www.together.ai/pricing"
---
# Together AI

**Category:** Platform (open-model inference API + GPU cloud)

**Website:** [together.ai](https://www.together.ai/)
**Pricing page:** [together.ai/pricing](https://www.together.ai/pricing)
**Serverless product:** [together.ai/serverless-inference](https://www.together.ai/serverless-inference)
**Docs:** [docs.together.ai](https://docs.together.ai/)

---

## Overview

Together AI is an inference and fine-tuning platform focused on open-source models. It exposes a per-token serverless API for 100+ open models (Llama, Qwen, DeepSeek, Mistral, FLUX, etc.) as well as Dedicated Endpoints (single-tenant GPU instances) and GPU Clusters (multi-node training/fine-tuning). The serverless API is OpenAI-compatible and offers an automatic prompt-cache discount on warmed prefixes.

## Key Details

### Pricing (per-token serverless, July 2026)

| Model class | Rate | Source |
|---|---|---|
| Llama 3.3 70B (input/output) | $1.04 / $1.04 per 1M tokens | third-party aggregator |
| Serverless per-token | per-model, model list at [together.ai/pricing](https://www.together.ai/pricing) | [together.ai/pricing](https://www.together.ai/pricing) |
| Cached input discount | automatic, no opt-in (prompt prefix reuse) | [docs.together.ai](https://docs.together.ai/docs/serverless/overview) |
| Batch API | 50% off for async non-urgent inference | [together.ai/pricing](https://www.together.ai/pricing) |

### Dedicated Endpoints / GPU Clusters

| Resource | Rate | Source |
|---|---|---|
| H100 on-demand (per GPU) | $5.49/hr | third-party aggregator |
| H100 reserved (7-30 day) | from $3.99/hr | third-party aggregator |
| H200 on-demand | $6.79/hr | third-party aggregator |
| Fine-tune hosting | $4 minimum per job, per-token billing | [together.ai/pricing](https://www.together.ai/pricing) |

### API and SDK

- OpenAI-compatible HTTP API.
- Image, video, audio, embeddings, rerank, and chat endpoints share one schema.
- Streaming, function calling, JSON mode supported.
- Python and TypeScript SDKs.

## Provisioning

- **CLI:** `tg` (the Together CLI) — install via `uv tool install "together[cli]"`; supports fine-tuning, checkpoint management, and GPU cluster operations. See [Together CLI getting started](https://docs.together.ai/reference/cli/getting-started).
- **Terraform:** Community provider at [github.com/togethercomputer/terraform-provider-together](https://github.com/togethercomputer/terraform-provider-together) — manages dedicated endpoints and clusters.
- **API:** REST API for chat, embeddings, images, audio, fine-tuning, and GPU clusters.
- **Web UI:** Together dashboard for model playground, fine-tuning, cluster creation.
- **SkyPilot:** Together publishes a SkyPilot integration for cluster workloads. See [Together GPU clusters API docs](https://docs.together.ai/docs/gpu-clusters-api).
- **CI/CD:** Documented GitHub Actions pattern using the `tg` CLI for cluster create/run/cleanup.
- **CLI examples:** `tg beta clusters create --name my-cluster --num-gpus 8 --gpu-type H100_SXM --region us-central-8 --billing-type ON_DEMAND --cluster-type KUBERNETES`

### Cold starts

Serverless tier has cold starts on less-trafficked models. Dedicated Endpoints have no cold starts.

### Data privacy

- SOC 2 Type II compliant.
- HIPAA available on enterprise tier.
- Dedicated Endpoints are single-tenant but still on Together's hardware; no documented BYOC.

### Storage

No native persistent storage; weights are loaded from Together's model registry or Hugging Face IDs uploaded at endpoint creation. Customer data in flight is processed on Together's infrastructure.

### Free tier

$5 in free credit on sign-up; no permanent free tier.

## Strengths

- Strong throughput tuning for Qwen, DeepSeek, Llama families.
- Automatic prompt caching reduces effective cost for chat workloads with repeated system prompts.
- Batch API offers 50% off for non-urgent workloads.

## Limitations

- No bare-metal or BYOC; data residency is fixed to Together's regions.
- H100 on-demand rate is higher than bare-metal providers (~$2/hr).
- Serverless rate limits and cold starts can hurt latency-sensitive real-time workloads.
