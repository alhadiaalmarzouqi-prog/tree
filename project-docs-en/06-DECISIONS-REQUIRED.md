# Decisions Required — Awaiting Owner Approval

**Purpose:** English reconstruction of the pending decision register, preserving every DR identifier, its alternatives, the technical recommendation, and the blocking status.
**Scope:** DR-01 to DR-31.
**Status:** All entries are PROPOSED technical recommendations. No decision in this list has been approved. Owner approval is required before an approved decision can be recorded (in Arabic sources this is stated by `DECISIONS-REQUIRED.md` header and `CLAUDE.md`). **[M2-R15 amendment:** DR-02, DR-03, DR-04, DR-05, DR-11, DR-19 (in part), DR-28, and DR-31 are now decided by the owner (Q1–Q12, 2026-11-02) — see `DECISIONS.md`. The entries below are preserved as historical text and remain descriptive for the parts not decided.]**
**Source references:** `project-docs/analysis/DECISIONS-REQUIRED.md`; clustering in `project-docs/analysis/DECISION-REGISTER.md`.
**Related documents:** `07-DECISION-EVIDENCE-REGISTER.md`, `05-CONFLICTS-AND-GAPS.md`, `15-UNRESOLVED-CONTRADICTIONS.md`.
**Last verified:** 2026-11-01.

## Conventions

- "Blocks execution" field: `Yes` here means the named phase does not start before the decision is resolved (per the source).
- Status tags: `PROPOSED` (not approved), `OPEN` (owner decision required), `CONFLICTED` (contradicts another DR), `DEFERRED` (explicitly deferred).
- The DR-01…DR-31 identifiers are preserved as-is, including DR-32…DR-34 which appear only as proposals in `DECISION-REGISTER.md` (not in `DECISIONS-REQUIRED.md`).

## DR-01 — Client applications: Flutter only, or Flutter with Next.js?

- **Question:** Is a web application built in the first release?
- **Why it matters:** Determines number of client surfaces, reuse, effort, and sharing logic.
- **Alternatives:**
  1. Flutter only; web deferred. Pros: focus on the MVP. Cons: no browser access; later web work may start from scratch.
  2. Flutter mobile with Next.js web from the start. Pros: wider coverage. Cons: two language/UI systems, significant added effort.
  3. Flutter Web instead of Next.js. Pros: one codebase. Cons: weaker performance/SEO, less suited to public content.
- **Technical recommendation:** Option 1 for the first release, with a clearly documented REST interface so that later web work does not require server changes.
- **Blocks execution?** Yes: phase 1 (project structure) and phase 5.
- **Status:** PROPOSED; OPEN.

## DR-02 — Kinship calculation architecture: Closure Table, Recursive CTE, or hybrid?

- **Question:** How are ancestors and kinship stored and calculated?
- **Why it matters:** Affects performance, ease of lineage updates, and error risk.
- **Alternatives:**
  1. Recursive CTE without helper storage. Pros: no duplication or rebuild logic. Cons: slow on large networks.
  2. Full Closure Table. Pros: fast queries. Cons: complex updates on lineage change, large data volume (CG-14).
  3. Hybrid: father/parent relationships are the sole source, a derived Closure Table is rebuilt with isolated logic when a documented relationship changes, with a depth limit of 10 and CTE for verification. Pros: balance of performance and correctness. Cons: dual logic requiring equivalence tests.
- **Technical recommendation:** Option 3. The derived table is updated inside the same transaction, with an equivalence test against the CTE after every change.
- **Blocks execution?** Yes: phase 0 (design), phase 2, phase 4.
- **Status:** PROPOSED, OPEN. **CONFLICTED with DR-28** (see `DECISION-REGISTER.md` section 4 and `15-UNRESOLVED-CONTRADICTIONS.md`).

## DR-03 — Are the Closure Table and the "ancestor helper table" the same thing?

- **Alternatives:**
  1. One table (ancestor, descendant, depth, path side). Pros: single source, no duplication. Cons: extra column for side.
  2. Two separate tables. Pros: faster specific queries. Cons: duplication and desynchronization risk.
- **Technical recommendation:** Option 1, with a column identifying the side (father, mother, mixed).
- **Blocks execution?** Yes: database design.
- **Status:** PROPOSED, OPEN. Linked to DR-02.

## DR-04 — Timing of RLS application

- **Alternatives:**
  1. Phase 1 for sensitive tables, expanded in phase 6. Pros: privacy-from-the-start; reduces RISK-005. Cons: early testing complexity.
  2. Phase 6 per specification. Pros: literal compliance. Cons: writing data without database-level controls in phases 1–5.
