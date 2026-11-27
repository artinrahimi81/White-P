# Task Status — <TASK_ID>

> Create this file only after the Senior Engineer selects the task. Replace every placeholder, retain all required sections, and keep this document as the task's live control record. The graph remains authoritative for task ID, direct prerequisites and graph status.

## 1. Task identity and control

- Task ID: <TASK_ID>
- Task title: <TITLE_FROM_TASK_CATALOG>
- Objective: <ONE_CLEAR_OUTCOME>
- Graph status: <not_started | in_progress | done | blocked | deferred_final>
- Execution phase: <planning | specialist_execution | integration | final_review | blocked>
- Selected by: senior-engineer
- Selection reason: <WHY_THIS_TASK_IS_NEXT>
- Created at: <ISO_8601_TIMESTAMP>
- Last updated at: <ISO_8601_TIMESTAMP>
- Current normal specialist turn: <ROLE_ID_OR_NONE>
- Orchestration state: <active | completed | blocked>

## 2. Source interpretation and task boundaries

- Authoritative source references: <PATHS_AND_SECTION_IDS>
- Original user requirement: <PRESERVE_MEANING; DO_NOT_REWRITE_AS_A_DIFFERENT_REQUIREMENT>
- Objective and expected outcome: <DETAIL>
- In scope:
  - <ITEM>
- Out of scope:
  - <ITEM>
- Verified current state: <OBSERVED_FACTS_AND_PATHS>
- Intended target state: <REQUIRED_FINAL_STATE>
- Assumptions: <EXPLICITLY_LABELLED_ASSUMPTIONS_OR_NONE>
- Open decisions / unknowns: <ITEMS_OR_NONE>

## 3. Direct prerequisite verification

| Prerequisite task ID | Graph status observed | Required output/contract | Evidence inspected | Ready |
|---|---|---|---|---|
| <TASK_ID> | <done or other actual status> | <OUTPUT_NEEDED> | <PATH/COMMIT/TEST> | <yes/no> |

Do not treat a preferred sequence as a prerequisite. Do not start normal execution unless every real direct prerequisite is done. If a prerequisite ID or status is invalid, stop and report it to the Senior Engineer.

## 4. Deliverables and acceptance criteria

| ID | Required output / acceptance check | Expected result | Actual output path | Verification method | Evidence | Status |
|---|---|---|---|---|---|---|
| ACC-001 | <CHECK> | <MEASURABLE_RESULT> | <PATH_OR_PENDING> | <HOW_TO_VERIFY> | <EVIDENCE_OR_PENDING> | <pending/passed/issue_found/not_applicable/needs_consultation> |

A generated document, directory, placeholder, mock, claim or expected path is not proof of implementation. Record only actual files, behavior, commands and results. Explain every not_applicable status.

## 5. Agent execution order

Record the complete intended order before activating the first specialist. Only selected roles receive a normal turn. Keep one role active at a time unless the project owner explicitly authorizes parallel work and the Senior Engineer records collision controls.

| Order | Fixed role ID | Assigned scope and responsibility | Required deliverables | Prompt path | Work-log path | Base-document destination | State |
|---:|---|---|---|---|---|---|---|
| 1 | <ROLE_ID> | <EXACT_SCOPE> | <OUTPUTS> | agents/<ROLE_ID>.md | Tasks/<TASK_ID>/<ROLE_ID>/work-log.md | base-documents/<ONE_OF_FIVE_ROLE_IDS>/ | <queued/not_scheduled/...> |

For every role, record why it is selected or why it is not applicable. Preserve completed order entries; record any justified change as an addendum with its reason and impact.

## 6. Agent lifecycle and parameter registers

Agent states: not_scheduled, queued, active, completed, not_applicable, blocked.

For every role, retain one Markdown Group 1 row per fixed parameter from the Senior Engineer's canonical registry. Do not replace several checks with one summary row. Before activation, selected roles' fixed checks start as pending; a role judged not applicable must show every fixed check as not_applicable and include the reason. Every row records the exact check text, expected result, evidence required and status.

Parameter review states: pending, passed, issue_found, not_applicable, needs_consultation.

Normal activation_count is 0 before starting and exactly 1 after the role begins its one normal turn. Resuming an already active role from its work-log does not increment the count. Consultation-only replies do not increment it. A completed role cannot be reactivated for normal work.

### senior-engineer — mandatory coordinator; specialist review is separate

- Orchestration state: active
- Specialist-work state: <not_scheduled | queued | active | completed | not_applicable | blocked>
- Normal specialist activation_count: <0 or 1>
- Start / end: <TIMESTAMPS_OR_PENDING>
- Assigned scope (if specialist review is scheduled): <SCOPE>
- Result / hand-off: <RESULT>
- Work log: Tasks/<TASK_ID>/senior-engineer/work-log.md
- Base-document destination: <ONE_OF_FIVE_EXISTING_FOLDERS>

**Group 1 — fixed Senior Engineer parameters:** Copy SE-01 through SE-16 verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, one row per ID. Give each an expected result, required evidence and one review status.

