---
title: "Espressif Systems"
details: "Shanghai-based fabless semiconductor company best known for the ESP32 family of low-cost Wi-Fi/Bluetooth SoCs; steward of the ESP-Claw agent framework."
tags:
  - entity
  - hardware
  - iot
  - open-source
created: 2026-08-14
updated: 2026-08-14
type: entity
source: "https://github.com/espressif"
---

# Espressif Systems

**Category:** Company
**Website:** https://www.espressif.com/
**GitHub:** https://github.com/espressif

## Overview

Espressif Systems is a fabless semiconductor company headquartered in Shanghai, China. It is best known for the ESP32 family of low-cost, low-power Wi-Fi + Bluetooth SoCs that have become a de-facto standard for hobbyist, maker, and increasingly commercial IoT. Beyond silicon, Espressif maintains an active open-source stack (ESP-IDF, ESP RainMaker, Matter support, etc.) and increasingly positions its chips as platforms for on-device intelligence — [[Entities/esp-claw|ESP-Claw]] being the most visible AI-agent-on-ESP32 project under the Espressif umbrella.

## Key Details

### Flagship Chip Families

| Series | Highlights |
|--------|-----------|
| ESP32 (original) | Dual-core Xtensa LX6, Wi-Fi + BT/BLE |
| ESP32-S2/S3 | LX7 core, USB OTG, vector instructions (S3) |
| ESP32-C3/C5/C6 | RISC-V single core, Wi-Fi 6 (C5/C6), BT 5 (C6) |
| ESP32-P4 | High-performance dual-core RISC-V, no radio, intended as host for ESP-HOSTED |
| ESP32-H2 | 802.15.4 (Thread/Zigbee), no Wi-Fi |

ESP-Claw targets S3, P4, C5, and S31 explicitly — a spread chosen to span from low-cost edge nodes (C5) to higher-compute hosts (P4).

### Software Stack

- **ESP-IDF** — official IoT Development Framework (Espressif's answer to vendor SDKs; monolithic CMake-based build).
- **ESP RainMaker** — managed cloud + phone-app platform for ESP32 fleets.
- **Matter / Thread** — first-party support across recent chips.

## Related Entities

- [[Entities/esp-claw]] — Espressif's on-device LLM agent framework
- [[Entities/openclaw]] — conceptual ancestor referenced in ESP-Claw's acknowledgements

## References

- https://www.espressif.com/
- https://github.com/espressif
