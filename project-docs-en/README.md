# Sovereign Lineage Platform — English Technical Documentation Set

**Purpose:** Canonical English technical documentation for the Sovereign Lineage Platform, reconstructed from the verified Arabic source files.
**Scope:** Requirements, conflicts and gaps, decisions (evidence register), mathematical reference (M0), master architecture, standards, traceability, and cross-cutting reports.
**Status:** Reconstruction in progress. Nothing in this set is owner-approved or independently reviewed. Approval decisions are the owner's alone.
**Source references:** All source files are in `project-docs/` (Arabic, immutable). See `00-SOURCE-MANIFEST.md` (corrected v2 physical line counts; the historical v1 is preserved unchanged as `00-SOURCE-MANIFEST.v1-original.md`; the correction record is `00-SOURCE-MANIFEST.v2-correction.md`).
**Related documents:** `01-MISSING-EVIDENCE.md`, `PHASE-A-GATE-REPORT.md`, `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md`.
**Last verified:** 2026-11-01.

## 1. Where the documents live

| Document | Path | Source file(s) |
|---|---|---|
| Requirements | `03-REQUIREMENTS.md` | `project-docs/analysis/REQUIREMENTS.md` |
| Traceability matrix | `04-TRACEABILITY-MATRIX.md` | `project-docs/analysis/TRACEABILITY-MATRIX.md` |
| Conflicts and gaps | `05-CONFLICTS-AND-GAPS.md` | `project-docs/analysis/CONFLICTS-AND-GAPS.md` |
| Decisions required | `06-DECISIONS-REQUIRED.md` | `project-docs/analysis/DECISIONS-REQUIRED.md` |
| Decision evidence register | `07-DECISION-EVIDENCE-REGISTER.md` | `DECISIONS-REQUIRED.md`, `DECISION-REGISTER.md`, `CLAUDE.md`, analysis docs |
| Decision register (owner-approved decisions) | `DECISIONS.md` | owner decisions Q1–Q12 and principles P1–P17 (M2-R15, 2026-11-02) |
| Mathematical reference (M0) | `08-MATHEMATICAL-REFERENCE.md` | `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` (protected) |
| Master architecture | `09-MASTER-ARCHITECTURE.md` | `project-docs/MASTER-ARCHITECTURE.md` |
| Analysis report | `10-ANALYSIS-REPORT.md` | `project-docs/analysis/ANALYSIS-REPORT.md` |
| Handoff | `11-NEXT-AGENT.md` | `project-docs/handoffs/NEXT-AGENT.md` |
| Standards (English) | `12-STANDARDS.md` | three `project-docs/standards/*.md` files |
| Source-to-English traceability | `13-SOURCE-TO-ENGLISH-TRACEABILITY.md` | all sources |
| Corrected documentation defects | `14-CORRECTED-DOCUMENTATION-DEFECTS.md` | analysis of conflicts |
| Unresolved contradictions and decisions | `15-UNRESOLVED-CONTRADICTIONS.md` | all sources |
| Validation report | `16-VALIDATION.md` | automated checks (Stage D) |
| Arabic/English consistency status | `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md` | `project-docs/MASTER-ARCHITECTURE.md`, `DECISIONS.md`, all sources (M2-R17, 2026-11-02) |

### 1.1 Authoritative inventory and counting categories

This is the single authoritative inventory for the set. All counts quoted elsewhere in this set refer to one of the categories below.

| Category | Files | Count |
|---|---|---|
| Numbered files `00`–`18` (including the two historical manifest variants) | `00-SOURCE-MANIFEST.md`, `00-SOURCE-MANIFEST.v1-original.md`, `00-SOURCE-MANIFEST.v2-correction.md`, `01-MISSING-EVIDENCE.md`, `02-GLOSSARY.md` … `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md` | 21 |
| — of which: numbered content documents `02`–`16` | `02-GLOSSARY.md` … `16-VALIDATION.md` | 15 |
| — of which: Phase C reconstructed content documents `03`–`16` | `03-REQUIREMENTS.md` … `16-VALIDATION.md` | 14 |
| Owner-order register (created M2-R15) | `DECISIONS.md` | 1 |
| Supporting top-level files | `README.md`, `PHASE-A-GATE-REPORT.md`, `verify-task1-counts.txt` | 3 |
| Verification artifacts | 5 scripts (`verification/*.py`) + 5 outputs (`verification/*.txt`) | 10 |
| **Total files in `project-docs-en/`** | | **35** |

Notes:
- "14 documents" in the migration report refers to the Phase C content documents `03`–`16`; the same report's status table covers `02`–`16` (15 documents).
- The automated structural check covered 13 documents (`03`–`15`); `02`, `16`, and `17` are outside that script's scan list (see `16-VALIDATION.md`).
- `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md` (M2-R17, 2026-11-02) is a numbered document outside the Phase C content set (`03`–`16`); it records the Arabic/English consistency classifications and the verification method for the README's register counts.

