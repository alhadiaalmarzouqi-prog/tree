# Conflicts, Gaps, and Risks

**Purpose:** English reconstruction of the source conflict/gap/risk catalogue, preserving every CG and RISK identifier and their decision references.
**Scope:** CG-01 to CG-43, the dependency table, RISK-001 to RISK-010.
**Status:** Draft — reconstructed from `project-docs/analysis/CONFLICTS-AND-GAPS.md` (verified: CG-01…CG-43 present; contents displayed across reads).
**Source references:** `project-docs/analysis/CONFLICTS-AND-GAPS.md`; requirements in `03-REQUIREMENTS.md`.
**Related documents:** `03-REQUIREMENTS.md`, `06-DECISIONS-REQUIRED.md`, `15-UNRESOLVED-CONTRADICTIONS.md`.
**Last verified:** 2026-11-01.

## A. Direct conflicts

### CG-01 — RLS: applied from the start or in phase 6?
- **Requirements:** SEC-004, SEC-001, PRV-002, PRV-005.
- **Conflict:** The specification (§13) places RLS in phase 6, while the privacy-from-the-start principle (principles 8 and 10 in the task text) requires it from phase 1.
- **Why it matters:** Delaying it means phases 1 and 2 data are written without database-level controls, and adding it later requires full re-testing.
- **Decision:** DR-04.

### CG-02 — Closure Table and the "ancestor helper table": the same thing?
- **Requirements:** TECH-012, TECH-013, FR-021.
- **Conflict:** The specification mentions Closure Table in the technical table and an "ancestor helper table" in the same paragraph, without clarifying the relationship between them.
- **Risk:** Data duplication or divergent results between the two tables.
- **Decision:** DR-02, DR-03.

### CG-03 — Age of majority and application of minor protection
- **Requirements:** PRV-005, DATA-002.
- **Conflict:** The specification requires special minor protection without defining age of majority, or whether protection starts at birth-date entry or at input.
- **Risk:** Showing a minor's data, or wrongly hiding an adult's data.
- **Decision:** DR-06.

### CG-04 — "Mutual confirmation" vs "no absolute proof by consent"
- **Requirements:** FR-017, FR-018, GOV-010, FR-020.
- **Conflict:** The specification says two people's agreement is not absolute proof and requires independent evidence to grow the network, without defining the minimum evidence or the meaning of "independent".
- **Risk:** Either accepting incorrect relationships too easily, or stalling network growth.
- **Decision:** DR-09.

## B. Incomplete technical requirements

### CG-05 — The "when needed" criterion for Next.js
- **Requirements:** TECH-004, TECH-005.
- **Gap:** No condition says when the web is needed, nor whether it is in the first release.
- **Decision:** DR-01.

### CG-06 — The "when needed" criterion for Redis
- **Requirements:** TECH-007, PERF-001.
- **Gap:** No threshold (users, latency, query count) triggers Redis.
- **Decision:** DR-08.

### CG-07 — Target performance undefined
- **Requirements:** PERF-001, PERF-002, PERF-003.
- **Gap:** No numbers: target people count, kinship-calculation latency, displayed network size.
- **Decision:** DR-24.

### CG-08 — Phone matching method undefined
- **Requirements:** PRV-010, SEC-002, FR-030.
- **Gap:** The specification does not say whether the phone is stored encrypted or hashed, nor how matching works without exposing the number.
- **Risk:** Phone number leakage or enumeration via search.
- **Decision:** DR-05.

### CG-09 — OTP provider undefined
- **Requirements:** FR-001.
- **Gap:** No provider, resend policy, or attempt count.
- **Decision:** DR-22.

### CG-10 — Encryption and key management undefined
- **Requirements:** SEC-002, SEC-003.
- **Gap:** The specification does not define the "sensitive" fields, the algorithm, or key storage/rotation.
- **Decision:** DR-20.

### CG-11 — Hosting and data location undefined
- **Requirements:** TECH-010, OPS-003, OPS-004.
- **Gap:** No hosting provider, storage region, or legal framework for personal data.
- **Decision:** DR-21.

### CG-12 — Interface language undefined
- **Requirements:** FR-027, FR-028.
- **Gap:** The specification is Arabic but does not say whether the first release is Arabic-only or multilingual.
- **Decision:** DR-23.

