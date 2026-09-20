---
title: "Cilium and eBPF"
details: "Cilium is the canonical eBPF-based Kubernetes CNI and observability platform; its Hubble component streams kernel-level network events (drops, DNS latency, policy decisions) without instrumenting applications, and Inspektor Gadget extends the same kernel-tracing model to general-purpose debugging."
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

# Cilium and eBPF

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Platform
**Website:** https://cilium.io

---

## Overview

Cilium is the leading eBPF-based networking and observability layer for Kubernetes. It replaces traditional iptables-based CNIs with eBPF programs attached to kernel hooks, and its Hubble observability component streams kernel-level network events (packet drops, DNS resolution latency, policy decisions) to engineers without requiring any application instrumentation.

## Key Details

- **CNI:** eBPF-based, with kube-proxy replacement (`--set kubeProxyReplacement=true`).
- **Hubble:** Network observability component; streams flow logs, DNS events, policy verdicts, and dropped-packet telemetry.
- **Inspektor Gadget:** Companion tool for general-purpose eBPF tracing on Kubernetes — `kubectl gadget run` exposes a curated set of kernel tracers (tcpconnect, biolatency, opensnoop, etc.).
- **Performance:** eBPF runs in kernel space, so overhead is bounded by event filtering rather than by instrumentation depth.

## Related Concepts

- [[Concepts/infrastructure-debugging-with-ebpf]] — Cilium / Hubble / Inspektor Gadget are the canonical implementations of the eBPF infrastructure-debugging pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8