## 2. Document status model

Every document in this set carries a status. The statuses mean:

| Status | Meaning | Used in |
|---|---|---|
| Draft | Reconstructed; not yet independently reviewed | All documents until review |
| Complete (awaiting review) | Content reconstructed from full source; structural checks pass | After Stage C8 |
| Complete (reviewed) | Independently reviewed (human or second agent) | Only after Stage D + owner acceptance |
| Blocked | Requires evidence that is missing (M1-E, specification, planning text) | Decision register, architecture |
| Owner decision pending | Requires an owner decision before it can move forward | OPEN items, DR items |

Nothing in this set may be marked "Complete (reviewed)" until an independent review has actually occurred. The presence of this README is not a review.

## 3. Evidence classification used in this set

| Class | Meaning | Marker in text |
|---|---|---|
| VERIFIED | Directly supported by an accessible source file in `project-docs/` | `[V: <source>]` |
| OWNER-APPROVED (claimed) | Label says owner approved; the M1-E report is missing, so the claim cannot be verified | `[OA-claimed: M1-E]` |
| OWNER-DIRECT-EVIDENCE | Decision stated directly by the owner; recorded in `DECISIONS.md` (M2-R15, 2026-11-02) | `OWNER-DIRECT-EVIDENCE` |
| PROPOSED | Technical recommendation; not approved | `[P]` |
| OPEN | Owner decision required | `[OPEN]` |
| CONFLICTED | Statements in source contradict each other | `[CONFLICT]` |
| MISSING | Evidence is not available | `[MISSING]` |
| REJECTED | Used inside DR entries to mark alternatives rejected by the source (e.g., plain-text phone storage in DR-05). No owner-rejected decision exists to date, and no `[R]` tag is used | within DR entries |

Rule: an OWNER-APPROVED label inside the Arabic source is treated as a claim, not as evidence of approval (mission restriction; see `01-MISSING-EVIDENCE.md` ME-01).

## 4. Preservation guarantees

- Every Arabic source file is byte-identical to the Phase A manifest (re-verified 14/14 by SHA-256).
- `kinship-reference-cases.json` (22 fixtures) and `KINSHIP-MATHEMATICAL-REFERENCE.md` are protected. They are only read.
- This workspace (`project-docs-en/`) is separate; nothing here modifies the sources.

## 5. Execution log

