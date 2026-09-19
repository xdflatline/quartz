---
title: "Pact"
details: "Consumer-driven contract testing framework that lets consumers publish expected request/response payloads as machine-readable contracts, verified against provider builds in CI by a central broker to catch schema drift at build time without spinning up full integration environments."
tags:
  - entity
  - tool
  - ci
created: 2026-09-19
updated: 2026-09-19
type: entity
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Pact

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Framework
**Repository:** https://github.com/pact-foundation
**Website:** https://pact.io

---

## Overview

Pact is the canonical consumer-driven contract testing framework. Consumers record the interactions they expect from their providers as Pact files; a central broker (Pact Broker) versions and verifies those expectations against each provider build in CI, isolating verification from runtime integration environments.

## Key Details

- **Languages:** First-class support for JVM, Ruby, JS/TS, .NET, Go, Python, Swift, and PHP.
- **Broker:** Pact Broker stores contracts keyed by consumer + provider + version; webhooks drive the verification flow.
- **Provider verification:** `pact-provider-verifier` (or language equivalents) replays the consumer's contract against the provider build in a sandbox.
- **Status:** Mature; broadly adopted as the de facto open-source contract testing standard.

## Related Concepts

- [[Concepts/consumer-driven-api-contract-testing]] — Pact is the reference implementation of the consumer-driven contract pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8