# Overall Vision — Design Engineer

## Purpose
Maintain a coherent, accessible, implementation-ready visual system while preserving approved product intent and documented interface requirements.

## Durable product context
- The authoritative product specification is Production/task-decomposition/main-document.md.
- The initial application platform is Windows and the specified UI language is English.
- The product has user-facing areas for AI Workspace, Explore, Blockchain & Wallet, and Settings. The detailed specification also describes Dashboard and Orders & Deliveries as wider operational views.
- The product includes local model use, creation/joining of distributed networks, defined tasks, service discovery, orders/deliveries, wallet and blockchain-related workflows. Design only what is relevant to an approved task.
- The source contains proposals and open decisions; they remain proposals/open decisions until approved.

## Principles to preserve
1. Keep components, typography, colors, layout hierarchy, and visual states consistent.
2. Design for the documented Windows-first desktop context and supported resizing/scaling.
3. Ensure visual decisions support clarity, accessibility, and predictable operation.
4. Provide implementation-ready specifications, not vague aesthetic opinions.
5. Do not invent screens, features, final branding decisions, or behavior outside approved scope.
6. Keep current implementation separate from proposed design.

## Append-only durable task notes
Append concise task-ID-labelled visual principles, component constraints, approved decisions, and unresolved design questions. Never rewrite prior entries.

## Owner-Directed UI Design Baseline — 2026-11-27
This is the approved design baseline for the application-wide visual language. It operationalizes, but does not replace or rewrite, the read-only product specification in `Production/task-decomposition/main-document.md`, especially Sections 2, 3, 11, 12, 16–19, 21–28 and 32. It applies to every approved product screen, not just the dashboard.

### Five-color rule — the only canonical UI palette

The product UI uses exactly these five canonical colors. Blue is the primary brand and interaction color.

| Token | Exact HEX | RGB | Required use |
|---|---|---|---|
| Primary Blue | `#2563EB` | `37, 99, 235` | Primary actions, selected navigation, links, focus indicators, active controls and key interactive emphasis |
| Deep Navy | `#0F172A` | `15, 23, 42` | Main headings, primary body text, high-emphasis icons and dark text surfaces |
| Slate Gray | `#64748B` | `100, 116, 139` | Secondary text, metadata, subdued icons, outlines and dividers |
| Soft Gray | `#F1F5F9` | `241, 245, 249` | Application canvas, grouped background regions and subtle neutral surfaces |
| White | `#FFFFFF` | `255, 255, 255` | Cards, forms, dialogs, menus and elevated content surfaces |

Rules:
- These five HEX values are the complete canonical palette. Do not introduce a sixth independent hue, arbitrary page-specific color, or unrelated gradient.
- Opacity variants may be derived from one of these five colors for hover, pressed, selected, border or overlay states; they must not introduce another hue.
- Use Primary Blue consistently for the same interaction meaning across the application. Do not use it as decoration where no interaction or hierarchy is intended.
- Use Deep Navy for readable primary text and Slate Gray only where secondary emphasis remains legible.
- Keep body text and controls readable against their actual surfaces. Primary Blue and Deep Navy may be used for text on White/Soft Gray; use White text on Primary Blue for filled primary actions. Do not rely on color alone to communicate state.
- Success, warning, error, pending, disabled and destructive states must also have explicit text, iconography and/or shape treatment. Do not add traffic-light colors outside the five-color palette without a separately approved change to the five-color rule.
- Check contrast for every real text/background pairing during implementation; do not assume that a color is accessible in every pairing merely because it belongs to this palette.

### One application-wide visual system

All pages use the same application shell defined by the product specification:
- Navigation Sidebar for the same global destinations.
- Top Bar for page title, breadcrumbs where useful, internet and blockchain status, wallet balance, notifications, account menu and a Network selector only when multiple networks are active.
- Main Content Area for page-specific content.

Keep shared component appearance consistent: page headers, cards, tables, forms, buttons, input controls, tabs, breadcrumbs, status indicators, alerts, dialogs, empty states, loading states and confirmation surfaces. A component must not acquire a different visual language merely because it belongs to AI Workspace, Explore, Orders & Deliveries or Blockchain & Wallet.

