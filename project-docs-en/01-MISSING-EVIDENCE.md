# 01 — Missing Evidence Register

**Document status:** Phase A. Records what could not be verified. It does not reconstruct any missing document.
**Scope:** Evidence required for the English documentation set (M2-R7) that is absent from the project root.
**Owner approval:** None recorded in this document.
**Last verified:** 2026-11-01.
**Related documents:** `00-SOURCE-MANIFEST.md`.

## 1. Missing Evidence Items

| ID | Missing item | Where it is referenced | Effect on traceability | Status |
|---|---|---|---|---|
| ME-01 | **M1-E report** (original owner decisions, numbered items 1–17 and sections 1–3 as cited) | 38 references across `MASTER-ARCHITECTURE.md`, `TRACEABILITY-MATRIX.md`, `DECISION-REGISTER.md`, `KINSHIP-MATHEMATICAL-REFERENCE.md`, `CONFLICTS-AND-GAPS.md` | Every `OWNER-APPROVED` label in `MASTER-ARCHITECTURE.md` cites M1-E. The labels cannot be checked against the original owner wording. | **BLOCKED** |
| ME-02 | `DECISIONS.md` (formal decision register) | `CLAUDE.md` line 35; `MASTER-ARCHITECTURE.md` section 16 item 5 says it is absent; `DOCUMENTATION-STANDARDS.md`, `AGENT-EXECUTION-RULES.md`, `CODE-ORGANIZATION-RULES.md` | A formal register now exists at `project-docs-en/DECISIONS.md` (created M2-R15, 2026-11-02); section 16 item 5 records the pre-M2-R15 state. | **RESOLVED (M2-R15)** |
| ME-03 | `PROJECT-STATUS.md` | `CLAUDE.md` line 38; `NEXT-AGENT.md`; `AGENT-EXECUTION-RULES.md` | Current phase cannot be determined from the project. | **MISSING** |
| ME-04 | Original specification "Sovereign Lineage Platform — الإصدار 1.0" (sections 1–17) | `REQUIREMENTS.md` header; `MASTER-ARCHITECTURE.md` section 16 item 4 | All 114 requirement IDs (FR, PRV, SEC, GOV, TECH, DATA, PERF, OPS, TST, SCOPE, PLAN) were extracted from `REQUIREMENTS.md`, not from the specification itself. Requirement wording cannot be verified against the specification. | **MISSING** |
| ME-05 | Planning-task text (the longer "Master Planning" prompt) | `REQUIREMENTS.md` header and PLAN-007; `CODE-ORGANIZATION-RULES.md` (900-line reference) | The 900-line versus 700-line conflict (CG-42) cannot be checked against the original prompt. | **MISSING** |
| ME-06 | Contradiction register `D-01` to `D-10` | The mission text references it. **Zero occurrences** in any project file. | Contradictions cannot be re-evaluated against a register that does not exist in the project. The closest documented equivalents are `CG-01`–`CG-43`. | **MISSING** (mapping undocumented) |
| ME-07 | Sessions 2 and 3 outputs (`DATABASE-DESIGN.md`, `RELATIONSHIP-ENGINE.md`, `SECURITY-AND-PRIVACY.md`, `API-SPECIFICATION.md`, `UI-UX-SPECIFICATION.md`, `TEST-STRATEGY.md`, `KNOWN-ISSUES.md`, `CHANGELOG.md`, `execution/`, `phases/`) | `DOCUMENTATION-STANDARDS.md` section 1; `NEXT-AGENT.md` section 3 | Not started. These are not defects. They are outstanding work. | **NOT STARTED** |
| ME-08 | Owner approval records for M1-B (section 3, growth of the endorsement circle) and M1-A (identifiers PD, NG, KD) | `MASTER-ARCHITECTURE.md` section 5.3 ("M1-B"), section 16 item 3 ("M1-A") | Cited approvals cannot be traced to any file. | **MISSING** |
| ME-09 | Owner decisions for DR-01 to DR-31 | `DECISIONS-REQUIRED.md` says "لم يُتخذ أي قرار" (no decision taken). `NEXT-AGENT.md` section 2 confirms. | No DR item is approved. Recommendations are PROPOSED only. | **OPEN** (owner decision pending, not missing evidence) |
| ME-10 | Legal review for age of majority, data retention, and key destruction | `DECISIONS-REQUIRED.md` DR-06, DR-19; `MASTER-ARCHITECTURE.md` section 8.5 | No legal opinion exists in the project. Legal conclusions must not be assumed. | **MISSING** |
| ME-11 | Independent reviewer identity and report (DR-31, CG-43) | `DECISIONS-REQUIRED.md` DR-31; `AGENT-EXECUTION-RULES.md` section 5 | Independent review of this migration cannot be claimed until an independent reviewer and report exist. | **OPEN** (owner decision DR-31 pending) |

