---
title: "Corne Keyboard"
details: "The Corne (also 'Eyelash Corne' in the Manuals+ vendor variant) is a 42-key wireless mechanical split keyboard running ZMK firmware on nrf52840, with PH2.0 1500mAh (504060) lithium battery, TypeC charging, OLED screen, optional EC11 knob, and optional joystick. Designed by foostan; the vendor variant documented here ships with the firmware pre-flashed to the a741725193 seller repos."
tags:
  - entity
  - hardware
created: 2026-08-20
updated: 2026-08-20
type: entity
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# Corne Keyboard

The **Corne** is a popular open-source 42-key wireless mechanical split keyboard. The "Eyelash Corne" variant documented in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual is sold via Manuals+ and ships with firmware from the `a741725193` GitHub repos.

## Specifications (Eyelash Corne variant)

| Spec | Value |
|------|-------|
| MCU | nrf52840 |
| Connectivity | Bluetooth + USB (TypeC) |
| Firmware | ZMK |
| Battery | 1500mAh (504060) lithium |
| Battery interface | PH2.0 socket |
| Keys | 42 (3×6 + 3 thumb cluster per side) |
| Screen | OLED (in Eyelash Corne OLED variant) |
| Optional hardware | EC11 rotary encoder (knob), joystick |

## Hardware definition files

- `corne.dtsi`
- `corne_left.dts`
- `corne_right.dts`

## Firmware repositories (vendor-specific)

- Eyelash Corne (base): https://github.com/a741725193/zmk-new-corne
- Eyelash Corne OLED: https://github.com/a741725193/zmk-corne-oled
- Corne Dongle: https://github.com/a741725193/zmk-corne-dongle

The MX version and the low-profile version share the same GitHub repo. Ask the seller which variant maps to your purchase.

## Hardware revisions

| Hardware | New version | Old version |
|----------|-------------|-------------|
| Power switch | MINI MKS12C01 | MKS12C02 |
| Reset switch | TS24CA | (older unmarked) |
| New-version thumb behaviour | Left knob press = SPACE; right joystick press = ENTER | (no knob/joystick on old version) |

## Related entities

- [[Entities/sofle-keyboard]] — the related 58-key Sofle layout from the same vendor
- [[Entities/zmk]] — the firmware project
- [[Entities/nrf52840]] — the MCU
- [[Entities/a741725193-github-repos]] — the seller-specific firmware repos
- [[Entities/ec11-rotary-encoder]] — the optional knob hardware

## Related concepts

- [[Concepts/split-keyboard-firmware-architecture]] — broader architecture
- [[Concepts/wireless-split-pairing-protocol]] — left/right pairing
- [[Concepts/zmk-tap-dance-behavior]] — the home-row multi-modifier pattern
- [[Concepts/bootloader-rubber-ducky-update]] — the firmware update flow
