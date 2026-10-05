---
title: "LifeOS: Observability (Philosophy)"
details: "The agents dashboard — every run and every agent working, live. A kanban of climb states (Traverse, Marking, Ascending, Anchoring, Camped, Cairn) with criteria count on each card; a capability strip; a spotlight panel on the active run."
tags:
  - raw
  - agent
  - observability
source: https://ourlifeos.ai/philosophy/observability/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Observability

**Source:** [https://ourlifeos.ai/philosophy/observability/](https://ourlifeos.ai/philosophy/observability/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Observability

The agents dashboard — every run and every agent working, live.


Fig. 22·Every agent's run in view; pull one forward

An agent you can’t watch is an agent you have to take on faith. LifeOS doesn’t ask for faith: the agents dashboard shows every run and every agent working, live, on one board.


_The agents dashboard: runs on a kanban of climb states, a capability strip up top, and a live spotlight on the active run — its altitude over time and every criterion as it opens and closes._

## What you’re looking at

- **The kanban of the climb.** Every run is a card, and the columns are [the states of a climb](https://ourlifeos.ai/philosophy/hill-climbing): Traverse, Marking, Ascending, Anchoring, Camped, and Cairn for finished work. A run’s card carries its [ISA](https://ourlifeos.ai/philosophy/the-isa) criteria count — `4/8` means four criteria closed on evidence, four to go.

- **The capability strip.** Tool calls, active skills, web activity, running agents, and parallelism across the last hour, six hours, or day — the system’s whole workload in one line.

- **The live spotlight.** The active run gets a full panel: altitude (criteria closed) over time, an activity histogram, and the criteria themselves — open on the left, verified on the right, each with the falsifier that would prove it wrong.


## Why criteria, not logs

Most observability answers “what did the process do?” This board answers a better question: “is the work actually done?” Because every LifeOS run climbs an ISA — a spec whose criteria each name their own test — the dashboard can show progress as verified criteria instead of scrolling log lines. When a card reaches Cairn, that’s not a status someone set. It’s evidence.

## Part of Pulse

The agents dashboard is a view inside [Pulse](https://ourlifeos.ai/philosophy/pulse), the Life Dashboard at `localhost:31337`. Pulse shows the whole life system; this view shows the machines at work inside it.

[Full documentationThe Observability System →](https://docs.ourlifeos.ai/Observability__ObservabilitySystem)
