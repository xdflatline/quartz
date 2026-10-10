---
title: "Discovery phase in software projects"
details: "Time-boxed upfront stage before design and build, in which the client and delivery team agree on the problem, users, requirements, architecture, estimates and risks, ending with a go/no-go decision and a signed-off first-release scope."
tags:
  - concept
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Discovery phase in software projects

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Process
**Status:** Production-validated (industry-consensus practice; UK Government Service Manual, NN/g, agency playbooks)

---

## Overview

A discovery phase is a short, time-boxed stage at the start of a software project that precedes design and build. Its job is to reduce the largest unknowns on paper, while changes are still cheap, and to end with a documented decision: build, change course, or stop. It is not a sales meeting, a free estimate, a polished design sprint, or a 100-page specification.

## Core content

### The eight canonical steps

Each step answers one question and leaves a written artifact.

| # | Step | Question it answers | Output |
|---|------|---------------------|--------|
| 1 | Frame the problem and the decision | Why are we doing this, and who decides? | Stakeholder list, background, first problem statement |
| 2 | Research users and the current process | Who has the problem, and how is the work done today? | Interview notes, users and actors, current journeys |
| 3 | Set goals and scope | What does success look like, and what is out? | Goals with metrics, in/out scope list |
| 4 | Write the requirements | What must the product do? | Prioritized, testable requirements |
| 5 | Explore the technical options | Can it be built, and on what? | Architecture diagrams, integration list, decision records |
| 6 | Sketch the key screens | What will people actually see? | Wireframes of the key screens |
| 7 | Plan, estimate and list the risks | How long, how much, and what could go wrong? | Milestones with low-high estimates, assumptions, risks |
| 8 | Decide and sign off | Build, change course, or stop? | Executive summary and signed-off first-release scope |

The steps overlap in real projects; later ones often send you back to earlier ones. The order still matters: requirements written before the problem is agreed tend to describe someone's favourite solution rather than the actual problem.

### Distinguishing from related practices

- **Product discovery** is the ongoing habit of a product team deciding what to build next; it never ends. A discovery phase is a one-off project stage with a deadline.
- **Inception** is usually a short, workshop-heavy kickoff that aligns the team on vision, scope and a first backlog; a long inception is a discovery by another name.
- **Scoping** is narrower — deciding what is in and out and pricing it — and is one output of discovery, often the input to a statement of work.
- **Legal e-discovery** is the exchange of electronic evidence in litigation; unrelated to software.

### Typical duration

| Duration | Use case |
|----------|----------|
| 1-2 weeks | Small MVP, one main user type, few integrations, client who answers fast |
| 3-6 weeks | Typical product with several user types, a few integrations, some open technical questions |
| 6-12 weeks | Regulated domains, many stakeholders, legacy replacement or data migration |

The actual length is set by the number of distinct user groups, the integrations to verify, the client's decision speed, and whether a compliance review is involved — not by the size of the idea.

### Effort and cost

The honest way to price is in person-weeks: **cost = people × weeks × blended weekly rate**.

| Discovery | Team | Effort |
|-----------|------|--------|
| Two weeks | 2 people (BA/PM + architect part-time) | ~3-4 person-weeks |
| Four weeks | 3 people (BA, designer, architect) | ~8-12 person-weeks |
| Six weeks | 3-4 people, plus specialists for security or data | ~15-24 person-weeks |

A rule of thumb from agency guides puts discovery at roughly 5-15% of the total build budget. Treat as a sanity check: the share falls on large projects and rises on small, risky ones.

### Red flags in a discovery proposal

- No list of deliverables ("workshops and alignment" without named documents)
- A fixed build price before discovery starts
- No time with real users (only the sponsor is interviewed)
- No technical person checking integrations
- Single-number estimates (must be a range with stated assumptions)
- The deliverables are not owned by the client
- No end date and no decision meeting
- Heavy visual design inside discovery
- The technology is chosen before the problem is understood

### Common mistakes

- Starting from a solution ("we need an app") instead of a problem
- Talking only to the buyer, not the users
- Writing a document nobody reads — the executive summary must stand on its own
- Skipping non-functional requirements (performance, security, offline, data residency)
- Estimating without assumptions
- Leaving open questions unowned
- Letting the documents drift apart after late changes
- Not involving the people who will build it

### When to skip

A formal discovery can be shrunk to a day or two when:

- the change is small and well understood, and a few tickets describe it fully
- a throwaway prototype is being built to test an idea (the prototype *is* the discovery)
- the same team has built the same kind of thing for the same client and little has changed
- the scope is fixed externally (regulator, contract) and the only open question is effort

Even then, write down the problem, goals, Musts, integrations and top risks — that takes hours, not weeks, and it is the part that saves projects.

## Key insights

1. A discovery phase is a time-box with a decision at the end. If it does not end with a decision and a scope the payer agrees with, it has not done its job.
2. Time alone does not narrow the estimate; decisions do. Discovery is where the first decisions are made on purpose.
3. A discovery that ends with "do not build this yet" has saved money, not wasted it. The cheap exit is the underrated value.

## Related concepts

- [[Concepts/cone-of-uncertainty]] — explains why early estimates need wide ranges
- [[Concepts/ranged-software-estimation]] — the pricing model used throughout
- [[Concepts/moscow-prioritization]] — the priority scheme applied to requirements
- [[Concepts/problem-statement-framing]] — the discipline applied in step 1
- [[Concepts/architecture-decision-record]] — the artifact produced in step 5
- [[Concepts/discovery-deliverables]] — the ten documents produced

## Related entities

- [[Entities/gov-uk-service-manual]] — canonical public-sector reference
- [[Entities/nielsen-norman-group]] — UX-side definition and team-size data
- [[Entities/steve-mcConnell]] — origin of the cone-of-uncertainty framing
- [[Entities/discovery-phase-ai]] — author's product for the writing/assembling side

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
