---
title: "One-Shot and Few-Shot Prompting"
details: "Prompt-engineering technique: include 1+ worked examples of the desired output in the prompt, demonstrating the format, tone, or style by example rather than description. One-shot is usually enough; escalate to few-shot only when one example doesn't pin down the behavior. Modern Claude 4.x+ pays very close attention to details in examples — make sure examples align with what you want."
tags:
  - concept
  - prompt-engineering
  - llm
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# One-Shot and Few-Shot Prompting

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic core technique)

---

## Overview

Examples aren't always necessary, but they shine when explaining concepts or demonstrating specific formats. **One-shot prompting** (one example) or **few-shot prompting** (a few examples) shows rather than tells, clarifying subtle requirements that are difficult to express through description alone.

## The example-to-behavior alignment warning

**Important note for modern models**: Claude 4.x and similar advanced models pay very close attention to details in examples. Ensure your examples align with the behaviors you want to encourage and minimize any patterns you want to avoid.

This is the most underappreciated prompt-engineering fact for modern LLMs. If your example has a subtle bug (e.g., you're showing how to summarize and your example summary contains an error), the model will faithfully reproduce the error. Examples are not just illustrations — they are training signal.

## Canonical example (Anthropic's article-summarization)

```
Here's an example of the summary style I want:

Article: [link to article about AI regulation]
Summary: EU passes comprehensive AI Act targeting high-risk systems. Key provisions include transparency requirements and human oversight mandates. Takes effect 2026.

Now summarize this article in the same style: [link to your new article]
```

The example pins down:
- Tone (declarative, factual)
- Length (one sentence per major point)
- Structure (prose, not bullets)
- Specificity (names actual provisions, doesn't generalize)

A description ("write a one-paragraph declarative factual summary") wouldn't pin down tone and length as precisely.

## When to use examples

- The desired format is easier to show than describe
- You need a specific tone or style
- The task involves subtle patterns or conventions
- Simple instructions haven't produced consistent results

## When to start with one-shot

**Pro tip**: Start with one example (one-shot). Only add more examples (few-shot) if the output still doesn't match your needs.

The reason: every example costs tokens, and a single good example is usually enough to demonstrate the pattern. Adding more examples is only worth it if the model fails to generalize from one. Escalating from 1 to 3 examples when 1 already works is wasted context budget.

## When examples mislead

- **Examples that contain the bug you want to avoid.** Modern Claude will faithfully reproduce the bug. Always check that your examples are actually correct.
- **Examples that are too polished.** If your example is unusually clean, the model may over-fit and produce output that looks "too good" — missing the natural variation that real tasks have.
- **Examples from a different domain.** An example from domain A applied to a task in domain B can confuse the model about what to generalize.
- **Too many examples.** Past 3-5, examples stop adding signal and start crowding out the actual instruction.

## When NOT to use examples

- The format is fully specifiable in words ("output JSON with these fields")
- The task is simple enough that one explicit instruction works
- Token budget is tight — examples are expensive

## Interaction with other techniques

- **[[Concepts/specificity-in-prompt-engineering]]** — examples are specificity at the output-shape level. Words can say "be concise"; an example shows what "concise" means in practice.
- **[[Concepts/response-prefilling-for-format-control]]** — when the format is rigid (JSON, XML), prefilling is more reliable than examples. Examples are for soft formats (tone, style, length).
- **[[Concepts/explicit-instruction-over-implicit-inference]]** — examples do *implicit* instruction (showing); explicit instruction does *explicit* (telling). Both work; explicit is cheaper; examples are more precise for subtle styles.

## Key insights

1. **One example beats a paragraph of description** for tone, style, and length. Description says "be concise"; an example shows what "concise" looks like.
2. **Examples are training signal in modern LLMs.** Make sure your example is correct, your tone is what you want, and you don't accidentally demonstrate the bug.
3. **Start with one, escalate to few only if needed.** The marginal value of the Nth example drops fast.

## Related Concepts

- [[Concepts/specificity-in-prompt-engineering] — examples are specificity at the output-shape level
- [[Concepts/response-prefilling-for-format-control]] — the stronger alternative for rigid formats
- [[Concepts/format-control-positive-framing]] — when you don't have room for an example

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>