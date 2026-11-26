# Task Catalog

This catalog stores task definitions, boundaries, source traceability, deliverables and acceptance criteria. It does not duplicate graph status or dependency lists. The dependency-graph.json file is the sole source of task IDs, direct prerequisites and execution status.

## WP-INIT-001 — Decompose the approved product specification into executable tasks

- **Source:** Production/task-decomposition/main-document.md, all 32 numbered sections and applicable introductory/final material.
- **Purpose:** Convert the complete approved product specification into a complete, traceable, non-duplicated set of bounded development tasks and a minimal dependency graph.
- **Scope:** Read and map the complete source; identify requirements, components, workflows, interfaces, security/privacy responsibilities, delivery and operations needs, proposals and unresolved decisions; define stable task IDs; specify objective, scope, exclusions, real outputs and individually verifiable acceptance criteria; identify only genuine direct prerequisites; validate catalog/graph consistency and graph integrity.
- **Exclusions:** Product-feature implementation; mock, stub or placeholder behavior; editing, moving, copying or renaming the source specification; resolving open decisions without approval; silently changing the meaning of informal user requirements; and selecting technologies not fixed by an approved source.
- **Required outputs:** A complete task catalog; dependency-graph.json in which every task object contains exactly id, depends_on and status; traceability from source requirements to task IDs; explicit recording of proposals, assumptions and unresolved decisions; and recorded evidence of dependency and graph validation.
- **Acceptance criteria:**
  1. All 32 numbered source sections are mapped.
  2. Every concrete requirement, workflow, component, interface, security/privacy concern and operational need is represented by one or more bounded tasks or explicitly recorded as unresolved/not yet approved.
  3. Every task has a clear objective, scope, exclusions, source references, deliverables and testable acceptance criteria.
  4. Duplicate, overlapping, orphaned, ambiguous and unnecessarily fragmented tasks are identified and resolved or documented.
  5. The graph contains only genuine direct prerequisites; mere preferred sequencing is excluded.
  6. Task IDs in the catalog and graph match exactly.
  7. Every graph task object has exactly three keys: id, depends_on and status.
  8. IDs are unique; prerequisite references are valid; self-dependencies, duplicate dependencies and cycles are absent.
  9. Graph statuses use only not_started, in_progress, done or blocked, and are not inferred from the existence of plans, folders or placeholder files.
  10. Proposals, assumptions, estimates and open decisions remain distinguishable from approved requirements.
  11. Specialist reviews, required consultations, evidence and Senior Engineer acceptance are recorded in the selected task workspace.
- **Initial state:** not_started. This task creates the task decomposition and execution plan; it does not authorize implementation of application features.

## Catalog rules

- Add or split tasks only when grounded in the source specification or a verified project need.
- Keep descriptions, scope, exclusions, outputs, acceptance criteria, source references and open decisions here or in the corresponding task-status.md; never put them in graph task objects.
- Do not duplicate dependency lists or status values in this catalog.
- Only the Senior Engineer may change this catalog or dependency-graph.json.
- Preserve source-to-task traceability when tasks are split, merged, changed or removed.
- Create a task workspace only after the Senior Engineer selects that task for execution.
- Preserve the user's intended meaning when translating informal wording into precise, testable requirements. Record uncertainty instead of silently resolving it.
