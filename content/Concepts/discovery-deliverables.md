---
title: "Discovery phase deliverables"
details: "The set of ten documents (or ten sections of one document) plus a risk log that a discovery phase should leave behind: stakeholders, background, executive summary, problem statement, goals and metrics, user experience, requirements, architecture, UI screens, and roadmap with estimates."
tags:
  - concept
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: concept
sources:
  - .Raw/devto-discovery-phase-software-development-2026-10-10.md
---

# Discovery phase deliverables

**Source:** [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
**Category:** Process artifact set
**Status:** Production-validated

---

## Overview

The discovery phase deliverables are the set of ten documents (or ten sections of one document) plus a risk log that a discovery phase should leave behind at the end. They are the same ten sections in every well-run discovery: stakeholders, background, executive summary, problem statement, goals and success metrics, user experience, requirements, architecture, UI screens, and roadmap with estimates.

## Core content

### The ten documents

| # | Deliverable | Contains | Done when |
|---|-------------|----------|-----------|
| 1 | **Stakeholders** | Name, role, what they need, influence, open disagreements | You know who signs off and who can say no |
| 2 | **Background** | Business, current process and tools, past attempts, hard constraints | A new team member could start with it on day one |
| 3 | **Executive summary** | Problem, proposed solution, outcome, scope, timeline and cost range, the decision needed | The sponsor can read it in two minutes and decide |
| 4 | **Problem statement** | Who is affected, what goes wrong, how often, what it costs, the evidence | It names no solution and everyone agrees with it |
| 5 | **Goals and success metrics** | Two or three goals, each metric with today's value, target and date, KPIs to watch | Every goal can be judged later |
| 6 | **User experience** | Users and actors, journeys step by step, key flows as diagrams | The main journey of each user is mapped |
| 7 | **Requirements** | Testable items with type, MoSCoW priority, acceptance criteria, linked goal, owner | Every Must has acceptance criteria and traces to a goal |
| 8 | **Architecture** | Context and component diagrams, integrations, decision records | Every integration is checked and every big choice recorded |
| 9 | **UI screens** | Wireframes of the main screens, which requirements each covers | Stakeholders agree on what users will see |
| 10 | **Roadmap and estimates** | Milestones, dates, low-high person-week ranges, dependencies, assumptions | Each estimate states what it assumes |
| + | **Risks, blockers and open questions** | Each item with likelihood, impact, owner and next step | Nothing known is left unowned |

### Design principles

- **The set is fixed, the order of writing is not.** Most discoveries write the executive summary last, even though it appears third in the list, because it summarizes the others.
- **Each artifact has a "done when" condition.** A discovery that cannot answer "is this done?" for each of the ten has not done its job.
- **Documents must not drift apart.** When a goal or requirement changes late, the architecture, screens, and estimate that depend on it must change too.
- **Traceability is the structural discipline.** Every requirement traces to a goal; every decision record traces to a question; every risk has an owner.

### Why ten, not one hundred

A long specification is a discovery failure mode. The article's common-mistakes list calls out "writing a document nobody reads" — ten clear sections beat a hundred pages. The executive summary must stand on its own; the sponsor should be able to read two pages and decide.

### Ownership of the deliverables

A discovery proposal that does not give the client ownership of the documents is a red flag. The client should be free to take the deliverables to another team. "Workshops and alignment" without named documents is another red flag — without a list of deliverables, the client cannot tell when the discovery is finished.

## Key insights

1. The deliverables are the test of whether a discovery happened. If the documents are not in the client's hands at the end, the discovery did not occur.
2. The executive summary is the only document the sponsor will read; everything else exists to support it and to be checked against it.
3. Drift is the most common failure. A late change to a goal must propagate to the requirements, the architecture, the screens, and the estimate — or the documents will silently disagree.

## Related concepts

- [[Concepts/discovery-phase-software-projects]] — the stage that produces these
- [[Concepts/problem-statement-framing]] — the problem statement is deliverable #4
- [[Concepts/moscow-prioritization]] — the priority scheme applied to deliverable #7
- [[Concepts/architecture-decision-record]] — the unit of deliverable #8
- [[Concepts/ranged-software-estimation]] — the estimation approach in deliverable #10

## References

- Raw article: [[Raw/devto-discovery-phase-software-development-2026-10-10.md]]
- Original: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
