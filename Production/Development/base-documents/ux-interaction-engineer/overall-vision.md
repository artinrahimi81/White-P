# Overall Vision — UX and Interaction Engineer

## Purpose
Keep the application understandable, predictable, efficient, accessible, and recoverable across the user journeys actually defined by the project.

## Durable product context
- The authoritative product specification is Production/task-decomposition/main-document.md.
- The initial release is Windows-first and the UI language is English.
- The documented main areas include AI Workspace, Explore, Blockchain & Wallet, and Settings; Dashboard and Orders & Deliveries provide cross-cutting operational views.
- User journeys include local model use, creating or joining a compute network, defining services/tasks, discovering services, placing and fulfilling orders, receiving results/files, and blockchain/wallet/reputation/verification workflows.
- Some workflows involve asynchronous execution, payments, reviews, verification, disputes, delivery, and settlement states.
- The source contains proposed options and unresolved decisions; do not present them as final behavior.

## Principles to preserve
1. Design interactions around a clear user goal and understandable state transitions.
2. Consider loading, progress, empty, success, error, cancellation, timeout, and recovery states.
3. Keep terminology, navigation, validation, and feedback consistent.
4. Consider keyboard access, focus behavior, readability, and Windows conventions.
5. Reduce unnecessary steps without weakening safety, transparency, or correctness.
6. Do not invent features or claim that a proposed flow already exists.

## Append-only durable task notes
Append concise task-ID-labelled journey constraints, interaction decisions, accessibility lessons, and unresolved usability issues. Never rewrite prior entries.

## WP-INIT-001 — UX and Interaction Engineer durable note

The decomposition preserves journeys from local inference and network participation through service discovery, ordering, delivery, customer feedback, two-stage verification and final settlement. No Feedback is not automatically positive or negative; Not Satisfied alone does not prove misconduct. Windows desktop, English UI, recovery, accessibility and explicit state-transition criteria remain part of downstream acceptance.


## WP-INIT-002 — UX and Interaction Engineer durable note

The task breakdown now separates the application shell, navigation, dashboard, settings, local inference, network participation, Defined Tasks, marketplace, ordering, delivery, feedback, wallet and verification interactions into individually verifiable work packages. Each user-facing child should specify entry conditions, controls, validation, progress/empty/error/cancel states, authorization, recovery and accessibility acceptance. No Feedback and Dispute remain distinct; pending chain payment is not finality.


## WP-INIT-003 — UX durable note
- Execution-level definitions preserve user journeys, explicit states, authorization, error/cancellation/recovery and accessibility acceptance where relevant.
- No Feedback is not positive or negative; Not Satisfied alone is not misconduct; chain confirmation is not finality; Frozen remains payout-blocking under approved policy.

## Owner-Directed Unified UX Baseline — 2026-11-27
This baseline applies across the entire application and follows the read-only product specification, particularly Sections 2–3, 5–13, 16–26 and 28. The UI language remains English and the initial product remains Windows-first. The goal is a simple interface that stays useful for advanced workflows without giving every screen a different interaction model.

### One consistent interaction model

- Keep the same global Navigation Sidebar, Top Bar and Main Content Area on every page. Navigation destinations and their names must remain stable across modules.
- Preserve the source-defined main areas: AI Workspace, Explore, Blockchain & Wallet and Settings. Dashboard and Orders & Deliveries remain cross-cutting operational destinations; they do not replace the four main areas.
- Use a repeatable page structure: page title and optional breadcrumb; a concise context/status summary; the primary content; then secondary details or history. Keep the main action in a predictable location.
- Prefer one clearly identifiable primary action per view. Secondary actions must be visually and spatially subordinate. Destructive or irreversible actions must never look like ordinary navigation.
- Use progressive disclosure: show the information needed for the current decision first, and place advanced settings, technical details and history in clearly named secondary panels or expandable sections.
- Reuse the same interaction patterns for search, filters, pagination, tabs, forms, confirmations, notifications, tables, status badges and detail views. Do not redesign the same kind of control independently in each module.
- Use source terminology consistently: for example, distinguish AI Compute Network from Blockchain Network; distinguish Blockchain Full Node, Blockchain Validator and AI Task Verification Node; distinguish Satisfied, Not Satisfied and No Feedback; and distinguish Pending, Confirmed and Finalized.
- Do not invent new screens, workflows, automatic decisions or product behavior. Where the source leaves a policy or value open, present it as unresolved until the owner approves it.

### Page-level simplicity without loss of capability

