# Expanded Task Catalog — White-P

## Purpose and authority

This catalog defines the detailed work breakdown for the Windows-first distributed AI and blockchain product. The authoritative product source remains read-only at Production/task-decomposition/main-document.md. dependency-graph.json is the sole authority for task IDs, direct prerequisites and statuses.

## Expansion history and continuity

- WP-INIT-001 remains completed and unchanged.
- WP-INIT-002 is the follow-up that deepens the first decomposition.
- The 27 original domain IDs ending in -001 remain immutable. Their role is now the domain-baseline/specification gate; implementation, verification, security and operations are represented by child tasks.
- New tasks continue the WP-DOMAIN-NNN namespace with unused sequence numbers. No ID is reused or renamed.
- This is a plan only. All domain and child tasks remain not_started; defining them does not claim implementation.

## Identifier convention

- WP = White-P work package; DOMAIN = stable uppercase functional domain; NNN = three-digit local sequence.
- IDs denote identity only, not order, priority, owner or status.
- A split/merge/scope change receives a new ID and traceability update.

## WP-INIT-001 — Decompose the approved product specification into executable tasks

- **Historical result:** completed on the previous run; status remains done and its original history is preserved.
- **Source:** Production/task-decomposition/main-document.md, introductory material and Sections 1–32.
- **Accepted output:** Initial catalog, valid 28-node graph and source-to-task traceability.
- **Boundary:** This follow-up does not reopen WP-INIT-001 or overwrite its status/logs.

## WP-INIT-002 — Deepen the decomposition into implementation-ready work packages

- **Objective:** Expand the first decomposition into a fine-grained, independently schedulable work breakdown while preserving all original IDs and WP-INIT-001 history.
- **Source:** Production/task-decomposition/main-document.md (all sections/subsections/flows/fields/states), current catalog/graph, status template, all role prompts, five baselines, WP-INIT-001 status and ten histories.
- **Scope:** Re-evaluate online state; deepen all 27 domains; convert existing -001 tasks into specification/contract gates; add granular implementation, verification, security, operations and acceptance tasks; define single-owner objectives, scope, exclusions, outputs, testable criteria, evidence and prerequisites; validate catalog/graph/path integrity; create this task status and ten histories; append selected-role baseline reports/notes.
- **Exclusions:** Reopening WP-INIT-001; modifying source; product implementation; mocks/stubs/placeholders; resolving unapproved technical/legal/custody/economic/cryptographic decisions; creating future task workspaces.
- **Required outputs:** Expanded catalog; exact three-key graph; preserved original IDs; new WP-DOMAIN-NNN child tasks; workstream mapping; owner/type/source/acceptance per child; updated traceability/open decisions; status and ten histories; append-only role reports/notes.
- **Acceptance:** All 27 domains have a baseline gate and at least three concrete child tasks; each child has one verifiable outcome; catalog/graph ID sets match; every graph node has only id/depends_on/status; no invalid refs, self/duplicate edges or cycles; statuses valid; source sections mapped; owner/output/acceptance defined; no unapproved choice becomes an approval; no app code or out-of-scope path changes.
- **Identifier rule:** Original WP-DOMAIN-001 IDs remain immutable as domain baseline tasks. Children continue same namespace with unused sequence numbers.
- **Dependency rule:** A domain baseline produces the domain contract/specification and is a real prerequisite for its implementation children. Child-to-child edge only when an output is consumed; preferred order alone is not a dependency.
- **Initial state:** not_started; planning/decomposition only.


## Domain baseline/specification tasks

## WP-ARCH-001 — Product architecture boundaries and shared contracts

- **Type:** Domain baseline / specification gate.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§1,2,14,17,29,32.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Architecture context, actor/component map, domain boundaries, cross-system contracts, quality attributes and open-decision register.
- **Acceptance:** All subsystems and roles are mapped; local/distributed compute and blockchain boundaries are explicit; Pipeline Parallelism differs from Tensor Parallelism; cross-domain interfaces have owners and versioned contracts; unresolved choices are not approved by implication.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-ARCH-002, WP-ARCH-003, WP-ARCH-004, WP-ARCH-005, WP-ARCH-006.

## WP-APP-001 — Windows desktop shell, navigation and dashboard

- **Type:** Domain baseline / specification gate.
- **Primary owner:** design-engineer.
- **Source:** §§2,3.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Screen inventory, navigation map, app-shell specification, shared UI conventions, dashboard data contract, settings information architecture and accessibility/resizing requirements.
- **Acceptance:** Every source-defined navigation item and global view is covered; Windows-first and English UI constraints are testable; dashboard data has sources; UI states and keyboard/scaling behavior are documented.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-APP-002, WP-APP-003, WP-APP-004, WP-APP-005, WP-APP-006, WP-APP-007.

## WP-MODEL-001 — Model catalogue, provenance and licence compliance

- **Type:** Domain baseline / specification gate.
- **Primary owner:** feasibility-engineer.
- **Source:** §§2,4,5,9.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Versioned model metadata schema, approved-source policy, provenance/integrity contract, per-version licence review and deployment-eligibility matrix.
- **Acceptance:** Catalogue fields are covered; exact versions/sources are traceable; integrity and licence reviews are separate; local/distributed eligibility differ; restricted or unknown models are not silently approved.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-MODEL-002, WP-MODEL-003, WP-MODEL-004, WP-MODEL-005, WP-MODEL-006.

## WP-AI-LOCAL-001 — Local model compatibility, installation and inference

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§2,5,29.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Local execution architecture, hardware inventory, compatibility rules, installation/runtime lifecycle, session behavior, local-data policy and recovery/test specification.
- **Acceptance:** All CPU/GPU/RAM/VRAM/storage/driver/runtime conditions are specified; three compatibility states are measurable; downloads are verified; lifecycle and failures are explicit; 20% margin remains provisional pending benchmarks.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-AI-LOCAL-002, WP-AI-LOCAL-003, WP-AI-LOCAL-004, WP-AI-LOCAL-005, WP-AI-LOCAL-006.

## WP-AI-TASK-001 — Defined Tasks authoring and prompt templating

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§3,6,28.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Task-definition model, version/publication contract, parameter editor, prompt grammar, variable-reference validation, customer-input contract and trust-boundary rules.
- **Acceptance:** 100-parameter limit, types, required flags, four-choice and unique 32-character keywords are testable; references cannot silently break; customer data is distinct from trusted instructions.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-AI-TASK-002, WP-AI-TASK-003, WP-AI-TASK-004, WP-AI-TASK-005.

## WP-AI-HISTORY-001 — Task execution and completed-task history

- **Type:** Domain baseline / specification gate.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§3,7,8,11,13.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Execution event schema, append-only task/order history, local/network participant rules, query/detail contract and retention/consistency decisions.
- **Acceptance:** Every history field maps to an authoritative record; local runs show no fictitious nodes; network contribution/failure data is evidenced; records link to order/reward/delivery without duplicating financial truth.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-AI-HISTORY-002, WP-AI-HISTORY-003, WP-AI-HISTORY-004.

## WP-REWARD-001 — Reward accounting, balances and reward history

- **Type:** Domain baseline / specification gate.
- **Primary owner:** feasibility-engineer.
- **Source:** §§8,15,23,26,27.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Reward-source taxonomy, ledger/balance definitions, owner/member allocation contracts, availability/withdrawal rules and reconciliation specification.
- **Acceptance:** Compute, verification, issuance and transaction-fee rewards remain distinct; customer revenue is not newly issued coin; balances reconcile; unknown split ratios stay open.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-REWARD-002, WP-REWARD-003, WP-REWARD-004, WP-REWARD-005.

## WP-NET-CREATE-001 — Distributed compute-network creation and ownership

- **Type:** Domain baseline / specification gate.
- **Primary owner:** project-structure-engineer.
- **Source:** §§1,9,14,28,29.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Network manifest and partition contract, owner-management model, first-node registration, setup state machine, backup/recovery requirements and partition decisions.
- **Acceptance:** Network ID and owner identity are unique; each partition maps to an executable stage; assignments have compatibility evidence; management state can be recovered without owner-device single point of failure.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-NET-CREATE-002, WP-NET-CREATE-003, WP-NET-CREATE-004, WP-NET-CREATE-005, WP-NET-CREATE-006.

## WP-NET-JOIN-001 — Existing-network admission and resource allocation

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§10,14,17.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Invitation/discovery, preflight, capacity allocation, admission approval, member registration and voluntary pause/exit contracts.
- **Acceptance:** All seven join steps are represented; identity differs from alias; approval precedes active membership; resource limits are enforceable/user-controlled.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-NET-JOIN-002, WP-NET-JOIN-003, WP-NET-JOIN-004, WP-NET-JOIN-005.

## WP-NET-OPS-001 — Network monitoring, testing, coverage and failover

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§9–11,29.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Node telemetry, health model, network tests, stage/backup coverage, checkpoint/failover and operator alert/recovery workflow.
- **Acceptance:** All Network Test dimensions are observable; primary/backup coverage differ; four connection states are evidence-based; failover uses last valid state and prevents stale outputs.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-NET-OPS-002, WP-NET-OPS-003, WP-NET-OPS-004, WP-NET-OPS-005, WP-NET-OPS-006, WP-NET-OPS-007.

## WP-MARKET-001 — Explore marketplace and provider discovery

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§3,6,12.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Provider/service registry, listing metadata, search/filter, service detail, availability freshness, ranking and abuse controls.
- **Acceptance:** All listing fields are present; local/network services differ; public detail precedes private inputs; availability/reputation have defined sources; registry topology remains open.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-MARKET-002, WP-MARKET-003, WP-MARKET-004, WP-MARKET-005, WP-MARKET-006.

## WP-ORDER-001 — Order intake, payment verification and lifecycle

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§6,7,12,13,23,26.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Order/contract schema, immutable price/popularity snapshots, in-app/external payment contracts, state machine, queue handoff, cancellation/refund/dispute and idempotency.
- **Acceptance:** Execution starts only after the applicable payment condition; chain finality differs from external approval; all states are covered; retries cannot duplicate orders/charges; unresolved refund/escrow policy stays open.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-ORDER-002, WP-ORDER-003, WP-ORDER-004, WP-ORDER-005, WP-ORDER-006, WP-ORDER-007, WP-ORDER-008, WP-ORDER-009.

## WP-DELIVERY-001 — Secure deliverable upload and private customer download

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§13,21,23,28.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Upload/manifest API, file validation/scanning, private storage/encryption, per-order authorization, revocable download and audit/notification.
- **Acceptance:** Files remain private; metadata/SHA-256 are recorded; only order customer accesses them; authorization is checked server-side; URL secrecy is not access control; private content stays off public chain.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-DELIVERY-002, WP-DELIVERY-003, WP-DELIVERY-004, WP-DELIVERY-005, WP-DELIVERY-006, WP-DELIVERY-007.

## WP-FEEDBACK-001 — Customer feedback, no-feedback and dispute entry

- **Type:** Domain baseline / specification gate.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §§13,22,23,31.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Feedback state machine, review window, three feedback outcomes, dispute evidence intake and handoff.
- **Acceptance:** Silence is not feedback; negative feedback is not proof of misconduct; choice links to order/delivery; dispute is separate; unspecified deadlines remain open.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-FEEDBACK-002, WP-FEEDBACK-003, WP-FEEDBACK-004.

## WP-IDENTITY-001 — Node identities, roles and ownership boundaries

- **Type:** Domain baseline / specification gate.
- **Primary owner:** safety-engineer.
- **Source:** §§9,10,14,15,17,18,19,28.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Principal/node identity model, ownership proof, role credentials, authorization matrix, lifecycle/revocation, key separation and Sybil requirements.
- **Acceptance:** Compute node, owner, full node, validator and verifier are distinct; aliases are not authority; concurrent roles do not accidentally share privileges, stake or keys.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-IDENTITY-002, WP-IDENTITY-003, WP-IDENTITY-004, WP-IDENTITY-005, WP-IDENTITY-006.

## WP-CHAIN-001 — Blockchain core, native coin and governance

- **Type:** Domain baseline / specification gate.
- **Primary owner:** feasibility-engineer.
- **Source:** §§8,14,15,16,18,27,31.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Chain/consensus decision package, P2P/transaction lifecycle, native-coin accounting, fee/emission separation, RPC/Explorer, Coin Rules and governance.
- **Acceptance:** Finality and components are specified; native coin is not an off-chain score; fees, protocol issuance and project fees are separate; consensus/Tokenomics remain unapproved until owner decision.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-CHAIN-002, WP-CHAIN-003, WP-CHAIN-004, WP-CHAIN-005, WP-CHAIN-006, WP-CHAIN-007.

## WP-WALLET-001 — Blockchain overview and wallet workflows

- **Type:** Domain baseline / specification gate.
- **Primary owner:** safety-engineer.
- **Source:** §§3,15,16,28,31.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Wallet custody decision, key lifecycle, create/import/restore, backup/recovery, transaction construction/signing, send/receive/history and overview.
- **Acceptance:** Every state is mapped; keys are not exposed to app servers; transaction details are confirmed before signing; custody conflict is a blocking owner decision.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-WALLET-002, WP-WALLET-003, WP-WALLET-004, WP-WALLET-005, WP-WALLET-006, WP-WALLET-007.

## WP-VALIDATOR-001 — Blockchain Validator Center and staking lifecycle

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§15,17,18,27,28.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Validator eligibility, registration, key/stake lifecycle, activation/exit, duty telemetry, rewards/penalties and unbonding.
- **Acceptance:** All registration steps/statuses are represented; validator identity/key/stake are separate from compute membership; unbonding blocks new duties and releases only after checks.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-VALIDATOR-002, WP-VALIDATOR-003, WP-VALIDATOR-004, WP-VALIDATOR-005.

## WP-VERIFY-NODES-001 — AI Task Verification Center and committee selection

- **Type:** Domain baseline / specification gate.
- **Primary owner:** safety-engineer.
- **Source:** §§17,19,24,25,28.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Verifier eligibility/stake, conflict declarations, verifiable randomness, Sybil controls, disjoint committee selection and capacity fallback.
- **Acceptance:** Two committees each have 100 eligible members and zero overlap; insufficient capacity remains Pending Verification; selection is auditable/conflict-aware; verifier is distinct from chain validator.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-VERIFY-NODES-002, WP-VERIFY-NODES-003, WP-VERIFY-NODES-004, WP-VERIFY-NODES-005, WP-VERIFY-NODES-006, WP-VERIFY-NODES-007.

## WP-REPUTATION-001 — Popularity allocation, Good/Bad Reputation and locks

- **Type:** Domain baseline / specification gate.
- **Primary owner:** feasibility-engineer.
- **Source:** §§8,20,22,23,31.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Formula, fixed per-order P snapshot, precision/rounding, Good/Bad ledger, lock/release lifecycle and dispute/no-feedback behavior.
- **Acceptance:** Formulas match Section 20; 10 percentage points apply to C; network fee excluded from C; locked assets unavailable; Good=0 yields N/A.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-REPUTATION-002, WP-REPUTATION-003, WP-REPUTATION-004, WP-REPUTATION-005, WP-REPUTATION-006.

## WP-SETTLEMENT-RECORD-001 — Project Settlement Record and integrity

- **Type:** Domain baseline / specification gate.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§13,21–26,28.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Canonical record schema/version/hash, evidence references, private/on-chain field boundary, signature model and lifecycle.
- **Acceptance:** Every Section 23 field is covered; signatures bind immutable versions; private data stays off-chain; transitions auditable; corrections create new versions.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-SETTLEMENT-RECORD-002, WP-SETTLEMENT-RECORD-003, WP-SETTLEMENT-RECORD-004, WP-SETTLEMENT-RECORD-005, WP-SETTLEMENT-RECORD-006.

## WP-VERIFY-STAGE1-001 — First committee and 80/20 verification

- **Type:** Domain baseline / specification gate.
- **Primary owner:** qa-testing-engineer.
- **Source:** §§19,23,24.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Evidence package, review workflow, signed-vote contract, valid-vote counting and 80/20 closure rule.
- **Acceptance:** Exactly 100 valid votes; at least 80 approvals pass; absent votes are not approval; signatures bind committee/vote/version; protocol computes closure.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-VERIFY-STAGE1-002, WP-VERIFY-STAGE1-003, WP-VERIFY-STAGE1-004, WP-VERIFY-STAGE1-005.

## WP-VERIFY-STAGE2-001 — Independent audit committee and 90/10 verification

- **Type:** Domain baseline / specification gate.
- **Primary owner:** qa-testing-engineer.
- **Source:** §§19,23–25.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Audit evidence, committee-independence proof, review/vote workflow, 90/10 evaluator and Frozen/Re-Review transitions.
- **Acceptance:** Second 100-member set has no overlap; exactly 100 valid votes; at least 90 approvals pass; failure freezes settlement and prevents payout.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-VERIFY-STAGE2-002, WP-VERIFY-STAGE2-003, WP-VERIFY-STAGE2-004, WP-VERIFY-STAGE2-005.

## WP-SETTLEMENT-FINAL-001 — Idempotent final settlement and payment distribution

- **Type:** Domain baseline / specification gate.
- **Primary owner:** execution-engineer.
- **Source:** §§8,12,13,20–27.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Eligibility guard, allocation engine, idempotent payout plan, escrow release, final hash/event and reconciliation.
- **Acceptance:** Both verification stages pass first; each payment binds to Settlement Record ID; retries cannot duplicate payouts; totals reconcile and finality is evidenced.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-SETTLEMENT-FINAL-002, WP-SETTLEMENT-FINAL-003, WP-SETTLEMENT-FINAL-004, WP-SETTLEMENT-FINAL-005, WP-SETTLEMENT-FINAL-006.

## WP-PROTOCOL-REWARDS-001 — Twenty-year protocol incentive schedule

- **Type:** Domain baseline / specification gate.
- **Primary owner:** feasibility-engineer.
- **Source:** §§8,15,18,19,27,31.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Protocol-time/emission formula, base reward/supply decisions, validator/verifier split, claim/record process and economic simulation.
- **Acceptance:** All 21 year points specified; multiplier zero at year 20; chain-derived time; reward streams remain separate; base amount is not invented.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-PROTOCOL-REWARDS-002, WP-PROTOCOL-REWARDS-003, WP-PROTOCOL-REWARDS-004, WP-PROTOCOL-REWARDS-005, WP-PROTOCOL-REWARDS-006.

## WP-SECURITY-001 — Cross-cutting security, privacy and trust controls

- **Type:** Domain baseline / specification gate.
- **Primary owner:** safety-engineer.
- **Source:** §§1,6,9,14–19,21,23–29.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Threat model, asset/data-flow inventory, preventive/detective/recovery controls, identity/key, provenance, isolation, privacy, file access, incident response and residual-risk register.
- **Acceptance:** Named threats/assets mapped; proposed and implemented controls separated; intermediate-data exposure accurately described; residual risks have approval owners.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-SECURITY-002, WP-SECURITY-003, WP-SECURITY-004, WP-SECURITY-005, WP-SECURITY-006, WP-SECURITY-007, WP-SECURITY-008.

## WP-MAINNET-READINESS-001 — Integrated security, economic and legal readiness gate

- **Type:** Domain baseline / specification gate.
- **Primary owner:** qa-testing-engineer.
- **Source:** §§15,27–31.
- **Objective:** Produce the approved domain architecture, contract and acceptance baseline required before implementation.
- **Scope:** Refine requirements into domain model, data ownership, interfaces, states, failure cases, quality constraints, security/privacy boundaries and implementation acceptance. Decompose work into child tasks.
- **Exclusions:** Product feature implementation; unapproved policy/technology decisions; duplicating child implementation ownership.
- **Deliverables:** Traceability and integration matrix, performance/security/economic/legal evidence, recovery rehearsal, risk acceptance and go/no-go/rollback plan.
- **Acceptance:** All ten phases map to deliverables; mandatory benchmark/security/economic/legal evidence exists; unresolved critical decisions block launch; rollback/stop criteria are testable.
- **Direct prerequisites:** WP-INIT-002 plus graph-listed upstream domain baselines.
- **Child work packages:** WP-MAINNET-READINESS-002, WP-MAINNET-READINESS-003, WP-MAINNET-READINESS-004, WP-MAINNET-READINESS-005, WP-MAINNET-READINESS-006, WP-MAINNET-READINESS-007.


## Granular child work packages

A child task is independently schedulable after its domain baseline and additional direct prerequisites are done. The child is not accepted merely because a parent document or directory exists.

### WP-ARCH-002 — System context, actors and operating modes

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§1,2,14,17.
- **Objective:** Define approved system context and every actor/operating mode.
- **In scope:** Enumerate customer, provider, owner, compute node, full node, validator, verifier and operator; distinguish local/distributed operation and the two networks.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Context diagram, actor catalogue and mode matrix.
- **Acceptance checks:** Every actor/mode has purpose, boundary and capability; no role inherits another role's privileges.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001.

### WP-ARCH-003 — Subsystem and responsibility decomposition

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§1,3,9,11,14–19.
- **Objective:** Break product into bounded subsystems with one owner each.
- **In scope:** Define UI, model catalogue, runtime, compute control plane, marketplace, order/payment, delivery, wallet, chain, verification, Reputation and settlement ownership.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Subsystem map and responsibility matrix.
- **Acceptance checks:** Each capability has one accountable subsystem; shared concerns have named interfaces; no component owns conflicting authoritative state.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001.

### WP-ARCH-004 — End-to-end data and control-flow models

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§5,9–14,18–27.
- **Objective:** Map data and control flows for principal journeys.
- **In scope:** Trace local inference, network formation/admission, service listing, order, payment, execution, delivery, feedback, two-stage verification and settlement.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Sequence/data-flow diagrams and event catalogue.
- **Acceptance checks:** Thirteen-step order flow and major AI/network/wallet flows have entry/exit, state owner, data class and failure branches.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001.

### WP-ARCH-005 — Cross-domain interface and event contracts

- **Type:** architecture.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§6–14,17–27.
- **Objective:** Define contracts between independently owned subsystems.
- **In scope:** Specify identifiers, versioning, request/response, events, idempotency, error semantics and compatibility; defer unspecified protocol choices.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Interface catalogue and contract schemas.
- **Acceptance checks:** Each interaction has producer, consumer, purpose, version rule, error model and owner; no hidden shared-database assumption.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001.

### WP-ARCH-006 — Quality attributes, failure model and decision records

- **Type:** architecture.
- **Primary owner:** feasibility-engineer.
- **Source:** §§1,2,11,14,28,29,31.
- **Objective:** Convert non-functional constraints and open choices into reviewable architecture decisions.
- **In scope:** Define availability, integrity, latency, throughput, resource bounds, privacy, observability, recovery, compatibility and operational constraints.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Quality-attribute register, failure catalogue and ADR list.
- **Acceptance checks:** Each quality attribute has rationale and verification method; open choice has options, impact and owner; no proposal is marked approved without evidence.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ARCH-001.

### WP-APP-002 — Window shell, regions and resize behavior

- **Type:** design.
- **Primary owner:** design-engineer.
- **Source:** §§2,3.1.
- **Objective:** Specify Windows shell and stable layout regions.
- **In scope:** Define window lifecycle, sidebar, top bar, breadcrumb, content area, collapse/expand, resizing, scaling and minimum usable viewport.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Shell layout specification and breakpoints.
- **Acceptance checks:** Each region has size/behavior constraints; resize/scaling are measurable; no mobile-first requirement invented.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-APP-001.

### WP-APP-003 — Navigation map, route identity and page access

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §§3.2–3.4.
- **Objective:** Specify navigation hierarchy and predictable movement.
- **In scope:** Map four primary areas, detailed pages, global Dashboard and Orders & Deliveries, breadcrumbs, selection and role-conditional entries.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Navigation tree and route map.
- **Acceptance checks:** All named pages are represented once; no required destination is orphaned; breadcrumbs/active state resolve to stable routes.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-APP-001.

### WP-APP-004 — Shared component catalogue and semantic states

- **Type:** design.
- **Primary owner:** design-engineer.
- **Source:** §§3,5,9–13,16,18,19.
- **Objective:** Define reusable UI components and state vocabulary.
- **In scope:** Specify forms, tables, cards, status indicators, dialogs, notifications, progress, empty/error/success/warning/disabled/selected/focus states.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Component inventory and state specification.
- **Acceptance checks:** Each component has purpose, inputs, variants, state behavior, accessibility and reuse boundary.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-APP-001.

### WP-APP-005 — Dashboard metrics, freshness and navigation actions

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §3.5.
- **Objective:** Specify dashboard data elements and authoritative sources.
- **In scope:** Map balances, locked reputation/stake, pending rewards, models/networks/tasks, health, orders, activity and quick actions.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Dashboard field dictionary/query contract.
- **Acceptance checks:** Every metric has source, unit, freshness, privacy, empty/error state and target route; unsupported values are never fabricated.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-APP-001.

### WP-APP-006 — Settings information architecture and preference persistence

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §3.2.
- **Objective:** Specify settings and preference behavior.
- **In scope:** Define account, security, wallet-security, notifications, privacy, storage and preferences; validation, save/cancel/reset, sensitive confirmation and persistence.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Settings page and preference contract.
- **Acceptance checks:** Every source category is represented; sensitive operations require confirmation; persistence and failure states are defined.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-APP-001.

### WP-APP-007 — Accessibility, keyboard, contrast and Windows scaling acceptance

- **Type:** design.
- **Primary owner:** design-engineer.
- **Source:** §§2,3.
- **Objective:** Make accessibility and desktop compatibility measurable.
- **In scope:** Define keyboard order, focus, tab/escape, text scaling, contrast, readable density and high-DPI scenarios.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Accessibility checklist and desktop test matrix.
- **Acceptance checks:** Critical pages work without pointer-only actions; focus visible; scaling does not hide controls; English labels stay legible.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-APP-001.

### WP-MODEL-002 — Canonical model metadata schema

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §4.
- **Objective:** Define a versioned schema for each catalogue item.
- **In scope:** Include model/version/developer/repository/architecture/parameters/size/type/tasks/hardware/RAM/VRAM/download/quantization/engine/context/licence.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Schema and field dictionary.
- **Acceptance checks:** Every field has type, validation and provenance; missing values are explicitly unknown.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001.

### WP-MODEL-003 — Official-source registry and acquisition adapters

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§2,4.1.
- **Objective:** Control retrieval from approved model repositories.
- **In scope:** Define trusted source allowlists, immutable revisions, download metadata, redirect rules and adapter failures.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Source registry and acquisition adapter.
- **Acceptance checks:** Only approved origins/versions selectable; origin/revision recorded; untrusted redirect changes fail closed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001.

### WP-MODEL-004 — Model-file integrity and authenticity verification

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§4.1,5.
- **Objective:** Verify artifacts before they can be loaded.
- **In scope:** Define digest/signature sources, streaming hash, interrupted-download handling, manifest consistency and quarantine.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Artifact verification module.
- **Acceptance checks:** Mismatched/truncated/unverified files cannot load; digest source recorded; retry cannot silently overwrite verified artifacts.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001.

### WP-MODEL-005 — Version-specific licence assessment and eligibility gates

- **Type:** governance.
- **Primary owner:** feasibility-engineer.
- **Source:** §§2,4.1,31.1.
- **Objective:** Create a licence decision for exact model version and intended use.
- **In scope:** Separate weights, code, commercial use, redistribution, node transfer, attribution and restrictions; record reviewer/date/evidence.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Licence decision record and eligibility policy.
- **Acceptance checks:** Local/distributed eligibility differ; family-wide licence assumption prohibited; unknown/incompatible terms block affected use.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001.

### WP-MODEL-006 — Model-runtime compatibility and quantization matrix

- **Type:** specification.
- **Primary owner:** execution-engineer.
- **Source:** §§4,5,9.
- **Objective:** Define supported model formats, quantizations, runtimes and platforms.
- **In scope:** Map model revision to engine, quantization, hardware and required features; document unsupported combinations.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Compatibility matrix.
- **Acceptance checks:** Every supported combination has evidence; unsupported combinations fail preflight with reason; no runtime selected without approval.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MODEL-001.

### WP-AI-LOCAL-002 — Windows hardware and runtime inventory

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §5.1.
- **Objective:** Collect local machine capabilities for compatibility.
- **In scope:** Read CPU/GPU/RAM/VRAM/storage/driver/runtime via supported interfaces; distinguish unavailable readings.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Hardware inventory service.
- **Acceptance checks:** Every dimension has value/unit/source/confidence; failed queries explicit; no capability guessed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001.

### WP-AI-LOCAL-003 — Compatibility thresholds and benchmark calibration

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§5.1,5.2.
- **Objective:** Define deterministic compatibility results and evidence.
- **In scope:** Specify minimum/recommended requirements, 20% margin, warning and incompatibility rules, benchmark calibration.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Decision rules and benchmark plan.
- **Acceptance checks:** Results reproducible from measured inputs/versioned thresholds; 20% margin marked provisional until calibrated.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001.

### WP-AI-LOCAL-004 — Model download, install and verified cache lifecycle

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§4.1,5.3.
- **Objective:** Manage safe download/install/cache lifecycle.
- **In scope:** Handle progress, resume, disk preflight, checksum, atomic activation, versioned storage, cancel and cleanup.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Download/install lifecycle.
- **Acceptance checks:** Partial downloads never load; artifacts pass integrity verification; cancel leaves consistent cache; disk use observable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001.

### WP-AI-LOCAL-005 — Inference runtime adapter and model load/unload lifecycle

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §5.3.
- **Objective:** Implement controlled runtime lifecycle inside application.
- **In scope:** Define adapter, dependencies, load/unload, memory reservation, warm-up, isolation and error mapping.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Runtime adapter and lifecycle service.
- **Acceptance checks:** States explicit; failures release resources; model/version bound to session; no separate chat app required.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001.

### WP-AI-LOCAL-006 — Local conversation sessions, context and cancellation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§5,6.
- **Objective:** Implement local prompt execution and session behavior.
- **In scope:** Handle message order, context limit, stop/cancel, retry, session isolation, formatting and metadata.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Conversation/session service.
- **Acceptance checks:** User sends/receives local messages; cancellation honored; context never leaks; overflow has explicit outcome.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-LOCAL-001.

### WP-AI-TASK-002 — Defined Task entity, version and publication lifecycle

- **Type:** data-contract.
- **Primary owner:** execution-engineer.
- **Source:** §6.
- **Objective:** Define stable task identity and versioning.
- **In scope:** Model draft, validation, published, paused and retired; owner; immutable versions referenced by accepted orders.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Task schema and lifecycle contract.
- **Acceptance checks:** Every order references immutable task version; published change creates new version or approved migration; no silent mutation.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001.

### WP-AI-TASK-003 — Input parameter editor and field validation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §6.1.
- **Objective:** Implement provider authoring of supported input fields.
- **In scope:** Enforce 100-field max, long-form/four-choice types, four options, required flags, unique keywords/32-char cap.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Parameter editor and validator.
- **Acceptance checks:** Boundary 0/1/100/101, duplicates, overlength keys, missing choices and required flags are tested.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001.

### WP-AI-TASK-004 — Prompt-template parser and keyword reference integrity

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §6.2.
- **Objective:** Parse and validate /keyword prompt references.
- **In scope:** Define grammar, autocomplete, tokenization, unknown/deleted/renamed errors, escaping and immutable published versions.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Template parser/reference resolver.
- **Acceptance checks:** Each variable resolves once; unknown/ambiguous refs block publication; rename/delete cannot mutate published order prompt.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001.

### WP-AI-TASK-005 — Customer input validation and trusted/untrusted prompt assembly

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §6.2,§28.
- **Objective:** Keep customer values as data, not trusted system instructions.
- **In scope:** Define input bounds, encoding, injection-aware assembly, logging minimization and safe rendering.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Prompt assembly trust-boundary rules.
- **Acceptance checks:** Customer text cannot alter instruction boundary by concatenation; raw input remains untrusted; no unsafe HTML/code execution.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-TASK-001.

### WP-AI-HISTORY-002 — Execution and order event schema

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §7.
- **Objective:** Define immutable events for execution and order history.
- **In scope:** Cover IDs, timestamps, status, duration, payment/reward refs, result and network participants when applicable.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Event schema/type dictionary.
- **Acceptance checks:** Every history field maps to typed events; event origin traceable; local runs omit node participants.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001.

### WP-AI-HISTORY-003 — History persistence, indexing and authorized retrieval

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§7,21,23.
- **Objective:** Persist history and expose authorized queries.
- **In scope:** Define transaction boundaries, indexes, pagination, filters, user/order scope, retention hooks and recovery.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** History repository/query API.
- **Acceptance checks:** Ownership enforced; records not duplicated; pagination stable; retention configurable until approved.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001.

### WP-AI-HISTORY-004 — History detail views and evidence cross-links

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §§3,7,11,23.
- **Objective:** Let users inspect an execution/order and its evidence.
- **In scope:** Link execution, nodes, payment, delivery, rewards and settlement without exposing private data.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** History detail flow.
- **Acceptance checks:** Displayed value has source record; inapplicable fields explained; links enforce authorization.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-AI-HISTORY-001.

### WP-REWARD-002 — Reward source ledger and event taxonomy

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §8,15,23,26,27.
- **Objective:** Define authoritative records for every reward source.
- **In scope:** Separate compute/order-funded rewards, verification fees, validator/block rewards, protocol emission and transaction fees; include reversal/pending.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Reward ledger schema.
- **Acceptance checks:** Every event has distinct source, amount, asset and origin reference.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REWARD-001.

### WP-REWARD-003 — Balance projection and available/locked/pending semantics

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§8,16,20,23.
- **Objective:** Calculate user-facing balances from ledger entries.
- **In scope:** Define total, available, locked, pending, withdrawn and approved; owner/member views; consistency snapshot.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Balance projection service.
- **Acceptance checks:** Each category has formula/source events; locked/pending cannot be spent; projection reconciles to ledger.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REWARD-001.

### WP-REWARD-004 — Network owner/member allocation accounting

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§8.2,9.3,26,27.
- **Objective:** Represent network-level receipts and member distributions.
- **In scope:** Map owner/member reward, allocated/distributed, source streams and unresolved ratios.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Allocation model.
- **Acceptance checks:** Every amount attributable to owner/member/source; split ratio not fabricated; remainder explicit.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REWARD-001.

### WP-REWARD-005 — Withdrawal eligibility and payout reconciliation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§8,15,16.
- **Objective:** Withdraw eligible rewards safely.
- **In scope:** Gate by availability, lock/vesting, fee and finality; prevent duplicate withdrawals; reconcile chain result.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Withdrawal lifecycle.
- **Acceptance checks:** Ineligible funds cannot withdraw; details confirmed; each request idempotent and chain-backed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REWARD-001.

### WP-NET-CREATE-002 — Model partition manifest and executable stage mapping

- **Type:** data-contract.
- **Primary owner:** execution-engineer.
- **Source:** §§1.1,9.1.
- **Objective:** Define versioned division of model into executable pipeline stages.
- **In scope:** Record model revision, stage order, artifact refs, resource minimums, stage I/O and compatibility.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Partition manifest.
- **Acceptance checks:** Every stage maps to exact model revision and predecessor/successor; uncovered/incompatible stage blocks activation; no implicit Tensor Parallelism.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-CREATE-001.

### WP-NET-CREATE-003 — Owner hardware capacity and partition benchmark

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer.
- **Source:** §9.2.
- **Objective:** Estimate capacity from measured hardware and model benchmarks.
- **In scope:** Measure memory/CPU/GPU/network constraints; distinguish predicted/measured values; record confidence/environment.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Benchmark procedure/report.
- **Acceptance checks:** Estimates cite conditions/model version; 20% margin marked provisional; no unsupported allocation.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-CREATE-001.

### WP-NET-CREATE-004 — Owner identity, configuration and secrets boundary

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §9.3,§28.
- **Objective:** Protect management-plane data and owner privileges.
- **In scope:** Separate owner identity, payout addresses, manifests, prompts, logs, backups and keys; define access control/secrets.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Owner-management data model.
- **Acceptance checks:** Owner-only actions require auth; secrets protected; compute role does not imply owner; state is recoverable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-CREATE-001.

### WP-NET-CREATE-005 — Network creation and first-member registration

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §9.4.
- **Objective:** Create network and register owner computer as first member.
- **In scope:** Create Network ID, initialize owner, bind manifest/settings, persist config and register initial node with recoverable steps.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Network creation service/state machine.
- **Acceptance checks:** Success yields unique ID and first node; partial failure resumes/rolls back without duplicates.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-CREATE-001.

### WP-NET-CREATE-006 — Management backup and restore drills

- **Type:** operations.
- **Primary owner:** execution-engineer.
- **Source:** §9.3,§28,§29.
- **Objective:** Recover network management state after owner device failure.
- **In scope:** Define encrypted backup, integrity, version, frequency policy, restore authority and secret handling.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Backup/restore procedure.
- **Acceptance checks:** Restore drill reconstructs required state; secrets protected; owner device not sole recovery point.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-CREATE-001.

### WP-NET-JOIN-002 — Invitation token and network discovery contract

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §10.1.
- **Objective:** Secure discovery/invitation for an existing network.
- **In scope:** Handle Network ID, invitation issuance/expiry/revocation, anti-enumeration and public metadata.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Invitation API/token lifecycle.
- **Acceptance checks:** Expired/revoked/invalid invites fail; invite is not treated as node identity.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-JOIN-001.

### WP-NET-JOIN-003 — Join preflight and hardware capability report

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §10.2–10.4.
- **Objective:** Check candidate device capability for requested contribution.
- **In scope:** Validate runtime/model/resources/bandwidth/stage capacity and show confidence/unsupported reasons.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Join preflight report.
- **Acceptance checks:** Every decision has measured input/model version; estimate shown before request; unsupported capacity is not overstated.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-JOIN-001.

### WP-NET-JOIN-004 — Resource quota, user limits and admission policy

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §10.5,§28.
- **Objective:** Define enforceable resource limits and owner policy.
- **In scope:** Model CPU/GPU/RAM/VRAM/bandwidth caps, pause, owner policy and quota changes.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Resource allocation contract.
- **Acceptance checks:** Limits explicit, validated and reversible; contributions cannot exceed user-approved caps.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-JOIN-001.

### WP-NET-JOIN-005 — Owner approval, registration and voluntary exit

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §10.6–10.7.
- **Objective:** Complete admission and member lifecycle.
- **In scope:** Persist request, approval/rejection, identity binding, activation, pause, withdrawal and outstanding-work handoff.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Admission state machine.
- **Acceptance checks:** Only approved nodes active; outcomes auditable; exit stops new work and resolves active assignment safely.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-JOIN-001.

### WP-NET-OPS-002 — Node telemetry, heartbeat and last-seen model

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§11.3–11.5.
- **Objective:** Collect minimum telemetry for each compute node.
- **In scope:** Record node ID/alias, resources, stages, heartbeat, connection metrics and last-seen.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Telemetry schema/ingestion.
- **Acceptance checks:** Freshness explicit; alias never replaces ID; stale metrics not shown as current.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-OPS-001.

### WP-NET-OPS-003 — Connection health and node state transitions

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §11.4.
- **Objective:** Implement four source-defined connection states.
- **In scope:** Define evidence/threshold inputs for Active, Inactive, Weak Connection and Unavailable; defer exact thresholds if unapproved.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Health state machine.
- **Acceptance checks:** Transitions carry reason/time; thresholds configurable/approved; flapping does not duplicate assignments.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-OPS-001.

### WP-NET-OPS-004 — Network Test and end-to-end inference probe

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §11.2.
- **Objective:** Test complete distributed inference path reproducibly.
- **In scope:** Check peers, throughput, latency, packet loss, runtime, stage order, test request and uncovered stages.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Network Test suite/report.
- **Acceptance checks:** All source checks have pass/fail evidence; failure names node/stage; probe is not a billable order.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-OPS-001.

### WP-NET-OPS-005 — Primary/backup stage coverage and redundancy

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §11.3,11.5.
- **Objective:** Calculate stage coverage separately for primary and backup nodes.
- **In scope:** Map model stages to assignments; identify uncovered, single-covered and redundant stages.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Coverage model/API.
- **Acceptance checks:** Coverage denominator is required model stages; primary/backup separately counted; allocation is not availability proof.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-OPS-001.

### WP-NET-OPS-006 — Checkpoint, failover and recovery consistency

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §11.5,29.
- **Objective:** Continue safely when a node fails or disconnects.
- **In scope:** Specify checkpoint identity/version, last valid state, reassignment, deduplication, replay and partial-output rollback.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Failover controller.
- **Acceptance checks:** Replacement resumes from authenticated state or restarts safely; stale output rejected; duplicate side effects prevented.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-OPS-001.

### WP-NET-OPS-007 — Operator alerts and network incident timeline

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §11.
- **Objective:** Make degradation/recovery understandable to operators.
- **In scope:** Define triggers, severity, node/stage, action, acknowledgement and event timeline.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Incident UX.
- **Acceptance checks:** Alerts actionable/nonduplicative; unresolved states clear; acknowledgements and recovery recorded.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-NET-OPS-001.

### WP-MARKET-002 — Provider and service registry schema

- **Type:** data-contract.
- **Primary owner:** execution-engineer.
- **Source:** §12,§6.
- **Objective:** Define provider/service discovery records and ownership.
- **In scope:** Model service version, provider, category, specialty, AI type, model, price, ETA, availability, reputation, popularity and publication state.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Registry schema.
- **Acceptance checks:** Each field typed/sourced/visible; private input/delivery excluded; unpublished/stale records not discoverable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MARKET-001.

### WP-MARKET-003 — Search, categories, filters and stable paging

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §12.1.
- **Objective:** Implement search and filtering over service listings.
- **In scope:** Define normalization, category/specialty facets, sorting and pagination; bound query resources.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Search/filter API/tests.
- **Acceptance checks:** Same snapshot/input gives stable results; invalid filters return errors; paging does not duplicate/drop records.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MARKET-001.

### WP-MARKET-004 — Service detail and pre-order disclosure

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §12.
- **Objective:** Specify public service detail before Continue.
- **In scope:** Present model/type/provider/category/price/time/availability/reputation/popularity/limits/payment options without private data.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Service detail flow.
- **Acceptance checks:** Listing details visible with units/estimate labels; input form follows disclosure; unknowns labelled.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MARKET-001.

### WP-MARKET-005 — Availability, ranking freshness and provider status

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §12.
- **Objective:** Define freshness/correctness of service availability and indicators.
- **In scope:** Set timestamps, source, cache invalidation, expiry and stale behavior; leave ranking policy open.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Availability contract/tests.
- **Acceptance checks:** Stale provider not shown live; freshness timestamp visible; ranking is not quality guarantee.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MARKET-001.

### WP-MARKET-006 — Listing validation, abuse report and provider moderation

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §12,§28.
- **Objective:** Protect marketplace from deceptive or malicious service listings.
- **In scope:** Define listing checks, provider ownership, reports, evidence, suspension and appeal boundaries.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Moderation workflow.
- **Acceptance checks:** Unauthorized provider cannot publish; reports auditable; suspension preserves orders/financial records; approval policy open.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MARKET-001.

### WP-ORDER-002 — Order draft and immutable customer-input snapshot

- **Type:** data-contract.
- **Primary owner:** execution-engineer.
- **Source:** §§6,12,13,23.
- **Objective:** Turn selected service inputs into an immutable order draft.
- **In scope:** Bind provider/service/task version, customer, validated inputs, Order ID, timestamp, consent and data class.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Order draft schema.
- **Acceptance checks:** Accepted order preserves exact task/input version; edits cannot mutate accepted data; sensitive input minimized.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-003 — Contract pricing, currency and terms snapshot

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§6.3,12.2–12.4,23,31.
- **Objective:** Define commercial terms fixed at acceptance.
- **In scope:** Specify USD/native coin amount, FX snapshot if approved, fee exclusions, popularity percentage and provider terms.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Immutable order terms contract.
- **Acceptance checks:** Amounts/currency unambiguous; FX source/time recorded; unresolved FX/fee blocks unsupported conversion.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-004 — In-app payment, confirmation and finality adapter

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §12.2,§15,§16.
- **Objective:** Integrate coin payment with order state.
- **In scope:** Create payment request, tx reference, finality monitor, duplicate/reorg/error handling and escrow reference.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Payment adapter.
- **Acceptance checks:** Order queues only after configured finality/escrow condition; pending/failed/reorged payments cannot dispatch.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-005 — External-payment verification queue

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §12.3.
- **Objective:** Accept external payment only through explicit review.
- **In scope:** Capture evidence, reviewer, decision, time, amount/currency reconciliation and approve/reject/pending.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** External payment workflow.
- **Acceptance checks:** No queue before authorized approval; evidence ties to exact order/amount; not represented as chain-confirmed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-006 — Order state machine and execution queue handoff

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §12.4,§13.
- **Objective:** Implement legal transitions and dispatch after payment.
- **In scope:** Define all source states, guards, scheduler handoff, retries and outbox guarantees.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** State machine/queue contract.
- **Acceptance checks:** Illegal transitions rejected; queue handoff once; transition auditable; failures recoverable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-007 — Cancellation, refund and reversal workflow

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §12.4,§31.2.
- **Objective:** Handle cancel/refund across payment states.
- **In scope:** Map pre/post-payment cancel, failed execution, refund approval, partial/full refund and chain limitations.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Refund state/transaction contract.
- **Acceptance checks:** Refunds auditable/idempotent; irreversible chain transfer not described as reversible; unknown policy not invented.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-008 — Dispute intake, evidence and escalation

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §12.4,§13,§22,§31.
- **Objective:** Define dispute path separate from feedback.
- **In scope:** Capture reason/evidence/order/delivery state, response window, authority, freeze and appeal.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Dispute workflow.
- **Acceptance checks:** Not Satisfied is not automatically dispute; sensitive evidence access controlled; frozen state follows approved policy.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-ORDER-009 — Order idempotency, retries and financial invariant tests

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §§12,13,26,28.
- **Objective:** Prevent duplicate charge/order/execution during retries.
- **In scope:** Test idempotency key scope, unique constraints, replayed webhooks, reconciliation and failpoints.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Invariant test suite.
- **Acceptance checks:** Duplicate calls yield one logical order/payment/dispatch; financial transitions reconcile; timeout cases tested.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-ORDER-001.

### WP-DELIVERY-002 — Upload session, multipart handling and manifest

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §21.1.
- **Objective:** Handle one/multiple final files or packages.
- **In scope:** Manage resumable uploads, IDs, file metadata, versions, timestamps and manifest.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Upload service/manifest schema.
- **Acceptance checks:** Incomplete upload not ready; files map to manifest; retries do not create duplicate delivery.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-DELIVERY-001.

### WP-DELIVERY-003 — File type, size and content validation

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §21.2,§28.4.
- **Objective:** Validate actual content before storage/release.
- **In scope:** Define MIME/magic-byte checks, size limits, archive/path traversal and decompression bounds.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Validation policy/module.
- **Acceptance checks:** Actual content checked rather than extension; malformed/disallowed content rejected or quarantined.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-DELIVERY-001.

### WP-DELIVERY-004 — Malware scan, SHA-256 and scan status

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §21.1–21.2.
- **Objective:** Verify integrity and scan deliverables.
- **In scope:** Compute SHA-256; bind manifest; record scanner/version/time/result and rescan policy.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Scan/integrity pipeline.
- **Acceptance checks:** Download blocked/quarantined pending required scan; hash mismatch detected; scan not claimed absolute safety.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-DELIVERY-001.

### WP-DELIVERY-005 — Private object storage, encryption and retention

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §21.2,§28.4.
- **Objective:** Store files privately with encryption and lifecycle policy.
- **In scope:** Define container privacy, encryption at rest, key access, replication, retention/deletion and backup.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Storage adapter/policy.
- **Acceptance checks:** No public read/list; encryption controlled; deletion/retention auditable; unknown periods remain open.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-DELIVERY-001.

### WP-DELIVERY-006 — Per-order authorization and revocable download links

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §21.3,§28.4.
- **Objective:** Enforce customer-specific authorization on every download.
- **In scope:** Bind Customer/Order IDs; check owner/current state server-side; issue short-lived/revocable link or stream; prevent IDOR.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Access control and tests.
- **Acceptance checks:** Cross-order ID change cannot access file; expired/revoked link fails; URL secrecy not sole control.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-DELIVERY-001.

### WP-DELIVERY-007 — Download audit, notification and review entry

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §21.3–21.4.
- **Objective:** Notify customer after deliverable is ready and record access.
- **In scope:** Display metadata/hash/scan status; audit downloads; notify after readiness; start review period only under approved rule.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Delivery timeline/notification contract.
- **Acceptance checks:** Customer identifies exact version/integrity evidence; every download logged; no premature notification.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-DELIVERY-001.

### WP-FEEDBACK-002 — Signed customer feedback capture

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§13,22,23.6.
- **Objective:** Capture one valid feedback choice and bind it to order/delivery.
- **In scope:** Implement three choices, actor check, one-response/revision policy, timestamp/signature and duplicate prevention.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Feedback API/event schema.
- **Acceptance checks:** Only order customer can respond; choice/time immutable; duplicates handled deterministically.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-FEEDBACK-001.

### WP-FEEDBACK-003 — No Feedback timer and pending-policy gate

- **Type:** governance.
- **Primary owner:** feasibility-engineer.
- **Source:** §§13,22,31.2.
- **Objective:** Specify behavior when customer does not respond.
- **In scope:** Define start trigger, clock source, reminders, expiry, pending state and decision owner.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** No Feedback decision record.
- **Acceptance checks:** Silence never becomes positive/negative; deadline/disposition owner-approved; pending status explicit.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-FEEDBACK-001.

### WP-FEEDBACK-004 — Dispute handoff and feedback separation tests

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §§22,31.
- **Objective:** Verify feedback and dispute semantics.
- **In scope:** Test Not Satisfied without dispute, dispute with evidence, No Feedback, duplicates, frozen state and authorization.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Scenario suite.
- **Acceptance checks:** Negative feedback alone never means misconduct; dispute has separate state/evidence; pending feedback follows approved rule.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-FEEDBACK-001.

### WP-IDENTITY-002 — Principal, account and cryptographic node identity schema

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§9.3,10,14,17,28.
- **Objective:** Define distinct principal/account/node identities.
- **In scope:** Separate person/account, device, compute node, owner and role identities; bind keys and ownership proof while minimizing data.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Identity schema.
- **Acceptance checks:** Each identity has unique ID, issuer/proof/lifecycle; alias display-only; sensitive identity data minimized.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-IDENTITY-001.

### WP-IDENTITY-003 — Role credential and key lifecycle separation

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§15–18,28.
- **Objective:** Define separate credentials for all node roles.
- **In scope:** Classify wallet/node/validator/verifier/owner/infra secrets; specify generation, storage, rotation, recovery and revocation.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Credential/key matrix.
- **Acceptance checks:** Keys purpose-separated; compute key cannot sign validator action; recovery cannot elevate privileges silently.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-IDENTITY-001.

### WP-IDENTITY-004 — Authorization matrix and privileged-operation guards

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§9,10,15–19,21,28.
- **Objective:** Enforce least privilege for owner/wallet/validator/verifier/order actions.
- **In scope:** Map role-action-resource matrix, server-side guards, step-up confirmation and denial logging.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Authorization policy/service.
- **Acceptance checks:** Every privileged endpoint checks authority; client alias/role never grants permission; unauthorized attempts denied/audited.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-IDENTITY-001.

### WP-IDENTITY-005 — Identity enrollment, rotation, suspension and revocation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§10,18,19,28.
- **Objective:** Implement lifecycle transitions and safe deactivation.
- **In scope:** Handle enrollment, key rotation, suspension, recovery, exit and revocation propagation.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Identity lifecycle service.
- **Acceptance checks:** Revoked credential cannot authorize new action; prior signed evidence remains verifiable; history preserved.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-IDENTITY-001.

### WP-IDENTITY-006 — Ownership linkage and Sybil-resistance evidence

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§10,19,28.
- **Objective:** Define owner linkage for committee independence and abuse controls.
- **In scope:** Record proof level, common ownership, conflict declarations, privacy boundaries and appeal without choosing intrusive method.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Ownership/Sybil specification.
- **Acceptance checks:** Selection can apply approved conflict controls; evidence auditable/privacy-aware; unresolved mechanisms stay open.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-IDENTITY-001.

### WP-CHAIN-002 — Consensus, finality and protocol decision package

- **Type:** architecture-decision.
- **Primary owner:** feasibility-engineer.
- **Source:** §15,§31.4.
- **Objective:** Compare consensus/finality options without prematurely selecting one.
- **In scope:** Define threat assumptions, duties, finality, reorg, hardware, network and governance criteria.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Consensus ADR options.
- **Acceptance checks:** No consensus approved without owner decision; security/performance/decentralization tradeoffs recorded.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-CHAIN-001.

### WP-CHAIN-003 — P2P peer protocol and network lifecycle

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§14.2,15.1.
- **Objective:** Specify peer discovery, authenticated connection and synchronization.
- **In scope:** Define identity handshake, versioning, gossip, rate limits, sync states and partition behavior.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** P2P protocol contract.
- **Acceptance checks:** Only compatible authenticated peers exchange messages; malformed payloads fail safely; peer state observable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-CHAIN-001.

### WP-CHAIN-004 — Transaction validation, mempool and replay protection

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §15.1,§28.5.
- **Objective:** Validate transactions before block inclusion.
- **In scope:** Check signatures, nonce, balances, fee, format, limits, replay and conflict; define mempool expiry/eviction.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Transaction validation engine.
- **Acceptance checks:** Invalid/replayed/double-spend rejected; validation deterministic; resource limits bound mempool.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-CHAIN-001.

### WP-CHAIN-005 — Native coin ledger, issuance and fee accounting

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§15.1,15.3–15.4,27,31.4.
- **Objective:** Define native asset accounting without inventing Tokenomics.
- **In scope:** Model supply, issuance, block rewards, fees, treasury and role-funded rewards as separate flows.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Coin accounting spec/parameter register.
- **Acceptance checks:** Sources/destinations/conservation explicit; unknown values remain parameters; off-chain score not coin.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-CHAIN-001.

### WP-CHAIN-006 — RPC/API, explorer and public data boundary

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §15.1,15.4,16,23.
- **Objective:** Define interfaces for wallets, app and chain inspection.
- **In scope:** Specify RPC, transaction/block query, pagination, indexing, finality fields and private-data exclusion.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** RPC contract/explorer dictionary.
- **Acceptance checks:** API versioned/access-controlled; explorer only public protocol data; prompts/files/private URLs excluded.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-CHAIN-001.

### WP-CHAIN-007 — Coin Rules, governance and protocol upgrades

- **Type:** governance.
- **Primary owner:** feasibility-engineer.
- **Source:** §§15.1,15.4,31.
- **Objective:** Define proposal/approval/activation of protocol parameter changes.
- **In scope:** Specify proposal, review, vote, activation height, compatibility, mitigation and audit; distinguish parameter vs protocol rules.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Governance/upgrade spec.
- **Acceptance checks:** Every rule has authority/quorum/activation semantics; unsafe unilateral changes blocked; governance model requires approval.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-CHAIN-001.

### WP-WALLET-002 — Wallet custody decision and key threat model

- **Type:** governance.
- **Primary owner:** safety-engineer.
- **Source:** §§15.2,16.2,28,31.4.
- **Objective:** Resolve Self-Custody vs Managed inconsistency before implementation.
- **In scope:** Compare possession/recovery/server access/user responsibility/threat/regulatory effects.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Owner decision and threat model.
- **Acceptance checks:** No wallet implementation approved until owner chooses; no custody guarantee implied.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-WALLET-001.

### WP-WALLET-003 — Wallet creation, import and restore workflow

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §16.2.
- **Objective:** Implement wallet lifecycle after custody approval.
- **In scope:** Define key generation/import validation/address derivation/network selection/restore errors/activation.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Wallet lifecycle API/UI.
- **Acceptance checks:** Only approved custody model implemented; wrong-network import fails; activation requires backup evidence.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-WALLET-001.

### WP-WALLET-004 — Encrypted backup, recovery and key rotation

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§16.2,28.3.
- **Objective:** Protect wallet backup across device loss.
- **In scope:** Specify encryption, recovery material, offline backup, integrity, rotation and anti-phishing warnings.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Backup/recovery design/tests.
- **Acceptance checks:** Secrets never logged; incorrect backup fails safely; recovery needs user action; old key authority revoked appropriately.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-WALLET-001.

### WP-WALLET-005 — Transaction construction, fee and signing boundary

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §16.3.
- **Objective:** Build transaction and present exact signing payload.
- **In scope:** Validate recipient, amount, network, fee, memo and total; separate unsigned tx from signer; prevent substitution/replay.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Transaction builder/signer interface.
- **Acceptance checks:** Displayed payload equals signed payload; fees confirmed; signer cannot silently change recipient/amount; key stays within approved boundary.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-WALLET-001.

### WP-WALLET-006 — Send/receive status tracking and history

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§16.3–16.5.
- **Objective:** Expose transfer and receipt states.
- **In scope:** Handle Signed/Broadcast/Pending/Confirmed/Finalized/Failed; QR/address; transaction categories and detail.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Wallet transaction tracking.
- **Acceptance checks:** Status backed by chain evidence; confirmation not mislabelled finality; history categories complete; duplicate ingestion idempotent.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-WALLET-001.

### WP-WALLET-007 — Wallet/blockchain overview balance projection

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §16.1–16.2.
- **Objective:** Define authoritative sources for overview metrics.
- **In scope:** Map available/locked/reputation/stake/pending, block height/finality/peers/validators/fee/sync.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Overview field dictionary.
- **Acceptance checks:** Every field has source/unit/freshness/unavailable state; projections do not claim finality; balances access-controlled.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-WALLET-001.

### WP-VALIDATOR-002 — Validator eligibility and hardware/network rules

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§18.1,18.3.
- **Objective:** Define blockchain validator qualification.
- **In scope:** Map identity, software, hardware, network, uptime and stake criteria; mark unknown thresholds.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Eligibility policy.
- **Acceptance checks:** Candidate result reproducible; unknown thresholds are parameters; compute membership alone is insufficient.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VALIDATOR-001.

### WP-VALIDATOR-003 — Validator registration, consensus key and activation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §18.2.
- **Objective:** Implement eight-stage validator registration.
- **In scope:** Create identity, register key, lock stake, submit transaction and manage activation queue.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Registration workflow.
- **Acceptance checks:** All eight stages explicit; failed registration recoverable; key/stake bound to correct identity.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VALIDATOR-001.

### WP-VALIDATOR-004 — Stake, unstake, unbonding and slashing lifecycle

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §18.2–18.5.
- **Objective:** Implement validator staking/exit under approved Coin Rules.
- **In scope:** Stop new assignments, finish active duties, start unbonding, apply approved penalty, release after checks.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Staking state machine.
- **Acceptance checks:** Locked stake not withdrawable early; chain reconciliation; no stake/period/penalty invented.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VALIDATOR-001.

### WP-VALIDATOR-005 — Validator duty telemetry, rewards and appeal records

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §18.3–18.5,§27.
- **Objective:** Verify status/performance/reward/penalty evidence.
- **In scope:** Test uptime, duties, consensus participation, reward events, penalties and last activity.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Performance test matrix.
- **Acceptance checks:** Metrics have source/window; payouts/penalties map to chain events; appeal traceable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VALIDATOR-001.

### WP-VERIFY-NODES-002 — Task-verifier registration, eligibility and stake

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §19.1–19.2.
- **Objective:** Register AI task-verification nodes.
- **In scope:** Capture identity, stake, software, availability, performance and conflict declaration.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Verifier registration service.
- **Acceptance checks:** Task-verifier identity distinct from blockchain validator; eligibility uses approved policy; separate stake/reward accounting.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-NODES-001.

### WP-VERIFY-NODES-003 — Conflict-of-interest, ownership and exclusion rules

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §19.3,§28.
- **Objective:** Exclude conflicted or commonly controlled committee members.
- **In scope:** Model owner linkage, provider/customer relations, prior membership, conflicts and auditable exclusions.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Conflict screening policy.
- **Acceptance checks:** Each exclusion has evidence; privacy minimized; alias change cannot bypass ownership checks.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-NODES-001.

### WP-VERIFY-NODES-004 — Verifiable randomness and committee-selection proof

- **Type:** architecture-decision.
- **Primary owner:** feasibility-engineer.
- **Source:** §19.3.
- **Objective:** Specify auditable randomness source for selection.
- **In scope:** Compare beacon/chain/commit-reveal alternatives, bias resistance, timing and fallback; don't choose without approval.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Randomness ADR.
- **Acceptance checks:** Selection reproducible; bias risks, assumptions and fallback explicit.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-NODES-001.

### WP-VERIFY-NODES-005 — Two disjoint 100-member committees

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §19.3,§24,§25.
- **Objective:** Select first and independent audit committees.
- **In scope:** Enforce 100 eligible members each, zero overlap, owner constraints, random selection and membership snapshots.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Committee selection service.
- **Acceptance checks:** Both sets exactly 100; second set no overlap; identities/proof persisted; smaller sets not called complete.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-NODES-001.

### WP-VERIFY-NODES-006 — Committee capacity, absence and replacement fallback

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §19.3,§25,§31.6.
- **Objective:** Handle insufficient capacity and nonresponding selected members.
- **In scope:** Manage pending, availability, replacement, timeout and re-selection preserving independence.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Capacity/replacement state machine.
- **Acceptance checks:** Insufficient capacity remains Pending Verification; no-response not valid vote; replacement is unbiased/auditable.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-NODES-001.

### WP-VERIFY-NODES-007 — Verifier dashboard, assignments and reward history

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §19.1–19.2.
- **Objective:** Specify verifier work queue and performance view.
- **In scope:** Present eligibility, stake, pending/completed review, correctness, reward, penalty and history.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Verifier dashboard contract.
- **Acceptance checks:** Metrics link to evidence; conflicted/ineligible tasks not assignable; states distinct.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-NODES-001.

### WP-REPUTATION-002 — Reputation formulas, decimal precision and rounding

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§20.2–20.7,31.
- **Objective:** Make formulas and monetary units unambiguous.
- **In scope:** Define C/P/G/B/D, fee exclusion, asset precision, rounding, dust, Good=0 and overflow.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Formula spec/golden vectors.
- **Acceptance checks:** Section 20 examples reproduce; ten percentage points apply to C; conservation/remainder rule explicit.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REPUTATION-001.

### WP-REPUTATION-003 — Popularity snapshot and order-time immutability

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§20.1–20.5,23.
- **Objective:** Freeze provider P at order acceptance.
- **In scope:** Enforce 10–70 range; snapshot value/version/time; prevent later edits and races.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Immutable snapshot.
- **Acceptance checks:** Out-of-range rejected; accepted order has one immutable P; later edits do not affect prior orders.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REPUTATION-001.

### WP-REPUTATION-004 — Good/Bad ledger allocations and reconciliation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§20.3–20.6,23.
- **Objective:** Post auditable Good and Bad allocation records.
- **In scope:** Implement formulas; bind to order/payment; prevent duplicate posting; reconcile totals.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Reputation ledger processor.
- **Acceptance checks:** Good+Bad+Remaining reconciles to eligible C subject to approved rounding; retries not duplicated.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REPUTATION-001.

### WP-REPUTATION-005 — Reputation lock, release and dispute interaction

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §20.6,§§22–26,31.
- **Objective:** Protect locked reputation balances and release conditions.
- **In scope:** Model locked/unlocked states only under approved policy; freeze disputes; require authorized release; no automatic burn.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Lock policy/security controls.
- **Acceptance checks:** Locked funds not spendable; release requires approved condition; no burn/slash without authority/evidence.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REPUTATION-001.

### WP-REPUTATION-006 — Reputation overview, history and No Feedback display

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §§8,20,22.
- **Objective:** Make Good/Bad and ratio comprehensible.
- **In scope:** Display balances, N/A when Good=0, history, P, locks and pending feedback.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Reputation UI contract.
- **Acceptance checks:** Units/status clear; N/A not zero; pending feedback not mislabelled.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-REPUTATION-001.

### WP-SETTLEMENT-RECORD-002 — Canonical settlement schema and field ownership

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §23.
- **Objective:** Define typed Project Settlement Record schema.
- **In scope:** Map every field to owner, type, source of truth, mutability, privacy class and nullable semantics.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Canonical schema/field dictionary.
- **Acceptance checks:** All Section 23 groups/fields represented; each field has authoritative source and classification.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001.

### WP-SETTLEMENT-RECORD-003 — Canonical serialization, version and SHA-256 hash

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§21,23,24.
- **Objective:** Create deterministic serialization and versioned hash.
- **In scope:** Define field ordering/encoding, canonicalization, version increment, hash, manifest inclusion and mutation semantics.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Serializer/hash service.
- **Acceptance checks:** Same version hashes identically; signed-field change creates new hash; null/default encoding tested.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001.

### WP-SETTLEMENT-RECORD-004 — Private storage versus on-chain commitment boundary

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§21,23.5,23.12,28.
- **Objective:** Specify private record fields and minimal public commitments.
- **In scope:** Classify prompts, customer identity, files, links, financials, hashes, signatures and identifiers.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** On/off-chain classification.
- **Acceptance checks:** No personal data/prompt/file/private URL public; each on-chain field justified; public references cannot enumerate private objects.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001.

### WP-SETTLEMENT-RECORD-005 — Signature envelopes and evidence references

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§23.7–23.10,24.
- **Objective:** Bind signatures and evidence hashes to precise record versions.
- **In scope:** Define signer role, public key ref, algorithm decision slot, committee ID, vote, evidence hash and timestamp.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Signature envelope/API.
- **Acceptance checks:** Signature verifies exact version and actor role; mutation invalidates former signature; unsupported algorithm fails closed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001.

### WP-SETTLEMENT-RECORD-006 — Settlement record lifecycle and transition validator

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §23.11,§§24–26.
- **Objective:** Validate allowed record statuses and legal transitions.
- **In scope:** Model Created through payment, processing, delivery, feedback, verification, approved/disputed/frozen, settled/refunded/closed.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Transition table/model tests.
- **Acceptance checks:** Each state has valid transitions; illegal transition rejected; Frozen blocks payout; terminal state cannot silently reopen.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001.

### WP-VERIFY-STAGE1-002 — First-stage evidence package and snapshot

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§23.7,24.1.
- **Objective:** Assemble evidence for each first-stage reviewer.
- **In scope:** Include order/payment/P/Good-Bad/delivery/hash/rewards/record version and provenance.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Stage-one manifest.
- **Acceptance checks:** All review fields present and bound to one immutable version; sensitive data minimized.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001.

### WP-VERIFY-STAGE1-003 — Verifier review workflow and decision capture

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer.
- **Source:** §24.1.
- **Objective:** Specify reviewer inspect/decide/submit flow.
- **In scope:** Define assignment, evidence viewer, checklist, vote/reason, evidence ref and confirmation.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Review workflow.
- **Acceptance checks:** Reviewer sees record version/evidence; vote cannot target another version; incomplete review not valid.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001.

### WP-VERIFY-STAGE1-004 — Signed vote validation and duplicate-vote prevention

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §24.2.
- **Objective:** Validate votes against membership and record snapshot.
- **In scope:** Check signer, membership, version/hash, vote, evidence, time and uniqueness.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Vote validation service.
- **Acceptance checks:** One valid vote per member/committee/version; invalid signature/member/version rejected; replay idempotent.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001.

### WP-VERIFY-STAGE1-005 — 80/20 tally, closure and boundary tests

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §24.3–24.4.
- **Objective:** Implement/test first-stage threshold and automatic closure.
- **In scope:** Require 100 valid votes; accept >=80 approvals; absent votes not counted; test boundaries.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Threshold evaluator/test report.
- **Acceptance checks:** 79 fails; 80 passes; 100 passes; invalid/missing votes do not inflate count; protocol closes stage.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE1-001.

### WP-VERIFY-STAGE2-002 — Second-stage audit evidence package

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§23.8,25.
- **Objective:** Assemble evidence to audit stage one, not repeat it.
- **In scope:** Include first selection proof, disjointness, votes/signatures, tally, formulas, contract and version hash.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Audit manifest.
- **Acceptance checks:** Each Section 25 audit point is verifiable from evidence on same immutable version.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001.

### WP-VERIFY-STAGE2-003 — Committee disjointness and independence proof

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§19.3,25.
- **Objective:** Prove audit set independent from first committee.
- **In scope:** Compare identities/owners, prior membership, conflict declarations, randomness and exclusions.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Independence report.
- **Acceptance checks:** Intersection empty; shared ownership/conflicts checked; unsupported assumptions labelled.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001.

### WP-VERIFY-STAGE2-004 — 90/10 audit tally and vote integrity

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §25.1.
- **Objective:** Apply second-stage threshold to exactly 100 valid votes.
- **In scope:** Validate membership/signature/version; count approvals/rejections; enforce 90 minimum.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Audit threshold tests.
- **Acceptance checks:** 89 fails; 90 passes; missing votes not approvals; duplicates/invalid signatures excluded.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001.

### WP-VERIFY-STAGE2-005 — Frozen state, dispute and re-review handoff

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §25.2,§31.3,31.6.
- **Objective:** Freeze settlement and route failed audits to controlled review.
- **In scope:** Block release; record cause/evidence; create dispute/re-review; choose new committee only under approved rules.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Frozen/re-review workflow.
- **Acceptance checks:** Failed audit blocks payout; unfreeze requires authorized outcome; no silent restart with same committee.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-VERIFY-STAGE2-001.

### WP-SETTLEMENT-FINAL-002 — Final-settlement eligibility guard

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §26.
- **Objective:** Require payment and both verification stages before settlement.
- **In scope:** Validate order/record version, stage results, Frozen/dispute/refund flags, escrow and finality.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Eligibility guard/invariant tests.
- **Acceptance checks:** Any missing/failed verification or active freeze blocks settlement; guard is authoritative.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001.

### WP-SETTLEMENT-FINAL-003 — Deterministic payout calculation and reconciliation

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §§8,20,23,26,31.
- **Objective:** Define deterministic calculation of every payout component.
- **In scope:** Map gross, Reputation, fee, provider, owner, compute, verifier, validator, treasury, refund and remainder; leave ratios open.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Payout formula spec/golden vectors.
- **Acceptance checks:** Every amount has source formula/unit; totals reconcile; unknown percentages block unsupported calculation.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001.

### WP-SETTLEMENT-FINAL-004 — Idempotent payout execution and transaction journal

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §26.
- **Objective:** Execute authorized payouts exactly once despite retries.
- **In scope:** Use settlement idempotency, durable journal, status reconciliation, outbox and retry-safe transitions.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Payout engine/journal.
- **Acceptance checks:** Repeated requests cannot pay twice; uncertain external outcome reconciled before retry; journal tamper-evident.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001.

### WP-SETTLEMENT-FINAL-005 — Escrow release and partial-failure recovery

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§12,13,25,26.
- **Objective:** Release only authorized funds and recover from partial distribution.
- **In scope:** Define release order, partial completion, retry/compensation and refund constraints.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Escrow/release state machine.
- **Acceptance checks:** No early release; partial failure visible/resumable; irreversible transfers not called reversible; totals conserved.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001.

### WP-SETTLEMENT-FINAL-006 — Final hash, completion event and reconciliation

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §23.10–23.12,§26.
- **Objective:** Close settlement with verifiable terminal evidence.
- **In scope:** Generate final hash, attach chain tx/block/finality, verify payouts/reputation/fees and mark complete only after reconciliation.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Final verification suite.
- **Acceptance checks:** Hash matches canonical record; all outputs reconcile; finality evidenced; duplicate/missing event prevents Completed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001.

### WP-PROTOCOL-REWARDS-002 — Protocol-year clock and completed-year calculation

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §27.3.
- **Objective:** Derive protocol year from chain state, not local clocks.
- **In scope:** Map genesis/start, block height, year boundaries and reorg handling.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Protocol time service.
- **Acceptance checks:** All nodes derive same year from canonical chain; local clock cannot change emission period.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001.

### WP-PROTOCOL-REWARDS-003 — Emission multiplier, base reward and supply constraints

- **Type:** specification.
- **Primary owner:** feasibility-engineer.
- **Source:** §27.2–27.4,31.4.
- **Objective:** Formalize linear multiplier without inventing base issuance.
- **In scope:** Represent max(0,100−5×years), base amount, precision, cap and activation height as parameters.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Emission formula specification.
- **Acceptance checks:** Years 0–20 match schedule; year 10=50%, year 20=0%; unknown base/cap stay open.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001.

### WP-PROTOCOL-REWARDS-004 — Protocol reward role split and eligibility

- **Type:** economics.
- **Primary owner:** feasibility-engineer.
- **Source:** §§27.5–27.7.
- **Objective:** Define validator/verifier distribution categories.
- **In scope:** Model eligible duties, uptime, valid review, missed duty, conflicts and appeals without conflating order revenue.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Role allocation spec.
- **Acceptance checks:** Only evidenced eligible work rewarded; fees/order rewards distinct; split stays unapproved until owner decision.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001.

### WP-PROTOCOL-REWARDS-005 — Reward accrual, claim and audit integration

- **Type:** implementation.
- **Primary owner:** execution-engineer.
- **Source:** §§8,15,18,19,27.
- **Objective:** Record protocol rewards and make them auditable/claimable.
- **In scope:** Bind emission period, role identity, duty evidence, amount, claim state and chain event.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Reward ledger integration.
- **Acceptance checks:** Each reward references valid event/duty; replay cannot duplicate claim; role ledgers remain distinct.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001.

### WP-PROTOCOL-REWARDS-006 — Emission simulation and adversarial economic review

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer.
- **Source:** §27,§§29–31.
- **Objective:** Simulate reward outcomes under participation assumptions.
- **In scope:** Test node counts, concentration, year boundaries, fees, incentive decay and supply scenarios.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Simulation report.
- **Acceptance checks:** Assumptions/sources disclosed; not a forecast/guarantee; risks and approvals listed.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001.

### WP-SECURITY-002 — Threat model, asset inventory and trust boundaries

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§1.2,6.2,9,14,17,21,23,28,29.
- **Objective:** Create cross-system threat model and actor/asset inventory.
- **In scope:** Map users/devices/owners/compute/providers/customers/validators/verifiers/platform/storage/chain; enumerate trust transitions.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Threat model/asset register.
- **Acceptance checks:** Sensitive assets/trust boundary have owner, threat, impact and control status.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-SECURITY-003 — Secrets, key separation and signing policy

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§15,16,18,19,24,28.
- **Objective:** Define protection, rotation and use of all role secrets.
- **In scope:** Classify wallet/node/validator/verifier/owner/infra secrets; define generation, storage, signing, recovery and revocation.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Key management policy.
- **Acceptance checks:** Keys purpose-separated; secrets never logged/plaintext; recovery/revocation testable; custody choices approval-gated.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-SECURITY-004 — Software/model provenance and secure updates

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§2,4,5,28.
- **Objective:** Protect app/models from tampered sources and unsafe update.
- **In scope:** Define signed manifests, allowlists, pinned versions, integrity, update auth, rollback and supply-chain response.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Supply-chain policy.
- **Acceptance checks:** Only verified artifacts eligible; authenticity before activation; rollback does not silently restore vulnerable content.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-SECURITY-005 — Sandboxing, resource isolation and prompt injection

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§5,6.2,9,28.
- **Objective:** Restrict untrusted model/input/peer execution and resource access.
- **In scope:** Define isolation, file/network permissions, quotas, prompt boundaries and malicious-input tests.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Isolation/security requirements.
- **Acceptance checks:** Untrusted data cannot become privileged instruction; runtime cannot access unrelated secrets; exhaustion bounded.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-SECURITY-006 — Node communication and intermediate-data privacy

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§1.2,9–11,14,28.1–28.2.
- **Objective:** Define authenticated communication and data visibility accurately.
- **In scope:** Specify channel auth/encryption, replay protection, minimization, transient storage and customer disclosure of what nodes can see.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Network security/privacy spec.
- **Acceptance checks:** Transport encryption is not misrepresented as hiding plaintext from compute nodes; exposure disclosed; replay/impersonation tested.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-SECURITY-007 — Storage, download authorization and data retention

- **Type:** security.
- **Primary owner:** safety-engineer.
- **Source:** §§21,23,28.4.
- **Objective:** Unify storage, private access, logs and retention.
- **In scope:** Classify files/logs/inputs/prompts/settlement; define encryption, ACL, audit, expiry/deletion and backup.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Data lifecycle/control matrix.
- **Acceptance checks:** No public/private confusion; server-side access; retention is not invented; logs minimize sensitive data.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-SECURITY-008 — Security monitoring, incident response and recovery

- **Type:** operations.
- **Primary owner:** safety-engineer.
- **Source:** §§11,28,29.
- **Objective:** Define detection, containment and recovery for named attacks/failures.
- **In scope:** Cover Sybil, double spend, impersonation, replay, malicious nodes, collusion, DoS, partition, invalid results and owner failure.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Security runbook/exercise plan.
- **Acceptance checks:** Each threat has signal, owner, containment and recovery; exercises repeatable; residual risks approved by authority.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-SECURITY-001.

### WP-MAINNET-READINESS-002 — Requirements-to-release traceability and integration matrix

- **Type:** integration.
- **Primary owner:** project-mapping-engineer.
- **Source:** §§3–27,30.
- **Objective:** Map source requirements to tasks/components/interfaces/release evidence.
- **In scope:** Identify critical end-to-end paths, contracts, owners, integration sequence and blockers.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Integration traceability matrix.
- **Acceptance checks:** Every requirement maps to acceptance/evidence; no critical interface orphan; phase order remains advisory.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MAINNET-READINESS-001.

### WP-MAINNET-READINESS-003 — Performance, capacity and distributed benchmark program

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer.
- **Source:** §§5,9–11,29–30.
- **Objective:** Define reproducible benchmarks for local and distributed AI.
- **In scope:** Measure startup/inference latency, throughput, transfer, imbalance, memory, degradation and recovery.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Benchmark protocol/results.
- **Acceptance checks:** Claims include environment/model/workload/repeatability; no data-center equivalence without evidence.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MAINNET-READINESS-001.

### WP-MAINNET-READINESS-004 — Failure injection, resilience and recovery acceptance

- **Type:** testing.
- **Primary owner:** qa-testing-engineer.
- **Source:** §§11,13,21,24–26,28–30.
- **Objective:** Test recovery from node, storage, payment, committee and settlement failures.
- **In scope:** Inject node loss, partition, timeout, corrupt artifact, duplicate webhook, absent committee, storage and partial payout failure.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Resilience test suite.
- **Acceptance checks:** Each scenario defines safe state, no duplicate side effects, recovery and actual evidence; severe unresolved failure blocks readiness.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MAINNET-READINESS-001.

### WP-MAINNET-READINESS-005 — Independent security review and remediation gate

- **Type:** governance.
- **Primary owner:** safety-engineer.
- **Source:** §§28–31.
- **Objective:** Require independent security review before public release.
- **In scope:** Define scope, reviewer qualifications, finding severity, remediation, retest and residual-risk approval.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Security audit plan/sign-off register.
- **Acceptance checks:** Critical/high issues block readiness absent verified remediation/authorized exception; self-review is not independent audit.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MAINNET-READINESS-001.

### WP-MAINNET-READINESS-006 — Economic, legal and operational decisions

- **Type:** governance.
- **Primary owner:** feasibility-engineer.
- **Source:** §§15,27,29,31.
- **Objective:** Collect qualified decisions for tokenomics/payments/custody/jurisdiction/operations.
- **In scope:** Record coin classification, exchange/payment obligations, custody, fee/emission/stake parameters, support, incident response and retention.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Decision package/owner matrix.
- **Acceptance checks:** No legal conclusion invented; approvals have evidence, jurisdiction, owner and effective date; unresolved approvals block launch.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MAINNET-READINESS-001.

### WP-MAINNET-READINESS-007 — Launch checklist, staged rollout and rollback

- **Type:** operations.
- **Primary owner:** execution-engineer.
- **Source:** §30.
- **Objective:** Define controlled release and rollback.
- **In scope:** Set environment promotion, feature flags, rollout cohort, chain genesis/upgrade, backups, monitoring, stop criteria and irreversible-chain constraints.
- **Out of scope:** Unapproved behavior/technology/policy; unrelated refactors; silent resolution of open decisions.
- **Required output:** Release runbook/go-no-go checklist.
- **Acceptance checks:** Release blocked while mandatory gates fail; rollback/stop criteria testable; user-fund safety explicit.
- **Verification evidence:** Reproducible tests/checks, schema/contract review, sample inputs/outputs and actual results appropriate to task type. A plan/empty placeholder is not implementation evidence.
- **Direct prerequisites:** WP-MAINNET-READINESS-001.


## Source-to-work-package traceability

| Source scope | Domain baseline | Granular work packages |
|---|---|---|
| Introductory purpose/scope | WP-ARCH-001, WP-MODEL-001, WP-SECURITY-001 | WP-ARCH-002–006; WP-MODEL-002–006; WP-SECURITY-002–008 |
| §1 architecture/pipeline | WP-ARCH-001, WP-NET-CREATE-001 | WP-ARCH-002–006; WP-NET-CREATE-002–006 |
| §2 platform principles | WP-APP-001, WP-MODEL-001, WP-AI-LOCAL-001 | WP-APP-002–007; WP-MODEL-002–006; WP-AI-LOCAL-002–006 |
| §3 UI/navigation | WP-APP-001, WP-WALLET-001, WP-AI-HISTORY-001 | WP-APP-002–007; WP-WALLET-007; WP-AI-HISTORY-002–004 |
| §4 catalogue/licensing | WP-MODEL-001 | WP-MODEL-002–006 |
| §5 local inference | WP-AI-LOCAL-001 | WP-AI-LOCAL-002–006 |
| §6 task authoring/prompt | WP-AI-TASK-001, WP-SECURITY-001 | WP-AI-TASK-002–005; WP-SECURITY-005 |
| §7 history | WP-AI-HISTORY-001 | WP-AI-HISTORY-002–004 |
| §8 rewards | WP-REWARD-001, WP-REPUTATION-001 | WP-REWARD-002–005; WP-REPUTATION-002–006 |
| §9 network creation | WP-NET-CREATE-001, WP-IDENTITY-001 | WP-NET-CREATE-002–006; WP-IDENTITY-002–006 |
| §10 joining | WP-NET-JOIN-001, WP-IDENTITY-001 | WP-NET-JOIN-002–005; WP-IDENTITY-002–006 |
| §11 network operations | WP-NET-OPS-001 | WP-NET-OPS-002–007 |
| §12 marketplace | WP-MARKET-001, WP-ORDER-001 | WP-MARKET-002–006; WP-ORDER-002–009 |
| §13 order/delivery/feedback | WP-ORDER-001, WP-DELIVERY-001, WP-FEEDBACK-001 | WP-ORDER-002–009; WP-DELIVERY-002–007; WP-FEEDBACK-002–004 |
| §14 network architecture | WP-ARCH-001, WP-IDENTITY-001, WP-CHAIN-001 | WP-ARCH-002–006; WP-IDENTITY-002–006; WP-CHAIN-002–007 |
| §15 blockchain/coin | WP-CHAIN-001, WP-REWARD-001, WP-WALLET-001 | WP-CHAIN-002–007; WP-REWARD-002–005; WP-WALLET-002–007 |
| §16 wallet | WP-WALLET-001 | WP-WALLET-002–007 |
| §17 node roles | WP-IDENTITY-001, WP-VALIDATOR-001, WP-VERIFY-NODES-001 | WP-IDENTITY-002–006; WP-VALIDATOR-002–005; WP-VERIFY-NODES-002–007 |
| §18 Validator Center | WP-VALIDATOR-001 | WP-VALIDATOR-002–005 |
| §19 committees | WP-VERIFY-NODES-001 | WP-VERIFY-NODES-002–007 |
| §20 Reputation | WP-REPUTATION-001 | WP-REPUTATION-002–006 |
| §21 private delivery | WP-DELIVERY-001, WP-SECURITY-001 | WP-DELIVERY-002–007; WP-SECURITY-007 |
| §22 feedback | WP-FEEDBACK-001, WP-REPUTATION-001 | WP-FEEDBACK-002–004; WP-REPUTATION-002–006 |
| §23 settlement record | WP-SETTLEMENT-RECORD-001 | WP-SETTLEMENT-RECORD-002–006 |
| §24 80/20 | WP-VERIFY-STAGE1-001 | WP-VERIFY-STAGE1-002–005 |
| §25 90/10 | WP-VERIFY-STAGE2-001 | WP-VERIFY-STAGE2-002–005 |
| §26 final settlement | WP-SETTLEMENT-FINAL-001 | WP-SETTLEMENT-FINAL-002–006 |
| §27 incentives | WP-PROTOCOL-REWARDS-001, WP-REWARD-001 | WP-PROTOCOL-REWARDS-002–006; WP-REWARD-002–005 |
| §28 security/privacy | WP-SECURITY-001 and feature baselines | WP-SECURITY-002–008 plus feature-specific security acceptance |
| §29 risks | WP-ARCH-001, WP-NET-OPS-001, WP-SECURITY-001, WP-MAINNET-READINESS-001 | WP-ARCH-006; WP-NET-OPS-004–007; WP-SECURITY-002–008; WP-MAINNET-READINESS-003–006 |
| §30 proposed phases | WP-MAINNET-READINESS-001 | WP-MAINNET-READINESS-002–007; order advisory |
| §31 open decisions | Relevant baselines and WP-MAINNET-READINESS-006 | Domain ADR/governance/approval child tasks |
| §32 final vision/settlement | WP-ARCH-001, WP-SETTLEMENT-RECORD-001, WP-SETTLEMENT-FINAL-001 | WP-ARCH-004–006; WP-SETTLEMENT-RECORD-002–006; WP-SETTLEMENT-FINAL-002–006 |


## Consolidated open-decision register

1. AI model family/modalities, runtime, partition granularity, Tensor Parallelism and hardware matrix.
2. Model-by-model licensing and distribution/commercial rights.
3. Provider registry topology, ranking/moderation, availability freshness and ETA.
4. FX source/expiry, external-payment evidence and payment-provider constraints.
5. Escrow, cancel/refund, dispute authority and review deadlines.
6. Wallet custody, key recovery and regulatory obligations.
7. Consensus/finality, supply, coin utility, platform fee, base reward and fee split.
8. Randomness, identity/ownership, Sybil/collusion controls, committee replacement and re-review.
9. Validator/verifier stake, duties, unbonding and penalties.
10. No Feedback disposition; Reputation release/burn/transfer; Frozen resolution.
11. Reputation precision/rounding/dust and remainder handling.
12. Data retention, storage topology, intermediate-data privacy and confidential computing.
13. Jurisdictions, native-coin status, exchange/payment rules and mainnet authority.

Each decision needs owner, alternatives, evidence, impact, state and approval date.


## Work-package standards

- Each task has one primary owner, one coherent outcome, explicit scope/exclusions, deliverable and testable acceptance evidence.
- A specification task is accepted on a reviewed contract; implementation requires working behavior; QA requires executed reproducible tests; operations requires a runbook and exercise evidence.
- Every task traces to source sections and a domain baseline. Cross-cutting security does not remove feature-specific security acceptance.
- A task is not done because its directory/log exists. Graph status is the scheduler authority.
- Create child workspaces only after Senior Engineer selection.
- Do not turn Section 30's preferred phase order into dependencies unless a concrete output/contract is required.
- Do not invent timelines, prices, thresholds, technologies, licences, legal rules or economic parameters.



## WP-INIT-003 — Decompose granular work packages into execution-level tasks

- **Status:** Completed as a planning/decomposition task; WP-INIT-001 and WP-INIT-002 remain unchanged and completed.
- **Objective:** Decompose all 137 existing granular child work packages into independently verifiable execution-level tasks, preserve all prior task IDs, formalize parent roll-up acceptance and connect only real blocking prerequisites.
- **Type:** planning/decomposition.
- **Primary owner:** senior-engineer.
- **Direct prerequisites:** WP-INIT-002.
- **Source:** Production/task-decomposition/main-document.md (introductory material and all Sections 1–32); existing catalog, graph, prompts, histories, baseline reports and current repository tree.
- **Scope:** Re-inspect online main; map each existing child package to two or more focused tasks; give every new task a unique ID, one primary owner, task type, source subsections, objective, in-scope work, exclusions, deliverable, testable acceptance, verification evidence and direct prerequisites; update parent roll-up edges; validate graph/catalog/path integrity.
- **Exclusions:** Reopening or rewriting WP-INIT-001/WP-INIT-002; modifying the source specification; implementing application/runtime/blockchain features; creating child workspaces; choosing unapproved technologies, licensing, custody, consensus, economic, legal or governance policy; inventing estimates.
- **Output:** Four execution-level work-breakdown files with 280 new work packages, 447-node task graph, expanded catalog and WP-INIT-003 status/role records.
- **Acceptance:** All 137 existing granular packages are represented in the parent map; all 280 new IDs are unique and catalog/graph-equal; exact three-key graph schema; no unknown/self/duplicate prerequisite or cycle; parent roll-ups wait for all their leaf tasks; every leaf's direct prerequisites exclude its own parent grouping and include WP-INIT-003; all open decisions remain open; only Production/Development paths change.
- **Task model:** The 27 `WP-DOMAIN-001` IDs remain domain specification gates. Existing 137 `WP-DOMAIN-NNN` children become intermediate roll-up packages. The 280 new `WP-DOMAIN-NNN` leaves are the next execution level. A parent/child membership is not itself a prerequisite; the parent depends on every child for completion, while each child depends on the actual domain prerequisite(s) plus WP-INIT-003.
- **Initial execution state:** All 280 new tasks are `not_started`; defining a task is not evidence that it has started or been implemented.

## Execution-level work breakdown files

| File | Scope | Parent packages | New tasks |
|---|---|---:|---:|
| [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md) | Architecture, Windows desktop, model catalogue, local AI, Defined Tasks and history | 28 | 61 |
| [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md) | Rewards, compute-network creation/join/operations and marketplace | 24 | 48 |
| [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md) | Orders, payments, delivery, feedback, identity, Reputation, verification stages and settlement | 45 | 91 |
| [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md) | Blockchain, wallet, validators, verification nodes, protocol rewards, security and mainnet readiness | 40 | 80 |

## Parent-to-execution-child roll-up register

| Existing granular parent | New execution-level child IDs | Count |
|---|---|---:|
| WP-AI-HISTORY-002 | WP-AI-HISTORY-005, WP-AI-HISTORY-006 | 2 |
| WP-AI-HISTORY-003 | WP-AI-HISTORY-007, WP-AI-HISTORY-008 | 2 |
| WP-AI-HISTORY-004 | WP-AI-HISTORY-009, WP-AI-HISTORY-010 | 2 |
| WP-AI-LOCAL-002 | WP-AI-LOCAL-007, WP-AI-LOCAL-008 | 2 |
| WP-AI-LOCAL-003 | WP-AI-LOCAL-009, WP-AI-LOCAL-010 | 2 |
| WP-AI-LOCAL-004 | WP-AI-LOCAL-011, WP-AI-LOCAL-012, WP-AI-LOCAL-013 | 3 |
| WP-AI-LOCAL-005 | WP-AI-LOCAL-014, WP-AI-LOCAL-015, WP-AI-LOCAL-016 | 3 |
| WP-AI-LOCAL-006 | WP-AI-LOCAL-017, WP-AI-LOCAL-018 | 2 |
| WP-AI-TASK-002 | WP-AI-TASK-006, WP-AI-TASK-007 | 2 |
| WP-AI-TASK-003 | WP-AI-TASK-008, WP-AI-TASK-009 | 2 |
| WP-AI-TASK-004 | WP-AI-TASK-010, WP-AI-TASK-011 | 2 |
| WP-AI-TASK-005 | WP-AI-TASK-012, WP-AI-TASK-013 | 2 |
| WP-APP-002 | WP-APP-008, WP-APP-009 | 2 |
| WP-APP-003 | WP-APP-010, WP-APP-011 | 2 |
| WP-APP-004 | WP-APP-012, WP-APP-013 | 2 |
| WP-APP-005 | WP-APP-014, WP-APP-015 | 2 |
| WP-APP-006 | WP-APP-016, WP-APP-017 | 2 |
| WP-APP-007 | WP-APP-018, WP-APP-019 | 2 |
| WP-ARCH-002 | WP-ARCH-007, WP-ARCH-008 | 2 |
| WP-ARCH-003 | WP-ARCH-009, WP-ARCH-010 | 2 |
| WP-ARCH-004 | WP-ARCH-011, WP-ARCH-012, WP-ARCH-013, WP-ARCH-014 | 4 |
| WP-ARCH-005 | WP-ARCH-015, WP-ARCH-016, WP-ARCH-017 | 3 |
| WP-ARCH-006 | WP-ARCH-018, WP-ARCH-019 | 2 |
| WP-CHAIN-002 | WP-CHAIN-008, WP-CHAIN-009 | 2 |
| WP-CHAIN-003 | WP-CHAIN-010, WP-CHAIN-011 | 2 |
| WP-CHAIN-004 | WP-CHAIN-012, WP-CHAIN-013 | 2 |
| WP-CHAIN-005 | WP-CHAIN-014, WP-CHAIN-015 | 2 |
| WP-CHAIN-006 | WP-CHAIN-016, WP-CHAIN-017 | 2 |
| WP-CHAIN-007 | WP-CHAIN-018, WP-CHAIN-019 | 2 |
| WP-DELIVERY-002 | WP-DELIVERY-008, WP-DELIVERY-009 | 2 |
| WP-DELIVERY-003 | WP-DELIVERY-010, WP-DELIVERY-011 | 2 |
| WP-DELIVERY-004 | WP-DELIVERY-012, WP-DELIVERY-013 | 2 |
| WP-DELIVERY-005 | WP-DELIVERY-014, WP-DELIVERY-015 | 2 |
| WP-DELIVERY-006 | WP-DELIVERY-016, WP-DELIVERY-017 | 2 |
| WP-DELIVERY-007 | WP-DELIVERY-018, WP-DELIVERY-019 | 2 |
| WP-FEEDBACK-002 | WP-FEEDBACK-005, WP-FEEDBACK-006 | 2 |
| WP-FEEDBACK-003 | WP-FEEDBACK-007, WP-FEEDBACK-008 | 2 |
| WP-FEEDBACK-004 | WP-FEEDBACK-009, WP-FEEDBACK-010 | 2 |
| WP-IDENTITY-002 | WP-IDENTITY-007, WP-IDENTITY-008 | 2 |
| WP-IDENTITY-003 | WP-IDENTITY-009, WP-IDENTITY-010 | 2 |
| WP-IDENTITY-004 | WP-IDENTITY-011, WP-IDENTITY-012 | 2 |
| WP-IDENTITY-005 | WP-IDENTITY-013, WP-IDENTITY-014 | 2 |
| WP-IDENTITY-006 | WP-IDENTITY-015, WP-IDENTITY-016 | 2 |
| WP-MAINNET-READINESS-002 | WP-MAINNET-READINESS-008, WP-MAINNET-READINESS-009 | 2 |
| WP-MAINNET-READINESS-003 | WP-MAINNET-READINESS-010, WP-MAINNET-READINESS-011 | 2 |
| WP-MAINNET-READINESS-004 | WP-MAINNET-READINESS-012, WP-MAINNET-READINESS-013 | 2 |
| WP-MAINNET-READINESS-005 | WP-MAINNET-READINESS-014, WP-MAINNET-READINESS-015 | 2 |
| WP-MAINNET-READINESS-006 | WP-MAINNET-READINESS-016, WP-MAINNET-READINESS-017 | 2 |
| WP-MAINNET-READINESS-007 | WP-MAINNET-READINESS-018, WP-MAINNET-READINESS-019 | 2 |
| WP-MARKET-002 | WP-MARKET-007, WP-MARKET-008 | 2 |
| WP-MARKET-003 | WP-MARKET-009, WP-MARKET-010 | 2 |
| WP-MARKET-004 | WP-MARKET-011, WP-MARKET-012 | 2 |
| WP-MARKET-005 | WP-MARKET-013, WP-MARKET-014 | 2 |
| WP-MARKET-006 | WP-MARKET-015, WP-MARKET-016 | 2 |
| WP-MODEL-002 | WP-MODEL-007, WP-MODEL-008 | 2 |
| WP-MODEL-003 | WP-MODEL-009, WP-MODEL-010 | 2 |
| WP-MODEL-004 | WP-MODEL-011, WP-MODEL-012 | 2 |
| WP-MODEL-005 | WP-MODEL-013, WP-MODEL-014 | 2 |
| WP-MODEL-006 | WP-MODEL-015, WP-MODEL-016 | 2 |
| WP-NET-CREATE-002 | WP-NET-CREATE-007, WP-NET-CREATE-008 | 2 |
| WP-NET-CREATE-003 | WP-NET-CREATE-009, WP-NET-CREATE-010 | 2 |
| WP-NET-CREATE-004 | WP-NET-CREATE-011, WP-NET-CREATE-012 | 2 |
| WP-NET-CREATE-005 | WP-NET-CREATE-013, WP-NET-CREATE-014 | 2 |
| WP-NET-CREATE-006 | WP-NET-CREATE-015, WP-NET-CREATE-016 | 2 |
| WP-NET-JOIN-002 | WP-NET-JOIN-006, WP-NET-JOIN-007 | 2 |
| WP-NET-JOIN-003 | WP-NET-JOIN-008, WP-NET-JOIN-009 | 2 |
| WP-NET-JOIN-004 | WP-NET-JOIN-010, WP-NET-JOIN-011 | 2 |
| WP-NET-JOIN-005 | WP-NET-JOIN-012, WP-NET-JOIN-013 | 2 |
| WP-NET-OPS-002 | WP-NET-OPS-008, WP-NET-OPS-009 | 2 |
| WP-NET-OPS-003 | WP-NET-OPS-010, WP-NET-OPS-011 | 2 |
| WP-NET-OPS-004 | WP-NET-OPS-012, WP-NET-OPS-013 | 2 |
| WP-NET-OPS-005 | WP-NET-OPS-014, WP-NET-OPS-015 | 2 |
| WP-NET-OPS-006 | WP-NET-OPS-016, WP-NET-OPS-017 | 2 |
| WP-NET-OPS-007 | WP-NET-OPS-018, WP-NET-OPS-019 | 2 |
| WP-ORDER-002 | WP-ORDER-010, WP-ORDER-011 | 2 |
| WP-ORDER-003 | WP-ORDER-012, WP-ORDER-013 | 2 |
| WP-ORDER-004 | WP-ORDER-014, WP-ORDER-015 | 2 |
| WP-ORDER-005 | WP-ORDER-016, WP-ORDER-017 | 2 |
| WP-ORDER-006 | WP-ORDER-018, WP-ORDER-019, WP-ORDER-020 | 3 |
| WP-ORDER-007 | WP-ORDER-021, WP-ORDER-022 | 2 |
| WP-ORDER-008 | WP-ORDER-023, WP-ORDER-024 | 2 |
| WP-ORDER-009 | WP-ORDER-025, WP-ORDER-026 | 2 |
| WP-PROTOCOL-REWARDS-002 | WP-PROTOCOL-REWARDS-007, WP-PROTOCOL-REWARDS-008 | 2 |
| WP-PROTOCOL-REWARDS-003 | WP-PROTOCOL-REWARDS-009, WP-PROTOCOL-REWARDS-010 | 2 |
| WP-PROTOCOL-REWARDS-004 | WP-PROTOCOL-REWARDS-011, WP-PROTOCOL-REWARDS-012 | 2 |
| WP-PROTOCOL-REWARDS-005 | WP-PROTOCOL-REWARDS-013, WP-PROTOCOL-REWARDS-014 | 2 |
| WP-PROTOCOL-REWARDS-006 | WP-PROTOCOL-REWARDS-015, WP-PROTOCOL-REWARDS-016 | 2 |
| WP-REPUTATION-002 | WP-REPUTATION-007, WP-REPUTATION-008 | 2 |
| WP-REPUTATION-003 | WP-REPUTATION-009, WP-REPUTATION-010 | 2 |
| WP-REPUTATION-004 | WP-REPUTATION-011, WP-REPUTATION-012 | 2 |
| WP-REPUTATION-005 | WP-REPUTATION-013, WP-REPUTATION-014 | 2 |
| WP-REPUTATION-006 | WP-REPUTATION-015, WP-REPUTATION-016 | 2 |
| WP-REWARD-002 | WP-REWARD-006, WP-REWARD-007 | 2 |
| WP-REWARD-003 | WP-REWARD-008, WP-REWARD-009 | 2 |
| WP-REWARD-004 | WP-REWARD-010, WP-REWARD-011 | 2 |
| WP-REWARD-005 | WP-REWARD-012, WP-REWARD-013 | 2 |
| WP-SECURITY-002 | WP-SECURITY-009, WP-SECURITY-010 | 2 |
| WP-SECURITY-003 | WP-SECURITY-011, WP-SECURITY-012 | 2 |
| WP-SECURITY-004 | WP-SECURITY-013, WP-SECURITY-014 | 2 |
| WP-SECURITY-005 | WP-SECURITY-015, WP-SECURITY-016 | 2 |
| WP-SECURITY-006 | WP-SECURITY-017, WP-SECURITY-018 | 2 |
| WP-SECURITY-007 | WP-SECURITY-019, WP-SECURITY-020 | 2 |
| WP-SECURITY-008 | WP-SECURITY-021, WP-SECURITY-022 | 2 |
| WP-SETTLEMENT-FINAL-002 | WP-SETTLEMENT-FINAL-007, WP-SETTLEMENT-FINAL-008 | 2 |
| WP-SETTLEMENT-FINAL-003 | WP-SETTLEMENT-FINAL-009, WP-SETTLEMENT-FINAL-010 | 2 |
| WP-SETTLEMENT-FINAL-004 | WP-SETTLEMENT-FINAL-011, WP-SETTLEMENT-FINAL-012 | 2 |
| WP-SETTLEMENT-FINAL-005 | WP-SETTLEMENT-FINAL-013, WP-SETTLEMENT-FINAL-014 | 2 |
| WP-SETTLEMENT-FINAL-006 | WP-SETTLEMENT-FINAL-015, WP-SETTLEMENT-FINAL-016 | 2 |
| WP-SETTLEMENT-RECORD-002 | WP-SETTLEMENT-RECORD-007, WP-SETTLEMENT-RECORD-008 | 2 |
| WP-SETTLEMENT-RECORD-003 | WP-SETTLEMENT-RECORD-009, WP-SETTLEMENT-RECORD-010 | 2 |
| WP-SETTLEMENT-RECORD-004 | WP-SETTLEMENT-RECORD-011, WP-SETTLEMENT-RECORD-012 | 2 |
| WP-SETTLEMENT-RECORD-005 | WP-SETTLEMENT-RECORD-013, WP-SETTLEMENT-RECORD-014 | 2 |
| WP-SETTLEMENT-RECORD-006 | WP-SETTLEMENT-RECORD-015, WP-SETTLEMENT-RECORD-016 | 2 |
| WP-VALIDATOR-002 | WP-VALIDATOR-006, WP-VALIDATOR-007 | 2 |
| WP-VALIDATOR-003 | WP-VALIDATOR-008, WP-VALIDATOR-009 | 2 |
| WP-VALIDATOR-004 | WP-VALIDATOR-010, WP-VALIDATOR-011 | 2 |
| WP-VALIDATOR-005 | WP-VALIDATOR-012, WP-VALIDATOR-013 | 2 |
| WP-VERIFY-NODES-002 | WP-VERIFY-NODES-008, WP-VERIFY-NODES-009 | 2 |
| WP-VERIFY-NODES-003 | WP-VERIFY-NODES-010, WP-VERIFY-NODES-011 | 2 |
| WP-VERIFY-NODES-004 | WP-VERIFY-NODES-012, WP-VERIFY-NODES-013 | 2 |
| WP-VERIFY-NODES-005 | WP-VERIFY-NODES-014, WP-VERIFY-NODES-015 | 2 |
| WP-VERIFY-NODES-006 | WP-VERIFY-NODES-016, WP-VERIFY-NODES-017 | 2 |
| WP-VERIFY-NODES-007 | WP-VERIFY-NODES-018, WP-VERIFY-NODES-019 | 2 |
| WP-VERIFY-STAGE1-002 | WP-VERIFY-STAGE1-006, WP-VERIFY-STAGE1-007 | 2 |
| WP-VERIFY-STAGE1-003 | WP-VERIFY-STAGE1-008, WP-VERIFY-STAGE1-009 | 2 |
| WP-VERIFY-STAGE1-004 | WP-VERIFY-STAGE1-010, WP-VERIFY-STAGE1-011 | 2 |
| WP-VERIFY-STAGE1-005 | WP-VERIFY-STAGE1-012, WP-VERIFY-STAGE1-013 | 2 |
| WP-VERIFY-STAGE2-002 | WP-VERIFY-STAGE2-006, WP-VERIFY-STAGE2-007 | 2 |
| WP-VERIFY-STAGE2-003 | WP-VERIFY-STAGE2-008, WP-VERIFY-STAGE2-009 | 2 |
| WP-VERIFY-STAGE2-004 | WP-VERIFY-STAGE2-010, WP-VERIFY-STAGE2-011 | 2 |
| WP-VERIFY-STAGE2-005 | WP-VERIFY-STAGE2-012, WP-VERIFY-STAGE2-013 | 2 |
| WP-WALLET-002 | WP-WALLET-008, WP-WALLET-009 | 2 |
| WP-WALLET-003 | WP-WALLET-010, WP-WALLET-011 | 2 |
| WP-WALLET-004 | WP-WALLET-012, WP-WALLET-013 | 2 |
| WP-WALLET-005 | WP-WALLET-014, WP-WALLET-015 | 2 |
| WP-WALLET-006 | WP-WALLET-016, WP-WALLET-017 | 2 |
| WP-WALLET-007 | WP-WALLET-018, WP-WALLET-019 | 2 |

## Execution-level work-package catalogue

Each detailed task contract is stored in its listed part file. The summary below is the searchable catalog index; `Parent work package` identifies roll-up membership, not a child prerequisite.

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-ARCH-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-APP-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-MODEL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-LOCAL-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-TASK-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-AI-HISTORY-001, WP-INIT-003
- **Detailed contract:** [01-architecture-desktop-and-ai.md](execution-work-breakdown/01-architecture-desktop-and-ai.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-REWARD-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-CREATE-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-JOIN-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-NET-OPS-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-MARKET-001, WP-INIT-003
- **Detailed contract:** [02-compute-network-and-marketplace.md](execution-work-breakdown/02-compute-network-and-marketplace.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-ORDER-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-DELIVERY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-FEEDBACK-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-IDENTITY-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-REPUTATION-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-RECORD-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE1-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-VERIFY-STAGE2-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

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
- **Direct prerequisites:** WP-SETTLEMENT-FINAL-001, WP-INIT-003
- **Detailed contract:** [03-orders-delivery-identity-and-settlement.md](execution-work-breakdown/03-orders-delivery-identity-and-settlement.md)

### WP-CHAIN-008 — Consensus threat model and design criteria

- **Type:** architecture-decision.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-CHAIN-002
- **Source:** §15,§31.4.
- **Objective:** Define the security, decentralization and operational assumptions that any consensus candidate must satisfy.
- **In scope:** Specify adversary capabilities, network synchrony assumptions, validator powers, quorum assumptions, liveness/safety trade-offs and failure domains.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Consensus threat model and evaluation criteria.
- **Acceptance checks:** Every candidate is assessed against explicit assumptions; unknown network/validator parameters remain open; no mechanism is selected by implication.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-009 — Consensus/finality alternatives and owner decision record

- **Type:** architecture-decision.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-CHAIN-002
- **Source:** §15,§31.4.
- **Objective:** Compare viable consensus and finality approaches without choosing a protocol for the owner.
- **In scope:** Evaluate finality delay, reorganization risk, hardware/network demand, validator concentration, governance and recovery; document options and evidence gaps.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Consensus/finality architecture decision record.
- **Acceptance checks:** Trade-offs are evidence-backed; finality and reorg definitions are explicit; production selection remains blocked pending owner approval.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-010 — Peer identity handshake, protocol version and admission

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-CHAIN-003
- **Source:** §§14.2,15.1.
- **Objective:** Define authenticated connection establishment between blockchain peers.
- **In scope:** Specify peer identity proof, protocol/version negotiation, capability exchange, authorization, connection refusal and key rollover.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** P2P handshake and peer-admission contract.
- **Acceptance checks:** Only authenticated compatible peers are admitted; downgrade and unknown identity fail closed; no trust by IP or alias.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-011 — Gossip, synchronization, rate limits and partition recovery

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-CHAIN-003
- **Source:** §§14.2,15.1.
- **Objective:** Specify message propagation and synchronization under normal and degraded network conditions.
- **In scope:** Define message envelope, duplicate suppression, sync checkpoints, resource caps, partition detection and reconnect behavior.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** P2P propagation/sync protocol and failure matrix.
- **Acceptance checks:** Messages are replay/dedup safe; resource use bounded; partition recovery does not silently accept conflicting chain history.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-012 — Transaction canonical format, signature and nonce validation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-CHAIN-004
- **Source:** §15.1,§28.5.
- **Objective:** Define deterministic validation of transaction bytes and signer authority.
- **In scope:** Specify canonical fields, signature verification, nonce/sequence, account/network binding, amount precision and malformed transaction outcomes.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Transaction format and validation specification.
- **Acceptance checks:** Same transaction validates identically across nodes; malformed/wrong-network/wrong-signer/invalid nonce transactions are rejected.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-013 — Mempool policy, replay/double-spend and resource bounds

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-CHAIN-004
- **Source:** §15.1,§28.5.
- **Objective:** Define pending transaction admission and conflict management.
- **In scope:** Specify duplicate/replay keys, conflicting spends, fee policy slots, expiry, eviction, capacity and reorg reinsertion.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Mempool lifecycle and adversarial test matrix.
- **Acceptance checks:** Double spend and replay cannot be included twice; resource limits are enforceable; fee/expiry parameters remain unapproved until decided.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-014 — Native coin supply, issuance and conservation model

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-CHAIN-005
- **Source:** §§15.1,15.3–15.4,27,31.4.
- **Objective:** Define all ways the native coin supply can be created, moved, locked and removed.
- **In scope:** Map genesis allocation, protocol emission, block reward, transaction fees, treasury and any burn/slash categories; distinguish circulating, total and locked supply.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Coin supply/conservation model and parameter register.
- **Acceptance checks:** Every supply change has source and destination; off-chain Reputation is not misrepresented as native coin; unknown supply parameters stay open.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-015 — Transaction fee, reward and treasury accounting separation

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-CHAIN-005
- **Source:** §§15.1,15.3–15.4,27,31.4.
- **Objective:** Specify distinct accounting for transaction fees, validator incentives and task-verification fees.
- **In scope:** Define source ledgers, eligibility references, distribution events and reconciliation links without inventing percentages.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Fee/reward/treasury accounting contract.
- **Acceptance checks:** No double-counting across reward streams; each allocation reconciles; ratios require explicit approved Tokenomics.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-016 — Versioned RPC command/query contract

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-CHAIN-006
- **Source:** §15.1,15.4,16,23.
- **Objective:** Define public and authenticated RPC operations used by app, wallet and protocol services.
- **In scope:** Specify endpoints/commands, request identity, schema version, pagination, error semantics, rate limits and authorization boundary.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** RPC/API specification.
- **Acceptance checks:** Every operation has typed input/output, version and access rule; private user data is not exposed in public query APIs.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-017 — Block/transaction explorer data dictionary and privacy filtering

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-CHAIN-006
- **Source:** §15.1,15.4,16,23.
- **Objective:** Define the public data fields available for blockchain inspection.
- **In scope:** Map block height, transaction ID, sender/recipient representation, fee, status, confirmation/finality, validator and public event data; exclude private order fields/files/prompts.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Explorer field dictionary and redaction policy.
- **Acceptance checks:** Only explicitly public protocol data is exposed; pagination and freshness are defined; private settlement content remains off-chain.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-018 — Protocol parameter proposal and review lifecycle

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-CHAIN-007
- **Source:** §§15.1,15.4,31.
- **Objective:** Define the controlled process for proposing changes to Coin Rules and protocol parameters.
- **In scope:** Specify proposal identity, proposer authority, supporting evidence, risk review, public disclosure, voting and rejection/withdrawal.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Governance proposal lifecycle and decision matrix.
- **Acceptance checks:** Each proposal has an explicit authority and status; no parameter change can be applied without the approved governance path.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-CHAIN-019 — Upgrade activation, compatibility, rollback and emergency powers

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-CHAIN-007
- **Source:** §§15.1,15.4,31.
- **Objective:** Specify how approved upgrades become active and how emergency changes are constrained.
- **In scope:** Define activation height/version, node compatibility, migration, stop/go, emergency key authority, audit and irreversible-chain limitations.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Protocol upgrade and emergency governance specification.
- **Acceptance checks:** Activation is deterministic across nodes; emergency authority is bounded/audited; irreversible changes are not represented as safely reversible.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-008 — Custody alternatives and user-responsibility comparison

- **Type:** governance.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-WALLET-002
- **Source:** §§15.2,16.2,28,31.4.
- **Objective:** Compare Self-Custody and Managed Wallet options against product, security and operational requirements.
- **In scope:** Assess key possession, server access, recovery, transaction authorization, support, loss scenarios and user responsibility.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Custody alternatives decision paper.
- **Acceptance checks:** Trade-offs are explicit; custody model remains unselected until owner approval; no custody guarantee is implied.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-009 — Wallet threat model, recovery authority and approval gate

- **Type:** governance.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-WALLET-002
- **Source:** §§15.2,16.2,28,31.4.
- **Objective:** Identify key compromise, phishing, device loss, insider, backup and transaction-substitution risks.
- **In scope:** Map controls and recovery powers for each custody alternative; record legal/regulatory review needs without giving a legal conclusion.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet threat model and owner decision gate.
- **Acceptance checks:** No wallet creation/transfer flow becomes production-approved before custody decision; residual risk and recovery authority are named.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-010 — Wallet creation/import and address-network binding

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-WALLET-003
- **Source:** §16.2.
- **Objective:** Specify key/address creation and import within the approved custody model.
- **In scope:** Define key generation/import, seed/private-key handling, derivation path, network selection, duplicate import and address validation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet create/import contract and state flow.
- **Acceptance checks:** No key is exposed in logs/UI history; address is bound to expected network; unsupported import fails safely.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-011 — Backup verification and restore activation workflow

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-WALLET-003
- **Source:** §16.2.
- **Objective:** Define the point at which a wallet is considered safely backed up and usable.
- **In scope:** Specify backup confirmation, restore test, incorrect recovery material, interrupted restore and account activation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet restore and activation acceptance matrix.
- **Acceptance checks:** Activation follows required backup evidence under the approved custody policy; failed recovery does not overwrite existing wallet state.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-012 — Encrypted wallet backup format and integrity verification

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-WALLET-004
- **Source:** §§16.2,28.3.
- **Objective:** Define how encrypted backup material is structured and verified.
- **In scope:** Specify versioned envelope, encryption parameters as approved slots, integrity/authenticity check, metadata minimization and offline export.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet backup format and verification rules.
- **Acceptance checks:** Backup cannot be read without authorized material; tampering is detected; no plaintext secret is persisted.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-013 — Recovery, key rotation and compromise-response workflow

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-WALLET-004
- **Source:** §§16.2,28.3.
- **Objective:** Specify recovery after loss/compromise and the retirement of prior credentials.
- **In scope:** Define user confirmation, recovery proof, replacement-key registration, address/authority changes, revocation and notifications.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet recovery/rotation runbook and test scenarios.
- **Acceptance checks:** Recovery requires explicit user-authorized proof; old key permissions are revoked where applicable; compromise response is auditable.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-014 — Transaction payload construction and field validation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-WALLET-005
- **Source:** §16.3.
- **Objective:** Define canonical unsigned transactions from user-entered send details.
- **In scope:** Validate recipient, amount, asset/network, memo, precision, balance, fee and destination format.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Unsigned transaction builder contract.
- **Acceptance checks:** Invalid amount/address/network rejected; exact payload fields are reviewable before signing; no hidden value mutation.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-015 — Signing boundary, user confirmation and anti-substitution checks

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-WALLET-005
- **Source:** §16.3.
- **Objective:** Specify the handoff from transaction preview to secure signing.
- **In scope:** Bind signing request to canonical transaction hash, user confirmation, signer identity, expiry and broadcast result.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet signing interface and substitution test matrix.
- **Acceptance checks:** Displayed transaction equals signed transaction; recipient/amount/network substitution is detected; keys stay within approved custody boundary.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-016 — Send/receive lifecycle and confirmation semantics

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-WALLET-006
- **Source:** §§16.3–16.5.
- **Objective:** Define the states shown for outgoing and incoming transfers.
- **In scope:** Map signed, broadcast, pending, included, confirmed, finalized, failed and reorged evidence with source-defined distinction.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet transfer lifecycle and status dictionary.
- **Acceptance checks:** Pending/confirmed is not mislabeled finalized; every state links to chain evidence and last update.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-017 — Transaction history categories, details and reconciliation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-WALLET-006
- **Source:** §§16.3–16.5.
- **Objective:** Specify searchable history and its relation to rewards, fees, stakes and settlements.
- **In scope:** Define category, transaction ID, amount/asset, timestamp/block, fee, status, recipient/sender display and duplicate ingestion controls.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet history contract and reconciliation cases.
- **Acceptance checks:** All listed categories are represented; every displayed transaction is chain-backed; indexer replay cannot duplicate history.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-018 — Wallet overview field ownership and source mapping

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-WALLET-007
- **Source:** §16.1–16.2.
- **Objective:** Identify the authoritative source for each account and chain overview metric.
- **In scope:** Map total/available/locked balances, Good/Bad Reputation, validator stake, pending rewards, Unbonding Balance, chain status, block height and peers.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Wallet/blockchain overview field dictionary.
- **Acceptance checks:** Every field identifies source, asset/unit, block/sequence and freshness; unavailable values are not substituted with zero.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-WALLET-019 — Overview consistency, finality and authorization contract

- **Type:** data-contract.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-WALLET-007
- **Source:** §16.1–16.2.
- **Objective:** Specify snapshot consistency across on-chain and off-chain projections.
- **In scope:** Define reconciliation version, stale indexer handling, role-based privacy and differences between total and spendable.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Overview consistency/query contract.
- **Acceptance checks:** Projections do not claim finality without proof; unauthorized user cannot inspect another account; stale/inconsistent snapshot is disclosed.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-006 — Validator candidate hardware/network/identity criteria

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-VALIDATOR-002
- **Source:** §§18.1,18.3.
- **Objective:** Define the candidate evidence required before validator registration.
- **In scope:** Map supported software/version, hardware and network availability, identity, uptime capability and owner decision slots.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator eligibility evidence schema.
- **Acceptance checks:** Every criterion has measurable evidence or an explicit unknown; compute-node membership alone does not imply validator eligibility.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-007 — Validator threshold policy and eligibility decision explainability

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-VALIDATOR-002
- **Source:** §§18.1,18.3.
- **Objective:** Specify how approved thresholds produce eligible/ineligible results.
- **In scope:** Define configurable minimum stake, uptime/performance, software, network and geographic/decentralization criteria as unapproved decision slots.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator eligibility decision table.
- **Acceptance checks:** Same evidence and approved policy yield same result; unapproved thresholds remain unresolved and cannot be fabricated.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-008 — Eight-stage validator registration workflow

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VALIDATOR-003
- **Source:** §18.2.
- **Objective:** Specify the full source-described progression from application to active validator.
- **In scope:** Map application, validation, approval, stake lock, key registration, on-chain submission, activation queue and active status.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator registration state machine.
- **Acceptance checks:** All eight stages have actor, guard, event and recovery; no node becomes active before required protocol activation.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-009 — Consensus-key binding, activation queue and retry safety

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VALIDATOR-003
- **Source:** §18.2.
- **Objective:** Define binding of consensus signing identity and stake to one validator registration.
- **In scope:** Specify key proof, chain transaction, pending activation, duplicate registration, failed submission and status reconciliation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator key/activation contract and tests.
- **Acceptance checks:** Key and stake bind to same validator ID; retries are idempotent; pending is not shown as Active.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-010 — Stake lock, unbonding and withdrawal eligibility

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VALIDATOR-004
- **Source:** §18.2–18.5.
- **Objective:** Specify the lifecycle of validator stake and conditions for release.
- **In scope:** Model stake deposit, locked balance, exit request, duty completion, unbonding period, release and chain reconciliation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator stake lifecycle contract.
- **Acceptance checks:** Locked stake cannot be withdrawn early; unbonding period remains an approved parameter; final release is chain-evidenced.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-011 — Slashing/penalty authority, evidence and appeal boundary

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VALIDATOR-004
- **Source:** §18.2–18.5.
- **Objective:** Define how penalties can be proposed, applied and contested.
- **In scope:** Map duty evidence, violation categories, severity parameters, decision authority, appeal, accounting and irreversible consequences.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator penalty/slashing governance register.
- **Acceptance checks:** No penalty is applied without approved rule and evidence; appeal and record linkage explicit; amounts/thresholds stay open.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-012 — Validator duty and performance evidence model

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-VALIDATOR-005
- **Source:** §18.3–18.5,§27.
- **Objective:** Define source and calculation of uptime, successful/missed duties and consensus participation.
- **In scope:** Specify observation source, time window, chain block reference, missing telemetry and correction handling.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator performance field dictionary.
- **Acceptance checks:** Every metric has source/window/units; missing telemetry is not treated as failure/success without policy.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VALIDATOR-013 — Validator reward, penalty and appeal reconciliation tests

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-VALIDATOR-005
- **Source:** §18.3–18.5,§27.
- **Objective:** Verify reward and penalty records against chain and duty evidence.
- **In scope:** Test reward origin, missed duty, double accrual, appeal status, corrected event and historical display.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Validator reward/penalty QA suite.
- **Acceptance checks:** Every payout/penalty links to duty and chain events; appeal remains traceable; retries do not duplicate financial records.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-008 — Verifier enrollment identity and role separation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-NODES-002
- **Source:** §19.1–19.2.
- **Objective:** Define verifier registration distinct from normal compute and blockchain-validation identities.
- **In scope:** Capture principal/node identity, role credential, software, availability, stake reference, conflict declaration and audit events.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Verifier enrollment schema and workflow.
- **Acceptance checks:** Verifier identity is separate from blockchain validator and compute worker; role-specific permissions are explicit.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-009 — Verifier eligibility, stake and activation policy gate

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-NODES-002
- **Source:** §19.1–19.2.
- **Objective:** Define the review needed before a verifier can receive assignments.
- **In scope:** Map eligibility evidence, approved stake threshold, availability, software state and approval/revocation conditions.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Verifier eligibility policy and decision record.
- **Acceptance checks:** No assignment before approved eligibility; task-verification stake is distinct from validator stake; unknown thresholds stay open.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-010 — Conflict-of-interest and related-party screening rules

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-VERIFY-NODES-003
- **Source:** §19.3,§28.
- **Objective:** Define the conflicts relevant to reviewing an order and settlement.
- **In scope:** Check customer/provider/owner relation, prior order involvement, common control, financial interest and prior committee participation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Conflict screening rulebook and evidence model.
- **Acceptance checks:** Each exclusion criterion has evidence, owner and appeal; missing evidence is not silently considered clean.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-011 — Exclusion audit, privacy and false-positive review

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-VERIFY-NODES-003
- **Source:** §19.3,§28.
- **Objective:** Specify how exclusions are recorded and challenged without exposing excessive personal data.
- **In scope:** Define reason codes, proof confidence, privacy minimization, audit access, review/appeal and re-entry condition.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Exclusion audit schema and review workflow.
- **Acceptance checks:** Every exclusion can be audited; privacy and appeal controls exist; alias changes cannot bypass known link evidence.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-012 — Randomness candidate comparison and bias-resistance analysis

- **Type:** architecture-decision.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-VERIFY-NODES-004
- **Source:** §19.3.
- **Objective:** Compare auditable random-selection sources for committee membership.
- **In scope:** Assess beacon, chain-derived randomness, commit-reveal or other candidates for manipulation, availability, timing, independence and complexity.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Randomness alternatives evaluation.
- **Acceptance checks:** Each candidate documents attack assumptions, bias window and fallback; no mechanism is selected without approval.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-013 — Selection proof format, reproducibility and fallback decision

- **Type:** architecture-decision.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-VERIFY-NODES-004
- **Source:** §19.3.
- **Objective:** Define evidence needed for any chosen random committee process.
- **In scope:** Specify input snapshot, seed/beacon reference, algorithm/version, eligibility filter, exclusions, output order and fallback evidence.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Committee selection proof schema and ADR.
- **Acceptance checks:** Independent reviewer can reproduce selected set from retained evidence; fallback is deterministic/approved; unverifiable selection cannot be called random.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-014 — Committee eligibility snapshot and 100-member set selection

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-NODES-005
- **Source:** §19.3,§24,§25.
- **Objective:** Define the membership snapshot and selection for stage one and stage two.
- **In scope:** Validate stake/role/availability/conflict evidence; capture 100-member sets and first-stage membership snapshot.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Committee membership snapshot and selection contract.
- **Acceptance checks:** Each selected committee has exactly 100 eligible unique identities; selection evidence is reproducible.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-015 — Disjoint second committee, assignment record and evidence persistence

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-NODES-005
- **Source:** §19.3,§24,§25.
- **Objective:** Ensure the second 100-member committee is independent from the first.
- **In scope:** Apply approved ownership/conflict exclusions, preserve random selection proof and persist both sets against same order/version.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Two-committee selection service contract.
- **Acceptance checks:** Second committee has zero member overlap and evidenced independence checks; insufficient eligible capacity stays Pending Verification.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-016 — Capacity shortage and Pending Verification state

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-NODES-006
- **Source:** §19.3,§25,§31.6.
- **Objective:** Define the safe order state when 200 eligible independent members are unavailable.
- **In scope:** Track available candidates, missing slots, reason, queue/retry policy and operator visibility without manufacturing a committee.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Verification capacity state machine.
- **Acceptance checks:** Fewer than 200 eligible independent members never appears as a completed two-committee assignment; state and cause are visible.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-017 — Absence, replacement and committee continuity rules

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-VERIFY-NODES-006
- **Source:** §19.3,§25,§31.6.
- **Objective:** Specify how selected but absent/unavailable members are handled.
- **In scope:** Record timeout evidence, replacement candidate source, disjointness recheck, selection proof update and effect on already submitted votes.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Committee replacement workflow and decision slots.
- **Acceptance checks:** Absent member is not counted as a vote; replacement preserves eligibility/disjointness; no arbitrary deadline or reselection rule is assumed.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-018 — Verifier dashboard data contract and queue states

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-VERIFY-NODES-007
- **Source:** §19.1–19.2.
- **Objective:** Define assignment, pending review, completed review and eligibility fields.
- **In scope:** Map task/order ID, committee/stage, deadline policy, evidence version, stake/eligibility and reward history to authoritative sources.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Verifier dashboard field dictionary.
- **Acceptance checks:** Each status and metric has a source; ineligible/conflicted reviewer sees no actionable assignment.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-VERIFY-NODES-019 — Verifier interaction, performance and reward history

- **Type:** ux.
- **Primary owner:** ux-interaction-engineer
- **Parent work package:** WP-VERIFY-NODES-007
- **Source:** §19.1–19.2.
- **Objective:** Specify work queue and historical performance views.
- **In scope:** Define evidence opening, conflict declaration, review submission, completed assignment, correctness evidence, reward and penalty history.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Verifier interaction flow and acceptance matrix.
- **Acceptance checks:** Review is bound to assigned record version; reward/penalty display is evidence-backed; hidden or unauthorized data is not shown.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-007 — Genesis/protocol start and block-height time anchor

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-002
- **Source:** §27.3.
- **Objective:** Define the authoritative start point for the twenty-year protocol reward schedule.
- **In scope:** Specify genesis/start block reference, canonical height source, network upgrade/reorg consideration and protocol-year numbering.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Protocol clock anchor specification.
- **Acceptance checks:** All nodes use the same chain-defined start point; wall-clock/device timezone does not affect year calculation.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-008 — Completed protocol-year boundary calculation and reorg behavior

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-002
- **Source:** §27.3.
- **Objective:** Define the exact point when a completed protocol year changes the emission multiplier.
- **In scope:** Specify block-height intervals, exact boundary semantics, chain reorganization handling and deterministic recomputation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Protocol-year calculation rules and boundary vectors.
- **Acceptance checks:** Year 0–20 transitions are deterministic; reorg handling cannot create inconsistent emissions; any block-count/year-length parameter remains approved/configured.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-009 — Linear emission multiplier and 20-year schedule vectors

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-003
- **Source:** §27.2–27.4,31.4.
- **Objective:** Formalize the proposed formula max(0,100−5×completed protocol years).
- **In scope:** Represent year 0 through year 20, multiplier precision, zero floor and transition boundaries as deterministic vectors.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Emission multiplier specification and golden table.
- **Acceptance checks:** All 21 schedule points match source; year 10 is 50%; year 20 onward is zero; rounding is explicit.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-010 — Base issuance, supply cap and activation parameter register

- **Type:** specification.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-003
- **Source:** §27.2–27.4,31.4.
- **Objective:** Define the remaining economic inputs needed to calculate actual token amounts.
- **In scope:** List base reward per block/period, supply cap, activation height, division precision and change authority as owner decision slots.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Emission parameter register and approval checklist.
- **Acceptance checks:** No actual token quantity is fabricated; every parameter has owner/source/state; unapproved parameters block production issuance.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-011 — Role eligibility evidence for validator and verifier rewards

- **Type:** economics.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-004
- **Source:** §§27.5–27.7.
- **Objective:** Define which completed duties can qualify for protocol incentives.
- **In scope:** Separate blockchain validator duties from AI task verification; map valid participation, uptime, signed review, conflict and appeal evidence.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Role reward eligibility specification.
- **Acceptance checks:** Only source-evidenced duties qualify; a vote direction alone does not establish misconduct or reward eligibility.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-012 — Role split, missed duty and reward conservation decision

- **Type:** economics.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-004
- **Source:** §§27.5–27.7.
- **Objective:** Model distribution between role classes and handling of ineligible/missed duties.
- **In scope:** Define allocation parameter slots, withheld/reverted amounts, missed-duty rules and reconciliation without inventing ratios.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Protocol role allocation and decision record.
- **Acceptance checks:** Validator/verifier streams remain separate from order compute rewards; all amounts reconcile; split remains unapproved until owner decision.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-013 — Reward accrual identity and chain event binding

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-005
- **Source:** §§8,15,18,19,27.
- **Objective:** Define canonical records for protocol reward accrual.
- **In scope:** Bind protocol year/block, source emission, role identity, eligible duty, amount, asset, transaction/event and claim state.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Protocol reward accrual schema.
- **Acceptance checks:** Every accrual traces to one valid duty and emission period; ineligible roles cannot claim.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-014 — Claim, replay prevention and cross-ledger reconciliation

- **Type:** implementation.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-005
- **Source:** §§8,15,18,19,27.
- **Objective:** Specify the claim lifecycle and reconciliation with reward balances.
- **In scope:** Define pending/accrued/claimable/claimed/reversed states, idempotency, chain receipt and source-stream separation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Reward claim state machine and invariant suite.
- **Acceptance checks:** Duplicate claim/replay cannot double-credit; role and fee ledgers reconcile; pending reward is not spendable.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-015 — Emission participation and concentration scenario matrix

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-006
- **Source:** §27,§§29–31.
- **Objective:** Define realistic scenarios for node participation and reward concentration.
- **In scope:** Vary eligible validator/verifier populations, participation, hardware diversity, rewards and concentration assumptions; disclose source of assumptions.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Economic scenario input matrix.
- **Acceptance checks:** Every assumption has provenance or is labelled illustrative; simulation is not described as a forecast or guarantee.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-PROTOCOL-REWARDS-016 — Adversarial incentive simulation and sensitivity report

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-PROTOCOL-REWARDS-006
- **Source:** §27,§§29–31.
- **Objective:** Evaluate attacks and system effects as incentives decline over twenty years.
- **In scope:** Test low participation, Sybil concentration, collusion, missed duties, reward capture, fee dependency and year boundary cases.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Adversarial simulation/report specification.
- **Acceptance checks:** Results disclose limitations, sensitivity and approval needs; unresolved emission parameters are not treated as known.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-009 — Asset, actor, trust-boundary and threat inventory

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-002
- **Source:** §§1.2,6.2,9,14,17,21,23,28,29.
- **Objective:** Inventory the valuable assets and actors across both compute and blockchain networks.
- **In scope:** Map user/customer/provider, owner, devices, compute nodes, chain peers, validators, verifiers, application services, storage and settlement records.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Threat model asset/actor/trust-boundary register.
- **Acceptance checks:** Each asset has owner/classification; each trust crossing has threat and control status; compute and blockchain trust domains remain distinct.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-010 — Abuse case, attack path and residual-risk register

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-002
- **Source:** §§1.2,6.2,9,14,17,21,23,28,29.
- **Objective:** Convert risks and named attacks into traceable abuse cases.
- **In scope:** Map Sybil, impersonation, replay, double-spend, collusion, DoS, node failure, malicious model, prompt injection and data exposure to attack path and impact.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Threat/abuse-case register and residual-risk owners.
- **Acceptance checks:** Each abuse case includes preconditions, impact, likelihood uncertainty, preventive/detective/recovery controls and accountable owner.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-011 — Secret classification and role key inventory

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-003
- **Source:** §§15,16,18,19,24,28.
- **Objective:** Create a complete inventory of secrets and cryptographic credentials.
- **In scope:** Separate wallet, owner, node, validator, verifier, application, storage and infrastructure keys; identify signing purpose and exposure impact.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Secret/key inventory and classification matrix.
- **Acceptance checks:** Every secret has a purpose, owner, storage boundary and rotation/revocation path; no generic shared master key assumption.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-012 — Signing authorization, rotation and compromise response rules

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-003
- **Source:** §§15,16,18,19,24,28.
- **Objective:** Specify how authorized signatures are produced and how compromise is contained.
- **In scope:** Define least-privilege signing, key lifecycle, backup/recovery, rotation, revocation propagation, audit and emergency response.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Signing/key lifecycle security policy.
- **Acceptance checks:** Secrets are not logged or exposed; roles cannot misuse each other's keys; custody and technology choices remain approval-gated.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-013 — Application and dependency provenance controls

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-004
- **Source:** §§2,4,5,28.
- **Objective:** Define integrity and trust controls for application releases and dependencies.
- **In scope:** Specify approved source, dependency pinning, manifests, signatures, build provenance, update authorization and vulnerability response.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Software supply-chain security requirements.
- **Acceptance checks:** Release artifacts are traceable to source/revision/build evidence; untrusted update cannot activate silently.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-014 — Model provenance, signed manifests and rollback safety

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-004
- **Source:** §§2,4,5,28.
- **Objective:** Define equivalent controls for model weights, runtime packages and update rollback.
- **In scope:** Bind publisher/revision, file hashes, licence status, runtime compatibility, manifest signature and known-vulnerable version handling.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Model/runtime provenance and update policy.
- **Acceptance checks:** Model origin and exact revision verified before activation; rollback cannot silently restore a compromised version.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-015 — Runtime sandbox capability and resource isolation matrix

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-005
- **Source:** §§5,6.2,9,28.
- **Objective:** Define process isolation and allowed access for local and distributed inference.
- **In scope:** Specify filesystem, network, process, device, memory, CPU/GPU, temp storage and inter-process boundaries as platform-tested controls.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Sandbox and resource isolation matrix.
- **Acceptance checks:** No runtime has blanket access by default; resource limits and permitted capabilities are measurable; unimplemented controls are labelled proposals.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-016 — Prompt injection, malicious inputs and peer workload abuse tests

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-005
- **Source:** §§5,6.2,9,28.
- **Objective:** Define attack cases for customer prompts, provider templates, model artifacts and remote node messages.
- **In scope:** Test instruction-boundary crossing, path traversal, oversized input, shell/code execution, malicious model metadata and resource exhaustion.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Security test corpus and acceptance cases.
- **Acceptance checks:** Untrusted text is data not privileged instruction; malicious inputs do not execute code or bypass authorization; observed results are recorded later.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-017 — Authenticated transport, replay and peer impersonation controls

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-006
- **Source:** §§1.2,9–11,14,28.1–28.2.
- **Objective:** Define secure channel and message authenticity requirements for node communications.
- **In scope:** Specify peer authentication, channel encryption, message signing/context, replay counters, versioning and reconnect key handling.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Node communications security contract.
- **Acceptance checks:** Peer identity is authenticated; replay/impersonation tests are specified; encryption is not claimed to conceal plaintext from the executing node.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-018 — Intermediate-data visibility, minimization and customer disclosure

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-006
- **Source:** §§1.2,9–11,14,28.1–28.2.
- **Objective:** Specify exactly what data participating compute nodes can observe during distributed inference.
- **In scope:** Map input fragments, activations, intermediate tensors, outputs, logs and transient storage; compare minimization/confidential-compute alternatives as open decisions.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Intermediate-data exposure analysis and disclosure requirements.
- **Acceptance checks:** Every visible data class and recipient is disclosed; no transport-encryption-only confidentiality claim; retention and protection decisions remain explicit.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-019 — Storage data classification, encryption and access-control matrix

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-007
- **Source:** §§21,23,28.4.
- **Objective:** Define privacy/security controls for customer inputs, outputs, prompts, files, logs and settlement evidence.
- **In scope:** Map data at rest/in transit, storage service access, keys, role ACLs, metadata and backups.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Storage data protection matrix.
- **Acceptance checks:** Every data class has sensitivity, permitted reader, encryption/access control and audit requirement; public chain contains no private file/prompt.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-020 — Retention, deletion, backup and access-audit lifecycle

- **Type:** security.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-007
- **Source:** §§21,23,28.4.
- **Objective:** Define data lifecycle controls without inventing retention periods.
- **In scope:** Map collection/minimization, purpose, expiry decision, legal hold, deletion propagation, backup expiry, download audit and incident preservation.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Data lifecycle and retention decision register.
- **Acceptance checks:** No arbitrary retention duration imposed; deletion covers replicas/caches as applicable; legal hold and auditable access are explicit.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-021 — Security monitoring signals, incident severity and escalation

- **Type:** operations.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-008
- **Source:** §§11,28,29.
- **Objective:** Define detection signals for named security events and system failures.
- **In scope:** Map event source, telemetry, severity, owner, on-call/escalation and false-positive handling for Sybil, DoS, malicious node, double spend, replay and key compromise.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Security monitoring and escalation matrix.
- **Acceptance checks:** Each high-impact threat has a detectable signal and responsible owner; monitoring avoids collecting unnecessary sensitive data.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-SECURITY-022 — Containment, recovery exercises and residual-risk acceptance

- **Type:** operations.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-SECURITY-008
- **Source:** §§11,28,29.
- **Objective:** Specify repeatable incident response and recovery for high-impact failures.
- **In scope:** Define node isolation, credential revocation, chain pause authority if approved, backup restore, data breach response, evidence preservation and exercise schedule.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Incident response runbook and exercise acceptance plan.
- **Acceptance checks:** Each scenario has containment/recovery steps and evidence; residual risk is explicitly approved by authorized owner; no unapproved kill-switch powers.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-008 — Requirement-to-task-to-component traceability audit

- **Type:** integration.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-MAINNET-READINESS-002
- **Source:** §§3–27,30.
- **Objective:** Verify every source requirement maps to one or more task outputs and actual component ownership.
- **In scope:** Cross-reference source sections, requirements, all 447 task IDs, responsible roles, architecture contracts and evidence paths.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Complete release traceability matrix.
- **Acceptance checks:** No source requirement or critical interface is orphaned; current implementation state is distinguished from target tasks.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-009 — End-to-end integration contract and dependency readiness review

- **Type:** integration.
- **Primary owner:** project-mapping-engineer
- **Parent work package:** WP-MAINNET-READINESS-002
- **Source:** §§3–27,30.
- **Objective:** Map integration seams across local AI, compute network, marketplace, order, delivery, identity, chain, verification and settlement.
- **In scope:** Specify producer/consumer contracts, schema versions, readiness evidence, ordering constraints and open decision blockers.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Integrated interface/readiness matrix.
- **Acceptance checks:** Every cross-domain interaction has owned contract and acceptance evidence; recommended development phase is not falsely treated as blocking edge.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-010 — Benchmark workloads, environments and measurement protocol

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-MAINNET-READINESS-003
- **Source:** §§5,9–11,29–30.
- **Objective:** Define comparable local and distributed workload profiles.
- **In scope:** Record model revision, quantization, hardware, network topology, prompt/input size, warm-up, repeats, concurrency and metrics.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Benchmark protocol and environment manifest.
- **Acceptance checks:** Measurements are repeatable and environment-specific; no claim of million-node scale/data-center equivalence without evidence.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-011 — Performance capacity, imbalance and scaling analysis

- **Type:** benchmark.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-MAINNET-READINESS-003
- **Source:** §§5,9–11,29–30.
- **Objective:** Define how measured results inform capacity and scalability decisions.
- **In scope:** Measure startup/inference, throughput, data transfer, memory, stage imbalance, latency, failure degradation and recovery; state confidence.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Capacity/scaling benchmark report template and decision criteria.
- **Acceptance checks:** Predictions separated from measurements; workload/conditions disclosed; unsupported targets remain unapproved.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-012 — Failure scenario catalogue and safety invariants

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-MAINNET-READINESS-004
- **Source:** §§11,13,21,24–26,28–30.
- **Objective:** Define fault-injection scenarios across compute, storage, payments, committees and settlement.
- **In scope:** Cover node loss, network partition, timeout, corrupted model/file, duplicate webhook, unavailable storage, committee shortfall and partial payout.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Failure scenario matrix and expected safe state.
- **Acceptance checks:** Each scenario has trigger, affected state, expected safe outcome, prohibited side effects and recovery owner.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-013 — Fault injection, recovery evidence and launch-blocking thresholds

- **Type:** testing.
- **Primary owner:** qa-testing-engineer
- **Parent work package:** WP-MAINNET-READINESS-004
- **Source:** §§11,13,21,24–26,28–30.
- **Objective:** Specify the actual test execution plan and severity treatment before mainnet.
- **In scope:** Define environment isolation, repeatability, data reset, financial invariants, recovery evidence and criteria for blocking release.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Resilience test plan and go/no-go criteria.
- **Acceptance checks:** Every critical scenario has an executable test and recovery evidence; severe unresolved failures block readiness; no test is claimed run until executed.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-014 — Independent audit scope, reviewer qualifications and evidence access

- **Type:** governance.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-MAINNET-READINESS-005
- **Source:** §§28–31.
- **Objective:** Define independent review requirements for security before release.
- **In scope:** Specify in-scope components, threat coverage, reviewer independence/qualification, evidence access, confidentiality and audit deliverables.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Security audit scope and reviewer criteria.
- **Acceptance checks:** Self-review is not labeled independent; reviewer conflict and scope limitation are disclosed.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-015 — Finding severity, remediation, retest and residual-risk approval

- **Type:** governance.
- **Primary owner:** safety-engineer
- **Parent work package:** WP-MAINNET-READINESS-005
- **Source:** §§28–31.
- **Objective:** Define how audit findings are triaged and closed.
- **In scope:** Specify severity taxonomy, responsible owner, remediation deadline decision, retest evidence, exception authority and unresolved risk register.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Audit finding lifecycle and sign-off register.
- **Acceptance checks:** Critical/high findings block release absent verified remediation or authorized exception; every closure has retest evidence.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-016 — Legal, jurisdiction, licensing and payment decision register

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-MAINNET-READINESS-006
- **Source:** §§15,27,29,31.
- **Objective:** Identify external approvals and qualified decisions needed before public operation.
- **In scope:** Record operating jurisdictions, coin classification, payments/exchange, consumer terms, model licences, privacy/data rules and responsible qualified reviewer.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Legal/compliance decision register.
- **Acceptance checks:** No legal conclusion is invented; each decision has jurisdiction, evidence, owner and state; unresolved items block affected deployment.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-017 — Tokenomics, custody, operations and retention approval package

- **Type:** governance.
- **Primary owner:** feasibility-engineer
- **Parent work package:** WP-MAINNET-READINESS-006
- **Source:** §§15,27,29,31.
- **Objective:** Consolidate technical-owner decisions that materially affect launch readiness.
- **In scope:** Record consensus/finality, supply/fee/emission/stake, wallet custody, dispute/refund, retention, incident support and upgrade authority.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Mainnet owner decision package.
- **Acceptance checks:** Every parameter is approved or explicitly blocks release; no default value or policy is silently promoted to accepted.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-018 — Release environment, staged rollout and go/no-go checklist

- **Type:** operations.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MAINNET-READINESS-007
- **Source:** §30.
- **Objective:** Define controlled promotion from development/test to candidate and mainnet environments.
- **In scope:** Specify build provenance, configuration separation, feature gates, release cohorts, observability, backups, owner approvals and stop criteria.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Environment promotion and go/no-go runbook.
- **Acceptance checks:** Every mandatory gate has evidence and approver; release configuration is reproducible; mainnet is not enabled by a planning artifact.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

### WP-MAINNET-READINESS-019 — Rollback, emergency stop and irreversible-chain response

- **Type:** operations.
- **Primary owner:** execution-engineer
- **Parent work package:** WP-MAINNET-READINESS-007
- **Source:** §30.
- **Objective:** Define safe rollback/stop behavior for app and chain components.
- **In scope:** Separate reversible application rollback from irreversible protocol/transaction outcomes; define data restore, key compromise and upgrade emergency authority.
- **Out of scope:** Sibling package outputs; unapproved technology, cryptography, economic, custody, governance, legal or policy decisions; unrelated refactors; changes to the read-only source.
- **Required output:** Rollback and emergency response playbook.
- **Acceptance checks:** Irreversible transfers/chain history are not claimed reversible; emergency authority is explicit/approved; user funds and evidence are preserved.
- **Verification evidence:** Reviewed decision/contract or runnable deliverable as appropriate; reproducible tests and actual results are mandatory for later implementation/QA tasks. Plans do not prove runtime effectiveness.
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003
- **Detailed contract:** [04-blockchain-security-and-readiness.md](execution-work-breakdown/04-blockchain-security-and-readiness.md)

## Static integration and graph result for WP-INIT-003
- Work packages: 280 new execution-level tasks across 137 existing granular parents.
- Current task inventory: 3 initialization tasks + 27 domain baselines + 137 intermediate roll-up packages + 280 execution leaves = 447 unique task IDs.
- Graph: 447 nodes and 1077 direct prerequisite edges; all 447 nodes were topologically visited; no cycle, unresolved ID, self-edge or duplicate dependency.
- Statuses: WP-INIT-001, WP-INIT-002 and WP-INIT-003 done; all 444 domain/intermediate/leaf work packages not_started.
- Existing task IDs and histories preserved; no product source or implementation code changed.
- Role reviews are sequential same-assistant passes; independent autonomous agents or independent QA sign-off are not claimed.

## Additional decomposition and roll-up rules
- The task catalog contains all 447 IDs. Full leaf definitions live in the four execution-level work-breakdown files; the catalog index carries each task's owner, source, objective, scope, exclusions, output, acceptance, evidence and prerequisites.
- An intermediate parent is a roll-up: it may be marked done only after all of its mapped execution-level children are done and its own acceptance checks pass.
- A new leaf does not depend on its intermediate parent; it depends on the real domain baseline and WP-INIT-003. This prevents circular dependencies while retaining auditable parent/child grouping.
- WP-INIT-003 completion permits scheduling the defined children once their other direct prerequisites are done. It does not authorize code or policy decisions.
- Keep Section 30's implementation phase order advisory unless a concrete output/contract is a true prerequisite.
