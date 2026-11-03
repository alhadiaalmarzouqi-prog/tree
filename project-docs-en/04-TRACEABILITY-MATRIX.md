# Traceability Matrix

**Purpose:** English reconstruction of the source traceability matrix linking every requirement to its design area, planned phase, verification method, and status.
**Scope:** 114 requirements (FR, PRV, SEC, GOV, TECH, DATA, PERF, OPS, TST, SCOPE, PLAN).
**Status:** Draft — reconstructed from `project-docs/analysis/TRACEABILITY-MATRIX.md` (verified: 114 IDs; all rows displayed across reads).
**Source references:** `project-docs/analysis/TRACEABILITY-MATRIX.md`; `03-REQUIREMENTS.md`.
**Related documents:** `03-REQUIREMENTS.md`, `05-CONFLICTS-AND-GAPS.md`, `09-MASTER-ARCHITECTURE.md`.
**Last verified:** 2026-11-01.

## 1. Status keys

| Key | Meaning |
|---|---|
| Open (مفتوح) | Not yet designed |
| Designed (مُصمَّم) | Documented in an approved document |
| Implemented (مُنفَّذ) | Present in reviewed code |
| Tested (مُختبَر) | Passed a named test |

Current status of every requirement: **Open**, except PLAN-001, PLAN-003, PLAN-004, PLAN-005, PLAN-006 which are "partially designed in this session" (see note in section 11). Phase keys are project phases 0–7 as in the specification (§13). "Design" refers to the expected documents to be written in later sessions.