| Parameter ID | Fixed check (copied from prompt) | Expected result | Evidence | Status |
|---|---|---|---|---|
| SE-01 | Read graph, catalog, relevant complete source, existing task records, all role prompts and five overall-vision files. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-02 | Select or resume only a task whose genuine direct prerequisites are satisfied. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-03 | Keep graph nodes to exactly three keys and validate true direct acyclic dependencies. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-04 | Define complete scope, exclusions, outputs, interfaces and verifiable acceptance criteria. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-05 | Choose relevant roles and their order, task-specific parameters and baseline destinations before activation. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-06 | Enforce one normal activation per role and bounded consultation-only responses. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-07 | Verify real outputs, evidence, tests, integration and final acceptance. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-08 | Capture the exact read-only source version, current main commit, source blob, graph blob and catalog blob before creating or resuming a task record. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-09 | Derive a deterministic topological order and conservative execution waves from the complete current graph. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-10 | Record each selected task's derived topological position and wave in task-status.md without adding scheduling fields to graph nodes. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-11 | Distinguish wave readiness from concurrency authorization; preserve White-P's one-active-task and sequential-role rules by default. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-12 | Version each approved requirement or shared-contract change and record exact changed requirement IDs, before/after versions, reason and evidence. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-13 | Trace each change to directly and transitively affected tasks, interfaces, consumers and acceptance evidence. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-14 | Reconcile every affected historical task individually while preserving its baseline status and previous evidence. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-15 | Require evidence-backed contract and acceptance revalidation before relying on affected historical completion; document any justified status transition. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SE-16 | Derive impact counts and status summaries from canonical change/reconciliation records instead of manually maintained duplicate totals. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

**Group 2 — task-specific parameters:** Define only checks needed for this task; do not duplicate Group 1.

| Parameter ID | Task-specific check/action | Expected result | Evidence required | Status |
|---|---|---|---|---|
| SE-T01 | <TASK_SPECIFIC_CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

### execution-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/execution-engineer/work-log.md
- Base-document destination: <ONE_OF_FIVE_EXISTING_FOLDERS>

Group 1: copy every EX-01 through EX-07 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Give each its own expected result, evidence and status.
Group 2: define unique EX-T01, EX-T02, … task-specific checks without duplicating Group 1.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| EX-01 | 1 | Conform to approved requirements and the exact task scope. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| EX-02 | 1 | Verify implementation logic and relevant state transitions. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| EX-03 | 1 | Create complete real outputs; plans, stubs, mocks and placeholders are not implementation. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| EX-04 | 1 | Respect approved APIs, contracts, data formats, persistence rules and interfaces. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| EX-05 | 1 | Keep changes within scope; avoid unrelated refactors and features. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| EX-06 | 1 | Follow existing project conventions and maintain readable, supportable code. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| EX-07 | 1 | Record exact changed paths and run appropriate initial checks; report only observed results. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### qa-testing-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/qa-testing-engineer/work-log.md
- Base-document destination: <ONE_OF_FIVE_EXISTING_FOLDERS>

Group 1: copy every QA-01 through QA-08 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique QA-T01, QA-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| QA-01 | 1 | Map every acceptance criterion to a check. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-02 | 1 | Verify valid and normal/positive workflows. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-03 | 1 | Test invalid, malformed, missing or unauthorized inputs where relevant. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-04 | 1 | Test boundary values and state transitions. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-05 | 1 | Verify relevant component integration and contracts. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-06 | 1 | Check for regressions in related existing behavior. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-07 | 1 | Record reproducible commands, environment assumptions and actual results. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| QA-08 | 1 | Record defects, severity, evidence, and retest results. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### safety-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/safety-engineer/work-log.md
- Base-document destination: base-documents/safety-engineer/

Group 1: copy every SAF-01 through SAF-07 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique SAF-T01, SAF-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| SAF-01 | 1 | Identify assets, actors, privileges, sensitive data and trust boundaries. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SAF-02 | 1 | Identify realistic threats, misuse, failures and harm scenarios. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SAF-03 | 1 | Assess likelihood and impact/severity separately and explain uncertainty. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SAF-04 | 1 | Identify preventive controls. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SAF-05 | 1 | Identify detection, containment, correction, rollback and recovery controls. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SAF-06 | 1 | Verify control effectiveness by inspection or tests; separate implemented from proposed controls. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| SAF-07 | 1 | Record residual risk, assumptions, owners and decisions requiring approval. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### project-structure-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/project-structure-engineer/work-log.md
- Base-document destination: base-documents/project-structure-engineer/

Group 1: copy every PS-01 through PS-07 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique PS-T01, PS-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| PS-01 | 1 | Verify every path exists at the intended location and serves a defined purpose. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PS-02 | 1 | Use lowercase-kebab-case for new paths unless a user-fixed name requires exact casing. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PS-03 | 1 | Detect duplicate, ambiguous, shadow or misleading paths. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PS-04 | 1 | Keep structure consistent with repository conventions and the Production/Development boundary. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PS-05 | 1 | Verify links, imports, config paths and documentation references. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PS-06 | 1 | Assess reference and migration risk before any authorized move or rename. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PS-07 | 1 | Preserve existing files and verify final repository integrity. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### design-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/design-engineer/work-log.md
- Base-document destination: base-documents/design-engineer/

