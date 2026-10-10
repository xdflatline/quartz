---
title: "Ranged software estimation"
details: "Practice of estimating software effort as a low-high range in person-weeks with the assumptions the range relies on written down, rather than as a single number, so the estimate can be checked and defended as decisions are made."
tags:
  - concept
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Ranged software estimation

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Estimation practice
**Status:** Production-validated

---

## Overview

Ranged software estimation is the practice of estimating software effort as a low-high range in person-weeks, with the assumptions the range relies on written down, rather than as a single number. The range is the honest output; a single number before decisions are made is theatre.

## Core content

### The formula

**cost = people × weeks × blended weekly rate**

A range replaces each scalar. The team size is a range (full-time vs part-time across roles), the duration is a range (calendar weeks accounting for client decision latency), and the rate is a range (per role, per region). Multiplied together, the result is a defensible low and high.

### Worked example from the article

At an illustrative blended rate of $4,000 per person-week, a four-week discovery of about 10 person-weeks costs about $40,000. The same 10 person-weeks at $1,500 per person-week costs $15,000. The spread between vendors and countries comes almost entirely from the rate, not the effort estimate — a useful diagnostic when comparing proposals.

### Why the assumptions are load-bearing

An estimate without its assumptions cannot be checked or defended later. The assumptions are the conditions under which the range holds. If those conditions change (a new integration, a missing API, a regulator adds a step), the range can be re-evaluated; without the assumptions, the team has to start over.

### The discovery context

During the plan-and-estimate step of a discovery phase, the work is split into milestones that each deliver something usable. Each milestone is estimated as a low-high range in person-weeks, and each estimate states what it assumes. The aggregation is the discovery's overall range.

### The 5-15% rule of thumb

A common rule of thumb, mostly from agency guides, puts the cost of discovery at roughly 5-15% of the total build budget. The article treats it as a sanity check rather than a fact: on a large project the share falls, and on a small, risky one it can be higher.

### Single-number estimates as a red flag

A discovery proposal that quotes a single number for the build cost — rather than a range with stated assumptions — is a red flag. The single number is either pulled out of the wide end of the cone of uncertainty or it is a sales number; either way, the variance is hidden from the client.

## Key insights

1. The range is the estimate. A single number is a sales number.
2. The assumptions are the audit trail. Without them, the range cannot be checked.
3. Rate variation explains most of the price difference between vendors and countries, not effort estimation skill. Use the rate spread as a diagnostic.

## Related concepts

- [[Concepts/discovery-phase-software-projects]] — the stage that produces ranged estimates
- [[Concepts/cone-of-uncertainty]] — the underlying model that justifies the range
- [[Concepts/discovery-deliverables]] — the roadmap and estimates are one of the ten

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
