---
title: "LifeOS: Assay (Philosophy)"
details: "The eval system: every output tested against a standard, so improvement is provable, not vibes. One of four verification tiers (code / glance / assay / human); calibrated against your own ratings; pairs deterministic checks first with model-judge fallbacks."
tags:
  - raw
  - agent
  - evaluation
source: https://ourlifeos.ai/philosophy/assay/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Assay

**Source:** [https://ourlifeos.ai/philosophy/assay/](https://ourlifeos.ai/philosophy/assay/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Assay

Every output tested against a standard, so better is a number you can trust.


Fig. 23·Five trials, one gate, then weighed against the standard

Assay is the eval system. To assay something is to test it against a standard and measure how good it is, the way a lab tests ore for how much gold it holds. That is what Assay does to AI output: it runs the work through fixed checks and reports how much of it met the bar.

Most AI setups improve by feel. You change a prompt, it seems better, you move on. LifeOS builds the measurement in: [every skill](https://ourlifeos.ai/philosophy/skill-system) answers the eval question when it’s created, and the ones that can be measured, are.

## Why it exists

You can’t [climb a hill](https://ourlifeos.ai/philosophy/hill-climbing) you can’t see. The whole system runs on verified iteration— [current state to ideal state](https://ourlifeos.ai/philosophy/current-to-ideal-state), checked at every step—and that only works when “better” is a number you can trust. Without evals, prompt changes are vibes. With them, a change either moved the score or it didn’t.

The other half is honesty about limits. Some work can’t be reduced to assertions—a piece of writing that has to land, a design that has to feel right. Forcing tests onto those produces fake rigor, which is worse than none. So the contract is a choice with a record: name a test suite, or decline with a written reason. The one hard requirement is that the question gets answered.

## Where it fits

Every check in LifeOS sits on the lowest of four tiers that can honestly answer it. Assay is the third:

- code→ a tool that exits zero or doesn't. The only tier allowed to block a deploy. exact
- glance→ one typed question, answered with a probability in about a tenth of a second. See [Glance](https://ourlifeos.ai/philosophy/glance). fast judgment
- assay→ a model reading an output against written levels, in seconds to minutes, calibrated against your own ratings. slow judgment
- human→ you, recognizing the thing when you see it. taste

Every [ISA](https://ourlifeos.ai/philosophy/the-isa) criterion that can only be judged carries an `eval` row, and [Bunker](https://ourlifeos.ai/philosophy/bunker) hands those rows to Assay from the same single command that runs the deterministic checks.

## How it works

Evals here follow [the same doctrine Anthropic publishes](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) for its own agent evaluation. A test case is an input plus assertions about the output. [Deterministic checks come first](https://danielmiessler.com/blog/early-thoughts-on-jev)—they’re fast, free, and objective. A model judge grades only what code can’t reach, and it’s treated as debt: calibrated against your own ratings before its verdicts count, and steadily replaced as its disagreements with you get mined into deterministic checks.

The scores are real statistics. Every suite reports its pass rate with a confidence interval, reliability is measured as passing every trial rather than one lucky run, and comparisons run paired—the same cases through both versions—so a verdict that one prompt or model beats another actually holds.

```
bun ~/.claude/skills/Assay/Tools/EvalRunner.ts -s <suite>
```

Coverage grows on its own. Skill runs are logged deterministically, failures become new test cases, and the system’s integrity check reports which skills are measured, which declined, and which haven’t answered yet. The question is built into how skills get made, so coverage grows by default.

[Full documentationLifeOS Testing Doctrine →](https://docs.ourlifeos.ai/Testing__TestingDoctrine)
