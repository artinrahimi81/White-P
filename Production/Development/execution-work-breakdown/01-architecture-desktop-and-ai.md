# Execution-Level Work Breakdown — Part 1

> This file defines independently verifiable execution-level packages grouped under existing granular work packages. Parent IDs are preserved; the parent package is an acceptance roll-up, not a predecessor of its own children.

## WP-ARCH-002 — System context, actors and operating modes

### WP-ARCH-007 — Actor catalogue and responsibility boundaries

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-002
- **Source:** §§1,2,14,17.
- **Objective:** Define stable actor identities and distinguish human accounts, organizations, machines and protocol roles.
- **In scope:** Enumerate customer, provider, network owner/member, compute node, full node, validator, task verifier and operator; state which are human principals, service identities or protocol identities.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Actor/principal catalogue and ownership map.
- **Acceptance checks:** Every named actor has an unambiguous definition, lifecycle and accountable owner; a human account is not silently treated as a node key.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-008 — Operating-mode capability matrix

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-002
- **Source:** §§1,2,14,17.
- **Objective:** Specify the supported local and distributed operating modes without blending their trust assumptions.
- **In scope:** For local inference, owner-managed network, joined node and blockchain participation, record required services, data flows, offline behavior and capability boundaries.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Operating-mode and capability matrix.
- **Acceptance checks:** Each mode has entry conditions, available capabilities, unavailable features and explicit transitions; blockchain participation is not a prerequisite for local inference.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-ARCH-003 — Subsystem and responsibility decomposition

### WP-ARCH-009 — Subsystem boundary catalogue

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-003
- **Source:** §§1,3,9,11,14–19.
- **Objective:** Define the product subsystems as independently owned capability groups.
- **In scope:** For UI, model catalogue, local runtime, compute control plane, marketplace, order/payment, delivery, wallet, blockchain, verification, Reputation and settlement, define responsibility and authoritative state.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Subsystem boundary catalogue.
- **Acceptance checks:** Every capability has one authoritative subsystem; no subsystem is assigned conflicting ownership of the same state.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-010 — Responsibility and shared-service matrix

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-003
- **Source:** §§1,3,9,11,14–19.
- **Objective:** Resolve cross-cutting ownership for identity, notifications, audit, configuration and storage.
- **In scope:** Map shared services to producers, consumers and operational owners; distinguish shared interfaces from shared database ownership.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Responsibility matrix and shared-service contracts.
- **Acceptance checks:** Every cross-cutting service has a single accountable owner, consumers and failure owner; no direct shared-database dependency is assumed.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-ARCH-004 — End-to-end data and control-flow models

### WP-ARCH-011 — Local inference and Defined Task sequence models

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-004
- **Source:** §§5,9–14,18–27.
- **Objective:** Model local model selection, installation, task authoring and inference as observable workflows.
- **In scope:** Trace model selection through compatibility, verified installation, session creation, prompt assembly, inference, cancellation and history recording.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Sequence diagrams and event list for local AI workflows.
- **Acceptance checks:** Every workflow includes actor, input, output, state owner, validation and at least one failure/cancel path.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-012 — Compute-network formation and recovery flows

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-004
- **Source:** §§5,9–14,18–27.
- **Objective:** Model creation, joining, node scheduling, health checks and failover across the AI compute network.
- **In scope:** Trace owner setup, partition manifest, admission, node registration, stage assignment, heartbeat, checkpoint, failover and recovery.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Network control/data-flow diagrams.
- **Acceptance checks:** Owner and member responsibilities are separate; every transfer has source, destination, authorization and recovery behavior.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-013 — Marketplace order and payment sequence models

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-004
- **Source:** §§5,9–14,18–27.
- **Objective:** Model customer discovery, order creation and payment confirmation as one traceable flow.
- **In scope:** Trace Explore search, provider selection, service snapshot, pricing/FX, in-app or external payment evidence, execution dispatch and cancellation.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Marketplace/order sequence diagrams and event catalogue.
- **Acceptance checks:** Order creation binds the exact listing and terms; payment pending, payment finality and external-payment verification remain distinct.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-014 — Delivery, feedback and two-stage settlement sequence models

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-004
- **Source:** §§5,9–14,18–27.
- **Objective:** Model the complete post-execution process through terminal settlement or refund.
- **In scope:** Trace upload, scan, private download, feedback/no-feedback, dispute, stage-one committee, stage-two audit, Frozen and final payout.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Post-delivery and settlement sequence diagrams.
- **Acceptance checks:** Each transition identifies the authoritative record version, actor, evidence, state mutation and payout-blocking conditions.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-ARCH-005 — Cross-domain interface and event contracts

### WP-ARCH-015 — Service request/response and error contract conventions

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-005
- **Source:** §§6–14,17–27.
- **Objective:** Define common service contract rules for internal APIs and adapters.
- **In scope:** Specify request correlation, typed responses, validation errors, authorization errors, retryable failures, timeout semantics and version compatibility.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** API contract convention and examples.
- **Acceptance checks:** Every interaction defines producer, consumer, schema version, error class and caller action; no untyped success/failure ambiguity.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-016 — Event envelope and compatibility rules

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-005
- **Source:** §§6–14,17–27.
- **Objective:** Define a stable envelope for cross-domain events and event evolution.
- **In scope:** Specify event identity, aggregate identity, order correlation, schema version, occurrence/recording time, producer, payload and compatibility rules.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Event envelope specification and compatibility policy.
- **Acceptance checks:** Duplicate delivery can be detected; old/new schema compatibility is documented; timestamps are not used as the sole ordering authority.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-017 — Idempotency and correlation contract register

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-ARCH-005
- **Source:** §§6–14,17–27.
- **Objective:** Define which commands require idempotency and how one operation is correlated across services.
- **In scope:** Map order, payment, upload finalization, vote, payout, reward claim and chain submission identifiers and their deduplication boundaries.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Idempotency/correlation register.
- **Acceptance checks:** Each retryable command has a stable key scope, uniqueness rule, retention requirement and reconciliation evidence.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-ARCH-006 — Quality attributes, failure model and decision records

### WP-ARCH-018 — Quality-attribute and measurable verification register

- **Type:** architecture.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-ARCH-006
- **Source:** §§1,2,11,14,28,29,31.
- **Objective:** Convert quality attributes into measurable requirements without inventing unsupported numeric targets.
- **In scope:** For latency, throughput, availability, integrity, confidentiality, resource use, recovery, compatibility and observability, define measurement method and pending target owner.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Quality-attribute register and verification methods.
- **Acceptance checks:** Every attribute has a measurement unit/method, affected workflow and target status; unspecified numeric thresholds remain open.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-ARCH-019 — Failure catalogue and architecture decision docket

- **Type:** architecture.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-ARCH-006
- **Source:** §§1,2,11,14,28,29,31.
- **Objective:** Turn documented risks and unresolved choices into controlled decision records.
- **In scope:** Record failure cause, impact, detection, safe state, recovery owner and decision alternatives for central-owner failure, partitions, node loss, data exposure and chain finality.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Failure-mode register and ADR backlog.
- **Acceptance checks:** Each decision has options, trade-offs, evidence needed, owner and approval state; proposals are not labelled approved.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-APP-002 — Window shell, regions and resize behavior

### WP-APP-008 — Window lifecycle and shell constraints

- **Type:** design.
- **Primary owner:** design-engineer
- **Parent work package:** WP-APP-002
- **Source:** §§2,3.1.
- **Objective:** Specify startup, restore, minimize, maximize and close behavior for the Windows desktop shell.
- **In scope:** Define lifecycle transitions, persistent window state, close confirmation where needed, minimum usable dimensions as an approval-controlled value and shell region boundaries.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Window lifecycle and shell constraint specification.
- **Acceptance checks:** All lifecycle states and transitions are defined; no unsupported fixed pixel threshold or mobile layout is introduced.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-APP-009 — Resize, scaling and region reflow rules

- **Type:** design.
- **Primary owner:** design-engineer
- **Parent work package:** WP-APP-002
- **Source:** §§2,3.1.
- **Objective:** Specify how sidebar, top bar, breadcrumb and content behave under resize and Windows scaling.
- **In scope:** Define collapse/expand behavior, overflow, minimum content area, high-DPI handling and focus retention during reflow.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Resize/scaling behavior matrix.
- **Acceptance checks:** All shell regions have deterministic resize behavior; content and controls remain usable at tested desktop scale factors.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-APP-003 — Navigation map, route identity and page access

### WP-APP-010 — Navigation destination registry

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-APP-003
- **Source:** §§3.2–3.4.
- **Objective:** Create one canonical inventory for all required pages and their parent navigation locations.
- **In scope:** Map AI Workspace, Explore, Blockchain & Wallet, Settings, Dashboard and Orders & Deliveries destinations, including subpages named in the source.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Navigation tree and destination registry.
- **Acceptance checks:** Every source-defined page appears exactly once with a stable route identity and parent; no unnamed feature page is added.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-APP-011 — Route access, breadcrumbs and history behavior

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-APP-003
- **Source:** §§3.2–3.4.
- **Objective:** Specify authorization-aware navigation and predictable return paths.
- **In scope:** Define active route, breadcrumb derivation, back/forward behavior, deep-link handling and role/ownership-based visibility without trusting hidden UI alone.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Route/access and breadcrumb contract.
- **Acceptance checks:** Unauthorized routes are rejected server-side; active navigation is deterministic; breadcrumb links never expose records without authorization.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-APP-004 — Shared component catalogue and semantic states

### WP-APP-012 — Shared component contracts and interaction APIs

- **Type:** design.
- **Primary owner:** design-engineer
- **Parent work package:** WP-APP-004
- **Source:** §§3,5,9–13,16,18,19.
- **Objective:** Define reusable form, table, card, status, dialog and notification component contracts.
- **In scope:** For each component, specify inputs, outputs, validation hooks, semantic variants, keyboard behavior and when it should be reused.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Shared component catalogue and component API specification.
- **Acceptance checks:** Each component has a single purpose, typed inputs/state and reuse boundary; domain rules remain outside generic presentation components.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-APP-013 — Semantic visual and operational state catalogue

- **Type:** design.
- **Primary owner:** design-engineer
- **Parent work package:** WP-APP-004
- **Source:** §§3,5,9–13,16,18,19.
- **Objective:** Normalize loading, empty, progress, success, warning, error, disabled, selected and focus states.
- **In scope:** Map shared states to controls and data components; define wording/icon semantics, accessibility announcements and retry/cancel affordances.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Semantic state matrix and examples.
- **Acceptance checks:** Every required state has consistent meaning and accessible feedback; error is not confused with pending or empty.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-APP-005 — Dashboard metrics, freshness and navigation actions

### WP-APP-014 — Dashboard metric source and freshness contracts

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-APP-005
- **Source:** §3.5.
- **Objective:** Bind each dashboard metric to an authoritative source and freshness policy.
- **In scope:** Map balance, locked Reputation, stake, pending rewards, model/network/task counts, health and order activity to owners, units and update times.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Dashboard field dictionary and query contract.
- **Acceptance checks:** Every metric has source, unit, freshness, privacy classification and unavailable behavior; no value is fabricated when source is absent.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-APP-015 — Dashboard action routing and empty/error behavior

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-APP-005
- **Source:** §3.5.
- **Objective:** Specify dashboard quick actions and recovery states.
- **In scope:** Map actions to model run, network creation/join, orders, rewards and settings; define empty state, stale data, loading, permission errors and navigation target.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Dashboard interaction/state specification.
- **Acceptance checks:** Each action has an authorized destination and outcome; stale/failed data is visibly distinguished from zero.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-APP-006 — Settings information architecture and preference persistence

### WP-APP-016 — Settings categories and preference schema

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-APP-006
- **Source:** §3.2.
- **Objective:** Define the settings information architecture and typed preference groups.
- **In scope:** Cover account, security, wallet security, notifications, privacy, storage and application preferences; classify device-local versus account-synced settings.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Settings taxonomy and preference schema.
- **Acceptance checks:** Every source category is represented; each preference has type, default source, sensitivity and persistence owner.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-APP-017 — Settings save, reset and sensitive-change workflow

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-APP-006
- **Source:** §3.2.
- **Objective:** Specify validation and safe persistence for editable settings.
- **In scope:** Define edit, save, cancel, reset, validation errors, concurrency conflict, secret rotation confirmation and failed persistence behavior.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Settings interaction and persistence contract.
- **Acceptance checks:** Unsaved edits are not reported as saved; sensitive changes require explicit confirmation; failed writes retain a clear recoverable state.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-APP-007 — Accessibility, keyboard, contrast and Windows scaling acceptance

### WP-APP-018 — Keyboard and focus behavior specification

- **Type:** design.
- **Primary owner:** design-engineer
- **Parent work package:** WP-APP-007
- **Source:** §§2,3.
- **Objective:** Make critical desktop journeys fully operable without pointer-only actions.
- **In scope:** Specify tab order, focus visibility, escape behavior, modal focus trap/restore and keyboard interaction for navigation, forms, tables and dialogs.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Keyboard/focus acceptance matrix.
- **Acceptance checks:** Every critical action is reachable and operable by keyboard; focus is visible and restored predictably after dialogs.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-APP-019 — Contrast, typography and high-DPI validation matrix

- **Type:** design.
- **Primary owner:** design-engineer
- **Parent work package:** WP-APP-007
- **Source:** §§2,3.
- **Objective:** Define measurable readability checks for Windows desktop use.
- **In scope:** Cover text hierarchy, contrast, scaling, clipping, dense tables, status colors and English label legibility across supported desktop contexts.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Accessibility and Windows display test matrix.
- **Acceptance checks:** No required control or information is lost under tested scaling; contrast/readability checks have explicit pass/fail evidence.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-APP-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-MODEL-002 — Canonical model metadata schema

### WP-MODEL-007 — Model identity, version and provenance schema

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-MODEL-002
- **Source:** §4.
- **Objective:** Define the canonical identity and provenance fields for each exact model artifact.
- **In scope:** Specify model ID, display name, publisher, repository, immutable revision, architecture, parameter count, artifact list and source provenance.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Versioned model identity/provenance schema.
- **Acceptance checks:** Two revisions cannot collide; every field has type and source; unknown metadata is represented as unknown rather than inferred.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-MODEL-008 — Hardware, task, quantization and licence metadata schema

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-MODEL-002
- **Source:** §4.
- **Objective:** Define capability and eligibility metadata used for filtering and preflight.
- **In scope:** Specify model modality/task support, RAM/VRAM requirements, context length, quantization, runtime and licence reference fields.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Model capability metadata schema and validation rules.
- **Acceptance checks:** Every field has a type/unit/allowed value rule; hardware figures identify measured versus publisher-supplied provenance.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-MODEL-003 — Official-source registry and acquisition adapters

### WP-MODEL-009 — Approved origin and immutable revision policy

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MODEL-003
- **Source:** §§2,4.1.
- **Objective:** Define source trust rules for model retrieval.
- **In scope:** Specify permitted repository origins, publisher identity, revision pinning, redirect allowlist and metadata retained for each retrieval.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Approved source registry and revision policy.
- **Acceptance checks:** Only allowlisted origins and pinned revisions are selectable; redirects to unapproved origins fail closed.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-MODEL-010 — Acquisition adapter behavior and failure handling

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MODEL-003
- **Source:** §§2,4.1.
- **Objective:** Specify the download adapter contract and recoverable failure semantics.
- **In scope:** Handle metadata lookup, redirects, rate limits, partial transfers, retries, unavailable files and source changes.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Acquisition adapter contract and failure matrix.
- **Acceptance checks:** Every artifact is tied to source/revision; retry cannot silently switch model revision; failures remain auditable.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-MODEL-004 — Model-file integrity and authenticity verification

### WP-MODEL-011 — Streaming artifact digest and signature verification

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MODEL-004
- **Source:** §§4.1,5.
- **Objective:** Define artifact authenticity checks before model activation.
- **In scope:** Specify digest calculation, trusted digest source, signature/key evidence, streaming verification and exact artifact identity.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Artifact verification contract and digest procedure.
- **Acceptance checks:** A mismatched or unverifiable artifact is quarantined and cannot be loaded; recorded digest is bound to the exact revision.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-MODEL-012 — Manifest consistency, interrupted downloads and quarantine

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MODEL-004
- **Source:** §§4.1,5.
- **Objective:** Define integrity behavior across multi-file models and partial transfers.
- **In scope:** Verify manifest/file set consistency, resume boundaries, atomic promotion and quarantine/cleanup after failures.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Model artifact manifest validation and recovery rules.
- **Acceptance checks:** Truncated/missing/extra files block activation; resumed download is reverified; verified cache is never overwritten by an unverified partial.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-MODEL-005 — Version-specific licence assessment and eligibility gates

### WP-MODEL-013 — Exact-version licence evidence register

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-MODEL-005
- **Source:** §§2,4.1,31.1.
- **Objective:** Assess licence terms for each exact model revision and its artifacts.
- **In scope:** Record weights/code licences, source URL, version, date, reviewer, attribution and redistribution terms with documentary evidence.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Version-specific licence assessment record.
- **Acceptance checks:** Every eligibility decision cites exact licence evidence and review date; unknown licence status blocks the affected use.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-MODEL-014 — Usage-context eligibility and distribution restrictions

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-MODEL-005
- **Source:** §§2,4.1,31.1.
- **Objective:** Translate the evidence into local, commercial and distributed-use gates.
- **In scope:** Assess local inference, commercial service, redistribution, transfer to compute nodes, caching and user downloads separately.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Model-use eligibility matrix.
- **Acceptance checks:** Local/distributed/commercial permissions are not conflated; no family-wide licence assumption; uncertain cases remain blocked for review.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-MODEL-006 — Model-runtime compatibility and quantization matrix

### WP-MODEL-015 — Runtime, format and hardware compatibility grid

- **Type:** specification.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MODEL-006
- **Source:** §§4,5,9.
- **Objective:** Map exact model revisions to candidate execution environments without choosing an unapproved runtime.
- **In scope:** Record file format, quantization, runtime version, CPU/GPU features, RAM/VRAM and platform limitations.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Versioned model/runtime compatibility matrix.
- **Acceptance checks:** Every supported combination has cited test or vendor evidence; unsupported combinations have a specific reason.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-MODEL-016 — Preflight rejection and compatibility evidence

- **Type:** specification.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MODEL-006
- **Source:** §§4,5,9.
- **Objective:** Define deterministic preflight outcomes and diagnostic evidence.
- **In scope:** Specify missing capability, insufficient memory, unsupported operation, driver/runtime mismatch and stale compatibility data outcomes.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Preflight rules and diagnostic contract.
- **Acceptance checks:** The same versioned inputs produce the same decision; unsupported combinations fail before load and show actionable reasons.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-LOCAL-002 — Windows hardware and runtime inventory

### WP-AI-LOCAL-007 — Windows hardware capability probes

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-002
- **Source:** §5.1.
- **Objective:** Specify reliable collection of CPU, GPU, RAM, VRAM, storage, driver and runtime data.
- **In scope:** Define supported system APIs, permission handling, missing sensors and distinction between detected and inferred capabilities.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Hardware inventory service contract.
- **Acceptance checks:** Each measurement records value, unit, collection method, time and confidence; inaccessible values are explicitly unavailable.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-008 — Normalized hardware snapshot and provenance

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-002
- **Source:** §5.1.
- **Objective:** Normalize heterogeneous hardware reports for compatibility decisions.
- **In scope:** Define canonical units, device identity, multi-GPU representation, driver/runtime versions and snapshot invalidation.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Normalized hardware capability snapshot schema.
- **Acceptance checks:** Equivalent devices normalize consistently; every value is traceable to a probe; no missing capacity is fabricated.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-LOCAL-003 — Compatibility thresholds and benchmark calibration

