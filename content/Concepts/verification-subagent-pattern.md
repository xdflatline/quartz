---
title: "Verification Subagent Pattern"
details: "A dedicated subagent whose sole responsibility is blackbox-testing or validating the main agent's work. Verification requires minimal context transfer by nature, so the verifier succeeds without knowing how the artifact was built. The pattern has a dominant failure mode — the 'early victory problem' where the verifier declares success after one or two passing tests — which is mitigated by explicit 'MUST run the full suite' instructions."
tags:
  - concept
  - multi-agent
  - orchestration
  - agentic-system
source: "[[Raw/claude-building-multi-agent-systems-2026-01-23]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Verification Subagent Pattern

**Source:** [[Raw/claude-building-multi-agent-systems-2026-01-23]] — Anthropic Claude blog (Jan 23, 2026)
**Category:** Architecture Pattern
**Status:** Production-validated (canonical Anthropic recommendation)

---

## Overview

A dedicated agent whose sole responsibility is testing or validating the main agent's work. The verifier is spawned with the artifact, clear success criteria, and verification tools. It does not need to understand *why* the artifact was built as it was — only whether it meets the specified criteria.

Verification subagents succeed precisely because they sidestep the [[Concepts/context-centric-decomposition|telephone game problem]]: verification requires minimal context transfer by nature, so a verifier can blackbox-test a system without needing the full history of how it was built. This makes the verifier the textbook example of a context-isolatable subagent.

## When to use

Verification subagents remain valuable when:

- Using less capable orchestrators (more capable models like Claude Opus 4.5 increasingly evaluate subagent work directly)
- Verification requires specialized tools (test runners, lint configs, schema validators)
- You want explicit verification checkpoints enforced in the workflow

## Canonical shape

```python
def implement_with_verification(requirements: str, max_attempts: int = 3):
    for attempt in range(max_attempts):
        result = CodingAgent().implement_feature(requirements)
        verification = VerificationAgent().verify_implementation(
            requirements, result['files_changed']
        )
        if verification['passed']:
            return result
        requirements += f"\n\nPrevious attempt failed: {verification['issues']}"
    raise Exception(f"Failed verification after {max_attempts} attempts")
```

The verification loop re-feeds failures into the next attempt's requirements — turning the verifier into a feedback channel rather than just a gate.

## Applications

- **Quality assurance.** Running test suites, linting code, validating outputs against schemas.
- **Compliance checking.** Verifying documents meet policy requirements, checking outputs against rules.
- **Output validation.** Confirming generated content meets specifications before delivery.
- **Factual verification.** Having a separate agent verify claims or citations in generated content.

## The early victory problem

The most significant failure mode for verification subagents is **marking outputs as passing without thorough testing**. The verifier runs one or two tests, observes them pass, and declares success.

This is a real and reproducible failure. Anthropic's mitigation strategies:

- **Concrete criteria.** Specify "Run the full test suite and report all failures" rather than "make sure it works."
- **Comprehensive checks.** Require the verifier to test multiple scenarios and edge cases.
- **Negative tests.** Direct the verifier to attempt inputs that should fail and confirm they do.
- **Explicit instructions.** The literal instruction "You MUST run the complete test suite before marking as passed" is essential. Without explicit requirements for comprehensive validation, verification agents take shortcuts.

## Why "MUST run the full suite" works (and is necessary)

LLM agents optimize for the apparent success signal — if the user's instruction says "make sure it works," the natural completion is "yes, I ran a test, it works." Adding the literal word **MUST** and naming the specific command (`pytest --verbose`) anchors the verifier to a behavioral contract rather than a goal. This is the same [[Concepts/explicit-instruction-over-implicit-inference|explicit-instruction principle]] that applies to prompt engineering generally — the verifier is itself just an LLM being prompted.

## Distinction from related patterns

- **[[Concepts/test-design-subagent-isolation]]** — focuses on the testing methodology for isolated unit verification; overlaps but emphasizes test design rather than the agent architecture.
- **[[Concepts/subagent-context-isolation]]** — the broader mechanism of putting subtasks in separate contexts; verification is one application.
- A verification subagent is also a [[Concepts/context-centric-decomposition|context-centric decomposition]] — the textbook case where context genuinely isolates.

## Key insights

1. **Verification is the canonical legitimate split.** It is the cleanest example of context isolation in multi-agent systems because verification is intrinsically blackbox.
2. **The verifier is itself just a prompted LLM.** The "early victory problem" is not a verifier-specific bug — it's the same failure mode any LLM has when given vague instructions. The mitigation is to apply the same [[Concepts/explicit-instruction-over-implicit-inference|explicit-instruction principle]] you'd apply to any prompt.
3. **The re-feed loop turns verification into feedback.** Returning `verification['issues']` into the next attempt's requirements makes the verifier a continuous improvement signal, not just a one-shot gate.

## Related Concepts

- [[Concepts/context-centric-decomposition]] — verification is the textbook context-centric split
- [[Concepts/subagent-context-isolation]] — the isolation mechanism
- [[Concepts/multi-agent-decision-framework]] — when multi-agent is worth it at all

## References

- Raw article: [[Raw/claude-building-multi-agent-systems-2026-01-23]]
- Original: <https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them>