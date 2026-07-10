---
title: "Agent Stack Layers (Model / Harness / Runtime / Platform)"
detail: "Decompose agent tooling into four layers — model, harness, runtime, platform — so a runtime like Kitaru can position itself relative to harnesses and platform governance rather than trying to own both."
details: "The four-layer decomposition of agent tooling: model (the LLM itself, picked per-call or per-agent), harness (prompts, tools, model loop, context management — picked per-team), runtime (durable checkpoints, faithful replay, cross-run diff, resume, wait, versioned deployments, artifact handling — Kitaru's layer), platform (auth, entitlements, interceptors, observability, policy — usually the org's existing stack). The decomposition exists so that 'is Kitaru a competitor to X?' has a precise answer: Kitaru competes with Temporal, DBOS, and the runtime portion of LangSmith Deployment; it sits beside PydanticAI, OpenAI Agents, Claude Agent SDK, and LangGraph at the harness layer; it integrates with the org's existing platform for auth/RBAC/egress policy. The same decomposition explains why 'I have a sandbox provider' is not the same as 'I have durable execution' — sandboxes are execution-plane machinery; durable execution is a runtime concern."
tags:
  - concepts
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: concept
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Agent Stack Layers (Model / Harness / Runtime / Platform)

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Agent tooling decomposes into four layers with distinct buyers, lifetimes, and replacement cycles. Knowing which layer is which is what answers "is Kitaru a competitor to X?" precisely: the runtime layer is where Kitaru sits, the harness layer is what it does not own, the platform layer is what it integrates with, and the model layer is upstream of all of it.

## Core Content

### The four layers

| Layer | What it is | Picked by | Example tools |
|-------|-----------|-----------|----------------|
| **Model** | The LLM itself — a compute unit over a context window | Per-call or per-agent | OpenAI, Anthropic, Google, open-weights, fine-tuned in-house |
| **Harness** | The loop around the model — prompts, tools, model loop, context management, structured outputs, in-turn memory | Per-agent or per-team | PydanticAI, Claude Agent SDK, OpenAI Agents, LangGraph, Deep Agents |
| **Runtime** | How the agent survives, executes, and improves — durable checkpoints, faithful replay, cross-run diff, resume, wait, versioned deployments, invocation routing, artifacts, execution placement | Per-org (platform team decision) | **Kitaru**, Temporal, DBOS, LangSmith Deployment (runtime + platform packaged), LangGraph (its own runtime) |
| **Platform** | How the org governs — auth, entitlements, interceptors, observability, product UI, policy | Per-org (already exists) | The org's existing stack |

### The responsibility split (Kitaru's stance)

| Concern | Kitaru owns? | Notes |
|---------|--------------|-------|
| Checkpoint / faithful replay / cross-run diff / resume | Yes | Core product |
| Flow versioning and invocation routing | Yes | Core product |
| Execution placement per checkpoint | Yes, as config | `@checkpoint(runtime="isolated")` |
| Sandbox implementation | No | Adapters, not mandate |
| Secrets storage | Partly | Alias-linked resolution for `kitaru.llm()` |
| Auth to invoke flows | Yes | Workspace keys / service accounts; no per-deployment tokens |
| Enterprise entitlements / RBAC | No | Integrate with your platform |
| Network egress policy | No | Determined by execution target |
| Interceptors / guardrails | No | Harness or platform owns this |
| Observability | Partly | Runtime metadata, logs, artifact lineage; integrate with tracing |
| Data compliance policy | No | Policy stays with your platform |

**The line to remember:** durability without execution policy is not enough for production agents — but Kitaru should make policy attachable to execution boundaries, not mandate the policy itself.

### The overlap to know

- LangGraph has its own checkpointer, resume, and time-travel — powerful inside its graph/state-machine model. Kitaru's difference: `@checkpoint` wraps ordinary Python boundaries independent of any harness
- LangSmith Deployment delivers durable execution + sandboxes + auth proxy as a packaged platform. Kitaru ships just the runtime primitives so platform teams bring their own auth, sandbox, governance
- Temporal is a battle-tested polyglot durable workflow engine. Kitaru is Python-first, agent-shaped, single-service
- DBOS is Postgres-backed and requires deterministic workflow bodies. Kitaru flows are plain Python with no determinism requirement; state lives in the user's cloud bucket

### When Kitaru fits (the buyer's profile)

- Application teams across the org pick different harnesses
- Infra must be self-hosted (regulated, on-prem, sovereignty)
- Platform team wants runtime primitives, not a packaged platform
- Deployment must plug into existing Kubernetes, secret manager, observability, and data policy
- Durable execution needs to be independent of any single framework's worldview

### When Kitaru is the wrong size

- The whole org standardizes on LangGraph + LangSmith — use what you have
- One agent for yourself that never leaves your laptop — a harness alone is enough
- Hosted all-in-one agent platform is the better buy (and self-host is not required)

### Shorthand

- Harnesses define behavior. Kitaru runs, replays, and improves it. Platforms define governance.
- Use a harness to build the agent. Use Kitaru when that agent becomes a durable, versioned production workload you need to replay and improve.

## Key Insights

1. The four-layer decomposition is a buyer's map: it tells you which layer the org is making a decision about, and which tools are substitutes vs. complements
2. The runtime layer is where "durable execution" lives — not the model, not the harness, not the platform. A model is a compute unit; a harness is a loop; a runtime is a record-and-replay guarantee
3. The boundary between runtime and platform (auth, RBAC, egress policy) is the most contested in practice — the right answer is "runtime makes policy attachable to execution boundaries, doesn't mandate the policy"
4. "I have a sandbox provider" is not the same as "I have durable execution" — sandboxes are bounded execution environments; durable execution is a property of the runner and the checkpoints it persists

## Related Concepts

- [[Concepts/three-plane-agent-runtime]] — how a single run executes inside the runtime
- [[Concepts/durable-checkpoint-record-and-replay]] — what the runtime actually records
- [[Concepts/faithful-replay-with-isolated-change]] — the runtime's differentiator
- [[Entities/kitaru]] — the runtime-layer tool

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Original: https://docs.zenml.io/kitaru/core-concepts/harness-runtime-platform