## 2. Functional (FR)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| FR-001 | Registration and OTP verification | DATABASE-DESIGN, API-SPECIFICATION | 1 | registration & OTP integration test | Open |
| FR-002 | Person records | DATABASE-DESIGN | 1 | unit & integration test | Open |
| FR-003 | Person/account separation | DATABASE-DESIGN, SECURITY-AND-PRIVACY | 1 | database test + SEC-006 | Open |
| FR-004 | Limited-permission unregistered records | SECURITY-AND-PRIVACY | 1 | permission test | Open |
| FR-005 | Person states (registered, unregistered, deceased, incomplete) | DATABASE-DESIGN | 1 | unit test of states | Open |
| FR-006 | Father/mother relationships | DATABASE-DESIGN, RELATIONSHIP-ENGINE | 2 | unit & integration test | Open |
| FR-007 | Siblings and half-siblings | RELATIONSHIP-ENGINE | 2, 4 | golden test TST-005 | Open |
| FR-008 | More than one marriage | DATABASE-DESIGN, RELATIONSHIP-ENGINE | 2 | unit test | Open |
| FR-009 | In-laws separate | RELATIONSHIP-ENGINE | 4 | golden test | Open |
| FR-010 | Adoption as independent type | DATABASE-DESIGN | 2 | unit test | Open |
| FR-011 | Breastfeeding (conditional) | DATABASE-DESIGN | deferred (DR-14) | not tested before decision | Open |
| FR-012 | Acquaintance without lineage | DATABASE-DESIGN | 2 | unit test | Open |
| FR-013 | Restricted automatic linking | RELATIONSHIP-ENGINE | 3 | negative test (no generalization) | Open |
| FR-014 | Suggestions | DISCOVERY (to be defined later) | 3 | search & classification test | Open |
| FR-015 | Show suggestion reason | API-SPECIFICATION | 3 | API response test | Open |
| FR-016 | User response options | API-SPECIFICATION, UI-UX | 3 | integration test | Open |
| FR-017 | Verification cycle | RELATIONSHIP-ENGINE | 3 | state transition test | Open |
| FR-018 | Relationship states | RELATIONSHIP-ENGINE | 2, 3 | state-model test | Open |
| FR-019 | Rejection, dispute, correction | RELATIONSHIP-ENGINE, SECURITY-AND-PRIVACY | 3 | dispute scenario test | Open |
| FR-020 | Exclude non-confirmed from calculation | RELATIONSHIP-ENGINE | 4 | golden test TST-003 | Open |
| FR-021 | Kinship for any two people | RELATIONSHIP-ENGINE | 4 | golden test TST-001 | Open |
| FR-022 | Nearest common ancestor and generations | RELATIONSHIP-ENGINE | 4 | golden test | Open |
| FR-023 | Multiple paths | RELATIONSHIP-ENGINE | 4 | TST-002 | Open |
| FR-024 | Tenth degree | RELATIONSHIP-ENGINE | 4 | depth-limit test | Open |
| FR-025 | Arabic description | RELATIONSHIP-ENGINE, UI-UX | 4 | golden description test | Open |
| FR-026 | Show actual path | RELATIONSHIP-ENGINE, UI-UX | 4, 5 | unit & UI test | Open |
| FR-027 | Term dictionary | RELATIONSHIP-ENGINE | 4 | owner review + load test | Open |
| FR-028 | Interactive network | UI-UX | 5 | UI test | Open |
| FR-029 | Home page | UI-UX | 5 | UI test | Open |
| FR-030 | Search by name/phone | API-SPECIFICATION, SECURITY-AND-PRIVACY | 3 | privacy & rate-limit test | Open |
| FR-031 | Show path of search result | API-SPECIFICATION | 3, 5 | integration test | Open |
| FR-032 | Relatives classification | RELATIONSHIP-ENGINE, UI-UX | 5 | unit test | Open |
| FR-033 | Zoom and progressive loading | UI-UX | 5 | performance test | Open |
| FR-034 | Notifications and confirmation requests | API-SPECIFICATION | 3 | integration test | Open |
| FR-035 | Audit record | SECURITY-AND-PRIVACY | 1 | read/write test | Open |
| FR-036 | Privacy and permission management | SECURITY-AND-PRIVACY | 1, 6 | permission test | Open |
| FR-037 | Modification history | DATABASE-DESIGN | 2 | event-log test | Open |
| FR-038 | Prevent cycles and impossible relationships | RELATIONSHIP-ENGINE | 2 | negative test | Open |
| FR-039 | Add ancestors gradually | UI-UX, API-SPECIFICATION | 2, 5 | integration test | Open |
| FR-040 | Minimal registration data | UI-UX | 1 | registration test | Open |
| FR-041 | Show allowlisted person data | API-SPECIFICATION, SECURITY-AND-PRIVACY | 5 | privacy test | Open |
| FR-042 | Suggestions and verification screens | UI-UX | 5 | UI test | Open |
| FR-043 | Profile and relatives list | UI-UX | 5 | UI test | Open |

## 3. Privacy (PRV)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| PRV-001 | Hide person from suggestions when disabled | SECURITY-AND-PRIVACY, RELATIONSHIP-ENGINE | 3 | privacy test | Open |
| PRV-002 | Do not show phone to others | SECURITY-AND-PRIVACY, API-SPECIFICATION | 1 | API response test | Open |
| PRV-003 | Do not show unregistered persons publicly | SECURITY-AND-PRIVACY | 1 | permission test | Open |
| PRV-004 | Pending contracts not shown as confirmed | RELATIONSHIP-ENGINE, UI-UX | 3, 5 | state test | Open |
| PRV-005 | Hide minors' data | SECURITY-AND-PRIVACY | 1 | permission test | Open |
| PRV-006 | User controls what is shown | SECURITY-AND-PRIVACY | 1, 6 | settings test | Open |
| PRV-007 | No direct modification of confirmed link | RELATIONSHIP-ENGINE | 2 | negative test | Open |
| PRV-008 | Correction and dispute mechanism | RELATIONSHIP-ENGINE | 3 | scenario test | Open |
| PRV-009 | Retention policy | SECURITY-AND-PRIVACY | 1 | document review + deletion test | Open |
| PRV-010 | Phone matching with consent | SECURITY-AND-PRIVACY | 1, 3 | consent test | Open |