### CG-13 — Weak connectivity and offline work
- **Requirements:** PERF-002.
- **Gap:** "Weak networks" without definition: is offline mode supported, and what is stored locally?
- **Decision:** to be added as an independent decision during the phase-5 review (not yet a standalone DR). Note: `DECISION-REGISTER.md` proposes DR-32 for this.

## C. Unclear business rules

### CG-14 — Tenth-degree behavior and storage
- **Requirements:** FR-024, FR-021, TECH-012.
- **Gap:** The specification does not define system behavior beyond the tenth degree: store the relationship without display? Show "out of scope"?
- **Risk:** Closure Table bloat or slow queries.
- **Decision:** DR-07.

### CG-15 — "Family acquaintance without proven lineage" and its effect on calculation
- **Requirements:** FR-012, GOV-011.
- **Gap:** The text does not say whether this relationship enters the blood-kinship engine, appears in the path, or is excluded.
- **Decision:** DR-14.

### CG-16 — Adoption and breastfeeding and their effect on blood kinship
- **Requirements:** FR-010, FR-011, GOV-012.
- **Gap:** The specification does not say whether adoption counts as lineage relationship in the calculation or is displayed with a different label. Breastfeeding is deferred subject to "if decided".
- **Decision:** DR-14.

### CG-17 — In-law calculation and description rules
- **Requirements:** FR-009, GOV-012, FR-025.
- **Gap:** No rule for calculating in-law relationships or merging their description with the blood-kinship description.
- **Decision:** DR-13.

### CG-18 — Order of multiple paths and which is shown
- **Requirements:** FR-023, FR-026.
- **Gap:** The specification does not define which path is shown first, or how the description is chosen with multiple paths.
- **Decision:** DR-15.

### CG-19 — Sex and descriptive representation
- **Requirements:** DATA-001, FR-025, FR-027.
- **Gap:** Arabic kinship terms depend on sex, but the specification does not define handling of an unspecified value.
- **Decision:** DR-29.

### CG-20 — Term dictionary: scope, source, responsibility
- **Requirements:** FR-027.
- **Gap:** The specification does not define who maintains the dictionary, the approved sources for Libyan terms, or how dialect differences are handled.
- **Decision:** DR-16.

### CG-21 — Arabic name matching rules
- **Requirements:** FR-014, GOV-008.
- **Gap:** No normalization algorithm (hamzas, ta-marbuta vs ha, alif-maqsura, abbreviations) and no similarity threshold.
- **Decision:** DR-17.

### CG-22 — Determining "grandfather" and "recorded ancestors"
- **Requirements:** FR-014 (search element 4).
- **Gap:** How does the system decide that a "grandfather" name is the grandfather without an independent identifier? Affects discovery and suggestions.
- **Decision:** handled within DR-17 and DR-09.

### CG-23 — Correct state of an automatically inferred relationship
- **Requirements:** FR-013, GOV-009, FR-018.
- **Gap:** The specification does not say whether an inferred relationship is shown as "proposed" or "confirmed", nor whether it needs explicit confirmation.
- **Risk:** Generalizing an unproven relationship, which the specification explicitly forbids.
- **Decision:** DR-09.

### CG-24 — Deceased person and their privacy
- **Requirements:** FR-005, PRV-003.
- **Gap:** The specification does not say whether a deceased person's data is shown fully, or who may modify it after death.
- **Decision:** DR-27.

### CG-25 — Who creates and owns the unregistered record?
- **Requirements:** FR-004, FR-002, GOV-003, PRV-003.
- **Gap:** The specification does not define who may create an unregistered person's record, who modifies it, and who may see it. This shapes the risk of one-sided false lineage input.
- **Decision:** DR-11.

### CG-26 — Claiming an existing record (Claim)
- **Requirements:** SEC-008, FR-003, FR-004.
- **Gap:** The specification forbids linking an account to a record by similarity, but does not describe the legitimate claim method.
- **Decision:** DR-12.

### CG-27 — Modification of a confirmed relationship and its effect
- **Requirements:** PRV-007, PRV-008, GOV-006.
- **Gap:** The specification forbids direct modification but does not define who decides a correction, how it is applied after approval, or whether it is a history change.
- **Decision:** DR-28, DR-10.

### CG-28 — Disputes without single authority
- **Requirements:** FR-019, PRV-008, GOV-003, GOV-004.
- **Substantive conflict:** The specification forbids any single authority (GOV-003) but requires a dispute mechanism without defining who adjudicates or the decision criterion. One of the most important gaps.
- **Decision:** DR-10, DR-26.

