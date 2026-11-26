---
title: "Grounding Over Honesty Prompting"
details: "Measured result from a severe-weather assistant on 117 real alert cases: without access to official alerts it called conditions calm during active warnings in 26 of 69 cases (38%); adding an instruction to admit it could not see official alerts made it worse at 31 of 69 (45%); with the alerts in context and a plain prompt, zero. Access to the right data at the right step fixes false reassurance, disclaimer instructions do not. Companion finding: a pattern-matching checker missed 53 of 57 real cases, so automated scoring needs hand-labelled calibration."
tags:
  - concept
  - agent
  - evaluation
  - prompt-engineering
created: 2026-11-26
updated: 2026-11-26
type: concept
sources:
  - "Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26.md"
---

# Grounding Over Honesty Prompting

**Source:** [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]] — Stormwise evaluation, 117 cases built from real National Weather Service alerts (arXiv 2611.05290)
**Category:** Evaluation finding
**Status:** Measured on one system (n = 69 warning cases); directionally consistent with the broader grounding literature, but the specific percentages are single-system results

---

## Overview

When a model lacks the information needed to answer safely, the intuitive fix is to instruct it to say so. The Stormwise evaluation measured that fix and found it does not work — and that it can make the failure rate worse.

The system was a severe-weather assistant asked about conditions during **active official warnings**, evaluated on 117 cases built from real National Weather Service alerts. "False reassurance" means the assistant told the user conditions were calm while a warning was active.

| Condition | False reassurance | Notes |
|---|---|---|
| No access to official alerts, plain prompt | **26 of 69 (38%)** | model answered from its own priors |
| No alert access **plus** "admit you can't see official alerts" instruction | **31 of 69 (45%)** | disclaimer instruction made it *worse* |
| Official alerts in context, plain prompt | **0 of 69** | no special prompting at all |

## Core Content

### Why the disclaimer instruction backfires

Three mechanisms are consistent with the observed direction:

1. **A disclaimer is not information.** Telling a model to acknowledge a gap does not give it the data; it changes the surface of the answer while the underlying belief stays wrong. The user still receives a confident claim, now wrapped in a hedge.
2. **Instruction-following pressure toward completion.** The prompt now contains two competing directives — answer the question, and admit ignorance. In a weather question where the model has *some* prior about Chennai in November, "answer" wins, and the hedge is attached to a wrong claim rather than replacing it.
3. **Verbal hedging is scored as compliance.** The model can satisfy the letter of the instruction ("I don't have official alerts, but conditions are typically…") while still emitting the unsafe reassurance. A string-level judge may even score that as honesty.

The practical conclusion is not "prompting is useless" but a scoping rule: **prompting can shape how a model expresses what it knows; it cannot supply what it does not know.** Where the failure is informational, fix the data path. Where the failure is stylistic or formatting, prompting is the right lever.

### The second finding: check the checker

The first measurement of false reassurance in the same project was done with a simple pattern-matching script. Against 57 real cases it **missed 53**, which pointed the analysis to the opposite conclusion. The author then hand-labelled all 342 responses.

Two transferable rules:

- **An automated judge is a component with a recall number, not an oracle.** Measure it against a hand-labelled sample before trusting its verdicts, especially when it is a regex or keyword matcher over free text where negation and hedging ("no warnings in effect" vs "warnings in effect, but…") invert meaning.
- **A checker agent inherits the problem.** Swapping the regex for an LLM judge changes the error profile, not the need for calibration. If one agent checks another, the checker needs its own labelled set.

### Where this generalizes in multi-agent systems

Every handoff in a multi-agent system is a chance for a model to be asked something its context cannot support. The failure mode is identical to the single-agent case — a plausible claim in the absence of evidence — but the opportunity count is multiplied by the number of stages. That makes **evidence routing** (getting the authoritative record into the context of the stage that decides) the higher-leverage investment, and prompt tuning the lower-leverage one.

## Key Insights

1. Access to the authoritative source drove false reassurance from 38% to 0% with no prompt engineering; instructing the model to admit ignorance moved it from 38% to 45%.
2. Honesty instructions shift the phrasing of an answer, not the belief behind it; the unsafe claim survives inside the hedge.
3. Fixing an informational failure with prompt text is a category error — provision the data, or constrain the output so a claim without evidence cannot be emitted.
4. Automated evaluation is itself a component to validate: 53 of 57 real cases were missed by a regex checker, and its verdict inverted the conclusion.
5. These two findings compose: the more stages an agent graph has, the more places a model is asked to answer without evidence, and the more your scoring needs hand-verified calibration.

## Related Concepts

- [[Concepts/grounded-answer-validation|Grounded Answer Validation]] — validation of the final answer against its evidence, by inspecting question, query, rows and prose separately
- [[Concepts/semantic-layer-agent-grounding|Semantic Layer Agent Grounding]] — the architectural version of "route the right data to the right step"
- [[Concepts/dual-view-evidence-retrieval|Dual-View Evidence Retrieval]] — retrieval design for getting authoritative records into context
- [[Concepts/evidence-gated-reflect-loop|Evidence-Gated Reflect Loop]] — making the absence of evidence block the answer rather than colour it
- [[Concepts/agent-epistemic-vigilance-deficit|Agent Epistemic Vigilance Deficit]] — why a model does not spontaneously discount its own unsupported priors
- [[Concepts/handoff-contract-validation|Handoff Contract Validation]] — the boundary check that stops an unsupported claim travelling between stages
- [[Concepts/temporal-reasoning-evaluation-benchmarks|Temporal Reasoning Evaluation Benchmarks]] — evaluation design for time-sensitive claims, of which alert freshness is one case

## References

- Raw Article: [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]]
- Original: https://kadhar.dev/blog/multi-agent-systems-from-scratch
- Evaluation write-up: https://arxiv.org/abs/2611.05290
