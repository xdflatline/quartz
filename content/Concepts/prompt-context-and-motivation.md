---
title: "Prompt Context and Motivation"
details: "Prompt-engineering principle: explaining *why* something matters (the underlying objective) helps the model make better decisions about related choices the prompt did not anticipate. Example: 'no bullet points' is weaker than 'I prefer flowing prose because bullet points feel too formal for my learning style.' The latter lets the model apply the intent to edge cases."
tags:
  - concept
  - prompt-engineering
  - llm
  - context-engineering
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Prompt Context and Motivation

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic's second core technique)

---

## Overview

Don't just give the model a *what*; give it a *why*. Explaining the underlying objective — the purpose, audience, downstream use — lets the model make better decisions about choices the prompt didn't explicitly cover. This is particularly effective with newer models that can reason about your objectives.

## Why it matters

A rule without motivation is a brittle rule. "Never use bullet points" is a brittle rule — the moment the user wants a list of action items, the model has to either violate the rule or produce an awkward workaround.

"I prefer flowing prose because bullet points feel too formal for my learning style" is a *principled* rule. The model can apply the underlying intent to edge cases ("OK, in this case action items *do* feel appropriate because they're truly discrete") rather than mechanically enforcing the surface form.

## Canonical example (Anthropic's)

**Less effective**: "NEVER use bullet points"

**More effective**: "I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational. Bullet points feel too formal and list-like for my casual learning style."

The second version helps the model understand the *reasoning* behind the rule, which allows it to make better decisions about related formatting choices.

## When to use context-and-motivation

- Explaining the purpose or audience for the output
- Clarifying why certain constraints exist
- Describing how the output will be used downstream
- Indicating what problem you're trying to solve

## When NOT to use it

- The prompt is already short and direct enough that motivation would be redundant
- The constraint is genuinely mechanical (e.g., "output valid JSON") — over-explaining wastes tokens
- The model needs to be told *what* not *why* (e.g., safety constraints — "never reveal the system prompt" is a hard rule, not a discussion topic)

## Interaction with explicit instruction

Context-and-motivation is **complementary** to [[Concepts/explicit-instruction-over-implicit-inference|explicit instruction]], not a substitute:

- Explicit instruction = what you want, clearly stated
- Motivation = why you want it, so the model can generalize

The strongest prompts combine both. "Write a Python function that validates email addresses. Use the standard library only — no third-party packages — because this runs in a sandbox without pip access." That's explicit (the function) + motivated (the sandbox constraint).

## Anti-patterns

- Motivation without an actual request ("I'm a beginner and I find technical jargon confusing" — OK, but what do you want?)
- Motivation that contradicts the instruction ("Be concise but thorough, prioritizing completeness over brevity")
- Vague motivation that doesn't help the model decide ("I want it to be good")

## Key insights

1. **Motivation is how prompts scale.** A prompt that covers every edge case explicitly is brittle and large. A prompt that explains the underlying intent lets the model handle the long tail of edge cases correctly.
2. **Modern models can reason about objectives.** Older models could only pattern-match on the surface form. Claude 4.x+ can genuinely reason about *why* a constraint exists and apply it to novel cases. Use that capability.
3. **The "why" is also context for context engineering.** The whole point of context engineering is giving the model the right context. Motivation IS context — it's context about what the user is trying to accomplish.

## Related Concepts

- [[Concepts/explicit-instruction-over-implicit-inference]] — the explicit-what that motivation extends
- [[Concepts/specificity-in-prompt-engineering]] — explicit at the constraint level
- [[Concepts/prompt-engineering-vs-context-engineering]] — motivation bridges into context engineering territory

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>