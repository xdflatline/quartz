---
title: "Generalized Hill Climbing — Step-by-Step Gap Closing"
details: "An architectural pattern for reaching any goal: from wherever you are, find the move that closes the most gap, take it, then look again. The same algorithm works on a bug, a book chapter, a career pivot, or an AI agent's next action — the shape of the work is always 'one small checked step toward a written target.' The full climb runs in phases; a quick lookup finishes in seconds, a hard cross-system design takes hours. Used as the underlying loop in LifeOS's The Algorithm and as the philosophical frame behind Miessler's writing on personal AI."
tags:
  - concept
  - architecture-pattern
  - agent
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-hill-climbing-2026-10-05]]"
---

# Generalized Hill Climbing — Step-by-Step Gap Closing

**Source:** [[Raw/lifeos-philosophy-hill-climbing-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Production-validated (underlies LifeOS The Algorithm)

## Overview

Hill climbing frames every goal as a hill with the agent partway up. The next good move is the step that takes it higher. The system does exactly that, over and over, on any problem where the goal can be written down and the steps can be checked.

The generalization is the point: the same algorithm works regardless of domain. Bug chasing, book writing, career planning, AI agent task execution — the shape of the work is the same. The system doesn't need a different procedure for every kind of goal; it needs one procedure it can apply repeatedly.

## Why hill climbing is honest at every point

A single step is small enough to check. You can look at one move and say whether it took you higher or not. That makes the climb verifiable at every point, not only at the end when it's too late to fix. The default failure mode in big goals is the same: you can't see the whole hill at once, so you freeze, or you commit to a plan and it breaks the moment it meets reality. Hill climbing replaces "the whole plan" with "the next step."

A worked climb"get the newsletter out, one move at a time"

- ✓ Pick the week's one throughline from your notes — higher
- ✓ Draft the three sections around it — higher
- ✓ Cut it to the length people actually read — higher
- ○ Next move: line up the links and ship — the step in front of you

You never see the whole hill. The system holds the shape of the goal and hands you the one step that's next — small enough to actually take.

## How the climb compounds

The steps get better as you go. **Memory** compounds, so each session reads the current state more accurately. **Skills** expand, which give new ways to act on the gap. **Hooks** automate the routine moves so they happen even when no one is asking. Each of those makes the next step land better than the one before.

## Phases of a full climb

A quick reply might take one obvious step and stop. A hard cross-system design pulls in agents, audits, stronger models, and hours. The full climb in phases:

1. **Traverse** — read the landscape: what's the goal, what's the current state, what tools/skills are at our disposal.
2. **Marking** — name the next specific move; not the whole hill, just the one step.
3. **Ascending** — take the step.
4. **Anchoring** — verify it landed, on evidence from a tool, not vibes.
5. **Camped** — pause, check if it's higher, plan the next step.
6. **Cairn** — finished; the criteria are all closed on evidence.

## How it differs from a project plan

A plan assumes you can see the steps in advance and that they survive reality. A climb assumes neither. It commits to the goal and the step-pattern, not to the intermediate steps themselves. When the work teaches you that a step was wrong, you take a different step; you don't pretend the plan was right.

## When NOT to climb

Some goals have only one viable path. If the search is trivial and the answer is one lookup away, hill climbing is overhead — just do the step. Hill climbing pays off when the goal is far enough that seeing it whole is itself the obstacle.

## Key Insights

1. **Never see the whole hill.** The system holds the shape; you only see the next move.
2. **Check every step.** A single step that didn't take you higher isn't neutral — it moved you down or sideways. Catch that immediately.
3. **Effort scales to the task.** Discovered from the work itself, never predicted from a label. Plain-language steer ("go heavy", "quick pass") outranks heuristics.
4. **Memory and skills are the climbing gear.** They make each step a step lower than it would otherwise be.

## Related Concepts

- [[Concepts/ideal-state-artifact-isa]] — the ISA is the written target the climb aims at
- [[Concepts/intent-engineering-as-productization]] — TELOS supplies the ideal-state end of the gap
- [[Entities/lifeos]] — productization of hill climbing as an agent runtime loop

## References

- Raw: [[Raw/lifeos-philosophy-hill-climbing-2026-10-05]] and [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]]
- Origin essay: [Generalized Hill Climbing](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing)