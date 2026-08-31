---
title: "Quickshell Documentation Bundle"
details: "Verbatim bundle of quickshell.org public pages (homepage, about, install guide, v0.3.0→v0.3.1 changelog) retrieved 2026-08-31. Covers Quickshell's QtQuick/QML desktop-shell toolkit, its Wayland/X11 compositor integrations, and the showcase desktop configurations built on top of it (Caelestia, Illogical-Impulse, Zephyr, outfoxxed's nixnew)."
tags:
  - raw
  - documentation
  - linux
  - desktop
  - qt
created: 2026-08-31
updated: 2026-08-31
type: raw
source: "https://quickshell.org/"
---

# Quickshell Documentation Bundle

**Source:** quickshell.org (homepage + /about + /docs/v0.3.0/guide/install-setup + /changelog)
**Date Retrieved:** 2026-08-31
**Type:** Documentation

This is a verbatim bundle of Quickshell's public-facing pages. Pages are concatenated in retrieval order so the original structure and ordering of headings, lists, and code blocks is preserved.

---

## 1. Homepage (https://quickshell.org/)

# Quickshell - Summary

## Overview

**Quickshell** is a toolkit for building status bars, widgets, lockscreens, and other desktop components using **QtQuick**. It works alongside your Wayland compositor or window manager to build a complete desktop environment.

**Latest Release:** Quickshell 0.3.1 — released 2026-08-20 ([changelog](https://quickshell.org/changelog))

**Tagline:** *"building blocks for your desktop"*

**Quick Links:**
- [Install](https://quickshell.org/docs/v0.3.0/guide/install-setup)
- [Documentation](https://quickshell.org/docs/v0.3.0/types)
- [More information](https://quickshell.org/about)

---

## Key Features

### 1. Real-Time Changes
> Quickshell loads changes as soon as they're saved, letting you iterate as fast as you can type.

### 2. Easy-to-Use Language
- Configured in **QML**, a simple language designed for creating flexible user interfaces
- Includes **LSP support**

### 3. Extensive Integrations
A large set of integrations with new ones arriving all the time.

**Supported/Integrated With:**
- Wayland
- Hyprland
- Pipewire
- X.Org
- Sway

## Code Example

A standard desktop window with an animated color-changing timer:

```qml
// a standard desktop window
FloatingWindow {
    Timer {
      // assign an id to the object, which can be
      // used to reference it
      id: timer
      property bool invert: false // a custom property

      // change the value of invert every half second
      running: true; repeat: true
      interval: 500 // ms
      onTriggered: timer.invert = !timer.invert
    }

    // change the window's color when timer.invert changes
    color: timer.invert ? "purple" : "green"
}
```

**What this demonstrates:**
- `FloatingWindow` — creates a desktop window
- `Timer` — built-in object with properties like `running`, `repeat`, `interval` (ms)
- Custom properties via `property bool invert: false`
- Reactivity — the `color` binding automatically updates when `timer.invert` changes
- Event handling via `onTriggered`

## Configuration Showcase

Example desktop configurations built with Quickshell:

| Author | Source |
|--------|--------|
| **soramane** | [caelestia-dots/shell](https://github.com/caelestia-dots/shell) |
| **end_4** | [dots-hyprland](https://github.com/end-4/dots-hyprland) |
| **outfoxxed** | [nixnew/modules/quickshell](https://git.outfoxxed.me/outfoxxed/nixnew/src/branch/master/modules/user/modules/quickshell) |
| **pfaj** & **bdebiase** | GitHub profiles available |
| **flicko** | [zephyr](https://github.com/flickowoa/zephyr) |
| **vaxry** | [vaxry.net](https://vaxry.net/) |

These showcase the range of customization possible with Quickshell across different workflows (including Nix-based setups).

---

## 2. About (https://quickshell.org/about)

# About Quickshell

Quickshell is a toolkit for building a desktop shell, which is to say components
of your desktop like bars, widgets, lock screens, display managers, and the like.

Quickshell is based on QtQuick and configured with QML, the QtQuick interface
description language. It provides integrations for common shell functionality,
as well as support for hot reloading and tools to work with processes,
sockets, files, and more.

Built-in integrations are currently provided for:

- Wayland and X11 for windowing
- Wayland for window management and screen recording
- Workspace management in Hyprland, I3, and Sway
- Pipewire for audio controls
- BlueZ for bluetooth
- Pam for authentication and building lockscreens
- Greetd for building a display manager
- UPower for monitoring battery statistics
- Power Profiles Daemon
- MPRIS compatible media players
- StatusNotifierItem compatible system tray clients

## Is Quickshell for me?

#### I want a preconfigured desktop

There are many setups intended to be useful without much tweaking, for example:

- [Caelestia](https://github.com/caelestia-dots/shell) by Soramane
- [Illogical-Impulse](https://github.com/end-4/dots-hyprland) by end\_4.

#### I want to make my own

Quickshell is a relatively low-level tool compared to simple status bars like Waybar.
When writing a Quickshell configuration, you are not just changing styles and layouts, but
practically programming, which is considerably more complex.

You can see the [QML Language Reference](https://quickshell.org/docs/guide/qml-language) to get an idea
of what you're getting into.

NEXT STEPS

See the [Usage Guide](https://quickshell.org/docs/guide) to learn how to set up and use Quickshell.

---

## 3. Install & Setup (https://quickshell.org/docs/v0.3.0/guide/install-setup)

# Quickshell Installation & Setup Guide

> **Note:** Quickshell is still in early development. Breaking changes are expected before 1.0, but a migration guide will be provided.

## Optional Dependencies

Install these additional packages for full functionality (names vary by distro):

- `qtsvg` — SVG image loading support (bundled with most packages)
- `qtimageformats` — WEBP and other less common image formats
- `qtmultimedia` — Video and audio playback
- `qt5compat` — Extra visual effects (notably gaussian blur). **MultiEffect is usually preferable**

## Installation Methods by Distribution

### Nix

Release versions available from Nixpkgs as `quickshell`.

Embedded flake mirrors:
- `git+https://git.outfoxxed.me/outfoxxed/quickshell`
- `github:quickshell-mirror/quickshell`

> **Tip:** Use `?ref=` to specify a tag for a tagged release.

**Example flake configuration:**
```nix
{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";

    quickshell = {
      # add ?ref=<tag> to track a tag
      url = "git+https://git.outfoxxed.me/outfoxxed/quickshell";

      # THIS IS IMPORTANT
      # Mismatched system dependencies will lead to crashes and other issues.
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
}
```

Package available as `quickshell.packages.<system>.default`. Can be added to `environment.systemPackages`, `home.packages` (home-manager), or a devshell.

**Add QML packages:** Use `<package>.withModules [ <extra modules> ]`

### Arch

```bash
pacman -S quickshell
```

For master branch: [`quickshell-git`](https://aur.archlinux.org/packages/quickshell-git) AUR package:
```bash
yay -S quickshell-git
```

> **Warning:** AUR packages may break when Qt is updated. Quickshell will warn you on detection—reinstall if warned.

### Fedora

```bash
sudo dnf install quickshell
```

**Fedora COPR** ([errornointernet/quickshell](https://copr.fedorainfracloud.org/coprs/errornointernet/quickshell)) offers:
- `quickshell` — latest release
- `quickshell-git` — master branch

```bash
sudo dnf copr enable errornointernet/quickshell
sudo dnf install quickshell
# or
sudo dnf install quickshell-git
```

### Debian

```bash
sudo apt install quickshell
```

### OpenSUSE

Via Open Build Service [`home:AvengeMedia:danklinux`](https://build.opensuse.org/project/show/home:AvengeMedia%3Adanklinux):
- `quickshell` — latest release — [Install](https://software.opensuse.org//download.html?project=home%3AAvengeMedia%3Adanklinux&package=quickshell)
- `quickshell-git` — master branch — [Install](https://software.opensuse.org//download.html?project=home%3AAvengeMedia%3Adanklinux&package=quickshell-git)

### Ubuntu

Via [`avengemedia/danklinux`](https://launchpad.net/~avengemedia/+archive/ubuntu/danklinux) PPA:
- `quickshell` — latest release
- `quickshell-git` — master branch

```bash
sudo add-apt-repository ppa:avengemedia/danklinux
sudo apt update
sudo apt install quickshell
# OR
sudo apt install quickshell-git
```

### Gentoo

Available in GURU as `gui-apps/quickshell`:
```bash
emerge eselect-repository
eselect repository enable guru
emerge --sync guru
emerge gui-apps/quickshell
```

### Guix

Available from `(gnu packages wm)` module:
```bash
guix install quickshell
```
Can also be added to Guix system or Guix Home configuration.

### Manual Build

See [BUILD.md](https://git.outfoxxed.me/quickshell/quickshell/src/branch/master/BUILD.md) for instructions.

---

## Editor Configuration

A QML grammar and LSP are recommended for writing configurations.

### Emacs

Install:
- [yuja/tree-sitter-qml](https://github.com/yuja/tree-sitter-qmljs) tree-sitter grammar
- [xhcoding/qml-ts-mode](https://github.com/xhcoding/qml-ts-mode) mode

Both available via Nix through [outfoxxed/nix-qml-support](https://git.outfoxxed.me/outfoxxed/nix-qml-support).

Either `lsp-mode` or `eglot` works for LSP.

**Example config:**
```elisp
(use-package qml-ts-mode
  :after lsp-mode
  :config
  (add-to-list 'lsp-language-id-configuration '(qml-ts-mode . "qml-ts"))
  (lsp-register-client
   (make-lsp-client :new-connection (lsp-stdio-connection '("qmlls"))
                    :activation-fn (lsp-activate-on "qml-ts")
                    :server-id 'qmlls))
  (add-hook 'qml-ts-mode-hook (lambda ()
                                (setq-local electric-indent-chars '(?\n ?\( ?\) ?{ ?} ?\[ ?\] ?\; ?,))
                                (lsp-deferred))))
```

### Neovim

Built-in syntax highlighting exists, but tree-sitter may work better:
```
:TSInstall qmljs
```

For LSP, install [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) and add:
```lua
require("lspconfig").qmlls.setup {}
```

### Helix

Built-in syntax highlighting and qmlls support included.

### VSCode

1. Install the [Official QML Support extension](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt-qml)
2. Enable the `qt-qml.qmlls.useQmlImportPathEnvVar` setting

---

## Language Server (qmlls)

[qmlls](https://doc.qt.io/qt-6/qtqml-tooling-qmlls.html) catches bad practic
[... truncated in source extraction, full page continues at source URL ...]

---

## 4. Changelog Summary (https://quickshell.org/changelog) — v0.1.0 → v0.3.1

# Quickshell Changelog Summary

A comprehensive changelog covering releases **v0.1.0 → v0.3.1** of Quickshell, a Linux desktop shell/UI framework.

## v0.3.1

[Documentation](https://quickshell.org/docs/v0.3.1/guide)

### Bug Fixes

- **ScreencopyView** not displaying when only lock surfaces are shown
- `WlSessionLockSurface.visible` crashing if accessed before backing surface creation
- `MprisPlayer` returning `rate` for `minRate` and `maxRate`
- Missing/wrong change signals on various properties
- Session lock crashes on sleep, wake, DPMS, and unlocking
- `QsWindow.updatesEnabled` ensures windows are redrawn when set to true
- Potential crashes from `WindowsetProjection.screens` during monitor unplug
- Crashes from accessing freed objects via `ScriptModel`
- Crashes when wifi networks disappear
- Unhandled notifications sending `NotificationClosed` out of order
- `qs kill` not waiting for process to exit
- IPC calls from children of crashed/relaunched process crashing
- `JsonAdapter` crashing when deserializing new objects into an array
- `Toplevel.unsetRectangle` crashing when called
- Intermittent `FileView` crashes when updating watched files
- `ColorQuantizer` deletion crashing if an operation was live
- Crashes when failing to create a `ScreencopyView`
- `PwNodePeakMonitor` crashing when sampling streams with mismatched channels
- Unsetting `PopupAnchor.item` causing a crash
- Hiding the last `PanelWindow` on screen causing a crash under X11
- Crashes when `ScriptModel.values` is set while processing previous values

## v0.3.0

[Documentation](https://quickshell.org/docs/v0.3.0/guide)

### Warning Breaking Changes

**Config paths are no longer canonicalized** — fixes nix configs changing shell-ids on rebuild. Shell id is now derived from the symlink path. Configs with symlinks will have different shell ids.

> Shell ids are used to derive the default config/state/cache folders, so those files will need to be manually moved if using a config behind a symlinked path without an explicitly set shell id.

### New Features

- Polkit agent creation support
- Wayland idle inhibitors
- Wayland idle timeouts
- Inhibiting wayland compositor shortcuts for focused windows
- Override `Quickshell.cacheDir` with custom path
- Minimized/maximized/fullscreen properties for `FloatingWindow`
- Move and resize event handling for `FloatingWindow`
- Pipewire service auto-reconnect on death/protocol error
- **Pipewire audio peak detection**
- **Network management support**
- Grabbing focus from popup windows
- IPC signal listeners
- Quickshell version checking and version-gated preprocessing
- Icon source detection (system theme vs. not)
- Vulkan support to screencopy
- Generic `WindowManager` interface implementing ext-workspace
- ext-background-effect **window blur support**
- Per-corner radius support to `Region`
- `ColorQuantizer` region selection
- Dialog window support for `FloatingWindow`
- Lua config support for Hyprland module

### Other Changes

- IPC operations filter available instances to current display connection by default
- `PwNodeLinkTracker` ignores sound level monitoring programs
- Replaced **breakpad with cpptrace**
- Reloads prevented if no file content changed
- New environment variables:
  - `QS_DISABLE_FILE_WATCHER` — disable file watching
  - `QS_DISABLE_CRASH_HANDLER` — disable crash handling
  - `QS_CRASHREPORT_URL` — override crash reporter link
- `AppId` pragma + `QS_APP_ID` env var for desktop application ID override
- `DropExpensiveFonts` pragma + `QS_DROP_EXPENSIVE_FONTS` env var (avoids laggy/memory-heavy fonts)
- `DefaultEnv` pragma to set env vars if not already set
- Unrecognized pragmas no longer a hard error (for future backward compatibility)

### Bug Fixes

- Volume control issues with pipewire pro audio, bluez streams, devices without route definitions
- Pipewire volumes not initializing if device was loaded before its node
- Hyprland: active toplevel not resetting after window closes; IPC window names/titles reversed; crash when refreshing toplevels before workspaces
- Missing signals for system tray item title/description updates
- Asynchronous loaders not working after reload / before window creation
- Memory leak in IPC handlers
- `ClippingRectangle` related crashes
- Crashes on monitor unplug and lost default pipewire devices
- `ToplevelManager` not clearing activeToplevel on deactivation
- Desktop action order preservation
- Partial socket reads in greetd and hyprland on slow machines
- Qt bug workaround for plugging/unplugging monitors
- `HyprlandFocusGrab` crash if windows destroyed after being passed
- `ScreencopyView` pixelation when scaled
- `JsonAdapter` crashes/bad data with `JsonObject`, unnecessary primitive property changes, list serialization
- Pipewire crashes after device hotplug and default output changes
- `--daemonize` launch failures on some systems
- Screencopy crashes across GPUs
- Pipewire volumes not working for some pw-pulse clients
- Nulls in
[... truncated in source extraction, full page continues at source URL ...]

### Earlier versions

The full changelog also documents releases **v0.1.0** and **v0.2.0** with their respective features and fixes. See the source URL for the complete history.