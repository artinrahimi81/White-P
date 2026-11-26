# Execution-Level Work Breakdown — Part 2

> Each work package below decomposes an existing granular package. Parent IDs are preserved; parent is an acceptance roll-up, not a prerequisite of its own children.

## WP-REWARD-002 — Reward source ledger and event taxonomy

### WP-REWARD-006 — Reward-source event and immutable ledger entry schema

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-REWARD-002
- **Source:** §8,15,23,26,27.
- **Objective:** Define one immutable ledger event format that identifies exactly where a reward or fee originated.
- **In scope:** Specify event type, asset, amount, unit precision, source order/network/block/duty, actor, correlation ID, pending/confirmed/reversed state and evidence reference.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Reward ledger event schema and field dictionary.
- **Acceptance checks:** Every event has a unique id, one source category and verifiable origin; reversals reference the original event instead of deleting it.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-REWARD-007 — Reward-source separation and reconciliation rules

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-REWARD-002
- **Source:** §8,15,23,26,27.
- **Objective:** Prevent accounting streams from being merged or counted twice.
- **In scope:** Specify separate event categories for compute/order-funded rewards, verification fees, validator/block rewards, protocol emissions and transaction fees; define duplicate and reversal handling.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Source taxonomy, reconciliation rules and golden examples.
- **Acceptance checks:** Each source stream reconciles independently; no event is counted twice across ledgers; unknown allocation ratios stay unresolved.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-REWARD-003 — Balance projection and available/locked/pending semantics

### WP-REWARD-008 — Balance projection formulas and consistency snapshots

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REWARD-003
- **Source:** §§8,16,20,23.
- **Objective:** Define deterministic formulas for each displayed balance category.
- **In scope:** Map total, available, locked, pending, approved, withdrawn and unbonding amounts to authoritative ledger events and chain finality.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Balance projection specification and sample vectors.
- **Acceptance checks:** Every category reconciles to source entries; unavailable and pending amounts are not spendable; rounding and asset units are explicit.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-REWARD-009 — Balance authorization, freshness and stale-state handling

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REWARD-003
- **Source:** §§8,16,20,23.
- **Objective:** Specify balance retrieval for account, provider, owner and member views.
- **In scope:** Define ownership filtering, snapshot block/sequence, last-updated marker, stale cache behavior and reconciliation on chain reorg.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Balance query/API contract and role-view matrix.
- **Acceptance checks:** Users see only authorized balances; stale state is identified; reorg or delayed indexer cannot silently promote pending to available.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-REWARD-004 — Network owner/member allocation accounting

### WP-REWARD-010 — Owner/member allocation input and attribution model

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-REWARD-004
- **Source:** §§8.2,9.3,26,27.
- **Objective:** Define how each network-level revenue/reward event is attributed to the owner and participating members.
- **In scope:** Model source amount, allocation base, eligible contribution evidence, owner share, member shares, rounding remainder and unresolved ratio fields.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Allocation input and attribution model.
- **Acceptance checks:** Every share references a source event and eligible participant; no split percentage is invented; remainder is explicitly conserved.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-REWARD-011 — Allocation simulation, statement and reconciliation

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-REWARD-004
- **Source:** §§8.2,9.3,26,27.
- **Objective:** Specify audit views for expected versus distributed allocations.
- **In scope:** Define allocation preview, period statement, participant breakdown, discrepancy reporting and approved formula activation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Allocation statement and reconciliation specification.
- **Acceptance checks:** Simulated values are labelled non-payable until approval; statements reconcile to ledger totals; changes are versioned and auditable.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-REWARD-005 — Withdrawal eligibility and payout reconciliation

### WP-REWARD-012 — Withdrawal eligibility and pre-signing confirmation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REWARD-005
- **Source:** §§8,15,16.
- **Objective:** Define the checks and information shown before a withdrawal is authorized.
- **In scope:** Verify available amount, locked/pending exclusion, minimum/fee policy slots, destination, asset/network and transaction preview.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Withdrawal eligibility contract and confirmation flow.
- **Acceptance checks:** Ineligible funds and unsupported destinations are blocked; user confirms exact amount, fee, destination and network before signing.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-REWARD-013 — Withdrawal execution, idempotency and chain reconciliation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-REWARD-005
- **Source:** §§8,15,16.
- **Objective:** Specify durable execution and recovery for withdrawal requests.
- **In scope:** Define request ID, signing boundary, broadcast state, timeout/unknown outcome, confirmation/finality, replacement and transaction history linkage.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Withdrawal state machine, journal and recovery tests.
- **Acceptance checks:** Repeated requests cannot double-withdraw; unknown broadcast outcome is reconciled before retry; final status is chain-evidenced.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-CREATE-002 — Model partition manifest and executable stage mapping

