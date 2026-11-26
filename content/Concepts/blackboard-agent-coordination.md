---
title: "Blackboard Agent Coordination"
details: "Coordination pattern where agents share one mutable workspace instead of a call graph: no lead agent owns the plan, each agent reads what is on the board, writes what it knows, and contributes when it has something useful. Strong fit when the next step cannot be known in advance (debugging, open-ended investigation). Weak fit for testability — nobody owns the plan and loops are the default failure mode, so it needs hop limits and a terminating condition."
tags:
  - concept
  - multi-agent
  - orchestration
  - architecture-pattern
created: 2026-11-26
updated: 2026-11-26
type: concept
sources:
  - "Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26.md"
---

# Blackboard Agent Coordination

**Source:** [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]] — Kadharmoideen Fadurudeen, "Building a Multi-Agent System: 3 Patterns, Explained Simply"
**Category:** Architecture Pattern
**Status:** Proposed best practice — the pattern is old (classic blackboard expert systems), but its use with LLM agents is characterized by practitioner experience rather than benchmarks

---

## Overview

A blackboard system has **one shared, mutable workspace** and a set of agents that are not wired to each other. Each agent reads the current state of the board, decides whether it can contribute, and writes back. There is no lead agent, no fixed order, and no fixed hand-off graph: the structure of the run is emergent, decided at runtime by what appears on the board.

The contrast with the other two common topologies is the point:

| Topology | Control | Data path | Order determined by |
|---|---|---|---|
| **Pipeline** | none (implicit in wiring) | each step → next step | design time |
| **Orchestrator** | one lead agent | helpers ↔ lead only | lead agent at runtime |
| **Blackboard** | none (implicit in state) | every agent ↔ shared board | whatever the board says |

In the source's kitchen analogy: pipeline is an assembly line, orchestrator is a head chef calling orders, blackboard is a whiteboard in the middle of the kitchen that anyone can read and add to.

## Core Content

### Mechanics

1. A request seeds the board (the initial goal, plus any known facts).
2. An agent inspects the board, decides whether it has a contribution, and appends or revises an entry.
3. The loop repeats — agents may run in parallel, may trigger each other, or may act as critics of existing entries.
4. Termination is a property of the board (goal satisfied, contradiction resolved, budget exhausted), not of a scripted sequence.

The source's worked example — a dinner request — has weather, place-search, food-idea and critic agents writing to a board that accumulates facts like "rain, 26 °C", "3 places nearby, one closes soon", "try vada and tea". A critic rounds it out by attacking what is written rather than producing anything new.

### When it is the right pattern

- **The next step depends on what you discover.** The canonical case is debugging: one agent proposes a cause, another looks for evidence, a third pokes holes in it, and what happens next is a function of what they find. The same shape applies to incident triage and open-ended research where the question itself evolves.
- No participant can know the steps in advance, and a checklist would be fiction.
- You want independent, adversarial contributions rather than a single planner's decomposition.

### Why it is the hardest pattern to run

- **Nobody owns the plan.** With a pipeline the sequence is auditable; with an orchestrator the lead's plan is a single artifact to review. On a blackboard the "plan" is the emergent trace, so failures are diagnosed after the fact from logs.
- **Loops are the default failure.** Two agents can each behave sensibly — A asks B for a missing fact, B asks A — and the system circles indefinitely. The source demonstrates exactly this in its playground by allowing agents to hand work back.
- **Testability is poor.** There is no fixed input/output boundary per step to unit-test; the observable is the whole run. You end up evaluating traces, not stages.
- **Board quality is a shared resource.** A wrong entry written early is inherited by every later agent unless a critic explicitly removes it — the same "arrives looking like fact" problem as any handoff, but with more readers.

### Practical guardrails

- **Strict, enforced limits** on total hops, wall-clock time, and model calls per request; blackboard is described as needing these more than the other patterns.
- A **terminating condition on the board** — an explicit "answer ready" marker written by a designated role — checked in code between rounds.
- A **critic or verifier role** with authority to strike entries, not just append.
- **Full message logging.** Because there is no plan artifact, the trace is the only debugging surface.

## Key Insights

1. Blackboard trades structural control for runtime flexibility; it is the right answer to "we cannot know the steps in advance" and the wrong answer to "we want this to be testable".
2. The absence of a lead removes a single point of planning failure but also removes the artifact you would otherwise review and test against.
3. Loops in a blackboard are not misbehaviour — every individual agent can be locally correct while the system as a whole diverges.
4. Choose it last, and only with strict limits: it is the pattern most likely to convert a clear request into an expensive, unowned investigation.

## Related Concepts

- [[Concepts/multi-agent-orchestration-patterns|Multi-Agent Orchestration Patterns]] — the garden's HN-derived catalogue of coordination topologies; blackboard is the decentralized case it does not cover
- [[Concepts/supervisor-agent-pattern|Supervisor Agent Pattern]] — the opposite choice: one supervisor owns the loop and subagents are tools
- [[Concepts/orchestrators-tax|Orchestrator's Tax]] — what the lead-based alternative costs; blackboard avoids the tax but pays in control
- [[Concepts/coordinator-worker-task-dag-orchestration|Coordinator-worker task-DAG orchestration]] — design-time task graph, the structural opposite of emergent ordering
- [[Concepts/handoff-contract-validation|Handoff Contract Validation]] — on a blackboard every board write is a handoff to every future reader, so the validation burden is higher, not lower
- [[Concepts/verification-subagent-pattern|Verification Subagent Pattern]] — the critic role, implemented explicitly

## References

- Raw Article: [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]]
- Original: https://kadhar.dev/blog/multi-agent-systems-from-scratch
