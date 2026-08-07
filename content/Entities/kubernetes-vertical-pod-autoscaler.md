---
title: "Kubernetes Vertical Pod Autoscaler (VPA)"

details: "A Kubernetes controller in the autoscaler family that observes historical and current resource usage and automatically updates pod `resources.requests` (and optionally `limits`) to match demand. Three components: recommender (analyzes history), updater (mutates pod specs), admission controller (applies changes to live pods). Relevant to right-sizing: for workloads with a 10-minute daily spike, VPA reduces annual over-allocation from 99.96% to near-zero by scaling down during idle periods. VPA cannot be combined with Horizontal Pod Autoscaler (HPA) on the same resource dimension; teams typically use HPA for CPU and VPA for memory, or use VPA in recommendation-only mode and apply changes via a separate process."
tags:
  - entities
  - kubernetes
  - infrastructure
created: 2026-07-25
updated: 2026-07-25
type: entity
source: "[[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]]"
---

# Kubernetes Vertical Pod Autoscaler (VPA)

**Source:** Alina Trofimova, DEV.to ([[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]])
**Category:** Tool / Kubernetes Controller
**Repository:** https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler
**Website:** https://github.com/kubernetes/autoscaler

## Overview

A Kubernetes controller that observes historical and current resource usage and automatically updates pod `resources.requests` (and optionally `limits`) to match demand. In the source article, VPA is the recommended automated mitigation for two of the six over-provisioning patterns: transient-load peak sizing and data-deficient initial provisioning.

## Key Details

### Components

- **Recommender:** Watches pod metrics, builds per-container usage distributions, and produces a recommended `requests` value.
- **Updater:** Identifies pods whose requests diverge from the recommendation and evicts them so the new requests can take effect (pod restart is required because `requests` is an immutable field on a running pod).
- **Admission Controller:** Intercepts pod creation and rewrites requests to match the recommendation at admission time, avoiding the need for an evict/restart cycle.

### Three Operating Modes

| Mode | Behavior |
|---|---|
| `Off` | Recommender runs but no changes are applied; useful for previewing recommendations |
| `Initial` | Recommendations are applied only at pod creation; live pods are not touched |
| `Auto` | Both admission-time rewriting and live-pod eviction |

### Quantitative Impact (per the source)

For a workload with a 10-minute daily spike provisioned at peak capacity, the source claims VPA reduces annual over-allocation from **99.96% to near-zero** by scaling requests down during idle periods and back up during the spike. This is the single highest-leverage intervention for the transient-load pattern.

### Known Constraints

- **VPA and HPA cannot be combined on the same resource dimension.** If VPA manages CPU requests, HPA cannot also use CPU utilization to drive replica count.
- **Pod restart required.** `requests` is immutable, so any change to a running pod's request value requires a restart. This is generally acceptable for stateless services but disruptive for stateful or long-running workloads.
- **Recommendation lag.** The recommender needs historical data (typically 8 days minimum), so a freshly-deployed workload will not get accurate recommendations immediately. This makes VPA a complement to, not a replacement for, the post-deployment audit.

## Related Concepts

- [[Concepts/k8s-over-provisioning-patterns]] — Patterns 2 (transient load) and 5 (data-deficient initial provisioning) are the primary targets
- [[Concepts/k8s-resource-feedback-loop-discipline]] — VPA is the automated right-sizing arm of the broader feedback-loop discipline

## References

- Raw Article: [[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]]
- Original: https://dev.to/alitron/improving-kubernetes-resource-efficiency-with-automated-feedback-loops-to-reduce-over-provisioning-2kba
- Project: https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler
