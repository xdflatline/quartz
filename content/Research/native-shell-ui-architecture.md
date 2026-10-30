---
title: "Native Shell UI Architecture"
details: "A synthesis of NSH's two normative guides: the design guide's visual and interaction judgment and the coding guide's architecture discipline. The two share one premise - code structure should preserve product intent, not replace it. Covers the design thesis, layer stack, reactive model, state ownership, behavior/presentation split, token discipline, and the checklists that gate a change."
tags:
  - research
  - desktop
  - architecture-pattern
  - documentation
created: 2026-10-30
updated: 2026-10-30
type: research
sources:
  - Raw/nsh-design-guides.md
  - Raw/nsh-coding-guides.md
---
# Native Shell UI Architecture

**Source:** [[Raw/nsh-design-guides]], [[Raw/nsh-coding-guides]]
**Type:** Research Synthesis
**Date:** 2026-10-30

## Scope

This page synthesizes Native Shell's two normative guides into one argument. The **Design Guides** carry product judgment; the **Coding Guides** carry architecture discipline. The coding guide opens by stating the relationship: *"Read the Design Guides first: code structure should preserve product intent, not replace it."*

Both use the same normative vocabulary — **must** for lifecycle, correctness or ecosystem constraints; **should** for the default that requires a concrete reason to depart; **may** for optional technique.

## The Shared Premise

NSH is a framework whose central bet is that **behavior and presentation are separable, and only the framework can own behavior**.

- `nsh` provides primitives: styles, layout, reactivity, environment.
- `nsh/base` provides reusable behavior: navigation, dialogs, popovers, menus, sheets, press targets — with focus, keyboard, dismissal, and accessibility contracts.
- The app provides the visual language and the domain meaning.

The design guide's contribution is the *judgment* the app layer must supply; the coding guide's contribution is the *mechanics* that keep the layers honest. Every design rule in the first has a mechanical counterpart in the second.

## Concepts Index

| Concept | Source guide | Core claim |
|---|---|---|
| [[Concepts/native-shell-design-system|Native Shell Design System]] | Design | Native, quiet, precise; clarity before personality; tokens before values |
| [[Concepts/semantic-color-tokens|Semantic Color Tokens]] | Both | Colors resolve by role; raw hex only in theme definitions |
| [[Concepts/native-shell-ui-language|Native Shell UI Language]] | Both | Words are interface architecture; context economy; one lexicon |
| [[Concepts/native-shell-architecture|Native Shell Architecture]] | Coding | Dependencies point downward; app shell → pages → components → nsh/base → nsh |
| [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]] | Coding | Component bodies run once; only bindings that read a changed signal re-run |
| [[Concepts/native-shell-state-ownership|Native Shell State Ownership]] | Coding | The narrowest owner that can keep state correct; controlled values over callbacks |
| [[Concepts/stable-domain-identity|Stable Domain Identity]] | Coding | A key is behavior; domain ids, never indices or random keys |
| [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] | Both | Base owns behavior; the app owns the visual language |
| [[Concepts/native-shell-api-widening|Native Shell API Widening]] | Coding | Signed packages may never be rebuilt; public APIs only widen |

## Entities

- [[Entities/native-shell-nsh|Native Shell (NSH)]] — the framework itself
- [[Entities/gpui-kit|GPUI Kit]] — the desktop kit whose judgment NSH carried over

## The Tenets, Mapped Across Both Guides

**1. Clarity before personality.** The design guide's first thesis. Its mechanical counterpart is "start from the task": write down the primary task, the object being viewed, the immediately available actions, the required decision information, and the empty/loading/error/offline/read-only/permission-denied states *before* drawing a screen.

**2. Composition before invention.** The counterpart is the behavior/presentation boundary: compose from the standard semantic component; do not reproduce a menu, popover, sheet or dialog from generic views merely to match one screenshot. If the standard component cannot express a recurring valid pattern, improve its explicit API rather than styling arbitrary descendants at each call site.

**3. Tokens before values.** The counterpart is semantic color tokens plus the scale discipline: a finite radius scale, a compact spacing scale (2/4/8/12/16/24/32), a type scale near 12/14/16/18/20, and the rule that application layout should not write literal point values. Missing roles are added to the app's theme file, not hardcoded at the call site.

**4. Platform before web convention.** The counterpart is the platform and capability boundary: platform-specific code goes where NSH gives it a place (`ios={{…}}`, `android={{…}}`, `desktop={{…}}`, `web={{…}}`), a platform branch must preserve the semantic contract even if presentation differs, and every branch on a value NSH reports needs a `default` because later releases add platforms.

**5. State must be visible.** The counterpart is state ownership and controlled values: hover, pressed, focus, selected, disabled, loading and error each have distinct treatment, and the app's state lives in the narrowest owner that can keep it correct.

**6. Geometry explains containment.** The counterpart is the alignment-spine discipline: a one-rendered-pixel difference between intended-equal gaps is a defect, but the fix is the structural owner, never a raw point offset.

**7. Feedback reflects reality.** The counterpart is explicit async states — a resource's `state()` is `unresolved`, `pending`, `ready`, `refreshing` or `errored`, and a loading treatment must represent actual waiting.

## The Web-Habit Translation Table

The design guide's most distinctive artifact is a table of web habits and their NSH defaults. It is a compact statement of the platform-first thesis:

