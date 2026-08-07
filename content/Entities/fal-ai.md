---
title: "Fal.ai"

details: "Fal.ai specializes in fast inference for image, video, 3D, and audio generation models (FLUX, Stable Diffusion, Wan, Hunyuan, LTX-Video, ControlNet, etc.). Pricing is per output unit (image, megapixel, second of video) rather than per GPU-second. Also offers a Compute product for raw GPU access."
tags:
  - entities
  - inference
  - serverless
created: 2026-07-24
updated: 2026-07-24
type: entity
source: "https://fal.ai/pricing"
---
# Fal.ai

**Category:** Platform (generative-media serverless inference)

**Website:** [fal.ai](https://fal.ai/)
**Pricing page:** [fal.ai/pricing](https://fal.ai/pricing)
**Serverless product:** [fal.ai/serverless](https://fal.ai/serverless)
**Docs:** [docs.fal.ai](https://docs.fal.ai/)

---

## Overview

Fal.ai is a serverless inference platform focused on generative media. The company operates one of the largest model galleries for image and video (FLUX, Stable Diffusion, Wan, Hunyuan, LTX-Video, ControlNet, etc.) and is the inference engine behind parts of Perplexity, Quora/Poe, and Canva. Pricing is per output unit (per image, per megapixel, per second of video) on the Model API, and per-GPU-second for custom deployments.

## Key Details

### Model API pricing (per output)

Pricing varies by model. Examples:
- FLUX.1-schnell: per-megapixel rate (~$0.003-0.05 per image depending on resolution/steps)
- FLUX.2-dev: ~$0.012 per 1024x1024 image at 28 steps (third-party benchmark)
- Wan 2.x video: ~$0.05/second of output video

Full model list at [fal.ai/pricing](https://fal.ai/pricing).

### Compute (per-second GPU, July 2026)

| GPU | List Price | Discounted | Source |
|---|---|---|---|
| B300 288GB | $8.50/hr | $4.49/hr | [fal.ai/pricing](https://fal.ai/pricing) |
| B200 180GB | $6.25/hr | $3.49/hr | [fal.ai/pricing](https://fal.ai/pricing) |
| H200 141GB | $4.50/hr | $2.10/hr | [fal.ai/pricing](https://fal.ai/pricing) |
| H100 80GB | $3.99/hr | $1.89/hr | [fal.ai/pricing](https://fal.ai/pricing) |
| RTX PRO 6000 96GB | $2.99/hr | $1.10/hr | [fal.ai/pricing](https://fal.ai/pricing) |

Reserved (committed-spend) pricing unlocks the discounted rates.

### API and SDK

- HTTP/REST + Python (`fal-client`) and TypeScript SDKs.
- Webhook callbacks for async jobs.
- Streaming responses.
- Custom model deployment via Docker image or `fal/apps` CLI.

## Provisioning

- **CLI:** `fal` — install via `pip install fal`; `fal auth login`; `fal deploy my_app.py::MyApp`. See [fal CLI overview](https://fal.ai/docs/api-reference/python-sdk/cli).
- **Terraform:** First-party provider at [github.com/fal-ai/terraform-provider-fal](https://github.com/fal-ai/terraform-provider-fal).
- **API:** REST API for inference, model registration, webhook callbacks.
- **Web UI:** Fal dashboard at [fal.ai/dashboard](https://fal.ai/dashboard) for model playground, custom deployment, environment management.
- **GitHub Actions:** Common pattern is `fal deploy` in CI; documented in [fal quick start](https://fal.ai/docs/documentation/development/getting-started/quick-start).
- **CLI examples:** `fal deploy hello_world.py::MyApp`, `fal environments create staging --description "Staging environment"`.

### Cold starts

No cold starts on the Model API (Fal maintains warm capacity for popular models). Custom Compute deployments have brief cold start on first request.

### Data privacy

- SOC 2 compliant.
- Single Sign-On and private endpoints on enterprise tier.
- Self-serve does not offer BYOC or specific data residency guarantees.

### Storage

Fal-managed object storage for input/upload. Outputs returned in the response and persisted in Fal's storage with a TTL. Customer-managed S3/GCS is supported via the Bring-Your-Own-Storage option on enterprise.

### Free tier

Limited free credits on sign-up; no permanent free tier for the Model API.

## Strengths

- Deep specialization in generative media; consistently among the fastest image/video inference engines in benchmarks.
- Per-output pricing is predictable for content-generation use cases.
- Large model gallery with many fine-tuned variants and ControlNet adapters.

## Limitations

- API-bounded inference parameters (no custom samplers, no LoRA chains, no checkpoint-level access).
- No multi-LoRA support in the Model API.
- Per-output costs scale linearly with volume, so high-volume workloads can be more expensive than self-hosted GPU.
