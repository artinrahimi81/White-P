# Execution-Level Work Breakdown — Part 3

> These work packages decompose existing order, delivery, identity, Reputation, verification and settlement packages. Parent IDs remain stable; parent/child membership is an acceptance roll-up rather than a child-to-parent blocking dependency.

## WP-ORDER-002 — Order draft and immutable customer-input snapshot

### WP-ORDER-010 — Order draft validation and identity binding

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-002
- **Source:** §§6,12,13,23.
- **Objective:** Validate a proposed order against the exact selected provider, service and customer input set.
- **In scope:** Bind customer/provider/service IDs, published task version, validated parameter values, consent, data classification and unique draft ID; define pre-acceptance edit rules.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Order draft validation contract and schema.
- **Acceptance checks:** Missing or unauthorized fields are rejected; draft identity is unique; each input is tied to the immutable task version.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-011 — Accepted input snapshot and tamper-evident audit trail

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-002
- **Source:** §§6,12,13,23.
- **Objective:** Freeze the exact input and disclosure set accepted by the customer.
- **In scope:** Define canonical snapshot, version, timestamp, terms acknowledgement, input hash and audit event; distinguish permitted private data from public references.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Immutable order-input snapshot specification.
- **Acceptance checks:** After acceptance, original input/terms cannot be silently mutated; correction requires a linked version/event; sensitive inputs remain private.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-003 — Contract pricing, currency and terms snapshot

### WP-ORDER-012 — Order price components, currency and fee vocabulary

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-ORDER-003
- **Source:** §§6.3,12.2–12.4,23,31.
- **Objective:** Define the complete price representation before any payment is requested.
- **In scope:** Separate quoted service price, network/native-coin amount, platform/chain fees, taxes if applicable, refund amounts and excluded charges; keep unapproved rates open.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Pricing field dictionary and contract schema.
- **Acceptance checks:** Every monetary value has asset/currency, precision, source and payer; unknown charges are not silently added.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-013 — FX quote provenance, expiry and accepted-terms freeze

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-ORDER-003
- **Source:** §§6.3,12.2–12.4,23,31.
- **Objective:** Specify conversion evidence where a USD-denominated price is converted to native coin.
- **In scope:** Define source identity, quote timestamp, validity window, rounding, slippage and stale quote behavior as owner decisions; freeze accepted quote in the order.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** FX quote contract and decision register.
- **Acceptance checks:** Conversion cannot occur without approved source/expiry rules; price snapshot is immutable after consent; stale quotes require renewed consent.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-004 — In-app payment, confirmation and finality adapter

### WP-ORDER-014 — Payment request construction and order binding

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-004
- **Source:** §12.2,§15,§16.
- **Objective:** Create a payment request bound to one accepted order and exact asset/network.
- **In scope:** Specify destination, amount, order ID, expiry/policy slot, memo/reference, confirmation display and wallet signing handoff.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Payment request/API contract.
- **Acceptance checks:** Payment request cannot be redirected to another order; displayed amount/asset/network matches signed payload.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-015 — Transaction observation, finality and reorganization handling

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-004
- **Source:** §12.2,§15,§16.
- **Objective:** Define how blockchain payment is confirmed before dispatch.
- **In scope:** Track submitted, observed, included, finalized, failed and reorged states; link chain transaction, block and configured finality evidence to the order.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Payment finality state machine and test vectors.
- **Acceptance checks:** Pending/included is not treated as final; reorg/failed states block queue handoff; finality policy remains explicitly configurable/approved.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-005 — External-payment verification queue

### WP-ORDER-016 — External payment evidence submission and validation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-005
- **Source:** §12.3.
- **Objective:** Define what evidence a customer may submit for an off-platform payment.
- **In scope:** Capture payment reference, amount/currency, payer/payee evidence, timestamp and securely uploaded proof; constrain file/metadata validation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** External payment evidence contract.
- **Acceptance checks:** Evidence is attached to exactly one order and cannot be substituted after decision without an audit event; sensitive proof is access-controlled.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-017 — Authorized review, reconciliation and decision audit

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-005
- **Source:** §12.3.
- **Objective:** Specify reviewer authority and evidence-based approval or rejection.
- **In scope:** Define role permission, amount/currency match, duplicate evidence, review outcome, reason, escalation and pending state.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** External-payment review workflow and audit schema.
- **Acceptance checks:** No execution dispatch before authorized approval; approval is not mislabeled blockchain finality; every decision and actor is recorded.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-006 — Order state machine and execution queue handoff

### WP-ORDER-018 — Order lifecycle states and guarded transition table

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-006
- **Source:** §12.4,§13.
- **Objective:** Define a canonical order state model aligned with source-defined statuses.
- **In scope:** Specify Draft, Waiting for Payment, Pending Verification, Queued, In Progress, Completed and Cancelled plus failure/refund extensions only when supported.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Order state model and transition table.
- **Acceptance checks:** Each state has entry/exit guards, owner and allowed transitions; illegal transitions are rejected and all source-defined states are represented.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-019 — Payment gate and exactly-once execution dispatch

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-006
- **Source:** §12.4,§13.
- **Objective:** Define the condition under which an order is eligible for the compute queue.
- **In scope:** Require in-app finality/escrow or authorized external-payment review; design outbox/idempotent dispatch and recovery for uncertain publication.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Execution dispatch contract and outbox model.
- **Acceptance checks:** Only paid/approved orders dispatch; repeated triggers create one queue entry; uncertain delivery is reconciled before retry.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-020 — Execution progress, timeout and terminal outcome handling

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-006
- **Source:** §12.4,§13.
- **Objective:** Define how execution updates the order and reaches completed/failed/cancelled outcomes.
- **In scope:** Map queue acceptance, start, progress, node loss, retry, customer-visible status and handoff to delivery; keep timeout thresholds open.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Execution/order status event specification.
- **Acceptance checks:** Every transition has authoritative producer and timestamp/sequence; timeout is not fabricated; terminal result links to real execution evidence.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-007 — Cancellation, refund and reversal workflow

