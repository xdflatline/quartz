---
title: "Durable Checkpoint Record and Replay"
detail: "Every unit of work in a flow records its inputs and output durably; that recording is the substrate of resume, retry, replay, and cross-run diff."
details: "A durable checkpoint is a unit of work inside a flow whose inputs and output are recorded durably, such that the runtime can later return those outputs without re-executing the work. Checkpoints are the contract between the runner (durable control flow: order, retry, replay, resume, wait) and the execution target (inline process, isolated container, sandbox, external tool). Decorated with @checkpoint in Kitaru; executed sequentially by default with .submit()/.map()/.product() for concurrent fan-out. A failed checkpoint is persisted as a typed artifact — durable context that the runner, the agent loop, a human, or a retry policy can reason about. This is what makes 'failures become data' in agent-native error handling: retry the same input, replay with one input overridden, replay with modified code, feed the error back to the agent, or wait for a human correction."
tags:
  - concepts
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: concept
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Durable Checkpoint Record and Replay

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

A durable checkpoint is a unit of work whose inputs and output are recorded durably so the runtime can serve those outputs later without re-executing the work. In Kitaru this is a function decorated with `@checkpoint`, called from inside a `@flow`. The recording is what makes resume, retry, faithful replay, and cross-run diff possible — without it, those are properties the user has to engineer case by case.

## Core Content

### The contract

The checkpoint is the seam between the runner and the execution target. The runner owns durable control flow (order, retry, replay, resume, wait). The execution target does the work. The checkpoint is the recorded boundary they agree on.

### The decorator

```python
@checkpoint
def research(topic: str) -> str:
    return kitaru.llm(f"Summarize {topic} in two sentences.")
```

Checkpoints compose inside a flow:

```python
@flow
def research_agent(topic: str) -> str:
    summary = research(topic)
    return draft_report(summary)
```

Checkpoints execute sequentially by default. For fan-out, use `.submit()` to get a runtime future, or `.map()` / `.product()` for batch concurrent execution. The future's `.result()` blocks until the value is available.

### Decorator options

| Option | Default | What it controls |
|--------|---------|------------------|
| `retries` | `0` | Automatic retries on failure |
| `cache` | `True` | Reuse persisted output from a previous run when inputs and code match |
| `type` | `None` | UI label (e.g. `"llm_call"`, `"tool_call"`) |
| `runtime` | `None` | `"inline"` or `"isolated"` (separate container on the stack) |

`cache=True` is what makes replay cheap: a no-change replay serves recorded outputs instead of re-executing expensive work. The runtime setting is independent of concurrency — `.submit()` controls when, `runtime` controls where.

### Failed checkpoints are durable context

In a classical pipeline, a failed step is a crash. In a durable-checkpoint runtime, a failed checkpoint is recorded as a typed artifact. Downstream consumers have real options:

- **Retry the same checkpoint** with the same input (per-checkpoint `retries`)
- **Replay** the run from a checkpoint with one input overridden (corrected document id, different model)
- **Replay with modified code** (new retrieval strategy)
- **Feed the error back** into the agent loop for self-correction
- **Wait for a human** via `kitaru.wait()` and resume

This is what "agent-native error handling" means: failures become data, durable state survives them, the same recorded run can be re-executed with one thing changed.

### Rules

- Checkpoints only work inside a flow (`KitaruContextError` otherwise)
- No nested checkpoints (`KitaruContextError`)
- `.submit()` / `.map()` / `.product()` require a running flow context
- Return values must be serializable (built-in types, Pydantic models, JSON-compatible)

## Key Insights

1. Recording is the enabler; replay and resume are what you do with the recording
2. A failed checkpoint being durable is more useful than it sounds — it converts a crash into a typed input to the next retry / replay / human-in-the-loop decision
3. Cache + replay compose: with `cache=True`, a no-change replay is essentially free, which is what makes "baseline then variant" feasible
4. The decorator options trade off independently: retries (how many), cache (whether to reuse), type (UI label), runtime (where it runs)

## Related Concepts

- [[Concepts/faithful-replay-with-isolated-change]] — what the recording enables
- [[Concepts/three-plane-agent-runtime]] — where the runner and execution target live
- [[Concepts/framework-agnostic-runtime-decorators]] — how `@checkpoint` stays harness-agnostic
- [[Concepts/agent-stack-layers]] — how this fits in the broader stack

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Original: https://docs.zenml.io/kitaru
