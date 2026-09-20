---
title: "Research Index: Systems for Modern Architecture"
details: "Synthesis of ten categories of developer tooling that operate across distributed runtime boundaries — distributed tracing, contract testing, repository intelligence, eBPF infrastructure debugging, database observability, FinOps, supply-chain security, load testing, progressive delivery, and AI-agent sandboxes — with their canonical implementations and the patterns they express."
tags:
  - research
  - architecture-pattern
  - tooling
created: 2026-09-19
updated: 2026-09-19
type: research
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Research Index: Systems for Modern Architecture

**Updated:** 2026-09-19
**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]

---

## Overview

The central claim of this research thread is that modern software architectures — microservices, distributed event brokers, autonomous AI agents, multi-region deployments — produce failure modes that local IDEs structurally cannot observe. The IDE is bound to a single process and a single memory allocation space; it has no representation of a request that has hopped across five services, a lock that is contended across nodes, or an image that was admitted to a cluster without provenance.

The ten tooling categories surveyed in [[Raw/devto-systems-for-modern-architectures-2026-09-19]] are not ten independent products — they are ten observation planes that together cover the failure modes a distributed system can exhibit. The research pages that follow organize them by what they observe and where the architectural boundary lies.

## Concepts

### Request-Flow Plane

- [[Concepts/distributed-tracing-fabrics]] — Reconstructs the end-to-end request DAG across RPC and messaging boundaries via the W3C `traceparent` context.
- [[Concepts/progressive-delivery-controllers]] — Shifts traffic incrementally and rolls back automatically when SLO thresholds are breached.

### Build-Time Verification Plane

- [[Concepts/consumer-driven-api-contract-testing]] — Verifies provider behavior against consumer-published contracts at CI time.
- [[Concepts/software-supply-chain-provenance-sboms]] — Verifies artifact identity and dependency graph at admission time via signed SBOMs and SLSA provenance.

### Host / Kernel Plane

- [[Concepts/infrastructure-debugging-with-ebpf]] — Observes kernel-level events (drops, DNS latency, cgroup throttling) without application instrumentation.
- [[Concepts/database-observability-platforms]] — Observes storage-engine internals (lock waits, connection pool saturation, plan regressions) that mock databases hide.

### Code-Intelligence Plane

- [[Concepts/cross-repo-semantic-code-graphs]] — Persists out-of-core semantic code graphs for cross-repository search and migration tracking.

### Cost / Capacity Plane

- [[Concepts/cloud-cost-engineering-finops]] — Attributes cloud spend back to PRs and pod specs to surface idle capacity before merge.
- [[Concepts/distributed-load-testing-traffic-simulation]] — Generates multi-zone concurrent workloads to expose concurrency-bound failure modes.

### AI Agent Plane

- [[Concepts/sandboxed-execution-for-ai-agents]] — Provides microVM-isolated execution sandboxes for LLM-generated code, with evaluation harnesses for non-deterministic behavior.

## Tools & Projects

### Open-Source Tracing

- [[Entities/opentelemetry]] — Vendor-neutral instrumentation framework and OTLP wire protocol.
- [[Entities/jaeger-tempo]] — Open-source tracing backends for span storage and DAG reconstruction.

### Contracts and Code Intelligence

- [[Entities/pact]] — Consumer-driven contract testing framework.
- [[Entities/sourcegraph-scip-lsif]] — Binary index formats for cross-repo semantic code graphs.

### Kernel and Cluster Debug

- [[Entities/cilium-ebpf]] — eBPF-based Kubernetes networking and observability.

### Cost and Security

- [[Entities/opencost-kubecost]] — Kubernetes cost allocation platforms.
- [[Entities/sigstore-cosign]] — Cryptographic signing stack for supply-chain integrity.

### Delivery and Load

- [[Entities/k6-locust]] — Open-source load-testing tools.
- [[Entities/flagger-argo-rollouts]] — Kubernetes-native progressive delivery controllers.

### AI Sandbox Runtime

- [[Entities/firecracker-microvm]] — AWS-developed VMM for lightweight microVM isolation.

## Raw Sources

- [[Raw/devto-systems-for-modern-architectures-2026-09-19]] — The article that frames the ten categories.

## Cross-Cutting Themes

### The IDE's Architectural Boundary

The single observation that unifies all ten categories is that the IDE is constrained to a single process and a single memory allocation space. Every category listed above addresses a failure mode that lives *outside* that boundary:

- Tracing addresses request flow that has crossed network hops.
- Contracts address behavior that lives in another team's release cycle.
- Repository intelligence addresses symbols that live in another repository.
- eBPF addresses kernel events the IDE debugger cannot attach to.
- Database observability addresses engine state that mock tests cannot reproduce.
- FinOps addresses spend that is invisible until the cloud bill arrives.
- Supply-chain security addresses identity that the build pipeline is not the only source of.
- Load testing addresses concurrency that a single-threaded test cannot express.
- Progressive delivery addresses release decisions that the IDE cannot represent.
- AI agent sandboxes address code that the model itself produced.

### Verification Planes Have Build-Time and Runtime Faces

Build-time verification (contracts, supply-chain) gates the artifact before it reaches the cluster. Runtime verification (tracing, eBPF, database observability, progressive delivery) observes the artifact in motion. FinOps straddles both — cost attribution is build-time, cost anomaly detection is runtime. Load testing is the bridge: it produces the workload that the runtime verification surfaces then observe.

### Canonical Implementations Cluster Around Two Ecosystems Per Category

Every category has at least two strong open-source reference implementations:

| Category | Canonical pair |
| --- | --- |
| Tracing | OpenTelemetry + Jaeger/Tempo |
| Contracts | Pact + Pact Broker |
| Code intelligence | Sourcegraph + SCIP/LSIF |
| eBPF | Cilium + Inspektor Gadget |
| FinOps | OpenCost + Kubecost |
| Supply-chain | Sigstore + Cosign/Rekor |
| Load testing | k6 + Locust |
| Progressive delivery | Flagger + Argo Rollouts |
| AI sandbox | Firecracker + gVisor |

The clustering is not accidental: each pair covers complementary trade-offs (e.g., Jaeger's self-contained UI vs. Tempo's cheap object-store retention; Pact's open-source broker vs. PactFlow's hosted SaaS).

## Next Research Directions

- [ ] **Prototype a minimal four-plane stack** — OpenTelemetry collector + Pact broker + Sigstore admission controller + Flagger canary on a single Kubernetes cluster, to verify the integration patterns documented in the article's appendix manifests.
- [ ] **Compare head-based vs. tail-based sampling cost** — quantify the cost differential and the p99-detection-latency tradeoff using a synthetic 10-service mesh.
- [ ] **Evaluate Firecracker vs. gVisor for an AI agent sandbox** — measure cold-start latency, memory overhead, and syscall-blocking surface across a representative agent workload (shell + HTTP + file edit).
- [ ] **Map the Flagger analysis metrics back to OpenTelemetry trace attributes** — verify that the SLO signals the controller evaluates are correctly derived from the trace pipeline, not from a separate metric store.
- [ ] **Reproduce the article's TCO worked example** with internal incident data to validate whether the claimed $65k/year saving on a 24-incident, 4-engineer, $115/hr organization holds for our scale.