### WP-AI-LOCAL-009 — Compatibility decision thresholds and safety margin policy

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-AI-LOCAL-003
- **Source:** §§5.1,5.2.
- **Objective:** Formalize deterministic compatible, warning and incompatible outcomes.
- **In scope:** Specify how model requirements, measured capacity and provisional 20% headroom are compared; keep threshold ownership and approval explicit.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Compatibility decision table and parameter register.
- **Acceptance checks:** Every result is reproducible from versioned inputs; provisional margins remain labelled until calibrated; no hidden threshold is assumed.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-010 — Benchmark calibration protocol for local inference

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-AI-LOCAL-003
- **Source:** §§5.1,5.2.
- **Objective:** Define repeatable tests to calibrate memory/performance assumptions.
- **In scope:** Specify model revision, quantization, prompt/workload, warm-up, repetitions, device/driver and metrics to collect.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Benchmark protocol and calibration evidence template.
- **Acceptance checks:** Results can be reproduced and compared only under equivalent conditions; predicted and measured values are separated.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-LOCAL-004 — Model download, install and verified cache lifecycle

### WP-AI-LOCAL-011 — Model transfer progress, resume and cancellation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-004
- **Source:** §§4.1,5.3.
- **Objective:** Specify reliable download behavior for large model artifacts.
- **In scope:** Define progress stages, resumable chunks, cancellation, timeout, retry and disk-space preflight.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Download transfer state machine and UI/API contract.
- **Acceptance checks:** Interrupted transfers resume only against the same immutable artifact; cancellation leaves no loadable partial file.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-012 — Verified installation and atomic cache activation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-004
- **Source:** §§4.1,5.3.
- **Objective:** Define the transition from downloaded artifact to available model cache.
- **In scope:** Bind verification results to cache metadata, activation, version isolation, rollback and concurrent installer behavior.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Install/activation transaction and cache manifest.
- **Acceptance checks:** Only verified artifacts become active; partial activation is impossible; concurrent install cannot corrupt a verified model.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-013 — Cache quota, cleanup and retention behavior

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-004
- **Source:** §§4.1,5.3.
- **Objective:** Specify cleanup of temporary, obsolete and failed model artifacts.
- **In scope:** Define reference tracking, safe eviction, user-visible storage use, retry after cleanup and protection of in-use models.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Cache cleanup/retention policy and tests.
- **Acceptance checks:** In-use or pinned versions are not evicted; cleanup is auditable and does not delete active session data.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-LOCAL-005 — Inference runtime adapter and model load/unload lifecycle

### WP-AI-LOCAL-014 — Inference runtime adapter contract

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-005
- **Source:** §5.3.
- **Objective:** Define a stable adapter boundary between application services and the selected model runtime.
- **In scope:** Specify model open/run/stream/stop/close operations, typed inputs/outputs, runtime capabilities and error mapping.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Runtime adapter interface contract.
- **Acceptance checks:** Application services are not coupled to provider-specific runtime internals; unsupported features are explicit.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-015 — Model load/unload and memory reservation lifecycle

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-005
- **Source:** §5.3.
- **Objective:** Specify memory reservation and safe lifecycle transitions.
- **In scope:** Define unloaded/loading/ready/running/unloading/failed states, concurrent access, cleanup and resource release.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Runtime lifecycle state machine.
- **Acceptance checks:** Every state transition is guarded; failure releases reserved resources; model version is pinned to a session.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-016 — Runtime isolation and failure containment

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-005
- **Source:** §5.3.
- **Objective:** Define process/resource isolation and failure reporting for local inference.
- **In scope:** Specify permissions, filesystem/network access, resource limits, crash containment and diagnostic redaction.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Runtime isolation and error-handling specification.
- **Acceptance checks:** A runtime failure cannot corrupt unrelated application state or expose secrets; errors are actionable without sensitive payloads.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-LOCAL-006 — Local conversation sessions, context and cancellation

