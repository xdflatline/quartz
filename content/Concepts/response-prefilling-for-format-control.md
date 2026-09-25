---
title: "Response Prefilling for Format Control"
details: "Advanced prompt-engineering technique: prepend an assistant message to the conversation (in the API) that starts the model's response — typically with an opening brace, a tag, or a fixed prefix. The model continues from where you started it, producing format-clean output without preambles. The strongest single technique for enforcing structured output (JSON, XML, no preamble)."
tags:
  - concept
  - prompt-engineering
  - llm
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Response Prefilling for Format Control

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic API feature, recommended for structured output)

---

## Overview

Prefilling is the technique of **starting the model's response for it**. You prepend an assistant message with the beginning of the desired output — typically an opening brace `{`, a tag, or a fixed prefix — and the model continues from there. This is the strongest single lever for enforcing structured output formats (JSON, XML) and skipping preambles ("Here's the JSON you requested:").

## How it works

In the Anthropic API, you add an assistant message before the final user message:

```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}  # prefill
]
```

The model continues from `{` and produces only valid JSON, no preamble.

## When to use prefilling

- The AI needs to output JSON, XML, or other structured formats
- You want to skip conversational preambles ("Sure! Here's...") and get straight to content
- You need to maintain a specific voice or character from the start of the response
- You want to control how the AI begins its response (e.g., always start with a heading)

## When prefilling is the wrong tool

- The chat interface (no API access) — you can't prepend an assistant message there. Workaround: be very explicit in the user message: "Begin your response with `{`" (see [[Concepts/explicit-instruction-over-implicit-inference]])
- You want free-form prose — prefilling a prose starter will bias the model's style
- The prefill is so long that it's basically writing the response yourself

## Worked example (Anthropic's combined prompt)

```
Extract key financial metrics from this quarterly report and present them in JSON format.

I need this data for automated processing, so it's critical that your response contains ONLY valid JSON with no preamble or explanation.

Use this structure:
{
  "revenue": "value with units",
  "profit_margin": "percentage",
  "growth_rate": "percentage"
}

If any metric is not clearly stated in the report, use null rather than guessing.

Begin your response with an opening brace: {
```

This is the **[[Concepts/explicit-instruction-over-implicit-inference|explicit]] + [[Concepts/specificity-in-prompt-engineering|specific]] + [[Concepts/permission-to-say-i-dont-know|permission-to-say-I-don't-know]] + prefill** combination. The prefill is the final guarantee that the output starts with `{`, even if the explicit instruction is misread.

## Prefill patterns

| Use case | Prefill |
| --- | --- |
| JSON output | `{` or `{"key":` |
| XML output | `<root>` or `<response>` |
| Skip preamble, start with content | `\n\n` (a blank line, forcing content) |
| Maintain persona | First-person continuation: `I think...` or `As a financial advisor, ` |
| Code with no commentary | ``` (markdown code fence open) |

## Interaction with other techniques

- **[[Concepts/format-control-positive-framing]]** — prefilling and positive framing ("output JSON" not "don't output prose") are complementary. Prefill enforces; positive framing shapes.
- **[[Concepts/prompt-chaining-for-complex-tasks]]** — prefilling is a *single-prompt* technique. Chaining is for tasks where prefilling isn't enough and you need multiple sequential prompts.
- **[[Concepts/chain-of-thought-prompting]]** — if you need reasoning before the structured output, prefilling should be on the reasoning block, not the final answer. Or use structured CoT with `<thinking>` / `<email>` tags.

## Key insights

1. **Prefill is the strongest enforcement lever.** Words in the user prompt can be misread; a literal `{` at the start of the assistant turn is unambiguous.
2. **Prefill is API-only in pure form.** Chat-interface approximations (e.g., "begin your response with `{`") work but are weaker because they're still user-side instructions.
3. **Use prefill for format, not content.** Prefilling the *content* is writing the response yourself. Prefill the *opening* and let the model write the substance.

## Related Concepts

- [[Concepts/format-control-positive-framing]] — the prose-only alternative when prefilling isn't available
- [[Concepts/prompt-chaining-for-complex-tasks]] — when one-prompt prefilling isn't enough
- [[Concepts/chain-of-thought-prompting]] — for tasks needing reasoning before structured output

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>