---
title: "Graph-Based Workflow Engine"

details: "A workflow engine that treats multi-step processes as a directed graph of typed steps. Each step has input/output schemas (Standard JSON Schema), a state schema for cross-step shared mutable state, and a control-flow API (.then for sequential, .parallel for concurrent fan-out, .branch for conditional routing, .map for schema transformation between mismatched steps). The engine persists run state to storage, supports suspension/resumption for human-in-the-loop, and can stream step results. Mastra's createStep/createWorkflow is the canonical implementation; LangGraph's StateGraph is the Python equivalent."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Graph-Based Workflow Engine

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A workflow engine that treats multi-step processes as a **directed graph of typed steps**, composed through explicit control-flow primitives, with schema-validated data flow and persistent execution state. The pattern is the canonical "predetermined multi-step" counterpart to free-form agentic loops — you declare the step graph; the engine handles orchestration, parallelism, suspension, and resumption.

## Core Content

### The Two Primitives

1. **Step (atomic unit)** — a typed function with `inputSchema`, `outputSchema`, optional `stateSchema`, and an `execute()` body
2. **Workflow (composer)** — a chain/branch/parallel of steps, finalized with `.commit()`

### Control-Flow Composition

| Primitive | Effect | Data Flow |
|-----------|--------|-----------|
| `.then(step)` | Sequential execution | Previous step's `outputSchema` → next step's `inputSchema` |
| `.parallel([step1, step2])` | Concurrent fan-out | Next step receives object keyed by each parallel step's `id` |
| `.branch([condition, step]...)` | Conditional routing | Output keyed by the executed branch's step `id`; conditions evaluated in order |
| `.map(fn)` | Inline data transformation | Reshape output of one step to match next step's `inputSchema` when schemas diverge |
| `.commit()` | Finalize the workflow graph | Required terminal call |

### Schema Constraints

- **First step's `inputSchema` must match the workflow's `inputSchema`**
- **Final step's `outputSchema` must match the workflow's `outputSchema`**
- **Adjacent step schemas must align** — use `.map()` when they don't

### State Schema (Cross-Step Mutable State)

```ts
const step1 = createStep({
  inputSchema: z.object({ message: z.string() }),
  outputSchema: z.object({ formatted: z.string() }),
  stateSchema: z.object({ counter: z.number() }),
  execute: async ({ inputData, state, setState }) => {
    setState({ ...state, counter: state.counter + 1 })
    return { formatted: inputData.message.toUpperCase() }
  },
})
```

`state` and `setState` let steps share values without threading them through every `inputSchema`/`outputSchema`. State persists across `suspend`/`resume`.

### Suspension and Resumption

The engine **persists run state to a storage backend** at each step boundary. A workflow can be suspended indefinitely (e.g., awaiting human approval) and resumed later with the same execution context. This is the substrate for human-in-the-loop patterns.

### Workflows as Steps (Nesting)

Workflows are themselves steps: a child workflow exposes `inputSchema` and `outputSchema` and can be referenced as a node in a parent workflow. `cloneWorkflow()` creates an independent copy under a new ID for separate observability tracking.

### Failure Semantics in `.parallel()`

**If any parallel step throws, the entire parallel block fails.** Recommended pattern: handle errors inside the step with `try/catch` and return typed results (e.g., `{ brief: string | null, failed: boolean }`) that downstream steps filter.

## Implementation Reference (Mastra)

```ts
import { createStep, createWorkflow } from '@mastra/core/workflows'
import { z } from 'zod'

const step1 = createStep({
  id: 'step-1',
  inputSchema: z.object({ message: z.string() }),
  outputSchema: z.object({ formatted: z.string() }),
  execute: async ({ inputData }) => ({ formatted: inputData.message.toUpperCase() }),
})

export const wf = createWorkflow({
  id: 'test-wf',
  inputSchema: z.object({ message: z.string() }),
  outputSchema: z.object({ output: z.string() }),
})
  .then(step1)
  .commit()
```

Alternative runtime: deploy to a managed workflow runner (e.g., Inngest) for step memoization, automatic retries, and real-time monitoring.

## Key Insights

1. **Schema-validated composition is the API contract** — adjacent steps must align, forcing explicit data flow decisions rather than implicit object passing.
2. **State is orthogonal to input/output** — `stateSchema` lets you share cross-step values without polluting the per-step contract.
3. **Persistent run state enables human-in-the-loop** — suspend/resume is a storage feature, not a runtime feature.
4. **Workflows nest as steps** — hierarchical composition is first-class, not an afterthought.
5. **Parallel failure is whole-block** — design for partial success with typed nullable results, not exception throwing.

## Related Concepts

- [[agent-composition-tree-mastra]] — How workflows slot into the broader Mastra composition tree
- [[multi-agent-orchestration-patterns]] — Workflows vs. agentic loops
- [[supervisor-agent-pattern]] — Alternative multi-step coordination via subagent delegation
- [[typed-tool-creation]] — The tool counterpart of the step contract
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs/workflows/overview
