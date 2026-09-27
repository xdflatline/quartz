---
title: "Compaction Trigger Taxonomy"
details: "Six trigger paths that drive automatic and manual context maintenance in oh-my-pi, with deliberately different semantics for overflow recovery (model retry), incomplete-output recovery (model retry, handoff allowed), threshold maintenance (auto-continue), mid-turn threshold maintenance (no separate continuation), and idle maintenance (no auto-continue). Each trigger routes through compaction.methodOrder with a distinct reason string."
tags:
  - concept
  - context-engineering
  - architecture-pattern
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/github-oh-my-pi-compaction-docs-2026-09-27.md
---

# Compaction Trigger Taxonomy

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated (oh-my-pi reference implementation)

## Overview

A canonical taxonomy of **six distinct trigger paths** for compaction/context maintenance, with deliberately different semantics. Each carries a `reason` string into the auto-maintenance path (`"overflow"`, `"incomplete"`, `"threshold"`, `"idle"`, plus manual `/compact` and `/handoff`) and a `willRetry` flag that controls whether the agent's next provider request is auto-scheduled.

## Core Content

### The six triggers

| # | Trigger | Reason | willRetry | Handoff allowed? | Auto-continue? |
|---|---------|--------|-----------|------------------|----------------|
| 1 | Manual `/compact [instructions]` | n/a (manual) | varies | varies | if abort cut a turn |
| 2 | Same-model assistant error matching context overflow | `overflow` | `true` | **No** (would reuse overflowing input) | yes, scheduled |
| 3 | Same-model assistant message ends `stopReason === "length"` | `incomplete` | `true` | **Yes** (input still usable) | yes, scheduled |
| 4 | Successful turn whose adjusted context exceeds resolved threshold | `threshold` | `false` | Yes, scheduled as post-prompt task | yes, if `autoContinue !== false` |
| 5 | Tool-loop turn crosses threshold before next provider request | `threshold` (mid-turn) | `false` | runs all methods inline | no (core loop owns next request) |
| 6 | `runIdleCompaction()` when not streaming/already compacting | `idle` | `false` | varies | no |

### Overflow recovery — distinctive behavior

- Triggered only when the assistant error is **not older than the latest compaction** (older errors are not context-overflow-shaped).
- The failing assistant error message is **removed from active agent state** before retry.
- Context promotion is tried first: if a configured larger model is available, the agent switches model and retries **without compacting**.
- If promotion fails, walks `compaction.methodOrder` with `reason: "overflow"` and `willRetry: true`. Handoff is **skipped** because its side-request would reuse the overflowing input.
- On success, `agent.continue()` is scheduled.

### Incomplete-output recovery — divergent from overflow

- Triggered when `stopReason === "length"` and the message is not older than the latest compaction.
- Incomplete assistant message is removed from active agent state.
- Context promotion first, then `compaction.methodOrder` with `reason: "incomplete"` and `willRetry: true`.
- **Unlike overflow**, a reachable `handoff` preference may run because the input context is still usable.
- On soft-compaction success, `agent.continue()` is scheduled.

### Threshold maintenance — measured against the budget

- Trigger: successful, non-error assistant message whose adjusted context tokens exceed `resolveThresholdTokens(...)`.
- The measured count comes from `calculateContextTokens(...)`, which **subtracts provider-side orchestration tokens** (billable, but never replayed into the conversation prefix) so auto-compaction and context-promotion thresholds are not inflated by them.
- Mid-turn also checks safe tool-loop boundaries before the next provider request when `compaction.midTurnEnabled !== false`.
- Tool-output pruning can reduce the measured count before threshold comparison.
- Context promotion is tried before post-turn compaction.
- When `handoff` is the next runnable method, post-turn maintenance **schedules a post-prompt task** that generates the handoff document and commits it as a compaction entry; pre-prompt and mid-turn checks run all methods inline to avoid racing the next turn.

### Mid-turn threshold — no separate continuation

- Same trigger condition as threshold maintenance but checked at a tool-loop boundary.
- Maintenance never schedules a separate continuation because the core loop already owns the next provider request — scheduling a continuation would race it.

### Idle maintenance

- Triggered by `runIdleCompaction()` when the agent is not streaming and not already compacting.
- Uses `reason: "idle"` and does not auto-continue afterward.
- Idle shake does not fall back to the next method on insufficient savings — the idle timer rechecks usage before running again.

### Failure-mode messages

| Path | Message |
|------|---------|
| Overflow | `Context overflow recovery failed: ...` |
| Incomplete | `Incomplete response recovery failed: ...` |
| Threshold / idle | `Auto-compaction failed: ...` |

## Key Insights

1. **Triggers are not interchangeable.** Overflow skips handoff; incomplete-output allows it; threshold/idle use different continuation policies. Lumping these into one "auto-compact" path loses the prompt-cache and turn-resume guarantees.
2. **Measured tokens ≠ billed tokens.** `calculateContextTokens` subtracts provider-orchestration tokens that are billable but never replayed into the prefix — this prevents threshold inflation by orchestration overhead.
3. **`willRetry` is the spine.** It determines whether the agent schedules its own `agent.continue()` after a successful compaction, which is what gives manual compaction its "cut and resume" behavior.
4. **Handoff scheduling is a race-avoidance decision.** Only post-turn threshold maintenance schedules handoff as a post-prompt task; pre-prompt and mid-turn run all methods inline to avoid racing the next provider request.

## Related Concepts

- [[Concepts/session-entry-compaction-model]] — what these triggers produce
- [[Concepts/async-speculative-compaction]] — pre-threshold variant of threshold maintenance
- [[Concepts/handoff-document-generation]] — distinct path that the handoff method opens
- [[Concepts/pre-compaction-tool-result-pruning]] — runs before threshold comparison, can defer a trigger

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#triggers