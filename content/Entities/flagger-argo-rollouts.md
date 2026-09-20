---
title: "Flagger and Argo Rollouts"
details: "Kubernetes-native progressive delivery controllers — Flagger (Flux ecosystem) and Argo Rollouts (Argo ecosystem) — that orchestrate canary traffic shifting via service mesh or ingress, evaluate runtime SLO metrics, and trigger automatic rollback without a new deployment commit when thresholds are breached."
tags:
  - entity
  - tooling
  - infrastructure
created: 2026-09-19
updated: 2026-09-19
type: entity
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Flagger and Argo Rollouts

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Controller
**Repository:** https://github.com/fluxcd/flagger / https://github.com/argoproj/argo-rollouts
**Website:** https://flagger.app / https://argoproj.github.io/argo-rollouts

---

## Overview

Flagger and Argo Rollouts are the two leading Kubernetes-native progressive delivery controllers. Both implement the Canary / Blue-Green custom resources, integrate with service meshes (Istio, Linkerd) or ingress controllers (NGINX, Contour, Gloo), evaluate metrics from Prometheus or Datadog, and roll back automatically when SLO thresholds are breached.

## Key Details

- **Flagger:** Part of the Flux CD ecosystem; tighter integration with Flux for GitOps-driven delivery; the example canary resource in the article is Flagger.
- **Argo Rollouts:** Part of the Argo ecosystem; richer UI dashboard; first-class support for traffic-splitting analysis via the AnalysisTemplate CR.
- **Metric providers:** Prometheus, Datadog, New Relic, CloudWatch, Wavefront, Graphite, and custom webhook providers.
- **Rollback:** Pure routing decision — the bad version stays deployed, traffic shifts away, no new commit required.

## Related Concepts

- [[Concepts/progressive-delivery-controllers]] — Flagger and Argo Rollouts are the canonical implementations of the progressive-delivery pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8