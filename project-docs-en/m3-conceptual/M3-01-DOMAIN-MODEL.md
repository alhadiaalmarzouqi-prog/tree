# M3-01 — Conceptual Domain Model

**Status:** M3 conceptual design draft. **Not owner-approved.** Not a physical schema. No table, column, migration, or code is defined here.
**Language:** English.
**Governing decisions:** `DECISIONS.md` (P1–P17, Q1–Q23, OQ-21-xx, §3C product-scope reset). This document applies them and does not change them.
**Calculation reference:** M0 (`08-MATHEMATICAL-REFERENCE.md`, protected) is unchanged.

---

## 1. Purpose and boundary

The platform is a family discovery and family-connection platform (`DECISIONS.md` §3C.1). This model describes conceptual entities, their ownership, and their boundaries. It is the input to the later M3 documents.

It separates seven concepts (OQ-21-14), listed in §2. Each has its own lifecycle. None is a status value of another.

---

## 2. The seven concepts (OQ-21-14)

| # | Concept | Meaning | Owns |
|---|---|---|---|
| 1 | **Person** | A real or documented individual who may appear in family records. | Identity record; stable Person ID; existence and basic attributes |
| 2 | **Proposal / contribution** | A claim that a relationship exists, submitted by someone. | Submission, its evidence, and its review history |
| 3 | **Account-to-Person association** | The link between a login account and a Person (OQ-21-19). | Who controls which Person, and how that control changed |
| 4 | **Biological relationship** | A parent-child link adopted by a family network as its biological parentage input (OQ-21-16). | The adopted parent role and its history |
| 5 | **Network adoption** | One family network's decision to adopt or not adopt a proposal (OQ-21-01). | Per-network decision and reasons |
| 6 | **Derived kinship** | A result calculated from an adopted graph using M0. | Nothing stored as truth; reproducible result only |
| 7 | **Personal-information visibility** | What each viewer may see of a person's information (OQ-21-03; PRV-011–013). | Per-field and per-group access settings |

**Rule:** the seven concepts are not collapsed into one status field or one lifecycle (OQ-21-14). A screen may display several together; the model keeps them separate.

---

## 3. Core entities (conceptual)

| Entity | Role | Key rule |
|---|---|---|
| **Person** | Concept 1 | Stable Person ID independent of any Account (Q13, D7). May exist without an account, including deceased and accountless persons (Q13, Q22, P8, P15). |
| **Account** | Login identity controlled by a user | Created by registration with OTP. OTP proves phone control only (OQ-21-10). Creating an Account does not create a Person. |
| **AccountPersonLink** | Concept 3 | Association between one Account and one Person over time (§4.3). |
| **FamilyNetwork** | Bounded family group whose members make network-level decisions (§5) | Not a legal entity; no authority over persons outside it. |
| **NetworkMembership** | A Person's participation in a FamilyNetwork | Membership is not parentage. A Person may belong to several networks. |
| **Proposal** | Concept 2 | Submitted claim with contributor, evidence references, and history (§6). |
| **ProposalEvidence** | Evidence attached to a Proposal | Recorded with source and provenance. Supporting only; never a confirmation by itself (Q5). |
| **NetworkDecision** | Concept 5 | One network's decision on one Proposal, with reasons and time (§7). |
| **AdoptedParentage** | Concept 4 within one network | The parent-role fact adopted by one network (§7). |
| **Objection** | Recorded objection to a Proposal or an adopted fact | Recorded and visible; does not automatically change adoption (Q3, G3). |
| **VisibilitySetting** | Concept 7 | Per-field and per-group rules (§9). |
| **AuditEvent** | Append-only change record (§11) | Written in the same transaction as the change it records (P2, P3). |

---

## 4. Person and Account lifecycle (concepts 1 and 3)

### 4.1 Person states (conceptual)
- **Recorded:** the Person exists in at least one network, with or without an account.
- **Associated:** at least one account is linked (§4.3).
- **Deceased:** a death indicator is set. It does not make information public (OQ-21-12).
- **Duplicate-flagged:** a suspected duplicate is flagged. The flag is not a merge (D5, Q13).

Person records are not deleted by ordinary operations. Corrections create new versions and audit events (P2).

### 4.2 Account states (conceptual)
- **Registered:** OTP verified phone control.
- **Active:** the single active account for its associated Person (§4.3 rule 2).
- **Inactive:** retained, not active, not automatically deleted (OQ-21-19 rule 3).
- **Closed by user:** retained for history and audit.

### 4.3 Association rules (OQ-21-19, applied)
1. One Person may be associated with several accounts over time.
2. Only one account may be active for a Person at a time.
3. Old accounts are not automatically deleted.
4. Recovery or transfer of association requires reliable verification beyond OTP (OQ-21-10). The method is open (legal and privacy review).
5. Association, unlinking, recovery, and transfer are audited.
6. Creating an account does not create a Person. A new account starts unassociated until the user creates or links a Person (§4.4).
7. The system prevents two simultaneously active accounts from claiming the same Person.

### 4.4 Linking an account to a Person
- A new account may create a new Person record, or request association with an existing Person.
- Association with an **existing** Person requires additional reliable verification (OQ-21-10, option B). If verification cannot be completed, an alternative review path exists (OQ-21-10).
- The verification method, result, and provenance are recorded (OQ-21-10).

### 4.5 Duplicate suggestions (D5, Q13, FR-048)
- Before creating a Person, the system suggests existing Persons using authorized information only.
- Suggestions never use name similarity alone and never reveal restricted fields (PRV-013).
- Accepting a suggestion is an association request, not an automatic merge.
- Existing suspected duplicates are flagged and reconciled through a controlled verification process with audit (D5). Nothing is merged while identity is uncertain.

---

## 5. Family networks and membership (concepts 1, 2, and 5)

- A **FamilyNetwork** is the unit within which members review and adopt relationships. Its boundary is set by its membership and eligibility rules.
- A Person may belong to several networks. Membership in one network does not grant membership in another.
- Each network's decisions apply only to that network (OQ-21-01). A decision in one network does not bind another.
- Membership is distinct from parentage: a member may have no adopted parents.
- **Open (design item):** the eligibility rules that define which members count as eligible reviewers. These belong to governance design (OQ-21-05) and are not fixed here.

---

## 6. Proposal and review lifecycle (concept 2)

Proposal states (conceptual; not one status column):
- **Submitted**, then **under review** in one or more networks.
- Per network: **accepted**, **rejected**, or **pending** (§7).
- **Disputed:** an active objection exists. Shown as disputed; does not change adoption automatically (Q3, G3).
- **Withdrawn** by the contributor.

Rules:
- A Proposal is the contributor's record. A rejection does not delete it (Q15).
- A rejected proposal may be reopened on new evidence or a material new reason. The original rejection stays visible (OQ-21-18).
- A non-response is neither acceptance nor rejection. An expired response period leaves the item pending or triggers an extension request (G4, Q20).
- Reconsideration requests are screened for seriousness and supporting grounds before reopening (G5).

**Open (design items):** the reopening procedure; response-period lengths (no number is set; OQ-21-05); abuse limits for repeated submission (OQ-21-07 and OQ-21-18).

---

## 7. Network-specific adoption (concepts 4 and 5)

- Each FamilyNetwork holds its own **NetworkDecision** on each Proposal (OQ-21-01).
- A network that accepts records an **AdoptedParentage** in its own adopted graph.
- A network that rejects, or has not reviewed, does not adopt (OQ-21-06).
- Every adopted graph must satisfy the M0 graph constraints (§8.2).
- Adoption is **not** a universal biological fact (OQ-21-16). A network's adoption must never be displayed as a global determination.
- Evidence weight and governance procedure are shown next to each adoption. No network is assumed to have equal evidentiary reliability (OQ-21-16, OQ-21-05).

---

## 8. Kinship calculation and M0 (unchanged)

### 8.1 Fixed rules
M0 §B–§C define the graph, upward paths, path length and count, COMMON, valid junction pairs, J, R, and the a, b, L values. These definitions are not changed by this model. The implementation of M0 is out of scope here.

### 8.2 Per-network application
- Each network's adopted graph is an input to M0 applied separately (OQ-21-02, OQ-21-16).
- Each adopted graph must satisfy M0 §B.1 and the biological integrity constraints: parent-child direction; one adopted `FATHER` and one `MOTHER` per child within a network state; no cycle; absence means unrecorded, not no parent (`09` §4.2, §19).

### 8.3 Why an ancestor table keyed only by shortest depth is not sufficient
M0 requires more than the nearest generation for each ancestor:
- **Path count** (C.3): two paths to the same ancestor can have the same length and still be distinct paths. A shortest-depth table keeps one row per ancestor and loses the count.
- **Valid junction pairs** (C.5): the pair is valid only if the two paths share no vertex other than the ancestor. Whether a pair is valid depends on the full path, not on depth.
- **R** (C.7) counts pairs over all junctions. Each junction may need several paths.
- **Multiple roles:** the role of each edge (`FATHER`/`MOTHER`) is part of the path, and `roles` is required output (fixture convention).

Therefore a design must store or derive enough path information to rebuild the valid pairs and their counts. A shortest-depth table alone cannot do that.

### 8.4 Storage and query alternatives (not selected here)

| Alternative | Supports M0 path and pair requirements | Main risk | Notes |
|---|---|---|---|
| Recursive traversal on the adopted parent graph, no stored closure | Yes; can enumerate all paths and pairs | Cost grows with path count in overlapping pedigrees | Simplest source of truth; reproducible from the graph |
| Stored all-paths closure (every ancestor and every path) | Yes | Size can grow quickly; updates on correction are expensive | Needs a rebuild rule per network |
| Closure with depth only (shortest-depth table) | **No** (§8.3) | Loses counts and pair validity | Not sufficient for M0 |
| Materialized paths per node | Partly; path strings can enumerate lines | Unlimited branching and recalculation on change | Needs a separate valid-pair step |
| Hybrid: canonical graph plus cached derived paths per network, rebuilt in the same transaction as a change | Yes, if the cache stores all paths needed | Cache consistency and rebuild cost | Recommended to evaluate first in M3-02, with an equivalence test against the recursive reference |

**Recommendation (AGENT-PROPOSAL, not approved):** keep the adopted graph as the source of truth, use recursive traversal as the reference, and evaluate a derived cache only if measured query cost requires it. The equivalence test (cache versus reference on all 22 fixtures and generated networks) must pass before any cache is used. This is a technical decision for M3-02.

### 8.5 Presentation rules
- `R` is a count of path pairs, not a count of relationships. It is never displayed as a relationship count (M0 C.7).
- Results are presented as a kinship description with its path, following M0 and FR-026. A truncated search never shows "no kinship" (`08` §F).
- Every result identifies its network and its adopted-input version (AGENT-PROPOSAL, `DECISIONS.md` §3B.5).

---

## 9. Privacy and visibility (concept 7)

Detailed rules, the visibility default, and the open visibility matrix are in `M3-02-PRIVACY-AUDIT-SECURITY.md` §1. This model keeps concept 7 separate from the other six concepts (§2).

## 10. Notes for the next M3 step

- Physical schema, RLS policies, and migrations are not defined here (M3-C only, after review gates).
- The storage choice for the ancestry structure is a technical decision for M3-B, with an equivalence test against the recursive reference (§8.4).






