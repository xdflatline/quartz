---
title: "Baseten"
detail: "Managed model deployment platform with the Truss open-source packaging framework, dedicated deployments, and Model APIs for open models."
details: "Baseten is an enterprise-focused inference platform that pairs the open-source Truss model packaging framework with managed dedicated deployments and per-token Model APIs. Known for the Baseten Inference Stack (custom kernels, decoding optimizations, advanced caching) and for serving high-throughput compound AI applications."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://www.baseten.co/pricing/"
---
# Baseten

**Category:** Platform (managed inference)

**Website:** [baseten.co](https://www.baseten.co/)
**Pricing page:** [baseten.co/pricing](https://www.baseten.co/pricing/)
**Docs:** [docs.baseten.co](https://docs.baseten.co/)

---

## Overview

Baseten is a model-deployment and inference platform aimed at production workloads for custom, fine-tuned, and open-source models. It is built around Truss, an open-source Python framework for packaging models, and offers both dedicated deployments (per-replica-minute billing) and per-token Model APIs for popular open models. Baseten also offers self-hosted deployment inside a customer's VPC (Enterprise tier).

## Key Details

### Pricing (Dedicated Deployments, per-minute, July 2026)

| GPU | VRAM | Rate | Source |
|---|---|---|---|
| T4 | 16 GB | $0.01052/min (~$0.63/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |
| L4 | 24 GB | $0.01414/min (~$0.85/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |
| A10G | 24 GB | $0.02012/min (~$1.21/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |
| A100 | 80 GB | $0.06667/min (~$4.00/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |
| H100 MIG | 40 GB | $0.0625/min (~$3.75/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |
| H100 | 80 GB | $0.10833/min (~$6.50/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |
| B200 | 180 GB | $0.16633/min (~$9.98/hr) | [baseten.co/pricing](https://www.baseten.co/pricing/) |

### Model API (per-token)

Examples (from the [Baseten pricing page](https://www.baseten.co/pricing/)):
- gpt-oss-120B: $0.10 input / $0.50 output per 1M tokens
- GLM-4.7: $0.60 input / $2.20 output per 1M tokens
- DeepSeek V4 Pro: $1.74 input / $3.48 output per 1M tokens
- Kimi K2.7 Code: $0.95 input / $4.00 output per 1M tokens
- Inkling: $1.00 input / $4.05 output per 1M tokens

### API and SDK

- OpenAI-compatible Model API.
- Truss (open-source Python framework) for packaging custom models.
- Baseten Chains for compound AI / multi-model workflows.
- Python SDK + REST API.
- Per-deployment HTTPS endpoint.

## Provisioning

- **CLI:** `truss` — install via `pip install --upgrade truss`; auth via `truss login` (or `uvx truss login`). The deployment loop is `truss push --watch` (dev), `truss watch` (live patch), `truss push --promote` (production). See [Truss CLI reference](https://docs.baseten.co/reference/cli/truss/overview).
- **Terraform:** No first-party Terraform provider as of July 2026. Truss is the canonical IaC-adjacent deployment surface; `truss push` is typically wired into CI.
- **API:** REST API for deployments, model APIs, fine-tuning.
- **Web UI:** Baseten dashboard for model playground, deployment config, monitoring.
- **GitHub Actions:** Standard pattern is `truss push` from CI; Truss supports `truss push --watch` for live reload during development.
- **CLI examples:** `truss push --watch`, `truss push --promote`, `truss watch`.

### Cold starts

Blazing-fast cold starts on the Baseten Inference Stack. Some workloads achieve sub-300ms first-token latency.

### Data privacy

- SOC 2 Type II compliant.
- HIPAA compliant.
- Self-hosted (your VPC) deployment available on enterprise tier.
- Single-tenant clusters for additional workload isolation.
- On-demand flex compute on Baseten Cloud as overflow for self-hosted.

### Storage

No native persistent storage; weights are packaged into the Truss deployment. S3/GCS accessible from the runtime via standard clients. No bundled blob storage.

### Free tier

$30 free credit on sign-up via the [Model API free tier](https://app.baseten.co/signup/). $0/month "Basic" tier with pay-as-you-go dedicated deployments.

## Strengths

- Baseten Inference Stack ships custom kernels and decoding optimizations for frontier-model performance.
- Truss is open-source, so models can be developed locally and deployed without lock-in.
- Self-hosted (your VPC) option for regulated workloads.
- Strong support for compound AI (Baseten Chains) and audio (sub-300ms transcription).

## Limitations

- Per-replica-hour pricing means idle replicas still cost money; not ideal for spiky traffic.
- Truss adds a deployment abstraction that creates some switching cost if migrating to another platform.
- H100 dedicated rate (~$6.50/hr) is among the highest in the category.