- **Technical recommendation:** Option 1.
- **Blocks execution?** Yes: phase 0 and phase 1.
- **Status:** PROPOSED, OPEN.

## DR-05 — Phone-number matching and masking

- **Alternatives:**
  1. Encrypted storage with an HMAC index using a secret key for matching. Pros: numbers cannot be enumerated easily without the key. Cons: sensitive key management.
  2. Keyless SHA-256 hashing. Cons: vulnerable to guessing over the limited phone-number space.
  3. Plain text with direct search. Rejected because it violates SEC-002.
- **Technical recommendation:** Option 1, with rate limiting on phone search, not showing the number to others (PRV-002), and explicit consent for matching (PRV-010).
- **Blocks execution?** Yes: phase 1 and phase 3.
- **Status:** PROPOSED, OPEN.

## DR-06 — Age of majority

- **Alternatives:** 18 years, 21 years, or an age set by the applicable legislation.
- **Technical recommendation:** 18 years as a configurable default, with legal review before launch.
- **Blocks execution?** Yes: phase 1 (date of birth).
- **Status:** PROPOSED, OPEN. Requires legal review (see `07-DECISION-EVIDENCE-REGISTER.md` ME-10).

## DR-07 — Tenth-degree behavior

- **Alternatives:**
  1. Calculate only up to degree 10; beyond is "out of supported scope". Pros: defined performance. Cons: may imply no kinship exists.
  2. Calculate without limit with a warning. Cons: unbounded cost.
- **Technical recommendation:** Option 1, storing full relationships and explicitly stating the calculation stopped at degree 10, not that kinship does not exist.
- **Blocks execution?** Yes: phase 4.
- **Status:** PROPOSED, OPEN.

## DR-08 — Criterion for using Redis

- **Alternatives:** Add it from the start; add it when a specific measured performance problem appears; or never use it.
- **Technical recommendation:** Not added in phase 1; added when a specific measured threshold is exceeded (recorded in `PROJECT-STATUS.md`).
- **Blocks execution?** No.
- **Status:** PROPOSED, OPEN.

## DR-09 — Minimum for adopting a relationship

- **Alternatives:**
  1. Confirmation of both parties for a private relationship, and independent evidence to grow the network.
  2. Confirmation of both parties plus endorsement by an independent third party from documented relationships.
  3. Mandatory document (birth certificate or family document).
- **Technical recommendation:** Option 2 as the minimum for network growth. The document is optional and marked as strong evidence. "Independent" is defined as a person not on the proposed relationship's path.
- **Blocks execution?** Yes: phase 3.
- **Status:** PROPOSED, OPEN.

## DR-10 — Dispute resolution without single authority

- **Question:** Who decides a disputed relationship?
- **Alternatives:**
  1. Freeze the relationship as disputed until parties agree or provide independent evidence. Pros: no one has authority. Cons: may last long.
  2. Vote of independent documented relatives. Pros: collective participation. Cons: can create a manipulable collective authority.
  3. Review by a neutral supervision team with written criteria. Pros: clear closure. Cons: central authority over lineage, conflicting with GOV-003 if extended to lineage rulings.
- **Technical recommendation:** Option 1 as the default. Option 3 is restricted to procedural review (checking evidence and applying rules), never issuing a lineage ruling, and is documented. Voting is not adopted.
- **Blocks execution?** Yes: phase 3.
- **Status:** PROPOSED, OPEN.

## DR-11 — Ownership and modification of an unregistered person's record

- **Alternatives:** Creator only; everyone linked to the record; only users with a documented relationship.
- **Technical recommendation:** The creator enters basic data, any relationship change goes through the verification cycle (FR-017), and display is limited to those with a documented relationship to the record (PRV-003).
- **Blocks execution?** Yes: phase 1 and phase 2.
- **Status:** PROPOSED, OPEN.

## DR-12 — Claiming an existing record

- **Alternatives:** Request and review by relatives; OTP to the phone recorded in the record; supporting document.
- **Technical recommendation:** A claim request with OTP verification and confirmation from at least one documented party, without automatic linking.
- **Blocks execution?** Yes: phase 2.
- **Status:** PROPOSED, OPEN.

## DR-13 — In-law calculation rules

- **Technical recommendation:** An independent in-law table linking each marriage to the spouse's kinship path, displayed as a separate category. Term formulation needs owner review.
- **Blocks execution?** Yes: phase 4.
- **Status:** PROPOSED, OPEN.

