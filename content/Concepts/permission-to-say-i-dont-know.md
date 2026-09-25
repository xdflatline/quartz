---
title: "Permission to Say \"I Don't Know\""
details: "Prompt-engineering pattern: explicitly grant the model permission to express uncertainty ('If the data is insufficient to draw conclusions, say so rather than speculating'). Directly reduces hallucinations. Also a design principle for verification subagents and tools that should return null on missing data rather than guess."
tags:
  - concept
  - prompt-engineering
  - llm
  - agent
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Permission to Say "I Don't Know"

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic core technique)

---

## Overview

LLMs have a strong default toward producing a confident-sounding answer even when the underlying data doesn't support one. The fix: **explicitly grant the model permission to say "I don't know," "the data is insufficient," or to return `null` for missing values**. This single instruction reliably reduces hallucinations and increases the trustworthiness of outputs.

## The pattern

The simplest application:

> "Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating."

That's the entire technique. The instruction adds one sentence and meaningfully changes the model's behavior.

## Why it works

LLMs optimize for producing an answer. Without an explicit "you're allowed to abstain" instruction, the model interprets "identify trends" as a requirement to produce trends, and will invent them if the data doesn't support any.

The "permission to abstain" instruction changes the success criterion from "produce trends" to "produce trends OR acknowledge insufficiency." The model no longer has to choose between satisfying the surface instruction and being honest about the data.

## Variations on the pattern

- **For data extraction**: "If any metric is not clearly stated in the report, use `null` rather than guessing."
- **For analytical tasks**: "If you can't determine this with confidence, say what additional information you would need."
- **For code generation**: "If the requirements are ambiguous, list the ambiguities rather than picking one interpretation."
- **For verification subagents**: "Mark as INSUFFICIENT_EVIDENCE rather than PASS if you can't run the full test suite."

## Interaction with explicit instruction

This is a special case of [[Concepts/explicit-instruction-over-implicit-inference]]. The default behavior (produce an answer) is what the explicit instruction is correcting. Without the explicit override, the model defaults to the surface-form answer.

The permission is also a kind of [[Concepts/specificity-in-prompt-engineering|specificity]] — it's specifying an output behavior ("abstain when data is insufficient") that the model would otherwise have to guess at.

## Connection to verification subagents

The [[Concepts/verification-subagent-pattern|verification subagent pattern]] has an analogous failure mode — the "early victory problem" — where the verifier marks outputs as passing after one or two tests. The mitigation is similar in spirit:

> "You MUST run the complete test suite before marking as passed."

This is the verifier equivalent of permission-to-say-I-don't-know: explicitly carve out the "I didn't verify thoroughly" outcome as a legitimate verdict. Without that, the verifier defaults to "PASS" because that's the surface instruction.

## Where this is most valuable

- **Domains where hallucinations are costly** — medical, legal, financial, scientific. The cost of a wrong confident answer is much higher than the cost of a "I don't know."
- **Long-context tasks** where the model might lose track of which parts of the input it actually parsed
- **Structured data extraction** where `null` is a valid value but the model is tempted to fill in plausible numbers

## Anti-patterns (when this can backfire)

- **Permission to abstain without permission to ask.** If the user genuinely needs an answer, the model should follow up with what additional information it would need, not just stop.
- **Over-broad abstention.** Some tasks have an obligation to give a best-effort answer even when uncertain (e.g., real-time decision support). Adding "or say I don't know" to a prompt where the user explicitly wants the model's best guess degrades the output.
- **Permission for the wrong audience.** For internal tools where you want the model to flag uncertainty, the permission helps. For end-user-facing assistants where "I don't know" sounds evasive, the permission can hurt UX.

## Key insights

1. **One sentence changes behavior.** The cheapest hallucination reduction technique known. Add it to any prompt where the cost of a wrong confident answer is non-trivial.
2. **Permission is not the same as encouragement.** The instruction is "you MAY abstain," not "you SHOULD abstain." The model should still answer when it has the data.
3. **Pair with structured uncertainty.** Saying "I don't know" is the human-language form. The structured form is returning `null`, marking `INSUFFICIENT_EVIDENCE`, listing ambiguities. Pick whichever the downstream consumer can act on.

## Related Concepts

- [[Concepts/explicit-instruction-over-implicit-inference]] — the broader principle
- [[Concepts/specificity-in-prompt-engineering]] — for cases where the right behavior is `null` rather than a guess
- [[Concepts/verification-subagent-pattern]] — analogous pattern for verification agents

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>