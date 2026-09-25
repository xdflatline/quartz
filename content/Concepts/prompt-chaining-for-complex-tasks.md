---
title: "Prompt Chaining for Complex Tasks"
details: "Advanced technique: break a complex task into sequential prompts, each handling one stage, with the output of each feeding into the next. Trades latency (multiple API calls) for accuracy and reliability. The right pattern when a single prompt produces inconsistent results on a multi-stage task. Distinct from subagents — chaining is single-context with multiple user turns; subagents have separate contexts."
tags:
  - concept
  - prompt-engineering
  - orchestration
  - agent
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Prompt Chaining for Complex Tasks

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Architecture Pattern
**Status:** Production-validated (Anthropic advanced technique)

---

## Overview

Unlike prefilling, examples, and chain-of-thought (all single-prompt techniques), **prompt chaining is multi-prompt by design**. A complex task is broken into sequential prompts; each prompt handles one stage; the output of each feeds into the next. This trades latency (multiple API calls) for accuracy and reliability on multi-stage tasks.

## Canonical shape (Anthropic's research-summary example)

1. **First prompt**: "Summarize this medical paper covering methodology, findings, and clinical implications."
2. **Second prompt**: "Review the summary above for accuracy, clarity, and completeness. Provide graded feedback."
3. **Third prompt**: "Improve the summary based on this feedback: [feedback from step 2]"

Each stage adds refinement through focused instruction. The summary improves through three specialized passes rather than one general "write a good summary" attempt.

## When to use chaining

- You have a complex request that needs breaking down into steps
- You need iterative refinement (draft → review → revise)
- You're doing multi-stage analysis where intermediate results feed forward
- **Intermediate validation adds value** — the review step in the research-summary example is itself useful output, not just a means to a better summary
- A single prompt produces inconsistent results on the same task

## When NOT to use chaining

- The task is simple enough for one prompt with [[Concepts/specificity-in-prompt-engineering|specificity]] and [[Concepts/explicit-instruction-over-implicit-inference|explicit instruction]]
- The stages don't actually have intermediate validation value (no review step, no checkpoint)
- Latency matters more than accuracy (chat UX where users wait between turns)
- The chain would be 5+ stages — at that point, you're building an agent loop, not prompting

## Trade-offs

| Dimension | Single prompt | Chained prompts |
| --- | --- | --- |
| Latency | Low (1 round-trip) | High (N round-trips) |
| Accuracy on complex tasks | Lower, inconsistent | Higher, consistent |
| Cost (tokens) | Lower per task | Higher (N× tokens) |
| Debugging | Hard — error attribution is unclear | Easy — each stage is inspectable |
| Failure mode | Model gives up or fabricates | One stage fails; previous stage's output is still salvageable |

## Distinction from subagent isolation

This is **not** the same as multi-agent. Chaining is single-context: the model sees all prior turns in the same conversation. Subagent isolation uses separate conversations. Trade-offs:

- **Chaining**: model has full context of prior stages. Best when stages depend on each other's reasoning.
- **Subagent isolation**: each stage has a clean context. Best when stages are independent and context volume would pollute.

For the research-summary example, chaining is right — the review stage needs to see the original summary to evaluate it. Subagent isolation would force you to re-send the summary as input.

## Distinction from other techniques

- **[[Concepts/response-prefilling-for-format-control]]** — single-prompt; controls the *start* of the output.
- **[[Concepts/chain-of-thought-prompting]]** — single-prompt; controls the *reasoning before* the output (in `<thinking>` tags or implicit).
- **[[Concepts/one-shot-and-few-shot-prompting]]** — single-prompt; controls the *style* of the output by example.

Chaining is the only one of these that requires multiple round-trips. The cost is real; the benefit (focused, validated stages) is also real.

## Implementation patterns

```python
# Naive chaining — feed forward the prior output
summary = llm(prompt_1, input=paper)
feedback = llm(prompt_2, input=summary)
final = llm(prompt_3, input=f"{feedback}\n\nOriginal: {summary}")

# Programmatic chaining — use intermediate output as control flow
if not llm_evaluator(feedback, threshold=0.8):
    final = llm_with_feedback(prompt_3, feedback=feedback)
else:
    final = summary
```

The second pattern uses intermediate validation to gate later stages — a more sophisticated version of the basic forward chain.

## Key insights

1. **Chaining is for focus, not for length.** The reason to chain is that each prompt can be *focused* on one thing and do it well. A single mega-prompt trying to do summary+review+revision does each worse.
2. **Intermediate output is the main benefit.** If you don't actually want the intermediate output (the review, the analysis), chaining is overkill — just write one better prompt.
3. **Debuggability is underrated.** Chaining makes it obvious which stage failed. With one mega-prompt, debugging "why did the output come out wrong" is much harder.

## Related Concepts

- [[Concepts/chain-of-thought-prompting]] — single-prompt alternative for tasks needing reasoning
- [[Concepts/response-prefilling-for-format-control]] — single-prompt format enforcement
- [[Concepts/verification-subagent-pattern]] — multi-agent analogue for validation; chaining is the single-context analogue
- [[Concepts/subagent-context-isolation]] — when each stage actually needs its own context (not just its own prompt)

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>