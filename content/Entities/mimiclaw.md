---
title: "MimiClaw"
details: "Memovai's ESP32-targeted agent implementation cited by ESP-Claw as the source of its agent loop, IM communication, and related capabilities; sibling project in the ESP32-agent lineage."
tags:
  - entity
  - agent
  - iot
  - open-source
created: 2026-08-14
updated: 2026-08-14
type: entity
source: "https://github.com/memovai/mimiclaw"
---

# MimiClaw

**Source:** [[Raw/github-esp-claw-overview-2026-08-14]] (acknowledgements only)
**Category:** Project (Open-source agent runtime)
**Organization:** Memovai
**Repository:** https://github.com/memovai/mimiclaw

## Overview

MimiClaw is an open-source agent runtime targeting ESP32 hardware, developed by Memovai. The [[Entities/esp-claw|ESP-Claw]] README credits MimiClaw as the source of its **agent loop**, **IM communication**, and related capabilities — making MimiClaw a sibling implementation in the broader ESP32-agent lineage, distinguished from ESP-Claw mainly by its steward (Memovai vs. Espressif) and its derivative role relative to the conceptual [[Entities/openclaw|OpenClaw]] parent.

> Note: this page captures what is known from ESP-Claw's acknowledgements. MimiClaw's repository and full design have not yet been directly ingested here; treat the contents below as derived-from-acknowledgement until a dedicated ingestion is performed.

## Key Details

- **Role in ESP-Claw lineage** — sibling / reference; ESP-Claw adopts and adapts MimiClaw's agent loop and IM plumbing.
- **Steward** — Memovai (a separate organization from Espressif).
- **Implication** — the on-device LLM-agent + IM-chat loop now has at least two ESP32 instantiations, increasing the credibility that the pattern works on resource-constrained chips.

## Related Entities

- [[Entities/esp-claw]] — derivative C implementation by Espressif
- [[Entities/openclaw]] — conceptual ancestor of the whole lineage
- [[Entities/espressif]] — chip vendor and ESP-Claw steward (not MimiClaw's steward)

## Related Concepts

- [[Concepts/on-device-llm-agent-runtime]] — the architectural family MimiClaw belongs to
- [[Concepts/im-as-agent-frontend]] — the user-interaction pattern MimiClaw shares with ESP-Claw

## References

- ESP-Claw acknowledgements: [[Raw/github-esp-claw-overview-2026-08-14]]
- Repository: https://github.com/memovai/mimiclaw
