# Standards (English reconstruction)

**Purpose:** English reconstruction of the project's three standards files.
**Scope:** Documentation standards, code-organization rules, and agent-execution rules.
**Status:** Draft — the sources mark these as procedural drafts that "need owner approval" (`DOCUMENTATION-STANDARDS.md`) or as "binding for every implementing phase and need owner approval before application" (`CODE-ORGANIZATION-RULES.md`). This reconstruction does not change that status.
**Source references:** `project-docs/standards/DOCUMENTATION-STANDARDS.md`, `project-docs/standards/CODE-ORGANIZATION-RULES.md`, `project-docs/standards/AGENT-EXECUTION-RULES.md`.
**Related documents:** `09-MASTER-ARCHITECTURE.md`, `README.md`.
**Last verified:** 2026-11-01.

## 1. Documentation standards (from DOCUMENTATION-STANDARDS.md)

### 1.1 Permanent structure
| Path | Content | Owner |
|---|---|---|
| `CLAUDE.md` | mandatory agent entry point (short, refers rather than repeats) | owner |
| `project-docs/analysis/` | specification analysis: requirements, conflicts, pending decisions, traceability | analysis phase |
| `project-docs/standards/` | documentation standards, code organization, agent rules | owner |
| `project-docs/handoffs/` | agent handoff files | executing agent |
| `project-docs/` (later) | `MASTER-ARCHITECTURE.md`, `DATABASE-DESIGN.md`, `RELATIONSHIP-ENGINE.md`, `SECURITY-AND-PRIVACY.md`, `API-SPECIFICATION.md`, `UI-UX-SPECIFICATION.md`, `TEST-STRATEGY.md`, `DECISIONS.md`, `PROJECT-STATUS.md`, `KNOWN-ISSUES.md`, `CHANGELOG.md`, `phases/`, `execution/` | after analysis approval |

### 1.2 Writing rules
1. Every requirement has a stable identifier (FR, PRV, SEC, GOV, TECH, DATA, PERF, OPS, TST, SCOPE, PLAN, DR, CG, RISK). No identifier is reused or re-meaninged.
2. Facts from the specification are separated from recommendations; a recommendation is written only under the heading "technical recommendation".
3. Any assumption is written under the heading "assumption" and linked to a decision.
4. "Complete", "implemented", or "tested" is written only with evidence from a real execution whose path and result are named.
5. No fabricated or estimated numbers/test results are written as if real.

### 1.3 Versioning and change
- Every approved document carries a version on its first line after the title (e.g., "version 0.1 — draft").
- Any change to an approved document is recorded in `CHANGELOG.md` with its date, reason, and affected identifiers.
- Changing an approved decision requires: recording the impact in `DECISIONS.md`, owner approval, and updating every affected document.
- The approved path in `DECISIONS.md` is not silently changed.

### 1.4 Specification conformance
- Every development document begins with references to the `REQUIREMENTS.md` identifiers it covers.
- `TRACEABILITY-MATRIX.md` is the reference for linking requirement to design, phase, and test.
- On a conflict between a document and the specification, the specification or an owner decision prevails, and the conflict is recorded in `CONFLICTS-AND-GAPS.md` or `KNOWN-ISSUES.md`.

### 1.5 Language and formatting
- The source documents are in Arabic with technical terms in English as-is (e.g., PostgreSQL, RLS).
- Identifiers are in English with three-digit numbers (FR-001).
- Markdown tables for requirements and decisions; numbered section headings.

> Note: the source standard mandates Arabic documentation. The English set (this workspace) is an added canonical set created by owner decision M2-R7; the source standard itself is unchanged.

## 2. Code-organization rules (from CODE-ORGANIZATION-RULES.md)

### 2.1 Principle
Every file has one clear responsibility. New logic is not added to a large file merely because it resembles the existing code; evaluate whether it deserves its own module.

### 2.2 Limits
| Limit | Value | Action |
|---|---|---|
| Usual target per source file | 300–500 lines | acceptable |
| Strict review threshold | 700 lines | split the file or document a convincing reason |
| Maximum after exception | not to be exceeded without owner approval | exception recorded in `DECISIONS.md` |

Note: the planning task text mentioned 900 lines. This standard adopts 700 as the strict threshold because it is the most restrictive (CG-42; owner confirmation pending).

### 2.3 Mandatory rules
1. Every feature/task/responsibility has a module or file with a clear name.
2. Forbidden to merge into one file: different services, database operations, UI components, validation rules, business logic.
3. Split large components into smaller reusable components.
4. Separate Models, Schemas, Repositories, Services, Controllers, Validators, and tests per the approved structure.
5. No meaningless parts created just to reduce line count; no tearing apart cohesive logic without reason.
6. Every new feature comes with its own tests.
7. File/folder names express responsibility (e.g., `kinship-path.service.ts` instead of `utils.ts`).
8. Rules apply to the server, the app, the web if present, the database (migration files), and the tests.

### 2.4 Implementation constraints
- No business-logic duplication across locations; one source for kinship.
- No exceedance of the 700-line threshold in a phase delivery without a split or approved exception.
- No generic junk files such as `helpers.ts` or `common.ts` collecting unrelated things.
- No mock data as evidence of module success.

### 2.5 Verification
- Before delivery, record the line count of every new or changed file, with the two largest files.
- Any file over 700 lines is named in the phase report with the reason and action.
- The independent reviewer checks this section before approving the phase.

### 2.6 Related standards
Naming, processing, logging, and testing details are defined later in `TEST-STRATEGY.md` and `MASTER-ARCHITECTURE.md` after the analysis is approved; they are not written here to avoid duplication.

## 3. Agent-execution rules (from AGENT-EXECUTION-RULES.md)

### 3.1 Session scope
1. Each phase is executed in a separate new conversation.
2. Each phase has a clear scope; a stage other than the assigned one is not executed.
3. After completing the phase, the agent stops and does not start the next automatically.

### 3.2 Read before execute
1. Read `CLAUDE.md` first.
2. Read only the assigned phase file.
3. Read only the reference documents named in that phase file.
4. Inspect the actual code in the repository before any modification.

### 3.3 Prohibitions
- No fabricating files, functions, tables, test results, or execution states.
- No changing an approved architecture or approved business rule without owner approval.
- No deciding a pending decision in `DECISIONS-REQUIRED.md` on the owner's behalf.
- No modifying files outside the phase scope or overwriting existing work without inspection.
- No marking a phase complete without running tests and publishing their actual results.
- No adding mock data as evidence of success.

### 3.4 Completion requirements
1. Run the required tests and record real results, including failures.
2. Update `PROJECT-STATUS.md` and `CHANGELOG.md`, and update `KNOWN-ISSUES.md` when needed.
3. Update `DECISIONS.md` only when an owner-approved decision exists.
4. Write an execution report in `execution/` including: files created/modified, test results, unfinished tasks, blockers.
5. Update `handoffs/NEXT-AGENT.md` with a handoff referring to documents, not the conversation log.

### 3.5 Review and approval
- A phase is not approved merely because the agent says it is complete.
- Independent review must be possible before approval (DR-31).
- If a phase cannot be completed, blockers are reported accurately without marking the phase complete.
- The final approval decision belongs to the owner.

### 3.6 Reporting
- The report states what was done, what was not, and what was not tested, clearly.
- Every assumption is stated explicitly.

> Note: the source Arabic standards remain in force for the project. This reconstruction documents the same rules in English without changing them.