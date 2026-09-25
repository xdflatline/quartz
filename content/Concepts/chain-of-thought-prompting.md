---
title: "Chain-of-Thought Prompting"
details: "Advanced prompt-engineering technique: instruct the model to reason step-by-step before answering. Three implementations — basic ('think step-by-step'), guided (specify the stages), structured (use tags to separate reasoning from final answer). For Claude 4.x+ when extended thinking is available, prefer that; CoT is the fallback when extended thinking isn't available or transparent reasoning is needed for review."
tags:
  - concept
  - prompt-engineering
  - llm
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Chain-of-Thought Prompting

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic advanced technique)

---

## Overview

Chain-of-thought (CoT) prompting instructs the model to **reason step-by-step before producing the final answer**. The reasoning can be implicit (in the same output) or explicit (in `<thinking>` tags, before the final answer). CoT is most valuable for complex analytical tasks that benefit from structured thinking.

## The modern shift: extended thinking

Claude 4.x+ has an [extended thinking](https://www.anthropic.com/news/visible-extended-thinking) feature that automates structured reasoning. **When extended thinking is available, it is generally preferable to manual CoT prompting.** Manual CoT remains valuable when:

- Extended thinking isn't available (e.g., the free Claude.ai plan)
- You need transparent reasoning you can review
- The task requires multiple analytical stages with specific framing
- You want to ensure the model considers specific factors

## Three implementations

### 1. Basic CoT

Simply add "Think step-by-step" to your instructions.

```
Draft personalized emails to donors asking for contributions to this year's Care for Kids program.

Program information:
<program>
{{PROGRAM_DETAILS}}
</program>

Donor information:
<donor>
{{DONOR_DETAILS}}
</donor>

Think step-by-step before you write the email.
```

Minimal scaffolding; lets the model decide how to reason.

### 2. Guided CoT

Specify the reasoning stages explicitly.

```
Think before you write the email. First, think through what messaging might appeal to this donor given their donation history. Then, consider which aspects of the Care for Kids program would resonate with them. Finally, write the personalized donor email using your analysis.
```

Best when you have specific reasoning steps in mind and don't want the model to skip any.

### 3. Structured CoT

Use tags to separate reasoning from the final answer — produces parseable reasoning output.

```
Think before you write the email in <thinking> tags. First, analyze what messaging would appeal to this donor. Then, identify relevant program aspects. Finally, write the personalized donor email in <email> tags, using your analysis.
```

Best when downstream code needs to extract the reasoning separately from the final answer, or when you want the user to be able to inspect the reasoning.

## When to use which

- **Basic CoT**: minimal scaffolding, you trust the model to reason well
- **Guided CoT**: you have specific stages the model should not skip (compliance reviews, multi-factor analysis)
- **Structured CoT**: downstream parsing of the reasoning, or transparency for the user

## When CoT backfires

- **Simple tasks** where reasoning is overhead — "what is 2+2" doesn't need CoT
- **Tasks where reasoning can mislead** — for some tasks, the model produces plausible-sounding but wrong reasoning that the final answer then follows. Guided CoT with well-chosen stages mitigates this.
- **Token efficiency matters** — CoT adds tokens for the reasoning. For high-volume API calls where every token matters, the cost may not be worth it.

## Interaction with other techniques

- **[[Concepts/prompt-chaining-for-complex-tasks]]** — chaining is for multi-stage tasks where the stages are separate prompts. CoT is for tasks where the stages happen inside one prompt.
- **[[Concepts/response-prefilling-for-format-control]]** — for structured CoT with `<thinking>` / `<email>` tags, prefilling can pre-seed the opening tag.
- **[[Concepts/extended-thinking-vs-manual-cot]]** — the explicit decision rule for which to use when both are available.

## Key insights

1. **CoT is the fallback, not the default.** With Claude 4.x+ extended thinking, manual CoT is the technique you reach for when extended thinking isn't an option.
2. **Guided > basic for high-stakes tasks.** If you have specific reasoning stages, naming them prevents the model from skipping the hard parts.
3. **Structured CoT is for machine-readable reasoning.** When downstream code needs to inspect the reasoning, `<thinking>` tags turn the model's scratchpad into parseable output.

## Related Concepts

- [[Concepts/prompt-chaining-for-complex-tasks]] — for stages that should be separate prompts
- [[Concepts/response-prefilling-for-format-control]] — for pre-seeding structured CoT tags
- [[Concepts/explicit-instruction-over-implicit-inference]] — CoT is itself a form of explicit instruction ("show your reasoning")

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>