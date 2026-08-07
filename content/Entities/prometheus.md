---
title: "Prometheus"

details: "An open-source monitoring system with a dimensional data model, pull-based collection, and a powerful query language (PromQL). The de facto standard for Kubernetes cluster metrics. In the source article, Prometheus is the substrate for the post-deployment audit: comparing 30-day P95 CPU and memory usage against declared `resources.requests` requires exactly the kind of historical aggregation Prometheus provides via `histogram_quantile` and recording rules. Most managed Kubernetes distributions ship with Prometheus or a compatible alternative, and `kube-state-metrics` exposes the pod-level resource spec for direct comparison against actual usage."
tags:
  - entities
  - infrastructure
  - kubernetes
created: 2026-07-25
updated: 2026-07-25
type: entity
source: "[[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]]"
---

# Prometheus

**Source:** Alina Trofimova, DEV.to ([[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]])
**Category:** Tool / Observability Platform
**Repository:** https://github.com/prometheus/prometheus
**Website:** https://prometheus.io

## Overview

An open-source monitoring system and time-series database with a dimensional data model, pull-based collection, and a query language (PromQL). In the source article, Prometheus is the substrate for the post-deployment audit: comparing 30-day P95 CPU and memory usage against declared `resources.requests` requires exactly the kind of historical aggregation Prometheus provides.

## Key Details

### Why It Appears in the Source

The post-deployment audit pattern depends on two capabilities:

1. **Per-pod resource usage history.** Prometheus scrapes `cAdvisor`-exposed container metrics on every kubelet, retaining them per its `--storage.tsdb.retention.time` (commonly 15-30 days).
2. **Per-pod declared resource spec.** Exposed by `kube-state-metrics` as `kube_pod_container_resource_requests` and similar metrics, joined to actual usage on the pod label.

A representative audit query:

```promql
# Per-pod, per-container: ratio of P95 usage to requested CPU
sum by (namespace, pod, container) (
  rate(container_cpu_usage_seconds_total[5m])
)
/
sum by (namespace, pod, container) (
  kube_pod_container_resource_requests{resource="cpu"}
)
```

A ratio below ~0.3 across the P95 window indicates 70%+ slack capacity on that pod's CPU.

### Strengths for the Audit Use Case

- **Pull model fits Kubernetes.** The kubelet exposes cAdvisor metrics on a stable path; Prometheus discovers pods via service discovery.
- **Recording rules** pre-compute the per-pod P95 ratio daily, making the audit a dashboard query rather than a real-time scrape.
- **AlertManager** can fire when the ratio drops below a threshold (e.g., 0.3 for 30 days), automating part of the audit pattern.

### Limitations

- **Long-term storage is not native.** For retention beyond the configured TSDB window, the standard pattern is to ship samples to Thanos, Cortex, or a managed alternative.
- **Histograms are pre-aggregated.** P95/P99 accuracy depends on bucket configuration. The default cAdvisor histograms are coarse; high-fidelity work requires custom recording rules.
- **Not a log store.** Prometheus is for metrics; log analysis requires a separate stack (typically Loki or ELK).

## Related Concepts

- [[Entities/grafana]] — the visualization layer that turns Prometheus queries into the audit dashboard
- [[Concepts/k8s-resource-feedback-loop-discipline]] — the post-deployment audit depends on Prometheus
- [[Entities/kubernetes-vertical-pod-autoscaler]] — VPA's recommender reads similar metrics independently

## References

- Raw Article: [[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]]
- Original: https://dev.to/alitron/improving-kubernetes-resource-efficiency-with-automated-feedback-loops-to-reduce-over-provisioning-2kba
- Project: https://github.com/prometheus/prometheus
