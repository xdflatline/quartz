---
title: "HIPAA"

details: "The Health Insurance Portability and Accountability Act (HIPAA) is a US federal law that sets privacy and security rules for Protected Health Information (PHI). Any vendor that creates, receives, maintains, or transmits PHI on behalf of a covered entity is a Business Associate and must sign a Business Associate Agreement (BAA) and implement safeguards. For serverless GPU providers, the practical question is: does the provider offer a BAA, and on which tier?"
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html"
---
# HIPAA

**Category:** Compliance framework / US federal law

**Issuer:** [US Department of Health and Human Services (HHS)](https://www.hhs.gov/hipaa)
**Statutory reference:** 45 CFR Parts 160, 162, and 164 (the HIPAA Privacy, Security, and Breach Notification Rules)

---

## Overview

The Health Insurance Portability and Accountability Act (HIPAA) is a 1996 US federal law whose Privacy, Security, and Breach Notification Rules govern the handling of Protected Health Information (PHI). It applies to "covered entities" (healthcare providers, health plans, healthcare clearinghouses) and to their "business associates" (any vendor that touches PHI on the covered entity's behalf).

For serverless GPU providers, HIPAA matters whenever a workload processes PHI. Inference on patient records, transcription of clinical conversations, fine-tuning on clinical datasets — all of these can involve PHI. The provider must be willing to sign a Business Associate Agreement (BAA) and implement administrative, physical, and technical safeguards.

## Key Concepts

- **PHI (Protected Health Information):** Individually identifiable health information held or transmitted by a covered entity or business associate. Includes anything that links a person to their health status, care, or payment.
- **Covered Entity:** Healthcare provider, health plan, or healthcare clearinghouse that transmits health information electronically.
- **Business Associate:** A person or entity that performs functions or activities involving the use or disclosure of PHI on behalf of a covered entity.
- **Business Associate Agreement (BAA):** A written contract required by HIPAA between a covered entity and a business associate. The BAA binds the business associate to the same HIPAA Rules and makes them directly liable for certain provisions.

## HIPAA Rules

1. **Privacy Rule (45 CFR Part 164 Subpart E):** Limits use and disclosure of PHI; grants patients rights over their data.
2. **Security Rule (45 CFR Part 164 Subpart C):** Administrative, physical, and technical safeguards for electronic PHI (ePHI).
3. **Breach Notification Rule (45 CFR §§ 164.400-414):** Notification requirements following a breach of unsecured PHI.
4. **Enforcement Rule:** HHS Office for Civil Rights (OCR) investigates and enforces.
5. **Omnibus Rule (2013):** Extended HIPAA requirements directly to business associates.

## Why It Matters for Serverless GPU Procurement

A cloud or inference provider that handles PHI without a signed BAA is a HIPAA violation. A provider that has SOC 2 but no BAA is **not** HIPAA-eligible for PHI workloads, regardless of how secure their stack is.

**Practical checklist for serverless GPU providers:**

- Does the provider offer a BAA on their standard tier, or only on enterprise?
- Does the BAA cover the specific product (serverless inference, fine-tuning, model storage)?
- Does the provider's infrastructure support the technical safeguards (encryption at rest, encryption in transit, access controls, audit logging)?
- Does the provider commit to breach notification within the HIPAA-prescribed window (60 days)?

Most of the providers in [[Research/serverless-gpu-inference-providers]] offer HIPAA on the enterprise tier; a few (e.g., Modal, DeepInfra, Fal.ai) do not. **A "HIPAA available" line in a comparison table is not a substitute for reading the BAA and confirming that the specific product surface is covered.**

## Penalties

HIPAA violations carry civil monetary penalties ranging from $137 to $2,067,813 per violation, per year (2024 adjusted figures, indexed for inflation), plus potential criminal penalties including fines and imprisonment for willful violations.

## Caveats

- HIPAA is a **US law**. It does not directly apply outside the US, though other jurisdictions have their own health-data laws (e.g., the UK ICO's health-data guidance, EU member-state implementations of GDPR for health data).
- A BAA is **a contractual tool, not a certification**. There is no "HIPAA certified" status. The provider attests to its safeguards and accepts liability; the covered entity's auditor confirms in due diligence.
- HIPAA does not require specific technical controls (e.g., specific encryption algorithms). It requires "reasonable and appropriate" safeguards. SOC 2 / HITRUST reports are common proxies.

## Related Concepts

- [[Entities/soc-2]] — common complementary attestation
- [[Entities/iso-27001]] — international ISMS standard, often used in conjunction with HIPAA
- [[Entities/gdpr]] — EU personal-data regulation; overlaps with but does not equal HIPAA
- [[Concepts/serverless-gpu-data-privacy]] — HIPAA's role in the serverless GPU compliance matrix

## References

- [HHS HIPAA for Professionals](https://www.hhs.gov/hipaa/for-professionals/index.html)
- [HHS Covered Entities and Business Associates](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html)
- [45 CFR Parts 160, 162, 164](https://www.ecfr.gov/current/title-45)
- [HHS Sample Business Associate Agreement Provisions](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html)
