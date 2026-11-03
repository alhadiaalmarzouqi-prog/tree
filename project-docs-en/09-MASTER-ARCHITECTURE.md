# Master Architecture — Sovereign Lineage Platform

**Purpose:** English reconstruction of the master architecture document.
**Scope:** Sections 1–16 of the Arabic source, including the open items, invariants, prohibitions, and the M3–M8 roadmap.
**Status:** Draft — reconstruction for review. **Not owner-approved.** This document becomes authoritative only after the owner approves it and the source documents are updated by separate order.
**Source references:** `project-docs/MASTER-ARCHITECTURE.md` (70 ownership labels occur there); also `03-REQUIREMENTS.md`, `06-DECISIONS-REQUIRED.md`, `08-MATHEMATICAL-REFERENCE.md`, `01-MISSING-EVIDENCE.md`.
**Related documents:** all English documents in this set; the Arabic sources remain the authority.
**Last verified:** 2026-11-01.

## 0. Status tags used in this document

| Tag | Meaning |
|---|---|
| `[V: <file>]` | Statement directly supported by that source file |
| `[OA-claimed: M1-E]` | Source labels the statement OWNER-APPROVED, citing M1-E; the M1-E report is missing, so this is a claim, not verified approval |
| `[P]` | Technical proposal; not a decision |
| `[OPEN]` | Owner decision required |
| `[CONFLICT]` | Sources contradict each other |
| `[MISSING]` | Required evidence not available |
| `[DEFERRED]` | Explicitly deferred to a later design/implementation phase |

Rule (from the source): any paragraph without an explicit tag is descriptive, not binding.

## 1. Vision, scope, and exclusions

### 1.1 Vision
A digital kinship-network platform that connects family members into an interlinked network built by the individuals themselves, not by one person entering a whole tree. The user should be able to know their relatives and how they relate to any other registered person, within the limits of privacy and documented information. `[V: REQUIREMENTS.md FR-021, FR-028]`

### 1.2 Scope (MVP)
- Mobile application (Flutter, per TECH-004) as the only client in the first release. DR-01 is not decided; Flutter as the only client is an unapproved proposal. `[P]` `[OPEN]`
- A single backend server (NestJS) and a single database (PostgreSQL) as the single source of truth in the first phase. `[V: REQUIREMENTS.md TECH-001, TECH-002, TECH-003]`
- Phone registration with OTP; creation of person records separate from accounts; biological father/mother links; network-confirmation cycle; internal kinship engine; audit record; notifications. `[V: REQUIREMENTS.md FR-001…FR-004, FR-006, FR-017…FR-021, FR-034, FR-035]`

### 1.3 Exclusions (outside the current scope)
- **Adoption:** outside current scope. `[OA-claimed: M1-E item 9]` No table or relationship is designed for it in the current release. `[V: REQUIREMENTS.md FR-010]` — the requirement requests it and the conflict is documented in section 16.2.
- **Breastfeeding (milk kinship) as a separate displayed category:** `[OA-claimed: M1-E item 10]`. Deferral of detailed implementation is `[P]` (the owner decision said implementation "may be deferred" until display requirements are defined). The architecture does not prevent adding it later. `[DEFERRED]` after approval of this deferral.
- **Web (Next.js) and broad admin dashboards:** `[DEFERRED]` with DR-01 and TECH-005.
- **Offline mode (CG-13):** `[DEFERRED]`.
- **Features deferred in the specification:** solidarity funds, full conversations, calls, maps, financial voting, advanced tribes. `[V: REQUIREMENTS.md SCOPE-001, SCOPE-002]`
- **Full event sourcing:** not required. `[OA-claimed: M1-E item 4]`
- **Neo4j:** not used initially. `[V: REQUIREMENTS.md TECH-011]`

### 1.4 Non-goals
- The platform is not a court for family disputes and does not impose acceptance or rejection on anyone. `[OA-claimed: M1-E item 7]`. Note: DR-10 in `DECISIONS-REQUIRED.md` has not been amended; its wording remains as originally written, with the proposed formulation `[P]`.
- The platform does not provide scientific (DNA) or legal proof of lineage; network confirmation is social information, not proof. `[P]` (consistent with the adopted "no ruling" principle; not an independent adopted item).
- The platform gives no lineage authority to any family head or supervisor. `[V: REQUIREMENTS.md GOV-003]`

## 2. Context and layers

### 2.1 Context
- **Users:** people registered with a phone account; and people present in the network without an account (unregistered). `[V: REQUIREMENTS.md FR-003, FR-004]`
- **External parties:** an OTP message provider (`[DEFERRED]` to DR-22) and a mobile notification service (FCM). `[V: REQUIREMENTS.md TECH-008]`
- **Operator:** the owner and operations team with limited administrative permissions. `[OPEN]` (DR-26; see section 9).

### 2.2 Main layers
| Layer | Responsibility | Boundaries |
|---|---|---|
| Mobile application (Flutter) | UI; display network, paths, states | does not calculate kinship, does not decide permissions, does not store sensitive data as a source of truth |
| API layer | request authentication, user identity, routing | application-level access authorization is mandatory; never trust the client |
| Business-logic layer | confirmation cycle, link-state management, structural validation, audit record | the place for documented business rules; independent of the client |
| Kinship engine | computes paths, common ancestors, junction points per M0 | reads only confirmed biological links; never writes |
| Data-access layer | queries, transactions, RLS application | atomic transactions for state and audit |
| Database (PostgreSQL) | single source of truth, structural constraints, RLS policies | `[V: REQUIREMENTS.md TECH-003]` |
| Notification service (FCM) | alerts for confirmation requests and updates | no sensitive information inside the notification |
| Key management | encryption, HMAC, audit keys | storage and retrieval location `[OPEN]` (DR-21, DR-20) |

Note: internal component modularization follows `12-STANDARDS.md` (from `CODE-ORGANIZATION-RULES.md`) and is not defined here.

