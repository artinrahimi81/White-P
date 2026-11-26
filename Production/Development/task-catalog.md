# Task Catalog

This catalog defines task objectives, scope, exclusions, source traceability, deliverables, acceptance criteria and unresolved decisions. It does not duplicate task status or dependency lists. The sole sources of task IDs, direct prerequisites and execution status are dependency-graph.json.

## Task identifier convention

- Use the immutable form WP-DOMAIN-NNN: uppercase domain code and a three-digit sequence within the domain.
- An identifier denotes task identity only. It does not encode priority, execution order, status, owner or file count.
- Once published, an identifier is never renamed, reused or reassigned. A split or merged task receives new identifiers and an explicit traceability update.
- Keep all task descriptions and acceptance details in this catalog or the selected task's task-status.md. Keep direct prerequisites and status only in dependency-graph.json.

## WP-INIT-001 — Decompose the approved product specification into executable tasks

- **Source:** Production/task-decomposition/main-document.md, introductory guide, all 32 numbered sections and final vision.
- **Purpose:** Convert the complete product specification into a complete, traceable, non-duplicated set of bounded development tasks and a minimal dependency graph.
- **Scope:** Read/map the complete source; identify requirements, components, workflows, interfaces, security/privacy responsibilities, delivery and operational needs, proposals and unresolved decisions; define stable IDs; specify objectives, boundaries, outputs and verifiable acceptance; identify genuine direct prerequisites; validate catalog/graph consistency and integrity.
- **Exclusions:** Feature implementation; mocks, stubs or placeholders; editing/copying/moving/renaming the source; resolving open decisions without approval; changing the user's intended meaning; choosing technologies not fixed by an approved source.
- **Deliverables:** Complete catalog; graph where every task object has exactly id, depends_on and status; section-to-task traceability; explicit proposal/assumption/open-decision records; selected-task status and append-only role histories; validation evidence.
- **Acceptance:** All 32 numbered sections plus applicable introductory/final material are mapped; concrete requirements and workflows are assigned to bounded tasks or explicitly left unresolved; every task has objective, scope, exclusions, sources, outputs and testable acceptance; duplicates/gaps/ambiguities are addressed; graph edges are genuine direct prerequisites; IDs match across catalog and graph; all graph objects have exactly three keys; IDs/references/statuses are valid; no self/duplicate edges or cycles; proposals remain distinct from approved requirements; role reviews and Senior Engineer acceptance are documented.
- **Initial state:** not_started. This is a planning/decomposition task and does not authorize application feature implementation.

## WP-ARCH-001 — Product architecture boundaries and shared contracts

- **Objective:** Define the system context and responsibilities of local inference, distributed AI computation, application management and the separate blockchain network.
- **Scope:** Map actors and major components; preserve Windows-first/open-source/English UI constraints; distinguish Pipeline Parallelism from Tensor Parallelism; describe model/runtime, network-management, blockchain and cross-network contracts; distinguish compute nodes, full nodes, blockchain validators and AI task-verification nodes.
- **Exclusions:** Selecting unapproved frameworks, consensus, cryptography, model implementations, deployment topology or economic policy; feature implementation.
- **Source:** Introduction and Sections 1, 2, 14, 17, 29, 32.
- **Deliverables:** Architecture context, component/responsibility map, data/control-flow contracts, constraints and unknowns.
- **Acceptance:** All major subsystems and actors have explicit boundaries; two networks remain separate but related; Pipeline and Tensor Parallelism are not conflated; proposals are not presented as decisions.
- **Open decisions:** Initial models/modalities, partition granularity, future Tensor Parallelism, network size, multi-network membership and deployment topology.

## WP-APP-001 — Windows desktop shell, navigation and dashboard

- **Objective:** Define the shared desktop application shell and global navigation surfaces.
- **Scope:** Sidebar/collapse, top bar, breadcrumbs and content region; AI Workspace, Explore, Blockchain & Wallet and Settings; Dashboard and Orders & Deliveries operational views; dashboard information and quick actions; account/security/wallet-security/notifications/privacy/storage/preferences settings; resizing and scaling.
- **Exclusions:** Reimplementing feature-specific workflows owned by other tasks; inventing screens or final visual branding.
- **Source:** Sections 2 and 3.
- **Deliverables:** Navigation/screen inventory, shared shell contracts, dashboard data requirements, settings requirements and testable display/interaction criteria.
- **Acceptance:** All primary and detailed navigation elements are covered; Dashboard and Orders & Deliveries remain cross-cutting views; top-bar/dashboard fields and actions are traceable; Windows scaling/resizing and English UI are verifiable.
- **Open decisions:** Final brand/tokens and unspecified account/preferences behavior.

