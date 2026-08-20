---
title: "a741725193 GitHub Repos (Corne/Sofle Firmware Forks)"
details: "Vendor-specific ZMK configuration forks hosted under the GitHub user a741725193 for the Manuals+ 'Eyelash' Corne and Sofle keyboards. Five repositories: zmk-new-corne (Eyelash Corne base), zmk-corne-oled (Eyelash Corne with OLED screen), zmk-corne-dongle (Corne USB dongle variant), zmk-sofle (Eyelash Sofle base), and zmk-sofle-dongle (Sofle USB dongle variant). MX and low-profile variants share each repo."
tags:
  - entity
  - github
created: 2026-08-20
updated: 2026-08-20
type: entity
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# a741725193 GitHub Repos (Corne/Sofle Firmware Forks)

The Manuals+ Corne/Sofle "Eyelash" keyboards ship with firmware pre-configured from five GitHub repositories under the user **a741725193**. Repositories are described as "irregularly updated." Each keyboard purchase maps to a specific repository — the manual instructs users to ask the seller which one matches.

## Repositories

| Keyboard | Repository | URL |
|----------|-----------|-----|
| Eyelash Corne (base) | `zmk-new-corne` | https://github.com/a741725193/zmk-new-corne |
| Eyelash Corne (OLED screen variant) | `zmk-corne-oled` | https://github.com/a741725193/zmk-corne-oled |
| Corne USB dongle | `zmk-corne-dongle` | https://github.com/a741725193/zmk-corne-dongle |
| Eyelash Sofle (base) | `zmk-sofle` | https://github.com/a741725193/zmk-sofle |
| Sofle USB dongle | `zmk-sofle-dongle` | https://github.com/a741725193/zmk-sofle-dongle |

## Variants

- **MX version and low-profile version** of each keyboard share the same repository (one firmware repo covers both physical switch variants).
- The **OLED variant** is a separate repo because the OLED screen requires a different device-tree overlay.
- The **dongle variants** are separate repos because the dongle is a USB-host device that pairs with the keyboard halves and presents itself to the computer over USB — a different role from the keyboard halves themselves.

## Relationship to upstream ZMK

These repos are **vendor configuration forks** on top of upstream ZMK. They contain:

- Hardware definition files (`corne.dtsi`, `sofle.dtsi`, and the per-side `*_left.dts` / `*_right.dts`)
- Vendor-specific keymaps
- Vendor-specific behaviors (e.g., the optional EC11 knob and joystick bindings)

The keycode reference in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual maps directly to the ZMK behavior system documented in [[Entities/zmk]].

## Related entities

- [[Entities/corne-keyboard]] — uses `zmk-new-corne`, `zmk-corne-oled`, `zmk-corne-dongle`
- [[Entities/sofle-keyboard]] — uses `zmk-sofle`, `zmk-sofle-dongle`
- [[Entities/zmk]] — the upstream firmware project
- [[Entities/nrf52840]] — the MCU the firmware runs on
