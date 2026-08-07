---
title: "SOC 2"

details: "SOC 2 (System and Organization Controls 2) is an auditing framework developed by the American Institute of Certified Public Accountants (AICPA). It evaluates a service organization's controls related to security, availability, processing integrity, confidentiality, and privacy, based on the AICPA's Trust Services Criteria. SOC 2 Type I reports on control design at a point in time; SOC 2 Type II reports on control operating effectiveness over a period (typically 6-12 months)."
tags:
  - entities
  - reference
  - recht
created: 2026-07-24
updated: 2026-07-24
type: entity
source: "https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services"
---
# SOC 2

**Category:** Compliance framework / certification

**Issuer:** [American Institute of Certified Public Accountants (AICPA)](https://www.aicpa-cima.com/)
**Standard reference:** [AICPA SOC suite of services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)

---

## Overview

SOC 2 (System and Organization Controls 2) is an auditing framework that assesses a service organization's controls against the AICPA's Trust Services Criteria. It is the de facto compliance bar for SaaS, cloud infrastructure, and any service provider that processes customer data on someone else's behalf. A SOC 2 report is issued by an independent CPA firm after an audit of the organization's controls.

## Trust Services Criteria

The five criteria against which controls are evaluated:

1. **Security** — protection against unauthorized access (mandatory in every SOC 2 report).
2. **Availability** — system uptime and performance commitments.
3. **Processing Integrity** — system processes are complete, accurate, timely, and authorized.
4. **Confidentiality** — confidential information is protected as committed.
5. **Privacy** — personal information is collected, used, retained, disclosed, and disposed of in line with the entity's privacy notice.

A SOC 2 report can cover Security only, or any combination of the five. Most cloud and SaaS providers cover at least Security, Availability, and Confidentiality.

## Type I vs Type II

| | Type I | Type II |
|---|---|---|
| What is audited | Design of controls at a point in time | Operating effectiveness of controls over a period |
| Audit window | A single date (e.g., 2026-07-24) | A period (typically 6-12 months) |
| Evidence required | Control documentation | Control documentation + operating evidence (logs, tickets, change records) |
| Typical use | "We have controls" (weaker signal) | "Our controls work in practice" (stronger signal) |
| Procurement weight | Lower | Higher; usually required by enterprise customers |

**SOC 2 Type II is the meaningful one.** Type I is a snapshot; Type II is a 6-12 month operating record. When evaluating a serverless GPU provider for a regulated workload, "SOC 2 Type II" is the phrase that matters; bare "SOC 2" usually means Type I.

## Why It Matters for Serverless GPU Procurement

SOC 2 is the most common compliance ask in enterprise procurement. A provider that does not have SOC 2 Type II will not pass most enterprise vendor risk assessments, regardless of the technical merits of the platform. Most of the providers in [[Research/serverless-gpu-inference-providers]] claim SOC 2 Type II; verify the actual report (or at least the bridge letter) before relying on it.

## Caveats

- SOC 2 is **a point-in-time or period-of-time attestation**, not a certification. There is no "SOC 2 certified" stamp; the deliverable is an auditor's report.
- The report is **confidential**. Most providers will share it under NDA during procurement; the existence of a report is the only thing they can advertise publicly.
- A SOC 2 report covers the **service organization**, not the customer. It does not absolve the customer of their own security responsibilities.
- SOC 2 is **not a substitute for HIPAA, ISO 27001, or GDPR compliance**. A provider can have SOC 2 without HIPAA; SOC 2 is broader and less prescriptive.

## Related Concepts

- [[Entities/hipaa]] — US healthcare-specific privacy/security framework
- [[Entities/iso-27001]] — international ISMS standard
- [[Entities/gdpr]] — EU personal-data protection regulation
- [[Concepts/serverless-gpu-data-privacy]] — how these certifications apply to serverless GPU providers

## References

- [AICPA SOC suite of services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [AICPA Trust Services Criteria](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-sga-2)
