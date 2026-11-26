---
title: "Multi-Agent Pattern Selection and Failure Lessons (Kadhar 2026)"
details: "Synthesis of a practitioner article that argues against defaulting to multi-agent designs: a four-question selection ladder (one agent, pipeline, orchestrator, blackboard), the three patterns compared on control, testability and failure mode, and five measured failure lessons from a 117-case weather-pipeline evaluation. The through-line is that the leverage sits in plain code around the agents — handoff checks, hop limits, one budget per request, full message logging, real evaluation — not in the prompts."
tags:
  - research
  - multi-agent
  - orchestration
  - evaluation
created: 2026-11-26
updated: 2026-11-26
type: research
sources:
  - "Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26.md"
---

# Multi-Agent Pattern Selection and Failure Lessons (Kadhar 2026)

**Updated:** 2026-11-26
**Source:** [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]] — Kadharmoideen Fadurudeen, "Building a Multi-Agent System: 3 Patterns, Explained Simply" (kadhar.dev)

---

## Overview

This article is a counterweight to multi-agent enthusiasm, written from two projects the author actually ran: a **single-agent** dinner recommender with three tools and a step cap, and **Stormwise**, a two-stage Claude pipeline for severe weather evaluated on 117 real National Weather Service alert cases.

Two claims organise it:

1. **Most jobs should stay single-agent.** Splitting is justified only by needing different instructions/tools per part, by parallelism, or by wanting independently testable parts — not by architectural ambition.
2. **The failure surface is the wiring, not the reasoning.** Every lesson the author reports is a boundary problem: data arriving from the previous step looking like fact, loops across agents, budget exhaustion on the cases that matter, and a checker that was itself wrong.

This index sits inside the garden's existing multi-agent cluster and is scoped to what it adds: a **selection ladder**, the **blackboard topology** (previously uncovered), and **measured grounding evidence**.

## The selection ladder

The article's decision procedure, in order — stop at the first match:

1. **Can one agent with tools do it?** → use one agent. Stop.
2. **Can you write the steps as a checklist?** → [[Concepts/agent-first-pipeline-architecture|pipeline]].
3. **Do you know the kinds of help needed, but not the details?** → [[Concepts/supervisor-agent-pattern|orchestrator]].
4. **Does the next step depend on what you discover?** → [[Concepts/blackboard-agent-coordination|blackboard]], with strict limits.

The ladder is coarser than the garden's existing [[Concepts/multi-agent-decision-framework|Multi-Agent Decision Framework]], which derives the same "start with one agent" conclusion from token economics (multi-agent costs 3–10× single-agent) and three specific justifications — context pollution, parallelizable search, separable specialization. The two are compatible and worth reading together: the ladder is the engineering shape, the framework is the cost argument. The article's three "split when" conditions map onto them almost exactly.

## The three topologies

| | Pipeline | Orchestrator | Blackboard |
|---|---|---|---|
| **Shape** | fixed sequence, each step → next | lead plans, dispatches, combines | shared workspace, no lead |
| **Who owns the plan** | the design (static) | the lead agent | nobody |
| **Order known** | at design time | at runtime, by the lead | emerges from board state |
| **Easiest to test** | yes — clear input/output per step | moderately — delegation hooks are inspectable | no — the run is the unit |
| **Characteristic failure** | rigidity: backtracking is bolted on until it silently becomes an orchestrator | plan error propagates to every helper | livelock: locally correct agents circle forever |
| **Real-world instance** | Stormwise (alerts → answer) | "deep research" features in Claude/ChatGPT | debugging swarms: hypothesise, gather evidence, attack |

The article's warning about the pipeline is worth keeping: the pattern does not fail loudly. A pipeline that needs occasional backtracking accretes special cases until it *is* an orchestrator without the orchestrator's visibility.

## Failure lessons with numbers

All from Stormwise (117 cases; 69 with an active warning).

