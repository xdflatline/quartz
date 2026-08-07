---
title: "ScientistOne"

details: "ScientistOne addresses a known failure mode of AI Scientist: plausible manuscripts with fabricated citations, implementation drift, or weak experimental results. By making verifiability a first-class design constraint and auditing every claim with Chain-of-Evidence checks, ScientistOne aims to surface fabrication before the manuscript is published. A direct response to the failure modes catalogued in [[Raw/lilianweng-harness-engineering-2026-07-04]]."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2605.26340
---

# ScientistOne

**Source:** Meng et al., "ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence," arXiv:2605.26340, 2026.

## Overview

A variant of [[Entities/ai-scientist]] where **verifiability is the central design constraint**. Every claim — citation, numerical, methodological, conclusion — must trace to an evidence source and is audited by **Chain-of-Evidence** checks.

## Why It Exists

AI Scientist demonstrates that an expert-designed harness can produce a plausible manuscript. But plausible ≠ correct. The known failure modes are:

- **Fabricated citations** — the model invents references that don't exist
- **Implementation drift** — the code does not match the method described in the paper
- **Weak experimental results** — the numbers don't support the claims
- **Wrong conclusions** — the manuscript interprets results incorrectly

ScientistOne addresses these by requiring every claim to be backed by a traceable evidence source, then auditing the claim-evidence pair with a Chain-of-Evidence check.

## Chain-of-Evidence

A pattern where each claim in the manuscript is linked to a specific evidence source (a file, a number, a paper section, a code path), and the link is verified by an automated check. The audit is structural, not just lexical: it verifies the claim is *consistent* with the evidence, not just that the evidence is mentioned.

## Related

- [[Entities/ai-scientist]] — the parent system
- [[Concepts/open-rsi-bottlenecks]] — bottleneck 1 (weak evaluators) is the issue ScientistOne attacks
- [[Concepts/evidence-driven-harness-edits]] — adjacent evidence-driven pattern in AHE
