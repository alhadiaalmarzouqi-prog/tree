# Source-to-English Traceability

**Purpose:** Trace every Arabic source file to the English document(s) that reconstruct it and every statement class to its evidence tag. This is the deliverable that makes the reconstruction auditable.
**Scope:** All 14 source files (incl. `CLAUDE.md`) → English documents; requirement/decision IDs; evidence classes.
**Status:** Draft.
**Source references:** `00-SOURCE-MANIFEST.md` (Phase A), the source files themselves.
**Last verified:** 2026-11-01.

## 1. File-to-English mapping

| Arabic source (authority) | English document(s) | Coverage |
|---|---|---|
| `CLAUDE.md` | `README.md`, `11-NEXT-AGENT.md`, `07-DECISION-EVIDENCE-REGISTER.md` | entry-point rules; decisions register rules; current-phase note |
| `project-docs/MASTER-ARCHITECTURE.md` | `09-MASTER-ARCHITECTURE.md` | sections 1–16, all status tags, OPEN table, roadmap |
| `project-docs/analysis/ANALYSIS-REPORT.md` | `10-ANALYSIS-REPORT.md` | extraction, conflicts, quality notes |
| `project-docs/analysis/CONFLICTS-AND-GAPS.md` | `05-CONFLICTS-AND-GAPS.md` | CG-01…CG-43, dependencies, RISK-001…010 |
| `project-docs/analysis/DECISION-REGISTER.md` | `07-DECISION-EVIDENCE-REGISTER.md`, `06-DECISIONS-REQUIRED.md` (notes) | DR groups, DR-02/DR-28 conflict, proposed DR-32…34 |
| `project-docs/analysis/DECISIONS-REQUIRED.md` | `06-DECISIONS-REQUIRED.md` | DR-01…DR-31 full text; blocking summary |
| `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` | `08-MATHEMATICAL-REFERENCE.md` | sections A–G restated, definitions unchanged |
| `project-docs/analysis/REQUIREMENTS.md` | `03-REQUIREMENTS.md`, `04-TRACEABILITY-MATRIX.md` | 114 requirements; matrix |
| `project-docs/analysis/TRACEABILITY-MATRIX.md` | `04-TRACEABILITY-MATRIX.md` | 114 rows; M0 note |
| `project-docs/handoffs/NEXT-AGENT.md` | `11-NEXT-AGENT.md` | handoff rules; action items |
| `project-docs/reference-fixtures/kinship-reference-cases.json` | `08-MATHEMATICAL-REFERENCE.md` §E/G; NOT copied in full | 22 fixtures, protected; referenced only |
| `project-docs/standards/AGENT-EXECUTION-RULES.md` | `12-STANDARDS.md` §3 | §3.1–3.6 |
| `project-docs/standards/CODE-ORGANIZATION-RULES.md` | `12-STANDARDS.md` §2 | §2.1–2.6 |
| `project-docs/standards/DOCUMENTATION-STANDARDS.md` | `12-STANDARDS.md` §1 | §1.1–1.5 |

## 2. Identifier families and where they appear

| Family | Source of record | English documents that use them |
|---|---|---|
| FR-001…FR-043 | `REQUIREMENTS.md` | 03, 04, 05, 09 |
| PRV, SEC, GOV, TECH, DATA, PERF, OPS, TST, SCOPE, PLAN | `REQUIREMENTS.md` | 03, 04, 05, 09 |
| CG-01…CG-43 | `CONFLICTS-AND-GAPS.md` | 05, 07, 15 |
| RISK-001…010 | `CONFLICTS-AND-GAPS.md` | 05 |
| DR-01…DR-31 | `DECISIONS-REQUIRED.md` | 06, 07, 09, 15 |
| DR-32…DR-34 | `DECISION-REGISTER.md` (proposals) | 06 (notes), 07 |
| KD-01, KD-02 | `KINSHIP-MATHEMATICAL-REFERENCE.md` §A; `MASTER-ARCHITECTURE.md` | 07, 08, 09 |
| OPEN-1…OPEN-21 | `MASTER-ARCHITECTURE.md` §13 | 09, 15 |
| M1-E, M1-A, M1-B, PD, NG | conversation-derived citations in `MASTER-ARCHITECTURE.md` | 07, 09 (as unverifiable claims) |
| KE-04, KE-05 | appear in `MASTER-ARCHITECTURE.md` §6.4 and OPEN-7 (path display order); no definition or authority in any project file — origin and meaning unverified | 09 (carried as-is) |
| D-01…D-10 | none in project | registered as missing in 15 |

## 3. Evidence-class usage

| Class | Mark | Used where |
|---|---|---|
| VERIFIED | `[V: …]` | citations to REQUIREMENTS, M0, CONFLICTS sources |
| OWNER-APPROVED (claimed) | `[OA-claimed: M1-E]` | architecture principles; never treated as verified |
| PROPOSED | `[P]` | recommendations, options |
| OPEN | `[OPEN]` | all OPEN-1…21; pending DRs |
| CONFLICTED | `[CONFLICT]` | DR-02/DR-28, CG-01, CG-28, CG-42, FR-010 |
| MISSING | `[MISSING]` (register) | M1-E, spec, planning text; DECISIONS.md — **created M2-R15** (`project-docs-en/DECISIONS.md`), no longer missing |
| REJECTED | used inside DR entries to mark alternatives rejected by the source (e.g., plain-text phone storage in DR-05); no owner-rejected decision exists to date | 06 (DR-05), 07 |

## 4. What is intentionally NOT in this set

- No literal translations (paraphrase-based reconstruction; meaning preserved).
- No copied fixture JSON (protected file is referenced, never duplicated elsewhere in the English set).
- No new requirement, decision, or approval IDs; DR-32…34 are carried over from the source proposal only and labeled as such.
- No claims of owner approval anywhere (all such labels are marked as claims).
---

## M2-R15 addendum — 2026-11-02

The decision register was created at `project-docs-en/DECISIONS.md` (2026-11-02, M2-R15). The `[MISSING]` (register) row above is updated accordingly. Remaining missing items (M1-E file, original specification §1–17, planning-task text) are unchanged.