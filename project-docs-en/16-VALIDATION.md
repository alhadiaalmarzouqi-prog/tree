# Validation Report (automated structural checks)

**Purpose:** Results of the automated validation of the English documentation set (mission §8).
**Scope:** The structural checks below. Semantic/manual review and a second independent reviewer are separate and not yet performed.
**Status:** Results recorded. This report is not an approval.
**Method:** `verification/validate_docs.py` (results also in `verification/validation-output.txt`).
**Last verified:** 2026-11-01 (final re-run after defect fixes).

## 1. Check results

| # | Check | Result |
|---|---|---|
| 1 | All source files unchanged (SHA-256 vs manifest) | PASS (14/14) |
| 2 | Protected fixture parses; 22 expected IDs | PASS |
| 3 | Fixture per-case pair-count consistency | PASS |
| 4 | Requirement identifiers preserved (source vs English set) | PASS (source 114, English 114, missing [], extra []) |
| 5 | English cross-references resolve | PASS after fixes (see defects below) |
| 6 | Decision identifiers defined in source | PASS (34 DR IDs; DR-32…34 documented as proposal-source) |
| 7 | OPEN identifiers within tracked range | PASS (OPEN-1…21 seen; none outside range) |

## 2. Defects found and fixed by validation

| # | Location | Defect | Fix |
|---|---|---|---|
| VAL-01 | `08-MATHEMATICAL-REFERENCE.md` section header | referenced `16-VALIDATION.md` before it existed | document created under that name |
| VAL-02 | `10-ANALYSIS-REFERENCE.md` (actual: `10-ANALYSIS-REPORT.md`) | wrong cross-reference `07-CONFLICTS-AND-GAPS.md` | corrected to `05-CONFLICTS-AND-GAPS.md` |

After these fixes the validation re-run reports **0 dangling references** and **0 identifier mismatches**.

## 3. What this validation does NOT prove

- It does not prove semantic equivalence of any English document with its Arabic source.
- It does not prove mathematical correctness of the M0 companion (a full recalculation of the 22 fixtures is a separate authorized task and was not performed).
- It does not prove owner approval of any label marked OWNER-APPROVED (see `07-DECISION-EVIDENCE-REGISTER.md`).
- It does not prove completeness of the reconstruction (a human/manual review of each document against its source is required).

## 4. Evidence and status

- Automated checks: **PASS** (`validation-output.txt` final run: exit 0, `RESULT: PASS ; failures=[]`; 13 documents covered by the automated structural check, namely `03`–`15` — see `README.md` §1.1 for the authoritative counting categories; 114/114 requirement IDs; 0 dangling references; 34 DR identifiers from source; OPEN range 1–21).
- Manual review: not yet performed (next step).
- Independent semantic review by a second reviewer: not yet performed (mission Phase D).
- English documents are therefore either "complete, awaiting independent review" or "blocked by missing evidence" as listed in the final migration report; none is "reviewed" or "approved".
---

## M2-R15 validation entry — 2026-11-02 (decision-register correction)

Checks executed for the M2-R15 correction; results are recorded from actual runs (no check reported without execution).

| Gate | Check | Result |
|---|---|---|
| G1 | New/added text is English (Arabic-script code points `[\u0600-\u06FF]` in added regions) | PASS — `DECISIONS.md` 0 Arabic chars; added regions of all changed documents 0 Arabic chars |
| G2 | Register coverage: Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12 present once; P1–P17 rows once | PASS — Q headers 10/10; P rows 17/17 |
| G3 | Unresolved items remain explicitly unresolved (Q4/OPEN-2, Q6/OPEN-4, OPEN-16 mechanism, DR-30/OPEN-19) | PASS — listed in register §4; no answer invented |
| G4 | No stale live-document claim that the register is absent | PASS — inline supersession/amendments in 00, 01, 07, 09, 13, 15; dated addenda in 17 and PHASE-A-GATE-REPORT; historical manifest variants labelled historical |
| G5 | New identifiers unique and defined only in M2-R15 sections | PASS — 22/22 new IDs, each defined once, first occurrence after historical sections (03) and after row 188 (04) |
| G6 | Full inventory diff vs M2-R14 baseline (47 files) | PASS — added: 1 (`DECISIONS.md`); changed: 15 English documents including this one; removed: 0; all other files byte-identical |
| G7 | Protected files unchanged | PASS — M0 = `B69AD1DF…`; fixtures = `FF52DF52…`; Arabic sources + `CLAUDE.md` 14/14 unchanged |
| G8 | Arabic draft archived; project copy removed | PASS — archive SHA-256 `ABEFBB230759C2B13EC39D0406C9B596A305B7135210F02DDA3A3F1D36A40E96`; project copy absent |

This entry itself modifies `16-VALIDATION.md` (the 15th changed English document in G6). The Arabic draft remains archived only as historical evidence.