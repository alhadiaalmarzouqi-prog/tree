# 00 — Source Manifest and Preservation Baseline

**Document status:** Phase A (source inventory and preservation). Not a reconstruction of any specification.
**Scope:** Every file under the project root `C:\Users\test\Desktop\شجرة العائلة` at the time of inventory.
**Owner approval:** None. This manifest records files; it does not approve any decision.
**Last verified:** 2026-11-01 (hashes and line counts computed in this session).
**Related documents:** `01-MISSING-EVIDENCE.md`.

## 1. Method

- Hash algorithm: SHA-256 (`Get-FileHash -Algorithm SHA256`), uppercase hexadecimal.
- Byte size: file length reported by the file system.
- Line count: number of physical lines in the decoded UTF-8 text (newline count, plus 1 only if the file does not end with LF). Corrected from the v1 method ("newline count + 1"); see `00-SOURCE-MANIFEST.v2-correction.md`.
- Inventory: recursive listing of the project root, including hidden files. Result: 14 files.
- Source files were only read. None was modified, renamed, moved, or deleted.

## 2. Source Inventory (baseline hashes)

| # | Relative path | Bytes | Lines | SHA-256 |
|---|---|---|---|---|
| 1 | `CLAUDE.md` | 3068 | 39 | AF5CC42A65D06F86E2CE1C26B55A3BCAD5E9F067D65069C7176DBE67EEEB23A0 |
| 2 | `project-docs\MASTER-ARCHITECTURE.md` | 54332 | 470 | AE1DCD6CDC0A4DDCB8D8BAE5DA39653625AC2C841EE721AAD8B96B9D500CC9E8 |
| 3 | `project-docs\analysis\ANALYSIS-REPORT.md` | 5181 | 62 | 387E0A4A1BC6EF3E1391D5A5B0C74D753C8DFFACEE986C359888E9F2172B2E56 |
| 4 | `project-docs\analysis\CONFLICTS-AND-GAPS.md` | 19821 | 272 | DDD4A13149FAC0D6FBD5EDAD3574A23916EAC04DFAE0D7F91FE80BC98A0E57F1 |
| 5 | `project-docs\analysis\DECISION-REGISTER.md` | 14235 | 123 | 76A5D69E2660369F400B0D52A5452D39BE224166C047C6F53B5A5047B7199F7A |
| 6 | `project-docs\analysis\DECISIONS-REQUIRED.md` | 17398 | 186 | A3A4F970FD2B43358D285A1CB0ABF9A5B08626F47BFC2CB9E3F48DA486BAD060 |
| 7 | `project-docs\analysis\KINSHIP-MATHEMATICAL-REFERENCE.md` | 18147 | 216 | B69AD1DF6188EB12FA77A125BFBB299B25AEFBCA1BB265B81F97443F0250DD45 |
| 8 | `project-docs\analysis\REQUIREMENTS.md` | 17755 | 202 | F6E198F24BD53BB0A0C8EEAA706F613902E20B624AFB527069441C7016937EA5 |
| 9 | `project-docs\analysis\TRACEABILITY-MATRIX.md` | 17834 | 183 | 34142D3E123DD6E902F57175762FE0B7519F725F29505BCB5EC72B891363653D |
| 10 | `project-docs\handoffs\NEXT-AGENT.md` | 4063 | 42 | E0ED5E3A39EC3C71F0093BC4AE7D92CE20281682174BACF4B34BF8A279BB6DDF |
| 11 | `project-docs\reference-fixtures\kinship-reference-cases.json` | 37807 | 819 | FF52DF522E07ADFC59EB84F78A5B27D007CF636D67228898DFFEA03E07243A46 |
| 12 | `project-docs\standards\AGENT-EXECUTION-RULES.md` | 2868 | 39 | 36214855C0E93DCA03D98622B6B2CB49CFF0A590686BADFAC1982097D8FB7BE2 |
| 13 | `project-docs\standards\CODE-ORGANIZATION-RULES.md` | 3528 | 39 | 0631003CBB1431FED8C3D75756C62D545B4ACFAA8D00E4E6C7D74815737F879A |
| 14 | `project-docs\standards\DOCUMENTATION-STANDARDS.md` | 3423 | 35 | C980829C75BE5C6C534A67C3718F4DC65A55CA4DAC6BAEC5BD31DB9C83EC7B51 |

**Line-count note (M2-R9):** the "Lines" column above contains the corrected physical line counts (v2). The historical v1 manifest (original line counts) is preserved unchanged as `00-SOURCE-MANIFEST.v1-original.md`; the correction details are in `00-SOURCE-MANIFEST.v2-correction.md`. Byte sizes and SHA-256 hashes are unchanged and continue to match.

## 3. Read Status (honest coverage)

"Read in full" means every line was displayed. "Partial" means some ranges returned placeholders or truncated output and were not fully re-displayed. Partial documents must not be treated as completely verified.

