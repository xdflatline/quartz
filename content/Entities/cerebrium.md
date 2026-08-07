---
title: "Cerebrium"

details: "Cerebrium is a serverless AI infrastructure platform designed for production inference, real-time AI, batch jobs, and voice AI. It supports 10+ GPU types, multi-region deployments, and a highly-available distributed router (Thalamus) for global real-time AI workloads. Brings-your-own-Dockerfile approach with no proprietary SDK or decorator required."
tags:
  - entities
  - serverless
  - inference
created: 2026-07-24
updated: 2026-07-24
type: entity
source: "https://cerebrium.ai/blog/2026-gpu-buyers-guide"
---
# Cerebrium

**Category:** Platform (serverless GPU for real-time AI)

**Website:** [cerebrium.ai](https://cerebrium.ai/)
**Pricing page:** [cerebrium.ai/pricing](https://cerebrium.ai/pricing)
**Docs:** [docs.cerebrium.ai](https://docs.cerebrium.ai/)

---

## Overview

Cerebrium is a serverless AI infrastructure platform focused on production inference and real-time AI. Unlike Modal (Python decorator) or Replicate (Cog container), Cerebrium accepts any Dockerfile as input and runs it as is, without rewrites or proprietary SDKs. It pairs per-second billing with a distributed router (Thalamus) for global low-latency deployment, and supports multi-region deployment as a first-class feature.

## Key Details

### Pricing (per-second, July 2026)

Cerebrium bills GPU, CPU, and memory as separate line items. Cold-start container spin-up is not billed. Specific rates vary by GPU class; the [pricing page](https://cerebrium.ai/pricing) lists per-second rates across 10+ GPU tiers (entry-level to H100/H200).

### API and SDK

- Bring-your-own-Dockerfile: point to a Dockerfile, Cerebrium builds and deploys.
- No proprietary SDK or decorator.
- WebSocket support for streaming and real-time workloads.
- Batching support built in.
- Bring-your-own ASGI app (Gradio, Streamlit, FastAPI) supported.

## Provisioning

- **CLI:** No first-party dedicated CLI as of July 2026. Cerebrium ships a `cerebrium` Python package and supports deployment via the `cerebrium deploy` workflow that points to a Dockerfile. The REST API is the primary provisioning surface.
- **Terraform:** No first-party Cerebrium Terraform provider. Customers typically drive deployments via the REST API in CI.
- **API:** REST API for deployment, scaling, real-time routing (Thalamus), secrets, volumes.
- **Web UI:** Cerebrium dashboard at [dashboard.cerebrium.ai](https://dashboard.cerebrium.ai/) for deployment config, multi-region setup, monitoring.
- **GitHub Actions:** Common pattern is `cerebrium deploy` from CI pointing to a Dockerfile in the repo.
- **Bring your own:** Dockerfiles, ASGI apps, and custom images are all first-class inputs.

### Cold starts

Build times 8-14 seconds. Cold start container spin-up not billed. Memory and GPU snapshotting can reduce warm-start time for supported models.

### Data privacy

- Multi-region deployment lets you pin data and inference to a specific geography.
- TLS by default.
- Enterprise plans include SOC 2, HIPAA, and BAA support.
- No documented BYOC; data resides in Cerebrium's regions.

### Storage

Persistent storage via volume mounts for weights and data. S3/GCS via standard clients from the runtime.

### Free tier

Hobby tier starts at no base cost with usage-based billing. Volume discounts on enterprise.

## Strengths

- No proprietary SDK lock-in: bring a Dockerfile.
- Multi-region deployment with the Thalamus distributed router is a differentiator for global real-time AI.
- Fast cold starts via memory snapshotting; cold-start container spin-up is not billed.
- Transparent billing (GPU, CPU, memory as separate line items).

## Limitations

- Smaller brand than Modal or RunPod.
- GPU catalog is broad but not as deep as RunPod's (which extends to B300).
- Multi-region deployment requires careful replication strategy; default single-region may surprise users.