## WP-MODEL-001 — Model catalogue, provenance and licence compliance

- **Objective:** Catalogue supported model versions and determine eligibility for the intended local or distributed use.
- **Scope:** Name/version, developer, official repository, architecture, parameter count, size, type/tasks, minimum/recommended hardware, RAM/VRAM, download size, quantizations, inference engines, context length and licence; official-source acquisition; version/hash checks; separate review of weights, code, commercial-use and redistribution terms.
- **Exclusions:** Assuming every version in a model family has the same licence; treating downloadable weights as automatically suitable for commercial or multi-node use.
- **Source:** Sections 2 and 4; related requirements in 5 and 9.
- **Deliverables:** Model metadata schema, provenance record, version-specific licence assessment and eligibility rules.
- **Acceptance:** Every catalogue field is represented; exact version and origin are recorded; integrity is checked; restrictions for the intended use are visible; incompatible versions are not marked eligible.
- **Open decisions:** Initial models, supported modalities and the authoritative licence-approval process. The Qwen example in the source remains version-specific and must be rechecked.

## WP-AI-LOCAL-001 — Local model compatibility, installation and inference

- **Objective:** Let a user assess a Windows computer, obtain an eligible model and run it locally in the application.
- **Scope:** Model selection; CPU/GPU/RAM/VRAM/storage/driver/runtime checks; Compatible, Compatible with Performance Warning and Not Compatible outcomes; initial 20% resource-margin rule and benchmark calibration; official download, version/hash validation, runtime preparation, model loading and in-app conversation.
- **Exclusions:** Distributed execution; treating resource estimates as proof of actual performance.
- **Source:** Section 5 and related risks in 29.
- **Deliverables:** Hardware-test contract, compatibility decision rules, local setup/run flow and failure/recovery criteria.
- **Acceptance:** All required resources/runtime dimensions are checked; the three outcomes follow documented thresholds; benchmark limitations are explicit; downloaded files are verified; user can converse with the local model inside the app.
- **Open decisions:** Initial runtime engines, benchmark suite, calibration of the 20% margin and supported hardware matrix.

## WP-AI-TASK-001 — Defined Tasks authoring and prompt templating

- **Objective:** Let a provider define a structured AI service and let customers supply valid inputs.
- **Scope:** Task naming/Add New Task; up to 100 input parameters; long-form or four-choice question types; unique keywords up to 32 characters; required/optional rules; prompt editor with /keyword insertion, suggestions and highlighting; broken-reference detection on rename/delete; customer validation; Category, Specialty, Expected Response Time, Contact Method, USD price and external-payment capability.
- **Exclusions:** Inventing new input types; treating estimated response time as a guarantee; silently fixing currency conversion or prompt trust policy.
- **Source:** Section 6 and security implications in 28.
- **Deliverables:** Task/input schema, prompt-template contract, editor behavior, customer validation and service metadata.
- **Acceptance:** Limits/types/keyword rules are testable; all required inputs validate; unresolved prompt references are caught; customer data is separated from trusted instructions; all General Information fields exist; ETA is labelled an estimate.
- **Open decisions:** Text constraints, editing/versioning of published tasks and USD-to-coin conversion source.

## WP-AI-HISTORY-001 — Task execution and completed-task history

- **Objective:** Provide traceable history for local and network executions.
- **Scope:** Group by defined task; Task ID, date/time, execution status, start/completion time, payment, approved reward, payment status and result; participating/inactive/faulty computers for network executions; links to order and reward records.
- **Exclusions:** Replacing the authoritative order or settlement ledger; inventing participants for local execution.
- **Source:** Section 7 and relevant views in Sections 3 and 11.
- **Deliverables:** History record/read model and local/network presentation rules.
- **Acceptance:** Every listed field is represented; local runs show no fictitious node participants; network participant/failure data is traceable; stable task/order identifiers are used.
- **Open decisions:** Retention, pagination/filtering and partially completed/disputed history rules.

## WP-REWARD-001 — Reward accounting, balances and history

