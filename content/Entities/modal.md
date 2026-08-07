---
title: "Modal"

details: "Modal lets developers run any Python function on GPUs by decorating it with @app.function(gpu='H100'). The platform handles containerization, scheduling, autoscaling, and billing. Modal is widely used for inference, fine-tuning, batch jobs, and sandboxes."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entity
source: "https://modal.com/pricing"
---
# Modal

**Category:** Platform (developer-focused serverless GPU)

**Website:** [modal.com](https://modal.com/)
**Pricing page:** [modal.com/pricing](https://modal.com/pricing)
**Docs:** [modal.com/docs](https://modal.com/docs)

---

## Overview

Modal is a serverless cloud platform purpose-built for Python developers running ML workloads. The user experience is centered on a Python SDK: a function is decorated with `@app.function(gpu="H100")` and Modal handles the rest (container build, GPU scheduling, autoscaling, billing). Modal's Rust-based container stack can spin up GPUs in under one second, making cold starts effectively invisible for most workloads.

## Key Details

### Pricing (per-second GPU, July 2026)

| Resource | Rate | Source |
|---|---|---|
| CPU physical core | $0.00003942/core/sec | [modal.com/pricing](https://modal.com/pricing) |
| Memory | $0.00000667/GiB/sec | [modal.com/pricing](https://modal.com/pricing) |
| T4 | $0.000164/sec (~$0.59/hr) | [modal.com/pricing](https://modal.com/pricing) |
| A10G | $0.000306/sec (~$1.10/hr) | third-party aggregator |
| A100 40GB | $0.001036/sec (~$3.73/hr) | third-party aggregator |
| A100 80GB | $0.000694/sec (~$2.50/hr) | [modal.com/pricing](https://modal.com/pricing) |
| H100 | $0.002778/sec (~$10.00/hr list) | third-party aggregator |

Modal also publishes a marketing "serverless cloud" comparison: 75 GPUs x 24 hrs x $3/GPU = $5,400 (traditional) vs Modal at 50 GPUs avg x 24 hrs x $3.95/GPU = $4,740 ([modal.com/pricing](https://modal.com/pricing)).

### API and SDK

- Python-first; `@app.function()` decorator pattern.
- HTTP webhook endpoints via `@modal.web_endpoint()`.
- Scheduled jobs via `@modal.schedule()`.
- Sandboxes (ephemeral, stateful execution environments).
- Region selection (US East, US West, Europe, Asia).

## Provisioning

- **CLI:** `modal` (Python) — `modal deploy`, `modal run`, `modal serve`. Auth via `modal token new`. See [Modal CLI reference](https://modal.com/docs/reference/cli).
- **Terraform:** No first-party Terraform provider. Pulumi is a viable alternative because Pulumi can bridge any Terraform provider, but no Modal-specific Pulumi provider exists either. Customers who need IaC typically use the `modal` CLI in a CI pipeline.
- **API:** All CLI operations are also available via Modal's REST API and Python SDK.
- **Web UI:** Modal dashboard at [modal.com/apps](https://modal.com/apps) for app lifecycle, logs, metrics, function history.
- **GitHub:** Modal deploys are typically driven by `modal deploy` from a CI pipeline; documented in [Modal deployment docs](https://modal.com/docs/guide/managing-deployments).

### Cold starts

Sub-second container spin-up via the Rust runtime and memory snapshotting. The memory snapshot feature can reduce cold start times for qualifying workloads.

### Data privacy

- SOC 2 Type II compliant. HIPAA available on enterprise tier.
- Static IP proxy available (good for allow-listing).
- SSO, Okta, audit logs, RBAC on enterprise tier.
- No documented BYOC option on standard tiers; data resides in Modal's infrastructure.

### Storage

Modal Volumes provide persistent file storage mounted into containers (for datasets, model weights, outputs). Modal also supports S3/GCS integration via standard client libraries. S3-compatible blob storage is not included by default.

### Free tier

$30/month free compute on the Developer plan; $100/month on Team.

## Strengths

- Best-in-class developer experience for Python ML teams.
- Sub-second cold starts with memory snapshotting.
- Mature support for the full ML lifecycle (inference, fine-tuning, batch, sandboxes) on one platform.

## Limitations

- Python-only SDK; non-Python stacks are second-class.
- Effective H100 rate at sustained load (~$3.95/hr) is higher than bare-metal providers.
- Lock-in via the decorator pattern: Modal-annotated functions do not run outside the Modal runtime.