### WP-ORDER-021 — Cancellation eligibility by order and payment phase

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-007
- **Source:** §12.4,§31.2.
- **Objective:** Define when cancellation may be requested and which authority decides it.
- **In scope:** Separate draft, unpaid, paid-not-started, in-progress, delivered and settled phases; map nonrefundable/partial cases to approval-controlled policy.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Cancellation eligibility matrix.
- **Acceptance checks:** No cancellation silently bypasses financial or execution state; unsupported refund entitlement is left open.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-022 — Refund/reversal calculation, execution and chain limitation handling

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-ORDER-007
- **Source:** §12.4,§31.2.
- **Objective:** Define auditable refund outcomes for supported scenarios.
- **In scope:** Represent full/partial refunds, payment source, fees, escrow, external payment and on-chain irreversible transfer constraints; specify compensation versus reversal.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Refund/reversal contract and scenario vectors.
- **Acceptance checks:** Refunds reference original payment/order and reconcile; irreversible transfers are not described as reversible; unapproved rules block execution.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-008 — Dispute intake, evidence and escalation

### WP-ORDER-023 — Dispute intake, evidence classification and access

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-ORDER-008
- **Source:** §12.4,§13,§22,§31.
- **Objective:** Define customer/provider dispute submissions and evidence permissions.
- **In scope:** Specify reasons, evidence upload/reference, order/delivery version, private-data classification, respondent roles and integrity record.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Dispute intake data contract and UX flow.
- **Acceptance checks:** Only authorized participants see evidence; case is bound to exact order/delivery version; feedback choice is separate from opening a dispute.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-024 — Dispute authority, Frozen guard and response timeline decisions

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-ORDER-008
- **Source:** §12.4,§13,§22,§31.
- **Objective:** Specify decisions required before dispute workflow can move funds or reputation.
- **In scope:** Record response windows, resolver authority, escalation, evidence deadline, Frozen entry/exit and appeal as unresolved decision fields.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Dispute policy decision register and state transition proposal.
- **Acceptance checks:** No resolver, deadline or release authority is invented; active dispute blocks prohibited settlement actions under approved policy.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-ORDER-009 — Order idempotency, retries and financial invariant tests

### WP-ORDER-025 — Order/payment/dispatch idempotency invariant matrix

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-ORDER-009
- **Source:** §§12,13,26,28.
- **Objective:** Enumerate operations that must be safe under duplicate requests and message replay.
- **In scope:** Cover draft acceptance, payment request, webhook, external payment approval, queue dispatch, cancellation, refund and settlement handoff.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Idempotency invariant matrix.
- **Acceptance checks:** Each command/event has key scope and duplicate outcome; no logical order can receive duplicate charge or dispatch.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-ORDER-026 — Fault-injection and reconciliation test cases

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-ORDER-009
- **Source:** §§12,13,26,28.
- **Objective:** Define reproducible failure tests for uncertain payment and order outcomes.
- **In scope:** Test duplicate webhook, lost acknowledgement, retry, timeout, reorg, late confirmation, concurrent cancellation and process restart.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Executable QA test case set and expected outcomes.
- **Acceptance checks:** Every failure case has setup, trigger, expected safe state and observed result; financial totals reconcile after recovery.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-DELIVERY-002 — Upload session, multipart handling and manifest

### WP-DELIVERY-008 — Upload session and authorization binding

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-DELIVERY-002
- **Source:** §21.1.
- **Objective:** Define creation of a secure upload session tied to provider, order and delivery.
- **In scope:** Validate actor, order state, file count/policy slot, destination context and unique upload session ID.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Upload-session API and permission contract.
- **Acceptance checks:** Unauthorized or wrong-order upload is denied; session cannot be rebound to another customer/order.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-DELIVERY-009 — Multipart resume, file manifest and delivery finalization

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-DELIVERY-002
- **Source:** §21.1.
- **Objective:** Specify multi-file and resumable upload completion.
- **In scope:** Define chunk identity, checksum, retry, version, filename, MIME claim, size, upload timestamp and atomic manifest finalization.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Multipart upload state machine and manifest schema.
- **Acceptance checks:** Incomplete/missing chunks cannot finalize; duplicate parts are detected; finalized delivery references immutable file versions.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-DELIVERY-003 — File type, size and content validation

### WP-DELIVERY-010 — File signature, MIME and archive validation rules

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-DELIVERY-003
- **Source:** §21.2,§28.4.
- **Objective:** Define validation of actual uploaded content rather than trusting extension or client headers.
- **In scope:** Check magic bytes, declared MIME consistency, archive nesting, path traversal, symlinks, decompression bounds and unsupported formats.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** File content validation rules and test corpus specification.
- **Acceptance checks:** MIME spoofing/path traversal/bomb cases are rejected or quarantined; resource limits are explicit and approval-controlled.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-DELIVERY-011 — Upload size policy, quarantine and rejection responses

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-DELIVERY-003
- **Source:** §21.2,§28.4.
- **Objective:** Specify safe limits and operator/customer response when an artifact fails validation.
- **In scope:** Keep unknown size limits as policy slots; define quarantine metadata, rejection codes, cleanup and resubmission behavior.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** File policy configuration and quarantine workflow.
- **Acceptance checks:** Invalid content is never released; rejected files retain a safe audit reference; no arbitrary limit is invented.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-DELIVERY-004 — Malware scan, SHA-256 and scan status

### WP-DELIVERY-012 — SHA-256 digest and immutable file manifest

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-DELIVERY-004
- **Source:** §21.1–21.2.
- **Objective:** Define the digest record for each uploaded file and final delivery package.
- **In scope:** Bind file ID/version, byte length, content type, SHA-256, upload session, order and canonical manifest.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** File integrity manifest schema and digest procedure.
- **Acceptance checks:** Digest is recomputable from exact bytes; any file change creates a new version/hash; empty or incomplete file cannot be marked verified.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-DELIVERY-013 — Malware scanning state and release gate

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-DELIVERY-004
- **Source:** §21.1–21.2.
- **Objective:** Specify scanning evidence and how scan outcome affects access.
- **In scope:** Record scanner identity/version, signatures update, scan time, result, quarantine, rescan and unavailable-scanner state.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Malware scan contract and release state machine.
- **Acceptance checks:** Customer download stays blocked until required scan policy passes; scan is not represented as proof of absolute safety; scan failure is visible.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-DELIVERY-005 — Private object storage, encryption and retention

### WP-DELIVERY-014 — Private object-store boundary and encryption/key ownership

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-DELIVERY-005
- **Source:** §21.2,§28.4.
- **Objective:** Define private storage requirements without selecting unapproved provider technology.
- **In scope:** Specify no-public-read/list, encryption at rest, key access boundaries, object naming, metadata minimization and replication.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Private storage security contract.
- **Acceptance checks:** Only authorized application services can access objects; key ownership and storage topology are explicit/open decisions.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-DELIVERY-015 — Retention, deletion, backup and lifecycle policy

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-DELIVERY-005
- **Source:** §21.2,§28.4.
- **Objective:** Specify lifecycle handling for deliverables, temporary chunks and derived copies.
- **In scope:** Map retention trigger, legal hold/dispute, backup expiry, deletion verification, restore and user-facing status; do not invent periods.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Data lifecycle matrix and retention decision record.
- **Acceptance checks:** No unsupported retention duration is assumed; deletion includes replicas/cache where applicable; legal hold prevents prohibited deletion.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-DELIVERY-006 — Per-order authorization and revocable download links

### WP-DELIVERY-016 — Server-side per-order/customer authorization policy

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-DELIVERY-006
- **Source:** §21.3,§28.4.
- **Objective:** Define authorization for every file metadata and byte retrieval path.
- **In scope:** Bind customer ID, order owner, delivery state, file version, expiry, role and dispute/settlement permission.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Per-order access-control matrix and enforcement contract.
- **Acceptance checks:** Changing order/file IDs cannot cross access boundaries; authorization enforced server-side for metadata and content.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-DELIVERY-017 — Revocable download capability and IDOR/expiry tests

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-DELIVERY-006
- **Source:** §21.3,§28.4.
- **Objective:** Specify safe download link or streaming capability lifecycle.
- **In scope:** Define token entropy, scope, expiry, revocation, one-time/reuse behavior, audit and response headers as implementation constraints.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Download capability lifecycle and security test cases.
- **Acceptance checks:** Expired/revoked/wrong-order tokens fail; guessing identifiers cannot reveal objects; URL secrecy alone is not access control.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-DELIVERY-007 — Download audit, notification and review entry

### WP-DELIVERY-018 — Delivery readiness, customer notification and status timeline

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-DELIVERY-007
- **Source:** §21.3–21.4.
- **Objective:** Define when a final deliverable can be announced as ready.
- **In scope:** Require finalized manifest, validation, required scan, private storage and order association; map email/in-app notification event without choosing provider.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Delivery readiness gate and notification contract.
- **Acceptance checks:** No notification before all required gates pass; notifications identify exact delivery version and can be retried without duplication.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-DELIVERY-019 — Download audit and customer review entry

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-DELIVERY-007
- **Source:** §21.3–21.4.
- **Objective:** Define audit history and link from download to customer feedback window.
- **In scope:** Record actor, file version, timestamp, result, access method and notification; keep feedback start/deadline policy open.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Download audit and review-entry specification.
- **Acceptance checks:** All downloads are attributable; missing telemetry is explicit; review period does not start from an unapproved trigger.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-FEEDBACK-002 — Signed customer feedback capture

### WP-FEEDBACK-005 — Feedback authorization, one-response and signature contract

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-FEEDBACK-002
- **Source:** §§13,22,23.6.
- **Objective:** Define exactly who may make a feedback selection and bind it to one order.
- **In scope:** Specify customer identity, order/delivery version, three source choices, timestamp, signature/evidence and duplicate/revision policy.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Feedback command/event schema.
- **Acceptance checks:** Non-customer cannot submit; response targets one immutable delivery version; duplicate/revision behavior follows an explicit policy.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-FEEDBACK-006 — Feedback capture, persistence and audit integration

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-FEEDBACK-002
- **Source:** §§13,22,23.6.
- **Objective:** Specify durable recording and linkage to history and settlement.
- **In scope:** Define validation, persisted event, history visibility, settlement record reference and safe retry handling.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Feedback persistence contract and integration mapping.
- **Acceptance checks:** Feedback is recorded once and linked to the correct settlement record; retry cannot change a submitted choice.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-FEEDBACK-003 — No Feedback timer and pending-policy gate

### WP-FEEDBACK-007 — No Feedback trigger, clock and reminder decision

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-FEEDBACK-003
- **Source:** §§13,22,31.2.
- **Objective:** Define when a no-response period begins and which clock is authoritative.
- **In scope:** Compare delivery-ready, first authorized download and other source-supported triggers; record owner decision, time zone/clock basis and reminder policy.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** No Feedback timing decision record.
- **Acceptance checks:** No trigger or deadline is invented; timer source is deterministic; reminder is not equivalent to feedback.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-FEEDBACK-008 — No Feedback expiry and disposition state machine

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-FEEDBACK-003
- **Source:** §§13,22,31.2.
- **Objective:** Specify what happens after the configured customer-response interval expires.
- **In scope:** Model awaiting response, reminder sent, expired-pending-decision and owner-approved disposition; preserve unresolved financial/reputation outcome.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** No Feedback lifecycle and approval gate.
- **Acceptance checks:** Silence is never converted to Satisfied/Not Satisfied; no reputation or payout effect occurs without approved policy.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-FEEDBACK-004 — Dispute handoff and feedback separation tests

### WP-FEEDBACK-009 — Feedback/dispute semantic truth table

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-FEEDBACK-004
- **Source:** §§22,31.
- **Objective:** Build a complete matrix for customer choices, disputes and no-response outcomes.
- **In scope:** Enumerate Satisfied, Not Satisfied, No Feedback, dispute opened/closed, delivery versions and verification/frozen outcomes.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Feedback and dispute truth table.
- **Acceptance checks:** Not Satisfied alone is not misconduct; No Feedback is neutral/pending; each combination has an explicit allowed consequence or open-decision marker.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-FEEDBACK-010 — Feedback authorization, duplicate and dispute regression suite

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-FEEDBACK-004
- **Source:** §§22,31.
- **Objective:** Specify reproducible test cases for interaction with order, Reputation and settlement.
- **In scope:** Cover forged customer, duplicate submissions, Not Satisfied without dispute, dispute evidence, No Feedback expiry and disputed frozen payout.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Feedback/dispute regression suite.
- **Acceptance checks:** Invalid actors/actions rejected; no implicit negative inference; no payout/reputation transition outside approved policy.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-IDENTITY-002 — Principal, account and cryptographic node identity schema

### WP-IDENTITY-007 — Principal, account, device and node entity schema

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-IDENTITY-002
- **Source:** §§9.3,10,14,17,28.
- **Objective:** Define each identity entity and its relationships without collapsing their meanings.
- **In scope:** Specify account/principal IDs, device identity, node identity, owner relation, public alias, lifecycle and evidence references.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Identity entity schema and field dictionary.
- **Acceptance checks:** Account, device and node are distinct entities; alias never serves as credential or unique authorization proof.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-IDENTITY-008 — Identity proof, binding and privacy classification

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-IDENTITY-002
- **Source:** §§9.3,10,14,17,28.
- **Objective:** Specify how identity bindings are evidenced and which attributes may be disclosed.
- **In scope:** Define proof source/strength, enrollment evidence, owner-to-device binding, rotation history and privacy class; leave identity mechanism open where undecided.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Identity binding contract and privacy matrix.
- **Acceptance checks:** Every binding has evidence and lifecycle; private identity attributes are not published without justification; unsupported verification is not claimed.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-IDENTITY-003 — Role credential and key lifecycle separation

### WP-IDENTITY-009 — Role-to-key purpose and signing authority matrix

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-IDENTITY-003
- **Source:** §§15–18,28.
- **Objective:** Map separate keys/credentials to wallet, node, owner, validator, verifier and infrastructure actions.
- **In scope:** Define signing purpose, authorization scope, cross-role prohibition, rotation and revocation effect.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Cryptographic purpose/authority matrix.
- **Acceptance checks:** No key is implicitly reusable across roles; each signature is attributable to one purpose and authority.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-IDENTITY-010 — Key generation, secure storage, recovery and revocation policy

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-IDENTITY-003
- **Source:** §§15–18,28.
- **Objective:** Specify lifecycle controls while preserving custody as an open decision.
- **In scope:** Record approved key generation source, secure storage boundary, backups, rotation, recovery quorum/authority and compromise response.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Key lifecycle policy and unresolved custody decisions.
- **Acceptance checks:** No storage technology or custody model is silently chosen; compromised key can be revoked and affected permissions enumerated.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-IDENTITY-004 — Authorization matrix and privileged-operation guards

### WP-IDENTITY-011 — Role/resource/action authorization matrix

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-IDENTITY-004
- **Source:** §§9,10,15–19,21,28.
- **Objective:** Define permissions for each principal against network, order, wallet, validator, verifier and file resources.
- **In scope:** Specify allow/deny conditions, resource ownership, tenant boundaries, delegation and privileged actions.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Authorization matrix and policy test cases.
- **Acceptance checks:** Every privileged action has one policy decision; no role receives implicit access by UI visibility or user-provided alias.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-IDENTITY-012 — Server-side enforcement, step-up and denial audit

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-IDENTITY-004
- **Source:** §§9,10,15–19,21,28.
- **Objective:** Specify how permission rules are applied consistently across APIs and client surfaces.
- **In scope:** Define authorization middleware/service, step-up confirmation for sensitive actions, denial codes and audit event handling.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Authorization enforcement design and denial audit schema.
- **Acceptance checks:** Unauthorized calls fail server-side even when UI is bypassed; sensitive actions require approved confirmation; denied attempts are logged without secrets.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-IDENTITY-005 — Identity enrollment, rotation, suspension and revocation

### WP-IDENTITY-013 — Enrollment, credential rotation and suspension state model

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-IDENTITY-005
- **Source:** §§10,18,19,28.
- **Objective:** Define lifecycle states and guards for identities and credentials.
- **In scope:** Map pending, active, rotating, suspended, revoked and recovered states; preserve role-specific approvals.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Identity lifecycle state machine.
- **Acceptance checks:** Invalid transitions rejected; rotation overlap and expiry are explicit; suspension blocks new authority as specified.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-IDENTITY-014 — Revocation propagation and historical signature verification

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-IDENTITY-005
- **Source:** §§10,18,19,28.
- **Objective:** Specify how revoked identities affect future actions and prior evidence.
- **In scope:** Define propagation to nodes/services/committees, cache invalidation, audit retention and validation of signatures made before revocation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Revocation propagation contract and test scenarios.
- **Acceptance checks:** Revoked credentials cannot authorize new events; historical signatures are judged against signing-time validity and preserved evidence.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-IDENTITY-006 — Ownership linkage and Sybil-resistance evidence

### WP-IDENTITY-015 — Ownership-link evidence and conflict-of-interest model

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-IDENTITY-006
- **Source:** §§10,19,28.
- **Objective:** Specify how common ownership and relationships relevant to committee independence are represented.
- **In scope:** Define ownership proof categories, evidence confidence, shared-control relationships, declarations and disclosure restrictions.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Ownership-link/conflict model.
- **Acceptance checks:** Selection rules can consume the approved proof; evidence confidence is visible; no unapproved intrusive identity collection is required.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-IDENTITY-016 — Sybil resistance, privacy and appeals decision package

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-IDENTITY-006
- **Source:** §§10,19,28.
- **Objective:** Evaluate alternative protections against multiple controlled identities and collusion.
- **In scope:** Compare approved candidate mechanisms, privacy impact, evasion limits, operational burden, false positives and appeal path.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Sybil-risk assessment and decision package.
- **Acceptance checks:** No single identity mechanism is asserted as solved without evidence; residual risks and appeal authority remain explicit.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-REPUTATION-002 — Reputation formulas, decimal precision and rounding

