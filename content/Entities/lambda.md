---
title: "Lambda"
detail: "GPU cloud provider focused on AI training and inference, with on-demand H100, H200, B200 instances and 1-Click Clusters for multi-node jobs."
details: "Lambda (Lambda Cloud) provides NVIDIA GPU instances (H100, H200, B200, A100, GH200) billed per-minute with no egress fees. Known for 1-Click Clusters (16 to 2,000+ GPU production clusters) and Superclusters. Lambda does not natively run a per-token serverless API but exposes its infrastructure for on-demand and reserved inference workloads."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://lambda.ai/pricing"
---
# Lambda

**Category:** Platform (GPU cloud)

**Website:** [lambda.ai](https://lambda.ai/)
**Pricing page:** [lambda.ai/pricing](https://lambda.ai/pricing)
**Instances page:** [lambda.ai/instances](https://lambda.ai/instances)

---

## Overview

Lambda is a GPU cloud provider purpose-built for AI training and inference. It exposes single-GPU instances (1-8x configurations) and multi-node Clusters (16-2,000+ GPUs) with InfiniBand interconnect. Lambda is known for transparent per-minute pricing, no egress fees, and tight integration with common ML frameworks.

Lambda does not offer a per-token serverless API; it is positioned as raw GPU infrastructure. Customers run their own inference server (vLLM, TGI, SGLang, etc.) on top.

## Key Details

### Pricing (per-GPU-hour, July 2026)

| GPU | Configuration | Rate | Source |
|---|---|---|---|
| NVIDIA A100 PCIe 40GB | 1-8 GPUs | $1.99/hr | [lambda.ai/instances](https://lambda.ai/instances) |
| NVIDIA A6000 48GB | 1-8 GPUs | $1.09/hr | [lambda.ai/instances](https://lambda.ai/instances) |
| H100 PCIe 80GB | 1-8 GPUs | contact sales / from ~$2.49/hr reserved | [lambda.ai/pricing](https://lambda.ai/pricing) |
| H200 | reserved | contact sales | [lambda.ai/pricing](https://lambda.ai/pricing) |
| B200 | reserved | contact sales | [lambda.ai/pricing](https://lambda.ai/pricing) |

1-Click Clusters (16-2,000+ GPU H100 or B200) and Superclusters are quoted on request.

### API and SDK

- Web dashboard for instance provisioning.
- Lambda Cloud API for programmatic provisioning.
- SSH access to instances.
- Compatible with standard NVIDIA CUDA, vLLM, TGI, SGLang stacks.

### Cold starts

No platform-induced cold starts. Container/VM boot time is typical Linux VM boot (1-3 minutes).

### Data privacy

- SOC 2 Type II compliant.
- HIPAA available on enterprise plans.
- Reserved capacity available for sensitive workloads.
- No documented BYOC; data resides on Lambda's hardware.

### Storage

- Each instance includes local NVMe SSD (1 TiB on A100, 512 GiB-1 TiB depending on size).
- Lambda offers persistent network storage (Lambda Stack) for datasets, checkpoints, outputs that survives between sessions.
- No egress fees for outbound traffic.

### Free tier

No free tier; sign-up requires a credit card.

## Strengths

- No egress fees, which is unusual in the category and matters for high-throughput inference serving.
- Mature support for multi-node training and inference with InfiniBand.
- 1-Click Clusters remove the operational burden of standing up a distributed training/inference stack.

## Limitations

- No per-token serverless API; the customer is responsible for serving infrastructure.
- Pricing is less aggressive than Spheron or community clouds on bare-metal H100.
- Reserved capacity is the reliable tier; on-demand supply can be tight.
