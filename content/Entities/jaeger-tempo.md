---
title: "Jaeger and Tempo"
details: "Open-source distributed tracing backends — Jaeger (Uber-originated, CNCF graduated) and Tempo (Grafana Labs, CNCF incubating) — that ingest OpenTelemetry-compatible spans and reconstruct end-to-end request DAGs for tail-latency isolation and cascaded-failure analysis."
tags:
  - entity
  - tool
  - observability
created: 2026-09-19
updated: 2026-09-19
type: entity
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Jaeger and Tempo

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Platform
**Repository:** https://github.com/jaegertracing/jaeger / https://github.com/grafana/tempo
**Website:** https://www.jaegertracing.io / https://grafana.com/oss/tempo

---

## Overview

Jaeger and Tempo are the two leading open-source backends for distributed tracing. Both ingest spans via the OpenTelemetry protocol (OTLP) and Jaeger format, and both reconstruct the end-to-end request DAG from independently-emitted spans so engineers can isolate tail-latency spikes and cascading failures across service boundaries.

## Key Details

- **Jaeger:** Uber-originated, CNCF graduated since 2019. Uses Cassandra or Elasticsearch for span storage; ships its own UI for trace search and DAG visualization.
- **Tempo:** Grafana Labs, CNCF incubating. Designed for low-cost object-store storage (S3/GCS/Azure Blob); tracing UI lives in Grafana proper.
- **Compatibility:** Both accept OTLP from OpenTelemetry collectors; both support tail-based sampling via the collector pipeline.
- **Selection rule of thumb:** Jaeger if you already have Cassandra/ES operational expertise and want a self-contained UI; Tempo if you already run Grafana and want cheap object-store retention.

## Related Concepts

- [[Concepts/distributed-tracing-fabrics]] — Jaeger and Tempo are the canonical backend implementations for the distributed-tracing pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8