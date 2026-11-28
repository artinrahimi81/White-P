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


## Owner-Directed Dual Distribution Layout and Release Versioning — 2026-11-28

This section establishes the repository's permanent structural rules for maintaining two distinct distribution tracks: a complete developer track and a curated open-source track. It is an owner-approved structural policy, not authorization to publish, expose, move, rename or delete existing repository content. The existing product specification at `Production/task-decomposition/main-document.md` remains read-only.

### 1. Two canonical project paths

The two distribution roots are siblings under `Production/`:

```text
Production/
├── Development/                 # Complete developer/internal project
│   ├── ...                      # Existing development process and project materials
│   └── releases/
│       └── v0.0.0/
│           ├── release-manifest.json
│           ├── CHANGELOG.md
│           └── ...              # Complete approved developer-version snapshot
└── open-source/                 # Curated public distribution only
    └── releases/
        └── v0.0.0/
            ├── release-manifest.json
            ├── CHANGELOG.md
            └── ...              # Only explicitly approved public artifacts
```

Rules:

- `Production/Development/` is the default, authoritative and complete development workspace. All approved development work, application source, architecture, internal documentation, agent prompts, task records, dependency planning, implementation evidence, tests and other project materials remain governed by this path and its existing internal organization.
- `Production/open-source/` is not a second unrestricted development workspace and is not an alternative source of truth. It contains only versioned, reviewed and explicitly approved distribution output intended for public use.
- The developer track is authoritative. An open-source release is derived from a specific approved developer state; it must never become the only copy or silently replace the developer source.
- Keep the two roots distinct. Do not intermix internal task histories, agent instructions, internal planning, private operational documentation or development-only configuration with public release artifacts.
- Do not move or rename existing paths to implement this policy unless a separate, explicitly scoped task authorizes that migration. Existing paths under `Production/Development/` remain valid.
- Use the exact existing `Development` directory spelling for compatibility. Use lowercase-kebab-case for newly introduced path names; therefore the sibling public directory is exactly `open-source`.
- Do not create speculative subdirectories, duplicate copies, aliases, symlinks or convenience paths. Every new path must have a defined owner and purpose.

### 2. Versioned release directory convention

Each distribution track stores its releases under its own `releases/` directory. A release directory name is the lowercase letter `v` followed immediately by the exact three-part version number:

- Developer release: `Production/Development/releases/v0.0.0/`
- Open-source release: `Production/open-source/releases/v0.0.0/`

The initial version identifier for **both** tracks is `v0.0.0`, explicitly supplied by the project owner. The human-readable form may be displayed as `V 0.0.0`; the canonical directory and tag form has no spaces: `v0.0.0`.

Permanent rules:

1. Each version gets its own directory. Never overwrite the contents of one released version with the contents of a later version.
2. The exact version must be visible in the directory name, release manifest, release notes and corresponding Git tag. Downloadable archives, when produced, must also identify both the project and distribution track, for example `white-p-developer-v0.0.0.zip` and `white-p-open-source-v0.0.0.zip`.
3. Each version directory must contain `release-manifest.json` and `CHANGELOG.md`. The manifest is the machine-readable identity record; the changelog explains the meaningful changes in that exact release.
4. The manifest must identify, at minimum, the distribution track (`developer` or `open-source`), exact release version, release state, UTC creation/publication time as applicable, source commit SHA, and owner-approval reference. The open-source manifest must additionally identify the corresponding developer release version/source reference without exposing internal-only paths, secrets or private records.
5. Keep release records and their tags unambiguous. Use distinct annotated tag names: `developer-v0.0.0` and `open-source-v0.0.0`. The two tracks may have different version numbers in the future; their tag prefixes prevent collisions even when their version numbers match.
6. Do not create an unversioned `latest`, `current`, `stable` or duplicate release directory. The release directories, manifests and tags are the canonical identifiers. Any future index or pointer requires a demonstrated need and owner approval.
7. A published release is immutable. Never silently replace its files, reuse its version number for different content, or move an existing release tag. A correction or new content requires a new owner-approved version.
8. A draft is not a published release. Do not create or publish a GitHub Release, tag, archive or public distribution merely because a version directory exists.

### 3. Version-number authority and Semantic Versioning