### CG-29 — Polygamy models and half-siblings
- **Requirements:** FR-007, FR-008.
- **Gap:** The model is undefined: is a sibling one who shares both mother and father? Is marriage an independent relationship bound to children? Directly affects the relationship-table design.
- **Decision:** DR-28.

### CG-30 — Modification-history pattern
- **Requirements:** FR-037, PRV-009, OPS-002.
- **Gap:** The specification does not say whether history is kept as an event log or as successive row copies. Affects deletion and correction rights.
- **Decision:** DR-28.

### CG-31 — Audit-record retention policy
- **Requirements:** FR-035, PRV-009, SEC-005.
- **Gap:** The specification demands a balance without a defined duration, and does not define the relationship between the record and the deletion right.
- **Decision:** DR-19.

### CG-32 — Export and deletion rights
- **Requirements:** GOV-005, PRV-006.
- **Gap:** No definition of the right to export data or delete the account, nor of the effect of deletion on records of linked relatives.
- **Decision:** no direct DR in the source; `DECISION-REGISTER.md` proposes DR-33. Tied to DR-19 and DR-20.

### CG-33 — Identity verification beyond OTP
- **Requirements:** FR-001, GOV-003, FR-017.
- **Gap:** OTP proves number ownership, not the person's identity. The specification does not define whether additional verification is required, nor how identity theft is prevented.
- **Decision:** DR-30.

### CG-34 — Abuse and enumeration
- **Requirements:** FR-030, PRV-001, PRV-010.
- **Risk:** Phone search and suggestions may be used to enumerate people or extract links. The specification does not mention request rate limiting.
- **Decision:** DR-05 (partly); needs a standalone security item during phase 0.

### CG-35 — Operational supervision role
- **Requirements:** GOV-003, FR-019, SEC-001.
- **Gap:** Operational administration (deleting abusive accounts, handling reports) needs permissions, but the specification forbids single authority over relationships. Platform administration must be separated from lineage authority.
- **Decision:** DR-26.

### CG-36 — Notifying unregistered people
- **Requirements:** FR-034, FR-004.
- **Gap:** An unregistered person has no account to receive notifications, and the specification does not define whether anything is sent to them outside the platform.
- **Decision:** DR-18.

### CG-37 — Displaying the large network
- **Requirements:** FR-033, PERF-001.
- **Gap:** The specification does not define the node count at which progressive loading starts, nor the display form with many relatives.
- **Decision:** DR-24.

### CG-38 — Deletion and data linked to other relationships
- **Requirements:** FR-002, FR-037, GOV-006.
- **Gap:** When a person linked to documented relationships is deleted, the specification does not define whether relationships are deleted, marked, or ancestors recalculated.
- **Decision:** DR-28 (partly); needs an independent decision at phase 2.