### WP-REPUTATION-007 — Popularity and Reputation formula formalization

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-REPUTATION-002
- **Source:** §§20.2–20.7,31.
- **Objective:** Translate source formulas into a typed, deterministic calculation specification.
- **In scope:** Define variables C/P/G/B/D, P bounds 10–70, ten-percentage-point rule, applicability to fee-excluded eligible amount and Good=0 display semantics.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Formal calculation specification and golden vectors.
- **Acceptance checks:** Every source example reproduces; numerator/denominator and percentage points are unambiguous; unsupported cases stay marked open.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-REPUTATION-008 — Precision, rounding, dust and conservation vectors

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-REPUTATION-002
- **Source:** §§20.2–20.7,31.
- **Objective:** Define numeric precision and rounding behavior for all Reputation calculations.
- **In scope:** Specify token decimals, fixed-point representation, rounding mode, minimum unit, remainder ownership, overflow and repeated split effects as decisions where absent.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Precision/rounding spec and golden test vectors.
- **Acceptance checks:** No floating-point drift; inputs and outputs are reproducible; Good+Bad+remaining reconciles under an explicitly approved remainder rule.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-REPUTATION-003 — Popularity snapshot and order-time immutability

### WP-REPUTATION-009 — Popularity eligibility, range and validation gate

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REPUTATION-003
- **Source:** §§20.1–20.5,23.
- **Objective:** Define when provider Popularity Percentage is valid for a new order.
- **In scope:** Validate P in 10–70 inclusive, provider status, source version, timestamp and update authority.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Popularity eligibility rule and validation cases.
- **Acceptance checks:** Values below 10 or above 70 are rejected; range endpoints accepted; missing/stale source does not become a fabricated default.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-REPUTATION-010 — Order-time snapshot, concurrency and historical immutability

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REPUTATION-003
- **Source:** §§20.1–20.5,23.
- **Objective:** Freeze the value used by a particular accepted order.
- **In scope:** Specify version, read consistency, race handling, snapshot timestamp and reference from settlement.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Order-time Popularity snapshot contract.
- **Acceptance checks:** Each order has exactly one stable P; simultaneous edit/order race has deterministic outcome; old orders never recalculate from current provider settings.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-REPUTATION-004 — Good/Bad ledger allocations and reconciliation

### WP-REPUTATION-011 — Reputation allocation ledger entry schema

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REPUTATION-004
- **Source:** §§20.3–20.6,23.
- **Objective:** Define independent Good and Bad records linked to their originating order.
- **In scope:** Specify event type, asset amount, source contract, P snapshot, feedback, order, settlement version and reversal reference.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reputation allocation event schema.
- **Acceptance checks:** Good/Bad entries are distinguishable and traceable to one order/version; no source event can be posted twice.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-REPUTATION-012 — Allocation posting, remainder and reconciliation workflow

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REPUTATION-004
- **Source:** §§20.3–20.6,23.
- **Objective:** Define when calculations are posted and how discrepancies are handled.
- **In scope:** Bind to eligibility and feedback states, approved formulas, lock rules, reversal/appeal and ledger reconciliation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Allocation processor contract and reconciliation vectors.
- **Acceptance checks:** No allocation occurs on unresolved/no-feedback state unless approved; totals conserve eligible amount; correction is append-only.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-REPUTATION-005 — Reputation lock, release and dispute interaction

### WP-REPUTATION-013 — Reputation lock reasons and spendability guards

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-REPUTATION-005
- **Source:** §20.6,§§22–26,31.
- **Objective:** Define why balances become locked and which operations are prohibited.
- **In scope:** Model verification, dispute, review, settlement and any owner-approved lock categories with source event and authority.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reputation lock reason model and access rules.
- **Acceptance checks:** Locked value is excluded from spendable balance; each lock has reason, amount, source and actor.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-REPUTATION-014 — Release, freeze, burn and slash governance controls

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-REPUTATION-005
- **Source:** §20.6,§§22–26,31.
- **Objective:** Separate release from any irreversible burn or slashing operation.
- **In scope:** Define approval roles, evidence, dispute resolution, event linkage, appeal and freeze/unfreeze authority; leave policy values open.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reputation release/burn decision register and control matrix.
- **Acceptance checks:** No automatic burn/slash; irreversible action requires explicit approved authority/evidence; disputed value remains protected.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-REPUTATION-006 — Reputation overview, history and No Feedback display

### WP-REPUTATION-015 — Reputation balance and history information model

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-REPUTATION-006
- **Source:** §§8,20,22.
- **Objective:** Define what data the user needs to inspect Good/Bad reputation.
- **In scope:** Specify balances, ratios, N/A semantics for Good=0, order links, lock reason, pending status and audit history.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reputation view data contract.
- **Acceptance checks:** Every displayed value has unit/source/time; N/A is not rendered as zero; sensitive counterparty data is limited.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-REPUTATION-016 — Role-specific display, no-feedback and dispute messaging

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-REPUTATION-006
- **Source:** §§8,20,22.
- **Objective:** Specify differences among customer/provider/owner views and neutral pending outcomes.
- **In scope:** Map applicable controls and evidence for Satisfied, Not Satisfied, No Feedback, dispute and Frozen states.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reputation UX/state matrix.
- **Acceptance checks:** No-feedback is never labelled positive/negative; users can distinguish pending, disputed, locked and available values.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-RECORD-002 — Canonical settlement schema and field ownership

### WP-SETTLEMENT-RECORD-007 — Section 23 field-by-field schema and data types

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-002
- **Source:** §23.
- **Objective:** Map every source settlement field to a typed canonical representation.
- **In scope:** Cover order, pricing, payment, Reputation, delivery, feedback, both verification stages, reward split, chain and terminal status fields.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Complete settlement field dictionary and schema.
- **Acceptance checks:** Every Section 23 field is included or explicitly justified not applicable; type, unit and nullability are defined.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-RECORD-008 — Field ownership, mutability and privacy classification

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-002
- **Source:** §23.
- **Objective:** Define who may write each field and its authoritative source.
- **In scope:** Record producer, owner, update rule, immutability point, privacy class and on/off-chain boundary for each field.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Field ownership/mutability/privacy matrix.
- **Acceptance checks:** No field has competing sources of truth; private data is classified; post-signature mutation creates a new version.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-RECORD-003 — Canonical serialization, version and SHA-256 hash

