---
title: "Corne / Sofle Eyelash ZMK Manual — Research Index"
details: "Cross-linked synthesis of the Manuals+ Corne Mechanical Split Keyboard Owner's Manual. Walks the system end-to-end — hardware (nrf52840, batteries, LEDs, EC11 knob, joystick), firmware (ZMK behaviors, keycodes, power management), architecture (asymmetric main/peripheral halves, pairing lifecycle, multi-profile host Bluetooth, USB-as-arbiter channel selection, USB-mass-storage bootloader), and the vendor-specific firmware fork landscape (a741725193 repos)."
tags:
  - research
  - hardware
  - firmware
created: 2026-08-20
updated: 2026-08-20
type: research
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# Corne / Sofle Eyelash ZMK Manual — Research Index

This page synthesizes the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual into a navigable map of the system: **what it is**, **what's inside it**, **how it works**, and **where the source material lives**.

## Source

| Field | Value |
|-------|-------|
| Title | Corne Mechanical Split Keyboard Owner's Manual |
| Source URL | https://manuals.plus/corne/mechanical-split-keyboard-manual |
| Mirrors consulted | https://manuals.plus/sv/corne/mechanical-split-keyboard-manual, https://manuals.plus/de/corne/mechanical-split-keyboard-manual |
| Type | Vendor hardware manual |
| Date retrieved | 2026-08-20 |

## System at a glance

| Subsystem | What it is | Where to read |
|-----------|-----------|---------------|
| Keyboards | Corne (42-key) and Sofle (58-key) wireless mechanical split layouts | [[Entities/corne-keyboard]], [[Entities/sofle-keyboard]] |
| MCU | Nordic nrf52840 with built-in BLE and USB device | [[Entities/nrf52840]] |
| Firmware | ZMK, open-source, behavior-based configuration | [[Entities/zmk]] |
| Vendor firmware forks | Five repos under GitHub user `a741725193` | [[Entities/a741725193-github-repos]] |
| Optional hardware | EC11 rotary encoder (knob), joystick | [[Entities/ec11-rotary-encoder]] |
| Architecture | Asymmetric halves, multi-profile host BT, USB-arbiter channel, drag-and-drop bootloader | [[Concepts/split-keyboard-firmware-architecture]] |
| Pairing | Persisted across updates, reset via `settings_reset` | [[Concepts/wireless-split-pairing-protocol]] |
| Firmware update | USB-mass-storage bootloader via double-press | [[Concepts/bootloader-rubber-ducky-update]] |
| Multi-action keys | Tap-dance (TD), hold-tap (`&lt`/`&gt`) | [[Concepts/zmk-tap-dance-behavior]] |

## Hardware walkthrough

### Power, charging, battery

- Each half has a toggle switch (down = ON).
- Charging via TypeC: 6–8 hours.
- Battery sizes: 1500mAh (504060) for Corne, 2000mAh (505060) for Sofle.
- Connector: **PH2.0 socket**.
- Batteries have built-in protective plates that auto-stop charging when full.
- **Only turn off the power switch if the keyboard will be unused for more than 6 months** (to protect the lithium cells).

### LED indicators

| LED | State | Meaning |
|-----|-------|---------|
| Green | Solid | Charging |
| Green | Off | Charging complete |
| Green | Flashing | Power switch off (and USB connected), or battery disconnected |
| Blue | Breathing | BootLoader, USB connected |
| Blue | Fast flashing | BootLoader, USB not connected |
| Blue | Off | Normal ZMK operation |

See [[Concepts/bootloader-rubber-ducky-update]] for the full indicator-state table and the rationale for the 0.5-second double-press window.

### Screws and switches

| Component | Spec |
|-----------|------|
| PCB-to-case screws | M2 × 4 with embedded nuts M2 × 2 × 3.2 |
| Positioning / PCB self-tap | M2 × 4 |
| Screen cover | Tempered glass, M2 × 2 |
| Foot pads | 10 × 2 rubber |
| Power switch (new Corne) | MINI MKS12C01 |
| Power switch (old Corne / Sofle) | MKS12C02 |
| Reset switch (new version) | TS24CA |

## Firmware walkthrough

### Bootloader — entering, flashing, resetting

