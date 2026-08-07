---
title: "Research Index: AgentOS"

details: "Comprehensive research on AgentOS (Apache-2.0, v0.2.7, by Rivet): an in-process Linux VM for AI agents with Rust kernel + V8 isolation, near-zero cold starts (~6 ms p50), 28 software packages, 9 sandbox providers, 5 file systems, and Rivet Actor orchestration. Covers the three-role architecture, kernel-syscall isolation model, binding CLI shim pattern, durable actor session sleep, Rivet/Kubernetes deployment recipe, sandbox mounting extension, and session event durability levels."
tags:
  - research
created: 2026-07-19
updated: 2026-07-19
type: research
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Research Index: AgentOS

**Updated:** 2026-07-19
**Source:** agentOS official docs + GitHub README, https://agentos-sdk.dev/docs/

## Overview

Comprehensive research on **AgentOS**, a portable open-source operating system for AI agents built on Rust kernel + V8 isolation + Rivet Actor orchestration. Captures the in-process VM architecture, the binding pattern, Kubernetes deployment recipe, and scaling model. Use this index as a starting point for any AgentOS evaluation or integration.

## Concepts

### Architecture
- [[Concepts/in-process-vm-agent-runtime-agentos]] — the canonical runtime pattern (V8 isolate + Rust kernel + shared sidecar)
- [[Concepts/kernel-syscall-isolation-vm]] — security model where executor holds no capability of its own
- [[Concepts/durable-actor-session-sleep]] — sleep/wake with SQLite-over-UDS persistence and three-tier ACP resume
- [[Concepts/session-event-durability-levels]] — ephemeral vs. durable events, sequence-based dedup

### Integration Patterns
- [[Concepts/binding-cli-shim-pattern]] — host JS functions exposed as auto-generated CLI commands inside the VM
- [[Concepts/zod-cli-flag-mapping]] — deterministic Zod-to-CLI conversion rules
- [[Concepts/sandbox-mounting-extension-pattern]] — pairing in-process VM with full sandboxes on demand

### Deployment & Scaling
- [[Concepts/rivet-actor-deployment-kubernetes]] — K8s recipe: graceful-shutdown, Ingress timeouts, secrets, scaling

## Tools & Projects

### Platforms
- [[Entities/agentos]] — the framework itself (Apache-2.0, v0.2.7, 3.9k stars, in preview)
- [[Entities/rivet]] — parent actor platform; RivetKit SDK + self-hostable engine + Rivet Cloud

## Raw Sources

