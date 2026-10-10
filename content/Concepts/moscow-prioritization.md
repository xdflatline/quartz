---
title: "MoSCoW prioritization"
details: "Four-tier prioritization scheme — Must, Should, Could, Won't — used to classify requirements by their necessity to a release, typically the first release defined in a discovery phase."
tags:
  - concept
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# MoSCoW prioritization

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Prioritization method
**Status:** Production-validated (widely used in agile delivery)

---

## Overview

MoSCoW is a four-tier prioritization scheme used to classify requirements by their necessity to a release, typically the first release defined in a discovery phase. The acronym stands for Must, Should, Could, Won't.

## Core content

### The four tiers

- **Must** — required for the release to be viable; without these, the release does not ship
- **Should** — important but not vital; the release can ship without them
- **Could** — desirable if time and budget allow; the first things cut
- **Won't** (this time) — explicitly out of scope for this release; a planning promise, not a refusal

### In the discovery context

MoSCoW is applied to the requirements produced in step 4 of a discovery phase. Each requirement is also given a type (functional, non-functional, or constraint), acceptance criteria (especially for Musts), and a link to the goal it supports. The "Won't" tier is the disciplined version of an "out of scope" list and prevents more arguments than any other single page in a discovery report.

### Variations

In agile settings, MoSCoW is often applied per-release rather than per-product, so a Could in release 1 can become a Must in release 2. The prioritization is local to a time-box.

## Key insights

1. The "Won't (this time)" tier is the load-bearing part. Naming what is explicitly out of scope prevents the most common scope-creep arguments later.
2. A requirement that has no acceptance criteria is not a Must; it is a wish.
3. Prioritization without a linked goal is decoration. Every Must must trace to a goal so it can be defended or cut.

## Related concepts

- [[Concepts/discovery-phase-software-projects]] — the stage that produces MoSCoW-tagged requirements
- [[Concepts/discovery-deliverables]] — the requirements list is one of the ten
- [[Concepts/problem-statement-framing]] — the goals that the Musts must trace to

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