Group 1: copy every DE-01 through DE-08 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique DE-T01, DE-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| DE-01 | 1 | Maintain coherent visual identity. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-02 | 1 | Ensure shared components and patterns are consistent. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-03 | 1 | Define consistent colors, tokens, contrast and semantic states. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-04 | 1 | Specify readable typography and hierarchy. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-05 | 1 | Check layout, spacing, alignment, density and content priority. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-06 | 1 | Specify relevant loading, empty, success, warning, error, disabled, selected and focus states. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-07 | 1 | Consider Windows desktop sizes, resizing and scaling. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| DE-08 | 1 | Provide measurable, implementation-ready specifications. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### ux-interaction-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/ux-interaction-engineer/work-log.md
- Base-document destination: base-documents/ux-interaction-engineer/

Group 1: copy every UX-01 through UX-08 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique UX-T01, UX-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| UX-01 | 1 | Map the user goal and complete interaction flow. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-02 | 1 | Ensure controls, terms, decisions and feedback are understandable. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-03 | 1 | Remove unnecessary steps and cognitive load without weakening safety. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-04 | 1 | Prevent avoidable user errors through clear constraints and feedback. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-05 | 1 | Address loading, empty, progress, success, error, cancellation and timeout states. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-06 | 1 | Provide suitable retry, resume, undo and recovery paths. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-07 | 1 | Consider keyboard use, focus, readability and accessibility. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| UX-08 | 1 | Preserve terminology, navigation and predictable state transitions. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### feasibility-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/feasibility-engineer/work-log.md
- Base-document destination: <ONE_OF_FIVE_EXISTING_FOLDERS>

Group 1: copy every FE-01 through FE-07 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique FE-T01, FE-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| FE-01 | 1 | Assess technical feasibility and platform/architecture constraints. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| FE-02 | 1 | Assess effort, duration and sequencing realistically. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| FE-03 | 1 | Identify economic, hardware, service, skill and maintenance resources. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| FE-04 | 1 | Identify third-party, approval, licensing, infrastructure and availability dependencies. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| FE-05 | 1 | List assumptions and evidence required to validate them. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| FE-06 | 1 | State estimate confidence, uncertainty and missing information. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| FE-07 | 1 | Compare realistic alternatives and fallbacks. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### idea-alignment-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/idea-alignment-engineer/work-log.md
- Base-document destination: <ONE_OF_FIVE_EXISTING_FOLDERS>

Group 1: copy every IA-01 through IA-06 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique IA-T01, IA-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| IA-01 | 1 | Check alignment with the approved product purpose. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| IA-02 | 1 | Preserve the intended value proposition. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| IA-03 | 1 | Check fit with target users and documented needs. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| IA-04 | 1 | Respect approved scope, exclusions and decisions. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| IA-05 | 1 | Detect feature creep, assumption-driven changes and goal substitution. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| IA-06 | 1 | Explain long-term impact and fidelity to user intent. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

### project-mapping-engineer

- State: <STATE>
- Normal activation_count: <0 or 1>
- Start / end / result: <DETAIL>
- Assigned scope and deliverables: <DETAIL>
- Work log: Tasks/<TASK_ID>/project-mapping-engineer/work-log.md
- Base-document destination: base-documents/project-mapping-engineer/

Group 1: copy every PM-01 through PM-07 check verbatim from the canonical fixed-parameter registry in agents/senior-engineer.md, using one row per ID. Group 2: define unique PM-T01, PM-T02, … task-specific checks.

| Parameter ID | Group (1 fixed / 2 task-specific) | Check/action | Expected result | Evidence | Status |
|---|---|---|---|---|---|
| PM-01 | 1 | Identify all relevant current and planned components. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PM-02 | 1 | Inspect and state actual current status from real files, code or behavior. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PM-03 | 1 | Trace inputs, outputs, owners and consumers. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PM-04 | 1 | Map component links, contracts, data flows and control flows. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PM-05 | 1 | Reference actual repository paths, source sections and evidence. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PM-06 | 1 | Detect gaps, duplicates, orphans, ambiguity and unknowns. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |
| PM-07 | 1 | Preserve requirement-to-task-to-component-to-evidence traceability and separate current from target state. | <EXPECTED_RESULT> | <EVIDENCE_REQUIRED> | pending |

## 7. Consultation register

Every consultation gets a unique sequential ID: CONS-<TASK_ID>-001, CONS-<TASK_ID>-002, and so on. Record incoming and outgoing consultations in this single register; both affected agents must append the consultation ID and their own action/result to their work logs.

| ID | Requester | Recipient | Date/order | Exact question | Reason and context | Evidence/paths | Requested answer | Actual response | Response evidence | Requester's decision/use | Result | State |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CONS-<TASK_ID>-001 | <ROLE_ID> | <ROLE_ID> | <TIME> | <QUESTION> | <WHY> | <PATHS> | <RESPONSE_NEEDED> | <ANSWER> | <EVIDENCE> | <HOW_USED> | <OUTCOME> | <requested/answered/accepted/rejected/unresolved> |

Rules:
- A consultant answers only the recorded question after completing its normal turn.
- Consultation is not a second normal activation and never reopens ordinary work.
- A consultant cannot consult or activate a third role; escalate that need to the Senior Engineer.
- The requester remains responsible for incorporating or rejecting the advice.
- Record disagreement, resolution and unresolved issues explicitly.

## 8. Integration and hand-off

| From role | To role | Contract / information handed over | Paths/evidence | Accepted by recipient | Follow-up |
|---|---|---|---|---|---|
| <ROLE_ID> | <ROLE_ID> | <DETAIL> | <PATHS> | <yes/no/pending> | <DETAIL> |