| # | File | Read status |
|---|---|---|
| 1 | CLAUDE.md | Read in full |
| 2 | MASTER-ARCHITECTURE.md | Read in full (in ranges covering lines 1–470) |
| 3 | ANALYSIS-REPORT.md | Read in full |
| 4 | CONFLICTS-AND-GAPS.md | Read in full (lines 1–272 covered across reads; 80–199 re-displayed by PowerShell) |
| 5 | DECISION-REGISTER.md | Read in full (lines 1–123 covered across reads; 41–62 re-displayed by PowerShell) |
| 6 | DECISIONS-REQUIRED.md | Read in full (lines 1–186 covered across reads; 57–117 re-displayed by PowerShell) |
| 7 | KINSHIP-MATHEMATICAL-REFERENCE.md | Read in full (sections A–G displayed across reads) |
| 8 | REQUIREMENTS.md | Read in full (FR, PRV, SEC, GOV, TECH, DATA, PERF, OPS, TST, SCOPE, PLAN). ID counts verified programmatically: 114 unique IDs. |
| 9 | TRACEABILITY-MATRIX.md | **Partial.** Lines 1–88 displayed (FR, PRV, SEC). Lines ~89–121 (GOV, TECH sections) were truncated and not re-displayed. Lines 122–183 displayed in the first read. |
| 10 | NEXT-AGENT.md | Read in full |
| 11 | kinship-reference-cases.json | **Partial for case-level detail.** Parsed successfully: 22 cases with the expected IDs. Cases T01–T10, T13, T14, DI-05a, DI-05b, ST-01, ST-02 displayed. Mid-file cases (T11, T12 body, ST-03 body, ST-04 and ST-05 bodies) were truncated and not fully re-displayed. The file was not modified. |
| 12 | AGENT-EXECUTION-RULES.md | Read in full |
| 13 | CODE-ORGANIZATION-RULES.md | Read in full |
| 14 | DOCUMENTATION-STANDARDS.md | Read in full |

**Consequence:** No English document may be marked "complete" for any part that relies on a partial file until that file's ranges are fully re-displayed.

## 4. Duplicates and Historical Versions

- No duplicate file content: all 14 SHA-256 hashes are distinct.
- No historical version of any project file exists inside the project root.
- `MASTER-ARCHITECTURE.md` section 16 says FR-017, FR-018, FR-020, PRV-005, DR-10, DR-28, and DR-02 in the existing analysis files still use older wording. That older wording is not present as separate files, so it cannot be re-verified.

## 5. Referenced But Absent Files

| Referenced by | Referenced name | Status |
|---|---|---|
| `CLAUDE.md`, `AGENT-EXECUTION-RULES.md`, `DOCUMENTATION-STANDARDS.md`, `NEXT-AGENT.md` | `project-docs/PROJECT-STATUS.md` | **MISSING** (planned, "to be created later") |
| `CLAUDE.md`, `MASTER-ARCHITECTURE.md`, `DOCUMENTATION-STANDARDS.md`, `CODE-ORGANIZATION-RULES.md`, and others | `DECISIONS.md` | **RESOLVED (M2-R15): created at `project-docs-en/DECISIONS.md`** — `MASTER-ARCHITECTURE.md` section 16 item 5 describes the pre-M2-R15 state |
| `MASTER-ARCHITECTURE.md`, `DECISION-REGISTER.md`, `KINSHIP-MATHEMATICAL-REFERENCE.md`, and others | M1-E report (decision evidence) | **MISSING** (see `01-MISSING-EVIDENCE.md`) |
| `REQUIREMENTS.md` header | Original specification "Sovereign Lineage Platform — الإصدار 1.0" (sections 1–17) | **MISSING** from project. `MASTER-ARCHITECTURE.md` section 16 item 4 says the spec's sections 5–7 are not inside the project |
| `REQUIREMENTS.md` header and PLAN-007 | Planning-task text ("نص مهمة التخطيط المرفق") | **MISSING** from project |
| `CODE-ORGANIZATION-RULES.md` section 6 and others | `KNOWN-ISSUES.md`, `CHANGELOG.md`, `TEST-STRATEGY.md`, `execution/` | **MISSING** (planned, not created) |
| `MASTER-ARCHITECTURE.md` section 15 | `DATABASE-DESIGN.md`, `RELATIONSHIP-ENGINE.md`, `SECURITY-AND-PRIVACY.md`, `API-SPECIFICATION.md`, `UI-UX-SPECIFICATION.md`, `TEST-STRATEGY.md` | **MISSING** (planned milestones M3–M8, not started) |
| Mission item `D-01` to `D-10` | Contradiction register D-01 to D-10 | **MISSING**. Zero occurrences of `D-01`–`D-10` in any project file. The project catalogues contradictions as `CG-01`–`CG-43`. The mapping is not documented. |

## 6. Files Not Fully Inspectable

- `kinship-reference-cases.json`: partial case-level inspection (see section 3). Field-level semantics were not recalculated; that is a separate task.
- `TRACEABILITY-MATRIX.md` lines ~89–122: not re-displayed after truncation.
- Documents labelled `OWNER-APPROVED` cannot be checked against owner communication, because the M1-E report and approval records are missing. The labels are recorded as claims, not as evidence.

## 7. Protected Items (must remain unchanged)

| Item | Protection rule | Baseline hash |
|---|---|---|
| `project-docs\reference-fixtures\kinship-reference-cases.json` | Must not change (mission restriction 3) | FF52DF522E07ADFC59EB84F78A5B27D007CF636D67228898DFFEA03E07243A46 |
| `project-docs\analysis\KINSHIP-MATHEMATICAL-REFERENCE.md` (M0 reference) | Must not change (mission restriction 2) | B69AD1DF6188EB12FA77A125BFBB299B25AEFBCA1BB265B81F97443F0250DD45 |
| All Arabic source files (items 1–14) | Must not be deleted, overwritten, or renamed | As listed in section 2 |

Any change to these hashes is a violation of the mission restrictions unless the owner explicitly approves it.

## 8. Re-verification

Before any English document is marked complete, re-run the SHA-256 inventory. A mismatch against section 2 means a source file changed; this manifest must then be rebuilt and the change reported.
---

## M2-R15 addendum — 2026-11-02

- The official decision register was created at `project-docs-en/DECISIONS.md` (2026-11-02, M2-R15). The missing-items row for `DECISIONS.md` above is marked **RESOLVED**; `MASTER-ARCHITECTURE.md` section 16 item 5 describes the pre-M2-R15 state and remains historical wording.
- The Arabic-source hashes in this manifest are unchanged by M2-R15; only the noted row was updated.
