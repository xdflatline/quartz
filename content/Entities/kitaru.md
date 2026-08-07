---
title: "Kitaru"

details: "Kitaru is the runtime layer of an agent stack — the layer that records every run as durable checkpoints so you can replay it, change one input, and diff the result. It wraps ordinary Python function boundaries with @flow and @checkpoint, records model and tool calls, and provides a runner + control-plane architecture. A Kitaru flow is a dynamic ZenML pipeline and runs on the same stacks, server, and dashboard. Adapters exist for PydanticAI, OpenAI Agents, Claude Agent SDK, Gemini Interactions, Google ADK (experimental), and LangGraph. Ships an MCP server and CLI so coding agents can drive the run/replay/improve loop. Self-host-first: single-service server on Kubernetes, artifacts in your own S3/GCS/Azure Blob, no mandatory SaaS control plane in the data path."
tags:
  - entities
  - runtime
  - agent
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: entity
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Kitaru

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Tool / Platform
**Repository:** https://github.com/zenml-io/kitaru-skills
**Website:** https://docs.zenml.io/kitaru / https://kitaru.ai

---

## Overview

Kitaru is the runtime for production AI agents: run them durably, replay them faithfully, improve them with evidence. It records every run as durable checkpoints, lets you re-execute a real run with one thing changed (a different model, a different prompt), and helps you roll the winning change across recent runs. The headline loop is run → replay → improve.

Kitaru is built by the team behind [ZenML](https://zenml.io) and runs on the same foundations. Each project works on its own — you can use Kitaru without ever touching ZenML. If you use both, they compose rather than coexist: a Kitaru flow is a dynamic ZenML pipeline under the hood, so your agents and pipelines run on the same stacks, persist artifacts to the same stores, and show up in the same server and dashboard.

## Key Details

### Position in the stack

Kitaru is the **runtime layer** of an agent stack, sitting between the harness (PydanticAI, OpenAI Agents, LangGraph, Claude Agent SDK, raw Python) and the platform (your org's governance, auth, observability). It is not a harness and not a packaged platform. Comparable tools: LangGraph (harness + its own runtime), LangSmith Deployment (runtime + platform packaged), Temporal (general-purpose durable workflow), DBOS (Postgres-backed durable workflows).

### Core primitives

- `@flow` — outer durable boundary for one run
- `@checkpoint` — unit of work whose inputs and output are persisted
- `flow.run(...).wait()` — start an execution; `FlowHandle` exposes `.exec_id`
- `flow.replay(exec_id, at="<checkpoint>", flow_overrides={...})` — re-execute a recorded run, optionally with overrides
- `kitaru.wait()` — pause a flow for external input; runner polls for `timeout` (default 600s), then exits and releases compute
- `kitaru.llm()` — tracked model call with secret resolution, prompt/response capture, token/latency logging
- `kitaru.log()` — scope-sensitive structured metadata (execution- or checkpoint-level)
- `kitaru.save()` / `kitaru.load()` — persistent named artifacts
- `KitaruClient` — programmatic inspection, replay, retry, resume, cancel
- MCP server — exposes replay and diff so a coding agent can drive the loop
- CLI — `kitaru executions replay <id> --at <checkpoint> --flow-overrides <json>`

### Replay override levels (three)

1. `flow_overrides` — changes top-level flow inputs
2. `checkpoint_overrides` — targets every recorded call with a checkpoint name
3. `invocation_overrides` — targets one recorded checkpoint, tool, or model call by invocation ID or call ID

### Deployment model

Deployments are versioned, remotely invocable entrypoints. Auto-versioned per flow (`v1`, `v2`, ...). Tags route traffic; `default` is reserved and always exclusive; shared tags can point to multiple versions but invoke requires single resolution. There is **no per-deployment token** — auth uses the same workspace/service-account credentials the CLI/SDK/MCP already use. Invocations are serverless (no long-lived per-version service).

### Architecture (three planes)

- **Control plane** — Kitaru server, UI, metadata DB, deployment registry, auth, credential brokering
- **Orchestration plane** — runner for a single execution; owns durable control flow (order, retry, replay, resume, wait)
- **Execution plane** — inline (same process) or isolated (separate container/job on the configured stack)

In local dev all three collapse into one Python process. In production the server is a Kubernetes pod, the runner is dispatched to the configured stack (Kubernetes, Vertex AI, SageMaker, AzureML), and artifacts live in the user's S3/GCS/Azure Blob bucket.

### Self-host posture

Single-service server on Kubernetes, deployed via Helm. Artifacts and state in the user's own object store. The server tracks metadata but does not access storage directly; clients fetch short-lived credentials brokered by the server. There is no mandatory SaaS control plane in the path of agent data.

### Adapters

| Framework | Adapter | Replay boundary (finest) |
|-----------|---------|--------------------------|
| PydanticAI | `KitaruAgent` | Per model/tool/MCP call, or one turn checkpoint |
| OpenAI Agents SDK | `KitaruRunner` | Per call, or one runner-call checkpoint |
| Claude Agent SDK | `KitaruClaudeRunner` | One completed Claude invocation |
| LangGraph | `KitaruGraphRunner` | One graph call, or middleware-wrapped model/tool calls |
| Gemini Interactions | (adapter) | Stable Interactions / Antigravity managed-agent responses |
| Google ADK | (adapter, experimental) | Whole-runner turn, or explicit ADK model/tool objects |

Migration skills live in the `zenml-io/kitaru-skills` package and are invokable from Claude Code as `/kitaru:<framework>-migration`.

## Status

Production. Documentation last updated 7 days before 2026-07-10 retrieval (deployments page 1 day before).

## Related Concepts

- [[Concepts/faithful-replay-with-isolated-change]] — the core replay primitive Kitaru exposes
- [[Concepts/durable-checkpoint-record-and-replay]] — the recording model
- [[Concepts/three-plane-agent-runtime]] — the control / orchestration / execution split
- [[Concepts/framework-agnostic-runtime-decorators]] — `@flow` and `@checkpoint` as Python decorators
- [[Concepts/agent-stack-layers]] — model / harness / runtime / platform
- [[Concepts/deployment-versioning-and-tag-routing]] — auto-versioning + exclusive/shared tags

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Docs: https://docs.zenml.io/kitaru
- Blog: https://kitaru.ai/blog/
- SDK reference: https://sdkdocs.kitaru.ai
- Migration skills: https://github.com/zenml-io/kitaru-skills
