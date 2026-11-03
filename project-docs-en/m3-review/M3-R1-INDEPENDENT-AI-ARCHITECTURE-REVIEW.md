# M3-R1 — Independent AI Architecture Review (M3 Conceptual Architecture)

**Review identifier:** M3-R1
**Reviewer type:** Independent AI reviewer. This reviewer did not author `M3-01` to `M3-04`.
**Human review:** NOT performed. This report does not satisfy the human software-engineer review required by Q11 / GOV-013. No human engineer has reviewed this design.
**Date:** 2026-11-03 (environment date).
**Scope:** `M3-01`, `M3-02`, `M3-03`, `M3-04`, the approved decision register, M0, and the 22 reference fixtures.
**Project files modified:** none. This report is the only new project file. The protected M0 document, the fixtures, and the M3 documents were not changed.

---

## 1. Executive verdict

**Verdict: NOT APPROVED** (at the conceptual level).

The conceptual architecture gets the foundations right:

- Person and Account are separated (`M3-01` §3, §4.1, §4.3 rule 6).
- The seven concepts of OQ-21-14 are kept separate (`M3-01` §2).
- Biological adoption is per network, not global (`M3-01` §5, §7, §8.2).
- M0 path requirements are analysed correctly: a shortest-depth table is insufficient (`M3-01` §8.3). My independent recalculation of M0 reproduces all 22 fixture outputs (§4 below).
- Audit is append-only and written in the same transaction (`M3-02` §3).
- Default-deny visibility and "no automatic merge" are stated (`M3-02` §1.2, `M3-01` §4.5).

The problems are gaps in the decisions the architecture depends on, not in its direction. Specifically:

- **One CRITICAL finding (C-01) blocks conceptual approval.** The documents do not define what a viewer may learn from a kinship result or shared-relative signal computed over a network the viewer does not belong to. Under default deny, this can expose relationships from a network the viewer is not part of.
- **Ten HIGH findings (H-01 to H-10)** must be resolved before any physical schema is designed. They cover network formation, account-side cardinality, account linking in the MVP, missing accountless-record permissions, concurrency enforcement, the MVP correction path, sensitive audit values, path-enumeration limits, shared-relative discovery in the MVP, and the missing marriage representation.
- **Six MEDIUM and three LOW findings** can be handled during detailed design.

Path to approval: amend the documents to close C-01 and H-01 to H-10, obtain the owner decisions listed in §8, run the Q11 human review, and then re-review. The likely result after that is APPROVED WITH CONDITIONS. Nothing here argues for a different architecture.

---

## 2. Documents and references actually inspected

### 2.1 Read

| Document | Coverage | Notes |
|---|---|---|
| `project-docs-en/m3-conceptual/M3-01-DOMAIN-MODEL.md` | Read in full except §7 tail and §8.1 (lines ~119–134). Those lines were not visible in any read output. | §8.1 content is therefore not assessed. |
| `project-docs-en/m3-conceptual/M3-02-PRIVACY-AUDIT-SECURITY.md` | Read in full (§1–§9). | |
| `project-docs-en/m3-conceptual/M3-03-MVP-SCOPE-AND-OPEN-ITEMS.md` | Read in full. | |
| `project-docs-en/m3-conceptual/M3-04-INDEPENDENT-REVIEW-PACKAGE.md` | Read in full. | |
| `project-docs-en/DECISIONS.md` | Read §§ 3B, 3C, and the Q/P tables. Also searched §4A and the OQ-21 entries. | §4A OQ-21-13 and OQ-21-15 wording not read directly (see §2.3). |
| `project-docs-en/08-MATHEMATICAL-REFERENCE.md` (M0 restatement) | Partially read (lines 40–160). | Protected. Not modified. |
| `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` (M0 source) | Consulted through search snippets (for example §C.13). | Not read in full. |
| `project-docs/reference-fixtures/kinship-reference-cases.json` | Read; structural fields inspected; used as input to the recalculation harness (22 cases). | Protected. Not modified. |
| `project-docs-en/15-UNRESOLVED-CONTRADICTIONS.md` | Read in part (C-R21-01 to C-R21-06, C-R22-01). | |
| `project-docs-en/03-REQUIREMENTS.md`, `09-MASTER-ARCHITECTURE.md`, `06-DECISIONS-REQUIRED.md`, `05-CONFLICTS-AND-GAPS.md`, `04-TRACEABILITY-MATRIX.md` | Consulted through targeted search snippets. | Not read in full. Citations below are to the snippet text. |
| `project-docs-en/verification/phase-a-verification-output.txt` | Search snippet only. | Used for the fixture hash record (§4.4). |

### 2.2 Commands and checks run

