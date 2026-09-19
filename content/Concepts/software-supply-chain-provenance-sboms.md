---
title: "Software Supply-Chain Provenance and SBOMs"
details: "Architecture pattern that operates inside build runners, artifact registries, and admission controllers to generate Software Bills of Materials (SPDX / CycloneDX), cryptographically sign artifacts (Sigstore / Cosign), and enforce SLSA provenance — blocking unsigned or vulnerable images from being scheduled onto production nodes."
tags:
  - concept
  - tooling
  - cybersecurity
created: 2026-09-19
updated: 2026-09-19
type: concept
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Software Supply-Chain Provenance and SBOMs

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Software supply-chain security tooling is the pattern of producing, signing, and verifying cryptographic provenance for every artifact that runs in production — combined with a bill of materials that names every transitive dependency — so that build-time gates can reject unsigned, unvetted, or vulnerable images before they are scheduled onto a node.

## Core Content

### Mechanism

1. **SBOM generation:** at build time, the runner enumerates every direct and transitive dependency and emits a machine-readable SBOM (SPDX or CycloneDX).
2. **Attestation:** the build pipeline signs the artifact with a short-lived key (Sigstore / Cosign) and records the provenance attestation (SLSA levels) — who built it, with what inputs, on what runner.
3. **Admission control:** the cluster's admission controller rejects images that lack a valid signature, lack a valid SBOM, or contain dependencies with known critical vulnerabilities.
4. **Vulnerability database correlation:** the SBOM is cross-referenced against a vulnerability feed so transitive risk (a vulnerable version of `libfoo` three layers deep) is surfaced.

### What It Defends Against

- Typosquatted dependencies uploaded to public package registries.
- Dependency-confusion attacks (an internal package name shadowed by a malicious public one).
- Compromised transitive dependencies that pass code review but fail attestation.
- Unsigned or unverified images promoted from a compromised pipeline.

### Operational Characteristics

| Property | Value |
| --- | --- |
| Primary failure domain | Malicious packages, unverified builds |
| Architectural plane | Build & Artifact Pipeline |
| Host boundary | Registry / Build Runner |
| State persistence | Attestation ledgers / Relational vulnerability DB |
| Network overhead | Zero runtime overhead (build-time gate) |

## Key Insights

1. The runtime overhead is zero because the verification happens at admission time — once an image is admitted, it runs as any other image would.
2. The trust root is the signing key, not the package registry — even a compromised registry cannot mint a valid signature without the build runner's key.
3. SBOMs without attestation are half a system — knowing the dependency tree is necessary but not sufficient; the attestation is what proves the tree was actually produced by the claimed build.

## Related Concepts

- [[Concepts/consumer-driven-api-contract-testing]] — both are build-time verification patterns, but contracts verify behavior and supply-chain verifies identity/provenance.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8