## 4. Security (SEC)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| SEC-001 | Prevent access between users | SECURITY-AND-PRIVACY | 1, 6 | access test | Open |
| SEC-002 | Encrypt sensitive data | SECURITY-AND-PRIVACY | 1 | encryption test | Open |
| SEC-003 | Database permissions | DATABASE-DESIGN | 1 | DB permission test | Open |
| SEC-004 | RLS | DATABASE-DESIGN | 1 (DR-04) | RLS test | Open |
| SEC-005 | Audit sensitive operations | SECURITY-AND-PRIVACY | 1 | log test | Open |
| SEC-006 | Inter-user access tests | TEST-STRATEGY | 6 | security test | Open |
| SEC-007 | Leak-path review | SECURITY-AND-PRIVACY | 6 | review + test | Open |
| SEC-008 | No linking by similarity | RELATIONSHIP-ENGINE | 2 | negative test | Open |
| SEC-009 | Protect unregistered persons | SECURITY-AND-PRIVACY | 1 | permission test | Open |

## 5. Governance (GOV)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| GOV-001 | No lineage by similarity | RELATIONSHIP-ENGINE | 3 | negative test | Open |
| GOV-002 | No automatic addition without path | RELATIONSHIP-ENGINE | 3 | negative test | Open |
| GOV-003 | No single authority | RELATIONSHIP-ENGINE, SECURITY-AND-PRIVACY | 3 | design review | Open |
| GOV-004 | Disputed not shown as fact | RELATIONSHIP-ENGINE | 3, 5 | state test | Open |
| GOV-005 | Person controls own data | SECURITY-AND-PRIVACY | 1, 6 | permission test | Open |
| GOV-006 | Record and verify every documented change | RELATIONSHIP-ENGINE | 2 | log test | Open |
| GOV-007 | Future features do not rebuild engine | MASTER-ARCHITECTURE | 0 | architecture review | Open |
| GOV-008 | Name only for candidates | RELATIONSHIP-ENGINE | 3 | negative test | Open |
| GOV-009 | Automatic network vs confirmed | RELATIONSHIP-ENGINE | 3, 4 | state test | Open |
| GOV-010 | Mutual agreement not absolute proof | RELATIONSHIP-ENGINE | 3 | state test | Open |
| GOV-011 | Separate biological kinship | RELATIONSHIP-ENGINE | 2, 4 | golden test | Open |
| GOV-012 | In-laws/adoption/breastfeeding independent | RELATIONSHIP-ENGINE | 2, 4 | golden test | Open |

## 6. Technical (TECH)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| TECH-001 | Unified app and single DB | MASTER-ARCHITECTURE | 0 | architecture review | Open |
| TECH-002 | NestJS | MASTER-ARCHITECTURE | 0, 1 | successful build | Open |
| TECH-003 | PostgreSQL source of truth | DATABASE-DESIGN | 0 | architecture review | Open |
| TECH-004 | Flutter mobile | MASTER-ARCHITECTURE | 0, 1 | successful build | Open |
| TECH-005 | Next.js when needed (DR-01) | MASTER-ARCHITECTURE | 0 | approved decision | Open |
| TECH-006 | PostgreSQL and Fuzzy search | DATABASE-DESIGN | 3 | search test | Open |
| TECH-007 | Redis when needed (DR-08) | MASTER-ARCHITECTURE | 7 | approved decision | Open |
| TECH-008 | FCM notifications | API-SPECIFICATION | 3 | integration test | Open |
| TECH-009 | Graph library | UI-UX | 5 | approved decision | Open |
| TECH-010 | Docker and CI/CD | MASTER-ARCHITECTURE | 7 | container build | Open |
| TECH-011 | No Neo4j | MASTER-ARCHITECTURE | 0 | architecture review | Open |
| TECH-012 | Closure Table (DR-02) | RELATIONSHIP-ENGINE, DATABASE-DESIGN | 2, 4 | equivalence test | Open |
| TECH-013 | Ancestor table (DR-03) | DATABASE-DESIGN | 2, 4 | equivalence test | Open |
| TECH-014 | Separate clear relationships | DATABASE-DESIGN | 2 | schema review | Open |