- [[Raw/agentos-sdk-dev-docs-2026-07-19]] — full extracted documentation bundle (intro, quickstart, crash course, architecture, deployment, sessions, persistence, cron, webhooks, bindings, software, registry, vs-sandbox, system-prompt, core package)

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [GitHub README](https://github.com/rivet-dev/agentos) | Overview, benchmarks, tech stack | Jul 18 2026 | Cold start 4.8 ms p50, 22-131 MB, 3-17× cheaper |
| [Architecture docs](https://agentos-sdk.dev/docs/architecture) | 3-role model, kernel/executor split | 2026 | Rust kernel, V8 isolate, no host fallthrough |
| [Deployment docs](https://agentos-sdk.dev/docs/deployment) | 3 production paths, 9 deploy targets | 2026 | Rivet Cloud, self-hosted, Core |
| [Kubernetes deploy](https://rivet.dev/docs/deploy/kubernetes) | K8s recipe | 2026 | `terminationGracePeriodSeconds: 2100`, 3600s timeouts |
| [Bindings](https://agentos-sdk.dev/docs/bindings) | Host-to-VM CLI shim pattern | 2026 | Zod schemas, 80% token reduction |
| [Registry](https://agentos-sdk.dev/registry) | 5 agents, 5 filesystems, 9 sandboxes, 28 software pkgs | 2026 | E2B, Daytona, Modal, Cloudflare, Vercel, ComputeSDK, Sprites |
| [Sessions](https://agentos-sdk.dev/docs/sessions) | ACP sessions, durability, history | 2026 | Three-tier resume, idempotency keys |
| [Persistence](https://agentos-sdk.dev/docs/persistence) | Sleep/wake, SQLite-UDS storage | 2026 | 30s idle, 15min graceful, 24.8d action timeout |
| [Cron](https://agentos-sdk.dev/docs/cron) | Scheduled jobs, agent sessions | 2026 | Overlap: skip/allow/queue |
| [Webhooks](https://agentos-sdk.dev/docs/webhooks) | External triggers (Slack example) | 2026 | Hono, auto-serialized concurrent prompts |
| [Core package](https://agentos-sdk.dev/docs/core) | Standalone VM without actor runtime | 2026 | `@rivet-dev/agentos-core` |
| [Versus sandbox](https://agentos-sdk.dev/docs/versus-sandbox) | VM vs full sandbox | 2026 | Side-by-side comparison table |
| [System prompt](https://agentos-sdk.dev/docs/system-prompt) | Injected context per session | 2026 | `additionalInstructions`, `skipOsInstructions` |

## Cross-Cutting Themes

### Isolation & Security

1. **Capability-stripped executor** is the security primitive — the kernel mediates every syscall, guest code cannot reach the host
2. **Two permission layers** — kernel-enforced policy (deny-by-default) plus agent-level approvals (`"ask"`)
3. **Granular, not coarse** — permissions per syscall beat container-level boundaries
4. **Credentials stay on host** — bindings run server-side; agents see only inputs/outputs

### Performance & Cost

1. **In-process VM density** — V8 isolates in tens of MB each, thousands per host
2. **516× faster cold start at p99** vs. fastest sandbox (E2B); 92× at p50
3. **47× smaller memory** for shell-only workloads vs. cheapest sandbox (Daytona)
4. **Up to 17× cheaper** self-hosted on Hetzner ARM
5. **Sleep/wake** keeps idle agents at near-zero resource cost

### Portability & Deployment

1. **Single npm package** — `agentOS()` runs on laptop, Vercel, Railway, Kubernetes, AWS, GCP, Hetzner, bare metal
2. **9 sandbox providers** in the registry — pick the best fit, avoid lock-in
3. **Self-hosted Rivet Engine** is the on-prem path for compliance-sensitive deployments
4. **Rivet Cloud** is the zero-ops managed path
5. **Core package** is the bare-bones alternative for embedding in any Node.js backend

### Orchestration

1. **Durable, named, addressable actors** — `vm.getOrCreate("name")` is the mental model
2. **Automatic sleep/wake** — idle agents sleep, next prompt transparently restores
3. **Workflow primitive** — `ctx.step()` is recorded, retried, resumed independently
4. **Agent-to-agent** — one agent calls another through a binding, no shared state
5. **Multiplayer** — multiple clients collaborate on the same actor session in real time
6. **Cron + Webhooks** — built-in scheduling and external event primitives

### Integration & Extensibility

1. **ACP universal transcript** — same format across Pi, Claude Code, OpenCode, Codex, custom
2. **Bindings replace MCP for first-party code** — direct host function calls, no network hop
3. **Code-mode token savings** — up to 80% reduction vs. tool-call round-trips
4. **28 WASM software packages** — common dev tools ship by default
5. **Custom software** — package your own agents and WASM commands

## Next Research Directions

- [ ] **Benchmark Rivet Actor sleep/wake** against Mastra's session model — does SQLite-UDS persistence actually scale beyond a few hundred concurrent actors?
- [ ] **Evaluate bindings vs. MCP in practice** — 80% token reduction is a claim; measure on real workloads
- [ ] **Compare in-process VM to container-per-agent** — at what agent count does the per-VM overhead exceed the per-container overhead?
- [ ] **Test Kubernetes deployment on a real cluster** — verify the `terminationGracePeriodSeconds: 2100` math, Ingress 3600s timeouts, and graceful drain behavior
- [ ] **Investigate WebSocket reconnect storms** — what monitoring/dashboards does Rivet Cloud expose for this failure mode?
- [ ] **Probe sandbox mounting** — measure the latency penalty for E2B/Daytona mounts vs. native in-process
- [ ] **Read the Rust kernel source** — how is the capability-stripped executor actually implemented? V8 isolates are a well-known primitive; the kernel side is less documented
- [ ] **Compare to OpenMontage/Mastra agent runtimes** — does the V8-isolate model offer advantages over subprocess or container isolation for our use cases?
