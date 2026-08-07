---
title: "Three-Plane Agent Runtime"

details: "The three-plane model splits agent-runtime responsibilities into distinct planes with different lifetimes and concerns. Control plane is the Kitaru server: long-lived, shared, holds metadata, deployment registry, auth, credential brokering. Orchestration plane is the per-run runner: durable control flow for one execution (order, retry, replay, resume, wait). Execution plane is the inline process or isolated container where the user's code actually runs. In local dev all three planes collapse into one Python process. In production the server is a Kubernetes pod, runners are dispatched to the configured stack (Kubernetes / Vertex AI / SageMaker / AzureML), and execution happens inline or in isolated containers/jobs. A sandboxes / external tools / custom backends are conceptual extensions of the execution plane. The model is distinct from the harness/runtime/platform stack-layer model, which describes where a runtime sits relative to harnesses and platform governance."
tags:
  - concepts
  - runtime
  - architecture-pattern
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: concept
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Three-Plane Agent Runtime

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

The three-plane model separates the responsibilities of an agent runtime into three planes with different lifetimes and concerns. It is a refinement of the older "control plane vs. data plane" split, specialized for agent workloads where the "data plane" needs its own subdivision because agent code has two distinct lifecycles: the durable control flow and the actual execution of work.

## Core Content

### The planes

| Plane | Lifetime | Responsibility | Runs user code? |
|-------|----------|----------------|-----------------|
| **Control plane** | Long-lived, shared | Kitaru server, UI, metadata DB, deployment registry, CLI/SDK/MCP APIs, auth and credential brokering | No |
| **Orchestration plane** | Per-run, durable | The runner: flow snapshot execution, checkpoint order, durable state, retry / replay / resume / wait | Yes, for inline checkpoints |
| **Execution plane** | Per-checkpoint or shorter | Inline process or isolated container (shipped); sandboxes, external tools, custom backends (conceptual) | Yes |

The control plane is what the org shares; the orchestration plane is one runner per execution; the execution plane is where the work happens.

### What runs where (extended)

| Component | What it does | Runs user code? |
|-----------|--------------|-----------------|
| Kitaru server | Deployment registry, execution metadata, checkpoint state, log metadata, auth, session state | No |
| Runner | Flow snapshot, checkpoint order, durable state, retry / replay / resume / wait | Yes, for inline checkpoints |
| Inline execution | Checkpoint inside the runner process/pod | Yes |
| Isolated runtime | Checkpoint in a separate container / job / pod / remote compute backend | Yes |
| Sandbox (conceptual) | Same contract as isolated, with stronger isolation or restricted egress. Not a shipped Kitaru execution target today | Yes, where integrated |
| External tool / MCP server | Performs work through a remote API | Outside Kitaru |
| Metadata store | Runs, versions, checkpoint statuses, replay lineage | No |
| Artifact / state store | Checkpoint outputs, files, logs, replay lineage | No |

### The run, step by step

1. Request arrives at the control plane (CLI / SDK / MCP / HTTP)
2. Server authenticates, resolves the flow (and version/tag), validates input, creates a run record and a `FlowHandle`
3. Control plane schedules a runner on the configured stack (Kubernetes pod, cloud job, local process)
4. Runner executes checkpoints in order — inline or delegating to an isolated target — persists outputs, advances
5. State is durable the entire time: if a checkpoint fails, the runner dies, or `kitaru.wait()` suspends, the server retains everything needed to retry / replay / resume
6. Consumer observes results via the `FlowHandle` (or UI / CLI / SDK / MCP)

### Runner vs. sandbox

The runner is the durable brain of a run. The sandbox (or isolated runtime) is the hands that perform work. If the sandbox dies mid-execution — evicted, partitioned, OOMed — the runner still holds durable checkpoint state and can retry that single checkpoint, resume from the last boundary, or replay with a modified input. The sandbox's failure is localized to the checkpoint that was executing.

**Implication:** a sandbox provider is not the same thing as durable execution. Sandboxes are bounded environments; durable execution is a property of the runner and the checkpoints it persists. Platform teams that conflate the two will get a sandbox failure that takes the whole run down.

### Local dev vs. production

In local dev, all three planes collapse into a single Python process on the developer's machine. The server is embedded, no DB to configure, checkpoint outputs on local filesystem. `kitaru init` produces a fully working durable execution environment in under a minute.

In production, the planes separate: server is a Kubernetes pod (Helm), runner is dispatched to the configured stack (Kubernetes, Vertex AI, SageMaker, AzureML), artifacts and state are in the user's own S3/GCS/Azure Blob bucket. The server tracks metadata but does not access storage directly; clients fetch short-lived credentials brokered by the server.

### Distinct from the stack-layer model

This is separate from the model / harness / runtime / platform stack-layer split. The stack-layer model says where a runtime sits relative to the LLM and the org's governance. The three-plane model says how a single run executes inside the runtime. A diagram with both stacked is the right mental model.

## Key Insights

1. The planes are about lifetime and concern, not about implementation — local dev collapses them for ergonomics; production separates them for scale and isolation
2. "I have a sandbox provider" is not "I have durable execution" — the sandbox is one execution-plane implementation; the runner is the durable brain
3. Control plane brokers credentials but does not access storage; clients fetch short-lived creds — this is what makes "no mandatory SaaS control plane in the data path" true
4. The model generalizes: any record-and-replay runtime (Kitaru, LangGraph with its checkpointer, Temporal) can be expressed in these terms, with differences in how strictly they separate the planes

## Related Concepts

- [[Concepts/durable-checkpoint-record-and-replay]] — the seam between orchestration and execution planes
- [[Concepts/faithful-replay-with-isolated-change]] — what the orchestration plane enables
- [[Concepts/framework-agnostic-runtime-decorators]] — what the user writes on the execution plane
- [[Concepts/agent-stack-layers]] — the model / harness / runtime / platform split (orthogonal)

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Original: https://docs.zenml.io/kitaru