## 2. Effect on Decision Traceability

1. Counted by text search (re-verified in the M2-R9 correction): the Arabic source corpus (14 files) contains **70** occurrences of the label `OWNER-APPROVED`, **all of them in `MASTER-ARCHITECTURE.md`** and none in any other Arabic source file. Textual mentions of the label inside this English set are documentation references, not source labels. Most of the 70 source labels cite M1-E by item number. Because the M1-E report is not in the project, these labels are **claims without accessible evidence**. Under the mission rules (restriction 11), the label alone is not sufficient evidence of approval.
2. The project's own `MASTER-ARCHITECTURE.md` section 16 item 5 states that `DECISIONS.md` has not been created and that OWNER-APPROVED items "must be registered by a separate order". No such order is present.
3. A decision-evidence reconstruction (mission Phase B) may only be built from owner statements that are verifiable in project material or accessible conversation records. No such owner statements were found in the project files as direct quotations. The project files paraphrase them (for example, `MASTER-ARCHITECTURE.md` section 6.4 quotes an owner message "ورد في رسالة المالك" without the message itself).

## 3. Required Follow-up

| Action | Owner or actor | Blocks |
|---|---|---|
| Provide the M1-E report, or confirm that no such report exists | Owner | Any OWNER-APPROVED traceability (ME-01) |
| Provide the original specification and the planning-task text | Owner | Requirement-to-source verification (ME-04, ME-05) |
| Provide the `D-01`–`D-10` register, or confirm it is superseded by `CG-xx` / `DR-xx` | Owner | Mission Phase D validation (ME-06) |
| Confirm whether `DECISIONS.md` should be created, and from which approvals | Owner | Decision register (ME-02) |
| Confirm the reviewer arrangement | Owner (DR-31) | Independent review (ME-11) |

No item above is resolved by this document.
---

## M2-R15 amendment — 2026-11-02

1. **ME-02 — RESOLVED.** The formal register was created at `project-docs-en/DECISIONS.md` (2026-11-02, M2-R15) under the owner's Q12 order; it records P1–P17 and owner decisions Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12. Section 2 note 2 is superseded for this item: `MASTER-ARCHITECTURE.md` section 16 item 5 describes the pre-M2-R15 state.
2. **Section 3 action "Confirm whether `DECISIONS.md` should be created, and from which approvals" — completed.** The owner approved creation and recording (Q12; M2-R15 authorization). The remaining owner action is review of the register's recorded decisions.
3. **ME-09 — partially satisfied.** Owner decisions Q1–Q12 (2026-11-02) decide DR-02, DR-03, DR-04, DR-05, DR-11, DR-19 (in part), DR-28, and DR-31; all other DR-01…DR-31 items remain pending owner decisions.
4. **ME-11 — arrangement decided, execution pending.** Q11 decides the review arrangement (an independent AI agent that did not prepare the reviewed documentation **and** an independent human software engineer; findings compared; material disagreements resolved; owner approval of the outcome before M3). The independent review itself has not occurred; ME-11 remains open until a review and report exist.