- **Objective:** Reconcile the distinct economic sources and user/network-owner reward views.
- **Scope:** Local/network reward summaries; total/approved/available/withdrawn/pending amounts; owner/member distributions; Compute Rewards, Verification Rewards and Blockchain Rewards kept distinct; references to settlement and protocol reward ledgers.
- **Exclusions:** Inventing fee percentages, issuance amounts or payout formulas; counting customer revenue as newly issued coin.
- **Source:** Sections 8, 23, 26 and 27.
- **Deliverables:** Reward ledger/read model, balance definitions, source reconciliation and summary-field requirements.
- **Acceptance:** Reward origins are distinguishable; customer-funded and newly issued rewards are not double-counted; local/network displays are defined; balances reconcile to source records.
- **Open decisions:** Reward splits, withdrawal rules/fees, platform fee, compute/verification funding shares and payout timing.

## WP-NET-CREATE-001 — Distributed compute-network creation and ownership

- **Objective:** Create a compute network around an eligible model and a verified partition manifest.
- **Scope:** Model eligibility and smallest executable unit; hardware/benchmark capacity; Pipeline stage map; Network ID and owner identity; model manifest, network configuration, defined tasks/prompts, reward/payout settings, ownership records, secure logs/backups/recovery; owner computer as first member.
- **Exclusions:** Confusing Tensor Parallelism with pipeline stages; making the owner's computer the only durable copy; hard-coding unresolved reward policy.
- **Source:** Section 9 and architecture/security constraints in 1, 14 and 28.
- **Deliverables:** Network creation flow, partition/manifest contract, management-data contract and backup/recovery requirements.
- **Acceptance:** Unique Network ID and owner identity are produced; partition assignments have compatibility evidence; owner joins as first member; management state is protected and recoverable; open reward settings are not invented.
- **Open decisions:** Partition strategy per model, maximum network size, backup location/retention and owner recovery authority.

## WP-NET-JOIN-001 — Existing-network admission and resource allocation

- **Objective:** Enable another computer to request and safely join an existing network.
- **Scope:** Network ID/invitation; model/resource information; hardware and stage-capacity assessment; CPU/GPU/RAM/VRAM/bandwidth limits; join request, owner approval, node registration and user pause/withdrawal.
- **Exclusions:** Treating a display alias as authenticated identity; admitting a node without the documented approval.
- **Source:** Section 10.
- **Deliverables:** Join/invitation flow, admission contract, resource limits and node-registration criteria.
- **Acceptance:** All seven source steps are covered; resource limits are enforced; identity differs from alias; approval precedes active membership; user can stop participation.
- **Open decisions:** Invitation expiry, approval timeout, multi-network membership and admission limits.

## WP-NET-OPS-001 — Network monitoring, tests, coverage and failover

- **Objective:** Make a compute network observable and recoverable when nodes slow down, fail or disconnect.
- **Scope:** Network status/start/stop; communication, throughput, latency, packet loss, runtime, stage order, end-to-end test and uncovered-stage test; normal/backup coverage; node ID/alias/stages/resources/status/last seen; backup assignment and failover using last valid computation state.
- **Exclusions:** Treating assigned coverage as guaranteed availability or failover as correct without state validation.
- **Source:** Section 11 and risks in 29.
- **Deliverables:** Network Test specification, node/coverage state model, monitoring data contract and failover workflow.
- **Acceptance:** Every test dimension is verifiable; normal and backup coverage are separate; all documented connection states exist; failover prevents stale/inconsistent output and records recovery.
- **Open decisions:** Health thresholds, heartbeat/retry intervals, checkpoint format and backup selection.

## WP-MARKET-001 — Explore marketplace and provider discovery

- **Objective:** Help customers discover active local and network AI services and inspect public service information.
- **Scope:** Provider/service registry; listing fields (name, provider, category, specialty, AI type, model, price, expected time, availability, reputation and popularity); categories/search/filters; public detail and Continue entry to order inputs.
- **Exclusions:** Treating a proposed distributed registry as a chosen technology; exposing private inputs/delivery data in public listings.
- **Source:** Section 12 and Explore navigation in 3.
- **Deliverables:** Listing schema, provider-discovery contract, search/filter behavior and service detail requirements.
- **Acceptance:** All listing fields and discovery capabilities are covered; local/network are distinguishable; availability is visible; details precede input collection; public/private data are separated.
- **Open decisions:** Registry topology, ranking, moderation and discovery freshness.