| Check | Command or method | Result |
|---|---|---|
| Independent M0 recalculation | `python` on a reviewer-written harness, `%TEMP%\m3r1\m0_recalc.py`, run against `kinship-reference-cases.json` | Reproduced all 22 expected outputs exactly (§4.1). |
| Pedigree-collapse benchmark | `python %TEMP%\m3r1\bench.py` on synthetic collapsed pedigrees | Ran successfully: 63 / 1,023 / 16,383 / 65,535 / 262,143 upward paths for 4 / 8 / 12 / 14 / 16 generations (§4.3). |
| Fixture integrity | Compared against recorded Phase A hash | The Phase A record shows `MATCH` for `kinship-reference-cases.json` (`FF52DF52…07243A46`, 37,807 bytes). My own `Get-FileHash` call returned no output, so I did not recompute the hash. |
| Protected-file edits | None | No project file other than this report was written. |

Some shell commands did not return output because the terminal stalled (a pager and a stuck `Get-FileHash` call). Their results are not used as evidence.

### 2.3 Limitations and unverified items

- **§8.1 of `M3-01` was not read.** Any defect that lives only there is not covered.
- **OQ-21-13 and OQ-21-15 wording in `DECISIONS.md` §4A was not read directly.** M-05 depends on this.
- **The M0 harness is the reviewer's own implementation.** It can share a misreading of M0 with the author. It is a recalculation check, not a formal proof. See §4.1.
- **No recalculation after an adopted change was tested.** The harness only computes a static graph. The M3 equivalence test is not yet built and was not run.
- **Missing evidence vs proven defect.** Where a finding depends on something absent from the documents, I say "not found in the documents I read." I do not claim the content is absent from the whole project.

---

## 3. Review findings by severity

Format per finding: Problem, Practical consequence, Evidence, Recommended correction, Blocks.

Blocking scope key: **CA** = conceptual approval; **PS** = physical schema; **IMP** = implementation; **FEAT** = one feature only.

### 3.1 CRITICAL

**C-01 — Cross-network kinship and shared-relative results are not scoped to the viewer's network boundary.**
- **Document and section:** `M3-01` §5 (networks), §8.5 (presentation); `M3-02` §1.1 (visibility) and §1.2 (default deny); `M3-03` §1.1 (shared relatives row).
- **Problem:** `M3-01` §5 says each network's decisions "apply only to that network", and a Person may belong to several networks. `M3-01` §8.5 says every result identifies its network. No section states what a viewer who is a member of network A may learn when a kinship or shared-relative result is computed on network B's adopted graph. `M3-03` §1.1 lists "Discovering shared relatives" in the first release, described as "A discovery signal, not a confirmed relationship", but does not define the authorization rule for that signal.
- **Practical consequence:** A viewer in network A could infer that two of their relatives share a relative in network B, or learn an adopted relationship from B. That can expose relationships the viewer has no permission to see. OQ-21-03 (`DECISIONS.md` §3C.2) says seeing a relative in another network does not grant access to that network's details. The architecture does not enforce this on the discovery path.
- **Evidence:** `DECISIONS.md` §3C.2 (OQ-21-03, option D). The M2-R22 amendment in `09-MASTER-ARCHITECTURE.md` (around line 420, before its §19 section) says "Q14 makes visibility bilateral and branch-limited ... Eligible-portion rules are OPEN (OQ-21-03)". `M3-02` §1.2 leaves the matrix open. `M3-03` §1.1 still places shared-relative discovery in the first release.
- **Recommended correction:** Before M6 (discovery) is designed, add a conceptual rule: a kinship or shared-relative result is computed only from graphs the viewer is entitled to read, and it names only the viewer-visible portion. Distinguish "hidden by authorization" from "no kinship", so a hidden path is never shown as "no kinship". Record this in `M3-02` §1. It is narrow enough that it need not wait for the full OQ-21-03 matrix.
- **Blocks:** CA (the conceptual privacy model is incomplete for the shared-relative feature) and FEAT (discovery).

### 3.2 HIGH

**H-01 — Network formation, membership, and eligibility are undefined.**
- **Document and section:** `M3-01` §5 ("Open (design item): the eligibility rules ..."); `M3-03` §2 (OQ-21-05, "Governance feature").
- **Problem:** The architecture depends on FamilyNetwork boundaries for adoption, visibility, and calculation. It does not say how a network is created, who may create one, how membership is granted or revoked, or what happens to adopted facts when a Person leaves. Eligibility is deferred to OQ-21-05, which is explicitly open.
- **Practical consequence:** The physical schema for `FamilyNetwork` and `NetworkMembership` cannot be designed. Network boundaries also drive RLS (see M-04).
- **Evidence:** `M3-01` §3 defines `FamilyNetwork` as "Not a legal entity; no authority over persons outside it", but no creation or membership rule appears in §5.
- **Recommended correction:** Add a conceptual section on network lifecycle: creation, membership grant and revocation, and the effect of leaving on adopted facts. A proposed default is that adopted facts remain with the network that adopted them, with a history record. Mark the governance thresholds as OQ-21-05.
- **Blocks:** PS (membership tables and RLS depend on it).

