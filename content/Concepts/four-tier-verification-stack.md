---
title: "Four-Tier Verification Stack (Code, Glance, Assay, Human)"
details: "An architectural pattern for assigning every check in an AI agent system to the lowest verification tier that can honestly answer it: code that exits zero or doesn't (the only tier allowed to block a deploy), a Glance-style small typed question answered with a probability in ~0.3s, an Assay-style model-judge reading an output against written levels, or a human reading the result. Checks migrate down the tiers as they earn labels — a human check becomes a Glance question once there are labels to calibrate against, and a Glance question becomes code once it's sharp enough to be a tool. Pairs deterministic checks first with model-judge fallbacks; treats judge disagreements as debt to be mined into deterministic rules."
tags:
  - concept
  - architecture-pattern
  - agent
  - evaluation
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-assay-2026-10-05]]"
---

# Four-Tier Verification Stack (Code, Glance, Assay, Human)

**Source:** [[Raw/lifeos-philosophy-assay-2026-10-05]] and [[Raw/lifeos-philosophy-glance-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Every check in an AI agent system sits on the lowest of four tiers that can honestly answer it. The tiers are ordered by speed and ambiguity: code is exact and instant, Glance is fast and probabilistic, Assay is slow and judgemental, human is the ground truth but expensive. The discipline is to use the cheapest one that catches the case.

## The four tiers

| Tier | What it is | Latency | Cost | Allowed to block a deploy? |
|---|---|---|---|---|
| **Code** | A tool that exits zero or doesn't. The only tier allowed to block a deploy. | instant | trivial | yes |
| **Glance** | One typed question, probability back in ~0.3s. | sub-second | small | no |
| **Assay** | A model reading an output against written levels. | seconds to minutes | moderate | no |
| **Human** | You, recognizing the thing when you see it. | minutes to hours | highest | yes (and always final) |

## Why the tiers in this order

Most checks should be exact. The default for a *worth-doing* system is to make fewer of them require judgment as the system builds them. **Deterministic checks come first**: they're fast, free, and objective. A model judge grades only what code can't reach, and that judge is treated as **debt**: calibrated against your own ratings before its verdicts count, and steadily replaced as its disagreements with you get mined into deterministic rules.

## Migration between tiers

Checks move down the tiers as they earn labels. A human check becomes a Glance question once there are labels to calibrate it against, and a Glance question becomes code once it is sharp enough to be a tool. The migration is how the system gets sharper over time.

The rule is that *every check has a home*, even when the home is "this needs a human." The one hard requirement is that the question gets answered — you can either name a test suite, or decline with a written reason. A check without a tier or a written decline is itself a fail.

## What this gives you

You can climb a hill you can see. You can have one answer to "is this version better than the previous one?" because you have a real number with a confidence interval, you measure reliability as passing every trial rather than one lucky run, and comparisons run paired — the same cases through both versions — so a verdict that one prompt beats another actually holds.

Coverage grows on its own. Skill runs are logged deterministically, failures become new test cases, and the system's integrity check reports which skills are measured, which declined, and which haven't answered yet. The question is built into how skills get made, so coverage grows by default.

## Why this matters for AI agent work

Without a verification stack, prompt changes are vibes. With one, a change either moved the score or it didn't. Forcing the tier assignment reveals the second category — checks you haven't actually quantified. That's most of the value: the system forces you to name what's testable, and that act of naming either produces a test or surfaces what you're pretending you know.

## Connection to other patterns

- [[Concepts/deterministic-hook-guardrails]] — the mechanism that enforces the lower tiers at fixed points so even an unreliable model can't skip them
- [[Concepts/ideal-state-artifact-isa]] — the criteria section names which tier each ISC belongs to
- [[Concepts/euphoric-surprise-as-success-metric]] — what the human tier is for

## Key Insights

1. **Code first.** If the question can be answered by a script, run the algorithm. Don't add preference.
2. **Treat judge disagreement as calibration work.** When Assay and human diverge, you haven't done a burndown; you've discovered a rule.
3. **Migration is the improvement.** The system gets sharper as checks migrate *from* human *to* Glance *to* code.
4. **Every check has a home.** Either a tier, or a written decline explaining why not.

## Related Concepts

- [[Concepts/deterministic-hook-guardrails]] — fixed-point enforcement of the lower tiers
- [[Concepts/ideal-state-artifact-isa]] — the document the tiers are applied to
- [[Concepts/euphoric-surprise-as-success-metric]] — what sits at the human tier

## References

- Raw: [[Raw/lifeos-philosophy-assay-2026-10-05]] and [[Raw/lifeos-philosophy-glance-2026-10-05]]
- Origin essay: [Early Thoughts on Jev](https://danielmiessler.com/blog/early-thoughts-on-jev)
- Doctrinal reference: [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Anthropic Engineering)