### WP-NET-CREATE-007 — Partition manifest identity and stage graph schema

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-CREATE-002
- **Source:** §§1.1,9.1.
- **Objective:** Define the canonical manifest representing a model split into ordered pipeline stages.
- **In scope:** Record immutable model revision, partition ID, ordered stages, artifact refs, stage I/O tensor contracts, predecessor/successor and version.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Partition manifest schema and validation rules.
- **Acceptance checks:** Every stage is uniquely identified and ordered; graph is connected and acyclic; exact model revision is pinned.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-CREATE-008 — Stage compatibility and execution-boundary validation

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-CREATE-002
- **Source:** §§1.1,9.1.
- **Objective:** Define checks that prove the manifest can be mapped to eligible nodes.
- **In scope:** Validate per-stage memory/resource minima, runtime/operator compatibility, input/output shape and inter-stage transfer requirements.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage validation report and activation gate.
- **Acceptance checks:** Missing or incompatible stages block network activation; no unstated Tensor Parallelism is assumed; all stage contracts match.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-CREATE-003 — Owner hardware capacity and partition benchmark

### WP-NET-CREATE-009 — Owner hardware profiling and resource measurement

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-NET-CREATE-003
- **Source:** §9.2.
- **Objective:** Specify repeatable profiling of the owner device before partition selection.
- **In scope:** Measure CPU/GPU, memory/VRAM, storage, drivers, runtime and network conditions; identify device-specific capabilities and missing readings.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Owner hardware profile and measurement protocol.
- **Acceptance checks:** Each measurement carries unit, method, timestamp and confidence; unavailable metrics are not guessed.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-CREATE-010 — Partition benchmark and capacity decision report

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-NET-CREATE-003
- **Source:** §9.2.
- **Objective:** Define benchmark execution and how evidence is converted into a capacity decision.
- **In scope:** Run pinned model revision/workload under recorded environment; measure stage memory, compute, transfer and reserve margin; distinguish predicted and measured values.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Partition benchmark report and capacity decision record.
- **Acceptance checks:** Results are reproducible; 20% reserve remains explicitly provisional unless approved; no node assignment exceeds evidenced capacity.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-CREATE-004 — Owner identity, configuration and secrets boundary

### WP-NET-CREATE-011 — Owner principal, permissions and payout identity model

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-NET-CREATE-004
- **Source:** §9.3,§28.
- **Objective:** Separate network-owner identity from machine identity and payout identity.
- **In scope:** Define owner principal, authorized operators, node IDs, payout-address references, transfer of ownership and recovery authority.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Owner authorization and identity contract.
- **Acceptance checks:** A compute node cannot acquire owner privileges by registration; payout keys are not embedded in public node metadata.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-CREATE-012 — Management configuration and secret lifecycle

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-NET-CREATE-004
- **Source:** §9.3,§28.
- **Objective:** Define protection and recovery of network settings, prompts, logs, manifests and secrets.
- **In scope:** Classify each item; specify encryption, access, rotation, backup, export and incident revocation without choosing unapproved custody technology.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Owner management data/secrets policy.
- **Acceptance checks:** Access is least-privilege; secrets never appear in logs or member-visible payloads; restore ownership is verifiable.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-CREATE-005 — Network creation and first-member registration

### WP-NET-CREATE-013 — Network creation validation and transactional initialization

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-CREATE-005
- **Source:** §9.4.
- **Objective:** Specify required checks before a new network is persisted and advertised.
- **In scope:** Validate owner authorization, model licence, model revision, partition manifest, owner capacity, network configuration and unique ID allocation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Network initialization contract and state machine.
- **Acceptance checks:** No partially configured network is advertised as active; failure leaves retryable or safely rolled-back state; ID uniqueness is enforced.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-CREATE-014 — First-node registration and creation recovery

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-CREATE-005
- **Source:** §9.4.
- **Objective:** Define registration of the owner computer as the first eligible network member.
- **In scope:** Bind node identity, stage assignment, health registration and management metadata; handle interruption between network and node persistence.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** First-node registration workflow and recovery tests.
- **Acceptance checks:** A successful network has exactly one valid owner and first node; retries are idempotent; incomplete registration is detectable and recoverable.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-CREATE-006 — Management backup and restore drills

### WP-NET-CREATE-015 — Encrypted management backup package and consistency model

- **Type:** operations.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-CREATE-006
- **Source:** §9.3,§28,§29.
- **Objective:** Specify which management-plane records must be recoverable after owner-device loss.
- **In scope:** Define backup scope, schema version, encryption boundary, integrity manifest, consistency point and secrets handling.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Management backup specification and package format.
- **Acceptance checks:** Backup contains all required control-plane state without exposing secrets; package integrity and compatibility are verifiable.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-CREATE-016 — Restore drill, owner-device replacement and key recovery

- **Type:** operations.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-CREATE-006
- **Source:** §9.3,§28,§29.
- **Objective:** Define controlled restoration on replacement hardware.
- **In scope:** Specify operator authorization, restore validation, node re-enrolment, key rotation, stale-member revocation and post-restore health checks.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Restore runbook and drill acceptance record.
- **Acceptance checks:** A documented drill restores required state; old device credentials can be revoked; restore does not duplicate active owner identities.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-JOIN-002 — Invitation token and network discovery contract

### WP-NET-JOIN-006 — Invitation issuance, scope and expiry contract

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-JOIN-002
- **Source:** §10.1.
- **Objective:** Define an invitation that grants a bounded opportunity to request network admission.
- **In scope:** Specify token entropy/uniqueness, target network, issuer, scope, expiration, use count, revocation and disclosure-safe response.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Invitation token contract and lifecycle.
- **Acceptance checks:** Token cannot grant owner rights or prove node identity; invalid/expired/revoked token is rejected without revealing network secrets.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-JOIN-007 — Network discovery and invitation redemption

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-JOIN-002
- **Source:** §10.1.
- **Objective:** Specify the joiner's discovery flow using an invitation or approved discovery mechanism.
- **In scope:** Define public versus private network metadata, redemption, replay protection and failure handling.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Network discovery/redemption API and UX flow.
- **Acceptance checks:** Unauthorized users cannot enumerate private networks; redemption is auditable and replay-safe.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-JOIN-003 — Join preflight and hardware capability report

### WP-NET-JOIN-008 — Candidate node identity and runtime preflight

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-JOIN-003
- **Source:** §10.2–10.4.
- **Objective:** Define the technical preflight performed before asking an owner to admit a node.
- **In scope:** Check node identity, supported runtime/model revision, hardware probes, drivers, required artifacts and platform compatibility.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Join compatibility report.
- **Acceptance checks:** Every result references actual probes and model/runtime versions; unknown capability is shown as unknown, not supported.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-JOIN-009 — Bandwidth, resource fit and stage suitability report

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-JOIN-003
- **Source:** §10.2–10.4.
- **Objective:** Determine whether the candidate can safely perform a requested stage or backup role.
- **In scope:** Measure network characteristics, memory/compute envelope, availability information and stage-specific requirements.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Stage suitability and resource fit report.
- **Acceptance checks:** The report distinguishes measured from estimated values, explains unsupported stages and is presented before admission.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-JOIN-004 — Resource quota, user limits and admission policy

### WP-NET-JOIN-010 — Resource quota semantics and enforcement points

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-NET-JOIN-004
- **Source:** §10.5,§28.
- **Objective:** Define which resources a member can contribute and which limits are enforceable.
- **In scope:** Specify CPU/GPU, RAM/VRAM, storage, network bandwidth, duty time and pause controls; identify enforcement owner and observed telemetry.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Resource quota schema and policy contract.
- **Acceptance checks:** Every quota has units, scope, owner and enforcement mechanism; unsupported hard limits are labelled advisory.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-JOIN-011 — Admission policy, user consent and limit-change flow

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-NET-JOIN-004
- **Source:** §10.5,§28.
- **Objective:** Specify how resource permissions are granted and changed over time.
- **In scope:** Define consent, owner constraints, member caps, revocation, pause, policy versioning and behavior with active work.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Admission and consent policy/flow.
- **Acceptance checks:** No resource contribution exceeds user-consented caps; limit changes are auditable and take effect at defined safe points.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-JOIN-005 — Owner approval, registration and voluntary exit

### WP-NET-JOIN-012 — Admission decision, node registration and activation transitions

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-JOIN-005
- **Source:** §10.6–10.7.
- **Objective:** Define the complete pending-to-active member admission state machine.
- **In scope:** Cover request, owner review, approve/reject, identity binding, stage assignment, registration and activation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Member admission state machine and API.
- **Acceptance checks:** Only approved and registered nodes become active; duplicate requests and repeated approvals are idempotent.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-JOIN-013 — Voluntary exit, pause and outstanding-work handoff

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-JOIN-005
- **Source:** §10.6–10.7.
- **Objective:** Specify safe member departure without corrupting distributed inference.
- **In scope:** Define stop-accepting-work, current task completion/cancel policy, checkpoint transfer, reward reconciliation and credential revocation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Member exit workflow and acceptance matrix.
- **Acceptance checks:** Exit prevents new assignments, preserves valid work evidence, hands off or safely cancels active work, and revokes access.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-OPS-002 — Node telemetry, heartbeat and last-seen model

### WP-NET-OPS-008 — Node heartbeat payload and telemetry provenance

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-002
- **Source:** §§11.3–11.5.
- **Objective:** Define the minimum periodic node-health message and its trust properties.
- **In scope:** Specify node ID, alias, timestamps/sequence, resources, stages, health, connection metrics, software revision and signature/authentication reference.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Heartbeat/telemetry schema.
- **Acceptance checks:** Node ID is authoritative; alias is display-only; replay/duplicate telemetry is detected and source authenticity is checked.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-OPS-009 — Telemetry freshness, aggregation and privacy filters

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-002
- **Source:** §§11.3–11.5.
- **Objective:** Specify how observations become current network status and operator-visible metrics.
- **In scope:** Define freshness windows as policy parameters, aggregation, missing telemetry, retention hook and exclusion of sensitive host data.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Telemetry ingestion/query contract.
- **Acceptance checks:** Stale/missing measurements are visibly stale/unavailable; only necessary hardware/network metadata is exposed to peers.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-OPS-003 — Connection health and node state transitions

### WP-NET-OPS-010 — Connection state transition model and evidence rules

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-003
- **Source:** §11.4.
- **Objective:** Formalize Active, Inactive, Weak Connection and Unavailable without guessing threshold values.
- **In scope:** Define required observations, transition guards, debounce/flapping controls and manual intervention evidence.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Connection health state machine.
- **Acceptance checks:** Each transition has reason, evidence and time; unknown thresholds remain configurable/approval-gated.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-OPS-011 — Assignment safety under degraded connection states

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-003
- **Source:** §11.4.
- **Objective:** Specify scheduling behavior when a node becomes weak, inactive or unavailable.
- **In scope:** Define admission freeze, in-flight task handling, reassignment eligibility, hysteresis and recovery confirmation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Degraded-node scheduling policy and tests.
- **Acceptance checks:** Degraded nodes do not receive unsafe new work; state flapping does not duplicate assignments or erase active work.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-OPS-004 — Network Test and end-to-end inference probe

### WP-NET-OPS-012 — Network Test probe catalogue and environment capture

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-NET-OPS-004
- **Source:** §11.2.
- **Objective:** Define every diagnostic probe performed by Network Test.
- **In scope:** Cover peer connectivity, throughput, latency, packet loss, runtime availability, stage order, model compatibility and stage coverage.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Network Test case catalogue and environment manifest.
- **Acceptance checks:** Every probe records input, environment, expected result and reproducible evidence; unsupported test is reported not_applicable.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-OPS-013 — End-to-end inference probe, failure isolation and report

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-NET-OPS-004
- **Source:** §11.2.
- **Objective:** Specify a non-billable test inference through the distributed pipeline.
- **In scope:** Define synthetic/test input, stage outputs, timeout, cleanup, node/stage-level diagnostics and report presentation.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** End-to-end Network Test runner/report.
- **Acceptance checks:** Probe is not an order or paid task; failure identifies the stage/node where possible; test data is not retained as customer data.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-OPS-005 — Primary/backup stage coverage and redundancy

### WP-NET-OPS-014 — Primary stage coverage calculation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-005
- **Source:** §11.3,11.5.
- **Objective:** Define the denominator and calculation for primary-stage coverage.
- **In scope:** Map each required stage in the pinned manifest to its primary assigned node and its verified capability/health.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Primary coverage calculator contract.
- **Acceptance checks:** Coverage numerator/denominator are explicit; stage without eligible assignment is uncovered; percent does not imply successful execution.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-OPS-015 — Backup coverage, redundancy and gap reporting

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-005
- **Source:** §11.3,11.5.
- **Objective:** Define backup stage coverage separately from primary placement.
- **In scope:** Map eligible backup candidates, independent failure domains where evidenced and missing backup stages.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Backup coverage model and gap report.
- **Acceptance checks:** Primary and backup coverage are never conflated; duplicate assignment to one node is not counted as independent redundancy.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-OPS-006 — Checkpoint, failover and recovery consistency

### WP-NET-OPS-016 — Checkpoint identity, integrity and resume eligibility

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-006
- **Source:** §11.5,29.
- **Objective:** Define authenticated checkpoint records for in-flight pipeline work.
- **In scope:** Specify job/stage/model version, sequence, input/output hashes, node identity, state version and resume eligibility.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Checkpoint schema and validation contract.
- **Acceptance checks:** Only a checkpoint matching the active job/model/stage version can resume; tampered or stale checkpoints are rejected.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-OPS-017 — Failover orchestration, replay and partial-output consistency

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-NET-OPS-006
- **Source:** §11.5,29.
- **Objective:** Specify reassignment after node loss and safe continuation of work.
- **In scope:** Define retry boundaries, duplicate suppression, stale output rejection, cleanup/compensation and safe full restart fallback.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Failover controller contract and failure scenarios.
- **Acceptance checks:** Replacement uses the latest valid checkpoint or a safe restart; no invalid/duplicate output becomes final; recovery actions are auditable.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-NET-OPS-007 — Operator alerts and network incident timeline

### WP-NET-OPS-018 — Incident severity, alert trigger and ownership rules

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-NET-OPS-007
- **Source:** §11.
- **Objective:** Define how telemetry and workflow failures become operator incidents.
- **In scope:** Specify signal, condition, severity dimensions, responsible operator, deduplication and escalation boundaries.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Incident/alert taxonomy and routing matrix.
- **Acceptance checks:** Each alert has actionable meaning and an owner; repeated signals are correlated rather than spammed.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-NET-OPS-019 — Operator incident timeline, acknowledgement and recovery UX

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-NET-OPS-007
- **Source:** §11.
- **Objective:** Specify the operator flow from alert receipt to resolution.
- **In scope:** Define incident detail, node/stage context, acknowledge/snooze, action links, notes and closure evidence.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Incident UX flow and state matrix.
- **Acceptance checks:** Open, acknowledged, mitigated and resolved states are distinct; all actions are auditable and recovery is visible.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-MARKET-002 — Provider and service registry schema

### WP-MARKET-007 — Provider identity and listing ownership schema

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MARKET-002
- **Source:** §12,§6.
- **Objective:** Define verified ownership and lifecycle metadata for marketplace providers.
- **In scope:** Specify provider/account ID, network/service ownership, eligibility, listing owner, verification status and audit history.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Provider and listing ownership schema.
- **Acceptance checks:** A provider cannot edit another provider's listing; public identifiers do not leak private identity data.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-MARKET-008 — Service listing schema, version and immutable offer snapshot

- **Type:** data-contract.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MARKET-002
- **Source:** §12,§6.
- **Objective:** Define listing fields and the snapshot carried into an order.
- **In scope:** Specify service name/category/specialty, AI type/model, price/currency, ETA, availability, reputation, popularity, version and publication status.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Service registry schema and order snapshot contract.
- **Acceptance checks:** All required display fields are typed and sourced; accepted order records the exact listing/terms version.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-MARKET-003 — Search, categories, filters and stable paging

### WP-MARKET-009 — Search normalization, categories and filter semantics

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MARKET-003
- **Source:** §12.1.
- **Objective:** Specify deterministic matching and filtering over approved listing fields.
- **In scope:** Define searchable text, category/specialty facets, exact/partial matching, invalid query behavior and sort keys.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Search/filter semantics and query contract.
- **Acceptance checks:** Same input and snapshot produce consistent results; private data is not searchable; invalid filters fail explicitly.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-MARKET-010 — Stable pagination, limits and index freshness behavior

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MARKET-003
- **Source:** §12.1.
- **Objective:** Define bounded pagination and search under concurrent listing changes.
- **In scope:** Specify cursor keys, stable ordering, maximum page/query bounds as configurable policy, index update and stale-index indicator.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Search paging and index consistency specification.
- **Acceptance checks:** Results are not duplicated/skipped across a cursor; stale results are labelled; resource bounds prevent unbounded queries.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-MARKET-004 — Service detail and pre-order disclosure

### WP-MARKET-011 — Service detail content and uncertainty disclosure

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-MARKET-004
- **Source:** §12.
- **Objective:** Define all information a customer must understand before starting an order.
- **In scope:** Specify provider, task/model, price/currency, estimated response time, availability, reputation, popularity, limits and payment method labels.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Service detail content specification.
- **Acceptance checks:** Estimate and guarantees are distinguished; missing values labelled; no unapproved ranking or service promises added.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-MARKET-012 — Continue action, input preparation and pre-order confirmation

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-MARKET-004
- **Source:** §12.
- **Objective:** Specify transition from public listing detail to order creation.
- **In scope:** Define required input prompt, parameter validation, price/terms snapshot and customer confirmation before payment.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Pre-order UX flow and validation criteria.
- **Acceptance checks:** Customer sees immutable order terms before payment; validation failures preserve entered values; no payment begins before explicit confirmation.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-MARKET-005 — Availability, ranking freshness and provider status

### WP-MARKET-013 — Availability source, freshness and stale state contract

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MARKET-005
- **Source:** §12.
- **Objective:** Define the source and freshness semantics of provider availability.
- **In scope:** Specify heartbeat/owner status/listing schedule as evidence sources, cache TTL policy slot, refresh and stale/unavailable outcomes.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Availability freshness contract.
- **Acceptance checks:** A stale provider is not presented as currently available; timestamp/source are exposed; unapproved TTL remains open.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-MARKET-014 — Ranking fields, ordering and non-guarantee disclosure

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MARKET-005
- **Source:** §12.
- **Objective:** Separate popularity, reputation, availability and ranking presentation.
- **In scope:** Define fields, version, sorting input references and user-visible caveat; do not approve ranking formula absent owner choice.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Ranking data contract and display rules.
- **Acceptance checks:** Ranking does not imply correctness or quality guarantee; no fabricated popularity/reputation score is produced.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

## WP-MARKET-006 — Listing validation, abuse report and provider moderation

### WP-MARKET-015 — Listing publication validation and provider authorization

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-MARKET-006
- **Source:** §12,§28.
- **Objective:** Define who may publish and which listing checks are required.
- **In scope:** Specify provider ownership, required fields, model licence status, pricing presence, unsupported claims and status transitions.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Listing moderation validation rules.
- **Acceptance checks:** Only authorized provider publishes; missing or ineligible model licence blocks publication; audit reason is retained.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.

### WP-MARKET-016 — Abuse report, investigation, suspension and appeal lifecycle

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-MARKET-006
- **Source:** §12,§28.
- **Objective:** Define the handling of deceptive, unsafe or abusive marketplace listings.
- **In scope:** Specify report intake, evidence confidentiality, triage, temporary restriction, order/fund preservation, appeal and final decision owner.
- **Out of scope:** Sibling work-package outputs; unapproved technical, economic, custody, legal, cryptographic or policy decisions; unrelated refactors; edits to the read-only source.
- **Required output:** Marketplace abuse/moderation workflow.
- **Acceptance checks:** Every decision records evidence and authority; suspension never silently deletes orders or financial records; appeal path remains visible.
- **Verification evidence:** Reviewable artifact/contract, source traceability, negative and boundary cases; later implementation requires reproducible executed checks and recorded outcomes.
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003. Parent membership is represented by the catalog and roll-up rule, not a dependency from child to parent.
