---
title: "Bootloader USB-Mass-Storage Firmware Update"
details: "The Corne/Sofle firmware update pattern: double-press the reset switch within 0.5s with USB plugged in to enter bootloader mode, the MCU then enumerates as a USB mass-storage device, and the user drags the new firmware file(s) onto the virtual disk. No host-side driver, no flashing tool, no left/right order required."
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

# Bootloader USB-Mass-Storage Firmware Update

The Corne / Sofle "Eyelash" keyboards documented in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual use a bootloader pattern that has become the de-facto standard for open-source keyboard firmware (also used by QMK's `katana`/`uf2` bootloaders on some boards). The pattern's defining properties:

## Procedure

1. Plug the keyboard into the host via USB.
2. **Double-press the physical reset switch within 0.5 seconds.**
3. The MCU enters **bootloader mode**. Indication: blue LED breathes (with USB connected) or fast-flashes (without USB).
4. The keyboard **enumerates as a USB mass-storage device** on the host — a virtual disk drive appears with no driver install required.
5. The user **drags the new firmware file(s)** onto the virtual disk (left and right files; **no order required**).
6. The MCU writes the firmware and reboots into the new image.

## Why this pattern

- **No host-side tool required.** Every modern OS already speaks USB mass storage natively. No `dfu-util`, no proprietary app, no Python script, no driver signing.
- **Order-independent.** Left and right halves flash independently; the user can drag both files in either order, or one at a time.
- **Reversible.** If the new firmware bricks the keyboard, the bootloader is still intact and the user can flash the old firmware back the same way.
- **Discoverable from the OS.** The disk appears in Finder / Explorer / Files — the same UI the user already uses for any other file copy.

## The double-press timing window

The 0.5-second double-press window is the gating condition. The reasoning:

- A **single press** is reserved for the normal "restart keyboard" function (and is harmless — the keyboard simply reboots).
- **Two presses within 0.5 seconds** unambiguously signals user intent to enter the bootloader.
- The window is short enough that accidental double-presses during normal use don't trigger it, and long enough that an intentional double-press is easy to land.

The `&bootloader` ZMK keycode provides a software path into the same state — useful for a keymap-reset-to-bootloader flow that doesn't require the user to find the physical switch.

## Indicator states (full table)

| LED color | State | Meaning |
|-----------|-------|---------|
| Blue | Breathing | BootLoader mode, USB connected to host |
| Blue | Fast flashing | BootLoader mode, USB not connected |
| Blue | Off | Normal ZMK operation |
| Green | Steady | Charging in progress |
| Green | Off | Charging complete |
| Green | Flashing | Battery not connected OR power switch off |

## Related concepts

- [[Concepts/split-keyboard-firmware-architecture]] — the broader architecture
- [[Concepts/wireless-split-pairing-protocol]] — how pairing interacts with updates
- [[Entities/zmk]] — the firmware project
- [[Entities/nrf52840]] — the MCU that provides the bootloader
