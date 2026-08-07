---
title: "AgentOS"

details: "AgentOS (by Rivet) is an in-process lightweight VM that runs AI coding agents with deny-by-default permissions, near-zero cold starts (~6 ms p50), and a shared sidecar architecture. Replaces traditional container sandboxes with kernel-syscall-level isolation, supports 9 sandbox providers as mountable extensions, and exposes 5 built-in agents (Pi, Claude Code, OpenCode, Codex, custom) over the Agent Communication Protocol (ACP). Apache-2.0, v0.2.7, ~131 MB per full coding agent vs ~1,024 MB for the cheapest sandbox."
tags:
  - entities
  - runtime
  - agent
created: 2026-07-19
updated: 2026-07-19
type: entity
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# AgentOS

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Tool / Framework
**Repository:** https://github.com/rivet-dev/agentos
**Website:** https://agentos-sdk.dev/
**License:** Apache-2.0
**Latest Release:** v0.2.7 (Jul 7, 2026) — preview status, API subject to change
**GitHub Stats:** 3.9k stars, 192 forks, 21 releases, 16 contributors

## Overview

AgentOS is a portable, open-source operating system for AI agents that runs as a lightweight in-process VM. It is the lightweight alternative to full Linux sandboxes (E2B, Daytona, Modal, Cloudflare Sandbox, Vercel, etc.), pairing with them via a sandbox-mounting extension when heavier workloads (browsers, native binaries, dev servers) are needed. Built on the same isolation technology trusted by browsers worldwide (V8 isolates + kernel-level syscall interception), it claims up to **516× faster cold starts** and **47× smaller memory footprint** than the cheapest sandbox providers at the p99 percentile.

## Key Details

### Core vs Actor

Two packages:

- **`@rivet-dev/agentos-core`** — bare-bones in-process VM control, no actor runtime, no client/server split. Use when you only need direct VM control in an existing Node.js backend.
- **`@rivet-dev/agentos`** — wraps the core VM in a Rivet Actor: adds durable state, automatic sleep/wake, distributed state, signed preview URLs, multiplayer, workflows/queues/cron orchestration, built-in auth, and agent-to-agent communication. Use when you need durability, scaling, or orchestration.

### Agents (built-in)

- **Pi** — lightweight, fast execution coding agent
- **Claude Code** (Beta) — full tool access, file editing, shell execution
- **Codex** (Beta) — OpenAI's coding agent
- **OpenCode** — open-source coding agent
- **Custom Agent** — bring your own by speaking ACP inside the VM

### Tech Stack

- **Primary language:** Rust (kernel, sidecar, secure-exec)
- **JavaScript runtime:** V8 JIT-compiled, full Node.js semantics
- **WASM:** shell, coreutils, custom command packages
- **Protocol:** Agent Communication Protocol (ACP) — universal transcript format across all agents
- **SDK languages:** TypeScript (primary), Rust
- **Database:** SQLite over Unix Domain Socket (UDS) — shared by filesystem, blocks, and session metadata
- **Built-in JS validation:** Zod for binding input schemas
- **Actor runtime:** Rivet / RivetKit

### Performance

- Cold start: p50 4.8 ms, p95 5.6 ms, p99 6.1 ms (Intel i7-12700KF, 10000 runs)
- Memory: ~22 MB (shell), ~131 MB (full coding agent with Pi + MCP + FS)
- Self-hosted cost: $0.0000011–0.0000053/s depending on hardware

### Integrations (Registry)

- **File systems:** Host Directory, S3 (chunked), Google Drive, In-Memory, Sandbox
- **Browsers:** Browserbase (Beta, no sandbox required)
- **Sandbox providers (9):** Local, Docker, E2B, Daytona, Modal, Cloudflare, Vercel, ComputeSDK, Sprites
- **Software packages (28):** git, ripgrep, jq, sqlite3, duckdb, vim, ssh (with strict known_hosts), wget, curl, coreutils, grep, sed, fd, tree, gawk, findutils, zip, unzip, envsubst, gzip, diffutils, yq, file, Codex CLI + meta-packages (`everything`, `build-essential`, `common`)

### Deployment Targets

- **Rivet Cloud** (managed, zero-ops)
- **Vercel** (serverless)
- **Railway** (cloud infrastructure)
- **Kubernetes** (self-hosted on your cluster)
- **AWS ECS**
- **Google Cloud Run**
- **Hetzner**
- **VM & Bare Metal**
- **Custom Platform**

## Key Insights

1. **In-process VM model** eliminates the cold-start and memory tax of container sandboxes by sharing a sidecar process across many V8-isolated VMs
2. **Two-layer permission model** — kernel-enforced syscall policy plus agent-level approvals — gives granular control without container-level coarse boundaries
3. **Bindings replace MCP for first-party code** — direct host JS function calls with Zod-derived CLI shims, near-zero latency, up to 80% token reduction via code mode
4. **ACP universal transcript format** lets you mix and match agents (Pi, Claude Code, OpenCode, Codex, custom) without reworking your session/history layer
5. **Rivet Actor runtime** is what makes AgentOS horizontally scalable — VMs become durable named server objects with automatic sleep/wake, not ephemeral processes

## Related Concepts

- [[Concepts/in-process-vm-agent-runtime-agentos]] — AgentOS's specific architecture pattern (V8 isolate + Rust kernel + shared sidecar)
- [[Concepts/binding-cli-shim-pattern]] — exposing host JS functions as auto-generated CLI commands inside the VM
- [[Concepts/durable-actor-session-sleep]] — Rivet's automatic sleep/wake with SQLite-UDS-persisted session history
- [[Concepts/kernel-syscall-isolation-vm]] — Rust-kernel-mediated VM with no host fallthrough
- [[Concepts/rivet-actor-deployment-kubernetes]] — Kubernetes deployment of agentOS via RivetKit pod replicas
- [[Concepts/sandbox-mounting-extension-pattern]] — pairing the in-process VM with external sandbox providers
- [[Concepts/session-event-durability-levels]] — ephemeral vs durable event tiers
- [[Concepts/zod-cli-flag-mapping]] — how Zod schemas become agentOS binding CLI flags

## Related Entities

- [[Entities/rivet]] — the parent actor platform on which AgentOS's actor model is built
- [[Entities/pi-coding-agent]] — built-in lightweight agent
- [[Entities/claude-code]] — built-in agent
- [[Entities/opencode]] — built-in agent
- [[Entities/codex-cli]] — installable as registry software
- [[Entities/browserbase]] — beta cloud browser integration

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Documentation site: https://agentos-sdk.dev/docs/
- GitHub repository: https://github.com/rivet-dev/agentos
- Issue tracker: https://github.com/rivet-dev/rivet/issues
- Discord: https://rivet.dev/discord
