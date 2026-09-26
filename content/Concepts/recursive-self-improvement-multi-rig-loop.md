---
title: "Recursive Self-Improvement Multi-Rig Loop"
details: "Operational pattern where multiple specialized rigs (build, product management, dogfood) form a closed feedback loop — dogfood rig feedback routes to PM rig, PM rig writes better specs, build rig ships them — running autonomously for weeks at a stretch."
tags:
  - concept
  - agent
  - agentic-system
  - self-improvement
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Recursive Self-Improvement Multi-Rig Loop

**Category:** Operational Pattern (Autonomy Dial at Maximum)
**Status:** Experimentally demonstrated (OpenRig, weeks-long runs)

---

## Overview

The maximum setting of OpenRig's autonomy dial is **recursive self-improvement (RSA)** — a multi-rig closed loop where the system improves itself. The author ran this on OpenRig itself: a build rig (ships code), a product management rig (writes specs), and a dogfood rig (stress-tests 24/7). Dogfood feedback → PM rig → better specs → build rig → new version → dogfood rig again. The loop closed.

> "It could run this way continuously. And it did so for a few weeks. It was weird. In RSA mode, it wasn't like I was building software anymore, obviously. It was more like I was growing it."

## The three-rig loop

```
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
        ▼                                                     │
   ┌──────────┐    spec.md     ┌──────────────┐               │
   │   PM     │ ─────────────► │    build     │ ───────┐      │
   │   rig    │                │     rig      │        │      │
   └──────────┘                └──────┬───────┘        │      │
        ▲                             │                ▼      │
        │                       new version        ┌──────────┐│
        │ feedback                       ────────► │ dogfood  │┘
        │                                       │   rig     │
        └───────────────────────────────────────│ (24/7)    │
                                                └──────────┘
```

Three rigs, three roles, one closed loop. Each rig is itself a [[Concepts/rig-meta-harness-team-wrapper]] with its own agents, workflows, and queue.

## Why three rigs, not one big rig

- **Separation of concerns.** The PM rig optimizes for spec quality. The build rig optimizes for shipping. The dogfood rig optimizes for finding breakage. Mixing these goals in one agent makes for confused trade-offs.
- **Independent failure modes.** If the dogfood rig finds nothing for a week, the build rig keeps shipping; if the build rig breaks, the PM rig is unaffected. In a monolithic rig, every failure threatens every role.
- **Each rig is itself steerable.** You can put each rig at a different altitude on the dial — the PM rig at high altitude (trust the planner), the dogfood rig at low altitude (you want to see every failure).

## What the source reports

- **Duration.** Ran continuously for a few weeks.
- **Failure mode.** Got stuck on rate limits repeatedly. When limits cleared, it resumed automatically.
- **Author's framing shift.** "It wasn't like I was building software anymore. It was more like I was growing it." — the human role shifts from author to gardener.
- **Subsequent dial-down.** After the experiment, the author dialed it back to mostly self-driving mode, citing the need for "better guardrails in place before I do that in a public project."
- **Empirical result.** The GitHub history "tells the story. It's currently shipping about as fast as it can without getting my Claude account banned."

## Guardrails the author flags as still-needed

- **Rate limit resilience.** Better backoff and graceful pause semantics.
- **Public-project safety.** The RSA run was on OpenRig itself (the author's own project). Doing this on someone else's project without their consent would be a category error.
- **Quality assurance on auto-generated specs.** Without a human reviewer in the loop, spec drift can compound.

## Relationship to other concepts

- [[Concepts/steering-by-altitude-manage-by-exception]] — RSA is the dial turned to maximum; this concept is what that maximum looks like in practice.
- [[Concepts/agent-self-improvement]] — the broader research lineage of self-improving agents.
- [[Concepts/rig-meta-harness-team-wrapper]] — each loop participant is a rig.
- [[Concepts/yaml-workflow-deterministic-rails]] — the loop itself is implemented as workflows + queues.

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Autonomy and recursive self-improvement"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "One more notch"
