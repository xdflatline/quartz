---
title: "Serverless GPU data privacy patterns"
detail: "Reference for the data-residency, BYOC, isolation, and compliance patterns used by serverless GPU providers."
details: "Serverless GPU providers offer different combinations of (a) data residency / region selection, (b) BYOC / VPC peering, (c) workload isolation (shared vs single-tenant), and (d) compliance certifications (SOC 2, ISO 27001, HIPAA, GDPR). Choosing a provider for a regulated workload requires checking all four."
tags:
  - concepts
created: 2026-07-24
updated: 2026-07-24
type: concept
source: "https://modal.com/docs/guide/security"
---
# Serverless GPU Data Privacy Patterns

Serverless GPU providers offer different combinations of (a) data residency / region selection, (b) BYOC / VPC peering, (c) workload isolation (shared vs single-tenant), and (d) compliance certifications (SOC 2, ISO 27001, HIPAA, GDPR). Choosing a provider for a regulated workload requires checking all four.

## Pattern 1: Public Multi-Tenant

**Examples:** Replicate public models, DeepInfra serverless, Together serverless, Fireworks serverless, Fal.ai Model API

- Hardware is shared across customers.
- Customer data is in flight to the GPU during inference only.
- Models are loaded from a shared registry; weights are not customer-owned.
- No data residency guarantees (region pinning is best-effort).
- SOC 2 typical; HIPAA rare; no BYOC.

**Best for:** Prototyping, public-data workloads, spiky traffic.

## Pattern 2: Public Single-Tenant (Dedicated)

**Examples:** Hugging Face Inference Endpoints, Baseten Dedicated, Together Dedicated, Fireworks On-Demand, RunPod Serverless, Modal Functions, Beam Tasks, Cerebrium, Replicate private deployments

- One customer's workload runs on dedicated hardware, but the hardware is still owned and operated by the provider.
- Region selection is usually supported.
- No BYOC, but workload isolation is real.
- SOC 2 and HIPAA commonly available; BAA on enterprise tier.
- Data at rest is not customer-managed (provider-owned ephemeral disk).

**Best for:** Production inference on custom models, latency-sensitive workloads, compliance-sensitive workloads without strict data-residency requirements.

## Pattern 3: BYOC (Compute in Customer's Cloud)

**Examples:** Beam (BYOC), Baseten (self-hosted), Anyscale (BYOC), Hugging Face Enterprise Hub, Fireworks Enterprise Reserved, Modal Enterprise Reserved

- The provider orchestrates compute inside the customer's own AWS / GCP / Azure account.
- Customer's existing GPU reservations, committed-use discounts, and egress allowances can be used.
- Data never leaves the customer's VPC.
- Highest compliance bar; often the only path for healthcare, financial services, and government workloads.

**Best for:** Regulated workloads, customers with existing cloud commitments, data that must stay in a specific region or VPC.

## Pattern 4: Decentralized / Permissionless

**Examples:** Akash Network

- Compute is provided by independent operators in many countries.
- No KYC; deployments are pseudonymous.
- Data residency is by provider, not by region.
- No SOC 2 / HIPAA in the traditional sense.
- Censorship resistance is the design goal, not regulatory compliance.

**Best for:** Censorship-resistant deployments, cost-first workloads, workloads where regulatory compliance is not a requirement.

## Compliance Certification Matrix (July 2026)

| Provider | SOC 2 | HIPAA | ISO 27001 | GDPR | BYOC | Region selection |
|---|---|---|---|---|---|---|
| Modal | Yes (Type II) | Yes (enterprise) | Yes | Yes | No | Yes |
| Replicate | Yes | No (no documented BAA) | Yes | Yes | No | No (best-effort) |
| RunPod | Yes (Type II) | Yes (enterprise) | Yes | Yes | No | Yes |
| Together AI | Yes (Type II) | Yes (enterprise) | Yes | Yes | No | Yes |
| Fireworks AI | Yes (Type II) | Yes (enterprise) | Yes | Yes | Yes (Reserved) | Yes |
| Hugging Face Endpoints | Yes (Type II) | Yes (enterprise) | Yes | Yes | Yes (Enterprise Hub) | Yes (AWS/GCP/Azure) |
| Fal.ai | Yes (SOC 2) | No (no documented BAA) | No | Yes | No | No |
| Baseten | Yes (Type II) | Yes | Yes | Yes | Yes (self-hosted) | Yes |
| Beam | Yes (enterprise) | Yes (enterprise) | Yes | Yes | Yes | Yes |
| Cerebrium | Yes (enterprise) | Yes (enterprise) | Yes | Yes | No | Yes (multi-region) |
| Anyscale | Yes (Type II) | Yes (enterprise) | Yes | Yes | Yes | Yes |
| DeepInfra | Yes | Yes | Yes | Yes | No | No |
| Lambda | Yes (Type II) | Yes (enterprise) | Yes | Yes | No | No |
| Akash | No (no BAA) | No (no BAA) | No | No | No | No (by provider) |

This matrix is approximate. Verify with the provider's current compliance documentation before relying on it for procurement.

## Practical Selection

- **Public-data LLM serving:** DeepInfra, Together, Fireworks serverless.
- **Custom-model production inference:** Modal, Beam, Baseten, RunPod Serverless, Cerebrium.
- **Latency-critical with custom models:** HF Endpoints, Baseten Dedicated, RunPod Serverless.
- **Regulated healthcare / finance:** HF Endpoints, Baseten self-hosted, Anyscale BYOC, Modal enterprise, Fireworks Reserved.
- **Censorship-resistant / cost-first:** Akash.
- **Egress-sensitive:** Lambda (no egress fees), Beam (free egress to customer cloud in BYOC).