**H-02 — The one-active-account rule is stated only from the Person side; "one account, several Persons" is not covered.**
- **Document and section:** `M3-01` §4.3 rules 1, 2, 7; `M3-02` §7 ("At most one active account per Person ... enforced under concurrency"); `DECISIONS.md` OQ-21-19.
- **Problem:** OQ-21-19 rule 2 is "only one account may be active for a Person at a time". The M3 documents do not say whether one account may be linked to several Persons. `DECISIONS.md` §3B.6 lists this as "Remaining open" (OPEN-4). `M3-01` §4.3 rule 7 says the system prevents two active accounts claiming one Person, with no mechanism given.
- **Practical consequence:** A schema could enforce one side without the other. If an account can link to many Persons with no rule, a user can attach themselves to several unrelated family records, which weakens identity protection. A one-sided check is also easy to race (see H-05).
- **Evidence:** `DECISIONS.md` §3B.6 "Remaining open: whether one Person may have several accounts, one account several Persons". `M3-01` §4.3 contains no rule for the account-to-many-Persons case.
- **Recommended correction:** Record "one account, several Persons" as an explicit owner question, or as a stated default the owner must approve (for example, one active Person per account). Do not infer it. Require a partial unique constraint for active links on the Person side and a matching rule on the account side, tested under concurrency.
- **Blocks:** PS.

**H-03 — Account-to-Person linking can be reached in the MVP without the required verification.**
- **Document and section:** `M3-03` §1.1 ("Suggesting existing Person records"); `M3-01` §4.5 (accepting a suggestion is "an association request"); `M3-02` §4 and OQ-21-10 (`DECISIONS.md` §3C.2).
- **Problem:** Associating an account with an existing Person requires additional verification whose method is not selected (OQ-21-10; DR-30 / OPEN-19). `M3-03` §2 classes OQ-21-10 as C (production). But `M3-01` §4.5 says accepting a suggestion is an association request, and `M3-03` §1.1 includes suggestions in the MVP. Nothing in the MVP table says association is blocked until verification exists.
- **Practical consequence:** The MVP could let a user associate with an existing Person of another family using only OTP, which OQ-21-10 says is insufficient.
- **Evidence:** `DECISIONS.md` §3C.2 OQ-21-10: "OTP verifies control of a phone number, not the real-world identity of a person". `M3-01` §4.5 bullet 3.
- **Recommended correction:** In `M3-03` §1.1, state that an association request to an existing Person is out of MVP scope, or that it goes only to the alternative review path of OQ-21-10.
- **Blocks:** FEAT (account association). Must be fixed before the MVP scope is accepted.

**H-04 — Permissions for accountless records are not specified to schema level.**
- **Document and section:** `M3-01` §3 (Person); `M3-02` §1.3; Q8 and DR-11 (`DECISIONS.md`); FR-047 (`03-REQUIREMENTS.md`).
- **Problem:** Q8 sets principles: the creator manages permitted basic information, creation grants no ownership, and sensitive changes need additional authorization. The M3 documents do not define the creator's permitted fields, what "additional authorization" means, or a permission matrix. `DECISIONS.md` lists "the precise permission matrix and field-level rules" as remaining open.
- **Practical consequence:** The authorization model for the most common record type (an unregistered relative added by someone else) has no defined form. This is where unauthorized edits or false-lineage entries are most likely.
- **Evidence:** `DECISIONS.md` Q8 "Remains open". `M3-02` §1.3 defines no matrix. `M3-03` §1.1 includes "Adding parents, siblings, children, and relatives".
- **Recommended correction:** Add a minimal accountless-record permission table to `M3-02` (creator: basic fields; sensitive fields and all relationship changes: network decision), marked as a design item. It is a required input to the RLS design (see M-03).
- **Blocks:** PS.

