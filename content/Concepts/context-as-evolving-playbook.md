---
title: "Context as Evolving Playbook (ACE)"
detail: "Agentic Context Engineering (Zhang et al. 2025): context is an evolving playbook of structured (id, description) bullets, not a lengthening prompt. Generator/Reflector/Curator roles. Curator outputs itemized bullets merged deterministically to prevent context collapse and brevity bias."
details: "ACE is a context-engineering method that treats the LLM context as a structured logbook of (identifier, description) bullets, refined and deduplicated over time. Three roles: Generator produces task trajectories with reference to bullets; Reflector distills insights from successes and failures; Curator updates the playbook with incremental, itemized entries. The key design rule that prevents context collapse: the curator does NOT rewrite a full prompt blob — it outputs structured bullets merged by deterministic logic. This separates the context-management workflow from the artifact content and gives the system a long-lived, inspectable, growing memory that survives many rollouts."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Context as Evolving Playbook (ACE)

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Learning Mechanism
**Status:** Active research area (ICLR 2026)

---

## Overview

**Agentic Context Engineering (ACE; Zhang et al. 2025)** treats context as an **evolving playbook of bullet points** rather than a lengthening prompt. The playbook is structured as `(identifier, description)` pairs, refined and deduplicated periodically. Three roles (Generator, Reflector, Curator) collaborate to grow the playbook from rollout experience.

## Core Content

### The Three Roles

| Role | Job |
|------|-----|
| **Generator** | Produces task trajectories, with reference to current bullet points |
| **Reflector** | Distills insights from successful AND failed trajectories |
| **Curator** | Updates the structured context with incremental, itemized entries `(id, description)` |

The loop: Generator attempts a task → Reflector analyzes success/failure → Curator updates the playbook → next iteration starts with a richer playbook.

![ACE framework](assets/lilianweng-harness-2026-07-04/ace.png)
*ACE framework. (Image source: Zhang et al. 2025)*

### The Key Design Rule: Structured Bullets, Not Prompt Blobs

> To prevent **context collapse** and **brevity bias** during iterative rewrites, the curator does **NOT rewrite a full prompt blob**. It outputs a collection of structured, itemized bullets in the form of `(identifier, description)`, merged into the structured logbook with **deterministic logic**.

This is the single most important design choice in ACE. Without it:

- **Context collapse** — each rewrite loses detail because the model is asked to compress everything into one prompt.
- **Brevity bias** — the model prefers shorter rewrites, dropping edge cases and rare-but-important facts.

By using deterministic merge of structured bullets, ACE keeps the playbook **growing monotonically** (with deduplication) rather than oscillating as full rewrites would.

### What Goes in a Bullet

- **Identifier** — stable handle (slug or hash) for the entry
- **Description** — self-contained description of the rule, fact, or pattern

Bullets can be:

- **Declarative** ("When parsing CSV, always check for trailing comma")
- **Procedural** ("If the test fails with 5xx, retry once with backoff")
- **Negative** ("Do NOT use the legacy /v1 API — it is deprecated")
- **Reference** ("See paper X, section 3.2 for the threshold choice")

### When to Use ACE

- Long-running agents that need to remember past failures and successes
- Workflows with many edge cases that the prompt can't enumerate up front
- Systems where human review of the playbook is desired (the bullets are auditable)

### When ACE is NOT Enough

ACE learns insights from rollouts, but the **update rules and overall workflow are still handcrafted**. To move toward a more self-improving loop, MCE (see [[Concepts/bi-level-context-skill-optimization]]) separates the mechanism from the content and runs skill evolution at the meta level.

## Key Insights

1. **Structured beats blob.** The `(id, description)` format with deterministic merge is what makes ACE stable across iterations. Full-prompt rewriting would collapse the context.
2. **Bullets are auditable.** A human operator can read the playbook, see why the agent behaves the way it does, and edit individual bullets.
3. **ACE is a memory substrate, not a workflow.** It is one component of a harness; the surrounding workflow (when to reflect, when to dedupe, when to apply) is handcrafted.
4. **ACE composes with MCE.** MCE adds meta-level skill evolution on top of ACE's base-level context engineering.

## Related Concepts

- [[Concepts/bi-level-context-skill-optimization]] — MCE, the meta-level evolution on top of ACE
- [[Concepts/file-system-as-agent-memory]] — files as the substrate; ACE bullets are one form of file-backed state
- [[Concepts/meta-harness-outer-loop]] — another level deeper: the harness code itself is the optimization target
- [[Concepts/harness-as-runtime-os-analog]] — the OS analogy; ACE is the "swap space" layer
- [[Concepts/scratchpad-context-window-management]] — adjacent in-context scratchpad pattern

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Paper: Zhang et al., "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models," ICLR 2026 (arXiv).
- Related Entity: [[Entities/ace-paper]]
