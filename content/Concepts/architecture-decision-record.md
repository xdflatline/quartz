---
title: "Architecture decision record"
details: "Short, written artifact capturing one significant technical choice — the question, the options compared, the choice and its consequences — produced during the technical-exploration step of a discovery phase so future readers can see why a decision was made."
tags:
  - concept
  - software-engineering
  - architecture-pattern
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Architecture decision record

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Architecture pattern / Process artifact
**Status:** Production-validated

---

## Overview

An architecture decision record (ADR) is a short, written artifact that captures one significant technical choice: the question that was asked, the options that were compared, the choice that was made, and its consequences. ADRs are produced during the technical-exploration step of a discovery phase so that future readers — and the team itself, six months later — can see *why* a decision was made, not just *what* was decided.

## Core content

### Structure

A typical ADR for each significant choice records:

- **Context / question** — the decision the team needed to make and why
- **Options considered** — the realistic alternatives, including the "do nothing" baseline
- **Trade-offs** — the relevant costs, risks, and unknowns for each option
- **Decision** — what was chosen
- **Consequences** — what becomes easier, what becomes harder, and what is now foreclosed

The aim is brevity and traceability, not completeness. One or two pages per decision is the right size.

### When to write one

During discovery, the prompt is straightforward: every significant choice gets a record. The article's criterion is "every big choice recorded." Common candidates include the technology stack, the database, the authentication approach, the integration strategy for a key external system, the deployment topology, and the data model for regulated data.

### In the discovery deliverables

ADRs are part of the **Architecture** deliverable in the ten-document discovery set, alongside context and component diagrams and the integration list. Every integration is checked (owner, API existence, documentation, capabilities) and every big choice is recorded.

## Key insights

1. The point of an ADR is to make the *reasoning* survive, not just the conclusion. A future engineer who reads "we chose Postgres" with no ADR has to guess; with one, they can challenge the reasoning or extend it.
2. Brevity is the discipline. A one-page ADR that gets read beats a ten-page design doc that does not.
3. The list of considered options is the load-bearing section. "We considered X, Y, and Z and chose Y" is far more useful than "we chose Y because reasons."

## Related concepts

- [[Concepts/discovery-phase-software-projects]] — the stage that produces ADRs
- [[Concepts/discovery-deliverables]] — ADRs are part of the Architecture document
- [[Concepts/ranged-software-estimation]] — technical spikes that inform ADR choices

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