## WP-ORDER-001 — Order intake, payment verification and lifecycle

- **Objective:** Create traceable orders and start execution only after the relevant payment condition is met.
- **Scope:** Customer inputs; order/contract; agreed price and exchange-rate snapshot; native-coin in-app confirmation/finality; escrow where applicable; external-payment acceptance and verification queue; provider approval; all source order states; cancellation, refund and dispute pathways.
- **Exclusions:** Auto-verifying external payment; treating pending chain transactions as final; inventing FX, escrow-release or refund policy.
- **Source:** Sections 12.2–12.4 and 13; open decisions in 31.2.
- **Deliverables:** Order state machine, payment adapter contracts, price snapshot rules, escrow/refund/dispute requirements.
- **Acceptance:** Source states and 13-step flow are covered; execution queues only after required payment; on-chain finality differs from external verification; payment and pricing snapshots are auditable; disputed/refund orders cannot silently settle.
- **Open decisions:** FX source, external evidence, expiry, escrow/release, rejection/refund, ETA measurement and dispute resolution.

## WP-DELIVERY-001 — Secure deliverable upload and private customer download

- **Objective:** Deliver completed files privately to the customer associated with the order.
- **Scope:** Multi-file/package upload; Order/Delivery IDs, name/type/size/version/time and SHA-256; private object storage, encryption at rest, file-type/size checks, security scanning, private reference, authenticated short-lived/revocable link, Customer/Order authorization, download history and notifications.
- **Exclusions:** Public buckets/chain file payloads or relying only on an unguessable URL.
- **Source:** Sections 13, 21, 23.5 and 28.4.
- **Deliverables:** Upload/manifest contract, private storage/access-control design, scanning/hash checks and download workflow.
- **Acceptance:** Required metadata and hashes are recorded; only the order customer can download; server authorization is checked per request; links expire or can be revoked; private file/location/URL are not public-chain data.
- **Open decisions:** Storage provider/topology, file policy, retention/deletion and scan tooling.

## WP-FEEDBACK-001 — Customer feedback, no-feedback and dispute entry

- **Objective:** Capture customer response without inferring satisfaction or provider misconduct from silence or a single negative response.
- **Scope:** Satisfied, Not Satisfied and No Feedback; timestamps/signature; review deadline; delivery review; distinct Dispute initiation for alleged contract breach; linkage to Reputation and settlement.
- **Exclusions:** Automatically converting silence into positive/negative feedback; treating Not Satisfied alone as proof of misconduct.
- **Source:** Sections 13, 22 and 23.6.
- **Deliverables:** Feedback state machine, review workflow, No Feedback and dispute hand-off contract.
- **Acceptance:** All three outcomes exist; no-feedback leaves Reputation pending unless an approved policy decides otherwise; negative feedback applies the defined allocation but is not proof of a violation; dispute is separate.
- **Open decisions:** Review deadline, No Feedback disposition, dispute evidence/authority and interaction with escrow/refund.

## WP-IDENTITY-001 — Node identities, roles and ownership boundaries

- **Objective:** Establish distinct, verifiable identities and permissions for network participants and node roles.
- **Scope:** Compute-node and Network Owner identity; Blockchain Full Node, Blockchain Validator and AI Task Verification Node; role-specific keys/credentials/permissions/ownership; separate staking, reputation, rewards and penalties; alias handling.
- **Exclusions:** Letting one role or alias confer another role's authority; choosing unapproved cryptographic algorithms.
- **Source:** Sections 9.3, 10, 14.3 and 17; key separation in 15 and 28.
- **Deliverables:** Identity/role model, authentication/authorization contracts, key lifecycle and ownership/Sybil inputs.
- **Acceptance:** All roles are distinct; aliases are non-authoritative; a computer may hold multiple roles without merging identity, key, stake or sanctions; proof/revocation requirements are explicit.
- **Open decisions:** Identity issuance/rotation/recovery, proof of ownership and Sybil-resistance mechanism.

## WP-CHAIN-001 — Blockchain core, native coin and governance

