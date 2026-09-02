---
title: "Graph Spec Template"
details: "Graph engineering template for describing a multi-agent system before writing code: GOAL, INPUT STATE, PARALLEL WORK, EDGE DATA, REDUCER, VERIFICATION, FAILURE POLICY, BUDGET, HUMAN GATE, OUTPUT. The spec is more valuable than twenty prompts because prompts optimize nodes; the spec optimizes the system."
tags:
  - concepts
  - agent
  - orchestration
  - protocol
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Graph Spec Template

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

Before writing any code or prompts, describe the multi-agent system as a spec. The article provides a 10-field template that is paste-compatible with most agent frameworks. The spec is more valuable than twenty prompts because **prompts optimize nodes; the spec optimizes the system**.

## Core Content

### The Template

```
GOAL:
What must exist at the end?

INPUT STATE:
What structured data enters the graph?

PARALLEL WORK:
Which tasks are truly independent?

EDGE DATA:
What exact information crosses each dependency?

REDUCER:
What can be normalized, deduplicated, ranked, or filtered with code?

VERIFICATION:
What independent test can reject weak output?

FAILURE POLICY:
What retries?
What fallback?
What can fail without killing the run?

BUDGET:
Maximum agents?
Maximum tokens/cost?
Maximum wall-clock time?

HUMAN GATE:
Which irreversible actions require approval?

OUTPUT:
What exact schema or artifact is returned?
```

### Why This Beats Writing Prompts First

> Because prompts optimize nodes.
> The spec optimizes the **system**.

You can write twenty brilliant node prompts and still ship a graph that fails on the wrong axis — too wide, no verification, no failure policy, no human gate. The spec surfaces those decisions before you commit to any of them.

## Key Insights

1. **Spec first, prompts second** — the order of operations is part of the discipline.
2. **The 10 fields cover the failure modes** — every principle in graph engineering has a corresponding spec field.
3. **Framework-portable** — the template is intentionally minimal so it can be implemented in Mastra, LangGraph, Kitaru, or any other runtime.

## Spec Field → Principle Mapping

| Field | Maps to Principle |
|-------|-------------------|
| INPUT STATE | 2. Structured Graph State |
| PARALLEL WORK | 1, 3. Order vs Dependency / Dependency Test |
| EDGE DATA | 3. Dependency Test for Edges |
| REDUCER | 6. Deterministic Reduce Before Synthesis |
| VERIFICATION | 7. Asymmetric Verification |
| FAILURE POLICY | 8. Failure Domain Policy |
| BUDGET | 4. Parallelism Width Budget |
| HUMAN GATE | 9. Human Approval as a Graph Edge |
| OUTPUT | 10, 13. Frozen Constraints / Spec |
| GOAL | 12, 14. Shape / When Not to Graph |

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/graph-shape-catalog|Five Graph Shapes]] — implicit in the spec (which shape is this)
- [[Concepts/standard-json-schema-tool-contracts|Standard JSON Schema Tool Contracts]] — the OUTPUT field needs a schema

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