- Changed files and exact paths: <LIST>
- Actual outputs created/updated: <LIST>
- Tests/checks actually executed and observed results: <LIST>
- Consultations resolved: <LIST>
- Limitations and blockers: <LIST>
- Open decisions requiring owner approval: <LIST>

## 9. Final acceptance and graph decision

- All selected agents completed: <yes/no>
- Every required Group 1 fixed parameter reviewed: <yes/no>
- Every applicable Group 2 task-specific parameter reviewed: <yes/no>
- Required consultations resolved or explicitly accepted as open: <yes/no>
- Actual deliverables exist: <yes/no>
- Acceptance criteria passed with inspectable evidence: <yes/no>
- Independent QA required and completed: <yes/no/not_applicable with reason>
- Safety risks requiring owner approval: <LIST_OR_NONE>
- Remaining blockers/open decisions: <LIST_OR_NONE>
- Senior Engineer's final decision and rationale: <DETAIL>
- Final graph status: <done | in_progress | blocked | deferred_final>
- Graph update evidence: <COMMIT/PATH/RESULT>

Only the Senior Engineer changes dependency-graph.json. Mark a task done only after actual outputs and all applicable acceptance checks are evidenced; agent completion declarations alone are insufficient.

## 10. Append-only change record

| Date/time | Author role | Section changed | Change | Reason/evidence |
|---|---|---|---|---|
| <TIME> | <ROLE_ID> | <SECTION> | <APPEND-ONLY SUMMARY> | <REASON> |

Preserve earlier records. Correct a previous statement by appending a dated clarification; do not silently erase history.


---

## 11. Dependency-edge review register

Every direct incoming dependency must have exactly one review in the canonical record below. Use the target task's status document as the review owner.

| Prerequisite task ID | Classification | Validation status | Concrete reason | Evidence | Scheduling effect |
|---|---|---|---|---|---|
| <TASK_ID> | <hard_dependency / contract_or_interface_dependency / sequencing_only / unreviewed> | <unreviewed / validated / disputed> | <WHY THIS RELATION EXISTS> | <PATHS_OR_HTTPS_URLS> | <must be done / validated sequencing-only bypass / blocked pending review> |

A validated edge requires a rationale and evidence. A sequencing-only edge can be bypassed only after validation. Record every added, removed or reclassified edge in the append-only edge-change log in the canonical record.

## 12. Task-level execution attempt ledger

Append one row for every attempt, including failures, partial work, blocked work, corrections and reopenings. Do not rewrite or delete earlier attempts.

| Attempt ID | Start/end | Result/summary | Changed files | Commit SHA + reason | Related commits | Tests/checks: name, command, result, run ID/URL, environment, note | Failure | Blocker/reopen | Contract changes | Device/host (redacted) | Model revision/hash | Pre/post-upgrade snapshot | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <TASK_ID>-A001 | <START_ISO>/<END_ISO> | <RESULT_AND_SUMMARY> | <EXACT_PATHS> | <40-CHAR SHA OR NULL + REASON> | <SHA_LIST> | <EXACT_TEST_RECORDS_AND_OBSERVED_RESULTS> | <DETAIL_OR_NONE> | <DETAIL_OR_NONE> | <CONTRACT_IDS_OR_NONE> | <REDACTED_DETAILS_OR_NOT_APPLICABLE> | <MODEL_ID_AND_SHA256_OR_NOT_APPLICABLE> | <PRE/POST_STATE_OR_NOT_APPLICABLE> | <NEXT_ACTION_OR_NONE> |

The execution summary must exactly match the history: attempt_count, failed_attempt_count, tests_passed and tests_failed. A task may be done only with a succeeded attempt and at least one passing, recorded verification.

## 13. Contract revalidation and external deferral

**Contract revalidation**
- State: <not_required | required | in_review | passed | failed>
- Triggering contract/interface changes: <LIST_OR_NONE>
- Affected direct/transitive task IDs: <LIST_OR_NONE>
- Review/test evidence: <PATHS_OR_URLS>
- Reason and remaining work: <DETAIL_OR_NONE>

**Blocked status**
- Concrete blocker: <DETAIL_OR_NONE>
- Missing prerequisite/input: <DETAIL_OR_NONE>
- Owner or next action: <DETAIL_OR_NONE>
- Unblocking condition: <DETAIL_OR_NONE>

**Final-stage deferral — fill only when graph status is deferred_final**
- Reason: <WHY_EXTERNAL_ACCEPTANCE_CAN_WAIT>
- Start condition: <ALL_REQUIRED_PRECONDITIONS>
- Final stage: <WHEN_IT_MUST_RUN_AND_WHAT_IT_BLOCKS>

## 14. Canonical machine-readable task-status record

Keep exactly one JSON block between the markers below. It belongs inside this task-status.md; do not create a separate metadata file. The block is the machine-readable source for the graph guard. Keep it synchronized with the human-readable sections above.

All paths are repository-relative POSIX paths. Use only verified actual files in actual_output_paths; expected paths stay in the acceptance section and never count as actual outputs. Use HTTPS for external evidence. Use null when a commit SHA was not recorded and explain that in the attempt summary.

The ten role entries below are mandatory. Update each entry's state, activation count, destination and parameter IDs from the completed Markdown registers. For selected/completed roles, list every fixed parameter ID from the canonical registry in agents/senior-engineer.md and all task-specific parameter IDs. For not_applicable roles, provide a concrete reason.

