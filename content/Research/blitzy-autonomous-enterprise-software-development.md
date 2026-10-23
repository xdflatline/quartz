---
title: "Autonomous Software Development at Enterprise Scale: Blitzy's Architecture"
details: "Synthesis of the Blitzy architecture from SED episode 1975, organised around the seven mechanisms that make autonomous work viable on multi-million-line codebases: the codebase knowledge graph as context substrate, single-graph contextualization, graph-anchored swarm coordination and scope partitioning, pre-planned checkpointed review stages, multi-model cross-tiebreak routing for scope convergence, refinement resumed from substrate rather than transcript, and harness-enforced security assurance. Includes the operating model, the pricing alignment, and the stated frontier of recursive self-improvement against product metrics."
tags:
  - research
  - agent
  - coding-agent
  - orchestration
  - multi-agent
created: 2026-10-23
updated: 2026-10-23
type: research
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Autonomous Software Development at Enterprise Scale: Blitzy's Architecture

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Guest:** [[Entities/sid-pardeshi]], CTO and co-founder of [[Entities/blitzy]]
**Host:** [[Entities/kevin-ball-kball]]
**Episode:** [Software Engineering Daily #1975](https://softwareengineeringdaily.com/wp-content/uploads/2026/10/SED1975-Blitzy.txt)
**Captured:** 2026-10-23

---

## Overview

Enterprise codebases break today's coding agents for a reason that has nothing to do with model capability: the work is bigger than the context window, and the stakes of a mistake are measured in review time, retest time, and production incidents. [[Entities/sid-pardeshi]]'s argument is that the intelligence problem is solved and the *context* problem is not — and that the context problem is an engineering substrate problem, not a prompting problem.

Blitzy's architecture is best read as a set of answers to seven specific failures of the default agent tooling. This page organises the episode around those seven, then covers the operating model and the stated frontier.

## The seven mechanisms

### 1. The codebase knowledge graph as context substrate

→ [[Concepts/codebase-knowledge-graph-context-substrate]]

The nominal context window is a capacity claim; the effective one is a quality claim. A million tokens maps to ~100,000 lines of code, but quadratic attention and provider-side sparse/sliding-window techniques put the practical ceiling near 30,000 tokens in a request (~30,000 lines). Past that, quality degrades — which is why providers push short-running jobs and why long single-agent sessions fall apart.

Blitzy's answer is a persistent graph of the entire codebase, built by **building and running the code** (not only parsing ASTs) so that "present but unused" code is distinguishable from live code, including code that was deprecated but never marked as such. It is populated over a 24–48 hour pre-run at onboarding — an explicit cost accepted in exchange for starting every subsequent job with the whole codebase structurally known.

The retrieval discipline is what makes it work: a graph-shaped substrate that agents query semantically and structurally, rather than grep over 30 million lines of noise.

### 2. Single-graph contextualization

→ [[Concepts/single-graph-contextualization]]

Commit history, file structure, folder structure, task state, and pattern learnings are **not** separate graphs. Their learnings are applied to the nodes of one graph whose shape mirrors the codebase, so every fact is contextualised by where it lives in the code. Recency is weighted, so a migrated-away pattern ("we have this, but don't do that") is respected even though the old usage is still visible in comments and history.

The deeper point: memory in most agent tooling is files strewn across a workspace. Finding the *right* memory for the *right* module at the *right* moment is the hard part, and structural representation is what makes that tractable. Memory also has to be *earned* — Blitzy's framing is learning from someone else's mistakes so you don't have to get hurt first.

### 3. Graph-anchored swarm coordination and scope partitioning

→ [[Concepts/graph-anchored-agent-swarm-coordination]]
→ [[Concepts/graph-anchored-scope-partitioning]]

The standard model — one coordinator, many workers — has a known weakness: a single coordinator bottlenecks and workers drift into conflicting readings of the goal. Blitzy runs **multiple coordinators at different levels** and no single top-level orchestrator, with the graph as the shared source of truth and coordination substrate.

The mechanism is scope anchoring. A scope document is broken down and distributed **against the graph's own structure** — if the graph is folder-shaped, agents get folders and their scope is limited to them. Work items become claimable graph nodes, with dependencies ordering execution. The result is that overlap is designed out rather than detected, and the ceiling on parallel agents is compute, not coordination.

The cost is stated plainly: everything must live on the graph. The benefit claimed is that the substrate survives pod death, unlike disk, and unlike git it does not clutter a workspace or endanger the commit history.

### 4. Pre-planned checkpointed review stages

→ [[Concepts/pre-planned-checkpointed-review-stages]]
→ [[Concepts/out-of-scope-finding-policy]]

In most tooling, verification is something the human must keep asking for — and every forgotten prompt is a silently skipped stage. Blitzy pre-plans the path to production as **synchronisation checkpoints** with expectations and acceptance criteria at each stage, and runs them by default. Whether a stage is even needed is decided dynamically by the agents.

Security review is one of these stages, with dedicated agents watching the work, and it catches two distinct classes: scratch-artifact leakage (an issue in temporary code that survives into production) and pattern non-conformance for new surface (a new API that ignores existing authentication or load-balancing conventions). Adversarial testing is part of the stage — break the product before someone else does.

Findings that fall outside the job's scope are **documented rather than fixed**, in a project guide that records both what was done and what was deliberately not done; if a finding is judged in scope, the agent adjusts the work.

### 5. Multi-model cross-tiebreak routing

→ [[Concepts/multi-model-cross-tiebreak-routing]]

The convergence problem: agents love to find one more thing to do, and the fix is not prompt or effort tuning — if the trajectory contains a thought that decides to look for another problem, no setting removes it, short of editing the conversation, which nobody does.

The fix is a **different model with a different context load** deciding the contested question. The implementer has the whole burden and a blown context; the tiebreaker sees only the agent action plan and therefore judges scope more effectively, answering "that's not in scope." A job is seen by at least eight specialised models before it reaches the user.

Model selection is driven by internal evals rather than vendor claims: results are distilled into tags, tags are ranked into ladders, and the runtime picks the fastest rung that delivers the required quality. The routing decision is itself delegated to an agent, which chooses the next model's LLM, system prompt, and tools.

### 6. Refinement resumed from substrate, not transcript

→ [[Concepts/refine-pr-resume-from-substrate]]

Feedback on a generated PR is applied by resuming the graph plus the SCM — the "Refine PR" workflow — rather than re-priming a chat transcript that has already passed the effective context wall and lost the bulk of the work it describes.

This comes with the pricing model that makes it structural: **billed on the lines of code in the resulting PR**. Feedback that shrinks the PR shrinks the bill; wasted intermediate work is free. Both vendor and customer are thereby aligned toward "the right code, not all the possible code," and the token anxiety of "let it rip" loses its appeal.

The paired review surface makes refinement affordable: a review experience foregrounding the key changes so a reviewer inspects ~50 files rather than 500, on the reasoning that 100 files of green unit tests in a known style need no individual review.

### 7. Harness-enforced security assurance

→ [[Concepts/harness-enforced-security-assurance]]

LLMs have increased the rate at which vulnerabilities are *found* and drastically increased the rate at which they are *introduced*. You do not prompt a human to write secure code; they learn it and retain it. You must prompt an LLM, and the prompt is not retained. Model training is dynamic and not a controllable lever, so assurance has to live in the harness: dedicated review agents, scheduled security checkpoints, pattern conformance, adversarial testing, dedicated workflows, and a dedicated team.

This is a **precondition** for the whole autonomous proposition, not a feature of it — customers have to get comfort on security, compliance, guardrails, and code quality before accepting the deeper transformation.

## Operating model

| Stage | What happens |
|---|---|
| Onboard | 24–48 h reverse-engineering pre-run; codebase knowledge graph built; generated documentation of branches and modules produced |
| Spec | Human-written and human-approved; the agent action plan (AAP) is the compact statement of scope |
| Plan | Scope document; decomposition anchored on the graph; checkpoint stages and acceptance criteria fixed |
| Execute | Parallel agents recruited against graph scopes; multi-level coordination; multi-model routing |
| Verify | Pre-planned checkpoints: code review, security review, adversarial testing, test generation — default-on, stage applicability agent-decided |
| Deliver | PR + project guide (work done, work deliberately not done) + guided review experience |
| Refine | "Refine PR" resumes from graph + SCM; billed on final lines of code |
| Operate | Connected to customer cloud; environments, secrets, and configuration captured and replicated; environments set up dynamically per run; access to logs and observability; agents optimise against goals, guardrails, and boundaries simultaneously, escalating when they cannot |

Two staged practices are recommended for customers before a large project: a **crawl-walk-run** sequence that starts with documentation (let the system confirm its understanding of the codebase, then add testing). This has a specific payoff — it makes acceptance criteria easier for a human to write, and easier for the system to validate against, which reduces the cost of the whole item. Long-lived legacy estates are named as the segment where this matters most: engineers with 35 years of context, including COBOL, validating that output matches how an expert would have done it.

## The alignment argument

The most transferable idea in the episode is not architectural but contractual: **price on the accepted artifact, not on the generation cost.**

Both the outcome-based pricing and the "focused review" experience point at the same goal — writing the right code rather than all the possible code. This is the commercial mechanism that makes a quality-first posture self-enforcing. It also inverts the usual token-economics anxiety that pushes teams toward "let it rip, burn all you can."

## The stated frontier: recursive self-improvement

The serious version of the thesis is not faster delivery but **autonomous maintenance against a metric**. The example: a large team shipping daily commits that must never regress a page-load-time target. Enforcement per committer is impractical, so the system sits behind the team, monitors and updates daily, and floats changes up for human review dynamically when needed. The goal is met.

Generalised, that becomes product-level autonomy: capture product objectives, metrics, and standards, and let an autonomous system run a well-defined product with only occasional human supervision — while human attention shifts to the dynamic products that need research, auditing, and compliance checks.

The other frontier — "code review as a process is going away, software engineering is dying" — is explicitly rejected as outrageous in the enterprise context, on the grounds of compliance-framework evolution speed and the actual comfort level of day-to-day model users. The models are placed between "glorified autocomplete" and AGI: sequence-to-sequence next-token predictors that are genuinely good at real-world use cases.

## Boundaries of this source

This page is derived from a single podcast interview. Points that are the vendor's own claims and were not independently verified in the episode:

- The 24–48 hour pre-run, the ~80% time-to-production saving, the eight-models-per-job figure, and the private sandbox quota.
- The claim that Blitzy's multi-coordinator swarm design has not been described elsewhere in the industry — a notable assertion, given the adjacent concept pages in this wiki.
- The characterisation of model context limits. The ~272,000-token long-context pricing threshold was explicitly flagged by the speaker as "not the official reason" for the observation, and the causal account (quadratic attention) is a mechanism sketch, not a measurement.
- "Mythos scare" is referenced as a security incident but not explained in the transcript; the term is not resolvable from this source.

Numbers the speaker declined to cite — notably the private sandbox quota — are left uncited here rather than guessed.

## Related Pages

### Source
- [[Raw/sedaily-episode-1975-blitzy-2026]]

### Entities
- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
- [[Entities/kevin-ball-kball]]
- [[Entities/claude-code]]
- [[Entities/codex-cli]]

### Concepts
- [[Concepts/codebase-knowledge-graph-context-substrate]]
- [[Concepts/single-graph-contextualization]]
- [[Concepts/agent-facing-graph-query-interface]]
- [[Concepts/graph-anchored-agent-swarm-coordination]]
- [[Concepts/graph-anchored-scope-partitioning]]
- [[Concepts/pre-planned-checkpointed-review-stages]]
- [[Concepts/out-of-scope-finding-policy]]
- [[Concepts/multi-model-cross-tiebreak-routing]]
- [[Concepts/refine-pr-resume-from-substrate]]
- [[Concepts/harness-enforced-security-assurance]]
- [[Concepts/context-wall-large-codebase-scale]]

### Adjacent in this wiki
- [[Concepts/cross-repo-semantic-code-graphs]] — the static-analysis variant of the same graph idea
- [[Concepts/coordinator-worker-task-dag-orchestration]] — the single-coordinator model Blitzy departs from
- [[Concepts/builder-reviewer-task-granularity]] — the review-granularity problem Blitzy's review experience addresses
- [[Concepts/agent-self-improvement]] — the wiki's prior treatment of the frontier Blitzy names
- [[Concepts/spec-driven-development-sdd-2026]] — the spec-driven lineage Blitzy's workflow belongs to
- [[Concepts/context-rot]] and [[Concepts/context-as-materialized-view]] — prior treatments of the context problems this architecture solves
- [[Research/sdlc-as-context-engineering-2026-08]] — the SDLC-as-context framing that overlaps with this page
- [[Research/spec-driven-development-agentic-software-engineering]] — the specification-as-contract framing