| Date | Action |
|---|---|
| 2026-11-01 | Phase A completed and gate PASSED (see `PHASE-A-GATE-REPORT.md`) |
| 2026-11-01 | Phase B/C reconstruction began; this index and glossary created |
| 2026-11-01 | M2-R9 defect corrections applied: authoritative inventory (this section), manifest line counts (v2), OWNER-APPROVED count, REJECTED class wording, FR-032 gloss removal, snapshot labelling, KE-04/KE-05 note, T12 cell formatting |
| 2026-11-02 | M2-R12 external deliverables (owner questions, decision evidence, dependency matrix, conflict register, manifest) produced in `%LOCALAPPDATA%\Temp\m2-r12\` |
| 2026-11-02 | M2-R13 owner decision briefing produced |
| 2026-11-02 | M2-R14: owner approved decisions Q1–Q12; an Arabic working draft of `DECISIONS.md` was created, then archived externally and removed from the project (M2-R15 correction) |
| 2026-11-02 | M2-R15: official register created in English at `DECISIONS.md`; affected English documents reconciled with dated amendment notes; Arabic sources and historical reports preserved unchanged |
| 2026-11-02 | M2-R17: stale register-absence statement corrected in `10-ANALYSIS-REPORT.md`; README register-count figure verified and corrected; `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md` created; governance note (§7) added; `07` status rows inline-marked. Arabic sources, M0, fixtures, `CLAUDE.md`, and `DECISIONS.md` unchanged |
| 2026-11-02 | M2-R24 execution: M3 conceptual design created under `m3-conceptual/` (M3-01 domain model, M3-02 privacy/audit/security/correction, M3-03 MVP and open-item classes, M3-04 review package, review status not performed). `DECISIONS.md` §3C extended: OQ-21-19 full rule set; OQ-21-18 exact wording. M0, fixtures, Arabic sources, historical reports unchanged. No migrations, schema, or code. |
| 2026-11-02 | M2-R24: product-scope reset (`DECISIONS.md` §3C.1); owner decisions OQ-21-03/05/07/08/10/12 recorded with partial status where detail remains; OQ-21-18 and OQ-21-19 recorded as owner decisions; amendments in `15`. P1, Q2, M0, fixtures, Arabic sources, and historical reports unchanged. |
| 2026-11-02 | M2-R23: OQ-21-16 recorded (`DECISIONS.md` §3B.4, option B, `OWNER-DIRECT-EVIDENCE`); M0 interpreted per network without modification; snapshot mechanism recorded as `AGENT-PROPOSAL` (§3B.5); OPEN-2 and OPEN-4 analysed, owner questions OQ-21-18 and OQ-21-19 (§3B.6); amendments in `02`, `03`, `09` (§19), `15`. Q11 independent review NOT executed (no review artifact found). M0, fixtures, Arabic sources, historical reports, and `CLAUDE.md` unchanged. |
| 2026-11-02 | M2-R22: owner confirmations mapped to Q13–Q23 (`DECISIONS.md` §3B; OQ-21-00 closed as a mapping, residual `UNVERIFIED`); OQ-21-01, OQ-21-02, OQ-21-06, OQ-21-14 recorded as owner decisions; OQ-21-15…17 opened; conflict C-R22-01 recorded; amendments in `03`, `09` (§5.3 note, §7.4, §18), `15`. M0, both M0 copies, the 22 fixtures, Arabic sources, historical reports, and `CLAUDE.md` unchanged. M3 remains BLOCKED. |
| 2026-11-02 | M2-R21: owner decisions from the M2-R21 brief registered as Q13–Q23 (`OWNER-APPROVED-CLAIM`, pending OQ-21-00); open matters OQ-21-00…OQ-21-14; conflicts C-R21-01…C-R21-06 recorded in `15-UNRESOLVED-CONTRADICTIONS.md`; amendment notes added to `03`, `09`, `15`. No P1–P17 or Q1–Q12 entry changed. M0, the 22 fixtures, Arabic sources, historical reports, and `CLAUDE.md` unchanged. M3 remains BLOCKED. |

### 5.1 M2-R15 language and preservation note

- Newly created or modified official engineering documentation in this set is written in **English** (owner's standing requirement).
- Decision registration and reconciliation (M2-R15) did **not** modify any original Arabic source document, `CLAUDE.md`, the M0 reference, the 22 reference fixtures, or the M2-R12/M2-R13 external deliverables.
- The historical reports (`PHASE-A-GATE-REPORT.md`, `17-MIGRATION-REPORT.md`) carry dated M2-R15 addenda; their original snapshot content is preserved.
- The Arabic working draft of `DECISIONS.md` is archived at `%LOCALAPPDATA%\Temp\m2-r14\DECISIONS.ar-draft-20261102.md` (SHA-256 `ABEFBB230759C2B13EC39D0406C9B596A305B7135210F02DDA3A3F1D36A40E96`) as historical evidence.

### 6. M2-R15 status summary

- **`DECISIONS.md` registers 17 principles (P1–P17) and owner decisions Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12; Q4 and Q6 are recorded as unresolved** (verified count on 2026-11-02: 17 principle rows + 12 Q identifiers in the register). The previously published "73 documented decisions/principle entries" figure is **not reproducible** from the register by any defined counting method and has been removed; the counting method is recorded in `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md` §3.
- Decisions recorded as `OWNER-DIRECT-EVIDENCE` (2026-11-02): Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12.
- Explicitly unresolved (no answer invented): Q4/OPEN-2, Q6/OPEN-4, OPEN-16 (mechanism), DR-30/OPEN-19.
- M3 remains **BLOCKED** until the dual independent review (Q11), owner approval of its outcome, and owner approval of the architecture are completed.

---

## 7. Governance — Arabic sources and the English decision register

Clarification (English only, 2026-11-02, M2-R17). It records how the existing documents are to be read; it does not amend any Arabic source and it does not approve any decision.

- The original Arabic documents under `project-docs/` are **preserved source records**. They are not modified by this set and are not edited without explicit owner authorization (see `00-SOURCE-MANIFEST.md` §7).
- `project-docs-en/DECISIONS.md` is the **current decision register** for decisions recorded in the English documentation workflow (created M2-R15, 2026-11-02). Current decision status is determined from the register and the reconciled English documents, subject to the evidence rules in `DECISIONS.md` §1.
- A statement in an Arabic source reflects the state at the time that source was written. **A historical statement in an Arabic source must not automatically be interpreted as the current project status.** Where a later recorded owner decision (Q1–Q12) supersedes an Arabic statement, the current status is the one recorded in the register and the reconciled English documents.
- The English documentation preserves **traceability to the Arabic source** (see `13-SOURCE-TO-ENGLISH-TRACEABILITY.md` and `18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md`).
- This clarification does **not** authorize changing the meaning of an Arabic source, does **not** invent missing owner-approval evidence, and does **not** convert proposals into decisions. Where a decision's approval evidence is unavailable, the matter remains unverified/open (see `01-MISSING-EVIDENCE.md` and `DECISIONS.md` §4).
