---
title: "YAML Workflow Deterministic Rails"
details: "Architecture pattern where a daemon-enforced YAML config file defines the sequence of agent handoffs (e.g., planner → builder → tester) — agents write the workflows themselves, the daemon carries work through the queue, and an optional watchdog wakes agents on a schedule."
tags:
  - concept
  - agent
  - orchestration
  - tooling
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# YAML Workflow Deterministic Rails

**Category:** Orchestration Pattern
**Status:** Production pattern (OpenRig)

---

## Overview

When agents need deterministic handoffs rather than ad-hoc coordination, a **workflow** (a YAML config file) defines the pipeline and the daemon enforces it. The agents themselves author the workflow files. The queue carries the work; the daemon watches the queue and routes each item to the next owner.

The author's framing: "I know you've seen pipelines like this before. What's different here is how simple it is."

## The shape

```yaml
# example workflow config — agents write these themselves
pipeline:
  - id: plan
    owner: planner-agent
    produces: spec.md
  - id: implement
    owner: builder-agent
    consumes: spec.md
  - id: test
    owner: tester-agent
    consumes: implementation
  - id: review
    owner: reviewer-agent
```

```
                 ┌────────┐
                 │ planner│ writes spec
                 └────┬───┘
                      ▼  (queue routes)
                 ┌────────┐
                 │ builder│ implements
                 └────┬───┘
                      ▼
                 ┌────────┐
                 │ tester │ runs tests
                 └────┬───┘
                      ▼
                 ┌────────┐
                 │reviewer│ signs off
                 └────────┘
```

## Three properties

1. **Daemon-enforced, not agent-enforced.** The agents themselves don't have to remember the order. The daemon reads the YAML and routes.
2. **Agents write the workflows.** This is unusual. Most pipelines are operator-authored. Here the planner agent can mint a new workflow on the fly when the project structure demands it.
3. **Paired with a watchdog (`rig watchdog`).** A clock that wakes agents on a schedule. Think Claude Code's `/loop`, but cross-harness — works for both Claude and Codex. Can keep an agent team alive for weeks.

## Why YAML, why the daemon

- **YAML is reviewable.** A pipeline change is a diff, not a code deploy.
- **The daemon is single-tenant.** It runs locally with the rig. No new infra.
- **The queue ([[Concepts/owner-status-queue-handoff]]) is the bus.** Workflow files declare the routing; the queue carries the actual items; the daemon ties them together.

## Trade-offs the source flags

- **Not novel.** Pipelines-as-config is a well-known pattern.
- **Sometimes brittle.** The author is explicit: "It's super simple, and sometimes a bit brittle, but it works."
- **Watchdog + rate limits need guardrails.** When using watchdog to run for weeks, you'll hit Claude/Codex rate limits. The author reports this happened repeatedly; the daemon auto-resumed when limits cleared.

## When to use

- You want the *order* of agent work guaranteed independent of agent memory or chat history.
- You want a human to read the pipeline ("planner → builder → tester") without reading agent prompts.
- You want agents to mint their own sub-pipelines without operator intervention.

## When NOT to use

- Pure chat-style collaboration where ordering doesn't matter.
- Work that requires human-in-the-loop between every step (use direct `rig send` instead).

## Related Concepts

- [[Concepts/owner-status-queue-handoff]] — the queue the workflow routes through
- [[Concepts/rig-meta-harness-team-wrapper]] — the team this workflow runs inside
- [[Concepts/coordinator-worker-task-dag-orchestration]] — broader lineage
- [[Concepts/recursive-self-improvement-multi-rig-loop]] — workflows composed across rigs

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Workflows: deterministic rails"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "Workflows"
