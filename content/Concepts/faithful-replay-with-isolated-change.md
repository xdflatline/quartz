---
title: "Faithful Replay With Isolated Change"
detail: "Re-execute a recorded run from a checkpoint with exactly one input changed, diff the result against a no-change baseline rerun; the baseline reproduces, so the diff is your change, not replay noise."
details: "Faithful replay is the differentiator of record-and-replay runtimes like Kitaru. The mechanic: every checkpoint in a flow has its inputs and output recorded durably. A no-change replay reproduces the original by serving those persisted outputs (the baseline). A second replay with one input overridden (a different model, a different prompt) re-executes only from the first affected checkpoint; everything before reproduces exactly. A diff between baseline and variant isolates the effect of the change. Three override levels exist in Kitaru: flow_overrides (top-level flow inputs), checkpoint_overrides (every recorded call with a checkpoint name), invocation_overrides (one recorded checkpoint, tool, or model call by ID). Faithful replay is distinct from output re-scoring (eval): the real run is re-executed, not its saved outputs compared to new ones."
tags:
  - concepts
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: concept
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Faithful Replay With Isolated Change

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Faithful replay is the ability to re-execute a recorded agent run from any checkpoint such that a no-change rerun reproduces the original exactly, and a one-input-changed rerun isolates the effect of that change. It is the foundation of the run → replay → improve loop and the reason durable execution matters at all for production agents.

## Core Content

### Why a baseline is the prerequisite

If you cannot make a no-change replay reproduce the original, any diff you compute is contaminated by replay noise — the difference between deterministic reproduction and the actual change. A faithful baseline is what lets you trust the diff.

The mechanism: every checkpoint records its inputs and output. On replay, completed checkpoints return their persisted outputs, and execution only re-enters at the first checkpoint affected by an override. This makes "the rest of the run is identical" a property of the runtime, not something the user has to engineer.

### The three override levels

| Level | Targets | Example |
|-------|---------|---------|
| `flow_overrides` | Top-level flow inputs (all calls) | `flow_overrides={"model": "anthropic/claude-opus-4"}` |
| `checkpoint_overrides` | Every recorded call with a given checkpoint name | Change one parameter for every call to a specific checkpoint |
| `invocation_overrides` | One recorded checkpoint, tool, or model call by invocation ID or call ID | Change one specific model call out of many |

Granularity matters: flow-level overrides are coarse but easy; invocation-level overrides are surgical but require knowing which call you want to change. A finer override level means you can replay from a single tool call rather than the whole turn.

### Faithful replay vs. output re-scoring (eval)

A common point of confusion: faithful replay re-executes the real run with one input swapped. An eval re-scores saved outputs against a new judge. They answer different questions — replay tells you how the change altered the run, eval tells you which saved output is better by some external metric. Both are useful; they are not substitutes.

### Pre-conditions for faithful replay

- Checkpoints must record real work — outputs the runtime actually executed, not wrappers around hidden framework internals
- Cache must be consistent — if a checkpoint returns a cached value that did not come from the recorded run, the diff lies
- The harness must expose the seams at which you want to record. If a framework makes internal model/tool calls without exposing them, the adapter cannot replay those hidden steps

## Key Insights

1. The baseline is the product — without a no-change replay that reproduces exactly, no diff is trustworthy
2. Three override granularities (flow / checkpoint / invocation) let you target the change at the right scope
3. Faithful replay is a runtime property, not a per-implementation property — it's what makes "swap one input, see the effect" a primitive instead of a project

## Related Concepts

- [[Concepts/durable-checkpoint-record-and-replay]] — the recording layer that makes replay faithful
- [[Concepts/three-plane-agent-runtime]] — where the runner and execution targets that implement replay live
- [[Concepts/framework-agnostic-runtime-decorators]] — how adapters expose the seam at the right granularity
- [[Entities/kitaru]] — the canonical implementation

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Original: https://docs.zenml.io/kitaru
