---
title: "Builder-Reviewer Separation at Task Granularity"
details: "Architectural pattern where a single feature workflow spawns four separate subagents — test designer, failure analyzer, verifier, linter — each in its own context, with the implementation agent acting on failure classifications (TEST_ISSUE, IMPL_ISSUE, DOC_ISSUE, UNCLEAR) but not choosing them. UNCLEAR escalates to a human. Circuit breakers cap the loop at three test-fix and two verification cycles before escalation. The separation must live at task level, not PR level, because a single agent session today spans what used to be a full PR."
tags:
  - concept
  - agent
  - multi-agent
created: 2026-08-17
updated: 2026-08-17
type: concept
---

# Builder-Reviewer Separation at Task Granularity

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Standard advice says the agent that wrote the code should not review the code. **Necessary but insufficient** when a single coding session spans implementation, tests, verification, and lint. The same context that decided "this implementation is correct" has every incentive to decide "this test is wrong" — and given the chance, it will. The fix is to enforce builder-reviewer separation **at task granularity**, with the workflow spawning four separate subagents per feature, each in its own reasoning context.

## Core Content

### The Four Subagents Per Feature

The `plan-implementer` skill spawns:

| Subagent | Role | Reasoning Context |
|----------|------|-------------------|
| **Test designer** | Plans test set from spec acceptance criteria + plan's Goals/Design | Isolated from implementation agent |
| **Failure analyzer** | When tests fail, classifies each as TEST_ISSUE / IMPL_ISSUE / DOC_ISSUE / UNCLEAR | Cannot be the impl agent |
| **Verifier** | Confirms implementation matches spec, independent of who wrote it | Cannot be the impl agent |
| **Linter** | Runs lint checks | Non-mutating by design (auto-fix lives under `make fmt`, never `lint`) |

### The Classification Authority

When tests fail:
1. The failure analyzer classifies each failure as `TEST_ISSUE`, `IMPL_ISSUE`, `DOC_ISSUE`, or `UNCLEAR`
2. The implementing agent **acts on the classification but does not get to choose it**
3. `UNCLEAR` is written into the policy and **escalated to a human** instead of being resolved on the spot

This is the structural mechanism that prevents self-rationalization. The implementing agent cannot decide the test is wrong; a different context makes that call.

### Circuit Breakers

The loop has hard caps:
- **Three test-fix cycles**
- **Two verification cycles**
- After that, the task **stops and escalates**

> "It does not get to keep trying forever just because it 'feels' close."

The cap is the point. Without it, a struggling agent will burn cycles "almost working" indefinitely; the cap forces early escalation while the loop is still productive.

### Why PR-Level Separation Is No Longer Enough

> "A single agent session today can be the size of what used to be a full PR a couple of years ago."

The traditional answer (separate author and reviewer at PR open time) assumed the agent session was small enough that one context could plausibly play both roles across different PRs. That assumption fails when the session itself spans implementation, tests, verification, and lint — the agent owns the whole PR, so PR-level separation does not separate anything.

### Shared Rubric

The human reviewer and CodeRabbit both read from the same canonical rubric in `docs/standards/code-review-rubric.md`. The separation is grounded in the workflow, not in a rule that asks anyone to behave.

## Key Insights

1. **Separation must be at task level, not just PR level.** A single agent session today owns what a PR used to own, so PR boundaries no longer cross reasoning contexts.
2. **The implementing agent must not classify its own failures.** A separate failure analyzer makes the call, and `UNCLEAR` is a first-class escalation state — not a fallback.
3. **Circuit breakers are the loop's immune system.** Without hard caps, the agent will burn cycles indefinitely on a misaligned task. Caps force early escalation while the loop is still productive.

## Related Concepts

- [[Concepts/test-design-subagent-isolation]] — specific instance of separation for tests
- [[Concepts/multi-agent-orchestration-patterns]] — the broader orchestrator/worker pattern
- [[Concepts/coordinator-worker-task-dag-orchestration]] — DAG-based workflows
- [[Concepts/hitl-approval-gates-for-tool-calls]] — `UNCLEAR` is a HITL gate at the failure-classification level

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering