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
- **Acceptance:** All 27 domains have a baseline gate and at least four concrete child tasks; each child has one verifiable outcome; catalog/graph ID sets match; every graph node has only id/depends_on/status; no invalid refs, self/duplicate edges or cycles; statuses valid; source sections mapped; owner/output/acceptance defined; no unapproved choice becomes an approval; no app code or out-of-scope path changes.
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

