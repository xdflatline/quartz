---
title: "Akash Network"

details: "Akash Network is a decentralized cloud computing marketplace built on the Cosmos SDK. It operates as an open, permissionless network where independent providers compete to offer high-performance compute and GPU resources, including for ML inference workloads."
tags:
  - entities
created: 2026-06-05
updated: 2026-07-24
type: entitie
---
# Akash Network

**Akash Network** is a decentralized cloud computing marketplace built on the Cosmos SDK. It operates as an open, permissionless network where independent providers compete to offer high-performance compute and GPU resources. Akash can host any Docker-containerized workload, making it a viable substrate for ML inference (vLLM, TGI, SGLang, ComfyUI) deployed via reverse auction.

## Core Capabilities

1. **Decentralized Marketplace**: Independent providers across 85+ countries compete to host workloads. No single entity controls the network.
2. **Reverse Auction Model**: Users define requirements in SDL (Stack Definition Language) YAML; providers bid; user selects the best offer.
3. **Significant Cost Savings**: Competitive bidding pushes workloads to ~85% lower cost than centralized hyperscalers.
4. **Censorship Resistance**: Permissionless deployment; no single entity can shut down a deployment.
5. **Universal Workload Support**: Any Docker container can run, including LLM inference servers and image generation pipelines.
6. **Flexible Payment**: Per-block streaming payments in AKT or USDC; no KYC.

## GPU Pricing (reverse auction, July 2026)

Akash pricing is set by reverse auction, not a fixed rate card. Typical ranges from the [Akash GPU Deployments documentation](https://akash.network/docs/learn/core-concepts/gpu-deployments/):

| GPU | Akash typical range | Source |
|---|---|---|
| RTX 4090 (24GB) | $0.50-$1.50/hr | [akash.network/docs](https://akash.network/docs/learn/core-concepts/gpu-deployments/) |
| A100 40GB | $1.50-$2.50/hr | [akash.network/docs](https://akash.network/docs/learn/core-concepts/gpu-deployments/) |
| A100 80GB | $2.50-$3.50/hr | [akash.network/docs](https://akash.network/docs/learn/core-concepts/gpu-deployments/) |
| H100 | $2.50-$4.00/hr | [akash.network/docs](https://akash.network/docs/learn/core-concepts/gpu-deployments/) |

GMI and io.net comparisons report comparable ranges ($2.50-$3.50/hr A100 80GB). Final price depends on provider bids, lease length, and resource commitment.

## Inference Workflow

1. **Define SDL**: Write a YAML file describing the GPU workload (image, exposed ports, resources, price ceiling).
2. **Bid**: Providers on the network submit competing bids.
3. **Accept**: User selects a bid.
4. **Run**: Container starts; payments stream per block.
5. **Inference**: Run vLLM, TGI, ComfyUI, or any custom Docker image.

Example SDL for a GPU workload (from the Akash docs):

```yaml
version: "2.0"
services:
  gpu-app:
    image: nvidia/cuda:12.0.0-runtime-ubuntu22.04
    expose:
      - port: 8080
        as: 80
        to:
          - global: true
profiles:
  compute:
    gpu-app:
      resources:
        cpu:
          units: 4.0
        memory:
          size: 16Gi
        storage:
          size: 100Gi
        gpu:
          units: 1
          attributes:
            vendor:
              nvidia:
  placement:
    akash:
      pricing:
        gpu-app:
          denom: uact
          amount: 100000
deployment:
  gpu-app:
    akash:
      profile: gpu-app
      count: 1
```

## API and Tooling

- `akash` CLI for deployment lifecycle.
- HTTP lease API for bid selection and lease management.
- Akash Console (web UI) for visual deployment.
- Provider tooling (`akash provider`) for running a node.

## Provisioning

- **CLI:** `akash` (deployment) and `provider-services` (provider operations) — see [Akash CLI docs](https://akash.network/docs/developers/deployment/cli/).
- **Terraform:** First-party provider at [registry.terraform.io/providers/akash-network/akash](https://registry.terraform.io/providers/akash-network/akash/latest/docs); also [akash-network/terraform-provider-akash on GitHub](https://github.com/akash-network/terraform-provider-akash).
- **API:** REST lease/bid API for programmatic deployment.
- **Web UI:** Akash Console at [console.akash.network](https://console.akash.network/) — 1-click templates, deployment status, custom SDLs.
- **Helm / Kubernetes:** No first-party Helm chart, but you can deploy an inference server in the SDL and expose ports for external Kubernetes ingress.

## Cold starts

No platform-induced cold starts once the lease is accepted and the container is running. Lease creation and container boot typically 5-30 minutes depending on bid acceptance and provider provisioning speed.

## Data privacy

- **No KYC**: deployments are permissionless and pseudonymous (wallet address).
- **Decentralized**: no single entity can access, inspect, or shut down a deployment.
- **Data residency**: workloads run on whichever provider wins the auction, which can be in any of 85+ countries. This is a feature for censorship resistance but a consideration for regulated workloads.
- **SOC 2 / HIPAA**: not applicable in the traditional sense. Akash is not designed for regulated-workload compliance; it is designed for resilience and cost.

## Storage

- Persistent volumes attached to deployments.
- IPFS integration for content-addressed data.
- Akash does not bundle S3-compatible blob storage; customers typically attach their own.

## Payment

- AKT (native token) or USDC.
- Escrow-based: deposit funds, deployment streams payments per block.

## Strengths

- Lowest published GPU rates in the category (especially consumer GPUs and idle data-center capacity).
- Censorship resistance: no single entity can shut down a deployment.
- Universal Docker container support.
- No KYC.

## Limitations

- Reverse auction is operationally heavier than a per-second API.
- Lease creation and provider provisioning is slow (5-30 minutes) compared to serverless scale-up.
- Data residency is by provider, not by region, which complicates regulated workloads.
- No first-party inference engine or model registry (must run vLLM/TGI/ComfyUI yourself).
- No managed SOC 2 / HIPAA tier.

## Resources

- [Official Documentation](https://akash.network/docs/)
- [GPU Deployments Guide](https://akash.network/docs/learn/core-concepts/gpu-deployments/)
- [Akash Console](https://console.akash.network/)
