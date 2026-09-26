---
title: "Steering By Altitude Manage By Exception"
details: "Operational pattern where the human sets a roadmap, hands off, and intervenes only by exception — staying at high altitude (light-touch review) and dropping to low altitude (terminal-deep hands-on) only when judgment is required. The level of autonomy becomes a dial."
tags:
  - concept
  - agent
  - agentic-system
  - orchestration
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Steering By Altitude Manage By Exception

**Category:** Operational Pattern
**Status:** Production pattern (OpenRig)

---

## Overview

Once the four primitives (rig, coordination, workflows, workspaces) are in place, the human's job collapses to one thing: **steering**. The operational model is **altitude** — you decide how much to trust the agents on a given task, and you **manage by exception**.

> "You stay up high while things are running just fine. And you drop all the way down into a terminal the moment you need to. So that level of autonomy becomes a dial that you control."

## The altitude dial

```
                ▲
                │  HUMAN VANTAGE POINT
                │
   high altitude │  roadmap / watch / approve / course-correct
                │
                │
                │
   mid altitude │  spot-check spec / proof / queue state
                │
                │
                │
  low altitude  │  live in a terminal, drive an agent directly
                │
                ▼
```

You can be at any altitude on any task. The right altitude depends on:

- **Stakes** — how expensive is a failure?
- **Novelty** — has the agent done this exact thing before?
- **Trust** — calibrated per-agent, per-task-type, from prior performance.

You don't pick one altitude globally; you pick per task and you move up and down as signals demand.

## Manage by exception

This is the key shift. The default state is: **you are not in the loop.** You set the roadmap, the rig runs, the queue carries work, you watch.

You enter the loop only when something needs your judgment — a spec the planner agent wrote looks wrong, a proof is missing, a rate limit blocked a critical path, a feature misaligned with intent.

Exception-driven intervention is the inverse of babysitting. Babysitting = "I'm here, watching every step." Exception management = "I'm here, watching for things that need me."

## The dial analogy

The author calls autonomy a **dial**, not a switch. You can:

- Turn it down to fully manual for sensitive work
- Turn it up to "self-driving" for well-trodden work
- Turn it past self-driving into "growing" (see [[Concepts/recursive-self-improvement-multi-rig-loop]])

The primitives (rig, queue, workflow, workspace) are what make the dial possible at all — without them, the dial is just a yes/no. With them, the dial is a continuous knob.

## Why this is a distinct pattern

It sounds obvious in the abstract ("of course the human should supervise at the right altitude"). The OpenRig contribution is:

1. **Naming it explicitly** so the operational model can be taught.
2. **Tying it to primitives** — without the markdown control plane and the queue, you can't actually stay at high altitude and intervene on demand; you have to be in the loop to know what's happening.
3. **Validating it experimentally** — the author ran the system in fully-closed-loop recursive-self-improvement mode for weeks, demonstrating that high-altitude is genuinely viable, not aspirational.

## Related Concepts

- [[Concepts/recursive-self-improvement-multi-rig-loop]] — turning the dial past self-driving
- [[Concepts/markdown-control-plane-workspace-engineering]] — what makes the high-altitude view legible
- [[Concepts/owner-status-queue-handoff]] — the queue you watch from altitude
- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — autonomy calibration as a harness mechanism (SDD 2026 lineage)

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Composing the software factory"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "Putting them together"
