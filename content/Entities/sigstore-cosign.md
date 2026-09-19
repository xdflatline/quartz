---
title: "Sigstore and Cosign"
details: "Cryptographic signing stack for software supply-chain integrity — Cosign signs container images and artifacts with short-lived keys tied to OIDC identity, and the Rekor transparency log records every signature for public auditability, together underpinning SLSA provenance and admission-controller verification."
tags:
  - entity
  - tool
  - cybersecurity
created: 2026-09-19
updated: 2026-09-19
type: entity
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Sigstore and Cosign

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Platform
**Repository:** https://github.com/sigstore
**Website:** https://www.sigstore.dev

---

## Overview

Sigstore is the Linux Foundation-hosted project that bundles three primitives for software supply-chain signing: Cosign (image and artifact signing with short-lived keys tied to OIDC identity), Fulcio (the free root-CA that issues those short-lived certificates), and Rekor (the append-only transparency log that records every signature). Together they underpin SLSA provenance verification at admission time.

## Key Details

- **Cosign:** Signs OCI images, SBOMs, and arbitrary blobs; verification is a single `cosign verify` call.
- **Keyless signing:** Uses OIDC identity (GitHub Actions, Google Cloud Build, etc.) to derive short-lived keys — no long-lived secret to leak.
- **Rekor:** Append-only transparency log; auditors can independently verify that a signature was logged at a specific time.
- **Admission control:** `policy-controller` (formerly Connaisseur) and Kyverno policies can reject unsigned images at the Kubernetes API server.

## Related Concepts

- [[Concepts/software-supply-chain-provenance-sboms]] — Sigstore and Cosign are the canonical implementation substrate for the supply-chain provenance pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8