### 2.3 Binding structural boundaries
- **Business logic separated from the client:** permission decisions and kinship calculation are not moved to the application. `[P]` (consistent with DR-01, not yet decided). Source note: the rule that RLS does not replace application authorization is `[OA-claimed: M1-E item 12]`.
- **Kinship is calculated from the source of truth only:** not from suggestions or pending states. `[V: REQUIREMENTS.md FR-020]`
- **No lineage decision outside the network:** no administrative layer decides lineage. `[V: REQUIREMENTS.md GOV-003]`

## 3. Account–person separation

### 3.1 Principle
The user account and the person record are separate entities. The account is a login credential; the person is a node in the kinship network. `[V: REQUIREMENTS.md FR-003]`

### 3.2 Unregistered people
- A person may have a record without an account, created by a relative as a limited-permission family record. `[V: REQUIREMENTS.md FR-004, FR-005]`
- An unregistered person appears in the network to anyone with a documented link to them, by name, relationship, and path. `[OA-claimed: M1-E item 11]`
- Sensitive information of the unregistered person (phone, exact date of birth, notes) is protected and not shown merely because of kinship. `[OA-claimed: M1-E]`

### 3.3 Linking an account to a person
- No account is linked to a person record by name or data similarity. `[V: REQUIREMENTS.md SEC-008, GOV-001]`
- Claiming an existing record (proving that a record belongs to the account holder) is an independent procedure with its own cycle. `[OPEN]` (full claim mechanism `[DEFERRED]` to identity design).

### 3.4 Duplicate identity
- **`[OPEN]`:** how do multiple accounts belonging to one person get identified and handled? The architecture makes no assumption. The only permitted architectural phrasing is: "A person is identified by an internal person identifier, and multiple accounts are not counted more than once." That phrasing is `[P]`, a description, not a solution.

## 4. Biological-link model

### 4.1 Principle
A biological parental relationship is a directed link from child to parent carrying the **parent role** `FATHER` or `MOTHER`. `[V: REQUIREMENTS.md FR-006]`; role naming per M0 §B.1. The parent role is required to distinguish full from half siblings. `[V: REQUIREMENTS.md FR-007]`

### 4.2 Safety invariants
1. **At most one confirmed biological father and at most one confirmed biological mother per child.** `[OA-claimed: M1-E item 14]`
2. **An unknown father stays absent; no fabricated record is created.** `[OA-claimed: M1-E item 15]`
3. **No cycle exists in the confirmed biological link set.** `[OA-claimed: M1-E item 16]`. Fixed architectural wording:
   > "No committed set of confirmed biological links contains a cycle."
   - The invariant is enforced **when a link transitions to network-confirmed**; no committed set is written that violates it, including under concurrent writes. `[P]` (wording), `[OA-claimed]` (existence of the invariant).
   - Enforcement mechanism `[DEFERRED]` to database design and concurrency testing. No lock type, Serializable, or trigger is chosen here.
   - Documenting the invariant does not prove it is implemented; it is done only when a concurrency test actually runs.
4. **Overlap is not a cycle.** Two paths to one ancestor through related parents are structurally valid. `[V: M0 §B.1(6)]`

### 4.3 Link state
Every parenting link carries a state that determines whether it enters the biological calculation. Not-confirmed links do not enter. `[V: REQUIREMENTS.md FR-020]`
- **Effect of an objection on a network-confirmed link:** `[OPEN]` — the architecture does not state that a confirmed link with an active objection automatically enters or leaves the calculation; the owner has not decided.

### 4.4 Absence
- An unrecorded parent means unrecorded or unknown lineage, not that the person has no parent. (Implied by M0 §B.1(4); unknown-father rule `[OA-claimed]`.)
- A person whose mother is known and father unknown is linked to the mother only and connects to relatives through the mother's side. `[OA-claimed: M1-E item 15]`

## 4A. Non-biological relationships (breastfeeding, marriage/in-laws, adoption, guardianship)

- **Breastfeeding** is a separate relationship category with clearly distinct visual marking and explicit "breastfeeding" labeling; milk-mother and milk-father are not biological parents, do not enter the biological calculation, and are not treated as a genetic or inheritance relation. `[OA-claimed: M1-E item 10]` Implementation details (screens, navigation, display rules) `[DEFERRED]`. The architecture does not prevent adding it later. Related DR: DR-14 (open).
- **Marriage/in-laws** is a separate in-law relationship; it is not stored as a parenting link and does not enter the biological calculation. `[V: REQUIREMENTS.md FR-009, GOV-011, GOV-012]` Multiple marriages for one person are a specification requirement (FR-008). Representation and child/marriage binding `[DEFERRED]` to database design (DR-28; CG-29). An independent in-law table and description rules `[DEFERRED]` to the in-law phase (DR-13, CG-17). This document does not model a full marriage model.
- **Adoption and guardianship:** adoption is outside current scope; no table or relationship is designed for it. `[OA-claimed: M1-E item 9]` The original requirement FR-010 requests it; documentation conflict awaits specification amendment. `[OPEN]` Guardianship bestows no lineage and does not enter the biological calculation. `[P]` Legal review and any related permissions `[OPEN]` (OPEN-14). No detailed guardianship requirement exists in the specification.
- **Mandatory distinction:** marriage, breastfeeding, adoption, and guardianship are not biological parenting links and are not stored as rows in the biological-links table. `[P]` (consistent with GOV-011 and M0 §B.2).

## 5. Link lifecycle and network confirmation

### 5.1 Conceptual states
The following states are conceptual, not tables. FR-018's wording in the specification has not been amended, so these states remain `[P]`, while the principle that the current state is the calculation source is `[OA-claimed]`.

| State | Meaning | Enters biological calculation? |
|---|---|---|
| Proposed | link submitted, not yet presented to the network | No |
| Awaiting network confirmation | presented to the eligible circle | No |
| Network-confirmed | gained confirmation per the adopted majority rule in the widened circle | see OPEN-1 (effect of active objection) |
| Rejected | completed network result against the link; resubmission `[OPEN]` (OPEN-2) | No |
| Disputed | an active objection on a confirmed link, or an unresolved conflict | `[OPEN]` (OPEN-1) |
| Unresolved | no decisive result after exhaustion of available eligible members | No |
| Corrected/replaced | replaced by another link after correction | No (previous state kept in audit) |
| Cancelled/withdrawn | cancelled without replacement | No |

