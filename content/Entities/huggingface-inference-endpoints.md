---
title: "Hugging Face Inference Endpoints"

details: "Hugging Face Inference Endpoints run any model from the Hub on dedicated infrastructure (AWS, GCP, or Azure) with auto-scaling. Endpoints are billed per-replica-hour, with optional scale-to-zero. There is also a free Inference API for prototyping and a multi-provider Inference Router (HF Router) for accessing serverless inference from many providers behind one API."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://huggingface.co/pricing"
---
# Hugging Face Inference Endpoints

**Category:** Platform (managed model deployment)

**Website:** [huggingface.co](https://huggingface.co/)
**Pricing page:** [huggingface.co/pricing](https://huggingface.co/pricing)
**Endpoints product:** [endpoints.huggingface.co](https://endpoints.huggingface.co/)
**Inference Providers (router):** [huggingface.co/docs/inference-providers](https://huggingface.co/docs/inference-providers/en/index)

---

## Overview

Hugging Face offers two inference surfaces: (1) **Inference Endpoints** (dedicated, fully-managed model deployments with no cold starts, scale-to-zero option) and (2) **Inference Providers** (a router that exposes 100+ models via a single OpenAI-compatible API, fanning out to underlying providers like Together, Replicate, and others). The Hub itself also exposes a free, rate-limited **Inference API** for prototyping.

## Key Details

### Pricing (Dedicated Endpoints, per-replica-hour, July 2026)

| Hardware | Configuration | Rate | Source |
|---|---|---|---|
| CPU | various | from $0.033/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| NVIDIA T4 (AWS) | 1x | $0.50/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| NVIDIA L4 (AWS) | 1x | $0.80/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| NVIDIA A10G (AWS) | 1x | $1.00/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| NVIDIA A100 (AWS) | 1x | $2.50/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| NVIDIA H100 (AWS) | 1x | $5.00/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| Inferentia2 (AWS) | 1x | $0.75/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| TPU v5e (GCP) | 1x1 | $1.20/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |
| NVIDIA RTX PRO 6000 (AWS) | 1x | $2.75/hr | [huggingface.co/pricing](https://huggingface.co/pricing) |

Endpoint formula: `instance hourly rate x ((hours x # min replicas) + (scale-up hours x # additional replicas)) = monthly cost` (from [Inference Endpoints pricing docs](https://huggingface.co/docs/inference-endpoints/en/pricing)).

### Inference API (free tier)

Rate-limited free inference for any model on the Hub, used for evaluation. Rate limits apply; no SLA.

### Inference Providers (router)

A single OpenAI-compatible API at `https://router.huggingface.co/v1/chat/completions` routes to a selection of underlying providers. Pricing is the underlying provider's price; HF adds convenience.

### API and SDK

- OpenAI-compatible HTTP API for chat, embeddings, image generation.
- Python `huggingface_hub` and JavaScript `@huggingface/inference` SDKs.
- Dedicated Endpoints expose a private HTTPS URL with token auth.
- Webhooks for async tasks.

## Provisioning

- **CLI:** `hf` (huggingface_hub Python CLI) — `hf endpoints deploy <name> --repo <repo> --framework pytorch --accelerator gpu --vendor aws --region us-east-1 --instance-size x2 --task text-generation`. Also `hf endpoints catalog deploy --repo <model>` for one-click catalog deploys.
- **Terraform:** Community provider at [github.com/issamemari/terraform-provider-huggingface](https://github.com/issamemari/terraform-provider-huggingface) — `huggingface_endpoint` resource with compute/model/cloud blocks.
- **Python SDK:** `huggingface_hub.create_inference_endpoint(...)` for programmatic endpoint creation with custom images and env vars.
- **API:** REST API for endpoint lifecycle, model registry, inference router.
- **Web UI:** Hugging Face dashboard for endpoint management, plus the catalog UI for one-click deploys.
- **Enterprise Hub:** Self-hosted Hub inside the customer's cloud supports all the same provisioning primitives.

### Cold starts

No cold starts on Dedicated Endpoints (replicas stay warm). Cold starts on the free Inference API.

### Data privacy

- SOC 2 Type II compliant.
- HIPAA available on enterprise plans.
- Endpoints run in your choice of AWS / GCP / Azure region.
- Customer data is processed on the dedicated instance for the duration of the request.
- Self-hosted enterprise option: "Enterprise Hub" runs entirely inside the customer's cloud.

### Storage

Hugging Face Hub acts as a model registry (private repos on paid plans). Inference Providers do not require uploaded weights; models are loaded from the Hub. S3/GCS integration is via standard client libraries.

### Free tier

Free Inference API for prototyping (rate-limited). Pro account ($9/month) adds private repos, higher rate limits, and zero-data-retention training.

## Strengths

- Tight integration with the Hugging Face Hub (one-click deployment of any of 1M+ models).
- Multi-cloud (AWS, GCP, Azure) with region selection for data residency.
- Inference Providers router is a single API surface for many underlying providers.
- Enterprise Hub can be fully self-hosted inside the customer's cloud.

## Limitations

- Dedicated Endpoints price is per-replica-hour, so idle replicas still cost money.
- Cold start behavior on scale-to-zero endpoints is not always predictable.
- Not the cheapest per-token option in the category.