## 7. Data (DATA)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| DATA-001 | Registration fields (mandatory uncertain) | DATABASE-DESIGN, UI-UX | 1 | validation test | Open |
| DATA-002 | Optional fields and minor protection | DATABASE-DESIGN | 1 | validation test | Open |
| DATA-003 | Simple registration | UI-UX | 1 | UI test | Open |

## 8. Performance (PERF)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| PERF-001 | Progressive loading | UI-UX | 5 | performance test | Open |
| PERF-002 | Phones and weak networks | UI-UX | 5 | performance test on constrained network | Open |
| PERF-003 | Pre-launch performance tests | TEST-STRATEGY | 7 | performance test | Open |

## 9. Operational (OPS)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| OPS-001 | Execute phases 0–7 | PROJECT-STATUS | 0–7 | report review | Open |
| OPS-002 | Phase 0 outputs | MASTER-ARCHITECTURE | 0 | document review | Open |
| OPS-003 | Backup and monitoring | MASTER-ARCHITECTURE | 7 | recovery test | Open |
| OPS-004 | Final deployment | MASTER-ARCHITECTURE | 7 | deployment review | Open |
| OPS-005 | Real-family trial | TEST-STRATEGY | 7 | written consent (DR-25) | Open |
| OPS-006 | Time estimate | PROJECT-STATUS | — | not verifiable | Open |

## 10. Testing (TST)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| TST-001 | Kinship accuracy tests | TEST-STRATEGY | 4, 7 | golden tests | Open |
| TST-002 | Multi-path tests | TEST-STRATEGY | 7 | test | Open |
| TST-003 | Verification and conflict tests | TEST-STRATEGY | 3, 7 | test | Open |
| TST-004 | Registration, search, privacy tests | TEST-STRATEGY | 7 | test | Open |
| TST-005 | Golden tests | TEST-STRATEGY | 4 | golden tests | Open |

## 11. Scope and planning (SCOPE, PLAN)

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| SCOPE-001 | Deferred features | PROJECT-CHARTER | outside release | not applicable | Open |
| SCOPE-002 | Platform future | PROJECT-CHARTER | outside release | not applicable | Open |
| PLAN-001 | Permanent agent documentation | DOCUMENTATION-STANDARDS | 0 | document review | Partially designed (this session) |
| PLAN-002 | Execution file per phase | DOCUMENTATION-STANDARDS | 0 | document review | Open |
| PLAN-003 | Security in every phase | AGENT-EXECUTION-RULES | 0 | document review | Partially designed (this session) |
| PLAN-004 | Phase closure and handoff | AGENT-EXECUTION-RULES | 0 | document review | Partially designed (this session) |
| PLAN-005 | Stop after each phase | AGENT-EXECUTION-RULES | 0 | document review | Partially designed (this session) |
| PLAN-006 | Report blockers | AGENT-EXECUTION-RULES | 0 | document review | Partially designed (this session) |
| PLAN-007 | Two-instruction conflict | ANALYSIS-REPORT | analysis | owner review | Open |

## 12. Notes

1. "Partially designed" in the source means the agent rules were written in this session and have not been owner-reviewed; they are not implemented requirements. No requirement has been executed or tested.
2. **M0 reference:** the reference cases in `project-docs/reference-fixtures/kinship-reference-cases.json` are an **internal mathematical reference** for TST-001 (kinship accuracy), TST-002 (multi-path), and TST-005 (golden tests). This linkage does not change any requirement status from Open; automated code execution and testing have not occurred yet.
---

## 13. M2-R15 additions — decision-derived requirements (2026-11-02)