### WP-SETTLEMENT-RECORD-009 — Canonical serialization and deterministic encoding

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-003
- **Source:** §§21,23,24.
- **Objective:** Define byte-level canonical representation before hashing or signing.
- **In scope:** Specify field ordering, encoding, numeric representation, Unicode normalization, null/default treatment and excluded transient metadata.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Canonical serialization specification and test vectors.
- **Acceptance checks:** Identical logical record versions yield identical bytes; ambiguous representations are rejected; canonicalization does not omit signed fields.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-RECORD-010 — Record versioning, SHA-256 and mutation invalidation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-003
- **Source:** §§21,23,24.
- **Objective:** Specify how each record version receives an integrity identifier.
- **In scope:** Bind version, previous version reference, canonical byte hash, evidence manifest and signature invalidation rules.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Record version/hash contract.
- **Acceptance checks:** Single-bit changes alter hash; same version gives same hash; changed signed content requires new version and fresh signatures.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-RECORD-004 — Private storage versus on-chain commitment boundary

### WP-SETTLEMENT-RECORD-011 — Data classification and field-level off-chain/on-chain matrix

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-004
- **Source:** §§21,23.5,23.12,28.
- **Objective:** Classify all settlement data based on sensitivity and audit necessity.
- **In scope:** Review customer identity, prompts, input, files, private URLs, payment details, identifiers, hashes and signatures; keep chain contents minimal.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Field-by-field data placement matrix.
- **Acceptance checks:** No personal data, prompt, file or private URL is published; every proposed on-chain field has an explicit necessity rationale.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-RECORD-012 — Public commitment privacy and private reference protection

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-004
- **Source:** §§21,23.5,23.12,28.
- **Objective:** Analyze whether hashes/IDs still leak linkability or permit enumeration.
- **In scope:** Define random identifiers, salt/commitment options, access-controlled lookup and metadata minimization as alternatives, not premature design.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Privacy threat assessment for settlement commitments.
- **Acceptance checks:** Public references cannot enumerate private objects or expose predictable customer/order data; residual linkability is recorded.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-RECORD-005 — Signature envelopes and evidence references

### WP-SETTLEMENT-RECORD-013 — Signature envelope, signer role and signed-object binding

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-005
- **Source:** §§23.7–23.10,24.
- **Objective:** Define exactly what a verifier/validator signs.
- **In scope:** Specify signer identity, key reference, role, committee, record version/hash, evidence digest, decision and protocol context.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Version-bound signature envelope schema.
- **Acceptance checks:** Signature binds to one object/version/context; a signer cannot claim a different role; invalid or ambiguous envelopes fail closed.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-RECORD-014 — Signature verification, key history and algorithm decision gate

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-005
- **Source:** §§23.7–23.10,24.
- **Objective:** Specify verification against historical key validity and approved cryptographic policy.
- **In scope:** Define algorithm policy slot, public-key version, revocation timing, evidence canonicalization and verification outcomes.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Signature verification contract and test vectors.
- **Acceptance checks:** Algorithm must be approved before production use; historical signatures are evaluated against signing-time evidence; unsupported algorithms rejected.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-RECORD-006 — Settlement record lifecycle and transition validator

### WP-SETTLEMENT-RECORD-015 — Settlement status catalogue and transition guards

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-006
- **Source:** §23.11,§§24–26.
- **Objective:** Define source states and legal transition paths for the settlement record.
- **In scope:** Map Created, Payment Locked, Processing, Delivery Uploaded, Awaiting Customer Feedback, both verification stages, Approved, Disputed, Frozen, Settled, Refunded and Closed.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Settlement lifecycle table and guard specification.
- **Acceptance checks:** Every state has owner/entry/exit guard; Frozen blocks payout; mutually exclusive terminal states cannot both occur.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-RECORD-016 — State transition property and regression test matrix

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-SETTLEMENT-RECORD-006
- **Source:** §23.11,§§24–26.
- **Objective:** Define testable invariants for every allowed/forbidden state transition.
- **In scope:** Cover payment, delivery, feedback, both committees, audit completion, dispute, refund, settlement, reopen attempt and event replay.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** State-transition test matrix with golden paths.
- **Acceptance checks:** All invalid transitions fail; accepted transitions preserve event history; terminal record cannot silently reopen.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE1-002 — First-stage evidence package and snapshot

### WP-VERIFY-STAGE1-006 — Stage-one evidence manifest and source binding

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-VERIFY-STAGE1-002
- **Source:** §§23.7,24.1.
- **Objective:** Define the complete evidence bundle presented to first-stage committee members.
- **In scope:** Bind accepted order, price/payment, P/Good/Bad, delivery hashes, feedback, rewards, version, provenance and privacy filters.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage-one evidence manifest schema.
- **Acceptance checks:** Every review field is linked to an immutable source version; missing evidence is explicit; private information is minimized.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE1-007 — Evidence snapshot integrity and committee access package

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-VERIFY-STAGE1-002
- **Source:** §§23.7,24.1.
- **Objective:** Ensure all reviewers receive equivalent evidence without expanding access to private material.
- **In scope:** Define manifest hash/version, access permissions, evidence availability and immutable review snapshot.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage-one reviewer package contract.
- **Acceptance checks:** Reviewers use identical evidence version; access is role-limited; subsequent changes do not rewrite the review snapshot.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE1-003 — Verifier review workflow and decision capture

### WP-VERIFY-STAGE1-008 — Reviewer assignment and evidence inspection journey

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-VERIFY-STAGE1-003
- **Source:** §24.1.
- **Objective:** Specify the complete interaction a selected reviewer follows before voting.
- **In scope:** Define assignment acceptance, evidence navigation, checklist, conflict flag, abstention/inability and timeout states as policy decisions.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reviewer journey and interaction specification.
- **Acceptance checks:** Reviewer can inspect required evidence before decision; assignment is tied to one committee/order/version; missing data prevents valid completion.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE1-009 — Decision capture, rationale and submission confirmation

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-VERIFY-STAGE1-003
- **Source:** §24.1.
- **Objective:** Specify how approve/reject votes and reasons are recorded.
- **In scope:** Define decision vocabulary, evidence references, reason fields, confirmation, withdrawal/correction policy and signature handoff.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Decision capture schema and UX flow.
- **Acceptance checks:** A vote cannot target a different record version; incomplete or duplicate decision is blocked; correction policy remains explicit.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE1-004 — Signed vote validation and duplicate-vote prevention