## DR-14 — Effect of adoption, breastfeeding, and acquaintance-without-lineage

- **Alternatives:** Include them in the blood-kinship calculation with a separate label; or exclude them from the blood calculation and show them as independent information.
- **Technical recommendation:** Exclude them from the blood-kinship calculation and show them independently ("adopted", "family acquaintance"); breastfeeding is deferred until support is decided.
- **Blocks execution?** Yes: phase 2 and phase 4.
- **Status:** PROPOSED, OPEN. Affects M0 relationship-type exclusions (GOV-011).

## DR-15 — Order of displaying multiple paths

- **Technical recommendation:** Shortest path first; a fixed order on equality; stating that other paths exist and allowing their display on request.
- **Blocks execution?** Yes: phase 4.
- **Status:** PROPOSED, OPEN.

## DR-16 — Dictionary of Arabic and Libyan terms

- **Technical recommendation:** An independent, editable data file reviewed by the owner and speakers from different regions; each term keeps its region.
- **Blocks execution?** Yes: phase 4.
- **Status:** PROPOSED, OPEN. Directly connected to KD-01 (naming system) and the M0 reference limits.

## DR-17 — Name-matching algorithm

- **Technical recommendation:** Arabic text normalization (unifying hamzas, alif-maqsura, ta-marbuta, removing diacritics), then PostgreSQL Full Text with Trigram for similarity; the result is a candidate filter only (GOV-008). The threshold is set by testing and documented.
- **Blocks execution?** Yes: phase 3.
- **Status:** PROPOSED, OPEN.

## DR-18 — Notifying unregistered people

- **Technical recommendation:** No notifications to unregistered people in the first release; they are handled through the user who created the record.
- **Blocks execution?** No.
- **Status:** PROPOSED, OPEN.

## DR-19 — Audit-record retention duration and deletion right

- **Technical recommendation:** A configurable default duration, with personal fields in the record stored pseudonymized so that the key can be destroyed on deletion request, subject to legal review.
- **Blocks execution?** Yes: phase 1 (audit table).
- **Status:** PROPOSED, OPEN. Legal review missing (see `07-DECISION-EVIDENCE-REGISTER.md` ME-10).

## DR-20 — Encryption and key management