**H-05 — Concurrency enforcement is named but not designed.**
- **Document and section:** `M3-02` §7 (one father and one mother, no cycle, one active account, "enforced under concurrency"); `M3-03` §2 (OPEN-16, class D, "Before database build is accepted").
- **Problem:** Four integrity invariants depend on concurrent writes (one father, one mother, no cycle, one active account). The mechanism is deferred to engineering. Cycle prevention is not local to one row: a check over a multi-row graph needs a lock or a serialisation strategy.
- **Practical consequence:** Without a chosen approach (for example, a per-network lock during any change to that network's adopted graph, or a unique constraint on child and role), two concurrent edits can create a cycle or a second father. This is an integrity risk.
- **Evidence:** `09-MASTER-ARCHITECTURE.md` OPEN-16 (`[DEFERRED]` to DB design and concurrency tests). `M3-03` §2 "Open (mechanism)".
- **Recommended correction:** Name at least one candidate enforcement approach, label it a proposal, and make a concurrency test a required artifact of M3-B. Do not treat any invariant as enforced until the test passes.
- **Blocks:** PS and IMP. Not CA, because the invariant itself is stated correctly.

**H-06 — The MVP correction path for adopted parentage is undefined.**
- **Document and section:** `M3-03` §1.2 ("Full correction workflow for confirmed parentage ... may record corrections as new proposals"); `M3-02` §4.
- **Problem:** `M3-03` allows correction "as new proposals" in the first release, but `M3-02` §4 defines a stricter correction workflow (Q17) in which the previous relationship remains intact. Neither section says what the adopted graph shows while a correction is pending, or whether the old parent is replaced when a correction is accepted.
- **Practical consequence:** The at-most-one-father invariant (`M3-02` §7) can be violated or left ambiguous while a correction is pending. Two parent records for one role must not both be adopted.
- **Evidence:** `M3-02` §4 (OQ-21-06: "a network with no completed review does not change automatically"). `15-UNRESOLVED-CONTRADICTIONS.md` C-R21-06: "The effective time of a replacement is not stated in any source."
- **Recommended correction:** State for the MVP that a parentage correction is recorded as a Proposal that does not change the adopted graph until a network decision is recorded, and the previous adopted parent remains until then. Confirm with the owner (OQ-21-06 is recorded as closed in `DECISIONS.md` §4A, but the effective-time wording is still unresolved in C-R21-06).
- **Blocks:** FEAT (correction), and PS if corrections are modelled as writes to the adopted parent column.

**H-07 — Audit values can expose restricted data.**
- **Document and section:** `M3-02` §3 (audit records "the old and new values", Q1); `M3-02` §1.1 (per-field visibility); `M3-02` §3 retention ("indefinite, subject to legal and privacy review").
- **Problem:** Audit records store old and new values. If a field was hidden from a viewer, the audit view may still reveal it. The M3 documents do not say who may read audit values, or whether values are masked in audit history.
- **Practical consequence:** A user who cannot see a relative's phone number could still read it in the audit history of a change. With indefinite retention, that exposure is permanent. The crypto-erase path is open (DR-19 remainder).
- **Evidence:** `M3-02` §3 bullets 2, 4, and 5. `DECISIONS.md` FR-046: "access to audit records is permission-controlled".
- **Recommended correction:** Apply the same field-level visibility to audit reads as to current state, or store sensitive audit values encrypted under a separately controlled key. Limit a viewer's audit access to their own changes plus controlled exceptions. Keep the legal retention question open.
- **Blocks:** PS (the audit table shape depends on whether values are stored encrypted).

**H-08 — Path enumeration has no concrete limit, and its cost is exponential under pedigree collapse.**
- **Document and section:** `M3-02` §8 ("Path enumeration must have explicit limits"); `M3-01` §8.4 (recursive traversal: "Cost grows with path count").
- **Problem:** The architecture requires explicit limits but gives no value or rule for what happens when a limit is reached. The reviewer benchmark (§4.3) shows path count doubling with each generation under full pedigree collapse: 63 paths at 4 generations, 16,383 at 12, 262,143 at 16. Recursive enumeration rose from about 0.0002 s to about 0.60 s on this machine. These are synthetic numbers, not production measurements.
- **Practical consequence:** An unlimited search is a denial-of-service risk. A limited search that silently truncates violates `M3-02` §8 unless the truncation is surfaced in the result.
- **Evidence:** Reviewer benchmark (§4.3). `M3-02` §8 bullets 1–2. `09-MASTER-ARCHITECTURE.md` §11.3, a `[P]` principle: the search limit "is disclosed at truncation".
- **Recommended correction:** Define a result state "truncated" that is distinct from "no kinship", before M7. Define the limit as a configuration value to be measured (DR-24, OPEN-17). Do not assume recursive enumeration meets any latency target without measurement.
- **Blocks:** PS (result shape) and IMP (M7).

**H-09 — The MVP lists "Discovering shared relatives" but its input signal is deferred.**
- **Document and section:** `M3-03` §1.1 ("Discovering shared relatives", basis "FR-014, OQ-21-03"); `M3-03` §2 (OQ-21-13, class E, "Later release"); `M3-02` §8 ("Discovery suggestions use indexed, authorized fields only").
- **Problem:** Shared-relative discovery needs common-ancestor data across people who may sit in different networks. The storage choice (M3-B) is not made. OQ-21-13 (shared-connection signals) is deferred to a later release. So the MVP lists a feature whose required signal is explicitly deferred.
- **Practical consequence:** Either the MVP ships a feature whose inputs are undecided, or it depends silently on a deferred decision. This is an internal MVP contradiction.
- **Evidence:** `M3-03` §1.1 versus §2 (OQ-21-13 class E). `DECISIONS.md` §4A OQ-21-13: "CAN BE DEFERRED TO A LATER PHASE".
- **Recommended correction:** Remove "Discovering shared relatives" from the first-release table, or narrow it to an explicitly authorized, same-network signal and state that cross-network discovery is deferred. This ties directly to C-01.
- **Blocks:** FEAT (shared-relative discovery).

**H-10 — Marriage and in-law representation is absent from the conceptual model, though the requirements depend on it.**
- **Document and section:** `M3-01` §3 (entity table: no marriage entity); `M3-02` §1.2; `03-REQUIREMENTS.md` FR-007, FR-008, FR-009, GOV-012; `05-CONFLICTS-AND-GAPS.md` CG-29.
- **Problem:** The entity table in `M3-01` §3 has no marriage or spouse entity. The in-law and sibling-marriage visibility matrix (OQ-21-03) is open, and `M3-03` §1.2 defers it. The requirements still call for multiple marriages (FR-008, Phase 2) and in-laws as a separate relationship type (FR-009, Phase 4). CG-29 (polygamy models and half-siblings) is open.
- **Practical consequence:** The relationship structure cannot represent in-laws or several marriages without later redesign. Half-sibling determination also depends on the parentage model (FR-007). This is a foundation gap, not a feature gap.
- **Evidence:** `M3-01` §3. `05-CONFLICTS-AND-GAPS.md` CG-29: "Directly affects the relationship-table design". `03-REQUIREMENTS.md` FR-008 and FR-009.
- **Recommended correction:** State in `M3-01` §3 that marriage is outside the first-release conceptual model, and that the relationship design must not preclude a later marriage entity. Record CG-29 / DR-28 as an open item in `M3-03` §2.
- **Blocks:** PS only in the sense that the relationship table must allow a later marriage entity. Not CA.

### 3.3 MEDIUM

**M-01 — "No public access after death" is not reconciled with per-field visibility wording.** `M3-03` §2 (OQ-21-12 "no public access after death") versus `M3-02` §1.1 (default deny plus personal settings). The term "public" is undefined. Default deny already prevents public access, so the two are consistent, but the wording could mislead. *Correction:* define "public" in `M3-02` §1. *Blocks:* FEAT (deceased-person records).

**M-02 — Notification limits can delay a high-risk correction notice.** `15-UNRESOLVED-CONTRADICTIONS.md` C-R21-05 records this as open under OQ-21-07. `M3-02` §5 says important pending requests stay accessible in the review queue, but does not say a correction notice is never delayed. *Correction:* add an explicit exemption as a design item, or state that correction notices are never batched. *Blocks:* FEAT (notifications).

**M-03 — RLS policy design depends on inputs that are not yet written.** `M3-02` §1.3 defers RLS policies to M3-C. Its inputs are the network membership model (H-01), the accountless-record permission table (H-04), and the visibility matrix (OQ-21-03). Those inputs are open, so RLS cannot yet be written. This is a sequencing constraint rather than a defect. *Correction:* list these three as RLS prerequisites in `M3-03` §3. *Blocks:* PS (sequencing only).

**M-04 — Network-boundary enforcement is not connected to RLS.** `M3-02` §1.3 and P12 require application authorization plus RLS, but the documents do not say how a network boundary becomes visible to the database (for example, a network identifier on each adopted row, or a join through membership). Without that, RLS cannot enforce network isolation. *Correction:* state the enforcement mechanism as a design option in `M3-02` §1.3, with a required isolation test (SEC-010). *Blocks:* PS.

**M-05 — OQ-21-13 and OQ-21-15 wording was not verified in full.** `M3-03` §2 and the `DECISIONS.md` §4A table are consistent with each other (both deferred or "must be decided before suggestion behaviour"). I did not read the full §4A entries. *Correction:* the author or the human reviewer should confirm. *Blocks:* none on its own.

**M-06 — Bulk approval and notification rules depend on criteria the documents do not define.** `M3-02` §5 limits bulk approval to "complete, eligible, low-risk items", but eligibility and the risk classification are left to feature design (OQ-21-08). Without a risk classification the rule cannot be tested. *Correction:* define a provisional risk classification in feature design. *Blocks:* FEAT (bulk approval, which `M3-03` §1.2 already defers).

### 3.4 LOW

**L-01 — Terminology.** `M3-01` §2 calls concept 4 "Biological relationship", `M3-01` §3 calls the entity "AdoptedParentage", and the glossary uses "Network-Confirmed Link". Choose one term for the physical schema and record the mapping.

**L-02 — `M3-04` §5 review status is accurate.** It correctly records "Not performed". Consider noting in §5 that this report is an AI review only and does not satisfy the Q11 human review.

**L-03 — Cross-reference for evidence storage.** `M3-03` §2 cites OQ-21-11 for evidence storage. `M3-02` §2 calls the evidence data model "a technical follow-up for M3". Add a cross-reference so an implementer can find the decision.

---

## 4. M0 compatibility assessment

### 4.1 Structural checks versus actual recalculation (distinguished)

- **Structural fixture checks** (performed by the M0 restatement author, `08` Protection notice): the 22 cases were parsed and the expected identifiers and structural fields were checked. This confirms the fixture file is well-formed. It does not prove the mathematics.
- **Actual recalculation** (performed by this reviewer): a Python harness, `C:\Users\test\AppData\Local\Temp\m3r1\m0_recalc.py` (outside the project), was written from the M0 definitions in `08-MATHEMATICAL-REFERENCE.md` and the fixture conventions, then run against `kinship-reference-cases.json`. Re-run for this report: `SUMMARY: 22/22 cases match expected values exactly`. The harness checks the common-ancestor set, the junction set, the path-pair count `R`, and the path count for each case. It does **not** independently check `cousin_degree`, `removal`, `shared_ancestor_lines`, or the role sequences, so those are not verified by this review.
- **Limit of this check:** the harness is the reviewer's own implementation. It shares any misreading of M0 this reviewer may hold. It is independent of the author's architecture but not an independent formal proof. A human engineer should re-derive a sample by hand.

### 4.2 Mandatory M0 capabilities

| Capability | Architecture support | Verdict |
|---|---|---|
| Multiple common ancestors | `M3-01` §8.3 requires per-ancestor data, not one row per ancestor | Supported in design |
| Multiple valid paths | `M3-01` §8.3 "Path count (C.3)"; recursive traversal (§8.4) enumerates all paths | Supported in design |
| Valid junction pairs | `M3-01` §8.3 "Valid junction pairs (C.5) ... depends on the full path" | Supported in design |
| Path-pair counting (`R`) | `M3-01` §8.3 "R (C.7) counts pairs over all junctions"; §8.5 forbids showing `R` as a relationship count | Supported in design |
| Parent roles | `M3-01` §8.3 "Multiple roles"; §8.2 one FATHER and one MOTHER per child | Supported in design |
| Network-specific graphs | `M3-01` §8.2 per-network adopted graph; OQ-21-02 | Supported in design |
| Recalculation after adoption changes | `M3-02` §4 and `M3-01` §8.4 (cache rebuild in same transaction, not yet selected) | Designed as a requirement; no mechanism selected |

### 4.3 Shortest-depth closure: insufficiency is proven, not assumed

The architecture rejects a shortest-depth closure (`M3-01` §8.3). This review confirms that rejection independently:

- Under M0, two distinct paths to one ancestor can share a length. A depth-only row keeps one row and loses the count.
- The reviewer benchmark (`C:\Users\test\AppData\Local\Temp\m3r1\bench.py`, outside the project) built synthetic fully collapsed pedigrees (each generation's two parents shared with the other lineage) and counted upward paths from the leaf:

| Generations | Upward paths (recursive enumeration) | Time on this machine |
|---|---|---|
| 4 | 63 | 0.0002 s |
| 8 | 1,023 | 0.0026 s |
| 12 | 16,383 | 0.0406 s |
| 14 | 65,535 | 0.1450 s |
| 16 | 262,143 | 0.6011 s |

These counts show the path count roughly doubles per generation under full collapse. They also show that any design must either store the paths or enumerate them with a limit (H-08). The shortest-depth table cannot keep the per-path information. The numbers are synthetic and only show scaling.

### 4.4 Fixture and protected-file integrity

- The Phase A verification output (`project-docs-en/verification/phase-a-verification-output.txt`) records `MATCH` for `kinship-reference-cases.json` (SHA-256 `FF52DF522E07ADFC59EB84F78A5B27D007CF636D67228898DFFEA03E07243A46`, 37,807 bytes). This review did not write to the fixture or to M0. My own hash command returned no output, so I rely on the recorded Phase A match, not on a new hash.
- No project file was modified by this review.

### 4.5 M0 verdict

- **M0 is preserved.** The architecture does not change M0's algorithm, formulas, or the 22 fixtures.
- **The reasoning that rejects a shortest-depth closure is correct** (§4.3).
- **The M0 wording gap remains.** `M3-01` and `DECISIONS.md` §3B.3 (C-R22-01) correctly record that M0 §B.1(3) says "biologically confirmed" without saying whether that is per-network or global. This is an owner reading (OQ-21-16), not an architecture defect. The architecture is correct to keep it open.
- **No recalculation after an adopted change was executed.** The incremental-update path (`M3-01` §8.4 hybrid cache) has no equivalence test yet. That test is a required M3-B artifact, not a finding against this design.

---

## 5. Security and privacy assessment

| Area | Assessment | Finding |
|---|---|---|
| Person / Account separation | Sound. Stated in `M3-01` §3 and §4.1, consistent with Q13 and OQ-21-19. | None |
| Account association to a Person | Rules exist (`M3-01` §4.3), but account-side cardinality and the MVP reach are incomplete. | H-02, H-03 |
| Authentication | OTP proves phone control only (OQ-21-10). Correctly stated. | None |
| Application authorization | Mandatory for every read and write (`M3-02` §1.3, P12). | None in the document |
| RLS | Designed to work with application authorization; policies deferred to M3-C. Network-boundary mechanism not stated. | M-03, M-04 |
| Visibility default | Default deny, with per-field settings (`M3-02` §1.1, §1.2). | C-01 (shared-relative path not scoped) |
| Cross-network disclosure | Not defined for discovery or shared-relative results. | C-01 |
| Accountless-record permissions | Principles only (Q8). No permission table. | H-04 |
| Deceased persons | Principle decided (OQ-21-12); "public" undefined. | M-01 |
| Duplicate suggestions | Authorized fields only, no name-only matching (PRV-013, D5). Thresholds deferred (OQ-21-15). | None (design item) |
| Audit | Append-only, same transaction (P2, P3). Old and new values may expose hidden fields. | H-07 |
| Encryption at rest and keyed lookup | Stated (Q10A, DR-05). Key management is OPEN-9, deferred to DR-20 and DR-21. | None in M3 scope |
| Abuse and rate limits | `[PROPOSED]` only (DR-34 / OPEN-20). | Deferred |
| Notification exposure | Batching with an accessible queue (OQ-21-07). Correction-notice exemption open. | M-02 |

**Summary:** the security model is directionally correct. Its weak points are the cross-network disclosure path (C-01), audit value exposure (H-07), and the missing accountless-record permission table (H-04).

---

## 6. MVP practicality assessment

**Verdict:** the first release is feasible in scope, but three items in `M3-03` §1.1 are not ready (shared-relative discovery, association to existing Persons, and correction as a Proposal) and should be narrowed or stated explicitly.

| MVP item (`M3-03` §1.1) | Practical? | Reason |
|---|---|---|
| Registration and login (OTP) | Yes | Well defined. Method limited to phone control. |
| Person profiles | Yes | Stable Person ID, optional fields. |
| Adding parents, siblings, children, relatives | Yes, with H-04 | Needs the accountless permission table first. |
| Suggesting existing Person records | Yes, with C-01 and H-03 | Authorized fields only; must not enable association without verification. |
| Preventing unsafe automatic merges | Yes | Flags only. |
| Family connection requests | Yes, with H-01 | Needs network membership rules. |
| Viewing confirmed family connections | Yes | Shown per network. |
| Discovering shared relatives | **No, as written** | Depends on deferred OQ-21-13 and unresolved C-01 (H-09). |
| Understanding kinship relationships | Yes, with H-08 | M0 unchanged. Needs a truncation result state. |
| Basic privacy settings | Yes | Per-field; default deny for matrix cases. |
| Notifications and review queue | Yes, with M-02 | Correction exemption needed. |
| Basic audit visibility | Yes, with H-07 | Audit reads must follow visibility. |

The first release reasonably defers the full correction workflow, reopening, specialist participation, evidence attachments, breastfeeding, adoption, the visibility matrix, and bulk approval (`M3-03` §1.2). These deferrals are safe, subject to H-06 for corrections.

---

## 7. Contradictions and missing decisions

| ID | Contradiction or gap | Where | Status |
|---|---|---|---|
| X-1 | Shared-relative discovery is in the MVP, but its signal is deferred. | `M3-03` §1.1 vs §2 (OQ-21-13) | H-09 |
| X-2 | Network eligibility is needed for everything, but is deferred. | `M3-01` §5 vs OQ-21-05 | H-01 |
| X-3 | "One account, several Persons" is open, but one-active-account is treated as settled. | `DECISIONS.md` §3B.6 (OPEN-4) vs OQ-21-19 rule 2 | H-02 |
| X-4 | Correction is "a new proposal" in the MVP, but must keep the previous relationship intact and at most one parent. | `M3-03` §1.2 vs `M3-02` §4 and §7 | H-06 |
| X-5 | M0 §B.1(3) "biologically confirmed" can be read as per-network or global. | `DECISIONS.md` §3B.3 (C-R22-01), OQ-21-16 | Owner decision open. Not a defect in this design. |
| X-6 | "Network-confirmed" and "adopted" are used for the same concept. | `02-GLOSSARY.md` vs `M3-01` §2 | L-01 |
| X-7 | Marriage and in-law representation is required by FR-008 and FR-009 but absent from the entity model. | `M3-01` §3 vs `03-REQUIREMENTS.md` | H-10 |
| X-8 | `M3-04` §5 review status is accurate. This AI review does not satisfy Q11. | `M3-04` §5 | Human review still required |

**Missing owner decisions (not inferred here):** OQ-21-05 (governance thresholds and eligibility); the OQ-21-06 effective-time wording (C-R21-06); OQ-21-10 (verification method); OQ-21-16 (M0 reading); OQ-21-03 (visibility matrix); "one account, several Persons" (OPEN-4); CG-29 (polygamy and half-siblings); and DR-30 / OPEN-19 (extra identity verification).

---

## 8. Required corrections before physical database design

These must be completed before `M3-C` (physical schema) is approved:

1. **C-01:** add the viewer-scoped rule for kinship and shared-relative results to `M3-02` §1.
2. **H-01:** add a network lifecycle and membership section to `M3-01` §5.
3. **H-02:** record "one account, several Persons" as an owner question or a stated default; require the active-link constraint on both sides.
4. **H-03:** state in `M3-03` §1.1 that association to an existing Person is outside the MVP or limited to the review path.
5. **H-04:** add the minimal accountless-record permission table to `M3-02`.
6. **H-05:** name a candidate concurrency-enforcement approach and make its test a required artifact.
7. **H-06:** state the MVP correction rule (previous adopted parent remains until a network decision).
8. **H-07:** state who may read audit values and how hidden values are handled.
9. **H-08:** define the "truncated" result state and make the limit a configuration value.
10. **H-09:** remove or narrow shared-relative discovery in `M3-03` §1.1.
11. **H-10:** state the marriage boundary in `M3-01` §3 and record CG-29 as open.
12. **M-03 and M-04:** list the RLS prerequisites and the network-boundary mechanism.

Each correction must be recorded as an amendment note in the relevant M3 document, not as a silent edit. Protected files (M0, fixtures, Arabic sources) must not change.

---

## 9. Issues safely deferrable to later phases

These do not block the conceptual design or the physical schema, provided the design leaves room for them:

- **Full correction workflow for confirmed parentage** (beyond the MVP rule in H-06). Deferrable, as `M3-03` §1.2 states.
- **Full reopening workflow.** Deferrable, but the reopen state must be recorded now (OQ-21-18 decided).
- **Specialist and elder participation** (OQ-21-05). Deferrable.
- **Historical or alternative lineage narratives** (OQ-21-17). Deferrable; a separate layer (OQ-21-14).
- **Evidence attachments** beyond source notes (OQ-21-11). Deferrable; source and contributor fields are enough initially.
- **Breastfeeding display category** (P10) and **adoption** (P9). Deferrable.
- **Advanced visibility matrix** for in-laws and sibling marriages (OQ-21-03). Deferrable, provided the default-deny rule (`M3-02` §1.2) is enforced first.
- **Advanced bulk approval** (OQ-21-08). Deferrable.
- **Numerical limits** for notifications, thresholds, and rate limits (OQ-21-07, OQ-21-15, DR-34 / OPEN-20). Deferrable to measurement or governance design.
- **Shared-connection signals** (OQ-21-13). Deferrable, which is why H-09 should narrow the MVP.
- **Performance targets** (DR-24, OPEN-17). Deferrable to M7 measurement, but the truncation state (H-08) is not deferrable.
- **Web client** (DR-01). Deferrable.

Not deferrable despite their later schedule: the truncation state (H-08), the accountless-record permissions (H-04), the network membership model (H-01), and the one-active-account constraint (H-02). Each is needed before physical design.

---

## 10. Final readiness verdict

**VERDICT: NOT APPROVED** (conceptual architecture, as of this review)

Reasons:
1. One CRITICAL finding (C-01) is unresolved: the viewer-scoped disclosure rule for kinship and shared-relative results.
2. Ten HIGH findings (H-01 to H-10) must be resolved before physical schema design. Several are owner decisions, not only technical ones.
3. The human software-engineer review required by Q11 / GOV-013 has not been performed. The AI review in this report does not satisfy that requirement.

What is sound and should be kept: the Person and Account separation, the seven-concept model, per-network adoption, the M0 path-count reasoning and its rejection of a shortest-depth table, default-deny visibility, and append-only audit. These are correct as written.

**Path to APPROVED WITH CONDITIONS:** complete the §8 corrections, obtain the owner decisions in §7, record each correction as an amendment note, run the Q11 independent human review, and re-submit for review. The most likely outcome after those steps is APPROVED WITH CONDITIONS, with conditions taken from the open items in `M3-03` §2.

**Scope of this verdict:** conceptual approval only. It does not authorise physical schema, migrations, or application code (`M3-03` §3 gates).