### WP-AI-LOCAL-017 — Session identity, context window and message ordering

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-006
- **Source:** §§5,6.
- **Objective:** Define local conversation session persistence and context management.
- **In scope:** Specify session IDs, ordered messages, context truncation/overflow behavior, model binding and concurrent session isolation.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Conversation/session data contract.
- **Acceptance checks:** Messages remain ordered and bound to the correct model/session; context overflow is explicit; sessions cannot read each other's content.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-LOCAL-018 — Cancellation, retry and response presentation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-LOCAL-006
- **Source:** §§5,6.
- **Objective:** Specify user controls and response behavior during inference.
- **In scope:** Define stop token/cancel acknowledgement, retry semantics, partial outputs, formatting and completion/error notifications.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Inference interaction contract and scenario tests.
- **Acceptance checks:** Cancellation stops or reports inability to stop; retries do not duplicate a session turn; partial output is never shown as final.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-TASK-002 — Defined Task entity, version and publication lifecycle

### WP-AI-TASK-006 — Defined Task identity, owner and immutable version schema

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-TASK-002
- **Source:** §6.
- **Objective:** Define fields and ownership for each reusable service/task definition.
- **In scope:** Specify stable task ID, owner/provider, version, title, input schema reference, prompt template, price/terms reference and lifecycle state.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Defined Task entity/version schema.
- **Acceptance checks:** Each accepted order references one immutable version; field owners and mutation rules are explicit.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-TASK-007 — Publication, pause, retire and historical-version behavior

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-TASK-002
- **Source:** §6.
- **Objective:** Specify the publication lifecycle and effects on existing orders.
- **In scope:** Define validation before publish, pause/new-order blocking, retirement, version replacement and historical access.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Task publication state machine.
- **Acceptance checks:** Publishing invalid data is rejected; changing a live definition creates a new version; existing orders remain bound to their accepted version.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-TASK-003 — Input parameter editor and field validation

### WP-AI-TASK-008 — Parameter field type, bounds and required validation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-TASK-003
- **Source:** §6.1.
- **Objective:** Define validation rules for each supported input parameter type.
- **In scope:** Cover long-form text, single-choice fields, required/optional flags, maximum 100 fields and invalid/empty input behavior.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Parameter validation contract and boundary test cases.
- **Acceptance checks:** 0/1/100/101 field boundaries and invalid types behave deterministically; required fields cannot be omitted.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-TASK-009 — Choice options, labels and keyword uniqueness

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-TASK-003
- **Source:** §6.1.
- **Objective:** Specify the rules for choice options and prompt-reference keywords.
- **In scope:** Enforce four choices per single-choice field, unique keyword identity and the 32-character keyword limit; define rename/delete validation.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Choice/keyword validation rules and editor acceptance.
- **Acceptance checks:** Missing/duplicate/overlong keywords and invalid option counts block publication; existing published versions remain unchanged.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-TASK-004 — Prompt-template parser and keyword reference integrity

### WP-AI-TASK-010 — Prompt template grammar and keyword tokenization

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-TASK-004
- **Source:** §6.2.
- **Objective:** Define the grammar for /keyword references and how templates are parsed.
- **In scope:** Specify token boundaries, whitespace/escape rules, duplicate use and autocomplete insertion behavior.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Prompt-template grammar and parser contract.
- **Acceptance checks:** Valid tokens resolve deterministically; malformed tokens are identified without silently rewriting provider text.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-TASK-011 — Reference integrity and published prompt snapshot

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-TASK-004
- **Source:** §6.2.
- **Objective:** Ensure all prompt references resolve to exact parameter definitions and versions.
- **In scope:** Define unknown/deleted/renamed reference handling, publish-time validation and immutable snapshot used by orders.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Prompt reference validator and immutable prompt snapshot format.
- **Acceptance checks:** Unknown or ambiguous references block publishing; accepted orders preserve the exact published template and parameter mapping.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-TASK-005 — Customer input validation and trusted/untrusted prompt assembly

