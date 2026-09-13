---
title: "Spec-Driven Development for Agentic Software Engineering (research index)"
details: "Research synthesis of arXiv:2609.00252 (Diaz et al., 2026) and its surrounding literature. Maps the eight methodological-harness mechanisms to the paper's three contributions (SDD model, harness characterization, interaction-pattern typology), identifies the empirical claims the paper makes (productivity paradox; consistency, absorption, transferability, compounding as predicted benefits), and outlines the research-agenda questions the paper opens (RA1 team dynamics, RA2 human–agent interaction patterns, RA3 human competences, RA4 organizational adoption, RA5 measurement frameworks)."
tags: [research, software-engineering, agentic, harness, index]
created: 2026-09-13
updated: 2026-09-13
type: index
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
  - "Raw/sdd-agentic-software-engineering-arxiv-2026.md"
---

# Spec-Driven Development for Agentic Software Engineering — research index

A synthesis of [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]] that maps the paper's claims to the wiki's existing concepts and identifies the open research questions.

## The paper's three contributions, in wiki terms

1. **Socio-technical SDD model** — see [[Concepts/spec-driven-development-sdd-2026]] and [[Concepts/specifications-as-contract-substrate-agentic-se]]. The substrate argument is that specifications replace chat history as the authoritative referent; this restores accountability, verifiability, and transferability that vibe coding dissolves.
2. **Harness characterization** — see [[Concepts/agentic-harness-team-governance-sdd-2026]]. Eight mechanisms grouped into three functions:
   - **Knowledge management**: [[Concepts/harness-mechanism-context-engineering-sdd-2026|H1 context engineering]], [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026|H2 persistent shared knowledge]].
   - **Production support**: [[Concepts/harness-mechanism-executable-specifications-sdd-2026|H3 executable specifications]], [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026|H4 evidence-backed acceptance]], [[Concepts/harness-mechanism-n-version-generation-sdd-2026|H5 N-version generation]], [[Concepts/harness-mechanism-working-tree-isolation-sdd-2026|H6 working-tree isolation]].
   - **Governance**: [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026|H7 autonomy calibration]], [[Concepts/harness-mechanism-normative-specifications-sdd-2026|H8 normative specifications]], [[Concepts/harness-mechanism-review-and-consultation-sdd-2026|review/consultation pathway]].
3. **Interaction-pattern typology** — see [[Concepts/human-agent-interaction-patterns-sdd-2026]]. Five patterns (authoring, interpretation, validation, enrichment, reuse) on the shared specification substrate.

## The empirical claims

### The productivity paradox (motivation)

The paper cites industrial evidence:

- **Faros AI (2025)**: 10,000+ developers across 1,255 teams. GenAI adoption: +21% task completion, +98% merged PRs, +91% PR review time, +9% defects per developer.
- **DORA 2024**: higher AI adoption associated with reduced delivery performance and greater team instability.
- **DORA 2025**: throughput association reversed; instability persisted. Summarized as "AI does not fix a team but amplifies what is already there."
- **METR (2025) RCT**: experienced developers 19% slower in their own repos while believing they were ~20% faster.
- **Stack Overflow 2025**: "almost correct, but not quite" outputs the most frequent frustration.
- **GitClear (2025)**: across 211M changed lines (2020–2024), refactoring share collapsed from 25% to below 10%; duplicated code blocks up 8x.

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 1]] visualizes the paradox.

### The predicted benefits (testable, not yet validated)

The paper claims SDD-governed ASE predicts four benefits, all framed as testable:

1. **Consistency** — shared context and normative specifications reduce stylistic/architectural divergence that individual GenAI use produces.
2. **Absorption** — evidence-backed acceptance addresses the review bottleneck.
3. **Transferability** — onboarding reads specifications and the persistent-knowledge store, not reconstructed intent from code. The property that makes work belong to a team rather than an individual.
4. **Compounding** — the persistent context asset grows with each feature; the marginal cost of agent supervision should decrease over time.

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 9]] visualizes the four benefits.

## Related wiki concepts outside this ingestion

- [[Concepts/agentic-harness-architecture]] and the broader **Weng-lineage** harness concepts ([[Concepts/agentic-harness-engineering-ahe|AHE]], [[Concepts/harness-as-runtime-os-analog|OS analogy]], [[Concepts/evolutionary-search-for-harnesses|evolutionary search]], [[Concepts/joint-harness-weight-optimization|Joint Harness + Weights (SIA)]], [[Concepts/meta-harness-outer-loop|Meta-Harness]], [[Concepts/self-harness-propose-evaluate-accept|Self-Harness]], [[Concepts/harness-updating-vs-harness-benefit-disentanglement|disentanglement]]) cover a distinct sense of "harness" — the code that wraps an LLM API for production deployment. The Diaz et al. sense is the team-governance layer. Both senses are needed to operate ASE in practice; they sit at different layers of the stack.
- [[Concepts/agentic-crossover-skill-evolution]] is an example of the per-agent-skill-evolution pattern that sits beneath the SDD harness's H1 (context engineering) and H8 (normative specifications for skills).

## The research agenda ([[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 10]])

The paper's research agenda spans three levels:

- **Human competences (RA3)**: what skills do humans need to author specifications, calibrate autonomy, and audit evidence? How does this evolve as the harness absorbs more of the production loop?
- **Team dynamics (RA1)**: how do teams adopt the harness in stages without paying discipline cost without receiving benefit? What are the early indicators of partial adoption degrading outcomes?
- **Organizational adoption (RA4)**: how does SDD-governed ASE change the economics of software organizations? What are the medium-term effects on hiring, review capacity, defect rates, and code health?

These are connected through the study of **human–agent interaction patterns (RA2)** — the wiki's [[Concepts/human-agent-interaction-patterns-sdd-2026]] — while **measurement frameworks (RA5)** provide the empirical basis for evaluating effectiveness, risks, and long-term impact.

## What the paper does not (yet) claim

- It does not claim SDD is empirically validated. The evidence base is gray literature.
- It does not claim the eight mechanisms are sufficient or minimal. They are illustrative of what a methodological harness looks like; the literature has not yet produced comparative studies.
- It does not claim SDD replaces DevOps. The paper positions SDD as the discipline that lets ASE sit on top of, not instead of, the DevOps practices the same group has previously characterized (López-Fernández et al., 2021, IEEE TSE).

## Source

- [[Raw/sdd-agentic-software-engineering-arxiv-2026]] — verbatim arXiv HTML rendering with all 10 figures (9 image files + 1 caption-only paradigm-progression diagram).
- [[Papers/spec-driven-development-agentic-software-engineering-2026]] — cited summary.
- [[Entities/diaz-2026-sdd-harness-paper]] — bibliographic entity.
- [[Entities/diaz-upm-research-group]] — author context and prior work.