<!-- WHITEP_TASK_STATUS_RECORD_START -->
```json
{
  "schema_version": "1.2",
  "task_id": "<TASK_ID>",
  "graph_status": "<not_started|in_progress|done|blocked|deferred_final>",
  "source_baseline": {
    "source_path": "Production/task-decomposition/main-document.md",
    "source_version": "<EXPLICIT_VERSION_OR_not_versioned>",
    "main_commit_sha": "<40-CHAR-CURRENT-MAIN-SHA>",
    "source_blob_sha": "<40-CHAR-SOURCE-BLOB-SHA>",
    "graph_blob_sha": "<40-CHAR-GRAPH-BLOB-SHA>",
    "catalog_blob_sha": "<40-CHAR-CATALOG-BLOB-SHA>",
    "captured_at": "<UTC-ISO-8601-TIMESTAMP>"
  },
  "execution_plan": {
    "topological_order": 1,
    "wave_id": "WAVE-001",
    "wave_index": 1,
    "scheduling_mode": "sequential_default",
    "parallelism_authorized": false,
    "parallelism_reason": "White-P retains one active task by default.",
    "parallelism_evidence": []
  },
  "prerequisite_reviews": [],
  "acceptance_criteria": [],
  "actual_output_paths": [],
  "evidence": [],
  "execution_history": [],
  "execution_summary": {
    "attempt_count": 0,
    "failed_attempt_count": 0,
    "last_attempt_id": null,
    "last_attempt_result": null,
    "changed_files": [],
    "related_commits": [],
    "tests_passed": [],
    "tests_failed": [],
    "blocked_reason": null,
    "reopened_reason": null
  },
  "agent_reviews": [
    {
      "role_id": "senior-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/senior-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/project-mapping-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "execution-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/execution-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/project-structure-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "qa-testing-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/qa-testing-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/safety-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "safety-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/safety-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/safety-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "project-structure-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/project-structure-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/project-structure-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "design-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/design-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/design-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/ux-interaction-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/ux-interaction-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "feasibility-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/feasibility-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/project-structure-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/idea-alignment-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/project-mapping-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    },
    {
      "role_id": "project-mapping-engineer",
      "state": "not_scheduled",
      "normal_activation_count": 0,
      "execution_mode": "not_run",
      "work_log_path": "Production/Development/Tasks/<TASK_ID>/project-mapping-engineer/work-log.md",
      "base_document_destination": "Production/Development/base-documents/project-mapping-engineer",
      "fixed_parameter_ids": [],
      "task_specific_parameter_ids": [],
      "not_applicable_reason": null
    }
  ],
  "consultations": [],
  "requirement_change_register": [],
  "affected_task_reconciliation": [],
  "edge_change_log": [],
  "contract_revalidation": {
    "state": "not_required",
    "triggering_contracts": [],
    "affected_task_ids": [],
    "reason": null,
    "evidence": []
  },
  "blocked_reason": null,
  "deferral": null,
  "task_definition": {
    "section": "<SOURCE_SECTION_OR_WORKSTREAM>",
    "source_task_id": null,
    "source_change_operation": null,
    "affected_task_ids": [],
    "description": "<COMPLETE_TASK_DESCRIPTION>",
    "implementation_focus": "<EXACT_IMPLEMENTATION_OR_REVIEW_FOCUS>",
    "inputs": [
      {
        "input_id": "IN-001",
        "description": "<INPUT_PURPOSE>",
        "source_refs": [
          "<SOURCE_PATH_OR_REQUIREMENT_ID>"
        ],
        "provider_task_ids": [],
        "required_artifact": "<EXACT_REQUIRED_INPUT_OR_CONTRACT>",
        "availability": "pending",
        "evidence": [],
        "notes": "<ASSUMPTIONS_OR_NONE>"
      }
    ],
    "outputs": [
      {
        "output_id": "OUT-001",
        "description": "<DELIVERABLE_AND_CONSUMER_PURPOSE>",
        "output_type": "<code|test|document|configuration|design|decision|other>",
        "expected_path": "<EXPECTED_REPOSITORY_RELATIVE_PATH>",
        "acceptance_criteria_ids": [
          "ACC-001"
        ],
        "status": "pending",
        "actual_paths": [],
        "evidence": [],
        "not_applicable_reason": null
      }
    ],
    "start_condition": "<ALL_EXPLICIT_START_CONDITIONS>",
    "acceptance_summary": "<COMPLETE_ACCEPTANCE_SUMMARY>",
    "status_label_fa": "<PERSIAN_STATUS_LABEL>",
    "notes": []
  },
  "expected_output_paths": [
    "<EXPECTED_REPOSITORY_RELATIVE_PATH>"
  ],
  "parameter_reviews": [
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-01",
      "group": "fixed",
      "check": "Read graph, catalog, relevant complete source, existing task records, all role prompts and five overall-vision files.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-02",
      "group": "fixed",
      "check": "Select or resume only a task whose genuine direct prerequisites are satisfied.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-03",
      "group": "fixed",
      "check": "Keep graph nodes to exactly three keys and validate true direct acyclic dependencies.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-04",
      "group": "fixed",
      "check": "Define complete scope, exclusions, outputs, interfaces and verifiable acceptance criteria.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-05",
      "group": "fixed",
      "check": "Choose relevant roles and their order, task-specific parameters and baseline destinations before activation.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-06",
      "group": "fixed",
      "check": "Enforce one normal activation per role and bounded consultation-only responses.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-07",
      "group": "fixed",
      "check": "Verify real outputs, evidence, tests, integration and final acceptance.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-08",
      "group": "fixed",
      "check": "Capture the exact read-only source version, current main commit, source blob, graph blob and catalog blob before creating or resuming a task record.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-09",
      "group": "fixed",
      "check": "Derive a deterministic topological order and conservative execution waves from the complete current graph.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-10",
      "group": "fixed",
      "check": "Record each selected task's derived topological position and wave in task-status.md without adding scheduling fields to graph nodes.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-11",
      "group": "fixed",
      "check": "Distinguish wave readiness from concurrency authorization; preserve White-P's one-active-task and sequential-role rules by default.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-12",
      "group": "fixed",
      "check": "Version each approved requirement or shared-contract change and record exact changed requirement IDs, before/after versions, reason and evidence.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-13",
      "group": "fixed",
      "check": "Trace each change to directly and transitively affected tasks, interfaces, consumers and acceptance evidence.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-14",
      "group": "fixed",
      "check": "Reconcile every affected historical task individually while preserving its baseline status and previous evidence.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-15",
      "group": "fixed",
      "check": "Require evidence-backed contract and acceptance revalidation before relying on affected historical completion; document any justified status transition.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "senior-engineer",
      "parameter_id": "SE-16",
      "group": "fixed",
      "check": "Derive impact counts and status summaries from canonical change/reconciliation records instead of manually maintained duplicate totals.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-01",
      "group": "fixed",
      "check": "Conform to approved requirements and the exact task scope.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-02",
      "group": "fixed",
      "check": "Verify implementation logic and relevant state transitions.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-03",
      "group": "fixed",
      "check": "Create complete real outputs; plans, stubs, mocks and placeholders are not implementation.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-04",
      "group": "fixed",
      "check": "Respect approved APIs, contracts, data formats, persistence rules and interfaces.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-05",
      "group": "fixed",
      "check": "Keep changes within scope; avoid unrelated refactors and features.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-06",
      "group": "fixed",
      "check": "Follow existing project conventions and maintain readable, supportable code.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "execution-engineer",
      "parameter_id": "EX-07",
      "group": "fixed",
      "check": "Record exact changed paths and run appropriate initial checks; report only observed results.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-01",
      "group": "fixed",
      "check": "Map every acceptance criterion to a check.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-02",
      "group": "fixed",
      "check": "Verify valid and normal/positive workflows.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-03",
      "group": "fixed",
      "check": "Test invalid, malformed, missing or unauthorized inputs where relevant.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-04",
      "group": "fixed",
      "check": "Test boundary values and state transitions.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-05",
      "group": "fixed",
      "check": "Verify relevant component integration and contracts.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-06",
      "group": "fixed",
      "check": "Check for regressions in related existing behavior.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-07",
      "group": "fixed",
      "check": "Record reproducible commands, environment assumptions and actual results.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "qa-testing-engineer",
      "parameter_id": "QA-08",
      "group": "fixed",
      "check": "Record defects, severity, evidence, and retest results.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-01",
      "group": "fixed",
      "check": "Identify assets, actors, privileges, sensitive data and trust boundaries.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-02",
      "group": "fixed",
      "check": "Identify realistic threats, misuse, failures and harm scenarios.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-03",
      "group": "fixed",
      "check": "Assess likelihood and impact/severity separately and explain uncertainty.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-04",
      "group": "fixed",
      "check": "Identify preventive controls.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-05",
      "group": "fixed",
      "check": "Identify detection, containment, correction, rollback and recovery controls.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-06",
      "group": "fixed",
      "check": "Verify control effectiveness by inspection or tests; separate implemented from proposed controls.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "safety-engineer",
      "parameter_id": "SAF-07",
      "group": "fixed",
      "check": "Record residual risk, assumptions, owners and decisions requiring approval.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-01",
      "group": "fixed",
      "check": "Verify every path exists at the intended location and serves a defined purpose.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-02",
      "group": "fixed",
      "check": "Use lowercase-kebab-case for new paths unless a user-fixed name requires exact casing.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-03",
      "group": "fixed",
      "check": "Detect duplicate, ambiguous, shadow or misleading paths.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-04",
      "group": "fixed",
      "check": "Keep structure consistent with repository conventions and the Production/Development boundary.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-05",
      "group": "fixed",
      "check": "Verify links, imports, config paths and documentation references.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-06",
      "group": "fixed",
      "check": "Assess reference and migration risk before any authorized move or rename.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-structure-engineer",
      "parameter_id": "PS-07",
      "group": "fixed",
      "check": "Preserve existing files and verify final repository integrity.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-01",
      "group": "fixed",
      "check": "Maintain coherent visual identity.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-02",
      "group": "fixed",
      "check": "Ensure shared components and patterns are consistent.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-03",
      "group": "fixed",
      "check": "Define consistent colors, tokens, contrast and semantic states.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-04",
      "group": "fixed",
      "check": "Specify readable typography and hierarchy.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-05",
      "group": "fixed",
      "check": "Check layout, spacing, alignment, density and content priority.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-06",
      "group": "fixed",
      "check": "Specify relevant loading, empty, success, warning, error, disabled, selected and focus states.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-07",
      "group": "fixed",
      "check": "Consider Windows desktop sizes, resizing and scaling.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "design-engineer",
      "parameter_id": "DE-08",
      "group": "fixed",
      "check": "Provide measurable, implementation-ready specifications.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-01",
      "group": "fixed",
      "check": "Map the user goal and complete interaction flow.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-02",
      "group": "fixed",
      "check": "Ensure controls, terms, decisions and feedback are understandable.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-03",
      "group": "fixed",
      "check": "Remove unnecessary steps and cognitive load without weakening safety.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-04",
      "group": "fixed",
      "check": "Prevent avoidable user errors through clear constraints and feedback.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-05",
      "group": "fixed",
      "check": "Address loading, empty, progress, success, error, cancellation and timeout states.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-06",
      "group": "fixed",
      "check": "Provide suitable retry, resume, undo and recovery paths.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-07",
      "group": "fixed",
      "check": "Consider keyboard use, focus, readability and accessibility.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "ux-interaction-engineer",
      "parameter_id": "UX-08",
      "group": "fixed",
      "check": "Preserve terminology, navigation and predictable state transitions.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-01",
      "group": "fixed",
      "check": "Assess technical feasibility and platform/architecture constraints.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-02",
      "group": "fixed",
      "check": "Assess effort, duration and sequencing realistically.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-03",
      "group": "fixed",
      "check": "Identify economic, hardware, service, skill and maintenance resources.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-04",
      "group": "fixed",
      "check": "Identify third-party, approval, licensing, infrastructure and availability dependencies.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-05",
      "group": "fixed",
      "check": "List assumptions and evidence required to validate them.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-06",
      "group": "fixed",
      "check": "State estimate confidence, uncertainty and missing information.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "feasibility-engineer",
      "parameter_id": "FE-07",
      "group": "fixed",
      "check": "Compare realistic alternatives and fallbacks.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "parameter_id": "IA-01",
      "group": "fixed",
      "check": "Check alignment with the approved product purpose.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "parameter_id": "IA-02",
      "group": "fixed",
      "check": "Preserve the intended value proposition.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "parameter_id": "IA-03",
      "group": "fixed",
      "check": "Check fit with target users and documented needs.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "parameter_id": "IA-04",
      "group": "fixed",
      "check": "Respect approved scope, exclusions and decisions.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "parameter_id": "IA-05",
      "group": "fixed",
      "check": "Detect feature creep, assumption-driven changes and goal substitution.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "idea-alignment-engineer",
      "parameter_id": "IA-06",
      "group": "fixed",
      "check": "Explain long-term impact and fidelity to user intent.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-01",
      "group": "fixed",
      "check": "Identify all relevant current and planned components.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-02",
      "group": "fixed",
      "check": "Inspect and state actual current status from real files, code or behavior.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-03",
      "group": "fixed",
      "check": "Trace inputs, outputs, owners and consumers.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-04",
      "group": "fixed",
      "check": "Map component links, contracts, data flows and control flows.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-05",
      "group": "fixed",
      "check": "Reference actual repository paths, source sections and evidence.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-06",
      "group": "fixed",
      "check": "Detect gaps, duplicates, orphans, ambiguity and unknowns.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    },
    {
      "role_id": "project-mapping-engineer",
      "parameter_id": "PM-07",
      "group": "fixed",
      "check": "Preserve requirement-to-task-to-component-to-evidence traceability and separate current from target state.",
      "expected_result": "<EXPECTED_RESULT>",
      "evidence_required": "<EVIDENCE_REQUIRED>",
      "status": "pending",
      "evidence": [],
      "rationale": null
    }
  ]
}
```
<!-- WHITEP_TASK_STATUS_RECORD_END -->