### WP-VERIFY-STAGE1-010 — Vote envelope and signer eligibility validation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-STAGE1-004
- **Source:** §24.2.
- **Objective:** Define the exact signed object submitted by each first-stage reviewer.
- **In scope:** Bind committee ID, order, record hash/version, vote, evidence reference, signing time and reviewer key.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Vote envelope schema and validation rules.
- **Acceptance checks:** Signature and membership both verified; wrong committee/order/version rejected; replay is detected.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE1-011 — One-vote invariant, duplicates and revocation edge cases

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-STAGE1-004
- **Source:** §24.2.
- **Objective:** Define uniqueness and timing rules for votes.
- **In scope:** Specify one valid vote per member/committee/record version, replacement policy if any, revoked key timing and network retries.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Vote uniqueness/integrity tests.
- **Acceptance checks:** Duplicate submission has idempotent outcome; unauthorized replacement rejected; key revocation is handled by approved signing-time rule.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE1-005 — 80/20 tally, closure and boundary tests

### WP-VERIFY-STAGE1-012 — Valid-vote denominator and 80-percent acceptance calculation

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-VERIFY-STAGE1-005
- **Source:** §24.3–24.4.
- **Objective:** Define exact arithmetic for the 100-member first-stage committee.
- **In scope:** Specify eligible membership snapshot, valid vote definition, absent/invalid vote treatment and exact ratio computation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** 80/20 threshold calculation specification.
- **Acceptance checks:** Exactly 100 valid votes required; 79 approvals fail, 80 pass, 100 pass; non-votes are not silently counted as approvals.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE1-013 — Stage-one closure, boundary/property and replay tests

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-VERIFY-STAGE1-005
- **Source:** §24.3–24.4.
- **Objective:** Specify how the stage becomes closed and how outcomes resist replay.
- **In scope:** Cover quorum, duplicate votes, invalid signatures, vote arriving after closure, concurrent tally and retry after restart.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage-one closure test matrix.
- **Acceptance checks:** Closure is deterministic/idempotent; post-close mutations rejected; all boundary cases have recorded outcomes.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE2-002 — Second-stage audit evidence package

### WP-VERIFY-STAGE2-006 — Audit evidence manifest and stage-one proof inclusion

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-VERIFY-STAGE2-002
- **Source:** §§23.8,25.
- **Objective:** Define the second-stage evidence package required to audit the first stage.
- **In scope:** Include membership proof, randomness, disjointness, signatures, vote counts, thresholds, source formulas and immutable record hash.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage-two audit manifest.
- **Acceptance checks:** Every audit criterion in Section 25 maps to evidence; incomplete stage-one proof is not treated as auditable.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE2-007 — Independent evidence reproduction and discrepancy capture

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-VERIFY-STAGE2-002
- **Source:** §§23.8,25.
- **Objective:** Specify how auditors recompute stage-one outcomes rather than merely trusting a summary.
- **In scope:** Define reproducible calculation inputs, algorithm/version, signature proof and discrepancy classification.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Audit reproduction protocol and discrepancy record.
- **Acceptance checks:** A second-stage reviewer can reproduce the tally and hash from authorized evidence; discrepancies are recorded, not silently reconciled.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE2-003 — Committee disjointness and independence proof

### WP-VERIFY-STAGE2-008 — Committee disjointness and shared-control checks

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-VERIFY-STAGE2-003
- **Source:** §§19.3,25.
- **Objective:** Define the mathematical and identity-level independence check for second committee.
- **In scope:** Compare member IDs, owner links, device/control evidence, prior assignment and declared conflicts against first committee.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Committee independence verification contract.
- **Acceptance checks:** Intersection of members is empty; shared control/conflict checks are evidenced; missing ownership proof is not treated as independence.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE2-009 — Randomness/exclusion evidence and residual collusion risk

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-VERIFY-STAGE2-003
- **Source:** §§19.3,25.
- **Objective:** Specify the evidence needed to audit second committee selection.
- **In scope:** Record randomness source/proof, eligibility snapshot, exclusions, replacements and risk of collusion; keep the random mechanism open until approved.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Committee selection audit report and decision slots.
- **Acceptance checks:** Selection is reproducible from recorded evidence; unapproved randomness is not claimed secure; residual Sybil/collusion risks disclosed.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE2-004 — 90/10 audit tally and vote integrity

### WP-VERIFY-STAGE2-010 — Stage-two 90/10 tally and valid-vote arithmetic

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-VERIFY-STAGE2-004
- **Source:** §25.1.
- **Objective:** Define exact denominator and approval rule for the second-stage committee.
- **In scope:** Specify 100 valid votes, 90% acceptance, invalid/absent/duplicate treatment and evidence validation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** 90/10 threshold calculation specification.
- **Acceptance checks:** 89 approvals fail, 90 pass; missing/invalid votes do not improve threshold; calculations are deterministic.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE2-011 — Stage-two closure, evidence audit and replay tests

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-VERIFY-STAGE2-004
- **Source:** §25.1.
- **Objective:** Specify closure and adversarial conditions around the second-stage decision.
- **In scope:** Test signatures, membership, stale hashes, duplicate votes, late submission, tampered evidence and restart.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage-two integrity test matrix.
- **Acceptance checks:** Tally binds to immutable record/evidence; replay cannot change a closed result; failed audit routes to approved Frozen/re-review policy.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-VERIFY-STAGE2-005 — Frozen state, dispute and re-review handoff