Use a restrained desktop product style: clear hierarchy, generous but efficient spacing, aligned content, readable density and minimal decoration. Use one consistent Windows-friendly sans-serif typography system (Segoe UI/system UI fallback), a 4/8/12/16/24/32 spacing scale, consistent control heights and consistent corner/border treatment. Visual polish must never obscure operational information.

### Responsive layout specification

Responsive behavior is based on the available logical viewport width (effective CSS/device-independent pixels), not the physical monitor resolution or a device-name guess. The same page must reflow when the user resizes, maximizes, restores or snaps the Windows window.

Use these canonical layout ranges:

| Logical viewport width | Layout mode | Required behavior |
|---|---|---|
| `>= 1440 px` | Wide desktop | Expanded 256 px sidebar; flexible multi-column content; up to four summary cards only where each remains readable; wide data views may use available space |
| `1200–1439 px` | Standard desktop | Expanded 256 px sidebar; normally two or three content columns; prevent cards and forms from becoming cramped |
| `1024–1199 px` | Compact desktop | Collapse sidebar to a 72 px icon rail with accessible labels/tooltips; use at most two content columns; simplify noncritical Top Bar items into menus |
| `768–1023 px` | Narrow window | Replace the permanent sidebar/rail with an accessible navigation drawer; use one column by default and two only when each column has sufficient width; wrap or relocate secondary Top Bar items |
| `< 768 px` | Very narrow fallback | Use a single-column content flow and overlay navigation; stack cards and form fields; keep all actions reachable; allow local scrolling for dense tables rather than shrinking text or controls to illegibility |

Additional responsive invariants:
- Treat 800 × 600 logical pixels as the minimum recommended usable window target, not as permission to clip content below that size. Below it, preserve access through scrolling, wrapping and compact navigation; never overlap or silently remove essential controls.
- Support Windows display scaling at 100%, 125%, 150%, 175% and 200%. All dimensions, typography and hit areas must scale with logical units; do not assume physical pixels equal logical pixels.
- Use responsive Grid/Flex layouts and minimum-content constraints. Set shrinkable children to allow shrinking; prevent long IDs, addresses, filenames, model names and transaction hashes from forcing the entire page wider.
- Do not give a page, card, form or dialog a fixed width that prevents it fitting the available content area. Avoid fixed heights for content-bearing regions; allow vertical scrolling.
- The main page must not create accidental horizontal scrolling. When a genuinely wide data table cannot be transformed without losing meaning, confine horizontal scrolling to that table region and keep its key identifier/status columns available.
- At narrow widths, convert dense tables to structured cards or stacked key/value rows when that preserves the information. Never hide financial, security, order or validation facts merely to fit.
- Forms use two columns only when the available width supports clear labels and comfortable controls; otherwise stack fields in one column. Keep primary and destructive actions visible and unambiguous.
- Dialogs and menus must fit within the viewport, use a bounded maximum height, and scroll internally when necessary. They must not open off-screen.
- Charts, network maps and node lists must resize, reflow or provide a local scroll/zoom strategy without hiding their legends or critical status.
- Preserve keyboard focus visibility, readable labels and usable hit targets in every layout mode. Do not solve responsive pressure by reducing text or control sizes below usable limits.

### Responsive design verification matrix

A later implementation must be visually and functionally checked at minimum at:
- 1024 × 768
- 1280 × 720
- 1366 × 768
- 1920 × 1080
- 2560 × 1440
- 3440 × 1440

Repeat representative checks at Windows scaling levels of 100%, 125%, 150% and 200%, including resizing and snapped-window states. Record actual results; this baseline is a specification, not evidence that implementation has already passed.

### Design acceptance rules

A screen is not design-complete unless it:
1. uses the five-color palette and shared component language;
2. fits the relevant responsive modes without clipped or overlapping content;
3. preserves visual hierarchy and readable density;
4. defines default, hover, focus, selected, disabled, loading, empty, success, warning and error appearances where relevant;
5. remains consistent with the source-defined page and workflow; and
6. can be implemented without inventing an unapproved product capability.