## 15. Completion and preservation rules

- The canonical record and Markdown tables must agree; the graph guard rejects mismatched graph/task status, missing incoming-edge reviews, missing role records, invalid activation counts, incomplete acceptance, missing outputs/evidence, inconsistent attempt summaries and invalid deferral metadata.
- Completed tasks need actual existing output files, passing acceptance criteria, reviewable evidence, a succeeded attempt, and at least one recorded passing verification.
- A completed role must have exactly one normal activation and an existing work log; a not_applicable role must have zero activations and an explicit reason. Do not describe sequential same-assistant passes as independent agents.
- For code outputs, evidence must include test source under tests/ or test/. Known TODO, NotImplemented, mock, placeholder and simulated-response markers are rejected from code files claimed as actual outputs.
- Keep task-status history append-only. Correct earlier information by adding a dated clarification or a new attempt; never silently erase it.


## 16. Immutable planning baseline

At task creation, capture the live `main` commit SHA, source document version/revision, source blob SHA, graph blob SHA, catalog blob SHA and UTC timestamp. Never use a remembered revision. Do not change the initial baseline when a later requirement or contract changes; append a new change record instead. Use `not_versioned` only when the source has no declared version.

## 17. Derived topological order and execution wave

The Senior Engineer derives the stable topological position and wave ID from the complete graph. The graph guard derives the same result independently and rejects mismatches. Use graph array order as the tie-breaker. All graph edges are included conservatively in the baseline wave calculation.

