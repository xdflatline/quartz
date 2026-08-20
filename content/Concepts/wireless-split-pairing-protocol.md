---
title: "Wireless Split-Keyboard Pairing Protocol"
details: "The Corne/Sofle pairing lifecycle documented in the manual: left half is main, pairing is set during the first firmware update and preserved across subsequent updates, normal inter-half range is 0.6–0.8 meters, and resetting requires flashing a separate 'settings_reset' firmware to wipe the paired-device store before reflashing normal firmware."
tags:
  - concept
  - hardware
  - firmware
created: 2026-08-20
updated: 2026-08-20
type: concept
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# Wireless Split-Keyboard Pairing Protocol

The Corne / Sofle "Eyelash" firmware (documented in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual) implements a specific pairing protocol between the two halves of a split keyboard. The protocol is intentionally simple but has subtleties that matter for anyone building or troubleshooting.

## Pairing lifecycle

1. **First firmware flash** — the user flashes both halves for the first time. This **completes the pairing** between them.
2. **Subsequent firmware flashes** — the pairing state is **preserved** across firmware updates. The user does not need to re-pair after updating.
3. **To reset pairing** — the user flashes a dedicated `settings_reset` firmware **separately** on the affected half, then flashes normal firmware on both sides. The halves then auto-connect again.

## Operational rules

- **Left half = main.** It performs more work and consumes more battery. The right half is the input peripheral.
- **Auto-connect on power-up** — when both halves are switched on, they connect without user action.
- **Normal range:** 0.6–0.8 meters. This is the typical "hands on home row" distance; the manual does not document longer-range performance, suggesting the radio is tuned for very short range.

## Why a separate `settings_reset` firmware?

The pairing state is **stored in a non-volatile region that ordinary firmware updates do not touch**. The reasoning:

- Routine firmware updates (bug fixes, keymap changes, layer tweaks) must never silently break the user's working keyboard.
- When the user *does* want to wipe settings (debugging, selling the keyboard, switching halves between two keyboards), they need an explicit, one-shot escape hatch.
- A separate firmware variant — not a keycode — is the cleanest way to gate the destructive operation behind a deliberate action.

## Relationship to host Bluetooth

Pairing between halves is **independent** of pairing between the keyboard (main half) and a host computer. The keyboard can store **4–5 host Bluetooth profiles** separately from the single inter-half pairing. Resetting one does not reset the other.

## Related concepts

- [[Concepts/split-keyboard-firmware-architecture]] — broader architecture
- [[Concepts/bootloader-rubber-ducky-update]] — how firmware updates are delivered
- [[Entities/corne-keyboard]] — the canonical example
- [[Entities/nrf52840]] — the MCU providing the radio
