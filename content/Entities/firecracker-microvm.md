---
title: "Firecracker MicroVMs"
details: "AWS-developed VMM that boots lightweight microVMs in under 125 ms with a minimal device model and a hardened threat surface — the canonical isolation primitive for sandboxes that execute LLM-generated code, where the threat model is the model itself rather than a co-tenant workload."
tags:
  - entity
  - tooling
  - runtime
created: 2026-09-19
updated: 2026-09-19
type: entity
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Firecracker MicroVMs

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Hypervisor
**Repository:** https://github.com/firecracker-microvm/firecracker
**Website:** https://firecracker-microvm.github.io

---

## Overview

Firecracker is the AWS-developed VMM (Virtual Machine Monitor) that powers AWS Lambda and AWS Fargate. It boots a minimal Linux microVM in under 125 ms with a deliberately small device model and a hardened attack surface — making it the canonical isolation primitive for sandboxed AI-agent execution.

## Key Details

- **Footprint:** < 125 ms cold-start, < 5 MiB memory baseline per microVM.
- **Device model:** Minimal — virtio-net, virtio-block, virtio-vsock, serial console, keyboard; no PCI passthrough, no USB.
- **Threat surface:** Reduces the attack surface to ~50 Linux syscalls; jailer cgroup/namespace isolation by default.
- **Adoption:** AWS Lambda, Fly Machines, Fly.io's app platform, E2B, many AI agent sandbox products.
- **Alternative:** gVisor (Google) takes a different approach — user-space kernel interception rather than hardware-virtualization isolation.

## Related Concepts

- [[Concepts/sandboxed-execution-for-ai-agents]] — Firecracker is the canonical implementation substrate for the AI-agent sandbox pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8