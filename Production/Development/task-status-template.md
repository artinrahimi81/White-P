# Task Status — <TASK_ID>

> Create this file only after the Senior Engineer selects the task. Replace every placeholder, retain all required sections, and keep this document as the task's live control record. The graph remains authoritative for task ID, direct prerequisites and graph status.

## 1. Task identity and control

- Task ID: <TASK_ID>
- Task title: <TITLE_FROM_TASK_CATALOG>
- Objective: <ONE_CLEAR_OUTCOME>
- Graph status: <not_started | in_progress | done | blocked>
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

**Group 1 — fixed Senior Engineer parameters:** Copy SE-01 through SE-07 with their exact checks from agents/senior-engineer.md. Give each an expected result, required evidence and one review status.

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

Group 1: copy EX-01 through EX-07 from the fixed prompt with expected result, evidence and status.
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

Group 1: copy QA-01 through QA-08 from the fixed prompt. Group 2: define unique QA-T01, QA-T02, … task-specific checks.

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

Group 1: copy SAF-01 through SAF-07 from the fixed prompt. Group 2: define unique SAF-T01, SAF-T02, … task-specific checks.

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

Group 1: copy PS-01 through PS-07 from the fixed prompt. Group 2: define unique PS-T01, PS-T02, … task-specific checks.

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

Group 1: copy DE-01 through DE-08 from the fixed prompt. Group 2: define unique DE-T01, DE-T02, … task-specific checks.

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

Group 1: copy UX-01 through UX-08 from the fixed prompt. Group 2: define unique UX-T01, UX-T02, … task-specific checks.

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

Group 1: copy FE-01 through FE-07 from the fixed prompt. Group 2: define unique FE-T01, FE-T02, … task-specific checks.

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

Group 1: copy IA-01 through IA-06 from the fixed prompt. Group 2: define unique IA-T01, IA-T02, … task-specific checks.

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

Group 1: copy PM-01 through PM-07 from the fixed prompt. Group 2: define unique PM-T01, PM-T02, … task-specific checks.

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
- Final graph status: <done | in_progress | blocked>
- Graph update evidence: <COMMIT/PATH/RESULT>

Only the Senior Engineer changes dependency-graph.json. Mark a task done only after actual outputs and all applicable acceptance checks are evidenced; agent completion declarations alone are insufficient.

## 10. Append-only change record

| Date/time | Author role | Section changed | Change | Reason/evidence |
|---|---|---|---|---|
| <TIME> | <ROLE_ID> | <SECTION> | <APPEND-ONLY SUMMARY> | <REASON> |

Preserve earlier records. Correct a previous statement by appending a dated clarification; do not silently erase history.
