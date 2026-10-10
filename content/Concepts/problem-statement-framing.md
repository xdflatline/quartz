---
title: "Problem statement framing"
details: "Discipline of writing a solution-free statement of who is affected, what goes wrong, how often, what it costs, and what the evidence is, before any requirements, design or technology decisions are made."
tags:
  - concept
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Problem statement framing

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Process discipline
**Status:** Production-validated

---

## Overview

Problem statement framing is the discipline of writing a solution-free statement of who is affected, what goes wrong, how often, what it costs, and what the evidence is, before any requirements, design, or technology decisions are made. It is the first concrete artifact of a discovery phase and the one that everything else must trace back to.

## Core content

### What a good problem statement contains

- **Who is affected** — the users, actors, or systems that experience the problem
- **What goes wrong** — the observable failure or gap, described in the affected party's terms
- **How often** — the frequency or volume, with evidence (numbers, complaints, observed workarounds)
- **What it costs** — the impact in time, money, risk, or missed opportunity
- **The evidence** — interviews, analytics, support tickets, contracts with current vendors

A good problem statement names no solution. "We need an app" is not a problem statement; "field technicians lose an average of 90 minutes per shift to manual work-order re-entry, costing roughly $X per year and driving two complaints per week" is.

### The framing test

The test is whether the affected parties, the sponsor, and the team can all describe the same problem in the same words. If the sponsor says "we need better reporting" and the users say "we cannot find orders quickly," the problem has not yet been framed.

### Why it comes first

Requirements written before the problem is agreed tend to describe someone's favourite solution. Once a solution is in writing, the framing conversation collapses into defending or attacking the solution. The problem statement is the artifact that keeps the conversation open long enough to find the real issue.

### The GOV.UK reframing guidance

The UK Government Service Manual advises reapplying this discipline whenever a predetermined solution is brought to discovery: take the proposed solution and ask "what problem does this solve?" If the problem is not worth solving, neither is the solution. The same principle applies to most commercial projects.

## Key insights

1. A problem statement that names a solution is a solution in disguise. It is the most common failure mode and the hardest to spot because it reads as a normal requirement.
2. The evidence section is the load-bearing one. "Users are frustrated" is not evidence; "12 of 14 interviews identified X, supported by 4,200 support tickets over 6 months" is.
3. The problem statement is the document that lets you change direction cheaply. Without one, every later artifact is anchored to a solution.

## Related concepts

- [[Concepts/discovery-phase-software-projects]] — the first step of which produces the problem statement
- [[Concepts/moscow-prioritization]] — priorities that must trace to the agreed problem
- [[Concepts/discovery-deliverables]] — the problem statement is one of the ten

## Related entities

- [[Entities/gov-uk-service-manual]] — source of the reframing guidance

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