- **Objective:** Specify and implement the independent blockchain and native coin.
- **Scope:** Core, P2P, transaction validation, consensus, native coin, block rewards, fees, explorer, RPC/API, governance, Coin Rules, finality semantics and separate accounting for protocol issuance, transaction fees and project verification fees.
- **Exclusions:** Assuming consensus, supply, price, liquidity, exchange listing or Tokenomics not approved; making an exchange mandatory.
- **Source:** Sections 14.2 and 15; open decisions in 31.4.
- **Deliverables:** Chain component contracts, transaction/finality model, coin-rule schema, governance/economics register and order/settlement integration.
- **Acceptance:** All listed components are covered; native coin differs from an off-chain score; payment finality is explicit; reward/fee sources remain separate; unapproved values remain open.
- **Open decisions:** Consensus, supply, utility, external use, exchange/bridge, platform fee, fee split, base issuance and legal constraints.

## WP-WALLET-001 — Blockchain overview and wallet workflows

- **Objective:** Provide blockchain and wallet information architecture in the Windows application.
- **Scope:** Create/import/restore; address/key generation; secure setup and backup; send/receive; amount/recipient/network/fee/memo confirmation; signed/broadcast/pending/confirmed/finalized/failed states; history categories; wallet/chain overview; separation of wallet keys from node/validator/owner/treasury keys.
- **Exclusions:** Storing readable private keys on an app server; exchange implementation; silently resolving custody inconsistency.
- **Source:** Section 16 and key separation requirements in 15 and 28.
- **Deliverables:** Wallet screens/flows and transaction contracts, key lifecycle/backup rules and history model.
- **Acceptance:** All listed screens/states are represented; details are confirmed before signing; keys are separated; private keys are not readable by the app server; custody conflict is resolved before final approval.
- **Open decisions:** Section 16.2 describes Self-Custody while Section 31.4 asks Self-Custody vs Managed; recovery and network configuration also need approval.

## WP-VALIDATOR-001 — Blockchain Validator Center and staking lifecycle

- **Objective:** Manage blockchain consensus validators independently from compute-node membership.
- **Scope:** Overview, registration, identity/consensus key, required stake, hardware/network/software eligibility, registration transaction, activation queue, statuses, performance/rewards/penalties, exit, unbonding and slashing-related states.
- **Exclusions:** Inventing stake amounts, unbonding duration or consensus duties.
- **Source:** Sections 17.2 and 18.
- **Deliverables:** Eligibility/registration contract, lifecycle state machine and staking/performance records.
- **Acceptance:** All eight registration steps and source statuses are represented; stake/keys are validator-specific; exit stops new duties but completes active commitments; release occurs only after policy checks.
- **Open decisions:** Minimum stake, hardware/network thresholds, duty schedule, unbonding, slashing and performance thresholds.

## WP-VERIFY-NODES-001 — AI Task Verification Center and committee selection

- **Objective:** Register task-verification nodes and select two independent committees for settlement review.
- **Scope:** Verification identity/stake/software/availability/conflict declarations; eligibility dashboard/history; verifiable-random selection; ownership/Sybil controls; conflict screening; first 100-member committee and a second disjoint 100-member audit committee; Pending Verification if capacity is insufficient.
- **Exclusions:** Equating task verifiers with blockchain validators; accepting fewer than 100/200 while showing a complete committee; treating a vote alone as proof of honesty.
- **Source:** Sections 17.3 and 19; committee rules in 24 and 25.
- **Deliverables:** Verification-node model, eligibility rules, selection algorithm requirements, disjoint-set/capacity rules and audit trail.
- **Acceptance:** Role is independent of blockchain validator; selection is verifiable and conflict-aware; committees do not overlap; shared ownership/Sybil limits are considered; insufficient capacity remains Pending Verification.
- **Open decisions:** Randomness source, owner linkage, stake, eligibility, replacement and re-review policy.

## WP-REPUTATION-001 — Popularity allocation, Good/Bad Reputation and locks

- **Objective:** Apply the source-defined feedback allocation to auditable Good and Bad Reputation balances.
- **Scope:** Popularity 10–70% fixed in each accepted order; C/P/G/B/D variables; Satisfied/Not Satisfied formula; 10 percentage-point Bad allocation on Not Satisfied; separate Good/Bad accounts and locks; Reputation = Bad/Good, N/A if Good is zero.
- **Exclusions:** Treating 10 percentage points as 10% of P; automatically burning/transferring locked balances; equating popularity with customer satisfaction or validator approval.
- **Source:** Sections 8, 20 and 22; financial fields in 23.
- **Deliverables:** Formula contract, order snapshot/allocation rules, Good/Bad balance/lock model and test examples.
- **Acceptance:** Satisfied: G=C×P/100, B=0, D=C−G. Not Satisfied: B=C×10/100, G=C×(P−10)/100, D=C−G−B. Network fee excluded from C; P is immutable per order; Good=0 displays N/A; locked funds are not spendable.
- **Open decisions:** No Feedback, release conditions, burn/transfer/penalty authority, disputes/Frozen and selection of P within the allowed range.

