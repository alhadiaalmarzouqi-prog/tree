# Handoff to the Next Agent

**Purpose:** English reconstruction of the handoff file that tells the next agent which documents to read and what is blocked.
**Status:** Draft — reconstruction of `project-docs/handoffs/NEXT-AGENT.md` plus the current M2-R7 status.
**Source references:** `project-docs/handoffs/NEXT-AGENT.md`, `project-docs/CLAUDE.md`, `PHASE-A-GATE-REPORT.md`, this documentation set.
**Last verified:** 2026-11-01.

## 1. Current state

- The analysis session and core project documents are complete (session 1 of the source record). No project decision has been approved.
- Location: `C:\Users\test\Desktop\شجرة العائلة`.
- Current phase per this migration: M2 completed analysis documents; the English documentation set is under reconstruction (`project-docs-en/`). No execution phase is active. Phase 0 (planning and design) has not formally started.
- The current-phase file mentioned by `CLAUDE.md` (`project-docs/PROJECT-STATUS.md`) does not exist.

## 2. Files to read, in order

1. `CLAUDE.md` (project root).
2. `project-docs/analysis/ANALYSIS-REPORT.md` (Arabic) or `project-docs-en/10-ANALYSIS-REPORT.md` (English).
3. `project-docs/analysis/DECISIONS-REQUIRED.md` (Arabic) or `project-docs-en/06-DECISIONS-REQUIRED.md`.
4. `project-docs/standards/AGENT-EXECUTION-RULES.md` (Arabic) or `project-docs-en/12-STANDARDS.md` §3.
5. `project-docs/standards/DOCUMENTATION-STANDARDS.md` (Arabic) or `project-docs-en/12-STANDARDS.md` §1.
6. `project-docs/standards/CODE-ORGANIZATION-RULES.md` (Arabic) or `project-docs-en/12-STANDARDS.md` §2.

Reference only when needed: `REQUIREMENTS.md`/`03-REQUIREMENTS.md`, `CONFLICTS-AND-GAPS.md`/`05-…`, `TRACEABILITY-MATRIX.md`/`04-…`, `DECISION-REGISTER.md`/`07-…`.

## 3. M0 update (protected reference)

The internal mathematical reference `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` and the machine-readable reference fixtures `project-docs/reference-fixtures/kinship-reference-cases.json` (22 cases: T01–T14, ST-01–ST-06, DI-05a, DI-05b) are the internal baseline for future tests. They are not approvals of any pending decision and do not prove any application correct. When the kinship engine is implemented, this file is used and its definitions are not re-interpreted.

## 4. Decision-review-session update

`project-docs/analysis/DECISION-REGISTER.md` is a classification of the 31 decisions into four groups (A: architecture, B: database, C: phase-specific, D: configurable/deferred). It must be read before `DECISIONS-REQUIRED.md`. No original recommendation was changed and no decision was approved.

## 5. What awaits owner approval

- All DR-01…DR-31 in `06-DECISIONS-REQUIRED.md`; none resolved.
- Endorsement of CG-13 (weak connectivity/offline) as an independent decision.
- Confirmation of the 700-line file threshold (CG-42).

## 6. What to do only after owner approval

- Do not start any architecture document before the owner approves the analysis and the decisions that block phase 0.
- After approval, write the core documents in session 2: `MASTER-ARCHITECTURE.md`, `DATABASE-DESIGN.md`, `RELATIONSHIP-ENGINE.md`, `SECURITY-AND-PRIVACY.md`, `DECISIONS.md`.
- Then write phase files in session 3 with `PROJECT-STATUS.md` and an updated `handoffs/NEXT-AGENT.md`.

## 7. Prohibitions on the next agent

- No application files, code, database, or migrations.
- No package/installation/installation of dependencies.
- No pending decision made on the owner's behalf.
- No phase 1 or any execution phase without explicit approval.
- Nothing may be declared complete or tested without evidence.

## 8. Required owner action

Review `06-DECISIONS-REQUIRED.md` and approve or amend each decision, then reply in the same session. The next agent then starts session 2 per the plan above.

## 9. Note on handoff discipline

This file is updated at the end of every session. Agents rely on the files named here, not on the conversation log.
---

## M2-R15 Update — 2026-11-02

- A formal decision register now exists: `project-docs-en/DECISIONS.md` (English). It records P1–P17 and owner decisions Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12.
- Add to the read order (§2): **read `DECISIONS.md` after `06-DECISIONS-REQUIRED.md` / `07-DECISION-EVIDENCE-REGISTER.md`.**
- §5 ("What awaits owner approval") is updated: DR-02, DR-03, DR-04, DR-05, DR-11, DR-19 (in part), DR-28, DR-31 are **decided**; OPEN-1, OPEN-3, OPEN-8 (in scope), OPEN-21 (principle) resolved — see the register.
- Outstanding before M3: (a) the dual independent review required by Q11 (an independent AI agent that did not prepare the reviewed documentation AND an independent human software engineer; findings compared; material disagreements resolved; owner approval of the outcome) — **not yet performed**; (b) owner decisions on OPEN-2, OPEN-4, OPEN-16 (mechanism), DR-30/OPEN-19; (c) owner approval of the architecture. **M3 remains BLOCKED** until these are completed.
- Historical statements in §5/§6 ("no decision approved") describe the pre-M2-R15 state and are superseded to the extent above.