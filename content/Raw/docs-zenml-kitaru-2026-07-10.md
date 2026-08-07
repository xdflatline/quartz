---
title: "Kitaru Documentation (ZenML)"

details: "Full verbatim extraction of the Kitaru documentation as of 2026-07-10. Covers the run/replay/improve loop, harness-vs-runtime-vs-platform positioning, the control/orchestration/execution three-plane model, the runner-vs-sandbox contract, inline-vs-isolated checkpoint execution, deployment versioning and tag routing, wait/input/resume semantics, the supported adapter surface (PydanticAI, OpenAI Agents, Claude Agent SDK, Gemini Interactions, Google ADK, LangGraph), and the structured-metadata vs runtime-log observability split. Last updated in source: ~7 days before retrieval."
tags:
  - raw
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: raw
---

# Kitaru Documentation (ZenML)

**Source:** Kitaru Docs (https://docs.zenml.io/kitaru)
**Date Retrieved:** 2026-07-10
**Type:** Product Documentation (GitBook-hosted)

---

## Welcome to Kitaru

Kitaru is the runtime for production AI agents: run, replay, improve. It records every model call and tool call as a durable checkpoint, then lets you re-execute a real run faithfully with one thing changed — a different model, a different prompt — and diff the result against the original. Because the baseline reproduces, the difference you see is your change, not replay noise.

The harness you already picked (PydanticAI, OpenAI Agents SDK, LangGraph, Claude Agent SDK, raw Python) keeps owning how the agent thinks. Kitaru owns the run record and the replay loop. A Kitaru flow is a dynamic ZenML pipeline, so agents run on the same stacks, server, and dashboard as your ZenML pipelines.

### Run, replay, improve

- **Run (durable).** Every `@checkpoint` is a durable unit of work; its output is persisted automatically, and every model and tool call is recorded. If a flow fails partway, replaying it reuses recorded results instead of re-running expensive work.
- **Replay (the differentiator).** Re-execute a recorded run from any checkpoint. A plain rerun with no change reproduces the original — that is your baseline. Replay again with one input overridden and diff the two. This re-executes the real run from a checkpoint; it is not re-scoring saved outputs like an eval.
- **Improve.** Apply the same change across a cohort of recent runs, measure cost, latency, and quality, and keep the winner.

Kitaru is self-host-first: a single-service server on your own Kubernetes, artifacts in your own S3/GCS/Azure Blob. No mandatory SaaS control plane in the path of your agent's data.

### The replay loop

```python
import kitaru
from kitaru import checkpoint, flow

@checkpoint
def research(topic: str) -> str:
    return kitaru.llm(f"Summarize {topic} in two sentences.")

@checkpoint
def draft_report(summary: str) -> str:
    return kitaru.llm(f"Write a short report based on: {summary}")

@flow
def research_agent(topic: str) -> str:
    summary = research(topic)
    return draft_report(summary)

if __name__ == "__main__":
    # Run, then replay from a checkpoint with one input changed.
    run = research_agent.run(topic="Why do agents need durable execution?").wait()

    baseline = research_agent.replay(run.exec_id, at="draft_report")
    variant = research_agent.replay(
        run.exec_id,
        at="draft_report",
        flow_overrides={"model": "anthropic/claude-opus-4"},
    )
    # baseline reproduces the original; diff variant against it to isolate your change.
```

`run(...)` returns a handle; `.wait()` blocks for the result and exposes `.exec_id`. `replay(exec_id, at="<checkpoint>", flow_overrides={...})` re-executes from that checkpoint, overriding flow inputs such as the model or prompt profile. The same loop is available over the CLI and the MCP server so a coding agent can drive it.

### Where ZenML fits

Kitaru is built by the team behind ZenML, the open-source framework for production ML and LLM pipelines, and runs on the same foundations. Each project works on its own — you can use Kitaru without ever touching ZenML. If you use both, they compose rather than coexist: a Kitaru flow is a dynamic ZenML pipeline under the hood, so your agents and pipelines run on the same stacks, persist artifacts to the same stores, and show up in the same server and dashboard.

### Runtime primitives

These are the primitives Kitaru adds on top of your existing Python agent code. You keep your harness and your control flow; Kitaru records the run and makes it replayable.

- **Replay and override:** Re-execute any run from any checkpoint — to recover from a failure, or with overrides (a different model or parameter) to isolate the effect of a change before you ship it. Use invocation overrides when you need to change one recorded checkpoint, tool, or model call instead of every call with the same checkpoint name.
- **Durable execution:** Wrap steps in `@checkpoint` and your agent picks up where it left off without re-running expensive work.
- **Wait and resume:** Add `kitaru.wait()` and let agents pause for a human, another system, or later input; after the polling timeout, compute is released and the run resumes when input lands.
- **Artifact lineage:** Every checkpoint output is written to your object store as a typed, versioned artifact — step through runs, diff outputs across runs, and trace a bad final output back to the exact step that produced it.
- **Execution management:** `KitaruClient` lets you inspect, replay, retry, resume, and cancel executions from code or CLI.
- **Tracked LLM calls:** Use `kitaru.llm()` and every call gets automatic secret resolution, prompt/response capture, and token/latency logging.
- **Persistent data:** `kitaru.save()` / `kitaru.load()` let agents store and retrieve files, objects, and results across executions.
- **Structured observability:** `kitaru.log()` attaches key-value metadata to any checkpoint or flow for debugging and the UI.
- **Runtime configuration:** `kitaru.configure()` sets your model, log store, and stack defaults in one call.
- **Framework and infrastructure portability:** Keep your Python control flow, use your preferred framework, and run locally or on remote stacks — Kubernetes, Vertex AI, SageMaker, AzureML.

---

## Harness, Runtime, Platform

Kitaru is the runtime layer of an agent stack — the layer that records every run as durable checkpoints so you can replay it, change one input, and diff the result. It is not a harness (how an agent reasons) and not a platform (how your org governs). Knowing which layer is which is where most "is Kitaru a competitor to X?" questions get answered.

Agent tooling spans four layers:

- **Model layer** — the LLM itself. A compute unit over a context window, picked per-call or per-agent: OpenAI, Anthropic, Google, open-weights, fine-tuned in-house.
- **Harness layer** — the loop around the model. Prompts, tools, model loop, context management, structured outputs, in-turn memory. Picked per-agent or per-team.
- **Runtime layer** — how the agent survives, executes, and improves over time. Durable checkpoints, faithful replay, cross-run diff, resume, wait states, versioned deployments, invocation routing, artifact + state handling, execution placement.
- **Platform layer** — how the organization governs. Auth, entitlements, interceptors, observability, product UI, policy. Usually lives in your existing stack.

Kitaru sits in the runtime layer. It is not a harness and it is not a packaged platform. It gives platform teams the durable execution primitives — record, replay, diff — that attach to the harness their app teams picked and the platform their org already runs. Durability is the enabler; faithful replay and cross-run diff are what you do with it.

### Where Kitaru is — and isn't

| Tool | Primary layer | What it optimizes for |
|------|---------------|----------------------|
| Pydantic AI | Harness | Typed, ergonomic Python agent logic |
| Claude Agent SDK | Harness | Claude-native autonomous coding / tool loops |
| OpenAI Agents SDK | Harness | Hosted-tool agents on the OpenAI stack |
| LangGraph | Harness + runtime (in its own model) | Graph-native agents with built-in checkpointer |
| Deep Agents | Harness (on LangGraph) | Opinionated multi-agent pattern |
| LangSmith Deployment | Runtime + platform (packaged) | Adopting the LangChain-hosted stack |
| Temporal | Runtime (general-purpose) | Polyglot, deterministic workflow engine |
| DBOS | Runtime (general-purpose) | Postgres-backed durable workflows |
| **Kitaru** | **Runtime (Python-agent-shaped)** | **Framework-agnostic durable execution primitives** |

### The overlap

- LangGraph has its own checkpointer, resume, and time-travel — powerful inside its graph/state-machine model. Kitaru's difference is that `@checkpoint` wraps ordinary Python boundaries independent of any harness.
- LangSmith Deployment delivers durable execution + sandboxes + auth proxy as a packaged platform. Kitaru ships just the runtime primitives so platform teams bring their own auth, sandbox provider, and governance.
- Temporal is a battle-tested polyglot durable workflow engine. Kitaru is Python-first, agent-shaped (first-class `kitaru.llm()`, `kitaru.wait()`, artifact lineage), with a simpler single-service deployment.
- DBOS is a Postgres-backed durable workflow library with deterministic workflow bodies. Kitaru flows are plain Python with no determinism requirement; state and artifacts live in your own cloud bucket, not Postgres.

### What Kitaru owns vs integrates with

| Concern | Kitaru owns? | Kitaru's stance |
|---------|--------------|-----------------|
| Checkpoint / faithful replay / cross-run diff / resume | Yes | Core product — the run/replay/improve loop |
| Flow versioning and invocation routing | Yes | Core product |
| Execution placement per checkpoint | Yes, as config | `@checkpoint(runtime="isolated")` today; richer policy evolving |
| Sandbox implementation | No | Provide adapters; don't mandate a vendor |
| Secrets storage | Partly | Alias-linked secret resolution for `kitaru.llm()`; integrate with your secret manager |
| Auth to invoke flows | Yes | Workspace keys / service accounts; no per-deployment tokens |
| Enterprise entitlements / RBAC | No | Integrate with your platform |
| Network egress policy | No | Determined by the execution target your stack provides; Kitaru does not enforce it |
| Interceptors / guardrails | No | Harness or your platform owns this |
| Observability | Partly | Runtime metadata, logs, artifact lineage; integrate with your tracing |
| Data compliance policy | No | Policy stays with your platform; Kitaru does not mandate one |

**The line to remember:** Durability without execution policy is not enough for production agents — but Kitaru should make policy attachable to execution boundaries, not mandate the policy itself.

**Shorthand:** Harnesses define behavior. Kitaru runs, replays, and improves it. Platforms define governance.

---

## How It Works

Kitaru is the runtime for production AI agents: run them durably, replay them faithfully, improve them with evidence.

### The mental model

A Kitaru flow is a dynamic ZenML pipeline, and a checkpoint is like a step. Your agent runs on the same stacks, the same server, and the same dashboard as your ZenML pipelines — there is no separate agent runtime to operate.

The difference from a classical pipeline is that a flow's shape is decided at runtime by the agent, not fixed in advance. Each `@checkpoint` you cross records its inputs and output as a durable unit. That recording is what the rest of Kitaru is built on.

**The loop:**

- **Run (record).** Every model call and tool call is recorded as a durable checkpoint. This is the enabler, not the headline.
- **Replay (the point).** Re-execute a real run from a checkpoint with exactly one input changed — a different model, a different prompt. Compare it against a faithful baseline rerun (the same run with nothing changed). Because the baseline reproduces, the diff is your change, not noise.
- **Improve.** Apply the winning change across a cohort of recent runs, measure cost / latency / quality, keep what wins.

Durable execution is the how, replay is the why. Recording every checkpoint is what lets Kitaru reconstruct a run's exact starting state and re-execute it with one input swapped. Without durable checkpoints you can re-score outputs (an eval); you cannot faithfully re-run the agent.

### Components

When you call `.run()` on a flow, three things work together to make it durable: the Kitaru server (shared metadata, auth, deployment registry), the runner (per-run durable control flow), and one or more execution targets (where each checkpoint's code actually executes). During local development all three collapse into a single Python process. In production they separate across your infrastructure.

Kitaru separates durable control flow from code execution:

- The Kitaru server stores shared metadata, deployment snapshots, checkpoint state, execution logs, and control-plane data.
- For each run, a runner (the durable brain of an execution) executes the selected flow snapshot, manages checkpoint order, persists state, and handles retry, replay, resume, and wait.
- Individual checkpoints can run inline in the runner or in an isolated runtime (a separate container, Kubernetes job, or cloud job on the configured stack).

**Key idea:** The runner owns the durable run: checkpoint order, state, retry, replay, resume, and wait. Execution targets do the work. Checkpoints are the contract between the two.

### Control / orchestration / execution

Kitaru splits runtime responsibilities into three planes. (This is separate from the harness / runtime / platform split, which is about where Kitaru sits in the broader agent stack — not about how a single run executes.)

| Plane | What lives here | Responsibility |
|-------|-----------------|----------------|
| Control plane | Kitaru server, UI, metadata DB, deployment registry, CLI/SDK/MCP APIs, auth and credential brokering | Knows what exists and who can call what |
| Orchestration plane | The runner for a single execution | Owns durable control flow for one run |
| Execution plane | Inline process or isolated container (shipped today); sandboxes, external tools, and custom backends are conceptual extensions of the same contract | Performs work |

The control plane is long-lived and shared. The orchestration plane is per-run and durable. The execution plane is where your code (and your agent's code) actually executes.

### What runs where

| Component | What it does | Runs user code? |
|-----------|--------------|-----------------|
| Kitaru server (control plane) | Stores deployment registry, execution metadata, checkpoint state, log metadata, auth and session state | No |
| Runner (orchestration plane) | Runs the selected flow snapshot, controls checkpoint order, persists durable state, handles retry / replay / resume / wait | Yes, for inline checkpoints |
| Inline execution | Runs a checkpoint inside the runner process/pod | Yes |
| Isolated runtime | Runs a checkpoint in a separate container, job, pod, or remote compute backend | Yes |
| Sandbox (conceptual) | The same contract as isolated, tightened with stronger isolation or restricted egress. Not a shipped Kitaru execution target today — provided via adapters / your platform. | Yes, where integrated |
| External tool / MCP server | Performs work through a remote API or capability | Outside Kitaru |
| Metadata store | Stores runs, versions, checkpoint statuses, replay lineage | No |
| Artifact / state store | Stores checkpoint outputs, files, logs, replay lineage | No |

### The run, step by step

1. **Request arrives.** A user, service, or upstream agent calls the Kitaru invocation API (via CLI, SDK, MCP, or HTTP).
2. **Server resolves the flow.** The server authenticates the caller, resolves the target flow (and optionally a version or tag), validates the input schema, and creates a run record plus a `FlowHandle`.
3. **Runner starts.** The control plane schedules a runner on your configured stack — a Kubernetes pod, a cloud job, or the local process in dev. The runner loads the selected flow snapshot.
4. **Runner executes checkpoints in order.** For each checkpoint, the runner either executes inline or delegates to an isolated target. It waits for the result, persists the output to the artifact/state store, and advances.
5. **State is durable the entire time.** If a checkpoint fails, if the runner dies, or if a `kitaru.wait()` suspends the run, the server retains everything needed to retry, replay, or resume later.
6. **Consumer observes results.** The caller uses the returned `FlowHandle` (or the UI / CLI / SDK / MCP) to tail logs, inspect checkpoints, provide human input, replay, or cancel.

### Runner vs sandbox

The runner is the durable brain of a run. The sandbox (or isolated runtime) is the hands that perform work.

If a sandbox dies mid-execution — a container evicted, a network partition, a pod OOM — the runner still holds durable checkpoint state and can retry that single checkpoint, resume from the last known boundary, or replay the run with a modified input or code version. The sandbox's failure is localized to the checkpoint that was executing, not the whole agent.

This is why platform teams should not confuse "I have a sandbox provider" with "I have durable execution". A sandbox is a bounded execution environment. Durable execution is a property of the surrounding runner — and of the checkpoints it persists.

### Inline vs isolated checkpoints

Every checkpoint picks an execution target. Two are built in today: `inline` (same process as the runner) and `isolated` (a separate container or job on the configured stack).

### A failed checkpoint is durable context

In classical pipelines, a failed step is a crash. In Kitaru, a failed checkpoint is durable context — something the runner, the agent loop, a human, or a retry policy can reason about.

Because the retrieval checkpoint's failure is persisted as a typed artifact, a downstream consumer has several real options:

- Retry the same checkpoint with the same input
- Replay the run from a checkpoint with one input overridden (e.g. a corrected document id or a different model)
- Replay with modified code (e.g. a new retrieval strategy)
- Feed the error artifact back into the agent loop so it can self-correct
- Wait for a human to provide a correction via `kitaru.wait()`, then resume

This is what "agent-native error handling" means in practice: failures become data, durable state survives them, and the same recorded run can be re-executed with one thing changed.

### How deep do you integrate?

You don't have to restructure your agent to get value. Pick the depth that fits.

**Level 0 — Black-box harness.** Wrap the entire agent run as one checkpoint.
- Fastest integration
- Minimal code changes
- Framework-agnostic
- Tradeoff: replay boundary is coarse (one per agent run) and you see less of the agent's internal state.

**Level 1 — Coarse workflow checkpoints.** Add checkpoints around the phases that matter to your team.
- Useful replay points
- Better audit trail
- Good balance of portability and durability
- Tradeoff: you (not the framework) decide where the boundaries go.

**Level 2 — Framework-aware adapter.** Use a Kitaru adapter that tracks the framework's internals (model calls, tool calls, intermediate state) as child events under the enclosing checkpoint.
- Richer introspection
- Better debugging
- Tighter developer experience
- Tradeoff: adapters are per-framework and need maintenance.

### Framework-agnostic by construction

Kitaru does not require your agent to be written as a graph. `@checkpoint` wraps ordinary Python function boundaries, independent of the harness. A platform team supporting multiple harnesses can still standardize durability, replay, and execution metadata on a single runtime primitive. The harness choice stays a per-team decision.

### Local development

When you are developing locally, all three components run inside a single Python process on your machine. The server is embedded — no separate service to start, no database to configure. Checkpoint outputs are written to your local filesystem.

`kitaru init` produces a fully working durable execution environment in under a minute. Flows behave exactly the same as they will in production — same checkpointing, same replay, same observability — just without the cloud infrastructure underneath.

### Production

In production, the three components separate across your infrastructure:

- The server runs as a long-lived Kubernetes pod (deployed via Helm). It stores execution state in a database and serves the UI. Your whole team connects to it.
- The runner runs on the compute backend defined by your stack — Kubernetes, Vertex AI, SageMaker, AzureML. When you call `.run()`, the client fetches short-lived credentials from the server and dispatches the execution directly to the compute backend. The runner executes your checkpoints and writes outputs to cloud storage. If the execution crashes, replay picks up from the last completed checkpoint.
- Artifacts and state live in your own S3 / GCS / Azure Blob bucket. The server tracks metadata but does not access storage directly; when a client needs to read files, it fetches temporary credentials brokered by the server.

There is no mandatory SaaS control plane in the path of your agent's data.

---

## Core Concepts

### Core ideas

| Concept | What it is |
|---------|-----------|
| Flow | The outer durable boundary around your workflow |
| Checkpoint | A unit of work inside a flow whose output is persisted |
| Execution | A single run of a flow, identified by a unique ID |
| Structured metadata | Key-value data you attach to executions and checkpoints with `kitaru.log()` |
| Runtime log storage | Where runtime logs are sent (configured separately from structured metadata) |
| Active stack | The default execution target used when no per-run `stack=...` override is passed |

### What you can use today

Kitaru's current release includes:

- `@flow` — mark a function as a durable workflow
- `@checkpoint` — mark a function as a persisted work unit
- `flow.run(...).wait()` — run a flow to completion; the handle carries `.exec_id`
- `flow.replay(exec_id, at="<checkpoint>", flow_overrides={...})` — re-execute a recorded run from a checkpoint, optionally overriding flow inputs such as `model` or `prompt_profile`
- `kitaru.log()` — attach structured metadata to the current scope
- `kitaru.wait()` — pause a flow until external input is supplied
- `kitaru.llm()` — make tracked model calls with prompt/response capture
- `kitaru.connect()` — connect to a Kitaru server
- `kitaru.configure()` — set process-local runtime defaults
- `kitaru.save()` / `kitaru.load()` — persist and load named artifacts in checkpoints
- `kitaru.list_stacks()` / `kitaru.current_stack()` / `kitaru.use_stack()` — manage the default stack
- `KitaruClient` — inspect executions, fetch logs, resolve waits, retry, replay, and browse artifacts
- `FlowHandle` — interact with a running or finished execution

Replay and diff are also exposed over an MCP server and the `kitaru` CLI (`kitaru executions replay <id> --at <checkpoint> --flow-overrides <json>`), so a coding agent can drive the run → replay → improve loop directly.

---

## Flows

A flow is the durable boundary for one agent run — the unit your platform invokes and the runner executes. It matters because the flow is what you can later replay: every model call and tool call inside it is recorded at checkpoint boundaries, so a finished run can be reproduced faithfully and rerun with one input changed. A flow is a dynamic ZenML pipeline; it runs on the same stacks, server, and dashboard as your ZenML pipelines.

**The flow body is the orchestration layer. The checkpoints inside are the replay boundaries.**

### Defining a flow

Decorate your orchestration function with `@flow`. The decorated function becomes a callable wrapper object. Inside the flow body, you compose checkpoints — the units of work whose outputs are persisted.

### Running a flow

Use `.run()` to start an execution. `.run()` submits the execution and immediately returns a `FlowHandle`. The flow runs in the background while your code continues. Call `handle.wait()` when you need the result.

### FlowHandle

| Property / Method | What it does |
|-------------------|--------------|
| `handle.exec_id` | The unique execution identifier |
| `handle.status` | Current execution status (refreshed on each access) |
| `handle.wait()` | Block until the execution finishes, then return the persisted run output |
| `handle.get()` | Return the persisted run output immediately if finished, otherwise raise an error |

`handle.get()` does not wait. If the execution is still running, it raises a `KitaruStateError`. For flows that explicitly return a value, both methods return the saved run output. For flows that do not return a value, inspect the persisted artifacts instead.

If the flow execution fails, `handle.wait()` raises a typed `KitaruExecutionError` (or a more specific subclass) with the execution ID, final status, and the failure origin attached.

### Runtime options

| Option | Default | What it controls |
|--------|---------|------------------|
| `retries` | `0` | Number of automatic retries on failure |
| `cache` | `True` | Whether checkpointed outputs can be reused from previous runs. Set `False` to disable. |
| `stack` | `None` | Target execution environment for this run (overrides the active stack default) |
| `image` | `None` | Container image for remote execution |

Per-run values override decorator defaults.

For `stack`, the full precedence chain is:

1. `.run(..., stack="...")`
2. `@flow(stack="...")`
3. `kitaru.configure(stack="...")`
4. `KITARU_STACK`
5. `[tool.kitaru].stack` in `pyproject.toml`
6. active stack selected via `kitaru stack use ...`

### Rules to know

- Flow functions should compose checkpoints. The flow body is the orchestration layer — heavy work belongs in checkpoints.
- Use `.run()` to start flows directly from source. Direct calls (`my_agent(...)`) are not supported and raise `KitaruUsageError`. Use `my_agent.run(...)` for source-backed executions, or `.invoke(...)` for deployment-backed executions.
- Retries must be non-negative. Passing a negative `retries` value raises a `KitaruUsageError`.

---

## Checkpoints

A checkpoint is a unit of work inside a flow whose inputs and output are recorded durably. Checkpoints are the recorded boundaries that make two things possible: resume a failed run from where it stopped, and faithfully replay a real run so you can change one thing and trust the diff.

A checkpoint is also the contract between the runner and the execution target: the runner owns durable control flow (order, retry, replay, resume, wait), the execution target (inline, isolated container, sandbox, external tool) does the work, and the checkpoint is the recorded boundary they agree on. That is why a checkpoint failure is never just a crash — it is persisted context the runner, an agent loop, or a human can retry, replay, or feed back into the flow.

### Checkpoints are replay boundaries

Every checkpoint is a boundary the runner remembers. On the first run, each checkpoint's inputs and output are computed and stored. This recording is what makes replay faithful: when you replay an execution, completed checkpoints return their persisted outputs and execution only re-enters the first checkpoint affected by your change. Everything you didn't touch reproduces exactly, so a rerun with no change is a faithful baseline and any difference you see is your change — not replay noise.

Replay has three override levels:
- `flow_overrides` changes top-level flow inputs.
- `checkpoint_overrides` targets every recorded call with a checkpoint name.
- `invocation_overrides` targets one recorded checkpoint, tool, or model call by invocation ID or call ID.

### Decorator options

| Option | Default | What it controls |
|--------|---------|------------------|
| `retries` | `0` | Automatic retries on checkpoint failure |
| `cache` | `True` | Reuse the persisted output from a previous run when inputs and code match. Set `False` to disable. |
| `type` | `None` | A label for UI visualization (e.g. `"llm_call"`, `"tool_call"`) |
| `runtime` | `None` | Execution runtime: `"inline"` or `"isolated"` |

### Isolated runtime

By default, checkpoints run inline — in the same process/pod as the runner. For checkpoints that run untrusted code, need a different image or resources, or must be strongly isolated from the rest of the run, set `runtime="isolated"` and the runner will place the checkpoint on a separate container/job on the configured stack (Kubernetes, Vertex AI, SageMaker, AzureML). Locally it falls back to inline so dev loops stay fast.

`runtime` controls where a checkpoint runs (same process vs. separate container). `.submit()` controls when — it enables concurrency. The two are independent.

If the active orchestrator does not support isolated steps, the runtime is silently downgraded to inline with a warning.

### Concurrent execution

For independent work that can run in parallel, use `.submit()`. `.submit()` returns a future-like object. Call `.result()` on it to get the checkpoint's return value. This is the primary fan-out pattern in Kitaru. Kitaru also provides `.map()` and `.product()` for batch concurrent execution.

### Return values

Checkpoints return values must be serializable — Kitaru persists them so they can be reused in future executions. Prefer:
- Built-in Python types (`str`, `int`, `float`, `bool`, `list`, `dict`)
- Pydantic models
- JSON-compatible data structures

### Rules to know

- Checkpoints only work inside a flow. Calling a checkpoint outside a `@flow` raises `KitaruContextError`.
- No nested checkpoints. Calling one checkpoint from inside another is not supported and raises `KitaruContextError`.
- `.submit()` requires a running flow. Concurrent submission is only available during flow execution, not during flow compilation.
- `.map()` and `.product()` follow the same rules as `.submit()` — they require a running flow context.

---

## Deployments

A deployment is a versioned, remotely invocable entrypoint for a Kitaru flow. It lets a producer publish a flow once and consumers run it from anywhere by name — without importing the source or owning a long-lived service. Each invocation starts a fresh durable execution from a saved snapshot, so every deployed run is recorded, replayable, and improvable like any other Kitaru flow run.

**The flow source is the recipe, a deployment version is one immutable saved copy of it, and an invocation starts a fresh execution from that copy.**

### How to deploy

You can create deployments from three surfaces:
- CLI: `kitaru deploy path/to/file.py:flow_name`
- Python SDK: `flow_name.deploy(...)`
- MCP: `kitaru_deployments_deploy(target="path/to/file.py:flow_name", ...)`

The CLI also has `kitaru build path/to/file.py:flow_name` for the narrower case where you want to create an immutable deployment version without attaching a route yet.

You can then invoke the deployed flow without the original target path:
- CLI: `kitaru invoke flow_name`
- Python SDK: `flow_name.invoke(...)` or `deployment.invoke(...)`
- MCP: `kitaru_deployments_invoke(flow="flow_name", ...)`

### What gets saved

Deploying a flow creates a Kitaru-managed saved snapshot that Kitaru treats as an immutable deployment version. Kitaru records:
- The public flow name
- An integer version
- Representative deployment-time input values
- Deploy-time image config (when provided)
- The stack context
- Any public routing tags

Deployment-time inputs should be representative values. They let Kitaru prepare the saved deployment snapshot, especially for flows whose shape depends on concrete parameters. Later invocations can override those values by passing new inputs.

### Auto-versioning

Kitaru assigns deployment versions automatically per flow:
- The first deployment of `research_agent` becomes version `1`.
- The next deployment of `research_agent` becomes version `2`.
- Another flow gets its own independent version sequence.

Internally, Kitaru injects the version into the backend snapshot name. Kitaru can scan the existing deployment snapshots for a flow, find the highest `v<N>`, and allocate the next version.

### Tags and routing

Tags are human-readable selectors that point at deployment versions. They are how producers publish a route and consumers invoke it without memorizing version numbers.

There are two tag modes:

| Mode | Meaning | Example use |
|------|---------|-------------|
| Exclusive | The tag can point to only one version at a time. Adding it to a new version moves it away from older versions. | `default`, `stable`, `prod` |
| Shared | The tag can point to multiple versions. Invoking by that tag is only valid when it resolves to one version. | `experiment`, `team-a`, `benchmark` |

The `default` tag is special:
- `default` is reserved by Kitaru.
- `default` is always exclusive, even if you pass `exclusive=False`.
- The first deployment of a flow gets `default` automatically.
- `default` cannot be removed.
- A deployment that still has any exclusive tag cannot be deleted. Move or remove the exclusive tag first.

### Invocation model

`kitaru invoke` is the primary CLI command for deployed flows. If you omit both `--version` and `--tag`, Kitaru tries the implicit `default` route. If the flow has no deployments, Kitaru tells you that directly. If deployments exist but none is currently routed as `default`, invoke with an explicit tag or version, or move `default` with `kitaru flow tag ... --exclusive`.

In Python, `.invoke()` is the remote invocation verb for deployed flows.

### Serverless routing

Invoking a deployment starts a new durable Kitaru execution from a saved version. It does not call a long-lived Python process owned by the producer, and it does not create a separate always-on service for each version. The resulting run records checkpoints exactly like a locally launched flow, so you can replay and diff it later.

The route is just: flow name + tag/version selector.

- The consumer invokes one flow route, e.g. `research_agent` + `stable`.
- Kitaru resolves that route to the saved snapshot for the selected deployment version.
- Kitaru starts a normal execution from that saved snapshot and returns a normal execution handle.

There is no long-lived per-version service and no per-deployment token.

### Authentication

Deployments do not have per-deployment tokens. Access is controlled by the same active Kitaru server connection that the CLI, SDK, and MCP server already use.

For a remote Kitaru server, authenticate once and choose the project you want to work in. For headless environments, configure the same connection with environment variables. For automation, `KITARU_AUTH_TOKEN` should normally be a service-account API key created with `kitaru auth service-accounts create` and `kitaru auth api-keys create`.

After that, `kitaru invoke`, `KitaruClient().deployments.invoke(...)`, and MCP `kitaru_deployments_invoke(...)` all use the active Kitaru server connection. The invocation request does not carry a separate deployment-specific token.

For shell scripts or CI jobs, `kitaru flow deployments curl FLOW` generates a copy-pasteable curl command for the active Kitaru server.

---

## Wait, Input, and Resume

`kitaru.wait()` suspends a running flow until a human, another agent, or an external system provides input. It exists because durable runs let a flow stop and resume without losing state: when execution hits a wait, the server holds the run's checkpoints and the runner can release compute. The execution resumes seconds, hours, or months later when input lands, picking up at the exact wait point with the same state and artifacts. In non-interactive runs the runner polls for input up to its `timeout` (default 600 seconds), then exits.

### Where wait() can be called

`kitaru.wait()` must be called at flow scope. In practice, that means inside the `@flow` function body, before or after checkpoint calls, not inside a `@checkpoint` function.

A wait pauses the whole run. If `wait()` pauses from inside a checkpoint, the run can stop before that checkpoint call has completed cleanly. That can leave things in a confusing state where the run is waiting for input, but the checkpoint call is marked failed.

### Wait parameters

| Parameter | Default | What it does |
|-----------|---------|--------------|
| `name` | Auto-generated | Identifier for this wait point (used when providing input) |
| `question` | `None` | Human-readable prompt shown in the CLI, UI, and MCP |
| `schema` | `None` | Expected type of the input. When `None`, the wait acts as a continue/abort gate returning `None`. |
| `timeout` | `600` | Seconds the runner polls before exiting (not a wait expiration) |
| `metadata` | `None` | Additional key-value data attached to the wait record |

The `timeout` is not a deadline on the wait itself — the wait never expires. It only controls how long the runner process stays alive polling for a response. After timeout, the input can still be provided at any time.

---

## Logging and Metadata

Metadata is the structured data you attach to a run so you can compare runs later. When you diff a baseline against a replay, or measure a cohort, the numbers you read back are the ones you logged here: `cost`, `latency`, `tokens`, `model`. Log it once and it travels with the execution and its checkpoints.

Kitaru has two separate observability channels:

| Channel | What it does | How you use it |
|---------|--------------|----------------|
| Structured metadata | Key-value data attached to a specific execution or checkpoint | `kitaru.log(key=value)` in Python |
| Runtime logs | Execution/checkpoint stdout/stderr retrieval + backend destination configuration | `kitaru executions logs ...`, `KitaruClient.executions.logs(...)`, and `kitaru log-store ...` |

### Attaching metadata with `kitaru.log()`

Call `kitaru.log()` with keyword arguments to attach structured metadata. You can call `kitaru.log()` multiple times — metadata accumulates rather than replacing previous entries.

`kitaru.log()` is scope-sensitive. It automatically detects where it is called and attaches metadata to the right target (execution-level vs. checkpoint-level). Execution-level and checkpoint-level metadata remain separate — they do not mix together.

When you log the same key multiple times in the same scope, the behavior depends on the value type:
- Dictionary: Values are merged (keys from both calls are combined)
- Scalar: The latest value wins

### What values are accepted

Metadata values should be JSON-serializable:
- Strings, numbers, booleans
- Lists and dictionaries
- Nested combinations of the above

Standard keys like `cost`, `tokens`, `latency`, and `model` are common conventions, but you can use any key name.

These are the keys that pay off at replay time. After `flow.replay(exec_id, at="...", flow_overrides={"model": "..."})`, a cross-run diff lines up the metadata from the baseline against the replay, so consistent keys like `cost` and `latency` make the difference your change produced easy to read.

### Runtime logs (separate system)

Retrieve logs with:
- `kitaru executions logs <exec_id>`
- `KitaruClient().executions.logs(exec_id, ...)`
- MCP `get_execution_logs`

Configure the preferred backend destination with `kitaru log-store ...`.

---

## Adapters

Adapters let Kitaru record and replay an agent you built with another framework, without rewriting it. Your framework still runs the agent — it decides how the agent thinks, calls tools, streams, pauses, and resumes — while the adapter wraps the durable seams so each model call, tool call, or graph invocation lands as a checkpoint you can replay later.

That boundary is deliberate. Kitaru records what passes through the seam the framework exposes safely; it does not claim to replay work it never saw. That honesty is what makes a replay faithful: a rerun with no change reproduces the original run, so when you replay again with one input changed, the diff is your change and not replay noise.

### Choose an adapter

| Framework | Adapter object | Replay boundary (finest) |
|-----------|----------------|--------------------------|
| Plain Python functions | `@flow` + `@checkpoint` | Your function boundaries — you choose them |
| PydanticAI agent | `KitaruAgent` | Per model/tool/MCP call by default, or one turn checkpoint |
| OpenAI Agents SDK | `KitaruRunner` | Per call, or one runner-call checkpoint |
| Claude Agent SDK | `KitaruClaudeRunner` | One completed Claude invocation |
| LangGraph | `KitaruGraphRunner` | One graph call, or middleware-wrapped model/tool calls |

Per-call checkpointing is fullest in the PydanticAI (`KitaruAgent`) and OpenAI Agents SDK (`KitaruRunner`) adapters. The Claude Agent SDK adapter currently checkpoints at the invocation boundary, and LangGraph's per-call granularity depends on middleware wrapping the model/tool calls. If call-level replay fidelity is your priority, prefer PydanticAI or OpenAI calls mode.

### What adapters do not promise

Adapters record work that passes through the seam, not work the framework hides inside itself. If a framework makes an internal model call, shell command, browser step, or tool call without exposing it, Kitaru cannot replay that hidden step — it can only save the result that comes back out. Record at the boundary you control, and what you record replays faithfully.

### Migration skills

The `zenml-io/kitaru-skills` package includes migration skills that walk your coding agent through the conservative adapter path. In Claude Code, invoke the skill that matches your current framework:

- `/kitaru:kitaru-pydantic-ai-migration`
- `/kitaru:kitaru-openai-agents-migration`
- `/kitaru:kitaru-langgraph-migration`
- `/kitaru:kitaru-claude-agent-sdk-migration`
- `/kitaru:kitaru-gemini-interactions-migration`

Google ADK support is experimental.

---

## References

- Kitaru docs root: https://docs.zenml.io/kitaru
- Kitaru blog: https://kitaru.ai/blog/
- Kitaru SDK reference: https://sdkdocs.kitaru.ai
- ZenML: https://zenml.io / https://docs.zenml.io
- kitaru-skills repo: https://github.com/zenml-io/kitaru-skills
