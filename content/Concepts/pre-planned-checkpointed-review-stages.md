---
title: "Pre-Planned Checkpointed Review Stages"
details: "Verification pattern in which the review pipeline — implementation, code review, security review, test generation — is decided in advance as a set of synchronisation checkpoints with acceptance criteria at each stage, and the decision of whether a stage is needed is made dynamically by the agents themselves. The pipeline runs by default rather than by repeated prompting, and hands off to a human only when the result is shippable."
tags:
  - concept
  - agent
  - testing
  - orchestration
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Pre-Planned Checkpointed Review Stages

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Verification / Pipeline Pattern
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

In most agent tooling, verification is something the human has to keep asking for. The agent finishes implementing; the human says "now review it"; the review comes back; the human says "now security review"; the review comes back; the human says "now run the tests." Each of these is a prompt the human must remember to write, and every one that is forgotten is a stage of the pipeline silently skipped.

This pattern makes the review pipeline **pre-planned as a set of synchronisation checkpoints**, each with its own expectations and acceptance criteria, and drives the agents through it automatically. The result is a shippable artifact, at which point control passes to the human.

## The design

| Element | Role |
|---|---|
| Stage list | Decided up front: what the path to production is |
| Checkpoints | Where synchronisation happens; when to check |
| Expectations | What should be complete at each checkpoint |
| Acceptance criteria | What "done" means at each stage |
| Stage applicability | Decided dynamically, by the agents — whether testing is even needed for this change is an agent decision |
| Execution | Default-on, not prompt-triggered |

The dynamic applicability is what distinguishes this from a static pipeline. A static pipeline runs every stage for every job; this one runs the stages that are warranted, decided by the agent that knows what it built.

## Why the pipeline is "synchronisation" rather than "steps"

The stages are not sequential calls to a chain of specialists — they are **synchronisation points** in a parallel swarm. Work that shares a dependency waits at a checkpoint; work that does not, proceeds. This is why the pattern is paired with the graph: the checkpoint state, the in-flight work, and the workflow that must run are all mapped onto the graph, with results committed to the SCM. See [[Concepts/graph-anchored-agent-swarm-coordination]].

## Security as a first-class stage

Security review is not an add-on but a scheduled checkpoint with dedicated agents watching the work. Two distinct catches are named:

1. **Scratch-code leakage.** An issue introduced in a scratch or temporary agent-written artifact, later discarded, but the gap persists into production unless a checkpoint catches it.
2. **Pattern conformance for new surface.** When a feature introduces a new API, the checkpoint verifies it follows existing authentication patterns, load-balancing rules, and the other established core constraints — not for security alone but as housekeeping.

The checkpoint also runs **adversarial testing** — trying to break the system before someone else does — and reports design gaps nobody else saw. The handling rule for a discovered gap is explicit: if it is out of scope, it is **documented**; if it is judged in scope for the job, the agent adjusts the work. See [[Concepts/out-of-scope-finding-policy]].

## Related Concepts

- [[Concepts/graph-anchored-agent-swarm-coordination]]
- [[Concepts/out-of-scope-finding-policy]]
- [[Concepts/harness-enforced-security-assurance]]
- [[Concepts/builder-reviewer-task-granularity]]
- [[Concepts/four-tier-verification-stack]]
- [[Concepts/extraction-based-task-verification]]
- [[Concepts/hitl-approval-gates-for-tool-calls]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