| Web habit | NSH default |
|---|---|
| Pointing-hand cursor on every button | Default cursor; pointing hand for links |
| Page navigation as the main structure | Persistent windows, panes, sidebars, tabs, menus on desktops; a `NavStack` with the system's back on phones |
| Browser focus and scrolling as a fallback | Explicit focus ownership and region-owned scrolling (`Scroll`, `List`) |
| Mobile-first single column | One column on phones, a resizable shell with a defined minimum window size on desktops |
| Hover-revealed critical actions | Keyboard-, touch- and pointer-reachable actions that do not depend on hover |
| A row of hover-only icon buttons | A visible primary action plus `Menu` or `ContextMenu` |
| Link-styled text for application commands | A `Button` in default, outline or ghost style; link styling only for URLs, web resources, email |
| Large touch density everywhere | Touch-sized targets on touch screens; medium density with a pointer, compact only where information work benefits |
| A drawn header and alert card on every platform | The system's header and `AlertDialog` on iOS and Android; the page's `header` slot on desktops and web |
| CSS overrides across descendants | The app's components, their parts, and the theme's tokens |

## Command Placement and Overlay Selection

Two rules carry most of the interaction design:

**Prefer command surfaces over hover toolbars.** Keep the primary or frequent action visible as a labeled button; put secondary actions for the current region behind a visible `Menu` trigger; put object-scoped commands in a `ContextMenu`; expose the same important command through a keyboard shortcut and the application menu. A hover-revealed icon may only be a *shortcut* to a command reachable elsewhere. This is more than visual preference — a custom strip of hover buttons rebuilds behavior that `nsh/base` already owns and is invisible to touch, keyboard-only, and many assistive-technology workflows.

**Choose the smallest surface that fits the decision:** tooltip (short explanation or shortcut), popover (contextual controls that do not interrupt), menu (compact list of actions), notification (async status, no decision), dialog (focused decision or short form), alert dialog (explicit confirmation of a consequential action), sheet (supplementary work needing more persistent space). Each takes the form its device expects — `Menu` is a popup with cascading submenus on desktops but a bottom sheet with in-place submenus on phones; `AlertDialog` is the platform's alert or action sheet on mobile.

## Gateways: The Three Checklists

The guides end with three checklists that function as release gates.

**Accessibility checklist** — every action reachable and operable by keyboard, touch and screen reader; focus order follows visual and task order; focus remains visible and is restored after overlays; controls have accessible names; status not communicated by color alone; disabled and read-only distinguishable; content usable with longer translations, right to left and larger text; touch targets at least 44 × 44 points.

**Design review checklist** — eight questions in order: is the task clear; does every action keep its promise; is hierarchy decisive and restrained; could the interface do less, better; is the structure exact; does it follow the component system; does it remain usable in every state and constraint; has it been tested on real platforms.

**Implementation checklist** — state and side-effect ownership explicit; plain function vs component chosen deliberately; stable domain-based keys and test ids; theme tokens and the Tailwind scale replace isolated literals; presses, shortcuts, focus, disabled state and overlays work together; decisions the system needs on the spot are props set beforehand; loading/empty/error/cancellation paths represented; long data sets use `List` with per-item state in data; public API additions only widen; tests prove behavior at the appropriate layer; formatting, Clippy, `nsh check` and targeted tests pass.

## Rules for Coding Agents

Both guides give explicit instructions for agents, and they are unusually concrete. From the design guide: an AI changing an NSH interface should first inspect the nearest feature, the app's components and theme tokens, and the component documentation and declarations (`.nsh/types`); it should state the primary task, state owner, component composition, and keyboard and touch paths before generating code; and it must not infer an API from React, React Native or Shadcn examples or invent an NSH prop or method because the name seems plausible — `nsh check` and the build's class check report what does not exist.

From the coding guide, before editing, an agent must read the nearest implementation, its tests, the module's public exports, and the relevant reference page, and must search the current source and `.nsh/types` for signatures instead of translating a React, React Native, CSS or GPUI example by analogy.

For each change, the agent should be able to name six things: the behavior owner and presentation owner; the retained identity and state lifecycle; the press, keyboard, focus and accessibility contract; the layout and scrolling owner; the theme tokens and intentional exceptions; and the test that would fail if the behavior regressed.

The governing statement is a quality bar, not a process preference:

> Generated code must be reviewed and tested by a person. "Compiles" is not a UI quality bar, and a broad refactor that merely makes generated code look tidy is not a substitute for matching the app's architecture.

## Boundaries of This Source

- Both guides are **normative for NSH**, not general UI doctrine. "Native" here means the platform conventions of iOS, Android, macOS, Linux desktops and the web as NSH models them.
- The guides state that the **Elements and API pages remain authoritative** for individual props and methods, and that current source and the declarations in `.nsh/types` are authoritative for exact signatures. The guides are the rule layer, not the reference layer.
- The design guide's accessibility checklist references a separate accessibility page and a device-and-environment page for text size; those were not part of this ingestion, so the details of Dynamic Type and platform contrast thresholds are not represented here.
- NSH is a young project. The guides describe intent and constraints; they are not evidence that every constraint has been validated against shipped platforms. The design guide's own instruction — "Has it been tested on real platforms?" — applies to NSH's own components as much as to an app's.

## Related Concepts

- [[Entities/native-shell-nsh|Native Shell (NSH)]] — the framework
- [[Concepts/native-shell-architecture|Native Shell Architecture]] — the layered dependency direction
- [[Concepts/native-shell-design-system|Native Shell Design System]] — the visual and interaction rules
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — the Base/app split that both guides rest on
