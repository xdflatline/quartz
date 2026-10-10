---
title: "Software project discovery playbook"
details: "Synthesis of the upfront discovery phase as a software-engineering practice: the steps, the deliverables, the estimation model that justifies the cost, the prioritization scheme, and the decision artifacts that come out of a well-run discovery."
tags:
  - research
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: research
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Research Index: Software project discovery playbook

**Updated:** 2026-10-10
**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]] (Oleksandr Tytarenko, dev.to, 2026-10-10)

---

## Overview

This index synthesizes the practice of running an upfront discovery phase at the start of a software project — the steps, the team, the deliverables, the estimation model that justifies the cost, the prioritization scheme, and the decision artifacts. The framing is that a discovery is a time-boxed stage with a decision at the end: build, change course, or stop. It is not a sales meeting, a free estimate, a polished design sprint, or a long specification.

The synthesis draws on Tytarenko's practitioner guide, the GOV.UK Service Manual (public-sector definition and reframing guidance), Nielsen Norman Group (UX-side definition and team-size data), and Steve McConnell's cone-of-uncertainty model (the estimation theory that justifies ranged pre-build estimates and the discovery stage itself).

## Concepts

### Process

- [[Concepts/discovery-phase-software-projects]] — the eight-step time-boxed stage that produces a go/no-go decision and a signed-off first-release scope
- [[Concepts/discovery-deliverables]] — the ten documents (plus risk log) that a discovery should leave in the client's hands
- [[Concepts/problem-statement-framing]] — the discipline of writing a solution-free problem statement before any requirements, design or technology decisions

### Estimation and prioritization

- [[Concepts/cone-of-uncertainty]] — McConnell's model of how software estimation error narrows as decisions are made (factor of four at initial concept)
- [[Concepts/ranged-software-estimation]] — the practice of estimating effort as a low-high range in person-weeks, with stated assumptions
- [[Concepts/moscow-prioritization]] — the four-tier Must/Should/Could/Won't scheme applied to requirements

### Architecture and decision-making

- [[Concepts/architecture-decision-record]] — the short written artifact that captures a significant technical choice and its reasoning

## Tools & Projects

### Reference and research

- [[Entities/gov-uk-service-manual]] — public-sector reference for the discovery phase and the reframing guidance
- [[Entities/nielsen-norman-group]] — UX-side definition and team-size survey data
- [[Entities/steve-mcConnell]] — originator of the cone of uncertainty
- [[Entities/construx-software]] — publisher of the canonical cone-of-uncertainty white paper

### Vendor product

- [[Entities/discovery-phase-ai]] — tool that drafts the writing side of a discovery from existing material
- [[Entities/oleksandr-tytarenko]] — author of the source article and builder of Discovery Phase AI

## Raw Sources

- [[Raw/devto-discovery-phase-software-development-2026-10-10.md]] — full extracted text of the source article

## Key Sources Table

| Source | Topic | Date | Key items |
|--------|-------|------|-----------|
| [Tytarenko, dev.to](https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf) | Discovery phase steps, deliverables, cost | 2026-10-10 | Eight steps, ten deliverables, week plans, pricing formula, red flags, FAQ |
| [GOV.UK Service Manual — How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) | Public-sector definition of discovery | — | Discovery = understand the problem before building; no fixed duration |
| [NN/g — Discovery phase](https://www.nngroup.com/articles/discovery-phase/) | UX-side definition | — | Research the problem space; frame the problems; gather evidence to decide |
| [NN/g — Discoveries in industry](https://www.nngroup.com/articles/discoveries-in-industry-revealed/) | Team-size data | — | ~4 full-time people on average; designer, researcher, PM |
| [Construx — Cone of Uncertainty white paper](https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf) | Estimation model | 2019 | Factor-of-four range at initial concept; narrows only as decisions are made |

## Cross-cutting themes

### 1. Decisions, not time, narrow uncertainty

The cone of uncertainty is the load-bearing argument for the discovery stage: time alone does not narrow an estimate; decisions do. The discovery is the stage that makes the narrowing decisions on purpose. This is why a discovery is time-boxed (the decisions should be made within the box) and why single-number pre-build estimates are a red flag.

### 2. Traceability is the structural discipline

Every requirement traces to a goal. Every decision record traces to a question. Every risk has an owner. The ten-deliverable set is not a pile of documents — it is a graph in which each artifact refers to and is checked against the others. A late change to a goal must propagate to the requirements, the architecture, the screens, and the estimate, or the documents will silently disagree.

### 3. The cheap exit is the underrated value

A discovery that ends with "do not build this yet" has saved money, not wasted it. The pre-build stage exists to learn the worst news cheaply. This recasts the discovery from a cost center into an option — a chance to abandon or reshape a project before the bulk of the money is spent.

### 4. Public-sector and commercial practice have converged

The GOV.UK Service Manual, NN/g, and the agency-side practice described in the article use the same vocabulary and the same artifact set. The differences are mostly in duration and in the level of formal compliance review, not in the underlying model.

### 5. AI helps with the writing, not the decisions

The article is candid: AI is good at drafting the early stages of a discovery from existing material (decks, documents, transcripts), and at spotting gaps and contradictions between sections. It is not good at interviewing users, judging which stakeholder is right, or owning a risk. The decisions stay with the team.

## Next research directions

- [ ] Compare discovery-phase practice across three to five agency playbooks (thoughtworks, thoughtbot, fog creek, etc.) to extract the common structural artifact set and the points of divergence.
- [ ] Evaluate whether MoSCoW is sufficient for non-functional requirements (security, accessibility, data residency) or whether a separate scheme is needed for those.
- [ ] Investigate the cost-quality tradeoff of replacing the 4-week week-by-week plan with a spike-driven discovery for highly uncertain integrations (legacy systems, undocumented APIs).
- [ ] Compare ranged-estimation practice (low-high person-weeks with assumptions) against probabilistic estimation methods (PERT, Monte Carlo) for the same project, on a real retrospective dataset.
- [ ] Survey the failure modes of the ten-deliverable set in practice — which deliverable is most often dropped, which most often drifts, and which is most often ignored by the executive sponsor.