| Topological position | Wave ID | Wave number | Scheduling mode | Parallel execution authorized? | Collision/resource assessment and evidence |
|---:|---|---:|---|---|---|
| <DERIVED_POSITION> | <DERIVED_WAVE_ID> | <DERIVED_WAVE_NUMBER> | <sequential_default/controlled_parallel> | <false/true> | <REASON_AND_EVIDENCE> |

A wave indicates readiness, not concurrency permission. One active task and sequential specialist roles remain the default. Parallel task execution requires explicit project-owner approval and documented file, interface, resource and QA collision controls. Never add wave metadata to dependency-graph.json.

## 18. Versioned requirement changes and affected-task reconciliation

Append every approved source/contract change to `requirement_change_register`. Each entry has a unique change ID, before/after source versions, exact changed requirement/section IDs, summary, reason, evidence, affected task IDs, author, timestamp and state.

For every affected task, append exactly one `affected_task_reconciliation` entry for that change. Preserve its baseline status and prior acceptance evidence; record impact classification, decision, impact-review state, implementation-revalidation state and any justified status transition. Impact mapping marked reviewed does not mean implementation revalidation passed.

A task status must never change merely because the task was listed as affected. A transition requires explicit from/to status, reason, evidence, Senior Engineer reviewer and timestamp. Do not create future task workspaces only to hold impact markers. Record whether an affected task-status.md exists and carry the reference into that task when it is selected.

