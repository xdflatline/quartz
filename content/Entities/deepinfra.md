---
title: "DeepInfra"

details: "DeepInfra is an AI inference cloud that provides serverless APIs for 100+ open-weight models (LLM, embeddings, image, speech) on H100/A100 hardware, plus dedicated GPU rentals. The API is OpenAI-compatible. Known for transparent pricing, low per-token rates, and a simple per-request billing model."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://deepinfra.com/pricing"
---
# DeepInfra

**Category:** Platform (serverless inference API + GPU cloud)

**Website:** [deepinfra.com](https://deepinfra.com/)
**Pricing page:** [deepinfra.com/pricing](https://deepinfra.com/pricing)
**Docs:** [deepinfra.com/docs](https://deepinfra.com/docs)

---

## Overview

DeepInfra is an AI inference cloud running 100+ open-weight models as serverless API endpoints (Kimi K2, Qwen3.5, GLM-5, DeepSeek V3.2, gpt-oss-120B, Llama 3.x/4.x, Nemotron, FLUX 3, Whisper, etc.). The API is OpenAI-compatible, so switching from OpenAI usually means changing a base URL and API key. DeepInfra also offers dedicated GPU rentals at transparent hourly rates.

## Key Details

### Pricing (per-token serverless, July 2026)

Examples from the DeepInfra model list:
- gpt-oss-120B: ~$0.08 per 1M blended tokens (third-party aggregator)
- Llama 3.2 3B: from $0.02 per 1M tokens
- Largest models: ~$1.50 per 1M tokens

No minimum commitment. Automatic tier progression reduces cost as spending increases. Full per-model pricing at [deepinfra.com/pricing](https://deepinfra.com/pricing).

### Dedicated GPU (per hour, transparent)

- A100, H100, H200, B200, B300 all published.
- H100 starting from $0.89/hr according to third-party aggregators.
- No long-term commitments; pay-as-you-go.

### API and SDK

- OpenAI-compatible HTTP API.
- Streaming, function calling, JSON mode, structured output.
- LoRA adapter support for text and image models.
- Custom model deployment.
- Python and JavaScript SDKs.

## Provisioning

- **CLI:** No first-party DeepInfra CLI as of July 2026. The REST API is the primary provisioning surface; inference is also available via the OpenAI-compatible endpoint with no setup beyond the API token.
- **Terraform:** No first-party DeepInfra Terraform provider. Customers typically drive deployments via the REST API in CI.
- **API:** REST API for inference, model deployment, dedicated GPU rental, deploy stats. See [DeepInfra API reference](https://docs.deepinfra.com/api-reference/introduction).
- **Web UI:** DeepInfra dashboard at [deepinfra.com/dashboard](https://deepinfra.com/dashboard) for model playground, deployments, usage.
- **GitHub:** Standard pattern is curl/HTTP from CI; the docs include a [Native API](https://docs.deepinfra.com/apis/deepinfra-native) reference with curl examples for every model type.
- **API examples:** `curl -X POST https://api.deepinfra.com/v1/inference/<model> -H "Authorization: Bearer $DEEPINFRA_TOKEN" -d '{"prompt":"..."}'`

### Cold starts

No cold starts on popular public models. Less-trafficked models may cold start.

### Data privacy

- SOC 2, ISO 27001, GDPR, and HIPAA compliance certifications.
- US-based secure data centers.
- No documented BYOC; data resides in DeepInfra's infrastructure.

### Storage

No native persistent storage beyond model weights. S3/GCS accessible via standard clients from the runtime.

### Free tier

Free trial credit on sign-up. No permanent free tier.

## Strengths

- Among the lowest per-token rates in the market on common open models.
- OpenAI-compatible API for drop-in replacement.
- Simple per-request billing, no replica overhead.
- Wide model catalog (100+ open-weight models).

## Limitations

- Not all models have LoRA adapter support.
- No BYOC or VPC peering.
- Less brand awareness than Together, Fireworks, or Replicate.