### WP-VERIFY-STAGE2-012 — Frozen settlement guard and authorized transition conditions

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-STAGE2-005
- **Source:** §25.2,§31.3,31.6.
- **Objective:** Define what actions are blocked while settlement is Frozen.
- **In scope:** Specify release/payout/withdrawal restrictions, preserving evidence, allowed administrative actions and resolution ownership.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Frozen state policy and enforcement contract.
- **Acceptance checks:** Frozen prevents prohibited transfer; only authorized evidence-backed decision can leave Frozen; no hidden bypass.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-VERIFY-STAGE2-013 — Re-review creation and new-committee handoff decision

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-STAGE2-005
- **Source:** §25.2,§31.3,31.6.
- **Objective:** Specify how failed/contested audit is escalated to fresh review.
- **In scope:** Record appeal eligibility, new case identity, evidence delta, committee replacement, disjointness and source decision owners.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Re-review workflow and unresolved decision register.
- **Acceptance checks:** A new committee is not selected by an unapproved method; prior results remain immutable; same committee is not silently reused.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-FINAL-002 — Final-settlement eligibility guard

### WP-SETTLEMENT-FINAL-007 — Final eligibility predicate and required evidence

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-002
- **Source:** §26.
- **Objective:** Define a single explicit predicate for settlement readiness.
- **In scope:** Require correct record version, final payment/escrow state, accepted stage-one and stage-two outcomes, no active Frozen/dispute/refund and all required evidence.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Settlement eligibility predicate specification.
- **Acceptance checks:** Every predicate input has authoritative source; missing or unknown condition fails closed; no user-interface-only gate.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-FINAL-008 — Authoritative guard enforcement and race-condition prevention

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-002
- **Source:** §26.
- **Objective:** Specify where and when eligibility is checked immediately before transfer.
- **In scope:** Define transactional compare-and-set/version binding, concurrent dispute/freeze arrival and finality re-check.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Settlement guard enforcement contract and race tests.
- **Acceptance checks:** A dispute/freeze or record-version change between check and payout blocks transfer; race tests demonstrate safe outcome.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-FINAL-003 — Deterministic payout calculation and reconciliation

### WP-SETTLEMENT-FINAL-009 — Payout component formula catalogue and units

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-003
- **Source:** §§8,20,23,26,31.
- **Objective:** Define each payout component separately before applying amounts.
- **In scope:** Map gross price, fee, provider, owner, compute, verifier, validator, treasury, refund, Reputation and remainder to source/asset/precision; keep unknown ratios open.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Payout component schema and formula register.
- **Acceptance checks:** Every component has formula source, unit and eligibility; no unknown percentage is guessed.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-FINAL-010 — Golden-vector reconciliation and rounding policy

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-003
- **Source:** §§8,20,23,26,31.
- **Objective:** Specify exact calculations and conservation checks once approved ratios are supplied.
- **In scope:** Build deterministic cases for zero/maximum/minimum, fees, refunds, multiple recipients, dust/remainder and precision boundaries.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Payout golden vectors and conservation tests.
- **Acceptance checks:** Input equals accounted allocations plus explicitly classified remainder/refund; unsupported ratios prevent payable output.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-FINAL-004 — Idempotent payout execution and transaction journal

### WP-SETTLEMENT-FINAL-011 — Payout command identity, journal and exactly-once semantics

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-004
- **Source:** §26.
- **Objective:** Define durable identity for every payout instruction.
- **In scope:** Specify settlement ID/version, recipient, asset, amount, idempotency key, transaction reference, journal sequence and status.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Payout journal schema and idempotency contract.
- **Acceptance checks:** One logical payout has one durable identity; duplicate command cannot create another transfer.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-FINAL-012 — Partial failure, unknown result and reconciliation recovery

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-004
- **Source:** §26.
- **Objective:** Specify recovery when some recipients pay and others fail or confirmation is unknown.
- **In scope:** Define outbox/inbox, retry, confirmation query, compensation limits and human intervention case.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Payout recovery state machine and failure tests.
- **Acceptance checks:** Unknown broadcast is reconciled before retry; completed recipients are not paid again; compensation never implies reversible chain transfer.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-FINAL-005 — Escrow release and partial-failure recovery

### WP-SETTLEMENT-FINAL-013 — Escrow state and release-order specification

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-005
- **Source:** §§12,13,25,26.
- **Objective:** Define how funds remain locked until all authorized conditions are met.
- **In scope:** Model escrow creation, lock, partial release, refund reservation, release authorization and terminal state.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Escrow lifecycle and release ordering contract.
- **Acceptance checks:** Funds remain unavailable before eligibility; release ordering is deterministic and linked to order/settlement record.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-FINAL-014 — Partial payout recovery and asset-conservation validation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-005
- **Source:** §§12,13,25,26.
- **Objective:** Specify recovery of interrupted distribution while preserving correct totals.
- **In scope:** Model recipient-level outcomes, retryable/nonretryable failure, refund interaction, ledger reconciliation and irreversible transfer handling.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Partial payout recovery procedure and test matrix.
- **Acceptance checks:** No value is lost or duplicated; confirmed transfers remain final; unresolved difference blocks completion.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

## WP-SETTLEMENT-FINAL-006 — Final hash, completion event and reconciliation

### WP-SETTLEMENT-FINAL-015 — Final record commitment and chain receipt verification

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-006
- **Source:** §23.10–23.12,§26.
- **Objective:** Define the evidence needed to close the record after settlement.
- **In scope:** Recompute canonical hash, verify transaction IDs, block height, finality evidence, signatures and referenced versions.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Final settlement verification contract.
- **Acceptance checks:** On-chain commitment matches the canonical final record; all receipts and evidence reference the same settlement version.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.

### WP-SETTLEMENT-FINAL-016 — Terminal completion reconciliation and negative-path suite

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-SETTLEMENT-FINAL-006
- **Source:** §23.10–23.12,§26.
- **Objective:** Verify the system only reaches Settled/Completed when all financial and audit invariants hold.
- **In scope:** Test payout reconciliation, Reputation, fees, reward records, missing receipt, duplicate event, chain reorg, Frozen state and partial failure.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, legal, privacy, custody, cryptographic or governance decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Final settlement acceptance suite.
- **Acceptance checks:** All totals reconcile and finality is evidenced; missing/duplicate/inconsistent event blocks completion; terminal status is idempotent.
- **Verification evidence:** Versioned contract/artifact, source references, normal/negative/boundary cases and reviewable evidence. Any later implementation requires actual reproducible test results, not a plan or declaration.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003. Parent membership is catalog roll-up only; the parent is not a direct predecessor of this child.