## WP-SETTLEMENT-RECORD-001 — Project Settlement Record and integrity

- **Objective:** Bind contract, payment, delivery, feedback, Reputation, verification and payout evidence into one auditable record.
- **Scope:** All Section 23 fields; version/hash; signatures tied to exact versions; private full-record storage; explicitly permitted on-chain identifiers/financial data/cryptographic roots; status transitions including Frozen; private references without public URLs or customer data.
- **Exclusions:** Public-chain publication of prompts, personal data, files or download links; treating a changed record as the same signed version.
- **Source:** Section 23 and integrity/privacy requirements in 21, 24 and 25.
- **Deliverables:** Record schema, version/hash/signature contract, private/on-chain boundary and state machine.
- **Acceptance:** Every Section 23 field is covered; signatures bind exact versions; private data stays off public chain; on-chain fields are enumerated; source states and Frozen are represented.
- **Open decisions:** Storage technology, retention, data minimization, schema evolution and correction/review authority.

## WP-VERIFY-STAGE1-001 — First committee and 80/20 verification

- **Objective:** Verify the settlement record using the first independent 100-member committee.
- **Scope:** Review order/payment/popularity/reputation/delivery/hash/rewards/integrity evidence; signed votes bound to record version hash; 100 valid votes; at least 80 approvals and at most 20 rejections; protocol-calculated closure.
- **Exclusions:** Counting missing votes as approvals; letting the last voter unilaterally decide closure; conflating computation checking and blockchain consensus.
- **Source:** Section 24.
- **Deliverables:** Review contract, signed-vote format, threshold evaluator and closure event/evidence.
- **Acceptance:** 100 eligible independent members; signatures bind committee, record version and vote; 80/20 applies to 100 valid votes; protocol computes closure; record mutation invalidates signatures of the former version.
- **Open decisions:** Vote timeout, replacement, evidence format and appeal/re-review trigger.

## WP-VERIFY-STAGE2-001 — Independent audit committee and 90/10 verification

- **Objective:** Audit the first-stage process with a second independent 100-member committee.
- **Scope:** Check first-stage signatures/independence/counts/80-20 arithmetic, popularity and Reputation formulas, contract amounts, immutability and duplicate-payment prevention; 100 valid votes; 90 approvals/10 rejections; Frozen and Re-Review on failure.
- **Exclusions:** Repeating first-stage votes without audit; overlapping committees; releasing settlement after failed audit.
- **Source:** Section 25.
- **Deliverables:** Audit workflow/evidence contract, 90/10 evaluator and Frozen/re-review transitions.
- **Acceptance:** Second committee has 100 members and no overlap; it audits required first-stage evidence; exactly 100 valid votes; 90/10 applied correctly; failure freezes payment and routes to Dispute/Re-Review.
- **Open decisions:** Audit timeout/replacement, re-review selection and Frozen-clearance criteria.

## WP-SETTLEMENT-FINAL-001 — Idempotent final settlement and payment distribution

- **Objective:** Distribute funds only after required verification stages pass.
- **Scope:** Confirm payment; finalize record; verify Reputation allocations/locks; calculate platform/provider/network-owner/compute/verification/blockchain rewards; release permitted escrow; record reward transactions and Final Settlement Hash; announce completion.
- **Exclusions:** Duplicate payment; release on incomplete/failed verification; client-side unaudited settlement.
- **Source:** Section 26 and financial record in 23.
- **Deliverables:** Final-settlement state machine, payout/escrow contracts, idempotency keys and reconciliation evidence.
- **Acceptance:** Both verification stages must pass first; every payout binds to Settlement Record ID; retries cannot pay twice; amounts reconcile to approved sources; escrow and final hash are recorded.
- **Open decisions:** Platform fee, provider/network-owner splits, compute/verification shares, treasury contribution, refunds and rounding.

## WP-PROTOCOL-REWARDS-001 — Twenty-year protocol incentive schedule

