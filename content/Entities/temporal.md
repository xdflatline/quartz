---
title: "Temporal"
details: "Durable Execution platform founded in 2019 by Maxim Fateev and Samar Abbas (creators of the Cadence workflow language at Uber). Provides a workflow orchestration engine where developer code runs as a Workflow (deterministic, replayable) that schedules Activities (side-effecting, retried). Replay-based recovery, event history as source of truth, native timers of arbitrary length. Self-hosted or Temporal Cloud (managed). The platform that named and defined the term \"Durable Execution\" in its 2025/2026 blog series."
tags:
  - entity
  - runtime
  - orchestration
  - durable-execution
created: 2026-09-10
updated: 2026-09-10
type: entity
sources:
  - ".Raw/temporal-what-is-durable-execution-2026-09-10.md"
---

# Temporal

**Source:** Temporal Blog ([[Raw/temporal-what-is-durable-execution-2026-09-10]])

---

## Overview

Temporal is a Durable Execution platform: a runtime that runs long-lived workflows with automatic crash recovery, built-in timers of arbitrary length, and replay-based state reconstruction. Founded in 2019 by Maxim Fateev and Samar Abbas, both formerly of Uber where they created the Cadence workflow language. Temporal is the company and platform that coined the term **Durable Execution** as a category and published the canonical definition in the May 2026 blog post "The definitive guide to Durable Execution" by Tom Wheeler.

## The Two Primitives

Temporal's programming model has two distinct primitives:

- **Workflow** — deterministic, replayable code. The application logic, written as a regular function in a Temporal SDK (Go, Java, TypeScript, Python, .NET, Rust, PHP). Side effects are not performed directly inside a Workflow; instead, the Workflow **schedules** Activities.
- **Activity** — non-deterministic, side-effecting code. The actual work: HTTP calls, database writes, message sends. Retried on failure; result recorded so the Workflow never has to call it twice for the same logical step.

The separation is what makes **replay** possible: when a Workflow resumes after a crash, the runtime replays the Workflow code from the beginning, but each completed Activity returns its **recorded result** instead of re-executing. The Workflow re-derives its state deterministically and continues.

## What Temporal Provides

- **Crash-proof execution** — workflow resumes from reconstructed state on any failure
- **Arbitrary-length timers** — `sleep(Time.days(180))` suspends without holding a process
- **Automatic state preservation** — workflow variables durable across crashes; no manual save/load
- **Hardware agnosticism** — runs on commodity VMs/containers, cloud-native
- **Activity retries with policies** — exponential backoff, max attempts, non-retryable error types
- **Signals and Queries** — external code can inject events (Signal) or read state (Query) without resuming execution
- **Versions and ContinueAsNew** — workflow code can evolve; long-running workflows can be partitioned into chunks via `ContinueAsNew`

## Deployment

- **Self-hosted** — Temporal OSS server, deployable on any Kubernetes cluster or VM set; backed by a relational database (PostgreSQL or MySQL) and an optional visibility store
- **Temporal Cloud** — managed SaaS offering; same API, no operational burden

## History

- **2015–2017** — Cadence developed at Uber by Fateev and Abbas to replace brittle ad-hoc stateful code paths
- **2019** — Temporal Technologies founded; Cadence rewritten as Temporal
- **2026-05-06** — Tom Wheeler publishes "The definitive guide to Durable Execution," formalizing the four-characteristic definition

## Related Concepts

- [[Concepts/durable-execution]] — the umbrella pattern Temporal defined
- [[Concepts/hardware-vs-software-fault-tolerance]] — characteristic #4 of the pattern
- [[Concepts/durable-checkpoint-record-and-replay]] — Kitaru's adjacent realization
- [[Concepts/graph-based-workflow-engine]] — Mastra's adjacent realization (not durable by default)
- [[Concepts/durable-actor-session-sleep]] — AgentOS's adjacent realization
- [[Concepts/coordinator-worker-task-dag-orchestration]] — orchestration topology Temporal hosts

## References

- Raw Article: [[Raw/temporal-what-is-durable-execution-2026-09-10]]
- Original: https://temporal.io/blog/what-is-durable-execution
- Documentation: https://docs.temporal.io/
- Code: https://github.com/temporalio
- Samples: https://learn.temporal.io/examples
- Wheeler's Replay '25 talk: https://temporal.io/resources/on-demand/durable-execution-this-changes-everything
