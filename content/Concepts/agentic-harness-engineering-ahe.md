---
title: "Agentic Harness Engineering (AHE) with Observability Pillars"
detail: "Lin et al. 2026: a closed loop for harness evolution with three observability pillars — component (every editable component has a file-system representation), experience (per-task analysis reports aggregated into a benchmark overview), and decision (every edit is a falsifiable file-level claim with a manifesto entry)."
details: "AHE sees the bottleneck of harness evolution as observability: when a rollout fails, you need to know which component is responsible; every edit should be grounded by evidence. The 7 editable harness components: system prompt, tool description, tool implementation, middleware, skill, sub-agent configuration, long-term memory. Two hard constraints: (1) edits are only applied to the harness workspace — the runs directory, tracer, verifier, and LLM config are read-only, disabling a set of reward hacking (disabling the verifier, swapping the model, raising the reasoning budget); (2) edits are evidence-driven with a manifesto entry: failure evidence name, inferred root cause, targeted fix, predicted impact. On Terminal-Bench-2, AHE beat human-designed harnesses (OpenCode, Terminus-2, Codex) except for the Hard tier; the frozen evolved harness transfers to SWE-bench-verified, indicating it encodes engineering experience rather than benchmark-specific optimization."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Agentic Harness Engineering (AHE) with Observability Pillars

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Architecture Pattern
**Status:** Active research area (arXiv 2026)

---

## Overview

**Agentic Harness Engineering (AHE; Lin et al. 2026)** frames the bottleneck of harness evolution as **observability** — when a rollout fails, you need to know which component is responsible; every edit should be grounded by evidence. AHE creates a closed loop with **three observability pillars** and **two hard constraints** that together prevent reward hacking while still letting the loop improve the harness.

## Core Content

### The Three Observability Pillars

#### 1. Component Observability

Every editable harness component has a **representation in the file system** so the action space is explicit and traceable.

The seven harness components AHE identifies:

| # | Component | What it is |
|---|-----------|------------|
| 1 | System prompt | The model-facing instructions |
| 2 | Tool description | Tool spec and parameter docs |
| 3 | Tool implementation | The function bodies behind the tool calls |
| 4 | Middleware | Pre/post hooks around tool calls |
| 5 | Skill | Reusable sub-procedure (see [[Concepts/on-demand-skills-catalog-pattern]]) |
| 6 | Sub-agent configuration | Tool allow-list, system prompt, model selection for a sub-agent |
| 7 | Long-term memory | Persistent state across sessions (see [[Concepts/file-system-as-agent-memory]]) |

Each failure pattern is mapped to **one** component so the edit can be targeted.

#### 2. Experience Observability

Analyze and summarize a large amount of raw trajectories into a hierarchy of evidence and failure patterns.

- Each harness generates $k$ rollouts
- An "**Agent debugger**" analyzes the trajectories (each stored in one file) and generates per-task analysis reports on root cause
- All per-task reports are aggregated into a **benchmark overview** for the next step
- Raw traces can still be accessed if needed
- This **layered access** structure is more token-efficient than re-reading every trace

#### 3. Decision Observability

Every edit is paired with a **prediction for the next round** to validate.

- An "**Evolve agent**" reads the repo, decides which component to edit, then produces the edit and the reasoning behind it
- Every edit is a **file-level, falsifiable claim** — verifiable in the next round

### The Two Hard Constraints

These are what make AHE not a free-for-all:

1. **Workspace isolation** — edits are only applied to the **harness workspace**. The runs directory, tracer, verifier, and LLM configuration are **read-only**. This disables a set of reward hacking (disabling the verifier, swapping the model, raising the reasoning budget) and keeps every recorded gain attributable to harness edits.
2. **Evidence-driven edits** — every edit has a **manifesto entry**:
   - The failure evidence's name
   - The inferred root cause
   - The targeted fix
   - A predicted impact (expected fixes + at-risk regressions)

The manifesto entry is the audit trail. If the edit doesn't deliver its predicted impact, the failure is in the prediction, not the loop.

### Results

On Terminal-Bench-2, AHE achieved better than human-designed harnesses (**OpenCode, Terminus-2, Codex**) except for the Hard tier and a few other self-evolve baselines (ACE, TF-GRPO).

The key cross-benchmark result: the **same frozen harness, without further evolving, transfers to SWE-bench-verified**. This indicates the evolved harness encodes **engineering experience** rather than benchmark-specific optimization.

## Key Insights

1. **Observability is the bottleneck, not optimization.** The hard part of harness evolution is knowing *why* a rollout failed, not the search algorithm.
2. **The 7-component decomposition is a useful mental model.** Every edit should target one of: prompt, tool, middleware, skill, sub-agent config, memory — and the mapping should be auditable.
3. **Workspace isolation disables reward hacking.** Making the runs directory, tracer, verifier, and LLM config read-only is a structural guarantee that gains are real.
4. **The manifesto entry is the prediction interface.** Each edit is a falsifiable claim with a predicted impact — this is the loop that lets AHE be empirically validated.
5. **The harness is engineering experience.** Cross-benchmark transfer is the evidence that the loop is encoding something general, not overfitting.

## Related Concepts

- [[Concepts/self-harness-propose-evaluate-accept]] — sibling approach with regression tests instead of manifesto entries
- [[Concepts/darwin-godel-machine]] — the unbounded alternative
- [[Concepts/meta-harness-outer-loop]] — the harness-for-harnesses approach without the observability discipline
- [[Concepts/reward-hacking-rsi]] — the failure mode AHE's read-only constraints address
- [[Concepts/evidence-driven-harness-edits]] — the manifesto entry pattern
- [[Concepts/observational-memory-pattern]] — adjacent observability framing

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Paper: Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv:2604.25850, 2026.