- **Objective:** Specify the proposed 20-year incentive curve while keeping funding streams separate.
- **Scope:** Linear reduction by five percentage points per completed protocol year; block-height/protocol time; multiplier max(0, 100−5×completed years); role allocation between validators and task verifiers; separation from transaction fees, project-verification fees and compute rewards.
- **Exclusions:** Local device clocks as protocol time; treating the proposed curve or role split as approved Tokenomics; ending all node income at year 20.
- **Source:** Section 27 and reward distinctions in 8 and 15.
- **Deliverables:** Emission schedule, protocol-year calculation, source accounting and role-allocation decision record.
- **Acceptance:** All 21 year points represented; year 10 is 50% and year 20 is 0%; chain-derived time; non-issuance income remains distinct; unknown base amounts/splits are not hard-coded.
- **Open decisions:** Base reward, role split, supply cap, genesis/start time and economic simulation.

## WP-SECURITY-001 — Cross-cutting security, privacy and trust controls

- **Objective:** Translate the source's security and privacy principles and named threats into verifiable system-wide requirements.
- **Scope:** Assets/actors/privileges/trust boundaries; encrypted communication; node auth; replay/tampering; no execution of unknown peer code; sandboxing; signed software/model integrity; prompt-injection boundary; data minimization; wallet/key protection; private-file authorization; Sybil/collusion/DoS/partition/double-spend/impersonation risks; detection, containment and recovery.
- **Exclusions:** Claiming end-to-end confidentiality for distributed intermediate data without proof; inventing cryptographic algorithms; calling proposed controls implemented/effective without tests.
- **Source:** Sections 1.2, 6.2, 9, 14–19 and 21–29.
- **Deliverables:** Threat model, trust/data-flow map, preventive/detective/recovery controls, security acceptance checks and residual-risk register.
- **Acceptance:** Named threats/assets mapped; proposed controls separated from implemented controls; intermediate-data visibility disclosed; private-file/key boundaries specified; residual risks and approval owners recorded.
- **Open decisions:** Cryptography, sandbox design, key custody/recovery, retention, confidential computing and security governance.

## WP-MAINNET-READINESS-001 — Integrated security, economic and legal readiness gate

- **Objective:** Establish an evidence-based go/no-go review before any public/mainnet release.
- **Scope:** Trace the proposed development stages; verify local/distributed benchmarks and integrated marketplace/order/delivery/settlement/reputation/committee flows; review protocol economics, security, privacy and applicable legal/regulatory requirements; record risk acceptance and blockers.
- **Exclusions:** Deploying mainnet within this planning task; treating Section 30 sequencing as mandatory graph edges; deciding legal/economic questions without qualified review and owner approval.
- **Source:** Sections 15.5 and 27–31, especially 29–31.
- **Deliverables:** Readiness checklist, integration evidence, risk/decision register and go/no-go recommendation.
- **Acceptance:** All ten proposed development stages trace to tasks; security/economic/legal reviews precede mainnet; performance claims have benchmark evidence; open owner decisions remain blockers; mainnet is not marked ready while material risks/reviews remain open.
- **Open decisions:** Jurisdictions, native-coin regulation, exchange/payment obligations, final Tokenomics, security audit scope and go-live authority.

## Source-to-task traceability

This matrix is a traceability index, not a dependency list. A source section may map to multiple tasks where it defines shared requirements.

