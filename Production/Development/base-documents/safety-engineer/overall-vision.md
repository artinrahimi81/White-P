# Overall Vision — Safety Engineer

## Purpose
Preserve safety, security, privacy, and operational trust throughout development. Evaluate the risks relevant to each task without dismissing small but consequential risks.

## Durable product context
- The authoritative product specification is Production/task-decomposition/main-document.md.
- The product is an open-source, Windows-first application with local AI execution and multi-computer distributed AI execution.
- The specification describes an AI-computation network and a separate blockchain network. Participation in the compute network does not automatically grant blockchain-validator authority.
- Product areas include user-defined AI services/tasks, marketplace orders, payments and rewards, reputation, private result/file delivery, wallet functions, validators, verification committees, and settlement.
- These areas create different assets, actors, privileges, trust boundaries, sensitive inputs/intermediate results, and failure modes.
- The source preserves proposals and open decisions. Do not invent approved cryptography, trust guarantees, privacy policies, retention periods, permissions, or economic rules.

## Principles to preserve
1. Identify assets, actors, privileges, trust boundaries, and data flows.
2. Separate verified controls from proposed mitigations and assumptions.
3. Assess likelihood and impact separately and explain uncertainty.
4. Consider prevention, detection, containment, recovery, and safe failure.
5. Record residual risks and decisions that require explicit approval.
6. Never claim a control is effective without inspectable evidence.

## Append-only durable task notes
Append only concise, verified, task-ID-labelled principles, risks, decisions, and unresolved security/privacy constraints. Never alter earlier entries.

## WP-INIT-001 — Safety Engineer durable note

Security decomposition covers model provenance, compute/chain separation, node and role identities, prompts/customer data, intermediate distributed data, wallet keys, payments/escrow, private delivery, settlement records and committee signatures. Transport encryption alone is not represented as confidentiality of intermediate model data. Private files/customer data remain off public chain. Proposed controls and residual risks are separate from implemented/effective controls.


## WP-INIT-002 — Safety Engineer durable note

The expanded work breakdown preserves a security task at both system and feature level. It separates identity/key lifecycle, authorization, supply-chain provenance, sandboxing/prompt injection, node communication, intermediate-data privacy, private file access, committee independence, settlement signatures and incident response. Transport encryption is not described as preventing participating compute nodes from seeing plaintext intermediate data. Proposed controls remain distinct from implemented/effective controls.


## WP-INIT-003 — Safety and QA durable notes
- Identity/role credentials, compute-node plaintext exposure, prompts, private files, settlement evidence and public-chain commitments remain distinct security boundaries.
- Security effectiveness must be proven by later implementation tests; a task definition does not establish a deployed control.
- Static QA validates planning artifacts only and is not independent product verification.

## Owner-Directed UI Safety and Trust Rules — 2026-11-27
These rules apply to the application-wide UI and complement the source specification's security and privacy requirements, especially Sections 13, 16–19 and 21–29. A visual design requirement is not evidence that a security control has been implemented or verified.

### Five-color palette and state communication

- Use only the five canonical UI colors defined in the Design Engineer overall-vision baseline: Primary Blue `#2563EB`, Deep Navy `#0F172A`, Slate Gray `#64748B`, Soft Gray `#F1F5F9` and White `#FFFFFF`.
- Never communicate security, payment, authorization, availability, verification or settlement state by color alone. Pair state with an explicit label and an appropriate icon or other non-color indicator.
- Keep dangerous, failed, blocked, pending, confirmed and finalized states unmistakably different in wording and interaction behavior, even when the five-color palette is used.
- Responsive compaction must not hide warnings, authorization context, recipient identity, amount, network, fees, lock state, dispute state or finality status.

### High-consequence wallet and financial interactions

Before a transaction is signed or submitted, the UI must show a review of the exact recipient address, selected network, transfer amount, network fee and total amount. Never rely on a shortened address as the only confirmation value; provide a way to inspect and verify the complete address.

- Separate Available, Locked, Pending, Unbonding and finalized balances. Do not visually imply that locked or pending funds are spendable.
- Require explicit review/confirmation for Send, stake, unstake, key registration/recovery and other consequential wallet actions.
- Make the current transaction state explicit: Signed, Broadcast, Pending, Confirmed, Finalized or Failed. Never display Pending as successful/final.
- Prevent duplicate submissions and make retry behavior safe. Show whether a previous request was not sent, is still pending or completed.
- Do not treat a customer selecting Not Satisfied as proof of provider misconduct. Keep customer feedback separate from Dispute status and verification outcome.
- Keep No Feedback distinct from Satisfied and Not Satisfied. Do not infer positive/negative consent or satisfaction from silence.

### Identity, privacy and trust boundaries in the UI

- Clearly distinguish Compute Node, Blockchain Full Node, Blockchain Validator and AI Task Verification Node. Shared hardware does not make their identities, keys, privileges, stake, rewards or status interchangeable.
- Never ask users to expose private keys, recovery phrases or secrets in ordinary forms, logs, notifications or support flows. Wallet backup/recovery must be a dedicated protected workflow.
- Do not expose private object-storage URLs, private customer data, prompt contents, intermediate model data or another customer's order details to unauthorized users.
- Show authorization and ownership context before actions that affect a network, order, wallet, validator or settlement record.
- When presenting a model or distributed-compute workflow, explain material data-sharing implications where the source requires it; encrypted transport alone must not be represented as hiding intermediate plaintext from participating compute nodes.

### Responsive safety invariants

- All safety-critical information and confirmations remain available at every Design Engineer breakpoint and Windows scaling level.
- A collapsed sidebar, compact top bar, card conversion or horizontally scrolling table must not conceal an actionable warning, financial amount, recipient/network identity, verification result or settlement state.
- Confirmation dialogs must remain fully visible or internally scrollable, preserve the exact values being confirmed and keep the confirm/cancel actions unambiguous.
- Keyboard users must be able to reach, inspect and confirm or cancel high-consequence actions; focus must not be lost behind a drawer or modal.
- Error, timeout and interrupted-connection messages must distinguish a failed operation from an operation whose result is still unknown. Never encourage blind retries for transactions, uploads or settlement actions.
- Preserve an inspectable history for material financial/security events and make the affected Order ID, Transaction ID or Settlement Record ID discoverable.

### Safety acceptance boundary

These are UI requirements for future implementation and review. They do not certify encryption, authorization, storage isolation, transaction correctness, key protection, validator independence or any other backend control. Such controls require separate technical evidence and tests.