- Dashboard should summarize account, AI, orders, recent activity and quick actions; detailed operations remain in their relevant destinations.
- AI Workspace should make the three source-defined paths immediately understandable: Run Model Locally, Create a Network and Join an Existing Network. Defined Tasks, Completed Tasks History and Rewards remain discoverable in the same area.
- Explore should prioritize service discovery, categories, search and filters, then show service details and the source-defined Continue flow.
- Orders & Deliveries should consistently separate My Orders, Incoming Orders, Deliveries and Disputes.
- Blockchain & Wallet should separate overview, wallet actions, transactions, reputation, validator operations, task verification, coin rules and explorer information. Do not collapse distinct financial or verification responsibilities into a generic action.
- Settings should group account, security, wallet security, notifications, privacy, storage and application preferences using stable labels.

### Consistent interaction states and feedback

Every interactive page or component must define the relevant states: initial/loading, ready, empty, in progress, success, warning, recoverable error, blocking error, disabled, cancelled, timed out and retry/resume where applicable. Feedback must say what happened, what the system is doing now and what the user can safely do next.

Use the product's actual state distinctions:
- Network: Active, Inactive, Weak Connection and Unavailable.
- Order: Draft, Awaiting Payment, Payment Pending, Payment Verification, Queued, Running, Completed, Failed, Cancelled, Disputed and Refunded.
- Blockchain transaction: Signed, Broadcast, Pending, Confirmed, Finalized and Failed.
- Settlement: preserve states such as Awaiting Customer Feedback, Awaiting First Verification, Awaiting Second Verification, Approved, Disputed, Frozen, Settled and Refunded.
- Customer feedback: Satisfied, Not Satisfied and No Feedback are three different states. No Feedback must not be silently converted into either positive or negative feedback.
- A pending transaction is not a finalized payment; an uploaded delivery is not the same as an accepted settlement.

Use visible text labels and clear icons alongside visual treatment. Color must never be the only means of communicating state, success, failure, risk or availability.

### Forms, decisions and recovery

- Every input has a persistent label, clear required/optional indication, format guidance when needed and a validation message next to the relevant field.
- Validate at the appropriate time; preserve valid user input after recoverable errors. Do not clear an entire form because one field failed.
- Explain why an action is unavailable and what condition is needed to continue. Do not leave disabled controls without a reason where the reason is not obvious.
- Before wallet transfers, staking, unstaking, key generation/recovery or other consequential actions, present a review step with the exact network, recipient/identity, amount, fee, total and relevant lock/release condition. Require explicit confirmation before signing or committing.
- Prevent accidental duplicate submission for payments, order placement, uploads, votes and settlement-triggering actions. Show an in-progress state and disable duplicate submission until the operation is resolved.
- For recoverable failures, provide a safe retry or resume path and explain whether the previous action was completed, pending or not submitted. Never invite a retry that could create duplicate payment or delivery.
- Explain cancellation consequences and distinguish cancellation from failure, refund and dispute.
- Keep history and audit details available without making routine screens unnecessarily dense.

### Responsive interaction behavior

Apply the canonical breakpoints and layout modes defined in the Design Engineer's overall-vision baseline; do not create a competing set of breakpoint values here.

- At wide sizes, keep navigation expanded and use extra width for useful information, not decoration or unnecessary empty panels.
- At compact desktop widths, allow the navigation rail to collapse while keeping the current destination identifiable.
- At narrow window widths, use a keyboard-accessible navigation drawer; restore the same navigation structure when it closes.
- Reflow content in reading order. Stack independent cards and form fields before reducing legibility. Keep the page title, current task context, primary action and critical status discoverable.
- Tables may become structured cards or use a clearly labelled local horizontal scroll region. Do not make users horizontally scroll the whole application to reach basic actions.
- Dialogs, menus, notifications and confirmation steps must stay within the available viewport and remain operable by keyboard.
- Resizing the window must not reset form data, lose the current workflow step or change the meaning of an action.

### Accessibility and predictable operation

Keep keyboard navigation, logical tab order, visible focus, readable typography, sufficient contrast, descriptive accessible names and understandable error messages. Do not rely on hover alone to reveal essential information. Important actions must be reachable without a mouse. Respect Windows scaling and text enlargement without clipping.

### UX acceptance rules

A workflow is interaction-ready only when its entry point, user goal, required decisions, validation, progress, completion, error, cancellation and recovery behavior are clear; the same control behaves consistently across the application; and narrowing the window does not hide critical information or break the workflow. These are future acceptance requirements, not claims of implemented behavior.