- **Technical recommendation:** Sensitive fields (phone number, date of birth, notes, minors' data) encrypted at the application level with AES-256-GCM, key outside the database (environment variable or secrets manager). This is a proposal requiring approval.
- **Blocks execution?** Yes: phase 1.
- **Status:** PROPOSED, OPEN.

## DR-21 — Hosting and data region

- **Technical recommendation:** Provider and region chosen after legal review. No hosting is approved before the data location is known.
- **Blocks execution?** Yes: phase 0 (architecture choice) and phase 7 (deployment).
- **Status:** PROPOSED, OPEN. Legal review missing.

## DR-22 — OTP message provider

- **Technical recommendation:** An approved provider chosen after comparing coverage and cost in Libya, wrapped behind an adapter interface for easy replacement.
- **Blocks execution?** Yes: phase 1.
- **Status:** PROPOSED, OPEN.

## DR-23 — Interface languages

- **Technical recommendation:** Arabic (RTL) only in the MVP, with texts separated into files so later translation is easy.
- **Blocks execution?** No, but it affects phase 5.
- **Status:** PROPOSED, OPEN.

## DR-24 — Performance targets

- **Technical recommendation:** Tentative targets set in phase 0 and measured in phase 7, for example kinship-calculation response under one second for a 10,000-person network. The number is a proposal needing approval.
- **Blocks execution?** No, but it must be set before phase 7.
- **Status:** PROPOSED, OPEN.

## DR-25 — Real-family trial

- **Technical recommendation:** Written consent, limited-scope real data, option to withdraw, and separation of the data from production.
- **Blocks execution?** No, but it blocks phase 7.
- **Status:** PROPOSED, OPEN.

## DR-26 — Operational supervision role

- **Technical recommendation:** A limited supervision role covering only accounts and reports, with no authority over relationships or lineage; every action of the role is recorded.
- **Blocks execution?** Yes: phase 3.
- **Status:** PROPOSED, OPEN.

## DR-27 — Deceased-person status

- **Technical recommendation:** The record is marked as deceased, basic data appears, and privacy is restricted per rules set by the owner.
- **Blocks execution?** No, but it partially blocks phase 2.
- **Status:** PROPOSED, OPEN.

## DR-28 — History pattern and polygamy representation

- **Alternatives:** An append-only event log for relationships with derived current state; or successive row copies.
- **Technical recommendation:** An append-only event log; marriage is an independent relationship linked to both parties; children are linked to the marriage and to both parents.
- **Blocks execution?** Yes: phase 2.
- **Status:** PROPOSED, OPEN. **CONFLICTED with DR-02** regarding which is the primary source (see `DECISION-REGISTER.md` section 4 and `15-UNRESOLVED-CONTRADICTIONS.md`).

## DR-29 — Handling unspecified sex

- **Technical recommendation:** A neutral description when not specified, with a warning to the user.
- **Blocks execution?** No, but it affects phase 4.
- **Status:** PROPOSED, OPEN.

## DR-30 — Identity verification beyond OTP

- **Technical recommendation:** Not required in the MVP, with an account confidence level (not fully identity-verified) shown in the interface.
- **Blocks execution?** No.
- **Status:** PROPOSED, OPEN.

## DR-31 — Independent review before phase approval

- **Technical recommendation:** The owner approves after an independent report by an agent in a separate session, with the reviewer running the tests.
- **Blocks execution?** Yes: blocks transition between phases.
- **Status:** PROPOSED, OPEN.

## Summary

| Status | Decisions | Count |
|---|---|---|
| Blocks execution (Yes) | DR-01, 02, 03, 04, 05, 06, 07, 09, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 26, 28, 31 | 23 |
| Does not block directly | DR-08, 18, 23, 24, 25, 27, 29, 30 | 8 |
| **Total** | | **31** |

**Notes (from source):**
1. Gap CG-13 (weak connectivity/offline) has no standalone decision yet; it is raised as an additional question in `ANALYSIS-REPORT.md`. `DECISION-REGISTER.md` proposes DR-32.
2. DR-02 and DR-03 are linked and must be resolved together.
3. `DECISION-REGISTER.md` also proposes DR-33 (export/deletion rights, from CG-32) and DR-34 (abuse/rate limits, from CG-34). These are proposals only and are not part of `DECISIONS-REQUIRED.md`.
4. None of DR-01…DR-34 is approved. See `07-DECISION-EVIDENCE-REGISTER.md`.
---

## M2-R15 Status Amendment — 2026-11-02

Owner decisions Q1–Q12 (see `DECISIONS.md`) decide the following. The DR text above is preserved unchanged as historical record; the register is authoritative for what was decided.

- **DR-02 — decided (Q1/Q2).** Current-state authority; immutable audit history with who/when/change type/affected information/old+new values in the same transaction; no full Event Sourcing; full historical reconstruction not required; derived structures reproducible from original relationships and preserving all path and parent-role information required by M0; shortest-depth-only Closure Table not assumed sufficient.
- **DR-03 — decided at principle level by Q2;** the physical one-table vs two-table choice remains database design (constrained by Q2).
- **DR-04 — decided (Q9).** RLS from the beginning of database design and implementation (phase 1); app authorization + RLS together; isolation plan/tests; explicit examination of table ownership, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, and application database roles; no effectiveness claim without executable security tests.
- **DR-05 — decided (Q10A).** Encrypted at rest with managed keys + separate keyed HMAC for exact phone lookup/matching; no plaintext searchable copy. Rate-limit values remain open (DR-34 / OPEN-20 `[PROPOSED]`).
- **DR-11 — decided at principle level (Q8).** Accountless-record permissions (creator role limited; no unrestricted ownership; network governance for biological confirmation; audit/provenance; no automatic sensitive access). Field-level permission design and the claim mechanism (DR-12) remain.
- **DR-19 — decided in scope (Q7).** No automatic expiration; application functions must not delete audit records; access permission-controlled. Pseudonymous audit identifier and legal-linked deletion/key-destruction path remain open (legal review).
- **DR-28 — decided (Q1).** Audit is an immutable history, not the source of current state; the old event-log-as-source-of-truth interpretation is superseded. The marriage/polygamy representation portion remains design/deferral per existing documents.
- **DR-31 — decided as a requirement (Q11).** Dual independent review (independent AI agent that did not prepare the reviewed documentation AND independent human software engineer; findings compared; material disagreements resolved; owner approval of the outcome) is required before M3. The review has **not** occurred; the gate is pending.
- OPEN-1 → resolved by Q3; OPEN-3 → resolved by Q5; OPEN-8/DR-19 retention scope → Q7; OPEN-21 → Q8 (principle).
- All other DR-01…DR-31 entries remain pending as written above.