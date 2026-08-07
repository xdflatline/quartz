---
title: "Grafana"

details: "An open-source analytics and visualization platform, typically used as the presentation layer on top of Prometheus (and many other time-series backends). In the source article, Grafana is cited alongside Prometheus as the tool pair that automates the post-deployment resource audit: Grafana dashboards display per-pod P95 usage vs. declared `resources.requests`, and Grafana alerts (or AlertManager wired through Grafana) trigger the incident-triggered review path. The combination of Prometheus for data collection and Grafana for visualization is the de facto standard for Kubernetes cluster observability."
tags:
  - entities
created: 2026-07-25
updated: 2026-07-25
type: entity
source: "[[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]]"
---

# Grafana

**Source:** Alina Trofimova, DEV.to ([[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]])
**Category:** Tool / Observability Visualization
**Repository:** https://github.com/grafana/grafana
**Website:** https://grafana.com

## Overview

An open-source analytics and visualization platform, typically used as the presentation layer on top of Prometheus (and many other time-series backends). In the source article, Grafana is cited alongside Prometheus as the tool pair that automates the post-deployment resource audit.

## Key Details

### Role in the Audit Pattern

The post-deployment audit is most usefully consumed as a Grafana dashboard, not a one-off query. A useful panel set:

- **Per-pod P95 CPU usage vs. requested** (single-stat with threshold coloring; red if ratio < 0.3)
- **Per-pod P95 memory usage vs. requested** (same)
- **Top 10 pods by absolute slack capacity** (bar gauge, ordered by `requested - actual`)
- **Cluster-wide utilization over time** (line graph, against the efficiency SLA target)

Grafana's threshold coloring and `No data` handling make the "this pod has been wasting resources for 30 days" signal immediate.

### Alerting

Grafana can fire alerts directly (since v8+) or delegate to AlertManager. For the resource-audit pattern, the most useful alerts are:

- **Sustained low utilization.** `P95 ratio < 0.3` for 30 days on a given pod → fires an efficiency-review ticket.
- **Sustained near-saturation.** `P95 ratio > 0.9` for 7 days → fires an under-provisioning review (the symmetric concern).

### Strengths

- **Wide data-source support.** The same dashboard tool works against Prometheus, Loki, Tempo, CloudWatch, BigQuery, and many others—useful for hybrid infrastructure.
- **Templating.** Dashboard variables (`$namespace`, `$pod`) make a single dashboard serve the full cluster.
- **Provisioning via YAML.** Dashboards are stored as JSON/YAML and applied via the Grafana provisioning system, making the audit dashboard reviewable in git and reproducible across clusters.

### Limitations

- **Read-mostly.** Grafana is a visualization layer; it does not collect or store metrics. The audit pattern still depends on Prometheus (or equivalent) for the underlying data.
- **No native control-loop action.** Grafana can fire alerts, but closing the loop on a low-utilization alert (i.e., actually adjusting the pod spec) is a separate process. This is where the feedback-loop discipline (humans or a controller like VPA) closes the gap.

## Related Concepts

- [[Entities/prometheus]] — the data source Grafana typically visualizes
- [[Concepts/k8s-resource-feedback-loop-discipline]] — the audit dashboard is the surface that surfaces waste to humans
- [[Entities/kubernetes-vertical-pod-autoscaler]] — closes the loop automatically; Grafana surfaces the loop to humans

## References

- Raw Article: [[Raw/devto-k8s-feedback-loop-overprovisioning-2026-07-25]]
- Original: https://dev.to/alitron/improving-kubernetes-resource-efficiency-with-automated-feedback-loops-to-reduce-over-provisioning-2kba
- Project: https://github.com/grafana/grafana
