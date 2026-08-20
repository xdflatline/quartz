---
title: "Corne Mechanical Split Keyboard Owner's Manual"
details: "Owner's manual for the Eyelash Corne / Sofle mechanical split keyboard sold via manuals.plus, covering ZMK firmware on nrf52840, charging/pairing/reset procedures, the full ZMK keycode reference (Bluetooth profiles, RGB, channel selection, state control, tap-dance, layer-tap thumbs, EC11 knob, joystick), hardware specs (batteries, screws, switches, LEDs), and the seller-specific GitHub firmware repositories."
tags:
  - raw
  - documentation
  - hardware
source: https://manuals.plus/corne/mechanical-split-keyboard-manual
created: 2026-08-20
updated: 2026-08-20
type: raw
---

# Corne Mechanical Split Keyboard Owner's Manual

**Source:** Manuals+ (https://manuals.plus/corne/mechanical-split-keyboard-manual)
**Date Retrieved:** 2026-08-20
**Type:** Hardware manual / vendor documentation

> Verbatim ingestion of the Manuals+ Corne Mechanical Split Keyboard Owner's Manual, merged with the Swedish (sv) and German (de) mirror pages for completeness. All keycodes, hardware specs, repository links, and procedural details are preserved.

---

## Overview

The Corne is a **wireless mechanical split keyboard** running the open-source **ZMK** keyboard firmware on an **nrf52840** microcontroller, with Bluetooth connectivity, hot-swappable switches, and OLED screen support. The same vendor also sells a related **Sofle** layout that shares firmware conventions. The manual covers the Corne/Sofle "Eyelash" variant sold by the `a741725193` seller (whose GitHub hosts the firmware configuration repositories).

## Specifications

| Component | Details |
|-----------|---------|
| **MCU** | nrf52840 |
| **Main control core board** | 52840micro |
| **Wireless connectivity** | Bluetooth |
| **Wired connectivity** | USB (TypeC) |
| **Keyboard layouts** | Corne, Sofle |
| **Firmware** | ZMK (open-source) |
| **Battery (Corne)** | 1500mAh (504060) lithium battery |
| **Battery (Sofle)** | 2000mAh (505060) lithium battery |
| **Battery interface** | PH2.0 socket |
| **Battery protection** | Built-in protective plates auto-stop charging when full |
| **Charging time** | 6–8 hours (varies by battery capacity) |
| **Charging source** | Any phone charging head + TypeC cable |

## GitHub Repositories (Firmware Configurations)

> Each keyboard has its own specific GitHub repository. **Ask the seller which repo corresponds to your purchase.** Repositories are described as "irregularly updated."

| Keyboard | Repository |
|----------|-----------|
| Eyelash Corne | https://github.com/a741725193/zmk-new-corne |
| Eyelash Sofle | https://github.com/a741725193/zmk-sofle |
| Sofle Dongle | https://github.com/a741725193/zmk-sofle-dongle |
| Corne Dongle | https://github.com/a741725193/zmk-corne-dongle |
| Eyelash Corne OLED | https://github.com/a741725193/zmk-corne-oled |

> Low-profile Corne and Sofle use the **same GitHub repo** as the MX version. A shell model file will be uploaded to the repository in the future.

## Hardware Definition Files

- Corne: `corne.dtsi`, `corne_left.dts`, `corne_right.dts`
- Sofle: `sofle.dtsi`, `sofle_left.dts`, `sofle_right.dts`

## Detailed Usage Method

### 1. Power Switch & Charging

- Both Corne and Sofle have a **toggle switch on each side** (left and right)
- **Switch flipped down = ON (open) state**
- **Switch must be ON when charging** (otherwise battery cannot charge)
- **Charging time:** 6–8 hours (varies by battery capacity)

**Green LED status (charging indicator, located at the TypeC interface on the new version):**

| State | Meaning |
|-------|---------|
| Solid / steady on | Charging in progress |
| Off | Charging complete |
| Flashing | Power switch is disconnected (off), OR battery is not connected |

> **Battery maintenance:** Only turn off the power switch if the keyboard will be unused for **more than 6 months**, to avoid lithium battery damage. Batteries have protective plates that auto-stop charging when full.

### 2. Reset & Firmware Flashing

- There is a **press switch near the keyboard switches** — single press = restart
- To enter firmware flashing mode:
  1. Plug in the USB cable
  2. Press the reset switch **twice within 0.5 seconds**
- After entering flashing mode, the keyboard appears as a **USB disk** on the computer
- Drag left and right firmware files into the virtual USB disk — **no left/right order required**

**Blue LED status (MCU working status):**

| State | Meaning |
|-------|---------|
| Breathing | BootLoader mode, USB connected to computer |
| Fast flashing | BootLoader mode, USB not connected (cannot communicate) |
| Off | ZMK firmware running normally |

### 3. Left/Right Pairing

- After power-on, the **left and right halves automatically connect**
- **Left half = main keyboard** (performs more work, consumes more battery)
- **Pairing is completed during the first firmware update**
- Subsequent firmware updates **do not clear** left/right pairing info
- **Normal communication distance:** 0.6–0.8 meters

**To reset left/right pairing:**

1. Flash `settings_reset` firmware separately (on the affected half)
2. Then flash normal firmware on both sides
3. The halves will auto-connect again

### 4. Bluetooth Connection (to computer / phone)

- Power on the keyboard
- On the host's Bluetooth page, add a new device, or click the device named **"corner"** or **"sofle"**
- The keyboard can store **4–5 Bluetooth configuration profiles** (for multiple devices: PC, phone, tablet)
- The **currently active profile is displayed on the OLED screen**

**Warning:** If you accidentally press a profile keycode while connected (e.g., switch from profile 1 to profile 2), **keycodes will not reach your original host**. They will go to the host currently bound to the selected profile.

**On abnormal connection:** Press `BT_CLEAR_ALL` (located on layer 2; requires a key combo) to reset, then reconnect.

### 5. Keymap Reference

- Button functions are shown in the **keymap diagram** (in the product intro and screenshots)
- Most buttons use **combination keys** — refer to the GitHub repository for button icons

## ZMK Keycode Reference

### Bluetooth Management

| Keycode | Function |
|---------|----------|
| `Bt_clear_all` | Clear all Bluetooth connections (use for abnormal connections, then reconnect) |
| `BT_SEL_0` | Bluetooth profile 0 |
| `BT_SEL_1` | Bluetooth profile 1 |
| `BT_SEL_2`, `BT_SEL_3`, ... | Additional profiles (up to 4–5 devices) |

### Power Output Switch (RGB ext-power)

RGB chips continuously consume power even when "off" due to small chips inside the LEDs. The keyboard **automatically cuts off positive power to RGB** when off, but retains the `EP_ON` keycode in firmware. Accidentally pressing `EP_ON` significantly drains battery.

| Keycode | Function |
|---------|----------|
| `ext_power EP_OFF` | Turn off RGB power |
| `ext_power EP_ON` | Turn on RGB power (⚠️ battery drain — consider deleting this keycode from your keymap) |

> **Daily use:** RGB on/off automatically activates/deactivates RGB output. If battery life is suddenly poor, you may have accidentally pressed `EP_ON`. Consider removing the `EP_ON` keycode from the keymap entirely to prevent accidental activation.

### RGB Light Control

RGB consumes significant power. Use mainly for photos or status indication.

| Keycode | Function |
|---------|----------|
| `RGB_ON` | Turn on RGB |
| `RGB_OFF` | Turn off RGB |

**Power consumption (per side):**

- Single RGB LED ≈ **15mA**
- 30 keys per side ≈ **450mA total per side**
- **Backlight mode** (briefly lights up, then gradually fades) uses much less power than constant backlight
- Left and right RGB control **synchronizes** — useful for testing left/right connection

### Bluetooth / USB Channel Selection

When a TypeC cable is plugged in, keycodes **automatically route to USB**, not Bluetooth. This matters during charging: keycodes won't send via Bluetooth while the cable is connected.

| Keycode | Function |
|---------|----------|
| `OUT_BL` | Force send keycodes to Bluetooth channel |
| `OUT_USB` | Force send keycodes to USB channel |

### Keyboard State Control

| Keycode | Function |
|---------|----------|
| `&Soft_off` | Enter soft shutdown state |
| `&sys_deset` | Restart the keyboard |
| `&bootloader` | Enter bootloader flashing state (or double-click the physical reset switch) |

### Special Characters (ZMK keypress format)

On keyboards without a number row (like the Corne), use direct key combinations. The shift layer maps shift+1 → "!", etc.

```
&kp EXCL  →  "!"
&kp AT    →  "@"
&kp HASH  →  "#"
```

Refer to the GitHub repository and README for the complete mapping.

### Tap-Dance (TD) Combination Buttons

Example from the keymap file (`td0` defined as a tap-dance behavior):

```dts
td0: td0 {
    compatible = "zmk,behavior-tap-dance";
    label = "TD0";
    #binding-cells = <0>;
    bindings = <&kp LEFT_SHIFT>, <&kp CAPS>;
};
```

Behavior: **short press** = Left Shift; **double click** = Caps Lock.

Users can add additional tap-dance behaviors (`TD1`, `TD2`, etc.), modify `TD0`, or move them to other button positions.

### Thumb Key Behavior (Corne)

| Keycode | Short press | Long press |
|---------|-------------|------------|
| `&lt 3 SPACE` | SPACE | Layer 3 |
| `&gt 3 ENTER` | ENTER | Layer 3 |

**New version (hardware revision with knob / joystick):**

- **Left knob press** = SPACE
- **Right joystick press** = ENTER

## Knob (EC11) and Joystick

### Knob (EC11 encoder)

| Action | Function |
|--------|----------|
| Rotate | Volume adjustment |
| Press | SPACE (sent to PC) |
| Other layers | Mouse wheel scroll |

### Joystick

| Context | Function |
|---------|----------|
| Layer 1 | Direction keys (up/down/left/right); press = ENTER |
| Other layers | Mouse movement simulation; press = left mouse button |

> **Note:** The joystick mouse function is **far less user-friendly than a real mouse**. It is only a **temporary backup** and cannot replace a mouse fully.

## Hardware Details

### LED Indicators (full reference)

| LED Color | State | Meaning |
|-----------|-------|---------|
| Green | Solid / steady | Charging in progress |
| Green | Off | Charging complete |
| Green | Flashing | Battery disconnected OR power switch off (and USB connected) |
| Blue | Breathing | BootLoader mode, USB connected |
| Blue | Fast flashing | BootLoader mode, no USB connection |
| Blue | Off | Normal ZMK operation |

### Screws and Components

| Component | Specification |
|-----------|---------------|
| PCB-to-case screws | M2 × 4 with embedded nuts M2 × 2 × 3.2 (M2 × 2 × 3 copper nuts also work) |
| Positioning board / PCB screws | M2 × 4 self-tapping |
| Screen cover | Tempered glass, fixed with M2 × 2 screws (easy maintenance) |
| Foot pads | 10 × 2 rubber |
| Main control board | 52840micro |

### Power Switch Models

| Hardware revision | Model |
|-------------------|-------|
| New Corne | MINI MKS12C01 |
| Old Corne / Sofle | MKS12C02 |
| Reset switch (new Corne / Sofle) | TS24CA |

### Battery Maintenance

- Only turn off the power switch if the keyboard will be unused for **more than 6 months**, to avoid lithium battery damage
- Batteries have **built-in protective plates** that auto-stop charging when full
- Charging interface: **PH2.0 socket**

### Hardware Definition Files

- Corne: `corne.dtsi`, `corne_left.dts`, `corne_right.dts`
- Sofle: `sofle.dtsi`, `sofle_left.dts`, `sofle_right.dts`

## ZMK Firmware Repositories (Seller-Specific Summary)

> Each keyboard has its own GitHub repo. **Ask the seller which repo matches your purchase.** Repositories are irregularly updated.

| Keyboard | Repository |
|----------|-----------|
| Eyelash Corne | https://github.com/a741725193/zmk-new-corne |
| Eyelash Sofle | https://github.com/a741725193/zmk-sofle |
| Sofle Dongle | https://github.com/a741725193/zmk-sofle-dongle |
| Corne Dongle | https://github.com/a741725193/zmk-corne-dongle |
| Eyelash Corne OLED | https://github.com/a741725193/zmk-corne-oled |

> Low-profile Corne and Sofle use the **same GitHub repo** as the MX version.

## Quick-Reference Summary

**To power on:** Toggle switch down on both halves.

**To charge:** Plug TypeC cable into any phone charger; 6–8 hours. Green LED solid = charging, off = full.

**To flash firmware:** Plug USB → double-press reset switch within 0.5s → blue LED breathes → keyboard appears as USB disk → drag firmware files.

**To pair left/right halves:** Happens automatically on first firmware flash. To reset: flash `settings_reset` firmware separately, then reflash normal firmware.

**To connect Bluetooth:** Add device named "corner" or "sofle". Can store 4–5 profiles.

**To clear Bluetooth state:** Press `BT_CLEAR_ALL` (on layer 2).

**To enter bootloader:** Double-click reset switch within 0.5s with USB plugged in.

**To soft-off:** Press `&Soft_off`.

**To force Bluetooth output:** Press `OUT_BL`.

**To force USB output:** Press `OUT_USB`.
