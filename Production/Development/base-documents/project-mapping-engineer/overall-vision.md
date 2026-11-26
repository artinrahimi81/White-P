# Overall Vision — Project Mapping Engineer

## Purpose
Maintain a traceable, evidence-based map of requirements, product components, workflows, ownership, inputs/outputs, interfaces, and actual implementation state.

## Durable product context
- The authoritative product specification is Production/task-decomposition/main-document.md and contains 32 numbered sections.
- The source covers product goals and architecture, Windows principles, UI, model catalogue/licensing, local and distributed inference, task/service marketplace workflows, orders/delivery, rewards/reputation, blockchain/wallet, validator and task-verification roles, settlement, privacy/security, risks, proposed development phases, open decisions, and long-term vision.
- The product has two distinct but interacting infrastructures: the AI computation network and the blockchain network.
- Pipeline Parallelism is the stated base model-distribution concept; it must not be conflated with Tensor Parallelism.
- Proposed items and open decisions must not be represented as approved behavior.

## Principles to preserve
1. Trace each source requirement to task IDs, components, workflows, interfaces, outputs, and acceptance evidence.
2. Inspect real files and observable behavior before describing current state.
3. Keep current state and target state visibly separate.
4. Identify owners, inputs, outputs, interfaces, data/control flows, and external dependencies.
5. Detect missing, duplicated, disconnected, ambiguous, or orphaned requirements/components.
6. Reference real source paths and evidence; label unknowns honestly.
7. Preserve traceability when tasks/components are split, merged, changed, or removed.

## Append-only durable task notes
Append concise task-ID-labelled maps, traceability changes, verified component relationships, and durable unknowns. Never rewrite prior entries.

## WP-INIT-001 — Senior Engineer durable note

The specification is decomposed into 27 bounded product-development tasks plus WP-INIT-001. The catalog maps all 32 numbered sections, separates current repository state from target product state, and preserves unresolved decisions. The dependency graph is the sole authority for IDs, genuine direct prerequisites and status. Role reviews were same-assistant sequential passes; independent agent execution is not claimed.

## WP-INIT-001 — Project Mapping Engineer durable note

Traceability covers introductory/final material and every numbered source section. The product remains a Windows-first local/distributed AI application with a distinct but connected blockchain network. Pipeline Parallelism is not conflated with Tensor Parallelism. The inspected repository is documentation/process-only; target components are not described as implemented. Wallet custody and other unresolved decisions remain explicit.


## WP-INIT-002 — Senior Engineer durable note

The original completed WP-INIT-001 is preserved. WP-INIT-002 deepens its output into 27 domain specification gates and 137 independently schedulable child work packages. The graph remains the sole authority for IDs, direct dependencies and statuses; unresolved product decisions remain open. Role reviews were same-assistant sequential passes, not independent agent execution.

## WP-INIT-002 — Project Mapping Engineer durable note

The expanded catalog maps the 32-section source to 166 task identities. Each original domain -001 task is the specification/contract baseline for its children. Child tasks have one primary owner, source references, objective, scope, exclusion, output, acceptance and direct prerequisites. Current repository state remains distinct from intended product state; no application implementation is claimed.


## WP-INIT-003 — Mapping, intent and orchestration durable notes
- Task breakdown now has 27 domain specification gates, 137 intermediate roll-up packages and 280 execution-level leaves.
- Parent/child grouping is not a blocking dependency: parents wait for leaves; leaves depend on actual domain prerequisites and WP-INIT-003. This avoids cycles.
- Product scope and unresolved decisions remain preserved; planning does not imply implementation.
