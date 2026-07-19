---
title: "Rivet"
detail: "Open-source actor platform that powers AgentOS — durable server objects with portable runtime, automatic sleep/wake, workflows, and self-hostable orchestration engine."
details: "Rivet is the actor platform underlying AgentOS. RivetKit (the SDK) lets you write long-lived stateful server objects (actors) that are reachable by name, distributed across infrastructure, and portable across deploy targets (Vercel, Railway, Kubernetes, AWS ECS, Google Cloud Run, Hetzner, VM/Bare Metal, Custom). Rivet Cloud offers fully managed zero-ops hosting; the open-source engine can be self-hosted. The platform also offers Rivet Compute as a managed deploy target for AgentOS. Apache-2.0, https://rivet.dev"
tags:
  - entity
created: 2026-07-19
updated: 2026-07-19
type: entity
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Rivet

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Platform / Project
**Website:** https://rivet.dev/
**Repository:** https://github.com/rivet-dev/rivet
**License:** Apache-2.0

## Overview

Rivet is the open-source actor platform on which AgentOS is built. It provides the durable state, scheduling, orchestration, and cross-infrastructure portability layer that wraps the raw AgentOS VM into a long-lived server object. RivetKit is the SDK; Rivet Engine is the orchestration plane (cloud or self-hosted); Rivet Cloud offers fully managed zero-ops hosting.

## Key Details

### Components

- **RivetKit** — the SDK for writing actors. The `agentOS()` function from `@rivet-dev/agentos` returns an ordinary TypeScript Rivet actor definition; AgentOS actions and events are merged in automatically (their names are reserved).
- **Rivet Engine** — the orchestration plane. Self-hostable on Kubernetes, Hetzner, VMs, bare metal, or any container platform. Rivet Cloud hosts it for you.
- **Rivet Compute** — fully managed deployment target for AgentOS on Rivet Cloud.
- **Dashboard** — https://dashboard.rivet.dev/ for project creation, environment variable provisioning, and live connection status.

### Actor Semantics

- **Durable server objects** — reach by name: `vm.getOrCreate("my-agent")`
- **Stateful by default** — filesystem, actor state, durable session metadata, completed ACP history
- **Portable runtime** — consistent across all supported deploy targets
- **Sleep/wake** — default 30s idle timeout; 15min graceful shutdown; 24.8-day action timeout
- **Multiplayer** — multiple clients observe/collaborate with the same actor in real time
- **Cron & Webhooks** — built-in scheduling and external event primitives
- **Workflows** — wrap `run` handler in `workflow()`; each `ctx.step()` is recorded, retried, resumed independently
- **Agent-to-agent** — built-in delegation through host-defined bindings
- **Authentication** — pluggable API keys, OAuth, JWTs
- **Long-lived WebSockets** — envoys connect to your app over WS; default Ingress idle timeouts (30-60s) drop these — must be raised to at least 1 hour (3600s)

### Deployment Targets

- Rivet Compute (managed)
- Vercel
- Cloudflare
- Supabase
- Railway
- Kubernetes
- AWS ECS
- Google Cloud Run
- Hetzner
- VM & Bare Metal
- Custom Platform

### Kubernetes-Specific

Required manifest settings for RivetKit apps on Kubernetes:

- `terminationGracePeriodSeconds: 2100` (35 min) — Rivet runner waits up to 30m for actors to finish, plus shutdown overhead
- `RIVET_ENDPOINT` and `RIVET_PUBLIC_ENDPOINT` env vars via Secret
- `replicas: N` controls the stateless worker pool
- Ingress/load-balancer idle/read/send timeouts must be at least 3600 seconds (1 hour) to keep WebSocket connections alive

## Key Insights

1. **Rivet is the reason AgentOS is deployable** — without the actor runtime, the in-process VM would only work in single-process Core mode
2. **The actor abstraction maps perfectly onto agent workloads** — long-lived, stateful, named, addressable, with built-in scheduling
3. **Self-hosted engine** keeps AgentOS portable for compliance-sensitive deployments that cannot use Rivet Cloud
4. **Long-lived WebSocket assumptions** are a non-obvious deployment gotcha — most managed Ingress defaults (30-60s) break Rivet's connection model

## Related Concepts

- [[Concepts/rivet-actor-deployment-kubernetes]] — Kubernetes deployment of RivetKit apps
- [[Concepts/durable-actor-session-sleep]] — automatic sleep/wake + stateful actors
- [[Concepts/in-process-vm-agent-runtime-agentos]] — AgentOS's specific runtime built on Rivet
- [[Concepts/sandbox-mounting-extension-pattern]] — AgentOS extension to sandbox providers; Rivet hosts the actors

## Related Entities

- [[Entities/agentos]] — AgentOS is built on Rivet's actor model

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Rivet docs: https://rivet.dev/docs/
- Rivet deploy targets: https://rivet.dev/docs/deploy/
- Kubernetes deploy: https://rivet.dev/docs/deploy/kubernetes
- Self-hosting guide: https://rivet.dev/docs/general/self-hosting
- Dashboard: https://dashboard.rivet.dev/
