# Execution-Level Work Breakdown — Part 4

> These work packages decompose blockchain, wallet, validator, committee, protocol reward, security and launch-readiness packages. Parent IDs remain stable and are acceptance roll-ups; child tasks depend only on real prerequisite outputs and the WP-INIT-003 decomposition baseline.

## WP-CHAIN-002 — Consensus, finality and protocol decision package

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-CHAIN-003 — P2P peer protocol and network lifecycle

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-CHAIN-004 — Transaction validation, mempool and replay protection

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-CHAIN-005 — Native coin ledger, issuance and fee accounting

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-CHAIN-006 — RPC/API, explorer and public data boundary

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-CHAIN-007 — Coin Rules, governance and protocol upgrades

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-CHAIN-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-WALLET-002 — Wallet custody decision and key threat model

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-WALLET-003 — Wallet creation, import and restore workflow

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-WALLET-004 — Encrypted backup, recovery and key rotation

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-WALLET-005 — Transaction construction, fee and signing boundary

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-WALLET-006 — Send/receive status tracking and history

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-WALLET-007 — Wallet/blockchain overview balance projection

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-WALLET-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VALIDATOR-002 — Validator eligibility and hardware/network rules

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VALIDATOR-003 — Validator registration, consensus key and activation

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VALIDATOR-004 — Stake, unstake, unbonding and slashing lifecycle

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VALIDATOR-005 — Validator duty telemetry, rewards and appeal records

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VALIDATOR-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VERIFY-NODES-002 — Task-verifier registration, eligibility and stake

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VERIFY-NODES-003 — Conflict-of-interest, ownership and exclusion rules

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VERIFY-NODES-004 — Verifiable randomness and committee-selection proof

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VERIFY-NODES-005 — Two disjoint 100-member committees

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VERIFY-NODES-006 — Committee capacity, absence and replacement fallback

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-VERIFY-NODES-007 — Verifier dashboard, assignments and reward history

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-VERIFY-NODES-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-PROTOCOL-REWARDS-002 — Protocol-year clock and completed-year calculation

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-PROTOCOL-REWARDS-003 — Emission multiplier, base reward and supply constraints

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-PROTOCOL-REWARDS-004 — Protocol reward role split and eligibility

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-PROTOCOL-REWARDS-005 — Reward accrual, claim and audit integration

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-PROTOCOL-REWARDS-006 — Emission simulation and adversarial economic review

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-PROTOCOL-REWARDS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-002 — Threat model, asset inventory and trust boundaries

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-003 — Secrets, key separation and signing policy

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-004 — Software/model provenance and secure updates

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-005 — Sandboxing, resource isolation and prompt injection

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-006 — Node communication and intermediate-data privacy

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-007 — Storage, download authorization and data retention

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-SECURITY-008 — Security monitoring, incident response and recovery

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-SECURITY-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-MAINNET-READINESS-002 — Requirements-to-release traceability and integration matrix

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-MAINNET-READINESS-003 — Performance, capacity and distributed benchmark program

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-MAINNET-READINESS-004 — Failure injection, resilience and recovery acceptance

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-MAINNET-READINESS-005 — Independent security review and remediation gate

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-MAINNET-READINESS-006 — Economic, legal and operational decisions

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

## WP-MAINNET-READINESS-007 — Launch checklist, staged rollout and rollback

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.

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
- **Direct prerequisites:** WP-MAINNET-READINESS-001, WP-INIT-003. Parent membership is the catalog roll-up relation and is intentionally not a child prerequisite.