Rows below trace the owner-decision-derived requirements added in `03-REQUIREMENTS.md` §15 (owner decisions Q1–Q12, 2026-11-02, see `DECISIONS.md`). Status key applies as in §1; none of these is implemented or tested.

| ID | Brief description | Design area | Planned phase | Verification method | Status |
|---|---|---|---|---|---|
| FR-044 | Objection-active confirmed link stays in biological calculation | RELATIONSHIP-ENGINE | 3, 4 | objection/dispute scenario test | Open |
| FR-045 | Independent evidence as linked supporting data | RELATIONSHIP-ENGINE | 2, 3 | evidence-model test | Open |
| FR-046 | Audit retention and access control | SECURITY-AND-PRIVACY | 1, 4 | audit access and retention test | Open |
| FR-047 | Accountless record permissions | SECURITY-AND-PRIVACY | 1 | permission test | Open |
| FR-048 | Duplicate-person detection and resolution | DATABASE-DESIGN, API-SPECIFICATION, UI-UX | 2, 3 | duplicate-resolution scenario test | Open |
| PRV-011 | Per-field visibility control (optional profile fields) | SECURITY-AND-PRIVACY, UI-UX | 3 | visibility-policy test | Open |
| PRV-012 | Kinship-degree visibility groups, server-side enforcement | SECURITY-AND-PRIVACY | 3 | policy enforcement test | Open |
| PRV-013 | No private-data disclosure in duplicate suggestions | SECURITY-AND-PRIVACY | 3 | suggestion authorization test | Open |
| SEC-010 | RLS from the start; isolation plan/tests; ownership, BYPASSRLS, FORCE, app roles | SECURITY-AND-PRIVACY, DATABASE-DESIGN | 1, 4 | RLS isolation and direct-access test | Open |
| SEC-011 | Executable security tests required for RLS effectiveness claims | TEST-STRATEGY | 1, 8 | security test execution | Open |
| SEC-012 | At-rest encryption of phone and sensitive data | SECURITY-AND-PRIVACY | 1 | encryption test | Open |
| SEC-013 | Keyed HMAC phone lookup; no plaintext copy | SECURITY-AND-PRIVACY, DATABASE-DESIGN | 1 | HMAC lookup test | Open |
| GOV-013 | Dual independent review before M3 (AI agent + human engineer) | GOVERNANCE, MASTER-ARCHITECTURE | M2 close | independent-review report | Open (gate pending) |
| GOV-014 | No auto-merge by name similarity | RELATIONSHIP-ENGINE | 3 | negative merge test | Open |
| GOV-015 | Person-identity match does not confirm biological parentage | RELATIONSHIP-ENGINE | 3 | negative test | Open |
| GOV-016 | Kinship-description difference does not imply different people | RELATIONSHIP-ENGINE, DISCOVERY | 3 | duplicate-candidate test | Open |
| TECH-015 | Audit record fields (who/when/type/old+new); no full reconstruction | DATABASE-DESIGN | 1 | audit schema test | Open |
| TECH-016 | Derived structures reproducible; path/parent-role preserved; shortest-depth closure insufficient | DATABASE-DESIGN, RELATIONSHIP-ENGINE | 4 | derivation-equivalence test | Open |
| DATA-004 | Account ID vs Person ID | DATABASE-DESIGN | 1 | model test | Open |
| DATA-005 | Record without account; multiple candidate records | DATABASE-DESIGN | 1 | model test | Open |
| DATA-006 | Person ID uniqueness does not imply distinctness | DATABASE-DESIGN | 3 | model test | Open |
| OPS-007 | Formal register + documentation reconciliation | DOCUMENTATION-STANDARDS, MASTER-ARCHITECTURE | 0 (M2-R15) | document review | Partially designed (register created; approved review pending) |

**Note:** the list above supersedes no row in sections 1–12; each ID continues its existing series. The historical matrix (114 rows) remains in sections 1–12.