Note: "rejected" and "unresolved" are not merged: the first is a completed network decision, the second is a shortfall in eligible participation. `[P]` (the cited M1-E §2.E wording is unverifiable).

### 5.2 Transitions
Conceptual transitions (to be implemented later in business logic):
- Proposed → Awaiting network confirmation.
- Awaiting network confirmation → Network-confirmed, or Rejected, or Unresolved, or Disputed.
- Network-confirmed → Disputed (on an active objection; effect on calculation `[OPEN]`), or Corrected, or Cancelled.
- Disputed → Network-confirmed, or Rejected, or Unresolved.
- Unresolved → Awaiting network confirmation (when eligible members become available), or Rejected, or Confirmed.
- Rejected → Awaiting network confirmation: **not approved.** `[OPEN]` (OPEN-2). This document assumes neither that resubmission is possible nor that new evidence is mandatory or sufficient.
- Every transition is recorded in the audit record. `[OA-claimed]` (principle per FR-035 and GOV-006).

### 5.3 Network confirmation (principle)
- **Model:** confirmation by majority of the eligible circle. `[OA-claimed: M1-E items 5 and 6]`. **M2-R22 note:** this describes one network's decision. Per OQ-21-01 (owner-approved), each network holds its own acceptance state, so this majority applies within a network and does not decide other networks. The canonical-input rule is OPEN (OQ-21-16).
- **Parties:** participate as members, without individual veto or special weight. `[OA-claimed]`
- **Deceased:** a distinctly marked visible node; does not vote; no proxy. `[OA-claimed]`
- **Objection:** recorded and assessed through the network; it does not automatically reject the link. `[OA-claimed: M1-E item 7]`
- **Growth:** continues as long as eligible members exist, without a fixed numeric cap. `[OA-claimed, cited to M1-B §3 — unverifiable]`
- **No outcome:** the link stays "unresolved" and is not described as rejected or confirmed. `[OA-claimed]`
- **Eligibility (proposal, not an approved rule):** an eligible member has an independent confirmed relationship with one of the link's parties, and the link itself is not counted in that relationship. `[P]`; final eligibility conditions `[OPEN]`.
- **Parties, deceased, and numeric details** (denominator, quorum, majority) are not defined here. `[DEFERRED]`

### 5.4 Open issues in the lifecycle
- **`[OPEN]`:** does an active objection immediately suspend a confirmed link from the biological calculation? (M1-E §3.1 — unverifiable.) The two options (immediate suspension vs. remaining until a new network decision) affect kinship calculation and are unsettled. The architecture does not choose.
- **`[OPEN]`:** can a rejected link be resubmitted with new evidence? (M1-E §3.2 — unverifiable.) `[P]`: resubmission requires new information; prior history is kept.

### 5.5 Objections and abuse reduction (no automatic ruling)
All of the following are `[P]`; none decides automatic rejection:
- Recording an objection's reason is mandatory.
- One active objection per person per link (prevents duplicates; does not decide).
- A cooling-off period between repeated objections by the same person; no fixed number is set in this document.
- No special weight is given to an objector. `[P]` (consistent with the adopted "no individual veto" principle).

### 5.6 Independent evidence
- **`[OPEN]` (OPEN-3):** what does "supported by independent evidence" in FR-018 mean? Open questions: (a) is it a link-state? (b) is it supporting information bound to the link? (c) what is its relation to network confirmation? This document chooses no answer.
- **What may be represented without deciding:** evidence and provenance as data bound to the link, without assuming that it changes state or replaces network confirmation. `[P]`
- **FR-018's original wording stays as written in the specification** and is not removed or redefined here. `[V: REQUIREMENTS.md FR-018]`

## 6. Biological kinship engine

### 6.1 Reference
The engine applies the M0 mathematical reference unchanged: `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` and the 22 fixtures in `project-docs/reference-fixtures/kinship-reference-cases.json`. `[OA-claimed: M1-E item 17]` The reference is protected; this documentation set does not modify it.

### 6.2 Inputs
- **Only network-confirmed biological links**, after excluding the categories listed in section 4A and 5.1.
- Not entered: adoption (out of scope), breastfeeding, marriage/in-laws, guardianship, and disputed, unresolved, rejected, proposed, awaiting-confirmation, corrected, or cancelled links. `[OA-claimed]` (built on FR-020 and GOV-011).

### 6.3 Internal outputs
- Upward paths, common ancestors (COMMON), valid junction points (J), valid path-pair count (R), (a,b), combined length L, and structural classification — all as in M0.
- **`R` is a count of path pairs, not of human relationships.** `[V: M0 §C.7]`

### 6.4 What is displayed to the user
- **Arabic kinship naming:** `[OPEN]` (KD-01, DR-16). The engine does not generate it.
- **Meaning of "tenth degree":** `[OPEN]` (KD-02). This document sets no definition.
- **Path display order and grouping:** `[OPEN]` (DR-15, KE-04, KE-05). Adopted principle: every path is displayed independently and no important path is hidden behind a primary link. `[OA-claimed]` (recorded from an owner message; M1-E unverifiable; no identifier in project files).

### 6.5 Search limits and truncation
- A configurable technical search limit, separate from any degree definition. `[P]`
- **"No kinship" is not displayed if the search stopped due to the limit**; the display states that the check did not complete within the limit. `[P]` (consistent with M0 §F.3).
- **Limit values are not measured.** No numbers are set here.

### 6.6 Mathematical boundaries
- The reference verifies the displayed cases but does not prove the definition covers every tree. `[V: M0 §F.1]`
- Full path enumeration suits only small cases; it is not a production solution. `[V: M0 §F.2]`

## 7. Privacy, authorization, and minor protection

