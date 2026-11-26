---
title: "Handoff Contract Validation"
details: "Validate what one agent passes to the next in plain code outside the agents — format, freshness, and plausibility — because the receiving agent cannot distinguish an upstream guess from a fact. Field evidence from a two-stage weather pipeline: stale test alerts were consumed as live warnings, and per-request hop limits and one central budget are the companion controls. The rule is that data quality is checked at the boundary, not requested in the prompt."
tags:
  - concept
  - multi-agent
  - testing
  - architecture-pattern
created: 2026-11-26
updated: 2026-11-26
type: concept
sources:
  - "Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26.md"
---

# Handoff Contract Validation

**Source:** [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]] — failure lessons from Stormwise, a two-stage Claude weather pipeline evaluated on 117 real National Weather Service alert cases
**Category:** Verification discipline
**Status:** Production-validated in a single evaluated system (arXiv 2611.05290); the control itself is generic engineering practice

---

## Overview

In a multi-agent system, **the receiving agent has no way to tell an upstream guess from an upstream fact.** Provenance does not survive a natural-language handoff: once agent A writes "conditions are calm in the Chennai area" into a message, agent B sees a sentence with the same surface form whether A read that from an official alert, inferred it from an old reading, or invented it. The failure therefore does not look like hallucination at the point of use — it looks like a model that reasonably believed what it was told.

The discipline is to put validation **at the boundary, in plain code**, rather than asking agents in their instructions to be careful. The source's phrasing: "Check data at every handoff, in plain code." Concretely, three properties are checked per handoff: **format** (does it match the contract), **freshness** (is it current for the decision being made), and **sense** (is the value plausible given the request and other evidence).

## Core Content

### The worked failure: test alerts consumed as live warnings

Stormwise's pipeline had only two stages — fetch official alerts, then answer the question with them in hand. Weather services publish *test* alerts in the same feed as live ones. The pipeline passed some through, and the answering model treated them as real warnings.

The instructive part is where the defect lived: not in the model. The model did what it should with the input it received. **The step before it made the mistake, and the step after it could not see the difference.** In a single-agent system this concentrates in one place; in a multi-agent system it becomes the default, because every handoff is an opportunity to launder a guess into a fact.

### The five day-one guardrails

The source's list is deliberately unglamorous — all of it is code that sits outside the agents:

| Guardrail | What it enforces | Failure it prevents |
|---|---|---|
| **Check every handoff** | format, freshness, plausibility of the payload | upstream guess consumed as fact; stale data driving a live decision |
| **Limit the hops** | cap on bounce count between agents; escalate to a human past the cap | livelock — every agent locally sensible, system circling |
| **One budget per request** | a single counter for the whole run, not per-agent budgets | cost blowup on exactly the hard cases, where sub-budgets each look fine |
| **Log every inter-agent message** | replayable trace of payloads | undiagnosable failures; no way to attribute which stage corrupted the data |
| **Test with real cases** | a regression set drawn from real inputs, plus hand spot-checks of automatic scoring | an automated checker that is confidently wrong (see [[Concepts/grounding-over-honesty-prompting|Grounding Over Honesty Prompting]]) |

### Contract shape

The "contract" does not need to be elaborate. What it needs is to be **executable and outside the model**:

- **Typed payloads** rather than prose wherever a stage can emit structure — a JSON schema per handoff makes format checkable by a parser instead of by an LLM.
- **Explicit provenance fields** — `source`, `observed_at`, `kind` (`observed` / `derived` / `estimated`). The receiving prompt can then be told what it is reading, and the boundary check can reject a derived value where an observed one is required.
- **Freshness predicates** — a max age per field, evaluated against the decision time, not against wall clock at ingestion.
- **Reject-and-retry rather than accept-and-hope.** A failed check should route the work back to the producing stage with the reason attached, or terminate — not forward a degraded payload with a caveat.

### Hop limits are a separate control from budgets

They fail differently and are commonly conflated. A budget caps spend and is usually denominated in tokens or calls; a hop limit caps **structural looping** and is denominated in handoffs between agents. A run can loop cheaply forever within its budget, and can also burn its entire budget productively in one deep branch. The source recommends both, with a human escalation when the hop cap trips.

## Key Insights

1. Provenance is lost at every natural-language handoff; only an explicit field or an out-of-band check preserves it.
2. The receiving agent's failure is downstream of the producing stage's defect, so post-hoc inspection of the final answer attributes blame to the wrong component.
3. Validation belongs in plain code at the boundary; prompt-level instructions to "only trust verified data" have no mechanism behind them.
4. Hop limits, central budgets, and message logging are the three controls that make a multi-agent run diagnosable at all — without them, a wrong answer has no traceable cause.
5. Same-stage failure reappears in the evaluation layer: if the checker is code, its recall must be measured against hand labels (see the 53-of-57 miss in the companion concept).

## Related Concepts

- [[Concepts/multiagent-system-failure-modes|Multiagent System Failure Modes]] — the emergent-behaviour taxonomy (conformity, collusion, epistemic blindness, escalation); this page is the engineering control for the epistemic case
- [[Concepts/agent-epistemic-vigilance-deficit|Agent Epistemic Vigilance Deficit]] — why agents do not spontaneously discount untrusted peers
- [[Concepts/standard-json-schema-tool-contracts|Standard JSON Schema Tool Contracts]] — the typed-payload mechanism a handoff contract builds on
- [[Concepts/grounded-answer-validation|Grounded Answer Validation]] — the post-execution analogue: successful execution is not evidence of a correct answer
- [[Concepts/hitl-approval-gates-for-tool-calls|HITL Approval Gates for Tool Calls]] — where the hop-limit escalation terminates
- [[Concepts/verification-subagent-pattern|Verification Subagent Pattern]] — adding a checker agent; the checker itself needs calibration
- [[Concepts/blackboard-agent-coordination|Blackboard Agent Coordination]] — every board write is a handoff to all future readers

## References

- Raw Article: [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]]
- Original: https://kadhar.dev/blog/multi-agent-systems-from-scratch
- Evaluation write-up: https://arxiv.org/abs/2611.05290
