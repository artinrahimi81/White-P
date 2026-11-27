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

## Owner-Directed Application UI Map — 2026-11-27
This map is derived from the read-only product specification, not from assumptions about implemented screens. Its primary source is Section 3, with supporting workflows in Sections 5–13 and 16–28. The current repository's documentation/process artifacts must not be represented as a completed product UI.

### Canonical application shell

Every route belongs to one shared shell:
- **Navigation Sidebar:** stable global navigation to the product areas.
- **Top Bar:** Page Title, Breadcrumb Navigation, Internet Status, Blockchain Synchronization Status, Wallet Balance, Notifications and Account Menu; show the Network selector when multiple networks are active.
- **Main Content Area:** the current page's content, actions, state and supporting detail.

The shell is shared, while page content is owned by its functional module. Do not duplicate global navigation or treat a page-level subsection as a new independent application shell.

### Source-traceable page and module map

| Global destination | Source-defined pages and capabilities | Primary source sections |
|---|---|---|
| Dashboard | Overview; Account Overview; AI Overview; Orders Overview; Recent Activity; Quick Actions | 3.5, 11 |
| AI Workspace | Run Model Locally; Create a Network; Join an Existing Network; Defined Tasks; Completed Tasks History; Rewards | 3.2–3.3, 5–11 |
| Explore | Discover Services; Categories; Search and Filters; service detail and Continue/input flow | 3.2, 6, 12 |
| Orders & Deliveries | My Orders; Incoming Orders; Deliveries; Disputes; order lifecycle and delivery history | 3.2, 7, 12–13, 21–26 |
| Blockchain & Wallet | Overview; Wallet; Send; Receive; Transaction History; Reputation; Reputation Bonds; Validator Center; Task Verification Center; Coin Rules; Blockchain Explorer | 3.2, 8, 14–20, 23–28 |
| Settings | Account; Security; Wallet Security; Notifications; Privacy; Storage; Application Preferences | 3.2, 16, 21, 28 |

Dashboard and Orders & Deliveries are cross-cutting operational destinations in the detailed information architecture. They do not replace the four primary areas named in the source.

### Cross-module entities and traceability

Keep these product entities distinct when mapping pages, components, owners and data flows:
- **Model** and **Model Version** — catalog, licensing and local/distributed execution.
- **Compute Network** and **Compute Node** — network creation, joining, resource contribution, node status and model stages.
- **Defined Task** and **Service** — provider configuration, input parameters, prompt and Explore listing.
- **Order** and **Delivery** — customer request, payment, execution, file delivery, feedback, dispute and history.
- **Wallet**, **Transaction**, **Reputation** and **Stake** — available/locked balances, transfers, rewards, validator staking and reputation locks.
- **Settlement Record** — order-linked contract, payment, delivery, feedback, validation and final settlement evidence.
- **Blockchain Full Node**, **Blockchain Validator** and **AI Task Verification Node** — separate roles, identities, eligibility and reward paths.

The shared shell provides navigation and global context; it does not merge these entities or their state machines. In particular, compute-network status must remain distinguishable from blockchain synchronization; transaction Pending must remain distinguishable from Confirmed and Finalized; and Satisfied, Not Satisfied and No Feedback must remain distinct customer outcomes.

### UI traceability and change impact

For every new or changed UI route/component:
1. map it to the exact source section and requirement;
2. identify the owning module and shared-shell dependencies;
3. record its user goal, input/output, state transitions and consuming components;
4. identify linked entities and their data/control-flow contracts;
5. map each acceptance criterion to visible behavior and test evidence; and
6. identify all existing routes/components affected by a shared component or contract change.

The same page header, sidebar, top bar, status component, form, table and dialog should be mapped once as shared components and referenced by consuming modules, not re-described as independent copies. Keep observed current implementation separate from the source-defined target architecture and preserve all open decisions as open.
