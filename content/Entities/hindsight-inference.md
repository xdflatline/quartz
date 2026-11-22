---
title: "Hindsight Inference"
details: "Hindsight's hosted inference API for its three memory models: a System One-compatible decisions endpoint, a Cohere-Rerank-compatible reranker, and an OpenAI-Embeddings-compatible embedding endpoint. Input-token-only pricing from $0.005 per million tokens, drop-in client compatibility, a request playground, and $5 of starting credit on new Cloud accounts."
tags:
  - entity
  - inference
  - memory
  - tooling
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Hindsight Inference

**Category:** Hosted API / Product
**Vendor:** [[Entities/vectorize]]
**Status:** Launched 2026-11 as part of Hindsight Cloud

## Overview

Hindsight Inference serves the three models of the [[Concepts/purpose-built-memory-model-stack|Hindsight model stack]] to any application, not only to Hindsight memory banks. It is part of Hindsight Cloud: sign-in uses the same Cloud account, organization, teams and credit balance. New accounts start with **$5 of free credit**.

## Endpoints and pricing

| API | Endpoint | Models | Drop-in for | Price per 1M input tokens |
|---|---|---|---|---|
| Decisions | `POST /v1/systemone` | `hs-decide-1-flash` | System One (TypeSafe) | $0.02 |
| Reranker | `POST /v1/rerank` | `hs-rerank-1`, or `hs-decide-1-flash` to also drop irrelevant documents | Cohere Rerank | $0.015 / $0.02 |
| Embeddings | `POST /v1/embeddings` | `hs-embed-1` | OpenAI Embeddings | $0.005 |

None of the three generates text, so billing is **input tokens only**. Base URL is `https://inference.hindsight.vectorize.io`; for the OpenAI-compatible embeddings client, `https://inference.hindsight.vectorize.io/v1`.

## Drop-in compatibility

The design goal is that the client code does not change:

- Point a **Cohere** client at the Hindsight host and set the model to `hs-decide-1-flash` to get reranking plus relevance pruning.
- Point an **OpenAI** client at the `/v1` base and change the model name to `hs-embed-1`.
- Point a **System One** client at the decisions endpoint and change the model name to `hs-decide-1-flash`.

This is what makes the adoption path short: the model swap is a configuration change, not an integration project.

## Playground

Every model can be tried in the Playground before writing code: choose reranking, embeddings or a decision; each comes prefilled with an example; each run shows the answer, latency, token count and cost. The Playground then emits the equivalent request as curl, Python, the Cohere or OpenAI SDK, or a Hindsight config. Keys are created under **API Keys**.

## Use with self-hosted Hindsight

The hosted models can drive an open-source Hindsight 1.2 instance with one login and environment variables, no GPU:

```bash
hindsight-admin cloud login
export HINDSIGHT_API_DECISION_MODEL_PROVIDER=hindsight
export HINDSIGHT_API_RECALL_DECISION_MODEL_PROVIDER=hindsight   # optional
export HINDSIGHT_API_RECALL_DECISION_MODEL_PRUNE=true           # optional
export HINDSIGHT_API_RECALL_DECISION_MODEL_DEDUP=true           # optional
export HINDSIGHT_API_RERANKER_PROVIDER=hindsight
export HINDSIGHT_API_EMBEDDINGS_PROVIDER=hindsight
```

The vendor claims $5 of credit covers the decision model's share of about 4,000 reflects on its evals. That is a vendor estimate against its own eval mix, not a general workload figure.

## Related

- [[Entities/hs-decide-1-flash]] — the decision model served here
- [[Entities/hindsight-ai-model-family]] — reranker and embedder
- [[Concepts/decision-model-cost-leverage]] — the economics these prices feed
- [[Entities/vectorize]] — parent company

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Docs: https://docs.hindsight.vectorize.io/cloud/inference/overview/
- Console: https://inference.hindsight.vectorize.io/