All impact totals and status counts are derived from the arrays in this task-status record. Do not manually maintain a second summary counter or duplicate global change map.

The machine-readable field contracts are:

- `requirement_change_register[]`: `change_id`, `recorded_at`, `source_version_before`, `source_version_after`, `changed_requirement_ids[]`, `change_summary`, `reason`, `evidence[]`, `affected_task_ids[]`, `recorded_by`, `status`.
- `affected_task_reconciliation[]`: `change_id`, `task_id`, `baseline_status`, `current_status`, `impact_classification`, `decision`, `review_status`, `revalidation_status`, `status_changed`, `status_transition`, `task_status_path_exists`, `update_task_ids[]`, `evidence[]`, `reviewed_by`, `reviewed_at`.

Schema 1.0 records remain immutable historical snapshots. New task-status documents use schema 1.2; never backfill historical facts that were not captured at the time.


## 19. Complete task contract — project-equivalent fields outside the graph

Every newly selected task must have a complete `task_definition` in the canonical JSON record. Detailed task fields belong in this task's `task-status.md`, populated by the Senior Engineer from the authoritative task catalog/source; they must never be copied into dependency-graph.json.

| Project task-node field | White-P task-status location |
|---|---|
| `id` / `title` / `section` | `task_id`, Task identity and `task_definition.section` |
| `source_task_id` / `source_change_operation` / `affected_task_ids` | Matching fields in `task_definition` |
| `description` / `implementation_focus` / `start_condition` | Matching fields in `task_definition` |
| `inputs` / `outputs` | Structured `task_definition.inputs[]` and `task_definition.outputs[]` |
| `acceptance` / `acceptance_criteria` | `task_definition.acceptance_summary` and detailed `acceptance_criteria[]` |
| `status` / `status_fa` | `graph_status` plus `task_definition.status_label_fa` |
| `expected_output_paths` / `actual_output_paths` | Separate arrays; expected paths never prove that files exist |
| `evidence` / `notes` | Canonical `evidence[]` and `task_definition.notes[]` |
| `execution_summary` / `execution_history` | Derived summary plus append-only attempt ledger |

Inputs identify their source/reference, provider task (when applicable), exact required artifact, availability state and evidence. Outputs identify type, expected path, linked acceptance IDs, creation/verification state, actual paths and evidence. Every actual path must exist at the captured commit; an expected path is never evidence.

## 20. Machine-readable parameter audit

The canonical `parameter_reviews[]` array contains one record for every fixed parameter in all ten roles (81 records), using the exact check text from agents/senior-engineer.md. It also contains each task-specific parameter defined for a selected role. Every record has role, parameter ID, group, exact check/action, expected result, evidence required, review status, evidence and rationale.

The Markdown role tables and `parameter_reviews[]` are two representations of the same register and must agree. Every fixed ID appears exactly once. A passed parameter requires evidence; not_applicable requires a task-specific reason; pending or needs_consultation must never be presented as passed. A not-applicable role has zero activations and all its fixed checks visibly marked not_applicable. The graph guard validates this register against the canonical Senior Engineer prompt and the human-readable table.

## 21. Reproducible attempt and verification record

Every attempt, including implementation, local verification, CI, device testing, failure, partial work, skip, pending workflow, blocked work, correction or reopening, is append-only. Each schema 1.2 attempt records:
- unique attempt ID, start/end timestamps, result, summary, exact changed files;
- commit SHA or explicit null plus reason, related commit SHAs;
- each test/check name, exact command, result (`passed`, `failed`, `not_run`, `skipped`, `pending`), environment, run ID, HTTPS URL, summary/note and failure/skip details;
- failure, blocker, reopening, contract changes and next action;
- redacted device/host information, model revision/hash and pre/post-upgrade snapshot where relevant.

The execution summary is derived from attempt history: attempt counts, last attempt ID/result, changed files, related commits, passed/failed test commands, blocker and reopening reason. Do not manually change counters. A task cannot be done while its latest attempt is not succeeded, an applicable required check remains pending/skipped without an accepted scope reason, an output is missing, evidence is absent or material contract revalidation is unresolved.
