---
title: "GDPR"

details: "The General Data Protection Regulation (GDPR) is an EU regulation in force since 25 May 2018 that governs the processing of personal data of individuals in the EU/EEA. It applies to any organization processing such data, regardless of where the organization is based. The regulation introduced strengthened consent, data-subject rights, breach notification, and substantial penalties (up to 4% of annual global turnover or EUR 20 million, whichever is higher)."
tags:
  - entities
created: 2026-07-24
updated: 2026-07-24
type: entitie
source: "https://gdpr-info.eu"
---
# GDPR

**Category:** Compliance framework / EU regulation

**Issuer:** European Union
**Legal reference:** [Regulation (EU) 2016/679](https://gdpr-info.eu)
**In force since:** 25 May 2018

---

## Overview

The General Data Protection Regulation (GDPR) is the EU's primary data-protection law. It governs the processing of personal data of individuals in the EU/EEA and applies extraterritorially — any organization processing such data is subject to GDPR, regardless of where the organization is based. For serverless GPU providers, GDPR is the most common non-US compliance ask and the most common reason customers request EU data residency.

## Scope

GDPR applies to the processing of personal data of individuals in the EU/EEA by:

- An organization established in the EU/EEA, regardless of where the processing takes place.
- An organization not established in the EU/EEA, when it offers goods or services to individuals in the EU/EEA, or monitors their behavior.

## Key Concepts

- **Personal data:** Any information relating to an identified or identifiable natural person. Names, email addresses, IP addresses, biometric data, location data — all qualify.
- **Data subject:** The individual whose personal data is processed.
- **Controller:** The entity that determines the purposes and means of processing.
- **Processor:** The entity that processes personal data on behalf of the controller. **Serverless GPU providers are typically processors** when customers send user data through their inference APIs.
- **Data Processing Agreement (DPA):** A written contract between a controller and a processor, required by GDPR Article 28.

## The Seven Principles (Article 5)

Personal data must be:

1. Processed lawfully, fairly, and transparently.
2. Collected for specified, explicit, and legitimate purposes.
3. Adequate, relevant, and limited to what is necessary (data minimization).
4. Accurate and, where necessary, kept up to date.
5. Kept in a form permitting identification for no longer than is necessary (storage limitation).
6. Processed in a manner that ensures appropriate security.
7. Processed under the accountability principle — the controller is responsible for, and able to demonstrate, compliance.

## Lawful Bases (Article 6)

Processing is lawful only if and to the extent that at least one of the following applies:

1. **Consent** — the data subject has freely given specific, informed, and unambiguous consent.
2. **Contract** — processing is necessary for the performance of a contract with the data subject.
3. **Legal obligation** — processing is necessary to comply with a legal obligation.
4. **Vital interests** — processing is necessary to protect someone's life.
5. **Public task** — processing is necessary for a task carried out in the public interest.
6. **Legitimate interests** — processing is necessary for the controller's or a third party's legitimate interests, unless overridden by the data subject's rights.

## Data Subject Rights

Data subjects have the right to:

- **Access** their personal data (Article 15).
- **Rectification** of inaccurate data (Article 16).
- **Erasure** ("right to be forgotten") (Article 17).
- **Restriction** of processing (Article 18).
- **Data portability** in a structured, machine-readable format (Article 20).
- **Object** to processing, including profiling (Article 21).
- **Not be subject to a decision based solely on automated processing** (Article 22).

## Penalties

GDPR penalties are tiered:

- **Lower tier:** up to EUR 10 million or 2% of annual global turnover, whichever is higher.
- **Higher tier:** up to EUR 20 million or 4% of annual global turnover, whichever is higher.

The higher tier applies to violations of the core principles (Articles 5, 6, 7, 9, 22, 44-49), data-subject rights (Articles 12-22), and cross-border data-transfer rules (Chapter V).

## Why It Matters for Serverless GPU Procurement

- **Extraterritorial reach.** A US-based startup using a US-based inference provider to process data of EU residents is still subject to GDPR. The provider must offer GDPR-compliant terms.
- **Data Processing Agreement (DPA).** A signed DPA is the contract that binds the provider as a processor. **No DPA, no GDPR eligibility.**
- **Data residency / cross-border transfers.** Transfers of EU personal data outside the EEA are restricted. After *Schrems II* (CJEU, July 2020), the EU-US Data Privacy Framework and Standard Contractual Clauses (SCCs) are the primary legal mechanisms for transfers to the US. Customers will ask whether the provider supports EU regions, EU storage, and EU-trained personnel.
- **Sub-processors.** The provider's sub-processors (e.g., a third-party observability vendor, a payment processor) must be disclosed in the DPA. Customers have the right to object to new sub-processors.
- **Breach notification.** A processor must notify the controller "without undue delay" after becoming aware of a personal data breach. The controller then has 72 hours to notify the supervisory authority.

Most of the providers in [[Research/serverless-gpu-inference-providers]] claim GDPR compliance. Verify by reading the DPA, the sub-processor list, the breach-notification clause, and the data-residency options.

## Cross-Border Data Transfers

- **Adequacy decision:** the European Commission has recognized certain countries as providing adequate protection (e.g., the EU-US Data Privacy Framework for US-certified companies).
- **Standard Contractual Clauses (SCCs):** Pre-approved contract terms for transfers from the EEA to third countries.
- **Binding Corporate Rules (BCRs):** Internal data-transfer policies approved by a supervisory authority, used by multinationals.

## Related Concepts

- [[Entities/soc-2]] — common complementary attestation
- [[Entities/hipaa]] — US healthcare-specific regulation; overlaps with but does not equal GDPR
- [[Entities/iso-27001]] — international ISMS standard, often used in conjunction with GDPR
- [[Concepts/serverless-gpu-data-privacy]] — GDPR's role in the serverless GPU compliance matrix

## References

- [Full text of the GDPR (gdpr-info.eu)](https://gdpr-info.eu)
- [EDPB (European Data Protection Board) guidelines](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020_en)
- [EU Commission — International data transfers](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection_en)
