---
title: "Cone of uncertainty"
details: "Steve McConnell's model of how software estimation error narrows over the life of a project, beginning with a factor-of-four plausible error range at initial concept and tightening only as requirements and design decisions are actually made."
tags:
  - concept
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Cone of uncertainty

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Estimation model
**Status:** Production-validated (industry-standard reference)

---

## Overview

The cone of uncertainty is Steve McConnell's model of how software estimation error narrows over a project's life. At the initial-concept stage an estimate can plausibly be off by a factor of four in either direction, and the range narrows only as requirements and design decisions are actually made. Time alone does not narrow the cone; decisions do.

## Core content

### The principle

Early in a project, nobody knows enough to estimate it well. The cone represents the spread of plausible estimates at each stage:

- **Initial concept:** ±4× (the estimate can plausibly be one-quarter to four times the actual)
- **Approved requirements / scope:** ±2× to ±1×
- **Detailed design / early build:** narrows further as the team tests assumptions

The cone is a best case. Without deliberate effort to make decisions, the range does not collapse.

### Why a discovery phase is the mechanism to narrow the cone

A discovery phase is the explicit stage where the decisions that narrow the cone get made on purpose — problem framing, user research, requirements, architecture, technical spikes — instead of by accident halfway through the build.

### Implications

- Single-number estimates before decisions are made are a category error: the spread *is* the estimate.
- Effort spent early on framing, research and integration checks is justified precisely because it narrows the cone before money is committed to build.
- A discovery phase that ends with "do not build this yet" avoids building the project at the wide end of the cone.

## Key insights

1. Time does not narrow the cone; decisions do. Waiting does not produce a better estimate.
2. The cone justifies the upfront cost of discovery: narrowing a 4× range before a $1M build saves far more than the discovery itself costs.
3. A range with stated assumptions is honest; a single number before decisions are made is theatre.

## Related concepts

- [[Concepts/discovery-phase-software-projects]] — the stage that narrows the cone
- [[Concepts/ranged-software-estimation]] — the artifact that should reflect the cone
- [[Concepts/discovery-deliverables]] — what gets produced to narrow it

## Related entities

- [[Entities/steve-mcConnell]] — origin of the model
- [[Entities/construx-software]] — publisher of the canonical white paper

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
- Construx white paper: https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf
