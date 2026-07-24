---
title: "Replicate"
detail: "Serverless GPU inference platform with a public model registry; per-second GPU billing, scale-to-zero, no infra to manage."
details: "Replicate runs any ML model via a simple HTTP API. Users pick a public model from a registry of 50,000+ community and official models (FLUX, Stable Diffusion, Llama, Whisper, etc.) or deploy their own Cog container. Cold starts exist on private deployments but are typically free on popular public models that are kept warm by shared traffic."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://replicate.com/pricing"
---
# Replicate

**Category:** Platform (hosted inference API)

**Website:** [replicate.com](https://replicate.com/)
**Pricing page:** [replicate.com/pricing](https://replicate.com/pricing)
**Docs:** [replicate.com/docs](https://replicate.com/docs)

---

## Overview

Replicate is one of the earliest and largest serverless GPU inference marketplaces. Acquired by Cloudflare in late 2025, it remains a stand-alone product with the same per-second GPU billing model. The platform exposes a 50,000+ model registry (FLUX, Stable Diffusion variants, Llama, Whisper, etc.) as well as a hosted deployment surface for custom Cog containers.

## Key Details

### Pricing (per-second GPU, July 2026)

| Tier | Rate | Source |
|---|---|---|
| CPU | $0.000025/sec | [replicate.com/pricing](https://replicate.com/pricing) |
| NVIDIA T4 | $0.000225/sec (~$0.81/hr) | [replicate.com/pricing](https://replicate.com/pricing) |
| A100 80GB | $0.001400/sec (~$5.04/hr) | [replicate.com/pricing](https://replicate.com/pricing) |
| H100 | $0.001525/sec (~$5.49/hr) | [replicate.com/pricing](https://replicate.com/pricing) |
| Output-based (FLUX, etc.) | flat per-image / per-token | [replicate.com/pricing](https://replicate.com/pricing) |

Public models on shared hardware charge only for the active inference; setup and idle are free. Private deployments bill for the full online time including startup and idle, so cold start costs can be 10x the active compute cost for infrequently used models.

## API and SDK

- HTTP/REST + official Python and JavaScript clients.
- Webhooks for asynchronous predictions.
- Streaming responses supported for text models.
- Custom model deployment via [Cog](https://github.com/replicate/cog) container format.

## Provisioning

- **CLI:** `cog` (build, push, run) and the `replicate` CLI for managing models and predictions.
- **Terraform:** Community provider at [github.com/replicate/terraform-provider-replicate](https://github.com/replicate/terraform-provider-replicate) — manages deployment config via `terraform apply`. Not on the public Terraform Registry.
- **API:** REST API + webhooks; everything the CLI does is also available as an HTTP endpoint.
- **Web UI:** Replicate web dashboard for browsing models, viewing runs, configuring private deployments.
- **CI/CD:** Documented GitHub Actions workflow for `cog-safe-push` (continuous model deployment); see [Replicate CI/CD guide](https://replicate.com/docs/guides/build/continuous-model-deployment).
- **Cog:** The deployment surface is the Cog container format; `cog push` publishes a model, which then becomes a versioned API.

### Cold starts

Free on popular public models (other users keep them warm). On private deployments, cold starts of 1-2 minutes on H100 are common and bill for full boot time.

### Data privacy

- Public models run on shared infrastructure; data is in flight to the GPU during inference.
- Private deployments are dedicated but still on Replicate's hardware. There is no VPC peering or BYOC option.
- Replicate logs requests for billing/debugging. There is no documented data residency or HIPAA offering on the standard serverless tier.

### Storage

No native persistent storage beyond model weights. Input data is sent in the request body or via signed URL upload to Replicate-managed blob storage. Output is returned in the response and can be downloaded.

### Free tier

Limited number of free predictions to evaluate the platform. Production usage requires adding a payment method.

## Strengths

- Largest model registry in the category, including the FLUX and Stable Diffusion ecosystem.
- Free idle time on public models makes it cost-effective for sporadic workloads.
- Simple HTTP API, no SDK lock-in.

## Limitations

- Private deployments pay for boot/idle time, so utilization must be high to be cost-effective.
- No bare-metal, BYOC, or VPC peering option.
- Per-second rates on H100 are higher than bare-metal providers like Spheron ($2.01/hr) and Beam ($3.50/hr).
