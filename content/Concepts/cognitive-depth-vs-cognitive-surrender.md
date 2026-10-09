---
title: "Cognitive Depth vs Cognitive Surrender"
details: "Two opposite failure modes that emerge when humans use AI to assist software work. Cognitive depth is the gradual erosion of a developer's own ability to reason about the system; cognitive surrender is the immediate 'looks good to me, ship it' approval without ever engaging critically. Newman borrows the cognitive-depth framing from Margaret Ann Storey's work on cognitive debt, and treats cognitive surrender as a cultural / LGTM-pattern regression enabled by AI assistants."
tags:
  - concept
  - software-engineering
  - agent
created: 2026-10-09
updated: 2026-10-09
type: concept
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

## Definition

| Term | Mechanism | Time horizon | Symptom |
|------|-----------|--------------|---------|
| **Cognitive depth** | As people delegate more reasoning to AI, their own ability to evaluate outputs erodes. | Long, gradual. | "That doesn't feel right" — the subjective, often-unpinpointable sense that something is off, which disappears once the human hasn't done the work themselves in a long time. |
| **Cognitive surrender** | Humans approve AI output without engaging at all. | Immediate, per-PR. | LGTM-equivalent: the reviewer just accepts what the AI produced. |

## Why both matter

- **Cognitive depth** is the slow-burn version. Pairing worked as a knowledge-sharing mechanism because each human kept the system in their head. When AI replaces pairing, the *shared* mental model breaks down first, then the individual one. Margaret Ann Storey's term for the resulting backlog is **cognitive debt** — analogous to technical debt but living in the team's reasoning capacity rather than in code.
- **Cognitive surrender** is the acute version. The LLM "deletes the database" problem isn't a model issue — it's a human-in-the-loop issue. Removing the expert from the loop and replacing them with an approver is the worst-case pattern: one funnel, one signer, no actual review.

## The human-in-the-loop distinction (Doctorow framing)

Newman paraphrases Cory Doctorow's distinction:

- **LLM as augmentation** — *You* do the work; the LLM points at something you might have missed ("look over there"). Expert stays in the loop.
- **LLM as approver** — *LLM* does the work; *you* sign off. Expert is removed from the loop; sign-off becomes rubber-stamping. The organization fires 9 of 10 oncologists and the one remaining has to "approve" everything. This is the dangerous version.

## Mitigations

- **Keep humans in the loop on the parts that matter.** Modular boundaries let AI run loose inside safe modules; humans spend their cognitive budget on the *gaps between* modules.
- **Make the architecture explicit in the code.** George Fairbanks' "architecturally evident coding style" pattern.
- **Don't abandon code review wholesale.** Even when the volume is higher, the alternative (LGTM by default) is worse.
- **Force the spec to capture tacit knowledge.** Spec-driven development is only viable if the team can externalize the "feels off" judgements into written clauses. Otherwise the spec encodes only what was easy to write down.

## Related Concepts

- [[Concepts/lit-where-good-looks-like]] — If you can't define good for the module, cognitive surrender is the inevitable outcome
- [[Concepts/production-is-truth]] — The safety net that catches the bugs cognitive surrender lets through