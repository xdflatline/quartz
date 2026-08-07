---
title: "In-Process VM Agent Runtime (AgentOS)"

details: "AgentOS's distinctive runtime: a single Node.js process hosts a sidecar (the `default` pool) that brokers syscalls for many lightweight VMs, each of which is a V8 isolate plus kernel state. Per-VM memory is tens of MB; warm VM creation is single-digit milliseconds; the executor holds no capability of its own — every file read, process spawn, or socket open issues a syscall and blocks for the kernel's reply. The pattern achieves sandbox-grade isolation at sandbox-grade costs and replaces container-level coarse permissions with kernel-syscall-level granular ones."
tags:
  - concepts
  - runtime
  - kernel
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# In-Process VM Agent Runtime (AgentOS)

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern
**Status:** Production-validated (v0.2.7, used in production benchmarks)

## Overview

AgentOS's distinguishing architectural pattern: a trusted Rust kernel + a shared sidecar process hosting many lightweight VMs (V8 isolates + kernel state), all running inside a single Node.js process. The executor in each VM holds no capability of its own — every operation is a kernel-mediated syscall, eliminating host fallthrough entirely.

## Core Content

### Three-Role Model

| Role | What it is | Key trait |
|------|-----------|-----------|
| **App (Client)** | Your code (TypeScript or Rust) | Trusted caller; never runs guest code |
| **Server (Sidecar)** | Trusted core hosting VMs | Owns every kernel; brokers all syscalls |
| **VM** | Isolated Linux environment | Fully virtualized; unit of isolation |

### VM Anatomy (Security Boundary)

**Kernel (Trusted Core, Rust):**
- Virtual filesystem — per-VM VFS; guest I/O never hits host disk
- Process table — kernel-managed, no real host processes spawned
- Socket table & DNS — virtual network stack; egress gated by network allowlist
- Pipes / PTYs — kernel-owned IPC/terminals for real Linux shell behavior
- Policy & limits — permission policy, network allowlist, resource limits enforced on every request

**Executor (Untrusted):**
- JavaScript via V8 with full JIT inside an isolate (native speed, normal Node.js semantics)
- WASM for shell (`sh`), coreutils, and custom modules
- Mounted native binaries run inside the same boundary
- No host fallthrough — every operation is a syscall serviced by the kernel

### Sidecar Process Architecture

- Every VM runs inside a shared sidecar process (the `default` pool), not its own OS process
- Each additional VM adds only marginal cost — V8 isolate + kernel state
- Per-VM memory: tens of MB
- Warm VM creation: single-digit milliseconds
- Disposing a VM tears down only that VM; the shared sidecar stays alive for the host process lifetime
- Explicit sidecar option isolates a group of VMs in their own process for advanced use

### Process & Shell Model

- `exec()` / `run()` start fresh guest processes; `spawn` for long-running; interactive shells supported
- Each `exec()` / `run()` starts a brand new guest process — in-memory state never leaks between runs
- stdio bridged through kernel-owned pipes and PTYs

### Filesystem

- Layered engines: root layer (snapshot) + overlay (guest writes) + grafted mount points
- Host-backed mounts: guest paths can map to host directories, S3, or cloud stores
- Kernel restricts I/O to mount root, defeating symlink and `..` tricks
- `/home/agentos` survives sleep/wake

### Networking

- One authoritative transport. Guest `fetch()`, `node:http`, `node:net`, WASM sockets all target the same kernel socket table
- Egress gated by network allowlist; loopback stays confined to the VM
- Guest servers exposable via signed preview URLs

## Key Insights

1. **VM density is the headline benefit** — thousands of agents per host with sandbox-grade isolation at 1/47th the memory
2. **Capability-stripping at the executor** is the security model — no part of guest networking can open a real host socket on its own
3. **Sidecar pooling** keeps process-creation overhead amortized across many VMs
4. **Same-process, kernel-mediated isolation** sidesteps both the cold-start tax of containers and the coarse container-level permissions
5. **Inherits Rivet Actor semantics** when used via `agentOS()` — durable state, sleep/wake, multiplayer come from the actor runtime

## Related Concepts

- [[Concepts/kernel-syscall-isolation-vm]] — the specific security model AgentOS uses
- [[Concepts/durable-actor-session-sleep]] — what `agentOS()` adds on top
- [[Concepts/sandbox-mounting-extension-pattern]] — how it pairs with full sandboxes
- [[Concepts/rivet-actor-deployment-kubernetes]] — how it scales

## Related Entities

- [[Entities/agentos]] — the canonical implementation
- [[Entities/rivet]] — the actor runtime that wraps it

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Architecture docs: https://agentos-sdk.dev/docs/architecture
- Core package: https://agentos-sdk.dev/docs/core
