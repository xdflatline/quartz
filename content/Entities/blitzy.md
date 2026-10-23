---
title: "Blitzy"
details: "Enterprise-only autonomous software development platform co-founded by CTO Sid Pardeshi, targeting large codebases where well-defined, spec'd work makes up roughly 80% of enterprise engineering effort. Differentiators: a codebase knowledge graph built by a 24-48 hour reverse-engineering pre-run, multi-coordinator agent swarms without a single top-level orchestrator, pre-planned checkpointed review stages, cross-model tiebreaking on scope, and pricing that bills only the final lines of code in the resulting pull request."
tags:
  - entity
  - coding-agent
  - agent
  - orchestration
created: 2026-10-23
updated: 2026-10-23
type: entity
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Blitzy

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Company / Autonomous Software Development Platform
**Founded:** By [[Entities/sid-pardeshi]] (CTO, co-founder) and co-founders
**Positioning:** Enterprise-only
**Source episode:** [Software Engineering Daily #1975](https://softwareengineeringdaily.com/wp-content/uploads/2026/10/SED1975-Blitzy.txt)

---

## Overview

Blitzy is an autonomous software development platform for the enterprise. It differs from coding-agent tools like [[Entities/claude-code]], [[Entities/codex-cli]], Devin, and Factory by specialising in *very large enterprise jobs* — codebases where a fraction of the work is undefined exploration and most of it (the estimate given is ~80%) is already well-specified work waiting to be executed.

The workflow: a human-approved spec goes in, specialised agents work in parallel, and a reviewable pull request comes out.

## Architecture claims

| Area | Claim |
|---|---|
| Onboarding | 24–48 hour pre-run that reverse-engineers the entire codebase into a graph database |
| Retrieval | Agents query the graph via schema-aware tools and semantic search over summary embeddings; the graph is populated by building and running the code, not only by parsing ASTs |
| Coordination | Multi-coordinator swarms — no single top-level orchestrator; the graph is the shared source of truth and the coordination substrate |
| Scope | Work decomposed via a scope document and distributed anchored on graph structure (e.g. agents assigned to folders) |
| Verification | Pre-planned synchronisation checkpoints — code review, security review, testing — run by default, with stage applicability decided dynamically by the agents |
| Models | Multi-model with internal evals, tag-ranked ladders, and runtime routing; a job is seen by at least eight different models before reaching the user |
| Convergence control | A second model with a fresh, lighter context tiebreaks scope against the agent action plan |
| Resumption | "Refine PR" workflow resumes from the graph plus the SCM rather than from the chat transcript |
| Pricing | Billed on the lines of code in the **resulting** PR — corrections that shrink the PR shrink the bill |
| Environments | Customer cloud (AWS/GCP) connected; environments, secrets, and configuration captured and replicated across projects, set up dynamically by the agents each run |
| Observability | Agents given access to logs and observability, optimising against goals, guardrails, and boundaries simultaneously, escalating to a human when they cannot |
| Data policy | No training on customer code; strict data retention policies; customer code owned by the customer and not stored |

## Commercial framing

- **Enterprise-only.** Large enterprise customers are described as designing their entire SDLC around the platform.
- **Quality over cost.** Stated optimisation target is "the fastest model that gives you the best quality" — not token spend.
- **Reported outcome:** ~80% of the time-to-production saved on customer projects; the residual 20% attributed to access limits, unsupported integrations, and customer-side process policies.
- **Private sandbox tier:** companies with more than 250 employees signing up with a work email get automatic access with a quota for reverse-engineering and writing code — a low-friction evaluation path. Quota figures were not cited in the episode.
- **Long-lived legacy codebases** are named as the segment the platform serves best: engineers with 35 years of context, including COBOL estates, validating that the system's output matches how an expert would have done it.

## Stated outlook

Two visions of the frontier were discussed and the "software engineering is dying" position was explicitly rejected as outrageous for the enterprise, on grounds of compliance-framework evolution speed and the actual comfort level of day-to-day model users. The models are described as sitting between "glorified autocomplete" and AGI.

The serious thesis: split the work. Undefined discovery and research work stays with human-directed tools; well-defined work is handed to autonomous systems. The next frontier named is **recursive self-improvement** — an autonomous system that holds a metric (e.g. page load under one second) against a large team's daily commits, monitoring and updating daily, floating changes up for human review dynamically. That is then generalised from individual metrics to whole products, where capturing objectives, metrics, and standards allows a product to run with only occasional human supervision.

Self-filing tickets and self-scheduling follow-up work was described as in progress.

## Related Pages

- [[Raw/sedaily-episode-1975-blitzy-2026]] — source transcript
- [[Entities/sid-pardeshi]] — CTO and co-founder
- [[Concepts/codebase-knowledge-graph-context-substrate]]
- [[Concepts/graph-anchored-agent-swarm-coordination]]
- [[Concepts/graph-anchored-scope-partitioning]]
- [[Concepts/single-graph-contextualization]]
- [[Concepts/agent-facing-graph-query-interface]]
- [[Concepts/pre-planned-checkpointed-review-stages]]
- [[Concepts/harness-enforced-security-assurance]]
- [[Concepts/multi-model-cross-tiebreak-routing]]
- [[Concepts/refine-pr-resume-from-substrate]]
- [[Concepts/out-of-scope-finding-policy]]
- [[Concepts/context-wall-large-codebase-scale]]
- [[Research/blitzy-autonomous-enterprise-software-development]]
