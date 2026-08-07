---
title: "Darwin Gödel Machine (DGM)"
detail: "Zhang et al. 2025: an LLM-based coding agent that is allowed to modify its own harness codebase. Starts with one coding agent in a pool, iteratively picks a parent weighted by performance/inverse-children, proposes harness edits, evaluates, and keeps only high-fitness candidates."
details: "DGM is harness evolution under a fixed model. The selected parent agent examines its own benchmark evaluation log and proposes improvements to its own harness codebase to generate a new version of the coding agent. Code editing is implemented with two basic tools: bash (args: <bash_command>) and editor (args: view/create/edit <file_path>). New agents are evaluated; only those with sufficiently high performance are added back to the pool. On SWE-bench Verified: 20% → 50%. On Polyglot: 14.2% → 30.7% (Claude 3.5 Sonnet base, simple initial harness). Hyperagents (2026 follow-up) introduces a meta-agent to control the modification strategy."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Darwin Gödel Machine (DGM)

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Architecture Pattern
**Status:** Experimental (SWE-bench Verified and Polyglot evidence)

---

## Overview

**Darwin Gödel Machine (DGM; Zhang et al. 2025)** explicitly targets the evolution of an **editable harness-code repository** with an LLM-based coding agent — the agent is allowed to **modify its own harness**. The name invokes both Darwin (evolution by selection) and Gödel (self-reference, a system modifying itself).

## Core Content

### The Loop

1. Start with one coding agent in the pool
2. In each iteration, pick one parent with probability proportional to its performance and **inversely to the number of children it has**, to modify and branch off to produce new agents
3. The selected parent agent examines its own benchmark evaluation log and proposes improvements to its own harness codebase to generate a new version of the coding agent. Code editing uses two tools: (1) `bash` (args: `<bash_command>`) and (2) `editor` (args: `view/create/edit <file_path>`)
4. New coding agents are evaluated; only those with sufficiently high performance are added back into the pool
5. Repeat steps 2-4 until some stop criterion hits

### The Inverse-Children Trick

DGM's parent-selection rule is: probability ∝ performance / (1 + number_of_children). This explicitly **discourages a single high-scoring agent from dominating the parent pool**. Without it, the population collapses to a single mode; the inverse-children term keeps the search exploring.

### Minimal Tool Set

DGM deliberately uses only two tools: `bash` and `editor`. This is the minimum substrate for the agent to read and edit its own code. The harness around the agent is everything else.

### Results

| Benchmark | Hand-crafted | DGM-discovered |
|-----------|--------------|----------------|
| SWE-bench Verified | ~20% (simple initial harness) | up to 50% |
| Polyglot | 14.2% | 30.7% |

Base LLM: `Claude 3.5 Sonnet`. The initial harness was intentionally simple. DGM-improved agents reach strong results by **editing the harness code itself**, not the underlying model.

### Hyperagents (Follow-up)

**Hyperagents (Zhang et al. 2026)** addresses a gap in DGM: how should the agent decide *what kind* of edit to make? Hyperagents introduces a **meta-agent that controls how to modify existing task agents** to create new ones. The meta-agent learns a modification policy over the population.

### What DGM Does Well

- **Harness evolution, not model evolution** — DGM is harness evolution under a fixed model. The model is the substrate; the harness is the object.
- **Self-referential** — the agent reads its own log and writes a new version of itself. No external oracle.
- **No gradient** — pure selection. Works for code where RL would need a differentiable proxy.

### What DGM Doesn't Solve

- **Reward hacking** — without an external evaluator, DGM can drift toward "easier to evaluate" rather than "better"
- **Long-horizon memory** — the loop forgets its history unless files persist across iterations
- **Safety boundary** — the agent can edit anything in its harness, including safety checks. Hyperagents is one response; AHE's read-only constraints are another (see [[Concepts/agentic-harness-engineering-ahe]])

## Key Insights

1. **DGM is the boldest harness-evolution method** in Weng's survey — the agent edits its own code, not just the prompt or the context.
2. **Parent selection drives the search.** The inverse-children weighting is the single design choice that keeps the population diverse.
3. **Two tools is enough.** `bash` + `editor` covers the full surface; the rest is the harness the agent itself is evolving.
4. **The hard problem is the modification policy, not the modification.** Hyperagents exists because picking *what kind* of edit to make is itself a search problem.

## Related Concepts

- [[Concepts/evolutionary-search-for-harnesses]] — the family DGM belongs to
- [[Concepts/meta-harness-outer-loop]] — the concurrent "harness-for-harnesses" approach
- [[Concepts/agentic-harness-engineering-ahe]] — concurrent work with a stricter observability discipline
- [[Concepts/diversity-collapse-rsi]] — the mode-collapse failure mode DGM mitigates
- [[Concepts/file-system-as-agent-memory]] — the substrate that makes self-editing tractable
- [[Concepts/harness-as-runtime-os-analog]] — the OS analogy; DGM is the OS modifying itself

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Papers: Zhang et al., "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents," arXiv:2505.22954, 2025; Zhang et al., "Hyperagents," arXiv:2603.19461, 2026.
- Related Entities: [[Entities/darwin-godel-machine]], [[Entities/hyperagents]]
