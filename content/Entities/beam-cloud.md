---
title: "Beam Cloud"

details: "Beam (formerly Slai) is a serverless GPU platform for Python. It supports GPU Tasks, scheduled jobs, web endpoints with autoscaling, persistent volume mounts, and a dedicated Sandboxes product for untrusted-code execution. Beam also offers a Bring-Your-Own-Cloud product for running on AWS or GCP accounts."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://www.beam.cloud/pricing"
---
# Beam Cloud

**Category:** Platform (serverless GPU + sandboxes)

**Website:** [beam.cloud](https://www.beam.cloud/)
**Pricing page:** [beam.cloud/pricing](https://www.beam.cloud/pricing)
**Docs:** [docs.beam.cloud](https://docs.beam.cloud/)

---

## Overview

Beam Cloud is a serverless GPU platform built for Python workloads. It exposes four product surfaces: Serverless GPU Tasks (autoscaled functions), On-Demand (bare-metal or VM machines billed per hour), Sandboxes (ephemeral isolated code-execution environments), and Bring-Your-Own-Cloud (run Beam-managed compute on your own AWS/GCP account). Beam is known for memory-snapshotting fast cold starts, persistent volume mounts, and a self-hosted option for fully in-VPC execution.

## Key Details

### Pricing (Serverless, per-millisecond, July 2026)

| GPU | VRAM | Rate | Source |
|---|---|---|---|
| RTX 4090 PCIe | 24 GB | $0.000191667/sec (~$0.69/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| A6000 PCIe | 48 GB | $0.000227778/sec (~$0.82/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| RTX 5090 PCIe | 32 GB | $0.000303/sec (~$1.09/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| L40S PCIe | 48 GB | $0.000486/sec (~$1.75/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| A100 80GB SXM4 | 80 GB | $0.000625/sec (~$2.25/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| RTX PRO 6000 PCIe | 96 GB | $0.000758/sec (~$2.73/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| H100 PCIe | 80 GB | $0.000986/sec (~$3.55/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| H200 SXM5 | 141 GB | $0.001136/sec (~$4.09/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |
| B200 SXM6 | 180 GB | $0.001561/sec (~$5.62/hr) | [beam.cloud/pricing](https://www.beam.cloud/pricing) |

### On-Demand machines (per hour)

B200 from $3.93/hr, H200 from $1.99/hr, H100 from $1.74/hr, A100 from $1.30/hr. Full list at [beam.cloud/pricing](https://www.beam.cloud/pricing).

### CPU and memory (per millisecond)

Physical core (2 vCPU equivalent): $0.0000125/core/sec. RAM: $0.0000021/GiB/sec.

### API and SDK

- Python SDK (`beam-sdk`).
- HTTP endpoints via `@beam.rest_api()`.
- Scheduled/cron jobs.
- Persistent volume mounts.
- Multiple workers per container (vertical scaling).
- Docker-in-Docker support.

## Provisioning

- **CLI:** `beam` (Python) — `beam deploy app.py:handler --name inference-app`, `beam deployment list`, `beam deployment stop <id>`, `beam volume list --context dev`. Contexts (`--context staging`) let you maintain multiple environments. See [Beam CLI reference](https://docs.beam.cloud/v2/reference/cli).
- **Terraform:** No first-party Beam Terraform provider as of July 2026. Customers typically drive deployments via the `beam` CLI in CI; some use the Beam REST API behind a Terraform `external` data source or a community provider.
- **API:** REST API for deployments, tasks, volumes, secrets, scheduling.
- **Web UI:** Beam dashboard for app lifecycle, logs, metrics.
- **GitHub Actions:** Common pattern is `beam deploy` in CI; Beam supports deployment from GitHub Actions as documented on the [Beam homepage](https://www.beam.cloud/).
- **CLI examples:** `beam deploy create app.py:handler --name inference-app`, `beam task list -c production`.

### Cold starts

Fast cold starts via memory snapshotting and GPU checkpoint restore; cold starts are typically low-hundreds-of-milliseconds for smaller models.

### Data privacy

- Workloads run in non-root isolated containers.
- Self-hosted Beam product runs entirely inside the customer's VPC.
- No documented SOC 2 / HIPAA on the public docs but enterprise plans include compliance support.
- Free egress between Beam and customer cloud accounts in the BYOC product.

### Storage

Persistent volume mounts are a first-class concept; weights and data can be pre-loaded into a volume and mounted into multiple tasks. S3/GCS via standard clients.

### Free tier

$30 free credit refreshed monthly on sign-up.

## Strengths

- Persistent volume mounts are rare in the serverless GPU category and matter for models that cannot fit in container layers.
- BYOC product is well-developed: AWS or GCP account with Beam's management fees on top.
- Memory-snapshotting cold start is fast.
- Sandboxes product is a separate, well-supported path for untrusted-code execution.

## Limitations

- Smaller GPU catalog than RunPod (no B300 yet).
- Python-only SDK.
- Lower brand awareness than Modal or Replicate.