### WP-AI-TASK-012 — Trusted/untrusted prompt assembly boundary

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-AI-TASK-005
- **Source:** §6.2,§28.
- **Objective:** Define how system instructions, provider templates and customer values are assembled safely.
- **In scope:** Specify structured message separation, variable substitution, untrusted content labels and instruction precedence.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Prompt assembly security contract.
- **Acceptance checks:** Customer-supplied values remain data and cannot override system instructions through string concatenation.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-TASK-013 — Input limits, redaction and safe display rules

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-AI-TASK-005
- **Source:** §6.2,§28.
- **Objective:** Specify bounds, logging minimization and rendering of user-provided task values.
- **In scope:** Define maximum accepted payloads from approved policy slots, safe encoding, sensitive-field redaction and safe preview behavior.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Input handling and logging/privacy rules.
- **Acceptance checks:** Raw customer text is not executed as markup/code; sensitive values are not logged unnecessarily; unspecified limits remain open.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-HISTORY-002 — Execution and order event schema

### WP-AI-HISTORY-005 — Execution and order event field taxonomy

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-AI-HISTORY-002
- **Source:** §7.
- **Objective:** Define distinct typed event fields for local runs and paid orders.
- **In scope:** Specify task/order IDs, model/task version, start/end timestamps, status, result reference, payment and reward references.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** History event schema and field dictionary.
- **Acceptance checks:** Every displayed history field maps to a typed source event; local executions do not fabricate network-node participants.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-HISTORY-006 — Event chronology and source-record linkage

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-AI-HISTORY-002
- **Source:** §7.
- **Objective:** Define how history records preserve ordering and provenance.
- **In scope:** Specify event sequence, producer identity, correction/reversal linkage and references to authoritative order, payment, delivery and settlement records.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** History chronology and provenance contract.
- **Acceptance checks:** Corrections are appended or referenced rather than silently mutating history; each event is traceable to its producer and source record.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-HISTORY-003 — History persistence, indexing and authorized retrieval

### WP-AI-HISTORY-007 — Ownership-scoped history persistence and indexing

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-HISTORY-003
- **Source:** §§7,21,23.
- **Objective:** Define storage ownership and indexes for execution and order history.
- **In scope:** Specify transaction boundaries, user/customer/provider scope, order correlation and indexes supporting source-defined filters.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** History persistence schema and index plan.
- **Acceptance checks:** A user can retrieve only authorized records; record creation and related order events commit consistently; duplicate event ingestion is detected.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-HISTORY-008 — Stable pagination, filters and retention hooks

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-AI-HISTORY-003
- **Source:** §§7,21,23.
- **Objective:** Specify reliable history queries and future retention-policy integration.
- **In scope:** Define stable sort keys, cursor pagination, status/date filters and configurable retention hooks without choosing a retention period.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** History query API and retention integration contract.
- **Acceptance checks:** Pages do not duplicate/skip entries under concurrent writes; retention behavior is policy-driven and no period is invented.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

## WP-AI-HISTORY-004 — History detail views and evidence cross-links

### WP-AI-HISTORY-009 — History evidence cross-link model

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-AI-HISTORY-004
- **Source:** §§3,7,11,23.
- **Objective:** Define links from one history entry to related node, payment, delivery, reward and settlement evidence.
- **In scope:** Specify relation types, authorized lookup, missing-reference behavior and data provenance.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** History evidence relationship schema.
- **Acceptance checks:** Every link resolves to an authoritative record or explicit unavailable state; no raw private storage URL is exposed.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.

### WP-AI-HISTORY-010 — Role-specific history detail presentation

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-AI-HISTORY-004
- **Source:** §§3,7,11,23.
- **Objective:** Specify how local, owner, member, customer and provider views differ.
- **In scope:** Define applicable fields, privacy redaction, labels for inapplicable network/financial data and navigation to related detail pages.
- **Out of scope:** Other outputs assigned to sibling work packages; unapproved product, runtime, legal, custody, cryptographic or economic decisions; unrelated refactors; changes to the read-only source.
- **Required output:** History detail interaction specification.
- **Acceptance checks:** Only role-authorized fields appear; unavailable fields are explained; local history does not display fictitious participant data.
- **Verification evidence:** A reviewable contract/artifact and traceable source references; where implementation is later authorized, reproducible tests and observed results are required. A plan is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003. The parent ID is a grouping/roll-up relation, not a prerequisite for its own decomposed children.
