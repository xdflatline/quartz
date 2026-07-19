---
title: "Kernel-Syscall Isolation VM"
detail: "Security model where a user-space kernel mediates every guest operation as a syscall, with the executor holding no capability of its own."
details: "AgentOS's isolation model: a Rust kernel owns the virtual filesystem, process table, socket table, pipes/PTYs, and policy engine. The executor (V8 isolate + WASM + native binaries) has zero host capability — every file read, process spawn, and socket open issues a syscall and blocks for the kernel's reply. This eliminates host fallthrough (no real host socket can be opened by guest networking) and gives granular, deny-by-default permissions instead of container-level coarse boundaries."
tags:
  - concepts
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Kernel-Syscall Isolation VM

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern / Architecture Constraint
**Status:** Production-validated

## Overview

The isolation model underlying AgentOS: a single trusted kernel chokepoint services every kind of guest operation. The executor holds no capability of its own, so guest code cannot escape to the host. Permissions are enforced at the syscall boundary, not at the container boundary.

## Core Content

### The Kernel Chokepoint

> "The kernel is the single chokepoint. Each kind of guest operation is serviced by a kernel-owned subsystem, never by a real host capability."

| Subsystem | Owned by Kernel | Guest Effect |
|-----------|----------------|--------------|
| Virtual filesystem | Yes | Guest I/O never hits host disk |
| Process table | Yes | No real host processes spawned |
| Socket table & DNS | Yes | Outbound traffic gated by network allowlist |
| Pipes / PTYs | Yes | Real Linux shell behavior |
| Policy & limits | Yes | Permission/network/resource limits enforced on every request |

### The Capability-Stripped Executor

> "The executor holds no capability of its own. For every file read, process spawn, or socket open, it issues a syscall and blocks for the kernel's reply."

- **JavaScript acceleration:** native V8 with full JIT inside an isolate — native speed, normal Node.js semantics
- **WASM:** `sh`, coreutils, and custom modules
- **Native binaries:** mounted tools run inside the same boundary
- **No host fallthrough:** even native binaries cannot bypass the kernel

### Networking Without Host Sockets

> "One authoritative transport. Guest `fetch()`, `node:http`, `node:net`, and WASM sockets all target the same kernel socket table. No part of guest networking opens a real host socket on its own."

- Egress gated by network allowlist
- Loopback stays confined to the VM
- Guest servers exposable via signed preview URLs

### Two-Layer Permission Model

1. **Permission policy (kernel-enforced)** — `allow_all`, `reject_all`, or `"ask"`; nothing allowed until opted in
2. **Approvals (agent-level)** — "ask before using a tool" via session-event stream

`"ask"` requests never expire; they block the active turn until answered or a lifecycle transition wins the race.

## Key Insights

1. **Capability-stripped executor** is the security primitive — guest code physically cannot reach the host, regardless of bug or prompt injection
2. **Single chokepoint** simplifies policy enforcement — every request passes through the kernel, so a single subsystem mediates all decisions
3. **Granular deny-by-default** replaces coarse container-level boundaries — no need to define container images to scope agent capabilities
4. **Kernel-syscall isolation ≠ hardware virtualization** — no KVM, no hypervisor; just Rust user-space mediation. That's why startup is 4-6ms instead of seconds
5. **Credentials stay on host** — bindings run server-side, so agents see only inputs and outputs

## Related Concepts

- [[Concepts/in-process-vm-agent-runtime-agentos]] — the runtime that houses this isolation model
- [[Concepts/sandbox-mounting-extension-pattern]] — when kernel-syscall isolation is not enough, mount a full sandbox
- [[Concepts/durable-actor-session-sleep]] — how isolation is preserved across actor sleep/wake

## Related Entities

- [[Entities/agentos]] — the canonical implementation

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Architecture docs: https://agentos-sdk.dev/docs/architecture
- Versus sandbox comparison: https://agentos-sdk.dev/docs/versus-sandbox
