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


## WP-INIT-002 — Feasibility Engineer durable note

The expanded graph distinguishes domain specification gates from smaller child work packages. Edges represent only required outputs/contracts, not a preferred sequence. No unsupported schedule, budget, throughput or capacity estimate was created. Unresolved external dependencies and approval gates remain visible in the catalog.

## WP-INIT-002 — Project Structure Engineer durable note

The follow-up workspace is Production/Development/Tasks/WP-INIT-002/. The ten required role work-log files and task-status.md use the fixed names. Original WP-INIT-001 paths and identifiers remain preserved. All new/updated artifacts are contained within Production/Development; future child task workspaces are not pre-created.


## WP-INIT-003 — Feasibility and structure durable notes
- New identifiers continue the WP-DOMAIN-NNN scheme without renumbering prior tasks.
- Four domain-coherent breakdown files are stored in Production/Development/execution-work-breakdown/.
- Child task workspaces are not created ahead of Senior Engineer selection; parent roll-up dependencies are explicit and DAG-validated.
- Unsupported estimates and external approvals remain evidence-gated.

## Owner-Directed Responsive UI Structure Rules — 2026-11-27
These rules translate the application-wide UI direction into repository and implementation constraints. The product specification remains read-only at `Production/task-decomposition/main-document.md`. All future UI source, shared components, styling, tests and supporting implementation records must remain within the approved `Production/Development/` boundary.

### Single source of truth for shared UI foundations

- Implement one shared application shell used by all routes. Do not create separate page-specific sidebars, top bars or competing navigation systems.
- Keep the five canonical color tokens and responsive breakpoint definitions in one central design-token/theme source when product UI code is introduced. The Design Engineer's overall-vision baseline is the governing specification; do not redefine or drift from it in individual pages.
- Shared typography, spacing, component dimensions, focus styling, elevations, borders and state patterns must be centrally reusable. Page modules consume these tokens rather than hardcoding local alternatives.
- Create reusable components for repeated page headers, cards, forms, buttons, tables, dialogs, status indicators, navigation, notifications and empty/loading/error states. Extend an existing component before creating a duplicate.
- Keep route/page-specific content separate from global shell components. AI Workspace, Explore, Orders & Deliveries, Blockchain & Wallet, Dashboard and Settings must compose the same shared foundations.
- Do not choose or invent a product-source directory before inspecting the actual implementation tree. When implementation begins, place shared UI foundations in one clearly owned, conventional location inside Production/Development and record the actual paths.

### Responsive implementation constraints

Use the exact viewport ranges and visual behavior specified in the Design Engineer baseline (`>=1440`, `1200–1439`, `1024–1199`, `768–1023`, and `<768` logical pixels). Store breakpoint constants centrally; components must consume those constants rather than declaring local media-query thresholds.

- Adapt to available logical viewport size and Windows display scaling, not physical screen size, device labels or user-agent assumptions.
- Use Grid/Flex and fluid sizing for the main shell, page regions, cards and forms. Avoid fixed page widths, fixed content heights, absolute positioning for primary layout, and arbitrary per-page pixel offsets.
- Allow children to shrink within grid/flex containers; prevent long IDs, addresses, hashes and filenames from expanding the entire application.
- Keep vertical scrolling at page/content level. If a dense table needs horizontal scrolling, constrain it to the table container; do not make the whole application horizontally scroll.
- Prefer a responsive card/list representation for dense tables when the table structure no longer fits. Preserve all fields and their order/meaning during transformation.
- Dialogs and popovers must be viewport-bounded, scroll safely and remain attached to their triggering controls. No menu or modal may be positioned using assumptions that fail when the window is resized.
- Do not hide security, payment, validation, order or network status fields simply to fit a narrow layout. Compact or relocate secondary information while retaining access to critical facts.
- Keep controls, focus rings and labels usable under 100%, 125%, 150%, 175% and 200% Windows scaling. Avoid fixed pixel text sizes and fixed-height controls that clip enlarged content.

### Structural verification before accepting UI work

For every changed UI area, inspect the actual repository tree and verify:
1. one canonical implementation of the shared shell and navigation is used;
2. color, typography, spacing and breakpoint values come from central tokens;
3. no duplicate or shadow component has been introduced;
4. all page modules use the same shared interaction and visual states;
5. no responsive rule, import or asset path is broken;
6. page content reflows at each canonical breakpoint without overlap, clipping or accidental page-wide horizontal scrolling;
7. tables, dialogs, forms and long identifiers remain usable at the required viewport and scaling checks; and
8. all new files are within Production/Development and serve a defined purpose.

Run responsive checks at the Design Engineer's verification matrix and record the exact viewport, Windows scale, interaction and observed result. A passing repository path check alone does not prove responsive behavior. No UI implementation currently follows from this vision note; these are governing constraints for future approved work.