### 7.1 Binding principles
1. **Kinship alone does not grant access to sensitive information.** `[OA-claimed: M1-E item 11]`
2. **No unrestricted parental access automatically.** `[OA-claimed: M1-E item 11]`
3. **Sensitive fields are protected by default:** phone, exact date of birth, private notes, sensitive minor data. `[OA-claimed: M1-E item 11]` (the sensitive-fields detail was not approved as a specific list).
4. **A person's existence, lineage, and path are visible to qualified persons**, adult or minor. `[OA-claimed: M1-E item 11]`
5. **Visible vs. sensitive are separated:** seeing existence does not mean seeing fields. `[P]` (detailed later in permission design).

### 7.2 Access tiers
| Tier | Content | Rule |
|---|---|---|
| Existence, link, and path | name, kinship relation, path | shown to qualified network members `[OA-claimed]` |
| Basics | name, sex, city | per record owner's setting `[P]` |
| Sensitive | phone, exact date of birth, notes, sensitive minor data | protected by default; not granted by record ownership or kinship alone; explicit grant rules and limits `[OPEN]` (see 7.3) |

### 7.3 Minors
- A child appears as a node in the network to those with a confirmed link, with lineage and path displayed. `[OA-claimed]`
- A parent does not get unrestricted access to the child's sensitive fields. `[OA-claimed]`
- **`[OPEN]` (OPEN-11, OPEN-14):** definition of child/adult (DR-06, PRV-005); whether any path exists to grant a sensitive field of a child, and who grants it, and under which conditions. This document does not assume that a father, mother, or record owner holds this permission.
- **No one gets access to a child's sensitive fields merely for being a parent.** `[OA-claimed: M1-E item 11: no unrestricted parental access automatically]`
- **Constraining the "record manager" as father/mother:** `[P]`. The adopted source does not mention the record manager explicitly, and this constraint is not part of the adopted principle.
- **No guardianship model at this stage.** `[P]`, because legal guardianship requires legal review that has not been done.

### 7.4 Authorization and RLS
- **Application authorization is mandatory** on every request and identifies user identity and permissions. `[V: REQUIREMENTS.md SEC-001]`; `[OA-claimed: M1-E item 12]`
- **RLS is an extra layer**, not a replacement for application authorization. `[OA-claimed]` (principle; M1-E item 12)
- **RLS timing:** `[OPEN]` in the original text below. **Superseded by Q9 (`DECISIONS.md` §3, owner-approved):** RLS is designed and enabled from the beginning of database design. This statement is historical and is kept for traceability. See §17 (M2-R22).
- **Both layers must work consistently:** if application authorization rejects access, RLS must not grant it, and vice versa. `[P]`
- **RLS policy details, DB connection role, and `FORCE ROW LEVEL SECURITY`:** `[DEFERRED]` to database design.

### 7.5 Direction on conflict
- If application authorization conflicts with RLS, the safer rule is to narrow access, not widen it. `[P]`
- Any access not justified by an explicit grant is denied by default. `[P]`

## 8. Current state, audit trail, and data integrity

### 8.1 Source of truth
- **Current confirmed biological links are the current source of truth for biological calculation.** `[OA-claimed: M1-E item 1]`
- **An append-only, non-modifiable, non-deletable audit record** logs every link change: add, correct, cancel, reject, merge. `[OA-claimed: M1-E item 2]`; `[V: REQUIREMENTS.md FR-035, GOV-006]`
- **No full event sourcing.** `[OA-claimed: M1-E item 4]`
- **The DR-02/DR-28 record.** The conflict between DR-02 (current confirmed biological links as the sole source) and DR-28 (append-only event log as the basis) is **not resolved in the project**:
  - The architecture's source (§8.1) states that current state is the source and the audit is historical, citing OWNER-APPROVED; that label is **unverifiable** (M1-E missing), and the same source says the proposed rewording of DR-28 awaits editing in the source file.
  - `DECISION-REGISTER.md` §4 states DR-02 and DR-28 conflict and **cannot both be adopted as written**; its proposed resolution is itself `[P]` and needs explicit owner approval.
  - This document records the distinction between (a) current authoritative relationship state, (b) immutable historical audit records, and (c) derived ancestor/descendant structures, **without claiming the technical conflict is resolved**.

### 8.2 Consistency
- **Current state and audit record are updated in the same transaction.** If one fails, the whole transaction fails. `[OA-claimed: M1-E item 3]`
- **Derived structures (if any, e.g., ancestor indexes) are updated in the same transaction or rebuilt from confirmed links.** `[P]` (consistent with DR-02 and the M1-E-cited recommendation).
- **Derived structures are not read as a source of truth.** `[P]`

### 8.3 Correction and cancellation
- Correction does not delete the previous link; the previous link stays in history and the new link is created in its new state. `[OA-claimed: M1-E items 2 and 4]`
- Cancellation leaves the link in history with a "cancelled" state and does not enter the current calculation. `[P]` (consistent with GOV-006 and PRV-007).
- **A confirmed link is not directly modified.** `[V: REQUIREMENTS.md PRV-007]`

### 8.4 History: recorded versus real
- **Transaction time:** when information was recorded or corrected in the system; supported in the MVP. `[P]`
- **Valid time:** when the relationship actually held; fields are reserved in database design without an MVP interface. `[P]`, `[DEFERRED]` to design.
- **Transaction time is not displayed as valid time.** `[P]`

### 8.5 Records and deletion
- **`[OPEN]` (pending legal review):** audit-record retention duration and the pseudonymous audit identifier for personal data. `[V: REQUIREMENTS.md PRV-009]`; DR-19.
- **Three distinct layers that must not be mixed:**
  1. **Current personal data and encrypted fields:** current values, modifiable per permissions.
  2. **Immutable audit records:** log events; not modified or deleted by ordinary users. `[OA-claimed]` (existence and principle); `[V: REQUIREMENTS.md FR-035, SEC-005]`
  3. **Any legally required deletion, concealment, or deidentification:** a separate, not-yet-defined path. `[OPEN]`