### CG-39 — Validation rules for erroneous data and cycles
- **Requirements:** FR-038.
- **Gap:** The specification mentions cycle prevention without validation rules (for example: a person cannot be their own parent or an ancestor's ancestor).
- **Note:** No DR assigned in the source.

### CG-40 — Conflict between minimum-data and discovery accuracy
- **Requirements:** DATA-001, FR-014.
- **Gap:** If the mother's name is optional, discovery is less accurate; if mandatory, registration is more complex. The specification asks for both.
- **Note:** No DR assigned in the source.

### CG-41 — User annoyance from suggestions
- **Requirements:** FR-014, FR-034.
- **Gap:** The specification does not define limits on suggestion count, notification frequency, or handling of previously rejected suggestions.
- **Note:** No DR assigned in the source.

## D. Conflicts inside the attached planning documents

### CG-42 — File-size limit
- **Source:** The longer task text mentions an approximate 900-line limit, while the newer instructions ask for a reference target of 300–500 lines and 700 as the strict review threshold.
- **Proposed handling:** adopt 700 as the strict threshold because it is the most restrictive; adopted in `standards/CODE-ORGANIZATION-RULES.md`; needs owner confirmation (not a standalone DR).
- **Status:** Open pending owner confirmation.

### CG-43 — Independent reviewer and approval mechanism
- **Source:** The task text requires owner approval before moving on; the newer instructions forbid treating a phase as approved merely because the agent says it is complete.
- **Gap:** Who performs the independent review (human reviewer or another agent) is not defined.
- **Decision:** DR-31.

## E. Requirement dependencies

| Dependency | Requirements | Note |
|---|---|---|
| Record claiming depends on privacy policy | FR-003, SEC-008, PRV-003 | defined before phase 2 |
| Suggestions depend on visibility settings | FR-014, PRV-001 | requires PRV-001 before phase 3 |
| Kinship calculation depends on documented links only | FR-021, FR-020, GOV-009 | requires relationship-state classification (FR-018) before phase 4 |
| Cycle prevention depends on first database | FR-038, TECH-012 | required in phase 2; Closure Table built in phase 4 |
| RLS depends on table design | SEC-004, CG-01 | designed in phase 0 |
| Notifications depend on verification events | FR-034, FR-017 | starts after phase 3 |
| Network display depends on computed data volume | FR-033, PERF-001 | needs phase-4 outputs |
| Encryption affects phone search | SEC-002, PRV-010 | conflicts with direct search; needs DR-05 |

## F. Implementation risks

| ID | Risk | Impact | Likelihood |
|---|---|---|---|
| RISK-001 | Incorrect kinship calculation from path overlap or half-siblings | very high | medium |
| RISK-002 | Phone-number leakage via search | very high | medium |
| RISK-003 | Showing a disputed relationship as fact | high | medium |
| RISK-004 | Closure Table complexity when lineage changes | high | high |
| RISK-005 | Delaying RLS until phase 6 | high | medium |
| RISK-006 | Cultural-rule conflicts between regions | medium | high |
| RISK-007 | Person enumeration via search or suggestions | high | medium |
| RISK-008 | Lineage forgery by multiple users | high | medium |
| RISK-009 | Poor network performance with many nodes | medium | medium |
| RISK-010 | Data loss on deletion and correction | high | low |
---

## M2-R15 Amendment — CG status changes (2026-11-02)

Owner decisions Q1–Q12 (see `DECISIONS.md`) resolve or constrain the following CG entries. Each entry's original text above remains historical.

- **CG-01 — resolved by Q9.** RLS is designed and enabled from the beginning of database design and implementation; application authorization and RLS operate together; tenant/user isolation and unauthorized direct database access are planned and tested; table ownership, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, and application database roles are explicitly examined; no effectiveness claim without executable security tests.
- **CG-02 — resolved at principle level by Q2.** Derived structures (Closure / ancestor helper) are not independent sources of lineage truth; they are reproducible from original relationships and must preserve all path and parent-role information required by M0; a shortest-depth-only Closure Table is not assumed sufficient. The one-table vs two-table physical choice remains database design.
- **CG-08 — resolved by Q10A.** Phone: encrypted at rest with secure managed keys and a separate keyed HMAC for exact lookup; no plaintext searchable copy. The rate-limit value aspect remains open (DR-34 / OPEN-20 `[PROPOSED]`).
- **CG-25 — principle resolved by Q8.** Accountless-record permissions: creator manages permitted basic information; no unrestricted ownership; biological confirmation and changes follow network governance; audit/provenance maintained; no automatic sensitive access. Field-level permission design remains.
- **CG-30 — resolved by Q1.** Current state is authoritative; audit is an immutable append-only history; no full Event Sourcing; full historical state reconstruction is not required.
- **CG-31 — resolved in scope by Q7.** No automatic expiration; ordinary application functions must not delete audit records; access is permission-controlled. Legal-linked deletion and pseudonymization details remain open (DR-19 remainder).
- **CG-43 — resolved by Q11.** Independent review before M3 requires BOTH an independent AI agent that did not prepare the reviewed documentation AND an independent human software engineer; findings compared; material disagreements resolved; owner approves the outcome. The review itself has not yet occurred.
- **CG-27, CG-29, CG-38 — remain open** (correction-loop detail; marriage/polygamy representation; deletion behaviour for linked records). Not decided by Q1–Q12.
- **CG-14 — constrained, not closed.** The closure-storage portion is constrained by Q2; the tenth-degree definition (KD-02 / OPEN-5) remains open.
- **All other CG entries remain unchanged and open, including CG-03, CG-04, CG-05, CG-06, CG-07, CG-09, CG-10, CG-11, CG-12, CG-13, CG-15…CG-24, CG-26, CG-28, CG-32…CG-42.**