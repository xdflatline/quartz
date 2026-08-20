---
title: "EC11 Rotary Encoder"
details: "EC11 is a small incremental rotary encoder used as a 'knob' on the new-version Corne (Eyelash Corne). In ZMK it is mapped to: rotate = volume adjust; press = SPACE; other layers = mouse wheel scroll. The optional companion joystick on the same keyboard handles arrow-key and mouse-cursor duties."
tags:
  - entity
  - hardware
created: 2026-08-20
updated: 2026-08-20
type: entity
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# EC11 Rotary Encoder

The **EC11** is a small incremental rotary encoder used as the "knob" on the new-version [[Entities/corne-keyboard]] (Eyelash Corne). The Eyelash Corne ships with the EC11 as an optional hardware add-on; the old Corne and the Sofle do not include it.

## Mapping (ZMK)

| Action | Function |
|--------|----------|
| Rotate | Volume adjust |
| Press | SPACE |
| Other layers | Mouse wheel scroll |

## Companion hardware: joystick

The same Eyelash Corne also includes an optional **joystick**, mapped as:

| Layer | Function |
|-------|----------|
| Layer 1 | Direction keys (up/down/left/right); press = ENTER |
| Other layers | Mouse movement simulation; press = left mouse button |

> **Note:** The joystick mouse function is "far less user-friendly than a real mouse. It is only a temporary backup and cannot replace a mouse fully." (per the original manual)

## Thumb-cluster integration

The new-version Corne uses the EC11 + joystick to take over the thumb roles from the standard 42-key Corne layout:

- **Left knob press** = SPACE
- **Right joystick press** = ENTER

This replaces the `&lt 3 SPACE` / `&gt 3 ENTER` hold-tap pattern used on the older Corne variant.

## Related entities

- [[Entities/corne-keyboard]] — the keyboard the EC11 ships with

## Related concepts

- [[Concepts/zmk-tap-dance-behavior]] — the multi-action keycode behavior that complements the encoder's press-and-rotate model
