---
title: "Format Control by Positive Framing"
details: "Prompt-engineering principle for controlling output format: state what the model SHOULD do ('write in flowing prose paragraphs') instead of what it should NOT do ('don't use markdown'). Three mechanisms: positive framing, prompt-style/output-style matching, and explicit detailed formatting instructions. The negative-instruction anti-pattern is the most common prompt mistake."
tags:
  - concept
  - prompt-engineering
  - llm
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Format Control by Positive Framing

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic advanced technique)

---

## Overview

Three mechanisms for controlling the output's format, all oriented around *what the model should do* rather than *what it should avoid*:

1. **Positive framing** — "write in flowing prose paragraphs" not "don't use markdown"
2. **Style matching** — the prompt's own style influences the output's style; reduce markdown in the prompt if you want less markdown in the output
3. **Explicit detailed instructions** — name the format rules precisely

## The negative-instruction anti-pattern

The most common prompt mistake: telling the model what NOT to do.

**Wrong**: "Do not use markdown in your response"
**Right**: "Your response should be composed of smoothly flowing prose paragraphs"

The wrong version leaves the model to guess what positive behavior replaces the forbidden one. The right version names the replacement directly.

## Why negative instructions fail

LLMs process the *content* of an instruction, not its negation. "Do not use markdown" registers as "use markdown" + a not-operator that the model has to apply. That's two operations. "Write in flowing prose" is one operation.

The same effect applies in reverse for positive instructions — "Do not just say hello" is interpreted as "say hello" by most readers, including LLMs.

## The detailed-instructions pattern

For tight control over the output format:

```
When writing reports or analyses, write in clear, flowing prose using complete paragraphs. Use standard paragraph breaks for organization. Reserve markdown primarily for inline code, code blocks, and simple headings.

DO NOT use ordered lists or unordered lists unless you're presenting truly discrete items where a list format is the best option, or the user explicitly requests a list.

Instead of listing items with bullets, incorporate them naturally into sentences. Your goal is readable, flowing text that guides the reader naturally through ideas.
```

Note: even Anthropic's detailed-format instructions use one negative ("DO NOT use ordered lists...") — but it's wrapped in a positive frame ("Instead, incorporate them naturally into sentences"). The structure is positive-first, negative-as-edge-case.

## Prompt style ↔ output style

The formatting style used in your prompt may influence the AI's response style. If you want minimal markdown in the output, reduce markdown in the prompt.

This is subtle but real. A prompt with extensive `**bold**` headers and bullet lists primes the model to produce a similar output. A prompt with prose paragraphs and minimal formatting primes prose output. Match deliberately.

## When positive framing is not enough

- **Hard constraints** ("output valid JSON only") need [[Concepts/response-prefilling-for-format-control|prefilling]] for reliable enforcement. Positive framing can describe JSON; only prefill guarantees JSON.
- **Multi-format outputs** (some markdown, some prose) where positive instructions conflict — pick the dominant one and use prefilling to anchor the structure.
- **Output format is dictated by a downstream tool** (a parser expecting specific syntax) — prefill or schema-constrained decoding is more reliable than prose instructions.

## Interaction with other techniques

- **[[Concepts/explicit-instruction-over-implicit-inference]]** — positive framing is a special case of explicit instruction. State what you want, not what you don't want.
- **[[Concepts/response-prefilling-for-format-control]]** — for hard format constraints, prefilling is the stronger mechanism.
- **[[Concepts/specificity-in-prompt-engineering]]** — format constraints are a dimension of specificity.

## Common anti-patterns

| Anti-pattern | Better |
| --- | --- |
| "Don't use bullet points" | "Write in flowing prose paragraphs" |
| "Avoid markdown" | "Use prose with minimal formatting" |
| "Don't be verbose" | "Be concise — target 2-3 sentences" |
| "No preamble, just the answer" | "Begin your response with the answer" |
| "Don't use lists" | "Write the items as a flowing paragraph" |

Notice the pattern: the right version replaces the forbidden behavior with a named alternative.

## Key insights

1. **"Do X" is one operation; "don't do Y" is two.** Simpler instructions are more reliably executed.
2. **Prompt style primes output style.** Match deliberately.
3. **For hard format constraints, use prefill.** Positive framing describes; prefill enforces.

## Related Concepts

- [[Concepts/explicit-instruction-over-implicit-inference]] — the parent principle
- [[Concepts/response-prefilling-for-format-control]] — the stronger enforcement lever when positive framing isn't enough
- [[Concepts/specificity-in-prompt-engineering]] — format constraints are a specificity dimension

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>