# 00 — Source Manifest Correction v2 (M2-R7A)

**Status:** Correction to `00-SOURCE-MANIFEST.md` (v1). v1 is preserved unchanged as `00-SOURCE-MANIFEST.v1-original.md`.
**Date:** 2026-11-01.
**Reason:** v1 line counts used "newline count + 1", which counted an empty trailing segment for files ending in LF. Physical line counts are the correct figure for review.

## 1. Corrections

| Item | v1 value | v2 physical value | Change |
|---|---|---|---|
| Line-count method | newline count + 1 | number of physical lines (newline count, plus 1 only if the file does not end with LF) | Method corrected |
| Byte sizes | as recorded | unchanged (verified) | None |
| SHA-256 hashes | as recorded | unchanged (verified) | None |

## 2. Corrected physical line counts

| # | Relative path | Bytes | Physical lines (v2) | Physical lines (v1) |
|---|---|---|---|---|
| 1 | `CLAUDE.md` | 3068 | 39 | 40 |
| 2 | `project-docs\MASTER-ARCHITECTURE.md` | 54332 | 470 | 471 |
| 3 | `project-docs\analysis\ANALYSIS-REPORT.md` | 5181 | 62 | 63 |
| 4 | `project-docs\analysis\CONFLICTS-AND-GAPS.md` | 19821 | 272 | 273 |
| 5 | `project-docs\analysis\DECISION-REGISTER.md` | 14235 | 123 | 124 |
| 6 | `project-docs\analysis\DECISIONS-REQUIRED.md` | 17398 | 186 | 187 |
| 7 | `project-docs\analysis\KINSHIP-MATHEMATICAL-REFERENCE.md` | 18147 | 216 | 217 |
| 8 | `project-docs\analysis\REQUIREMENTS.md` | 17755 | 202 | 203 |
| 9 | `project-docs\analysis\TRACEABILITY-MATRIX.md` | 17834 | 183 | 184 |
| 10 | `project-docs\handoffs\NEXT-AGENT.md` | 4063 | 42 | 43 |
| 11 | `project-docs\reference-fixtures\kinship-reference-cases.json` | 37807 | 819 | 820 |
| 12 | `project-docs\standards\AGENT-EXECUTION-RULES.md` | 2868 | 39 | 40 |
| 13 | `project-docs\standards\CODE-ORGANIZATION-RULES.md` | 3528 | 39 | 40 |
| 14 | `project-docs\standards\DOCUMENTATION-STANDARDS.md` | 3423 | 35 | 36 |

## 3. Read-status correction for the two Task 1 files

| File | v1 status | v2 status |
|---|---|---|
| `kinship-reference-cases.json` | Partial (mid-file cases truncated in terminal output) | **Fully processed by script.** Read as bytes and parsed with `json.loads`; all 819 physical lines and 37,807 bytes were covered by the parser. 22 cases, IDs match the expected set, structural checks pass. Content was not modified (hash verified). Terminal truncation affected only display, not processing. |
| `TRACEABILITY-MATRIX.md` | Partial (lines ~89–122 not re-displayed) | **Fully processed by script.** 183 physical lines and 17,834 bytes read as UTF-8; 114 unique requirement IDs referenced, matching `REQUIREMENTS.md`. Human re-display of lines 89–122 was not performed; the script-level processing is the evidence for full processing. |

Note: the script result proves the file was fully read and parsed. It does not prove that each row was semantically checked against its source. Semantic review remains a Phase D task.

## 4. Hash verification result

All 14 source files (including `CLAUDE.md`) were recomputed. Results are in `project-docs-en/verification/phase-a-verification-output.txt`. Summary: 14 of 14 files matched the v1 manifest hash and byte size; 0 mismatches.