- **Key destruction does not automatically satisfy audit-record immutability.** Destroying a key makes encrypted values unreadable but does not mean the audit record is free of identifying elements, and it does not replace any legal deletion or deidentification action. `[P]` (idea); details `[OPEN]`.
- **Not decided here:** retention duration, deletion rights, key-destruction procedures, and whether destroyed encryption suffices as deletion. `[OPEN]` (OPEN-8) after legal review.
- **No legal-compliance judgment is made.** Legal requirements need an independent review.

## 9. Security, boundaries, and data isolation

### 9.1 Security boundaries
- **Identity:** phone + OTP. `[V: REQUIREMENTS.md FR-001]`. OTP provider `[DEFERRED]` to DR-22.
- **Authorization:** application-level and mandatory, then RLS as an extra layer (section 7.4). `[OA-claimed]`
- **Encryption:** for sensitive fields, using managed standard libraries, no custom algorithm. `[OA-claimed: M1-E item 13]`; `[V: REQUIREMENTS.md SEC-002]`

### 9.2 Data isolation between users
- A user sees another person's data only under a permission explicitly grounded in documented kinship or record ownership, per section 7. `[P]`
- **No separate "tenant" concept in the MVP.** The platform is single; isolation rests on access boundaries around the record and relationship, not on a separate database per family. `[P]` (this form is not decided in the sources and is an announced gap).
- **`[OPEN]`:** strict isolation of families from each other, if required, is a different decision to be made later; not assumed here.

### 9.3 Sensitive personal-data protection
- Sensitive fields identified in section 7.2 are encrypted at the application level. `[OA-claimed]`
- **Key storage, retrieval, and rotation:** `[DEFERRED]` to security design; related to hosting location decision (DR-21). No implementation details are written here.
- **Backup and recovery documentation before production:** mandatory. `[OA-claimed: M1-E item 13]`

### 9.4 Administrative (supervision) role
- The supervision role is limited to reports and accounts and has no authority over lineage. `[P]` (DR-26 in the specification; needs detailed approval). `[V: REQUIREMENTS.md GOV-003]`
- **`[OPEN]`:** scope of administration in the MVP and report procedures (see section 13).

## 10. Notifications and network participation

- **Notifications through the notification service (FCM).** `[V: REQUIREMENTS.md TECH-008, FR-034]`
- **The notification carries no sensitive information**; it points to a confirmation request or update and opens inside the app. `[P]`
- **Unregistered people receive no direct notifications** in the first release; they are handled through the user who created the record. `[P]` (DR-18).
- **Participation in network confirmation** means the eligible member is invited and shown the link with the necessary information, and records approval or objection. `[OA-claimed]` (principle); `[P]` (details).
- **Both parties are invited as members without veto right.** `[OA-claimed]`
- **The deceased is a distinctly marked visible node, does not vote, and is not represented by a proxy.** `[OA-claimed]` (adopted principle alone). No further eligibility or participation rules are derived from this; any additional detail `[DEFERRED]`.

## 11. Scalability and untested assumptions

### 11.1 Principle
This document declares no performance figures or capacity. Everything below is an assumption needing measurement.

### 11.2 Untested assumptions
- **Target person count:** not defined. `[OPEN]` (DR-24).
- **Kinship-calculation latency:** not measured. `[DEFERRED]` to phase 7 (PERF-003).
- **Effect of path explosion in overlapping trees:** not measured. `[V: M0 §F.2]`
- **Cost of recalculating derived structures on correction:** not measured. `[DEFERRED]`.

### 11.3 Scaling principles (no numbers)
- Kinship calculation reads only confirmed links and can be indexed later if measurement proves the need. `[P]`
- A technical search limit prevents calculation explosion and is disclosed at truncation (section 6.5). `[P]`
- Progressive network loading in the UI. `[V: REQUIREMENTS.md FR-033, PERF-001]`
- Storing confirmations and objections grows with link count and needs later indexing. `[P]`
- Redis is not added initially; it is added when a specific problem is measured. `[V: CONFLICTS-AND-GAPS.md CG-06, DR-08; REQUIREMENTS.md TECH-007]`

## 12. Architectural invariants and prohibitions

### 12.1 Invariants
1. **At most one confirmed biological father per child and at most one confirmed biological mother.** `[OA-claimed]`
2. **No committed set of confirmed biological links contains a cycle, including under concurrent writes.** `[OA-claimed]` (the invariant alone). Enforce-at-transition point `[P]`; enforcement mechanism `[DEFERRED]` to DB design + concurrency tests.
3. **Biological calculation reads confirmed links only.** `[OA-claimed]`, `[V: REQUIREMENTS.md FR-020]`
4. **A confirmed link is not directly modified; correction closes and replaces with history.** `[V: REQUIREMENTS.md PRV-007, GOV-006]`
5. **Every link change is recorded in the audit within the same transaction.** `[OA-claimed]`
6. **Kinship alone does not grant access to sensitive data.** `[OA-claimed]`
7. **No unrestricted parental access automatically.** `[OA-claimed]`
8. **Unknown father is absent; no fabricated record.** `[OA-claimed]`
9. **Breastfeeding, adoption, marriage, and guardianship do not enter the biological calculation.** `[OA-claimed]`, `[V: REQUIREMENTS.md GOV-011, GOV-012]`
10. **Network confirmation is not shown as scientific or legal proof.** `[P]` (consistent with the adopted "no ruling" principle).
11. **"No kinship" is not shown when the search stopped because of a limit.** `[P]`
12. **The deceased does not vote and has no proxy.** `[OA-claimed]`

