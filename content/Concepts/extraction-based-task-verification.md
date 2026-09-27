---
title: "Extraction-Based Task Verification for Synthetic Data"
details: "Synthetic data generation pipeline pattern that grounds LLM-as-judge relevance assessments in textual evidence rather than model opinion: for each supporting document, prompt the model to extract verbatim document_quotes paired with the corresponding clue_quotes from the generated question, normalize both, and confirm the document_quotes actually appear in the source text. A complementary distractor check extracts any occurrence of the answer in the distractor, filtering out distractors that inadvertently contain it. Chroma Context-1 (Bashir et al., March 2026) reports >80% human-judge alignment across all four domains (web 84.40%, distractor filtering 84%, email 87.5%, finance and legal in the same band) — replacing full-document human reading with quote-pair verification."
tags:
  - concept
  - rag
  - training
  - benchmark
  - evaluation
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/chroma-context-1-2026-03.md
related:
  - "[[Concepts/asymmetric-verification]]"
  - "[[Concepts/copyfail-vulnerability]]"
---

# Extraction-Based Task Verification for Synthetic Data

**Source:** [[Raw/chroma-context-1-2026-03]]
**Category:** Synthetic Data Methodology
**Related:** [[Concepts/asymmetric-verification]], [[Concepts/copyfail-vulnerability]]

## Overview

When generating synthetic tasks at scale, the failure mode that destroys training quality is **label noise** — supporting documents that don't actually support the generated clues, or distractors that inadvertently contain the answer. Two naive verification strategies both fail:

- **Ask the LLM to score relevance.** Unreliable; the model will happily say "yes, this document is relevant" when the quote doesn't actually appear.
- **Human label every document.** Prohibitively expensive at the volumes needed (8,000+ tasks in [Context-1]([[Raw/chroma-context-1-2026-03]])).

The extraction-based approach is a third way: convert the relevance judgment into a deterministic text-presence check.

## Mechanism

For each supporting document paired with a generated task, prompt an LLM to extract two sets of quotes:

- **`document_quotes`** — verbatim spans from the source text that support the answer.
- **`clue_quotes`** — the corresponding spans from the generated clues.

Then:

1. Normalize both (lowercase, strip excess whitespace, etc.).
2. Confirm that each `document_quote` actually appears in the source document. If any quote fails to appear, the supporting document is rejected.
3. Confirm that at least one document contains the answer. If none does, the entire task is filtered.

The human verification work reduces to: for each remaining (document, quote) pair, does the quote support the clue? That is a fast skim, not a full document read.

For distractors, run the complementary check: given the document and the answer, extract any occurrence of the answer in any form. If it appears, the distractor is filtered (it is no longer a distractor).

## Results Reported

The Context-1 paper reports >80% human-judge alignment across all four domains:

- Web domain: **84.40%** over 256 manually verified tasks
- Distractor filtering: **84%** over 256 tasks
- Email domain: **87.5%** over 200 tasks
- Finance and legal: in the same band, with full alignment metrics in the appendix

This is high enough that the residual label noise is dominated by edge cases the human labeler would also miss, rather than by systematic disagreement. The paper does not claim >95% because the residual is genuinely hard.

## Why It Works

The trick is moving the LLM's job from a subjective judgment ("is this document relevant?") to a mechanical one ("extract the supporting quote from this text"). Quote extraction is a much narrower capability and is well within the capability of any LLM that is being used to *generate* the synthetic data in the first place. The subjective judgment is then performed by a human on the (now much shorter) extracted evidence.

The pattern also reduces a second failure mode: **silent hallucination**. If the LLM says "document supports the clue" without producing a quote that appears in the document, the verification step rejects it. Without quote grounding, hallucinated supports slip through.

## Limits

- **Quote extraction is not the same as semantic support.** A document can contain a verbatim quote that, on a close reading, does not actually support the clue (wrong context, different referent, sarcasm). Human spot-checks remain necessary; the 80%+ alignment number is the residual rate of these failures.
- **Distractor check is shallow.** "Does the answer appear anywhere in this document?" is a low bar. A distractor that does not literally contain the answer but strongly implies it will pass. The Context-1 paper accepts this: distractors are only meant to look superficially relevant.
- **Domain dependence.** Quote-extraction quality depends on the LLM's ability to read structured documents (legal filings, SEC reports, email). For poorly-formatted sources, extraction accuracy drops.

## Comparison to WebExplorer's "Explore and Evolve"

[WebExplorer](https://arxiv.org/pdf/2509.06501) generates synthetic tasks fully automatically without a verification step. The Context-1 paper explicitly cites this as a limitation of WebExplorer's pipeline:

> WebExplorer's pipeline offers a more scalable alternative: an explorer agent collects facts on a seed topic until it can construct a challenging question, then an evolution step obfuscates the query to increase difficulty. While fully automated, this pipeline lacks a verification mechanism to ensure the accuracy of generated document pairings.

Context-1's extraction-based verification is the targeted fix: scale stays high (still automated end-to-end), label quality stays high (verified by quote presence).

## Related Work

- [WebExplorer](https://arxiv.org/pdf/2509.06501) — fully automated but unverified generation.
- [BrowseComp-Plus](https://arxiv.org/pdf/2508.06600) — manually curated, static corpus; high label quality but limited scale.
- [BrowseComp](https://arxiv.org/abs/2504.12516) — dynamic web content; reproducibility across time is the failure mode.

The extraction-based pattern occupies the middle: large-scale, automated, with quote-grounded verification rather than full human review.
