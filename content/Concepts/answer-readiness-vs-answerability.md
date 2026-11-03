---
title: "Answer readiness versus answerability"
details: "A pre-flight distinction for agentic query systems: being able to answer anything at all (a compiled semantic layer plus a live source connection) is independent of whether a specific question is covered by the semantic layer. Confusing the two produces the most misleading state in such a deployment, where the glossary reads fine and every question still fails after minutes of model calls."
tags:
  - concept
  - agent
  - mcp
  - architecture-pattern
created: 2026-11-03
updated: 2026-11-03
type: concept
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# Answer readiness versus answerability

**Source:** NVIDIA Auto Ontology MCP documentation and query skill ([[Raw/nvidia-auto-ontology-2026-11-03]])
**Category:** Operational pattern / pre-flight check
**Status:** Implemented as two distinct checks (`check_readiness`, `check_answerable`); the distinction generalises beyond this product

---

## Overview

A question-answering system over enterprise data has two independent failure axes, and they look identical from the outside:

- **Readiness** — can this deployment answer *anything*? It needs a compiled semantic layer to resolve vocabulary against **and** a live connection to run the generated SQL on.
- **Answerability** — does this deployment's semantic layer cover *this* question? It needs the question's nouns and measures to exist as terms with usable bindings.

Having one without the other is the dangerous state. The glossary reads, search returns terms, the UI looks healthy — and every question still fails, expensively and vaguely, after tens of seconds of sequential model calls. The cost of not distinguishing the two is paid in rephrased questions, because the natural response to an empty answer is to rewrite the question rather than to check the plumbing.

## Core Content

### Why the two checks cannot be merged

Readiness is a property of the deployment; answerability is a property of the question. A deployment can be perfectly ready and the question still unanswerable (the vocabulary is missing), and a question can be perfectly answerable in principle while the deployment cannot execute anything (the connection is gone).

The practical consequence is ordering: readiness first, then vocabulary discovery, then a cheap coverage check, then the expensive generation call. The Auto Ontology MCP tool sequence encodes exactly that — `check_readiness` → `search_terms` → `check_answerable` → `ask_question`.

### The misleading state, in detail

Three observations from the source that generalise:

1. **A named database is not a working connection.** The catalog outlives the connection it was ingested from, so a database listed in the catalog is evidence that ingestion once succeeded, not that SQL can run now. Readiness therefore reports `can_execute_sql` separately from the list of databases.
2. **A compiled layer can be empty without erroring.** A status flag (`calculated: false`) distinguishes "the glossary has never been compiled" from "the glossary is compiled and this term is unknown". Without that flag, both surface as a failed answer.
3. **Permission gaps masquerade as outages.** Connection details are admin-only by default, so a non-admin caller gets a 403 where an admin would get a list. Reporting that as `unverified` rather than as a blocker is what keeps a viewer's verdict honest — the check says what it could not verify instead of failing the whole pre-flight.

### Report all blockers at once

Readiness is only useful if it is exhaustive in one call. Reporting the first missing prerequisite sends the operator through a serial debug loop (fix key, retry, discover the layer is uncompiled, fix, retry, discover no connection). The implementation's contract is to report every blocker in a single response, which is the same principle as a linter reporting all errors rather than the first.

### Answerability is a coverage check, not a confidence score

`check_answerable` is explicitly a *cheap* pre-flight: it grades whether the semantic layer covers a question before paying for full text-to-SQL. It is a coverage question — do these terms exist and bind to columns — not a prediction of whether the generated SQL will be correct. Treating a positive coverage result as confidence in the answer is a category error, and is exactly the gap the answer-validation workflow exists to close.

## Key Insights

1. **"Can answer anything" and "can answer this" are different questions with different fixes.** Merging them turns a configuration error into an apparent prompt problem.
2. **The healthiest-looking state is the most misleading one.** Catalogue reads and term resolution are served from the semantic layer and survive the loss of the thing that actually executes queries.
3. **Cheap checks belong before expensive ones.** A coverage check that costs milliseconds should gate a call that costs tens of seconds and many model invocations.
4. **Report unverifiable as unverifiable.** A 403 on a connection listing is not a deployment failure; collapsing it into one is how pre-flight checks lose credibility.
5. **Empty answers should route to diagnostics, not to rephrasing.** The default human response — ask it differently — is the wrong move when the real cause is plumbing.

## Related Concepts

- [[Concepts/semantic-layer-agent-grounding]] — the layer whose availability readiness is checking
- [[Concepts/grounded-answer-validation]] — the post-execution counterpart to this pre-flight
- [[Concepts/agent-tool-surface-curation]] — why the checks are separate tools rather than one "ask"
- [[Concepts/semantic-contract-for-measures]] — what makes a term answerable in the first place

## Related Entities

- [[Entities/auto-ontology]]

## References

- Raw Source: [[Raw/nvidia-auto-ontology-2026-11-03]] (`docs/mcp.md` — "About `check_readiness`"; `skills/nvidia-ontology-query/SKILL.md`)