### 12.2 Architectural prohibitions
- **No full event sourcing.** `[OA-claimed]`
- **No administrative ruling on lineage.** `[OA-claimed]`, `[V: REQUIREMENTS.md GOV-003]`
- **No hiding of an unregistered person from the network merely for lacking an account.** `[OA-claimed]`
- **No direct modification of a confirmed link.** `[V: REQUIREMENTS.md PRV-007]`
- **No fabricated person record to represent an unknown father.** `[OA-claimed]`
- **No custom encryption algorithm.** `[OA-claimed]`
- **No reliance on authorization alone without RLS, nor on RLS alone without application authorization.** `[OA-claimed]`
- **No naming or definition of "tenth degree" or kinship naming in this document.** `[OPEN]` (KD-01, KD-02).
- **No reliance on name similarity to prove lineage.** `[V: REQUIREMENTS.md GOV-001, GOV-008]`
- **Pending states do not enter the calculation.** `[V: REQUIREMENTS.md FR-020]`

## 13. Open decisions and their effect on subsequent design

| ID | Issue | Tag | Effect on design |
|---|---|---|---|
| OPEN-1 | Does an active objection immediately suspend a confirmed link from the biological calculation? | `[OPEN — OWNER DECISION REQUIRED]` | defines calculation logic and objection transactions; affects state and audit design |
| OPEN-2 | Can a rejected link be resubmitted with new evidence? | `[OPEN — OWNER DECISION REQUIRED]` | defines the transition out of "Rejected"; affects link state and history |
| OPEN-3 | Is "supported by independent evidence" a state, or only supporting information? | `[OPEN — OWNER DECISION REQUIRED]` | decides whether evidence is part of the state or a separate property; affects the state table |
| OPEN-4 | How are multiple accounts of one person identified and handled? | `[OPEN — OWNER DECISION REQUIRED]` | affects per-person counting and anti-duplicate voting |
| OPEN-5 | Definition of "tenth degree" | `[OPEN]` (KD-02) | engine response contract |
| OPEN-6 | Arabic kinship naming and its dictionary | `[OPEN]` (KD-01, DR-16) | UI display |
| OPEN-7 | Display order and grouping of paths | `[OPEN]` (DR-15, KE-04, KE-05) | UI and response |
| OPEN-8 | Audit retention duration and the pseudonymous identifier | `[OPEN]` (DR-19, after legal review) | audit design |
| OPEN-9 | Key storage, retrieval, rotation | `[OPEN]` (DR-20, DR-21) | security and deployment design |
| OPEN-10 | OTP provider | `[OPEN]` (DR-22) | phone verification |
| OPEN-11 | Age of majority and definition of a minor | `[OPEN]` (DR-06, legal review) | minor permissions |
| OPEN-12 | Hosting and data region | `[OPEN]` (DR-21) | deployment |
| OPEN-13 | Scope of supervision role and report procedures | `[OPEN]` (DR-26) | administration |
| OPEN-14 | Permission to a sensitive field of a child | `[OPEN]` (legal review) | minor permissions |
| OPEN-15 | Strict family isolation, if required | `[OPEN]` (gap; see 9.2) | isolation model |
| OPEN-16 | Cycle-prevention enforcement under concurrency | `[DEFERRED]` to DB design and concurrency tests | locks and transactions |
| OPEN-17 | Values of technical limits (search, objection, cooldown) | `[DEFERRED]` to measurement | configuration |
| OPEN-18 | Export, deletion, and user data rights (CG-32, GOV-005, PRV-006) | `[OPEN]` (DR-19 retention; legal review) | UI, audit, deletion design; effect of deletion on linked relatives' records |
| OPEN-19 | Is identity verification beyond OTP required, and who decides? (CG-33, DR-30) | `[OPEN — OWNER DECISION REQUIRED]`; advanced trust-level implementation `[DEFERRED]`. The DR-30 recommendation to keep it out of the MVP is not an owner decision settling the original question | account registration, trust level display, impersonation |
| OPEN-20 | Abuse, enumeration, and rate limits (CG-34, DR-05) | `[OPEN]` (needs a standalone security item) | phone search, rate limiting, monitoring |
| OPEN-21 | Ownership, creation, modification, and visibility of an unregistered record (CG-25, DR-11, PRV-003) | `[OPEN]` (owner decision not taken) | permissions on accountless records; one-sided false-lineage risk |

## 14. Explicitly deferred details

- **Adoption:** outside current scope (`[OA-claimed]`). No table or relationship. Reconsideration requires a separate request.
- **Breastfeeding implementation:** the architecture does not prevent adding it later as a separate category. `[DEFERRED]`.
- **RLS details** (policies, connection role, `FORCE ROW LEVEL SECURITY`): `[DEFERRED]` to DB design.
- **Chosen cycle-prevention mechanism** (lock, Serializable, or trigger): `[DEFERRED]` to DB design and concurrency tests.
- **Majority formula, quorum, denominator, objection and cooldown values:** `[DEFERRED]` — depend on real data; not set by guessing.
- **Detailed field encryption, key location, retrieval:** `[DEFERRED]` to security design.
- **Kinship and Closure table structures:** `[DEFERRED]` to DB design (DR-02, DR-03).
- **API interfaces and contracts:** `[DEFERRED]` to the API phase.
- **Web, broad admin dashboards, offline mode, calls, conversations:** `[DEFERRED]` (outside MVP).

## 15. Phase roadmap and documents required before each phase

| Phase | Goal | Documents required before it | Gate |
|---|---|---|---|
| M2 (current) | this corrected master architecture | the documents listed above | independent (non-author) review, then owner approval |
| M3 — database design | table model, constraints, indexes, transactions; concurrency-test planning for the cycle invariant | `DATABASE-DESIGN.md`. M3 must not silently resolve any OPEN item affecting data structure or link lifecycle (OPEN-1…OPEN-4 where applicable) | after independent architecture review and owner approval |
| M4 — security design | RLS, roles, encryption, keys, backup and recovery | `SECURITY-AND-PRIVACY.md` | after M3; RLS timing still open (see 7.4) |
| M5 — kinship engine | implement the engine per M0 unchanged | `RELATIONSHIP-ENGINE.md`, automated M0 tests. Engine reads only network-confirmed links, so it depends on OPEN-1 (objection effect changes calculation inputs) | after OPEN-1 and OPEN-5 (KD-02) |
| M6 — confirmation cycle | objection/confirmation/growth/resubmission logic | `RELATIONSHIP-ENGINE.md` (network section) | after the owner closes OPEN-1, OPEN-2, OPEN-3 |
| M7 — interfaces and app | network screens, paths, states | `UI-UX-SPECIFICATION.md`, OPEN-7 | after M5 and M6 |
| M8 — testing and release | concurrency tests for cycles and conflicting father/mother are planned in M3 and executed with M5/M6; not all deferred to M8 | `TEST-STRATEGY.md`, `PROJECT-STATUS.md` | after M3–M7 |

