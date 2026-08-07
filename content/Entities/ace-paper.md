---
title: "ACE paper (Agentic Context Engineering)"

details: "Foundational paper for the [[Concepts/context-as-evolving-playbook]] concept. Published at ICLR 2026. The key design choice — the curator outputs structured bullets merged with deterministic logic, NOT a full prompt blob — is what prevents context collapse and brevity bias during iterative rewrites."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2409.10240
---

# ACE paper (Agentic Context Engineering)

**Source:** Zhang et al., "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models," ICLR 2026.

## Overview

The paper that introduced the [[Concepts/context-as-evolving-playbook]] pattern. Maintains a structured logbook of `(identifier, description)` bullets, refined and deduplicated over time. The three roles:

- **Generator** — produces task trajectories
- **Reflector** — distills insights from successes and failures
- **Curator** — updates the playbook with incremental entries

## The Key Design Choice

> The curator does NOT rewrite a full prompt blob. It outputs a collection of structured, itemized bullets in the form of `(identifier, description)`, merged into a structured logbook with **deterministic logic**.

This is the single most important design choice in the paper. Without it, iterative rewrites cause context collapse and brevity bias.

## Related

- [[Concepts/context-as-evolving-playbook]] — the concept extracted from this paper
- [[Entities/mce-paper]] — the meta-level successor
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
