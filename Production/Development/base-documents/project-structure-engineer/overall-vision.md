# Overall Vision — Project Structure Engineer

## Purpose
Keep repository paths, naming, directories, references, and file ownership coherent as the product grows. Create only paths required by approved work.

## Durable product context
- All development-process artifacts belong under Production/Development/.
- The authoritative product specification currently exists at Production/task-decomposition/main-document.md. It is a read-only input; do not move, rename, duplicate, or edit it without explicit authorization.
- The fixed process structure uses agents/, Tasks/, base-documents/, dependency-graph.json, task-catalog.md, task-status.md, and one work-log.md per agent per task.
- The ten fixed role IDs and path conventions are declared in agents/senior-engineer.md.
- Application source, configuration, tests, and build assets belong in coherent product-source locations inside Production/Development, not in per-task history folders.

## Principles to preserve
1. Inspect the actual repository tree before creating, moving, renaming, or deleting paths.
2. Use lowercase-kebab-case for new names unless a user-specified fixed name requires exact casing.
3. Prevent duplicate paths, duplicate sources, ambiguous ownership, and orphan references.
4. Keep task history separate from real application source.
5. Preserve existing files and references; assess migration/rename risk before any authorized move.
6. Do not add convenience files, templates, or folders without a concrete requirement.
7. Verify affected links, imports, configuration references, and documentation paths.

## Append-only durable task notes
Append only concise, verified, task-ID-labelled structural constraints and lessons. Never alter earlier entries.

## WP-INIT-001 — Feasibility Engineer durable note

The dependency graph contains only genuine output/contract prerequisites. The proposed development stages in source Section 30 are advisory and do not automatically become dependency edges. No unsupported development duration, cost, throughput or capacity estimate was introduced; external dependencies and evidence gaps remain visible in task definitions.

## WP-INIT-001 — Project Structure Engineer durable note

The selected task workspace is Production/Development/Tasks/WP-INIT-001/. All ten fixed role work-log filenames and task-status.md follow the Senior Engineer prompt. Baseline changes remain under Production/Development/base-documents/. The source specification and collaboration rules are preserved and were not moved, copied, renamed or edited.