**Rule:** M3 does not start before an independent (non-author) architecture review and owner approval. No later design work may resolve an OPEN item affecting data structure or link lifecycle without an explicit owner decision. `AGENT-EXECUTION-RULES` and `DOCUMENTATION-STANDARDS` apply.

## 16. Consistency notes with the source documents

These notes record differences between this document and the existing source files without modifying them:

1. **FR-017, FR-018, FR-020, PRV-005, DR-10, DR-28, DR-02 in the existing files still carry their older wording.** This document adopts the owner-approved formulations where labeled (unverifiable; M1-E missing) and notes that the source files will be amended only by a separate order. The two are therefore not literally consistent until that update is applied.
2. **FR-010 (adoption) conflicts with the deferral decision.** This document follows the deferral; the original requirement stays as written until amended.
3. **Identifiers PD, NG, and KD are not documented in project files.** They appear in this document only as explicit references to their conversational source (M1-A and later). Approved sources are treated as stated in the declared decisions. **KE-04 and KE-05 also appear in this document (OPEN-7 and §6.4) with no definition or authority in any project file; their original meaning is unverified (M2-R9 note) and they are carried as-is from the source.**
4. **The original specification (§5, §6, §7) is not present inside the project**; some references rest on the summarized file. This constrains verification.
5. **`DECISIONS.md` — superseded by M2-R15.** The original sentence read "`DECISIONS.md` does not exist"; the register was created at `project-docs-en/DECISIONS.md` on 2026-11-02 (M2-R15) by owner order, and the P1–P17 principles and Q1–Q12 decisions are recorded there. The earlier sentence is preserved above as historical wording.
6. **This document is not approved before owner review.** The tags describe the type of each item; they do not substitute for approval.

## 17. M2-R21 amendment — owner clarifications from M2-R20 (2026-11-02)

Recorded in `DECISIONS.md` §3A (Q13–Q23) and §4A (OQ-21-00…OQ-21-14). The sections above keep their original text. The points below apply where the sections are read with those entries. None of them changes a decision.

- **§3 (identity):** Q13 applies. The Person ID is stable and independent of the Account ID; a Person may exist without an account; no automatic merge; identity matching is separate from parentage. The account-association verification method remains OPEN (OQ-21-10).
- **§4.2 and §12.1 (biological links):** Q17 keeps the previous confirmed link intact during correction review. When a replacement takes effect, and which state kinship calculation uses during review, is not decided (OQ-21-06). Any design must preserve the at-most-one invariant (§12.1 item 1). The confirmation rule for biological links is OPEN (OQ-21-01).
- **§5.1 (state list):** the single state sequence conflicts with Q16 (separate layers). It is kept as the descriptive wording and is not amended until OQ-21-02 is answered.
- **§5.3 (network confirmation):** Q15 introduces branch-specific acceptance. The single-network eligibility model is not changed until OQ-21-01 and OQ-21-02 are answered.
- **§7 and §9 (visibility):** Q14 makes visibility bilateral and branch-limited. Q10A (per-field privacy) applies unchanged. Eligible-portion rules are OPEN (OQ-21-03).
- **§6 and M0:** no change to M0. Kinship calculation reads confirmed biological links only. `[P]`: if a path or relative is hidden from a viewer, the response must not present the result as "no kinship" (an extension of invariant 11). Whether results are canonical or viewer-scoped is OPEN (OQ-21-02).
- **§8.3 and §10 (reviews and notifications):** Q20 and Q21 apply. Expiry is not acceptance, and reopening preserves history. Limit values and the exemption for high-risk notices are OPEN (OQ-21-07).
- **§15 (M3 gate):** in addition to the existing gate (independent review under Q11, then owner approval), M3 requires OQ-21-00, OQ-21-01, OQ-21-02, OQ-21-06, OQ-21-14, and the pre-existing OPEN-2 and OPEN-4. **M3 remains BLOCKED.**

## 18. M2-R22 amendment — owner confirmations (2026-11-02)

Recorded in `DECISIONS.md` §3B. Original sections keep their text, and historical statements are marked superseded where a decision covers them.

- **§5.3 (network confirmation):** per-network acceptance (OQ-21-01). The majority rule applies within one network only. No network's decision is imposed on another.
- **§6.2 (kinship inputs):** the M0 mathematical rules are unchanged (OQ-21-02). Each network computes from its own adopted relationship set. Whether an adopted link counts as "biologically confirmed" for M0 §B.1(3) is OPEN (OQ-21-16).
- **§8.3 (correction):** each network independently adopts or keeps a correction (OQ-21-06). The previous adopted relationship is kept until that network decides. No automatic replacement occurs.
- **§2.2 / §4 layers:** seven technical layers are kept separate (OQ-21-14). The lifecycle in §5.1 covers proposal and link state only; network acceptance and biological parentage are not single status values.
- **§7.4:** RLS timing is decided by Q9. The earlier `[OPEN]` statement is historical.
- **§13 (OPEN table):** OQ-21-01, OQ-21-02, OQ-21-06, and OQ-21-14 are closed. OQ-21-16 and OQ-21-17 are added. OPEN-2, OPEN-4, and OPEN-16 remain as before.

## 19. M2-R23 amendment — OQ-21-16 and the M0 interpretation (2026-11-02)

Recorded in `DECISIONS.md` §3B.4 (OQ-21-16, `OWNER-DIRECT-EVIDENCE`, option B). Original sections keep their text. This section is an interpretation of the approved decision. It does not change M0.