Use Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`) as the version-numbering convention for both distribution tracks:

- `MAJOR`: an incompatible change to the public contract or behavior.
- `MINOR`: a backward-compatible addition of functionality.
- `PATCH`: a backward-compatible correction or fix.

Semantic Versioning supplies a consistent vocabulary for describing change impact; it does **not** grant an agent or engineer authority to choose a release number.

- Only the project owner may assign, approve, change or authorize a developer or open-source release version.
- Before creating a future version directory, changing a release manifest, preparing a release tag, publishing an archive or declaring a release, ask the owner for the exact version number and the track(s) to which it applies.
- Never calculate and apply the next version autonomously, even when the change appears to fit an obvious MAJOR, MINOR or PATCH increment. An agent may explain the likely Semantic Versioning category, but must wait for the owner's explicit version decision.
- Never infer a release version from a commit number, commit message, date, task ID, graph version, application version, previous release or the version of the other distribution track.
- The owner may approve the same version for both tracks or different versions for them. Do not assume that future developer and open-source versions must advance together.
- The current owner instruction fixes the initial version of both tracks at `v0.0.0`. This is the only release version pre-authorized by this section; it does not authorize an agent to choose any subsequent version.
- The repository's existing version-style commit-message convention (for example, `v 0.1.12`) is separate from product/distribution release versioning. Commit-message numbering must never be copied automatically into either release track.

Reference: Semantic Versioning 2.0.0 — https://semver.org/spec/v2.0.0.html

### 4. Developer-track content and information ownership

The developer track is the complete working and authoritative project record. Subject to existing project boundaries and applicable law, it may contain:

- Application source, build configuration, tests, development tools and technical documentation.
- Full architecture, implementation details, system maps, internal interfaces and operational procedures.
- Internal task catalogues, dependency graph, task-status records, agent prompts, task work logs, review reports and implementation evidence.
- Internal security architecture, threat models, risk assessments, control designs, vulnerability investigations, incident procedures and other security documentation not approved for public release.
- Internal configuration templates, deployment design and references to credentials or protected services.

Security distinction: the developer track may hold internal security **design and documentation**, but real secrets must not be stored as plaintext in Git, even in a private developer workspace. Passwords, API tokens, private keys, signing keys, recovery phrases, certificates and production credentials must be injected through an approved secret manager or protected runtime environment. Committed examples must use unmistakably nonfunctional placeholders. Local secret files must be excluded from version control and protected separately.

### 5. Open-source eligibility and mandatory exclusion rules

The open-source track is a deliberately curated public deliverable, not a copy of the developer track with a few known files removed.

- Build each public release from an explicit, reviewed **allowlist** of paths and artifacts that are approved for publication. A denylist alone is insufficient.
- Include only material whose publication is intentional, legally permitted, technically appropriate and approved by the owner.
- Exclude, unless the owner has explicitly authorized a safe public version: credentials and secret values; private keys and certificates; recovery material; personal or customer data; private endpoints and infrastructure details; internal logs and task histories; agent prompts and internal coordination records; private roadmap or planning material; non-public threat models; unresolved vulnerability details; incident evidence; deployment secrets; backups, dumps and local environment files.
- Do not publish security-sensitive implementation details merely because they are present in the developer track. Public security policies, high-level architecture or resolved advisories may be included only after an explicit publication review.
- Review third-party dependencies, copied assets, documentation and licenses. Include required license texts and third-party notices; do not publish material with unknown or incompatible redistribution rights.
- Do not place links, imports, symlinks, submodules or references in the public release that expose or depend on developer-only files, private paths, internal services or unapproved repositories.
- Keep the public release self-contained for its intended use. Do not omit required public runtime files merely to make the package appear smaller; verify that all included dependencies and instructions work without access to developer-only material.
- Record the public inclusion scope and the source developer version in the public manifest, without copying private file inventories or internal details into that manifest.

### 6. Required release preparation and verification

A release candidate must pass the following checks before publication:

1. **Source binding:** identify the exact approved developer source commit and owner-authorized version for the relevant track. Do not build a release from an ambiguous or moving working state.
2. **Path audit:** inspect the complete candidate tree; verify that every included path belongs to the correct track and every file has a clear purpose.
3. **Allowlist audit:** compare the complete candidate contents against the explicit public allowlist. Unexpected or unclassified files block the public release.
4. **Sensitive-data audit:** scan files and relevant Git history for tokens, passwords, private keys, personal data, customer information, internal endpoints, private logs and other sensitive material. A clean automated scan is useful evidence but does not replace human review.
5. **Dependency and license audit:** confirm the redistribution rights and required notices for included code, packages, assets and documentation.
6. **Reference audit:** check imports, links, configuration, build instructions and asset references. Public files must not point to developer-only locations.
7. **Build and verification:** run the release-appropriate build, tests and packaging checks. Record exact commands, environments and observed results; do not describe an unrun check as passed.
8. **Owner approval:** present the exact track, version, source commit, included scope, excluded categories, verification results and unresolved risks to the owner. Publication requires explicit approval.
9. **Release record:** create the track-specific manifest and changelog, then the corresponding immutable tag/release only after approval.
10. **Post-publication check:** verify the published artifact, version label, manifest, tag and download contents against the approved candidate.

GitHub secret scanning and push protection are defense-in-depth controls, not substitutes for path classification, review or owner approval. Reference: https://docs.github.com/en/code-security/concepts/secret-security/push-protection

### 7. Repository visibility is not a confidentiality boundary

A folder name, separate path, branch or release directory inside one repository does not make its contents private. When a repository is public, all committed paths and their accessible history are potentially public, including `Production/Development/`. Therefore, the two paths above provide logical organization and release separation only; they do not provide access control or confidentiality.

This policy does not change the repository's current visibility or move any files. Before the developer track is expected to become confidential while the open-source output remains public, the owner must approve and arrange a genuinely separate publication boundary, such as a dedicated public distribution repository or a filtered export that contains only the approved open-source release. Never claim that `Production/Development/` is hidden merely because `Production/open-source/` exists.

### 8. Scope and change control for this structural policy

- The Project Structure Engineer maintains these path, naming, release-layout and integrity rules. The Senior Engineer coordinates any task that implements them.
- No agent may independently assign release numbers, approve publication, change the distribution boundary, or decide that a file is safe for public release.
- A change to these permanent conventions requires explicit owner authorization and must be recorded as an append-only, task-labelled note.
- This policy defines the target structure; it does not itself create either release directory, copy the current project into a release snapshot, create manifests, generate archives, create tags, publish a release, change repository visibility or migrate existing content.
- Any such implementation must be handled in a separately scoped task, must inspect the live repository tree first, must create only required paths and must preserve all existing records.

