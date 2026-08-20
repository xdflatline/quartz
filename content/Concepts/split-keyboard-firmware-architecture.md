---
title: "Split Keyboard Firmware Architecture (ZMK)"
details: "Architecture of open-source wireless split-keyboard firmware as exemplified by ZMK on the nrf52840 — two halves with one designated 'main', left/right pairing persisted across firmware updates, a master Bluetooth profile store on the main half, USB/Bluetooth output channel selection with TypeC-as-arbiter, and a flashable USB-mass-storage bootloader that accepts drop-in firmware files in any order."
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

# Split Keyboard Firmware Architecture (ZMK)

The Corne / Sofle "Eyelash" keyboards documented in the [[Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20]] manual illustrate a recurring architectural pattern for open-source wireless split-keyboard firmware. The pattern is built around five interlocking subsystems.

## 1. Asymmetric halves with one designated "main"

In a ZMK split, the **left half is the main keyboard** — it performs more work and therefore consumes more battery than the right half. The right half is essentially an input peripheral that forwards key presses to the main over a short-range radio link. The "main" half owns the Bluetooth radio and the host-side USB/Bluetooth output selection; the "peripheral" half is concerned only with matrix scanning and inter-half transport.

This asymmetry is *load-bearing*: battery size, MCU choice, and antenna placement all assume one half is the radio side.

## 2. Pairing persisted across firmware updates

Left/right pairing is **completed during the first firmware update** and is preserved by subsequent updates. The pairing state lives in a separate settings area that firmware updates do not touch by default. To intentionally reset pairing, the user must flash a dedicated `settings_reset` firmware separately (not part of the normal update flow), then reflash normal firmware on both sides; the halves auto-connect after.

This is a deliberate choice: it makes routine firmware updates atomic and safe for users, while keeping a one-step escape hatch available when settings need to be wiped.

## 3. Multi-profile Bluetooth host storage on the main half

The main half stores **4–5 Bluetooth configuration profiles** for different host devices (PC, phone, tablet). The active profile is rendered on the OLED screen. Keycodes like `BT_SEL_0`, `BT_SEL_1`, `BT_SEL_2`, ... switch between profiles; `BT_CLEAR_ALL` resets all bindings.

The operational hazard this design invites: if the user is connected on profile 1 and accidentally presses the profile-2 keycode, **keystrokes silently route to a different host** — no error, no warning, just no characters appearing in the current window. The manual flags this prominently.

## 4. TypeC-as-arbiter between USB and Bluetooth output

A simple rule governs where keystrokes go: **when a TypeC cable is plugged in, keystrokes go to USB, not Bluetooth**. The firmware keycodes `OUT_BL` and `OUT_USB` override the rule and force routing to a specific channel.

The design rationale: while charging (which always requires USB), the user almost certainly wants to keep typing on the host. Forcing USB-when-plugged makes this the default and keeps `OUT_BL` available for the niche case where the user wants Bluetooth during charging.

## 5. Flashable USB-mass-storage bootloader with no driver

To flash firmware, the user:

1. Plugs in USB
2. Double-presses the reset switch within 0.5 seconds
3. The MCU enters bootloader mode (blue LED breathes)
4. The keyboard appears as a USB mass-storage device on the host
5. The user drags the new firmware files onto the virtual disk

**No flashing order is required** between left and right halves — each half's bootloader accepts its own file independently.

This bootloader pattern is the dominant alternative to vendor-flashing-tools (which require proprietary apps, drivers, or DFU-mode button combos). It works on every host OS without installing anything.

## Power management as a first-class concern

Three of the documented keycodes exist specifically to manage power — RGB's small LED driver chips leak current even when "off":

- `ext_power EP_OFF` / `ext_power EP_ON` — physically cut positive power to the RGB chain
- `RGB_ON` / `RGB_OFF` — software on/off (does not cut power)
- The firmware auto-cuts RGB positive power when RGB is off, but **retains the `EP_ON` keycode in the keymap by default** — the manual warns that accidental `EP_ON` presses are a leading cause of unexpectedly short battery life and recommends deleting that keycode from the keymap.

`&Soft_off` puts the keyboard into a low-power soft-shutdown state distinct from a hardware toggle off (which is reserved for >6-month storage to protect the lithium cells).

## Related concepts

- [[Concepts/zmk-tap-dance-behavior]] — the multi-press keycode behavior used to collapse modifier + Caps onto one key
- [[Concepts/wireless-split-pairing-protocol]] — the inter-half radio link and pairing lifecycle
- [[Concepts/bootloader-rubber-ducky-update]] — the drag-and-drop firmware update pattern in more detail
- [[Entities/zmk]] — the open-source firmware project
- [[Entities/corne-keyboard]] — the canonical example keyboard
- [[Entities/sofle-keyboard]] — the related Sofle layout
