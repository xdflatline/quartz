---
title: "\"Define What Good Looks Like\" — The Litmus Test for Handing Work to AI"
details: "Sam Newman's gate for any autonomous or semi-autonomous software work: you must (1) define what good looks like as a specification and (2) prove your system actually does what that good definition says. Without both, the work is not safe to hand to an agent. Borrowed into Kevin Hedy's three-axis reframe — development requirements, operational requirements, business requirements — as the verification surface."
tags:
  - concept
  - software-engineering
  - agent
created: 2026-10-09
updated: 2026-10-09
type: concept
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

## Definition

Newman's gate, stated bluntly in the interview:

> "You cannot hand your work over to agents unless it does these two things. One, **define what good looks like**. Two, **prove that your system does what this good definition looks like**."

If either condition is missing, the work is not safe to automate. Spec-driven development is *the on-ramp* to agent-driven development — you have to get the spec working first, even without any AI in the loop, before the spec can be the contract with an agent.

## Kevin Hedy's reframe: three axes of "good"

Newman agrees with Kevin Hedy's dislike of "non-functional requirements" (because "non-functional means it doesn't work"). Instead, decompose "good" along three axes:

| Axis | Question | Example |
|------|----------|---------|
| **Development requirements** | Is the code maintainable? | Test coverage, modularity, dependency hygiene. |
| **Operational requirements** | Will it run? | Latency budget, uptime, error rate. |
| **Business requirements** | Does it do the thing? | Feature correctness, user-flow success. |

For each axis, you need a *measurable* definition of good. If you can't define good on any one axis, you can't hand that work to an agent — but you can still do specs for the parts where you *can* define good.

## How this fits into the broader architecture strategy

Newman's recommendation for hybrid systems:

- **High-trust, well-bounded modules** — fully autonomous factory approach. AI does the work; humans check SLOs.
- **High-trust modules that are not on the critical path** — also candidates for the factory approach. Easy to roll back.
- **Mission-critical, not-yet-trusted areas** — collaborative human + AI mode. Humans stay intimately involved with the code.

The mistake is treating the system as a single black box and picking one approach for everything.

## Anti-patterns

- "Define good" without "prove good" — specs without verification. Agent output accepted on faith. Cognitive surrender at the system level.
- "Prove good" without "define good" — observability without a target. Vanity dashboards that don't actually correspond to user value.
- Treating "good" as a single global definition — different modules have different bugs, different criticality, different blast radii.

## Related Concepts

- [[Concepts/cognitive-depth-vs-cognitive-surrender]] — Without this gate, cognitive surrender is the inevitable result
- [[Concepts/production-is-truth]] — "Prove good" is exactly the production-as-truth discipline
- [[Concepts/spec-driven-development-sdd-2026]] — The SDD concept in the wiki's vocabulary is the formalization of Newman's "start with a spec" on-ramp