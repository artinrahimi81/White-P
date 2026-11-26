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
| SE-01 … SE-07 | <COPY_EXACT_CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <EX-01 or EX-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <QA-01 or QA-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <SAF-01 or SAF-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <PS-01 or PS-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <DE-01 or DE-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <UX-01 or UX-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <FE-01 or FE-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <IA-01 or IA-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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
| <PM-01 or PM-T01> | <1 or 2> | <CHECK> | <EXPECTED> | <EVIDENCE> | <STATUS> |

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

| Attempt ID | Start | End | Result | Summary | Changed files | Commit SHA or null + explanation | Commands/checks and observed result | Failure details | Blocker/reopen reason | Contract changes | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|---|
| <TASK_ID>-A001 | <ISO-8601> | <ISO-8601> | <succeeded/failed/partial/blocked/reopened> | <WHAT HAPPENED> | <EXACT PATHS> | <40-CHAR SHA OR NULL WITH REASON> | <EXACT COMMAND/CHECK, PASS/FAIL/NOT RUN> | <DETAIL OR NONE> | <DETAIL OR NONE> | <AFFECTED CONTRACTS OR NONE> | <NEXT ACTION OR NONE> |

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
  "schema_version": "1.1",
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
    "tests_passed": [],
    "tests_failed": []
  },
  "agent_reviews": [
    {"role_id":"senior-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/senior-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/project-mapping-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"execution-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/execution-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/project-structure-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"qa-testing-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/qa-testing-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/safety-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"safety-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/safety-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/safety-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"project-structure-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/project-structure-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/project-structure-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"design-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/design-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/design-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"ux-interaction-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/ux-interaction-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/ux-interaction-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"feasibility-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/feasibility-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/project-structure-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"idea-alignment-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/idea-alignment-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/project-mapping-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null},
    {"role_id":"project-mapping-engineer","state":"not_scheduled","normal_activation_count":0,"execution_mode":"not_run","work_log_path":"Production/Development/Tasks/<TASK_ID>/project-mapping-engineer/work-log.md","base_document_destination":"Production/Development/base-documents/project-mapping-engineer","fixed_parameter_ids":[],"task_specific_parameter_ids":[],"not_applicable_reason":null}
  ],
  "consultations": [],
  "requirement_change_register": [],
  "affected_task_reconciliation": [],
  "edge_change_log": [],
  "contract_revalidation": {"state":"not_required","affected_task_ids":[],"reason":null,"evidence":[]},
  "blocked_reason": null,
  "deferral": null
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

Schema 1.0 records remain immutable historical snapshots. New task-status documents use schema 1.1; never backfill historical facts that were not captured at the time.
