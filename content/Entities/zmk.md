---
title: "ZMK Firmware"
details: "ZMK is an open-source keyboard firmware generation tool, used by the Corne/Sofle 'Eyelash' keyboards on the nrf52840. Provides a behavior system (tap-dance, hold-tap/layer-tap, soft-off, RGB, ext-power), Bluetooth profile management (BT_SEL_0..4, BT_CLEAR_ALL), USB/Bluetooth output channel selection (OUT_USB, OUT_BL), and a USB-mass-storage bootloader for drag-and-drop firmware updates."
tags:
  - entity
  - firmware
  - hardware
created: 2026-08-20
updated: 2026-08-20
type: entity
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# ZMK Firmware

**ZMK** is an open-source keyboard firmware generation tool. The Corne / Sofle "Eyelash" keyboards documented in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual run ZMK on the [[Entities/nrf52840]] MCU.

## Key behaviors exposed by ZMK

### Bluetooth management

| Keycode | Function |
|---------|----------|
| `BT_CLEAR_ALL` | Clear all Bluetooth host profiles |
| `BT_SEL_0`, `BT_SEL_1`, `BT_SEL_2`, ... | Select host profile 0..N (up to 4–5 devices) |

### Power output (RGB physical power)

| Keycode | Function |
|---------|----------|
| `ext_power EP_OFF` | Cut positive power to RGB chain |
| `ext_power EP_ON` | Restore positive power to RGB chain (drains battery) |

### RGB control (software on/off)

| Keycode | Function |
|---------|----------|
| `RGB_ON` | Turn RGB on |
| `RGB_OFF` | Turn RGB off |

### Output channel routing

| Keycode | Function |
|---------|----------|
| `OUT_BL` | Force keystrokes to Bluetooth channel |
| `OUT_USB` | Force keystrokes to USB channel |

Default: when TypeC is plugged in, keystrokes automatically route to USB.

### Keyboard state control

| Keycode | Function |
|---------|----------|
| `&Soft_off` | Enter soft-shutdown state |
| `&sys_deset` | Restart keyboard |
| `&bootloader` | Enter bootloader (or double-press physical reset switch) |

### Behaviors

- **Tap-dance** (`zmk,behavior-tap-dance`): distinguish by tap count — short press vs. double-click maps to different actions on one key. See [[Concepts/zmk-tap-dance-behavior]].
- **Hold-tap / layer-tap** (`&lt`, `&gt`): distinguish by tap vs. hold — e.g. `&lt 3 SPACE` = short press SPACE, long press enter layer 3.

## Bootloader integration

ZMK uses a USB-mass-storage bootloader on supported boards (e.g. the nrf52840 used in Corne/Sofle). Users enter the bootloader via double-press of the reset switch (within 0.5 s) with USB plugged in, or via the `&bootloader` keycode. The MCU enumerates as a USB disk; firmware files are drag-and-dropped. See [[Concepts/bootloader-rubber-ducky-update]].

## Configuration model

ZMK is configured via **device-tree source** files (`*.dts`, `*.dtsi`). The Corne / Sofle hardware definition files are:

- Corne: `corne.dtsi`, `corne_left.dts`, `corne_right.dts`
- Sofle: `sofle.dtsi`, `sofle_left.dts`, `sofle_right.dts`

User customization (keymap, behaviors) is layered on top of the hardware definition files.

## Related entities

- [[Entities/corne-keyboard]] — canonical example keyboard
- [[Entities/sofle-keyboard]] — related Sofle layout
- [[Entities/nrf52840]] — the MCU
- [[Entities/a741725193-github-repos]] — the vendor-specific firmware forks

## Related concepts

- [[Concepts/split-keyboard-firmware-architecture]] — broader architecture
- [[Concepts/zmk-tap-dance-behavior]] — the tap-dance pattern
- [[Concepts/wireless-split-pairing-protocol]] — pairing lifecycle
- [[Concepts/bootloader-rubber-ducky-update]] — the firmware update flow
