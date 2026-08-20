---
title: "Sofle Keyboard"
details: "The Sofle is a 58-key wireless mechanical split keyboard running ZMK firmware on nrf52840, sold as the 'Eyelash Sofle' variant via Manuals+. Larger than the Corne (extra column per side), shares the same firmware conventions, uses a larger 2000mAh (505060) battery, and ships firmware from the a741725193 GitHub repos."
tags:
  - entity
  - hardware
created: 2026-08-20
updated: 2026-08-20
type: entity
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# Sofle Keyboard

The **Sofle** is an open-source wireless mechanical split keyboard larger than the [[Entities/corne-keyboard]] (58 keys vs. 42 — adds an extra column per side). The "Eyelash Sofle" variant documented in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual is sold via Manuals+ and shares firmware conventions with the Corne.

## Specifications (Eyelash Sofle variant)

| Spec | Value |
|------|-------|
| MCU | nrf52840 |
| Connectivity | Bluetooth + USB (TypeC) |
| Firmware | ZMK |
| Battery | 2000mAh (505060) lithium |
| Battery interface | PH2.0 socket |
| Keys | 58 |

## Hardware definition files

- `sofle.dtsi`
- `sofle_left.dts`
- `sofle_right.dts`

## Firmware repositories (vendor-specific)

- Eyelash Sofle: https://github.com/a741725193/zmk-sofle
- Sofle Dongle: https://github.com/a741725193/zmk-sofle-dongle

The MX version and the low-profile version share the same GitHub repo.

## Power switch

| Version | Model |
|---------|-------|
| Old Corne / Sofle | MKS12C02 |
| Reset switch (new version) | TS24CA |

## Related entities

- [[Entities/corne-keyboard]] — the smaller sibling
- [[Entities/zmk]] — the firmware project
- [[Entities/nrf52840]] — the MCU
- [[Entities/a741725193-github-repos]] — the seller-specific firmware repos
