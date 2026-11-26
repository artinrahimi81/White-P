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
