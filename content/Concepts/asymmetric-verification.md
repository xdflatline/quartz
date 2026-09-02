---
title: "Asymmetric Verification"
details: "Graph engineering principle that the worker and verifier must have asymmetric objectives: the worker is rewarded for finding the strongest answer; the verifier is rewarded for finding the reason to reject it. Asymmetric verification is the design that turns more candidates into a useful selection pressure rather than noise."
tags:
  - concepts
  - agent
  - orchestration
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Asymmetric Verification

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

A worker should not be rewarded for defending its own answer — that creates confirmation pressure. Instead, give the worker and verifier different objectives. The worker finds the strongest answer; the verifier finds the reason this answer should be rejected. Those are not the same task.

## Core Content

### The Asymmetry

> **Worker:** "Find the strongest answer."
> **Verifier:** "Find the reason this answer should be rejected."

The verifier should have permission to kill output. Otherwise it is decoration.

A useful graph does not just create more candidates. It creates a **selection pressure** that bad candidates must survive.

### Domain Examples

**Research system:**
```
WORKER:
Find evidence supporting or explaining the claim.

VERIFIER:
Try to falsify the claim.
Check the source.
Check the date.
Look for conflicting evidence.
```

**Code:**
```
WORKER:
Implement the change.

VERIFIER:
Try to break it.
Run tests.
Inspect edge cases.
Look for regressions.
```

**Strategy:**
```
WORKER:
Build the recommendation.

VERIFIER:
List conditions under which this recommendation fails.
```

## Key Insights

1. **Same-objective verification is a sham** — a worker defending its own answer creates confirmation bias.
2. **The verifier must have kill permission** — otherwise it is decoration.
3. **Adversarial objectives produce selection pressure** — the value of the verifier is the asymmetry, not the existence.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/builder-reviewer-task-granularity|Builder-Reviewer Task Granularity]] — adjacent role separation
- [[Concepts/verifier-kill-rate|Verifier Kill Rate]] — observability metric for whether the verifier is doing real work
- [[Concepts/agent-epistemic-vigilance-deficit|Agent Epistemic Vigilance Deficit]] — failure mode this mitigates

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