- **Approved interpretation:** biological parentage is adopted independently within each family network. "Biologically confirmed" in a network's calculation means adopted under that network's confirmation and governance rules (`DECISIONS.md` §3B.4). Network adoption is not proof of a universal biological fact.
- **M0 application (§6.2 and `08` §B.1(3)):** M0 is applied separately to each network's adopted parentage graph. The algorithm, formulas, symbols, and the 22 fixtures are unchanged.
- **Graph-integrity constraints that every network's adopted graph must satisfy (these are not new rules; they restate existing invariants):** parent-child direction; father and mother role distinction; at most one adopted biological father and one adopted biological mother per child within a network state (§4.2 item 1); no cycle within a network's adopted graph (§4.2 item 3); valid path and junction rules (`08` §C, §D).
- **§5.3 and §5.1 consistency:** per-network majority applies within one network only (OQ-21-01). A network's adopted graph changes only by that network's decision.
- **§8.3 correction:** a correction is adopted by a network only when that network decides; other networks keep their adopted relationship (OQ-21-06, OQ-21-16).
- **Evidence and certainty:** the system must show network adoption, supporting evidence, unresolved historical claims, and documentary or scientific certainty as separate items. No network is assumed to have equal evidentiary reliability.
- **Open after this amendment:** the calculation-snapshot mechanism (`DECISIONS.md` §3B.5, `AGENT-PROPOSAL`); the eligible-participant and threshold rules (OQ-21-05); the multiple-account and rejected-proposal rules (OQ-21-19, OQ-21-18).
- **Status of Q11 gate:** not executed. See `DECISIONS.md` §3 Q11 and the M2-R23 report.

**Final status:** draft for review. Every item not tagged `[OA-claimed]` remains proposed, open, or deferred.
---

## M2-R15 Amendment — owner decisions applied (2026-11-02)

Refer to `DECISIONS.md` (P1–P17; Q1–Q12). The sections above remain as originally drafted; the following items supersede their contested parts.

- **§5.4 / §13 (OPEN-1) — resolved by Q3.** An active objection does not automatically remove a confirmed biological relationship from biological kinship calculations; the relationship remains included until the network reaches a decision through the approved governance process. The objection (author, date, supporting evidence) is recorded and the disputed status is exposed to authorized viewers; one individual cannot unilaterally invalidate a confirmed relationship.
- **§5.6 / §13 (OPEN-3) — resolved by Q5.** Independent evidence is supporting information stored separately from the confirmation status, linked to the relationship, with provenance and metadata preserved; its presence or absence does not itself determine confirmation.
- **§5.2 / §13 (OPEN-2) — remains unresolved.** Q4 was not answered; the rejected → awaiting transition is still not approved.
- **§3.4 / §13 (OPEN-4) — remains unresolved.** Q6 was not answered; it is distinct from Q10's duplicate person-record behavior.
- **§4.2 invariant 3 / §12.1 / OPEN-16 — invariant stands; mechanism unresolved.** A reliable, concurrency-tested mechanism is required (P16); the specific mechanism and enforcement point remain engineering work (M3 planning / M8 execution). No mechanism is selected.
- **§6.2 (Inputs) — read with Q3.** A link that is Disputed solely because of an active objection on an already-confirmed link remains an engine input until a new network decision; the exclusion list applies to links that are not network-confirmed (proposed, awaiting, rejected, unresolved, corrected, cancelled) and to non-biological categories.
- **§7.1/§7.2 — Q10A.** Phone number, workplace, residence, and map location are optional profile fields; each field's visibility is controlled independently; configurable kinship-degree visibility groups are supported and enforced server-side; private information is not exposed in duplicate-person suggestions unless the viewer is authorized (PRV-011–013). Sensitive fields remain protected per the existing principles.
- **§7.4 — timing resolved by Q9.** RLS is designed and enabled from the beginning of database design and implementation; application authorization and RLS operate together; tenant/user isolation and unauthorized direct access are planned and tested; table ownership, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, and application database roles are explicitly examined; no effectiveness claim without executable security tests (SEC-010/011).
- **§8.1/§8.2 — Q1/Q2.** Current state remains the source of truth; audit records capture who/when, change type, affected information, and old and new values; state and audit are updated in the same transaction; full historical reconstruction is not required; derived structures are reproducible and preserve all path and parent-role information required by M0; a shortest-depth-only Closure Table is not assumed sufficient (TECH-015/016).
- **§8.5 — resolved in scope by Q7.** Audit history has no automatic expiration; ordinary application functions must not delete audit records; access is permission-controlled; legally defined privacy/deletion requirements remain for professional review (FR-046; DR-19 remainder open).
- **§3 / §9 (identity) — Q10B/C.** `Account ID` vs `Person ID`; a person may have a record without an account and multiple candidate records; a unique Person ID does not prove distinct people; duplicate-person detection/resolution behaviors are required (FR-048); DR-30/OPEN-19 status preserved; OPEN-4 remains open.
- **§13 OPEN table — status updates.** OPEN-1 decided (Q3); OPEN-3 decided (Q5); OPEN-8 decided in scope (Q7); OPEN-21 decided at principle level (Q8); DR-04 decided (Q9); DR-05 decided (Q10A); DR-11 decided at principle level (Q8); DR-19 decided in scope (Q7); DR-02/DR-28 decided (Q1/Q2); DR-31 decided as a requirement (Q11). OPEN-2, OPEN-4, OPEN-16 (mechanism), OPEN-19/DR-30 remain open; all other OPEN-5…OPEN-20 rows unchanged.
- **§15 roadmap (M3 gate) — Q11.** Before M3: an independent AI agent that did not prepare the reviewed documentation AND an independent human software engineer review the architecture; findings compared; material disagreements resolved; owner approves the outcome. **This gate is not yet satisfied; M3 remains BLOCKED.**
- **§16 item 5 — superseded.** The register exists at `project-docs-en/DECISIONS.md` (M2-R15).