1. Plug USB.
2. Double-press reset within 0.5 s → blue LED breathes.
3. Keyboard enumerates as a USB disk.
4. Drag firmware file(s) — **no left/right order required**.
5. MCU writes firmware and reboots.

Software path: press the `&bootloader` keycode from ZMK.

Full detail: [[Concepts/bootloader-rubber-ducky-update]].

### Pairing — left/right halves

- Auto-connects on power-up.
- **Left = main** (more work, more battery).
- Pairing set during first firmware flash; preserved across subsequent updates.
- To reset: flash `settings_reset` firmware separately, then reflash normal firmware.
- Normal range: 0.6–0.8 m.

Full detail: [[Concepts/wireless-split-pairing-protocol]].

### Host Bluetooth

- Pair from the host's Bluetooth page; device name is "corner" or "sofle".
- Stores 4–5 profiles for different hosts.
- Active profile shown on OLED screen.
- `BT_CLEAR_ALL` resets; `BT_SEL_0..N` selects.

**Pitfall:** accidentally pressing a profile-switch keycode while typing silently redirects keystrokes to a different host.

### Channel selection (USB vs. Bluetooth)

- TypeC plugged in → USB by default.
- `OUT_BL` / `OUT_USB` keycodes override.

### Power management (RGB)

- RGB chips leak current even when "off" in software.
- `ext_power EP_OFF` / `ext_power EP_ON` physically cut positive power.
- `RGB_ON` / `RGB_OFF` are software on/off.
- **Battery-life warning:** accidentally pressing `EP_ON` drains the battery; the manual recommends deleting that keycode from the keymap.

### Keyboard state

- `&Soft_off` — soft shutdown.
- `&sys_deset` — restart.
- `&bootloader` — enter bootloader.

### Behaviors on a 42-key Corne

- **Tap-dance** ([[Concepts/zmk-tap-dance-behavior]]): short press vs. double-tap on one key, e.g., TD0 = `LEFT_SHIFT` / `CAPS`.
- **Hold-tap / layer-tap**: `&lt 3 SPACE` (short = SPACE, hold = layer 3) and `&gt 3 ENTER` (short = ENTER, hold = layer 3).
- New-version Corne uses EC11 + joystick for SPACE/ENTER instead.

## Vendor-specific firmware landscape

Five repos under GitHub user `a741725193`, see [[Entities/a741725193-github-repos]]:

| Keyboard variant | Repo |
|------------------|------|
| Eyelash Corne (base) | `zmk-new-corne` |
| Eyelash Corne (OLED) | `zmk-corne-oled` |
| Corne USB dongle | `zmk-corne-dongle` |
| Eyelash Sofle | `zmk-sofle` |
| Sofle USB dongle | `zmk-sofle-dongle` |

MX and low-profile versions share each repo. Repositories are irregularly updated.

## Quick-reference cheat sheet

| Task | Action |
|------|--------|
| Power on | Toggle switch down on both halves |
| Charge | TypeC + any phone charger; 6–8 h; green LED solid=charging, off=full |
| Flash firmware | USB + double-press reset within 0.5 s → drag firmware files |
| Pair left/right | Happens on first firmware flash; reset with `settings_reset` + reflash |
| Bluetooth host | Add "corner" or "sofle" from host's Bluetooth page |
| Reset Bluetooth | `BT_CLEAR_ALL` on layer 2 |
| Force Bluetooth output | `OUT_BL` |
| Force USB output | `OUT_USB` |
| Soft shutdown | `&Soft_off` |
| Enter bootloader | Double-press reset, or `&bootloader` |
| Disable RGB power | `ext_power EP_OFF` (or remove `EP_ON` from keymap) |

## Cross-link index

**Concepts:**
- [[Concepts/split-keyboard-firmware-architecture]]
- [[Concepts/zmk-tap-dance-behavior]]
- [[Concepts/wireless-split-pairing-protocol]]
- [[Concepts/bootloader-rubber-ducky-update]]

**Entities:**
- [[Entities/corne-keyboard]]
- [[Entities/sofle-keyboard]]
- [[Entities/zmk]]
- [[Entities/nrf52840]]
- [[Entities/a741725193-github-repos]]
- [[Entities/ec11-rotary-encoder]]

**Raw source:**
- [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]]
