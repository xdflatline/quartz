---
title: "Ideal State Artifact (ISA) — Testable Specification Document"
details: "An architectural pattern for capturing 'done' as a structured document before work begins: 12 fixed sections running Problem → Vision → Out of Scope → Principles → Constraints → Goal → Criteria → Test Strategy → Features → Decisions → Changelog → Verification. The criteria (called ISCs, Ideal State Criteria) are the test suite — each names one binary condition and the single probe that would falsify it, so the same object functions as spec, test harness, and completion record. Anti-criteria turn ruled-out options into testable proof they stayed out. Popularized by Daniel Miessler's LifeOS but applicable anywhere work needs a falsifiable definition of done before it starts."
tags:
  - concept
  - architecture-pattern
  - agent
  - evaluation
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-the-isa-2026-10-05]]"
---

# Ideal State Artifact (ISA) — Testable Specification Document

**Source:** [[Raw/lifeos-philosophy-the-isa-2026-10-05]] and [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Production-validated (used in LifeOS, paired with the Algorithm loop)

## Overview

The Ideal State Artifact is a single structured document that does four jobs at once: the written articulation of "done," the test harness during the build, the completion condition when the build ends, and the long-lived record of what was actually shipped. The trick is that the criteria section is the test suite — every entry is one binary condition with one named probe — so nothing drifts between what you said "done" meant and what you actually checked.

## The twelve sections, in fixed order

The order is non-negotiable on purpose. You state what's wrong and what right looks like before you're allowed to name the goal.

1. **Problem** — what's actually wrong.
2. **Vision** — what right looks like, including what *euphoric surprise* would be on this task.
3. **Out of Scope** — what you're deliberately not doing.
4. **Principles** — how the system may think about it.
5. **Constraints** — what the solution may not do.
6. **Goal** — the one-line target, named only after the five sections above.
7. **Criteria** (the ISCs) — the testable heart of the document.
8. **Test Strategy** — the single probe behind each criterion.
9. **Features** — the work, tracked against the criteria.
10. **Decisions** — why the calls were made.
11. **Changelog** — what happened, in order.
12. **Verification** — the evidence that every criterion passed.

## Why the criteria section is the test suite

Each criterion states the falsifier: the one command, HTTP call, screenshot, diff, or model judgment that would prove it false. So progress is something the document computes rather than something you assert. The task is done when every ISC passes, with evidence attached. There is no separate acceptance suite bolted on later.

Two corollaries keep the document honest over time. **ISC IDs never renumber** once written, so a criterion you point at today still means the same thing three edits from now. **Anti-criteria** turn the things you ruled out into testable proof that they stayed out — an ISC of the form "the system did not deploy on Friday" can be probed after the fact.

## Connection to the algorithm loop

Every Algorithm-style run binds to an ISA. The run reads and writes the document the whole way through: it scaffolds from the sections, climbs toward them, and checks evidence into the Verification section at close. The Algorithm is the motion; the ISA is the thing that persists after the motion stops.

The ISA can live in one of two homes. **Work with a lasting identity** (an app, a library, a blog, the Algorithm itself) keeps a *project ISA* in its repo that grows across every session. **One-shot work** gets a *task ISA* under a work folder, created when the job starts and archived when it's done.

## When the criteria become the harness

The same artifact can drive a continuous validation system. In the LifeOS Bunker pattern, an app's ISA is the test suite: `bunker test` reads the document and runs every probe on a schedule, forever. The same file describes what the app should be and verifies what it is.

## Key Insights

1. **The order is the discipline.** Stating the problem and what "right" means before naming the goal prevents premature optimization toward the wrong thing.
2. **One probe per criterion.** A criterion that maps to multiple probes is under-decomposed; split it until each piece is one testable thing.
3. **Anti-criteria matter as much as criteria.** What you ruled out becomes a testable assertion that it stayed ruled out, which catches scope creep.
4. **The document computes "done."** You don't assert completion; the document asserts it, and you read it.

## Related Concepts

- [[Concepts/four-tier-verification-stack]] — where the probes sit in the broader verification ladder
- [[Concepts/generalized-hill-climbing-llm-tasks]] — the Algorithm pattern ISA is the target state and run-time spec for
- [[Concepts/intent-engineering-as-productization]] — TELOS holds the durable intent; ISA holds the task intent
- [[Entities/lifeos]] — primary productization of the ISA pattern

## References

- Raw: [[Raw/lifeos-philosophy-the-isa-2026-10-05]] and [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]]
- Origin essay: [Ideal State Articulation](https://danielmiessler.com/blog/ai-ideal-state-articulation)
- Docs: https://docs.ourlifeos.ai/ISA__ISASystem