- **Bad data launders into fact.** Weather services publish *test* alerts in the live feed. The pipeline consumed some as real warnings and the model believed them. The model was not at fault; the previous stage was, and the naive fix (watchfulness in the prompt) has no mechanism. Control: [[Concepts/handoff-contract-validation|validate format, freshness and sense at every handoff, in code]].
- **The right data beat a clever prompt.** False reassurance during active warnings: **38% (26/69)** without alert access; **45% (31/69)** after adding an instruction to admit it could not see official alerts; **0%** with the alerts in context and a plain prompt. Detail in [[Concepts/grounding-over-honesty-prompting|Grounding Over Honesty Prompting]].
- **Budgets break on the hard cases.** A token budget calibrated on everyday questions failed on complex storm questions — precisely the subset where failure is dangerous. Budgets need a *pre-decided* fallback: a short safe answer, not a truncated one.
- **The checker was wrong.** A pattern-matching scorer for false reassurance missed **53 of 57** real cases and pointed to the opposite conclusion; the author hand-labelled all **342** responses. If an agent checks an agent, the checker needs its own calibration set.
- **Loops and cost.** Loops are the blackboard's default pathology — each agent acts sensibly, the system circles. Cost is the quiet one: the dinner agent had a step limit and never ran away, and was still taken offline because API spend exceeded what a side project justified. More agents means more calls, every time.

## Guardrails that belong on day one

From the article, all of them plain code outside the agents:

1. **Check every handoff** — format, freshness, plausibility.
2. **Limit the hops** — past a bounce cap, stop and ask a person.
3. **One budget per request** — a single counter for the run, plus a pre-decided fallback answer.
4. **Log every inter-agent message** — the trace is the only replay surface.
5. **Test with real cases** — and spot-check automatic scoring by hand.

Items 1–3 and 5 are the same controls the garden's reliability pages arrive at from other directions: see [[Concepts/hitl-approval-gates-for-tool-calls|HITL approval gates]] for the escalation, [[Concepts/idempotency-for-ai-agents|idempotency for AI agents]] for replay safety, and [[Concepts/verification-subagent-pattern|verification subagent]] for the checker role.

## What this source does not establish

- The percentages come from **one system, one evaluator, one model family**, with no published labels, prompts, or code. The direction is credible and matches the grounding literature; the exact rates are illustrative, not benchmarks.
- "Blackboard" is described qualitatively. There is no comparison of blackboard against orchestrator on task success, cost, or latency — only the claim that it is hardest to test.
- The playground on the source page is explicitly **scripted**, not live AI, so it demonstrates mechanics rather than behaviour.
- The selection ladder is a practitioner heuristic, not an experimentally validated decision rule.

## Related Research

- [[Research/anthropic-multiagent-failure-modes-2026-08|Anthropic multi-agent failure modes]] — emergent social failures (conformity, collusion, escalation); this index covers mechanical ones (handoffs, loops, budgets)
- [[Research/claude-multi-agent-and-prompt-engineering-2026|Claude multi-agent and prompt engineering]] — vendor guidance on orchestration
- [[Research/agent-reliability-idempotency|Agent reliability and idempotency]] — the replay/retry side of the same reliability surface
- [[Research/ai-agent-memory-orchestration|AI agent memory and orchestration]] — the memory substrate the patterns run on

## Related Concepts

- [[Concepts/blackboard-agent-coordination|Blackboard Agent Coordination]] — the topology this source adds to the catalogue
- [[Concepts/handoff-contract-validation|Handoff Contract Validation]] — the day-one control, in detail
- [[Concepts/grounding-over-honesty-prompting|Grounding Over Honesty Prompting]] — the measured 38/45/0 result
- [[Concepts/multi-agent-decision-framework|Multi-Agent Decision Framework]] — the cost-based version of "start with one agent"
- [[Concepts/orchestrators-tax|Orchestrator's Tax]] — what the orchestrator topology costs
- [[Concepts/multi-agent-orchestration-patterns|Multi-Agent Orchestration Patterns]] — the earlier HN-derived pattern catalogue
- [[Concepts/coordinator-worker-task-dag-orchestration|Coordinator-worker task-DAG orchestration]] — design-time task graphs
- [[Concepts/multiagent-system-failure-modes|Multiagent System Failure Modes]] — the Anthropic failure taxonomy
- [[Entities/stormwise|Stormwise]] — the evaluated system

## Next Research Directions

- **Replicate the disclaimer-vs-grounding comparison** on a task with an authoritative retrieval source and a hand-labelled unsafe-claim set, to test whether the 38% → 45% inversion holds outside weather.
- **Benchmark blackboard against orchestrator** on an open-ended debugging task, measuring task success, total model calls, and wall-clock time, with a fixed hop cap in both arms.
- **Measure automated false-reassurance scorers** (regex vs LLM judge) against hand labels on the same 342-response corpus shape, reporting recall per scorer.
- **Evaluate freshness predicates as a handoff control** — inject a known-stale record at a stage boundary and measure whether code-level validation catches it at 100%, versus prompt-level instructions.