| Source area | Task IDs |
|---|---|
| Introductory purpose, source boundaries and proposal handling | WP-ARCH-001, WP-MODEL-001, WP-SECURITY-001, WP-MAINNET-READINESS-001 |
| 1. Purpose, pipeline architecture and management boundary | WP-ARCH-001 |
| 2. Windows, English UI, open source, model sources/licensing | WP-ARCH-001, WP-APP-001, WP-MODEL-001 |
| 3. App shell, navigation, dashboard and settings | WP-APP-001 |
| 4. Model catalogue and licence policy | WP-MODEL-001 |
| 5. Local inference and hardware compatibility | WP-AI-LOCAL-001 |
| 6. Defined Tasks, parameters and prompt templating | WP-AI-TASK-001 |
| 7. Task and order history | WP-AI-HISTORY-001 |
| 8. Rewards and Reputation overview | WP-REWARD-001, WP-REPUTATION-001 |
| 9. Network creation and owner management | WP-NET-CREATE-001, WP-IDENTITY-001 |
| 10. Network joining/admission | WP-NET-JOIN-001 |
| 11. Network dashboard, testing and failover | WP-NET-OPS-001 |
| 12. Explore/provider discovery/payment modes | WP-MARKET-001, WP-ORDER-001 |
| 13. Order, payment, execution, delivery and feedback | WP-ORDER-001, WP-DELIVERY-001, WP-FEEDBACK-001 |
| 14. Two-network architecture and role separation | WP-ARCH-001, WP-IDENTITY-001, WP-CHAIN-001 |
| 15. Blockchain core, coin, fees and economy | WP-CHAIN-001 |
| 16. Blockchain and Wallet UI/flows | WP-WALLET-001 |
| 17. Node roles and responsibility boundaries | WP-IDENTITY-001, WP-VALIDATOR-001, WP-VERIFY-NODES-001 |
| 18. Validator Center and staking | WP-VALIDATOR-001 |
| 19. Task Verification Center and committees | WP-VERIFY-NODES-001 |
| 20. Popularity and Reputation calculations | WP-REPUTATION-001 |
| 21. Private file delivery and storage | WP-DELIVERY-001 |
| 22. Customer feedback and Reputation effects | WP-FEEDBACK-001, WP-REPUTATION-001 |
| 23. Project Settlement Record | WP-SETTLEMENT-RECORD-001 |
| 24. First-stage 80/20 | WP-VERIFY-STAGE1-001 |
| 25. Second-stage 90/10 audit | WP-VERIFY-STAGE2-001 |
| 26. Final Settlement | WP-SETTLEMENT-FINAL-001 |
| 27. Twenty-year protocol rewards | WP-PROTOCOL-REWARDS-001, WP-REWARD-001 |
| 28. Security and privacy | WP-SECURITY-001 |
| 29. Risks and technical limitations | WP-ARCH-001, WP-NET-OPS-001, WP-SECURITY-001, WP-MAINNET-READINESS-001 |
| 30. Proposed development stages | WP-MAINNET-READINESS-001 and relevant feature workstreams; order is advisory |
| 31. Open decisions | Relevant task-specific open-decision entries and register below |
| 32. Long-term vision and settlement principle | WP-ARCH-001, WP-SETTLEMENT-RECORD-001, WP-SETTLEMENT-FINAL-001 |

## Consolidated open-decision register

These points remain unresolved and are not decided by WP-INIT-001:

1. **AI architecture:** initial models/modalities; smallest executable partition; future Tensor Parallelism; node limits; multi-network membership; runtime and benchmark choice.
2. **Marketplace/orders:** provider registry topology; response-time definition; rejection/refund/dispute rules; external-payment evidence; FX source; No Feedback deadline/disposition; price snapshots and timeout behavior.
3. **Verification/rewards:** verifiable randomness; ownership/Sybil/collusion controls; committee capacity/replacement; stake; Compute/Verification formulas; manager/member splits; re-review selection.
4. **Blockchain/Tokenomics:** supply; consensus; base reward; validator/verifier split; fees; platform fee; treasury; coin utility/external use; exchange/bridge; stakes, unbonding and penalties.
5. **Reputation/settlement:** P selection within 10–70%; No Feedback; Good/Bad release; burn/transfer/penalty authority; Frozen resolution; dispute/escrow interactions; idempotency and rounding.
6. **Wallet custody:** Section 16.2 describes Self-Custody while Section 31.4 still asks Self-Custody versus Managed. Owner approval is required; this conflict is not silently resolved.
7. **Committee governance:** insufficient 200-node capacity; unavailable selected nodes; appeals; replacement and independent re-review.
8. **Legal/operations:** jurisdiction, native coin and exchange status, payment-provider rules, security audit depth, data retention and mainnet go/no-go authority.

## Catalog rules

- Add/split tasks only when grounded in the source or a verified project need.
- Keep descriptions, scope, exclusions, outputs, acceptance, source references and open decisions here or in task-status.md; never put these in graph task objects.
- Do not duplicate dependencies or statuses in the catalog.
- Only the Senior Engineer may change this catalog or dependency-graph.json.
- Preserve traceability when tasks are split, merged, changed or removed.
- Create a task workspace only after the Senior Engineer selects that task.
- Preserve the user's intended meaning; record uncertainty rather than silently resolving it.
