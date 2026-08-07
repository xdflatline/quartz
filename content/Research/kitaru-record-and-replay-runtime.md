---
title: "Kitaru and the Record-and-Replay Runtime Layer for AI Agents"

details: "Research index on Kitaru, a self-host-first runtime for production AI agents built on top of ZenML. The central thesis: durable execution is the enabler, faithful replay is the differentiator, and cross-run diff is what makes 'improve' a measurable loop rather than a vibe. The index covers the four-layer agent stack (model / harness / runtime / platform), the three-plane runtime architecture (control / orchestration / execution), the @flow + @checkpoint decorator surface, the framework-agnostic adapter model (PydanticAI, OpenAI Agents, Claude Agent SDK, Gemini Interactions, Google ADK experimental, LangGraph), the deployment versioning + tag-routing model, and the self-host-first posture (single-service Kubernetes server, user-owned artifact store, no mandatory SaaS control plane in the data path). Use this index to navigate the concept pages and entity pages extracted from the source docs."
tags:
  - research
  - agent
  - runtime
  - infrastructure
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: research
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Research Index: Kitaru and the Record-and-Replay Runtime Layer for AI Agents

**Updated:** 2026-07-10
**Source:** Kitaru Documentation (https://docs.zenml.io/kitaru) — retrieved 2026-07-10

---

## Overview

Kitaru positions itself as the runtime layer of an agent stack — the layer that records every run as durable checkpoints so you can replay it, change one input, and diff the result. The headline loop is run → replay → improve. Kitaru is built on top of ZenML and shares its stacks, server, and dashboard; the two projects can also be used independently. The runtime is self-host-first: a single-service Kubernetes server, artifacts in the user's own S3/GCS/Azure Blob bucket, and no mandatory SaaS control plane in the data path.

The most important conceptual move is the distinction between **faithful replay** (re-execute the real run with one input swapped) and **output re-scoring** (eval-style: re-score saved outputs against a new judge). The whole architecture exists because faithful replay needs durable checkpoints, and durable checkpoints let you make a no-change baseline that reproduces exactly — so a one-change replay's diff isolates the change rather than replay noise.

## Concepts

### Core runtime primitives
- [[Concepts/faithful-replay-with-isolated-change]] — the three override levels (flow / checkpoint / invocation) and why a no-change baseline is the prerequisite for trustworthy diff
- [[Concepts/durable-checkpoint-record-and-replay]] — the `@checkpoint` decorator, `cache=True` semantics, failed-checkpoint-as-durable-context, retry / replay / resume from one recording model
- [[Concepts/framework-agnostic-runtime-decorators]] — three integration levels (black-box / coarse / framework-aware adapter), per-framework adapter tradeoffs, the honesty boundary

### Architecture
- [[Concepts/three-plane-agent-runtime]] — control / orchestration / execution split; runner vs. sandbox; what runs where in local dev vs. production
- [[Concepts/agent-stack-layers]] — model / harness / runtime / platform decomposition; what Kitaru owns vs. integrates with; the buyer profile that fits Kitaru
- [[Concepts/deployment-versioning-and-tag-routing]] — auto-versioning, exclusive vs. shared tags, the `default` tag's special rules, serverless routing, no per-deployment tokens

### Related (existing in the garden)
- [[Concepts/agent-first-pipeline-architecture]] — orthogonal: agent-as-orchestrator pattern (OpenMontage) vs. runtime-as-record-and-replay (Kitaru)
- [[Concepts/graph-based-workflow-engine]] — orthogonal: graph-based runtimes (LangGraph) vs. decorator-based runtimes (Kitaru)
- [[Concepts/agent-self-improvement]] — orthogonal: cognitive design paradigm for self-improving agents; Kitaru's `improve` step is the infrastructure substrate
- [[Concepts/friction-logging-for-agents]] — complementary: friction metrics for self-improvement; Kitaru's `kitaru.log()` structured metadata is the recording primitive
- [[Concepts/agent-memory-layer-patterns]] — orthogonal: persistent memory layers; Kitaru's `kitaru.save()` / `kitaru.load()` is the artifact primitive

## Tools & Projects

### Runtime layer
- [[Entities/kitaru]] — self-host-first runtime for production AI agents; durable checkpoints, faithful replay, cross-run diff, versioned deployments
- [[Entities/zenml]] — the open-source MLOps/LLMOps framework Kitaru is built on and composes with

### Harness-layer (integrated via Kitaru adapters, not separately indexed here)
- PydanticAI — `KitaruAgent` adapter (per model/tool/MCP call)
- OpenAI Agents SDK — `KitaruRunner` adapter (per call or one runner-call)
- Claude Agent SDK — `KitaruClaudeRunner` adapter (one Claude invocation)
- Gemini Interactions — adapter (stable Interactions / Antigravity)
- Google ADK — experimental adapter
- LangGraph — `KitaruGraphRunner` adapter (one graph call or middleware-wrapped)

### Runtime-layer alternatives named in the source
- Temporal — general-purpose polyglot durable workflow engine
- DBOS — Postgres-backed durable workflows with deterministic bodies
- LangGraph (its own runtime) — built into the harness's graph model
- LangSmith Deployment — runtime + platform packaged

## Raw Sources

- [[Raw/docs-zenml-kitaru-2026-07-10]] — full verbatim extraction of the Kitaru docs as of 2026-07-10

## Key Sources Table

| Source | Topic | Date Retrieved | Key Items |
|--------|-------|----------------|-----------|
| Kitaru docs (https://docs.zenml.io/kitaru) | Runtime for production AI agents | 2026-07-10 | Run/replay/improve loop, three-plane model, framework-agnostic adapters, deployment versioning + tag routing |
| Kitaru blog (https://kitaru.ai/blog/) | Durable execution essays | 2026-07-10 (referenced) | "Why agents need durable execution", "No journal replay" |
| kitaru-skills (https://github.com/zenml-io/kitaru-skills) | Migration skills for coding agents | 2026-07-10 (referenced) | Per-framework `/kitaru:<framework>-migration` skills for Claude Code |

## Cross-Cutting Themes

### The record-and-replay runtime as a category
1. **The runtime layer is its own layer in the agent stack** — distinct from model, harness, and platform; the buyer is typically a platform team, not an individual agent builder
2. **Durable execution is the enabler; faithful replay is the differentiator** — recording is necessary but not sufficient; the value is the no-change baseline that reproduces exactly
3. **Per-call replay fidelity is bounded by the harness's exposed seam** — frameworks that hide internal calls (LLM/tool calls inside their loop) cannot be replayed at that granularity, only at the outer checkpoint

### Self-host-first vs. packaged platform
1. **Kitaru is self-host-first; LangSmith Deployment is packaged** — the buyer profile is the discriminating factor. Kitaru fits regulated / multi-harness / platform-team-led orgs; LangSmith Deployment fits LangChain-standardized orgs
2. **No mandatory SaaS control plane in the data path** — the server brokers short-lived credentials to the user's own object store; this is the operational boundary that matters for regulated industries
3. **The deployment model has no per-deployment tokens** — auth uses the same workspace / service-account boundary the CLI/SDK/MCP already use; this removes a class of operational pain

### Failure modes that record-and-replay turn into features
1. **A failed checkpoint is durable context, not a crash** — typed artifact that can be retried, replayed, fed back to the agent, or surfaced to a human
2. **A sandbox death is localized to the executing checkpoint** — the runner still holds durable state and can retry / resume / replay
3. **An interrupted `kitaru.wait()` releases compute without losing state** — the run can be resumed seconds, hours, or months later with the same checkpoints and artifacts

## Next Research Directions

- [ ] Benchmark Kitaru's adapter boundary against LangGraph's middleware boundary for the same PydanticAI agent — measure per-call replay fidelity and developer ergonomics
- [ ] Evaluate Kitaru vs. Temporal for a multi-team agent platform: deployment complexity, language portability, cost of the orchestrator
- [ ] Prototype the cohort-diff pattern: replay N recent runs from a checkpoint with one override, aggregate `cost` / `latency` / `quality` from `kitaru.log()` metadata, return a winner
- [ ] Test the self-host posture with a real Kubernetes install: time-to-first-durable-execution, credential brokering ergonomics, RBAC integration story
- [ ] Compare `kitaru.wait()` ergonomics against LangGraph `interrupt` and OpenAI Agents SDK `approval` for human-in-the-loop patterns
