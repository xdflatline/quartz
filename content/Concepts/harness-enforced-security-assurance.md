---
title: "Harness-Enforced Security Assurance"
details: "Security posture in which the harness and surrounding system — not the model — is the control point for secure code, because model training is dynamic and cannot be steered with a prompt the way a human's learned habits can. The consequence is that security assurance must be built into how every line of generated code is produced, with dedicated review workflows and guardrails, rather than requested in a prompt."
tags:
  - concept
  - harness
  - cybersecurity
  - agent
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Harness-Enforced Security Assurance

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Security / Harness
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

The central claim: **LLMs have increased the pace at which vulnerabilities are found, and drastically increased the pace at which vulnerabilities are introduced.** The asymmetry is structural, not accidental.

- To get a human to write secure code, you do not prompt them. They learn it and retain it.
- To get an LLM to write secure code, you must prompt it — and the prompt is not retained beyond the context.

The labs will keep improving model security posture, but that improvement is **not a controllable lever** for a system built today. Training is dynamic; the design of the harness around the model is not. So assurance has to live in the harness.

## Why prompting cannot be the control

The argument is about optimisation targets, not model capability:

- "Write secure code" is not expressible as a target with a dial. It is not a scalar that can be tuned toward 0.99 the way a latency or cost target can. It is always *write secure*.
- The behaviour that produces insecure code is embedded in the trajectory, not in a missing instruction. Adding "be careful about X" to a prompt does not remove the token sequence that decides to take the shortcut.

Therefore: the control point is the system that *executes*, checks, and gates — the harness.

## What the harness must carry

1. **Dedicated security review agents** as a default stage, watching the work as it is produced rather than after the fact. See [[Concepts/pre-planned-checkpointed-review-stages]].
2. **Security checkpoints** at specific synchronisation points — including the check that a scratch artifact's issue does not survive into production.
3. **Pattern conformance** — a new API must follow existing authentication, load-balancing, and core conventions.
4. **Adversarial testing** — try to break the product before someone else does, and surface design gaps.
5. **A dedicated team and dedicated workflows**, factored into the design of how every line of generated code is built.

## The gating condition

This is not a nice-to-have layer. The stated sequence is: solve security, compliance, guardrails, and code quality — *then* customers get comfortable enough to accept the deeper transformation. Security assurance is the **precondition** for autonomous operation, not a component of it.

The reciprocal claim closes the loop: once the harness enforces security, autonomous systems can also increase the pace at which vulnerabilities are *found and fixed* — not only introduced. The same mechanism runs in both directions.

## Related Concepts

- [[Concepts/pre-planned-checkpointed-review-stages]]
- [[Concepts/deterministic-hook-guardrails]]
- [[Concepts/harness-as-runtime-os-analog]]
- [[Concepts/agentic-harness-engineering-ahe]]
- [[Concepts/cybersecurity]]
- [[Concepts/copyfail-vulnerability]]
- [[Concepts/deterministic-first-architecture]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
