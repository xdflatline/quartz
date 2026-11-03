---
title: "Grounded answer validation"
details: "A post-execution review discipline for agent-generated analytical answers: inspect the material question, the generated SQL, the returned rows, and the prose separately, because a successful query proves only that something ran. Includes the fanout and grain checks, truncation as a hard limit on completeness claims, distinct evidence states (observed, computed, modelled, predicted, recommended, committed), and fail-closed behaviour when a material constraint cannot be verified."
tags:
  - concept
  - agent
  - llm
  - testing
  - architecture-pattern
created: 2026-11-03
updated: 2026-11-03
type: concept
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# Grounded answer validation

**Source:** NVIDIA Auto Ontology `references/query-validation.md` ([[Raw/nvidia-auto-ontology-2026-11-03]])
**Category:** Verification discipline
**Status:** Shipped as a skill reference in an open-source framework; the discipline itself is product-independent

---

## Overview

The premise is blunt: **successful execution is not evidence that the intended question was answered.** A query returns 200 rows in 400 ms and the number is wrong, because the join fanned out, the measure was a ratio summed as a quantity, the time window was a horizon total rather than a period, or the population silently excluded the rows the question was about. Nothing in the execution layer catches any of these.

The discipline is to validate four things independently, in order: the **material question** (what must be true of any correct answer), the **SQL** (does it encode those constraints), the **rows** (are they consistent with the claim), and the **prose** (does it say what the rows support). Each stage can fail while the previous one passed, which is why they are not collapsed into "did the answer look right".

## Core Content

### 1. Resolve the material question first

Before generating anything, restate what the answer must satisfy:

- population and exclusions;
- measure, unit, and result grain;
- grouping, ordering, and distinctness;
- time range, as-of time, and comparison basis;
- run/scenario identity, parent lineage, status, validity, supersession;
- required source or artifact role.

The instruction attached to this list matters more than the list: **clarify material ambiguity instead of selecting a convenient default.** An agent that silently resolves "last quarter" to the most recent complete quarter, or "customers" to rows in the customer table, has answered a different question competently.

### 2. Inspect the SQL against the constraints

Concrete failure checks, all of which pass a syntax check:

- required tables, columns, joins, literals, and time predicates are present;
- joins use approved keys and direction;
- **detail rows are aggregated to detail grain before joining to run summaries**;
- **an already run-level metric is not summed after a one-to-many detail join** (the fanout that multiplies totals);
- quantity is not replaced by a ratio, rate, average, or horizon total;
- requested run/scenario/parent/status/validity filters are explicit;
- the selected identifier has the requested source role.

The grain/fanout pair is the most valuable part of this list because it is invisible in the result: a doubled total looks like a plausible total. When fanout is detected, the correct move is to obtain and execute a corrected run-grain query — not to present the number with a caveat, and not to relabel a supplied run-level value as a validated query result.

### 3. Check the rows independently

Validate keys, population, cardinality, values, units, time scope, denominator, provenance, and literal states. Recompute simple totals and ratios where the rows allow it. Two hard rules:

- **Empty or null is not zero.** A missing row is a missing observation.
- **A truncated result cannot prove a complete list, ranking, or total.** In the implementation, `ask_question` caps at 100 rows and reports `row_count` and `truncated`; when truncated, narrow the claim or ask for an aggregate over the full population. Reporting "the top customers are…" from a truncated set is a completeness claim the evidence does not support.

### 4. Check the answer prose

Lead with findings from the rows, not a description of what the SQL would do. The prose must match the validated values, units, scope, and status. Identifiers and literal recommendation states are preserved verbatim when the question asked for them.

This stage also enforces **evidence states**: observed, computed, modelled, predicted, recommended, and committed are not interchangeable. A retrieved recommendation does not become an approved action; a diagnostic association does not become a causal claim; a counterfactual needs different evidence again. Most answer-level overclaiming is a state promotion, not a numerical error.

### Fail closed, and leave a receipt

When a material constraint cannot be verified — missing evidence, wrong population, invalid state, unverifiable truncation — the instruction is to **fail closed** rather than silently trim, substitute, or pick the latest available row. What is retained is a concise receipt: question identity, ontology/source identity, SQL, rows, row count, truncation flag, answer, attempts, and observed gaps — never credentials. The receipt is what makes a later challenge to the number resolvable.

## Key Insights

1. **Execution success is orthogonal to answer correctness.** The four-stage split exists because each stage fails silently while the others pass.
2. **Fanout is the archetypal silent error.** It preserves shape and plausibility while destroying magnitude, and only an explicit grain check catches it.
3. **Truncation is a completeness ceiling, not a footnote.** Any claim about "all", "top", or "total" is invalidated by a truncated row set.
4. **Most overclaiming is evidence-state promotion.** Observed → predicted → recommended → committed is a ladder, and answers drift up it by accident.
5. **Fail-closed beats best-effort for decision-facing numbers.** A stated gap is recoverable; a confident wrong figure is not.

## Related Concepts

- [[Concepts/answer-readiness-vs-answerability]] — the pre-flight check that precedes this review
- [[Concepts/semantic-contract-for-measures]] — the definitions the SQL is validated against
- [[Concepts/semantic-layer-agent-grounding]] — why the layer can supply the provenance the receipt records
- [[Concepts/agent-tool-surface-curation]] — how the raw SQL and rows are returned as fields rather than prose

## Related Entities

- [[Entities/auto-ontology]]

## References

- Raw Source: [[Raw/nvidia-auto-ontology-2026-11-03]] (`skills/nvidia-ontology-query/references/query-validation.md`)
