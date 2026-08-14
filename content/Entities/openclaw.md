---
title: "OpenClaw"
details: "Conceptual ancestor referenced in ESP-Claw's acknowledgements as the origin of the 'Chat Coding' on-device agent idea; treated as a parent project in the emerging open-source IoT-agent lineage."
tags:
  - entity
  - agent
  - iot
  - open-source
created: 2026-08-14
updated: 2026-08-14
type: entity
source: "https://github.com/openclaw/openclaw"
---

# OpenClaw

**Source:** [[Raw/github-esp-claw-overview-2026-08-14]] (acknowledgements only)
**Category:** Project (Open-source concept / parent lineage)
**Repository:** https://github.com/openclaw/openclaw

## Overview

OpenClaw is the project credited in [[Entities/esp-claw|ESP-Claw]]'s acknowledgements as the **conceptual inspiration** for "Chat Coding" — the idea that device behavior is defined through conversation with an LLM rather than through hand-written firmware. ESP-Claw's README describes itself as "Inspired by the OpenClaw concept and reimplemented in C," placing OpenClaw in the role of upstream/parent in the on-device IoT-agent lineage.

> Note: this page captures what is known from ESP-Claw's own references. OpenClaw's repository and full design are not yet directly ingested here; treat the contents below as derived-from-acknowledgement until a dedicated ingestion is performed.

## Key Details

- **Role in ESP-Claw lineage** — upstream concept; ESP-Claw adapts the idea for ESP32-series hardware.
- **Implication** — the "Chat Coding" framing (IM chat + dynamic behavior loading) originates from OpenClaw's design rather than being invented by Espressif.

## Related Entities

- [[Entities/esp-claw]] — C reimplementation for ESP32, explicitly credited
- [[Entities/mimiclaw]] — sibling ESP32 agent implementation, also cited by ESP-Claw

## Related Concepts

- [[Concepts/on-device-llm-agent-runtime]] — the architectural family OpenClaw belongs to
- [[Concepts/im-as-agent-frontend]] — the user-interaction pattern OpenClaw popularized in this lineage

## References

- ESP-Claw acknowledgements: [[Raw/github-esp-claw-overview-2026-08-14]]
- Repository: https://github.com/openclaw/openclaw
