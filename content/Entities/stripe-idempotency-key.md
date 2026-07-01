---
title: Stripe Idempotency-Key
detail: Stripe's API pattern for making POST requests safe against retries by attaching a client-generated idempotency key that causes duplicate requests to return the original result.
details: Stripe's API pattern for making POST requests safe against retries. Clients attach an Idempotency-Key header (V4 UUID or high-entropy random string) to POST requests. The server stores the status code and body of the first request for each key; subsequent requests with the same key return the stored result. Keys are pruned after 24 hours. This pattern has been adopted for AI agent reliability, where the key is derived from the content of the intended action rather than a random client-generated ID.
tags:
  - entities
source: https://docs.stripe.com/api/idempotent_requests
created: 2026-07-01
updated: 2026-07-01
type: entity
sources:
  - Raw/devto-ai-agent-idempotency-2026.md
---

## Overview

Stripe's Idempotency-Key is an HTTP header mechanism that makes POST requests safe against network retries. It is the canonical implementation of idempotency in payments infrastructure and has been adopted as the foundation pattern for making write-capable [[Concepts/idempotency-for-ai-agents|AI agents]] reliable.

## How It Works

1. Client generates a unique key (V4 UUID or high-entropy random string)
2. Client attaches `Idempotency-Key` header to a POST request
3. Server executes the request and stores the status code + response body keyed by the idempotency key
4. If the same key is received again (retry), the server returns the **stored result** without re-executing
5. Keys are pruned after 24 hours

## Adaptation for AI Agents

In AI agent systems, there is no human "click" to generate a random key. Instead, the key is **derived from the content of the intended action**:

- Hash of tool name + parameters
- Same logical action produces the same key
- Works across retries and process restarts

This shifts the key generation from random (client-side) to deterministic (intent-based), which introduces its own design challenges around what constitutes "the same action."

## Relevance

- Foundation pattern for [[Concepts/idempotency-for-ai-agents|Idempotency for AI Agents]]
- Demonstrates that the solution to agent reliability predates LLMs
- Production-validated in payments for 10+ years

## References

- Stripe API Docs: https://docs.stripe.com/api/idempotent_requests
- Source Article: [[Raw/devto-ai-agent-idempotency-2026]]
