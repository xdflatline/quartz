---
title: "RunPod"

details: "RunPod offers two products: Pods (full GPU instances billed per second with no ingress fees) and Serverless (queue-based workers or load-balanced HTTP endpoints with scale-to-zero). The platform is known for aggressive pricing via Community Cloud and a broad GPU catalog from consumer (4090, 5090) to data-center (H100, H200, B200, B300)."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://www.runpod.io/pricing"
---
# RunPod

**Category:** Platform (GPU cloud + serverless)

**Website:** [runpod.io](https://www.runpod.io/)
**Pricing page:** [runpod.io/pricing](https://www.runpod.io/pricing)
**Serverless product:** [runpod.io/product/serverless](https://www.runpod.io/product/serverless)
**Docs:** [docs.runpod.io](https://docs.runpod.io/)

---

## Overview

RunPod is a GPU cloud that exposes two distinct products: Pods (dedicated VM-like GPU instances billed per second) and Serverless (queue-based workers or load-balanced HTTP endpoints with scale-to-zero and per-second billing). It carries one of the broadest GPU catalogs in the category, from consumer-grade RTX 4090/5090 to data-center H100, H200, B200, and B300.

## Key Details

### Pricing (Pods, per-second, July 2026)

| GPU | Rate | Source |
|---|---|---|
| RTX 4090 (24GB) | $0.69/hr | [runpod.io/pricing](https://www.runpod.io/pricing) |
| RTX 5090 (32GB) | $0.99/hr | [runpod.io/pricing](https://www.runpod.io/pricing) |
| A100 PCIe (80GB) | $1.49/hr | [runpod.io/pricing](https://www.runpod.io/pricing) |
| H100 PCIe (80GB) | $2.89/hr (Secure) / $1.39/hr (Community) | [runpod.io/pricing](https://www.runpod.io/pricing) |
| H200 | $3.19/hr | [runpod.io/pricing](https://www.runpod.io/pricing) |
| B200 | $4.39/hr | [runpod.io/pricing](https://www.runpod.io/pricing) |
| B300 | $7.39/hr | [runpod.io/pricing](https://www.runpod.io/pricing) |

### Serverless

Sub-200ms FlashBoot cold starts, per-second billing, scale to zero. H100 serverless workers run at $4.18/hr effective rate according to third-party benchmarks; entry-level 16GB GPU class workers start at $0.58/hr. RunPod also publishes a public-endpoints catalog with flat per-request pricing for popular models (FLUX, SDXL, Wan, etc.).

### API and SDK

- REST API + runpodctl CLI.
- Python and JavaScript SDKs.
- Serverless endpoints accept custom Docker images or Git repos as worker definitions.
- Queue-based (async job) and load-balanced (HTTP) endpoint types.

## Provisioning

- **CLI:** `runpodctl` — install via `brew install runpod/runpodctl/runpodctl`, `wget -qO- cli.runpod.net | sudo bash`, conda, or pixi. See [runpodctl overview](https://docs.runpod.io/runpodctl/overview).
- **Terraform:** First-party provider at [registry.terraform.io/providers/decentralized-infrastructure/runpod](https://registry.terraform.io/providers/decentralized-infrastructure/runpod/latest/docs).
- **API:** REST API at `https://rest.runpod.io/v1` for Pods, Serverless, and endpoints; full documentation in the RunPod docs.
- **Web UI:** RunPod Console at [console.runpod.io](https://console.runpod.io/) for Pod deployment, Serverless endpoint config, Hub model playground.
- **Docker / Hub:** RunPod Hub is a community model registry; one-click deploy from the Hub to a Pod or Serverless endpoint.
- **CLI examples:** `runpodctl pod create --name hello --gpu-id "NVIDIA A40" --image "runpod/pytorch:..."`

### Cold starts

FlashBoot claims sub-200ms cold starts on the serverless product. Bare-metal Pods have a 1-3 minute boot time.

### Data privacy

- SOC 2 Type II compliant.
- HIPAA available on enterprise plans.
- Community Cloud GPUs are run by independent providers and may not meet the same compliance bar as Secure Cloud.
- No documented BYOC or VPC peering option; data lives on RunPod's hardware.

### Storage

Network volumes (persistent block storage) and container registry built in. S3-compatible blob storage is not bundled but is trivially attached via standard SDKs.

### Free tier

No permanent free tier. $25 sign-up credit on first account.

## Strengths

- Broadest GPU catalog in the category (consumer to data-center).
- Community Cloud provides some of the lowest H100 rates in the market.
- Two product surfaces (Pods and Serverless) cover both training and inference.

## Limitations

- Community Cloud GPUs can be preempted; Secure Cloud is the reliable tier.
- Documentation and orchestration tooling are weaker than Modal or Baseten.
- No native multi-region orchestration for global low-latency deployment.
