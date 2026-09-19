---
title: "OpenTelemetry"
details: "Vendor-neutral observability framework that standardizes trace, metric, and log instrumentation through the W3C traceparent context header and the OTLP wire protocol, with collectors and SDKs that emit spans to distributed columnar or TSDB backends like Jaeger and Tempo."
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

# OpenTelemetry

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Framework
**Website:** https://opentelemetry.io

---

## Overview

OpenTelemetry (OTel) is the CNCF-incubating vendor-neutral standard for emitting traces, metrics, and logs from instrumented services. It defines the OTLP wire protocol, the W3C `traceparent` context header format, and a collector binary that ingests spans and exports them to a backend of the operator's choice.

## Key Details

- **Status:** CNCF Incubating; convergence target for OpenTracing and OpenCensus.
- **Components:** SDKs in 11+ languages, the `otelcol` collector, semantic conventions for HTTP, gRPC, databases, messaging.
- **Context propagation:** W3C Trace Context (`traceparent`, `tracestate`) is the default; B3 and Jaeger propagation are supported as fallbacks.
- **Backends:** Plugs into Jaeger, Tempo, Honeycomb, Datadog, Lightstep, etc. via OTLP exporters.
- **Sampling:** Head-based (decision at span start) and tail-based (decision after full trace observed) both supported.

## Related Concepts

- [[Concepts/distributed-tracing-fabrics]] — OpenTelemetry is the standard implementation substrate for the distributed-tracing pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8