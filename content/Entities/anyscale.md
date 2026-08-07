---
title: "Anyscale"

details: "Anyscale is a managed platform for running Ray-based distributed AI workloads at production scale. It supports both hosted (Anyscale-managed) and Bring-Your-Own-Cloud (BYOC) deployment models, with rack-aware GPU scheduling and NVIDIA cuDF support on Ray Data. Customers include Handshake, Canva, Attentive, and Coactive AI."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://www.anyscale.com/pricing"
---
# Anyscale

**Category:** Platform (managed Ray / distributed AI)

**Website:** [anyscale.com](https://www.anyscale.com/)
**Pricing page:** [anyscale.com/pricing](https://www.anyscale.com/pricing)
**Docs:** [docs.anyscale.com](https://docs.anyscale.com/)

---

## Overview

Anyscale is the commercial platform from the creators of Ray. It provides a managed environment for running distributed training, fine-tuning, batch inference, and online inference workloads on a pool of pooled GPUs. Anyscale offers two deployment models: Hosted (Anyscale-managed compute) and Bring-Your-Own-Cloud (run inside the customer's AWS / Azure / GCP account using existing GPU reservations).

## Key Details

### Pricing (Hosted, Anyscale Compute Units, July 2026)

Instance hourly rates in Anyscale Compute (AC) units (1 AC ≈ $1 base rate, varies by tier):

| Hardware | Rate | Source |
|---|---|---|
| CPU | AC 0.0135/hr | [anyscale.com/pricing](https://www.anyscale.com/pricing) |
| NVIDIA T4 | AC 0.5682/hr | [anyscale.com/pricing](https://www.anyscale.com/pricing) |
| NVIDIA L4 | AC 0.9542/hr | [anyscale.com/pricing](https://www.anyscale.com/pricing) |
| NVIDIA A10G | AC 1.3635/hr | [anyscale.com/pricing](https://www.anyscale.com/pricing) |
| NVIDIA A100 | AC 4.9591/hr | [anyscale.com/pricing](https://www.anyscale.com/pricing) |
| NVIDIA H/B/GB families | custom | [anyscale.com/pricing](https://www.anyscale.com/pricing) |

### Billing model

Usage-based, pay-as-you-go on Hosted. BYOC billed via Anyscale invoice or cloud marketplace (AWS / Azure / GCP), with the customer using existing cloud credits and GPU reservations.

### API and SDK

- Ray-native APIs (Ray Train, Ray Serve, Ray Data).
- Anyscale Jobs (cron-based recurring jobs).
- Anyscale Services (online inference with autoscaling).
- Python SDK + dashboard.
- Templates for common patterns (LLM fine-tuning, batch inference, VLA fine-tuning).

## Provisioning

- **CLI:** `anyscale` (Python) — `anyscale login`, `anyscale job submit`, `anyscale service deploy`. Auth via Anyscale Cloud or BYOC cluster.
- **Terraform:** No first-party Anyscale Terraform provider. Community reference architectures exist (e.g., [AKS-Anyscale-Private-Cluster-Sample](https://github.com/KenKilty/AKS-Anyscale-Private-Cluster-Sample) for Azure AKS, and the [anyscale/terraform-kubernetes-anyscale-foundation-modules](https://tessl.io/registry/skills/github/anyscale/terraform-kubernetes-anyscale-foundation-modules/deploy-gcp-gke) for GCP GKE) that provision the underlying K8s cluster and Anyscale control plane together.
- **API:** REST API for jobs, services, clusters, workspaces, billing.
- **Web UI:** Anyscale console for workspace, jobs, services, cluster ops.
- **CloudFormation / Helm:** Anyscale ships Helm charts and CloudFormation templates for BYOC deployments (AWS, Azure, GCP).
- **CLI examples:** `anyscale job submit --config config.yaml`, `anyscale service deploy my-service/`.

### Cold starts

No platform-induced cold starts on Anyscale Services; replicas stay warm. Anyscale Jobs have a brief cluster spin-up.

### Data privacy

- SOC 2 Type II compliant.
- HIPAA support on enterprise.
- BYOC deployment means compute and data never leave the customer's cloud.
- Rack-aware scheduling to maximize intra-rack bandwidth and reduce cross-rack data movement for sensitive workloads.

### Storage

Ray-native object store (compatible with S3). Volumes mounted into Anyscale Services. BYOC uses the customer's existing cloud storage.

### Free tier

$5 in credits to launch a project (template-based). No permanent free tier.

## Strengths

- BYOC is mature: Anyscale orchestrates Ray on the customer's cloud account, which is rare in the category and important for regulated workloads.
- Rack-aware GPU scheduling is a genuine differentiator for multi-rack training/inference.
- Ray-native API gives access to the full Ray ecosystem (Train, Serve, Data, RLlib).
- Strong fit for compound AI workloads that mix CPU preprocessing, GPU inference, and multi-step reasoning.

## Limitations

- Ray learning curve: not as simple to get started as Modal or Replicate.
- AC pricing is opaque relative to per-GPU-hour rates on RunPod or Lambda.
- Anyscale is the most expensive option for simple single-model inference; the value comes from distributed and compound workloads.
