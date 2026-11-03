# DECISIONS — Official Decision Register

**Purpose:** The single authoritative register of owner-approved decisions for the Sovereign Lineage Platform. No decision is effective, and no document may claim a decision is approved, unless it is recorded here with a stable identifier and traceable evidence.
**Authority:** Owner approval of Q12 (Option 3) and the M2-R15 corrective authorization (2026-11-02).
**Language:** English — per the owner's standing convention that newly created or modified official engineering documentation is written in English. The original Arabic source documents are preserved as historical reference and are not modified by this register.
**Evidence rule:** An entry is `OWNER-DIRECT-EVIDENCE` only when the owner stated it directly (here: the owner's decision messages recorded in the local conversation export, session `1793525922711_rqjpo` — M1-A, M1-C, the M1-E closure report, and the owner's acceptance of M1-E; and the Q1–Q12 decisions approved in the M2-R14/M2-R15 review). A label inside a repository file is recorded as `OWNER-APPROVED-CLAIM`, never as proof. `[PROPOSED]` marks agent proposals; `[INTERPRETATION]` marks derived technical readings that require design confirmation and are not owner decisions.
**Version / date:** M2-R21 — 2026-11-02. Adds owner clarifications Q13–Q23 (§3A) and open matters OQ-21-00…OQ-21-14 (§4A). No P1–P17 or Q1–Q12 entry was changed; the M2-R15 content is otherwise unchanged.
**Predecessor draft:** an Arabic-language working draft was archived outside the project as historical evidence (`%LOCALAPPDATA%\Temp\m2-r14\DECISIONS.ar-draft-20261102.md`, SHA-256 `ABEFBB230759C2B13EC39D0406C9B596A305B7135210F02DDA3A3F1D36A40E96`); it is not authoritative.

---

## 1. Classification legend

| Class | Meaning | Marker |
|---|---|---|
| Owner decision | Explicitly stated by the owner; registered verbatim below | `OWNER-DIRECT-EVIDENCE` |
| Claim (in-repository label) | A project file labels a statement `OWNER-APPROVED`; original evidence not in the repository | `OWNER-APPROVED-CLAIM` |
| Agent proposal | Proposed by an agent or reviewer; not approved; does not become a decision here | `[PROPOSED]` |
| Derived interpretation | A technical reading derived from an owner decision (e.g., what a decision implies for a table shape); requires design confirmation, never treated as the owner's own words | `[INTERPRETATION]` |
| Unresolved | No owner answer exists; explicitly kept open | `[UNRESOLVED]` |

Rule: a decision entry's governing text is the decision itself. Any "related identifiers" line is a **derived mapping** for traceability, not part of the decision, and is flagged as such.

---

## 2. Approved principles P1–P17 (evidence-classified)

The 17 principles were previously reported as approved and are confirmed by direct owner evidence in the preserved conversation export (M1-A, M1-C, M1-E acceptance). They are registered here under the owner's Q12 documentation order.

**Classification:** each principle is `OWNER-DIRECT-EVIDENCE` at conversation level and `OWNER-APPROVED-CLAIM` inside the repository files (the M1-E report is not stored in the project). Full evidence per principle is in `M2-R12-OWNER-DECISION-EVIDENCE.md` (external deliverable).

| ID | Principle (approved meaning) | Evidence references |
|---|---|---|
| P1 | Confirmed biological links are the current source of truth | M1-A §9; M1-C §9; M1-E item 1 |
| P2 | Immutable audit history records every change | M1-A §9; M1-C §9; M1-E item 2 |
| P3 | Current state and audit history are updated in the same transaction | M1-A §9; M1-C §9; M1-E item 3 |
| P4 | No full Event Sourcing | M1-A §9; M1-C §9; M1-E item 4 |
| P5 | Network majority confirmation; the platform is not a judge | M1-A §4; M1-C §1/§4; M1-E items 5–6 |
| P6 | Both parties participate; no individual veto | M1-C §1/§5; M1-E items 5–6 |
| P7 | Objections recorded and assessed through the network; objection does not automatically reject the link | M1-A §4; M1-C §1; M1-E item 7 |
| P8 | The deceased is a normal node, visually distinct, does not vote, and no one votes on their behalf | M1-C §3; M1-E item 8 |
| P9 | Adoption is deferred and outside the current release | M1-A §2; M1-C §6; M1-E item 9 |
| P10 | Breastfeeding is a distinct category, excluded from biological kinship calculation and inheritance; implementation detail deferred | M1-A §3; M1-C §6; M1-E item 10 |
| P11 | A child is visible to eligible relatives (existence, lineage, path); sensitive fields protected; no unrestricted automatic parental access | M1-A §7–8; M1-C §7; M1-E item 11 |
| P12 | Application-level authorization is mandatory; RLS is an additional layer working consistently with it | M1-C §10; M1-E item 12 |
| P13 | Standard supported cryptography only; backup and key-recovery documented before production | M1-C §10; M1-E item 13 |
| P14 | At most one confirmed biological father and one confirmed biological mother per child | M1-A §1; M1-C §11; M1-E item 14 |
| P15 | An unknown father remains absent; no fictitious person record | M1-A §1; M1-C §11; M1-E item 15 |
| P16 | Biological cycles are prevented by a reliable mechanism tested under concurrency; the mechanism itself remains an engineering decision | M1-C §12; M1-E item 16 |
| P17 | M0 and its 22 reference fixtures are immutable | M1-C §13; M1-E item 17; M2 authorization message |

All 17 principles are counted `OWNER-DIRECT-EVIDENCE` (0 `UNVERIFIED` after M2-R12 conversation recovery). Caveat preserved from M2-R12: these conversation-derived classifications stand only while the local session records are treated as authoritative.

---

## 3. Owner decisions Q1–Q12 (2026-11-02)

All decisions below are `OWNER-DIRECT-EVIDENCE`. The governing text is the owner's decision statement, recorded verbatim in English. Any "Related identifiers" line is a **derived mapping** (for traceability), not part of the decision text, and was drafted by the documenting agent; it does not expand or reinterpret the decision.

### Q1 — Current state and audit history

> Current relationship state remains the authoritative source of truth. Maintain an immutable audit history. Audit records must identify who performed each change and when. Record the change type and affected information. Preserve old and new values. Update current state and its audit record in the same database transaction. Do not implement full Event Sourcing. **Full historical state reconstruction is NOT required.**

- **Related identifiers (derived mapping):** DR-02, DR-28 (state source / audit pattern); aligns with P1–P4.
- **Resolves:** the DR-02 vs DR-28 conflict on the side of current-state authority with an immutable audit record storing old and new values (snapshot-style record).
- **`[INTERPRETATION]`:** "preserve old and new values" + "full reconstruction NOT required" is a natural design reading of a row-snapshot-style audit record; the concrete audit-record schema is M3/M4 design work, not part of the decision.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided.

### Q2 — Biological relationship source of truth

> Original biological parent-child relationships are the sole source of truth for biological lineage. Ancestor tables, path data, and other derived structures are not independent sources of lineage truth. Derived data must be reproducible from the original relationships. Derived structures must preserve all path and parent-role information required by M0. **Do not assume that a conventional Closure Table storing only shortest depth is sufficient.**

- **Related identifiers (derived mapping):** DR-02, DR-03, TECH-012, TECH-013.
- **Resolves:** the substantive source-of-truth question for derived structures (DR-02/DR-03 at principle level).
- **`[INTERPRETATION]`:** whether the derived structure is physically one table or two (DR-03's original option 1 vs option 2) is left to database design, **constrained** by the requirement to preserve all path and parent-role information and to be reproducible; a shortest-depth-only closure is explicitly insufficient.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided.

### Q3 — Objection against a confirmed relationship

> An active objection does not automatically remove a confirmed biological relationship from kinship calculations. The relationship remains included until the network reaches a decision through the approved governance process. Record the objection, its author, date, and supporting evidence. Clearly expose the disputed status to authorized viewers. **Do not let one individual unilaterally invalidate a confirmed relationship.**

- **Related identifiers (derived mapping):** OPEN-1.
- **Resolves:** OPEN-1 (the "remain included until network decision" alternative).
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided. Abuse-reduction mechanics (one active objection per person, mandatory reason, cooldown) remain `[PROPOSED]` design details and are not approved here.

### Q5 — Independent evidence

> Independent evidence must be stored separately from the relationship's confirmation status. Evidence records must be linked to the relevant relationship. The existence or absence of independent evidence must not itself determine whether a relationship is confirmed. Preserve evidence provenance and relevant metadata.

- **Related identifiers (derived mapping):** OPEN-3, FR-018 (semantics of "supported by independent evidence").
- **Resolves:** OPEN-3 (independent evidence is supporting information bound to the link, not a separate confirmation state).
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided.

### Q7 — Audit retention

> Audit history has no predefined automatic expiration period. Ordinary application functions must not delete audit records. Access to audit records must be permission-controlled. Preserve this owner decision while separately identifying applicable privacy, data-protection, and legal deletion requirements for professional review. **Do not silently weaken or reinterpret the owner's retention decision.**

- **Related identifiers (derived mapping):** OPEN-8, DR-19.
- **Resolves (partially):** retention duration (no automatic expiration) and the prohibition on application-level deletion; access control over audit records. **Remains open:** the pseudonymous audit-identifier scheme and any deletion/key-destruction path tied to legal requirements — those await legal review and are not decided by Q7.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided (scope limited to the bullets above).

### Q8 — Records belonging to people without accounts

> The record creator may manage permitted basic information. Record creation does not grant unrestricted ownership or control over the person or their biological lineage. Sensitive changes must follow additional authorization rules. Biological relationship confirmation and changes must follow the approved network governance process. The system must maintain audit history and provenance. **The creator must not automatically receive access to all sensitive personal information.**

- **Related identifiers (derived mapping):** OPEN-21, DR-11.
- **Resolves:** OPEN-21 at the principle level (creator's role is limited; no unrestricted ownership; network governance governs biological relationships; audit/provenance maintained; no automatic sensitive access).
- **Remains open:** the claim mechanism (DR-12), the precise permission matrix and field-level rules (design work), and how "additional authorization rules" for sensitive changes are specified.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided (principle level).

### Q9 — PostgreSQL Row-Level Security

> RLS must be designed and enabled from the beginning of database design and implementation. Application authorization and database RLS must operate together. Plan and test tenant/user isolation and unauthorized direct database access. Explicitly examine table ownership, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, and application database roles. **Do not claim RLS is effective without executable security tests.**

- **Related identifiers (derived mapping):** DR-04, SEC-004, P12.
- **Resolves:** DR-04 — RLS is applied from the beginning of database design/implementation (phase 1), as a layer alongside application authorization.
- **Remains open (engineering, M4):** the concrete RLS policies, database roles, and test designs. Q9 requires them to be planned and tested but does not define them.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided.

### Q10 — Personal information, encryption, privacy, and identity resolution

**A. Personal information protection**

> Encrypt phone numbers and sensitive personal information at rest. Use a separate keyed HMAC mechanism for exact phone-number lookup and matching without storing a plaintext searchable copy. Use secure, independently managed encryption keys. Phone number, workplace, residence, and map location are optional profile information. The person must control visibility of each information field independently. The person may hide information or authorize visibility to selected relatives. Visibility policies must support configurable kinship-degree groups, such as first-, second-, or third-degree relatives, and all eligible relatives. Enforce these policies server-side, not merely through UI hiding. Do not expose private information during duplicate-person suggestions unless the viewer is authorized to see it.

**B. Separate account and person identity**

> `Account ID` identifies a login account. `Person ID` identifies a person record in the lineage network. A person may have a record without having an account. A person may be represented by multiple independently created candidate records before duplicate resolution. A unique Person ID alone does not prove that two records represent different real people.

**C. Duplicate-person detection and resolution**

> The system must support this scenario: the same real person may be entered independently by multiple relatives (e.g., a brother, cousin, or other family member), and may later create their own account. Required behavior: (1) when a user attempts to add a person, search for plausible existing person records; (2) compare available, authorized information, including names, family relationships, and other permitted matching attributes; (3) present a candidate suggestion when an existing record may represent the same person; (4) the suggestion may explain the candidate using information the current user is authorized to view, such as the person's name and permitted residence area; (5) ask whether the user means the existing person; (6) if confirmed, link the new family relationship to the existing Person ID rather than creating another record; (7) preserve the first existing record as the primary record when the match is confirmed; (8) preserve the provenance of each contributor and the origin of every submitted relationship; (9) if the user rejects the suggestion, allow a separate record to be created; (10) if evidence is ambiguous or conflicting, route the case to an appropriate review process rather than automatically merging; (11) when the real person creates an account, support a controlled process to request and verify association with their existing person record; (12) preserve historical identifiers, source records, relationships, and audit history during any approved reconciliation.

**Constraints (part of the decision):** different kinship descriptions do not prove that two records represent different people (the same person can be a cousin through different family branches); similar names alone must never trigger automatic merging; a confirmed person-identity match does not automatically confirm a biological parent-child relationship; protected profile information must not be disclosed to facilitate matching; **identity-verification policy is not settled — DR-30 / OPEN-19 retains its existing status and remains subject to future decisions.**

- **Related identifiers (derived mapping):** DR-05 (phone storage/matching), SEC-002, PRV-002/006/010, FR-014/FR-016 (person suggestion behavior), FR-030, GOV-001/GOV-008 (name similarity), DATA-* (person identity), and the duplicate-person behavior in A/B/C above.
- **Resolves / touches:** DR-05 storage-and-matching approach (encrypted at rest + keyed HMAC lookup; plaintext excluded). **Scope limits:** Q10 does **not** resolve the complete identity-verification and duplicate-resolution design; it does **not** resolve DR-30/OPEN-19 (explicitly preserved); it does **not** resolve OPEN-4 (multiple accounts — a different question from duplicate person *records*); rate-limit/abuse values remain `[PROPOSED]` (DR-34/OPEN-20).
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided to the extent of the paragraphs above.

### Q11 — Independent review

> The owner requires BOTH: (1) an independent AI agent that did not prepare the reviewed documentation, and (2) an independent human software engineer. Their findings must be compared, material disagreements resolved, and the owner must approve the outcome before M3 begins.

- **Related identifiers (derived mapping):** DR-31, CG-43.
- **Resolves:** the review-arrangement form required before M3 (both an independent AI agent and an independent human engineer). **It does not mean the review has already happened** — the dual review and the owner's approval of its outcome remain outstanding gates before M3.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided (requirement), gate **not yet executed**.

### Q12 — Formal decision registration

> Create a formal `DECISIONS.md` file. Record all approved owner decisions with stable identifiers and traceable evidence. Update all affected authoritative documents so they no longer contradict the approved decisions. Preserve historical documentation and change traceability. Maintain consistency between Arabic source documents and English documentation.

- **Related identifiers (derived mapping):** this register; the M2-R15 documentation-correction authorization; original/OPS-002 (phase-0 deliverable).
- **Scope limit:** establishing the register and reconciling documentation **does not authorize M3** or any implementation work.
- **Status:** `OWNER-DIRECT-EVIDENCE` — decided; being executed by M2-R15.

---

## 3A. Owner clarifications Q13–Q23 (M2-R20 follow-up, registered in M2-R21)

**Evidence status (applies to every entry in this section):** The M2-R20 owner messages are not stored in the workspace or in the external report folders searched in M2-R21. The governing text below is the owner decision set stated in the M2-R21 brief, paraphrased for the register. Each entry is therefore `OWNER-APPROVED-CLAIM` (the owner's stated position, not yet verified against a dated owner message). No entry is `OWNER-DIRECT-EVIDENCE` until OQ-21-00 is closed. Verbatim owner text is pending OQ-21-00.

Where an entry conflicts with an approved principle or decision, the conflict is listed and is not resolved here (see `15-UNRESOLVED-CONTRADICTIONS.md`, M2-R21 amendment, C-R21-xx).

### Q13 — Account/Person separation and same-person matching

> Accounts and Person records are separate. Every Person has a stable unique Person ID independent of any Account ID. A Person may exist without an account, including deceased persons. Phone numbers and national identifiers are not mandatory to create a Person. Before creating a potentially duplicate Person, the system suggests existing records. Matching never relies on name similarity alone. Suspected duplicates are never merged automatically. A verified match preserves source provenance, existing relationships, and audit history. Account registration and account-to-Person association require safe verification. Identity matching is distinct from biological parentage confirmation.

- **Not decided:** the account-association verification method (OQ-21-10). DR-30 / OPEN-19 is unchanged.
- **Related identifiers (derived mapping):** Q10B, Q10C, P8, P15, Q5.
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q14 — Reciprocal association and branch-limited network visibility

> Family-network expansion is progressive and reciprocal. A user may suggest or add a person with an assumed relationship. The two parties must confirm the association before either party's wider family network is revealed. After bilateral confirmation, only the eligible portions of each network are revealed, according to the agreed relationship, branch, and privacy rules. The system never exposes every connected branch. Shared connections may help assess plausibility. An inconsistent association may be rejected or disconnected. Disconnection never destroys the original records or unrelated networks. Reciprocal visibility is not proof of biological parentage.

- **Not decided:** the eligible-portion matrix, including in-law and sibling-marriage branches (OQ-21-03); whether a non-responding party can block an association indefinitely (OQ-21-04).
- **Conflict:** C-R21-01 (potential tension with P6, if read as a participation right).
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q15 — Network-specific acceptance, rejection, and contributor notification

> Each individual and family branch controls which additions and relationships are accepted into its own network. One branch may accept an additional ancestor while another declines; the accepting network shows it, and the declining network does not change. A rejected proposal never deletes the contributor's information. A proposal not accepted into a network remains distinguishable from a confirmed, connected relationship. The contributor is notified of a rejection and may cancel, contact the rejecting relative, clarify, or request reconsideration. One person's rejection does not automatically remove a relationship from other networks, and one relative's objection does not automatically invalidate an addition in other networks. Network-specific acceptance is not canonical biological parentage and does not confirm a biological relationship globally.

- **Not decided:** whether network-specific acceptance changes biological inputs to kinship calculation (OQ-21-01, OQ-21-02).
- **Conflict:** C-R21-02 (direct conflict with the single-network majority model in P5, Q3, and `09-MASTER-ARCHITECTURE.md` §5.3).
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q16 — Layered relationship model

> The platform distinguishes at least seven layers and does not collapse them into one status field: (1) Person record existence; (2) proposed relationship; (3) bilateral account/person association; (4) network-specific acceptance; (5) confirmed biological parentage; (6) derived kinship; (7) private or restricted personal information.

- **Not decided:** how the layers coexist with the global biological source of truth (Q1, Q2, M0). Alternatives are analysed in the M2-R21 report, not approved (OQ-21-02, OQ-21-14).
- **Conflict:** C-R21-03 (FR-018 and `09-MASTER-ARCHITECTURE.md` §5.1 use one state sequence); C-R21-04 (viewer-dependent results vs M0 §B.1(3)).
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q17 — Non-conflicting addition and correction of confirmed parentage

> (A) An ancestor may be added where no confirmed parent relationship is being replaced. (B) Replacing a confirmed biological father or mother requires a stricter, controlled correction process. The previous relationship remains intact while the correction is reviewed. Preserve the previous relationship, the proposed replacement, evidence, contributors, participants, objections, decisions, reasons, timestamps, and historical state. No automatic deletion, suspension, or replacement occurs merely because a correction was proposed.

- **Not decided:** when a replacement takes effect and which state kinship calculation uses during review (OQ-21-06).
- **Related identifiers (derived mapping):** PRV-007, GOV-006, `09-MASTER-ARCHITECTURE.md` §8.3 and §12.1.
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q18 — Governance participants

> The system identifies relevant relatives from the affected branches. A qualified family specialist or knowledgeable elder may suggest additional participants. The reason for each selected participant is recorded. A specialist has no unilateral authority to determine or change biological parentage.

- **Not decided:** the definition of eligible participants and specialist qualifications (OQ-21-05).
- **Related identifiers (derived mapping):** GOV-003.
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q19 — Differentiated decision thresholds

> Governance is differentiated by the risk and type of change. No threshold, quorum, abstention rule, or response requirement is set by this register.

- **Not decided:** every value and rule in the owner brief: eligible participants, quorum, abstentions, response requirements, and thresholds per decision type (OQ-21-05). No percentage or voting threshold is recorded here.
- **Status:** `OWNER-APPROVED-CLAIM` (principle only).

### Q20 — Review deadlines and notification management

> Reviews may remain pending. The owner needs to manage review workload. Notifications go to the relevant persons, not to everyone. Notifications may be limited, grouped, or made configurable by daily limit or frequency. Expiry of a response period is never automatic acceptance or rejection. Extensions may be appropriate when material evidence or objections arise. Confirmed additions and additions requiring confirmation are separate categories.

- **Not decided:** limit values and whether mandatory notices for high-risk corrections are exempt from limits (C-R21-05; OQ-21-07).
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q21 — Reconsideration of previous decisions

> Relatives may request reconsideration of previously accepted additions or decisions. The original decision and the full review history are preserved. A new request never silently overwrites the previous state.

- **Not decided:** how reopening interacts with network-specific acceptance and with canonical correction (OQ-21-09).
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q22 — Accountless and deceased Persons; evidence and provenance

> The platform supports accountless and deceased Persons. Evidence may include family testimony, documents, historical records, knowledgeable relatives, and specialist review. The source and provenance of each claim are recorded. A specialist must not independently determine biological parentage. Identity or existence verification and biological-parentage verification remain separate.

- **Not decided:** the evidence data model (OQ-21-11) and the privacy scope for deceased persons (OQ-21-12).
- **Status:** `OWNER-APPROVED-CLAIM`.

### Q23 — Bulk review and approval

> Review queues may group notifications. Bulk approval may be used for eligible already-confirmed items where it is safe. Unconfirmed items are kept separate and are never included in bulk confirmation as if they were already approved.

- **Not decided:** what makes an item eligible for bulk approval, and the safeguards against unrelated or high-risk items (OQ-21-08).
- **Status:** `OWNER-APPROVED-CLAIM`.

---

## 3B. Owner confirmations supplied in M2-R22 — OQ-21-00 disposition and new decisions

**Provenance (recorded exactly as supplied):** the owner supplied these confirmations explicitly in the M2-R22 task brief, in the current conversation. No dated message export, verbatim quotation, or timestamp was supplied, and none is recorded here. The M2-R20 messages themselves were not recovered. Entries are therefore `OWNER-DIRECT-EVIDENCE` in the sense that the owner stated them in the current conversation; the exact wording still needs matching to a dated message if one becomes available.

### OQ-21-00 — disposition: CLOSED as a mapping, with a residual limit

- The owner confirmations supplied in M2-R22 (D13, G1–G5, D2, D5, D7, D11, D12, lineage branch acceptance, missing ancestor vs. parent replacement, notifications, rejection workflow, M0 disputed wording) are mapped to Q13–Q23 in the table below.
- **Closed:** the mapping of Q13–Q23 to owner confirmations.
- **Not closed:** the verbatim text and dated provenance of the M2-R20 messages. Recorded as `UNVERIFIED`. It does not block the decisions in §3B.2, but no entry may be cited as recovered M2-R20 evidence.

| Entry | Owner confirmation (M2-R22) | Disposition | Residual limit |
|---|---|---|---|
| Q13 | D13 (matching; association by bilateral confirmation), D7 (stable Person ID; phone and national ID optional), D5 (prevent duplicates; controlled reconciliation; never auto-merge when identity is uncertain), D12 (a suggestion is not a confirmation) | `OWNER-APPROVED-CLAIM` → mapped to owner confirmation | No numerical matching thresholds set (OQ-21-15). Account-association method open (OQ-21-10). |
| Q14 | D13, D12 (reciprocal confirmation before wider network visibility) | `OWNER-APPROVED-CLAIM` → mapped | Eligible-portion matrix open (OQ-21-03). Non-response rule open (OQ-21-04). |
| Q15 | Lineage branch acceptance (C), rejection workflow (B), G3 (objections do not impose across networks), OQ-21-01 (§3B.2) | `OWNER-APPROVED-CLAIM` → mapped; network-specific acceptance confirmed by OQ-21-01 | Effect on the canonical graph: see §3B.3 and OQ-21-16. |
| Q16 | OQ-21-14 (§3B.2) | `OWNER-APPROVED-CLAIM` → seven layers confirmed by OQ-21-14 | Storage for historical or alternative narratives not decided (OQ-21-14 residual; §4A). |
| Q17 | Missing ancestor vs. parent replacement (B), G1 (participants), OQ-21-06 (§3B.2) | `OWNER-APPROVED-CLAIM` → mapped; effective date confirmed by OQ-21-06 | Participant eligibility open (OQ-21-05). |
| Q18 | G1 (specialist may recommend participants, reason recorded; no unilateral authority) | `OWNER-APPROVED-CLAIM` → mapped | Eligibility and qualification open (OQ-21-05). |
| Q19 | G2 (approval varies by type and risk; no invented thresholds) | `OWNER-APPROVED-CLAIM` → mapped (principle) | All values open (OQ-21-05). |
| Q20 | Notifications (C with clarifications), G4 (expiry is not approval or rejection; extension on material objection or evidence) | `OWNER-APPROVED-CLAIM` → mapped | Limit values and high-risk exemption open (OQ-21-07). |
| Q21 | G5 (screened reconsideration; unsupported requests do not reopen everything; history preserved) | `OWNER-APPROVED-CLAIM` → mapped | Interaction with network acceptance and canonical correction open (OQ-21-09). |
| Q22 | D2 (accountless and deceased records from testimony, documents, records; source recorded; specialist recommends but does not decide alone; identity and parentage verification separate) | `OWNER-APPROVED-CLAIM` → mapped | Alternate verification methods and evidence data model open (OQ-21-11). |
| Q23 | Notifications clarification (bulk approval only for eligible, sufficiently complete, low-risk items; high-risk or incomplete never bulk-approved) | `OWNER-APPROVED-CLAIM` → mapped | Eligibility criteria and safeguards open (OQ-21-08). |

### 3B.2 Newly confirmed owner decisions

- **OQ-21-01 — Independent network acceptance (owner option C).** Status: `OWNER-DIRECT-EVIDENCE` (owner statement in the M2-R22 conversation). Each network has its own acceptance state for a proposed addition. One network may accept a proposal while another rejects it. A shared provenance record holds the proposal's source, contributors, decisions, and affected networks. No network's decision is forced onto another.
- **OQ-21-02 — Kinship calculation results (owner option C, with explicit clarification).** Status: `OWNER-DIRECT-EVIDENCE`. Kinship results may differ between users or networks. The M0 mathematical rules remain unchanged. Each network's calculation uses its own adopted relationship set. This is not a change to the M0 algorithm. The wording conflict with M0 §B.1(3) is recorded in §3B.3.
- **OQ-21-06 — Parentage correction effective date (owner option C).** Status: `OWNER-DIRECT-EVIDENCE`. Each network independently decides whether to adopt an approved correction. An adopting network uses the new relationship; a rejecting network keeps its previous adopted relationship; a network that has not completed review does not change automatically. The history of both relationships, evidence, objections, decisions, and timestamps is preserved. Acceptance in one network is not proof of a universal biological fact.
- **OQ-21-14 — Separate technical relationship layers (owner explicit approval).** Status: `OWNER-DIRECT-EVIDENCE`. Seven concepts are kept separate and not collapsed into one status field or one generic lifecycle: (1) Person record; (2) proposed addition or contribution; (3) account-to-person association; (4) biological relationship; (5) network-specific relationship acceptance; (6) derived kinship calculation; (7) personal-data privacy and visibility.
- **M0 disputed wording (owner option B).** Status: `OWNER-DIRECT-EVIDENCE`. An objection is recorded separately and does not automatically change a relationship's confirmation state or kinship calculation. Network-specific adoption and rejection are represented explicitly. M0 and its fixtures are not changed. This is consistent with Q3 (`OWNER-DIRECT-EVIDENCE`, M2-R15).

### 3B.3 Conflict status after these decisions (not resolved here)

- **C-R22-01 — OQ-21-02 versus M0 §B.1(3) wording.** M0 §B.1(3) says biological calculations use only "biologically confirmed" parenting links. OQ-21-02 allows results to differ between networks, with M0 unchanged. The M0 wording does not say whether "biologically confirmed" is a per-network or a global property. This is a **residual wording conflict**. It is not resolved by changing M0. It needs an explicit owner reading (OQ-21-16).
- **Network acceptance is not biological proof.** Per OQ-21-06 and Q16, acceptance in one network does not establish a biological fact. A global biological statement needs the separate biological-parentage path.
- **C-R21-02 and C-R21-03** are reconciled in `15-UNRESOLVED-CONTRADICTIONS.md` (M2-R22 amendment) and are not resolved in this section alone.

### 3B.4 OQ-21-16 — Network-specific biological parentage adoption (owner option B)

**Status:** `OWNER-DIRECT-EVIDENCE` — the owner explicitly selected option B in the M2-R23 conversation. No dated message export or verbatim quotation was supplied; the provenance limit recorded in §3B applies.

**Approved decision:**

- Biological parentage relationships are adopted independently within each family network.
- Each network's adopted biological relationship set is an input to its own kinship calculations.
- One network may adopt a parentage correction while another network retains the previous relationship.
- A network that has not completed its review does not automatically adopt the correction.
- An objection or rejection in one network does not automatically change the adopted relationship set in another network.
- A shared provenance and history record is kept for proposed relationships, sources, contributors, objections, reviews, and network decisions.
- The M0 mathematical rules remain fixed and unchanged.
- "Biologically confirmed", in a network's calculation, means the relationship has been adopted under that network's applicable confirmation and governance rules.
- Network adoption is not proof of a universally established biological fact.
- The system must distinguish network adoption, supporting evidence, unresolved historical claims, and scientific or documentary certainty.

**Limits (not decided by this entry):**

- Evidence quality may differ between networks. Governance and evidence quality must remain visible and traceable. No network is treated as having equal evidentiary reliability.
- The approved decision does not define the eligible-participant, quorum, or threshold rules (OQ-21-05).
- It does not decide the physical storage or snapshot mechanism for reproducible results (see §3B.5, AGENT-PROPOSAL).

**Consequence for M0 (interpretation, not modification):** M0 §B.1(3) is applied to each network's adopted graph separately. The algorithm and fixtures are unchanged. See `08` §B.1(3) (protected) and `09` §18.1.

### 3B.5 Calculation reproducibility — AGENT-PROPOSAL (not an owner decision)

**Status:** `AGENT-PROPOSAL`. The owner has not approved any snapshot or reproducibility mechanism. This entry does not register one as a decision.

**Proposal:** each kinship result records enough metadata to be reproduced: network identifier; network state or adopted-input version (the history point of the adopted parentage set); a reference to the relationship input (a snapshot or an equivalent reproducible reference); M0 specification version; and calculation timestamp or execution metadata where appropriate.

**Benefits:** results remain reproducible after later adoptions or corrections (OQ-21-06 preserves history); disputes can cite the exact input; the M0 fixture harness can be replayed per network.

**Costs and alternatives:** (a) full input snapshot per calculation: exact, but storage-heavy; (b) versioned adopted-set identifier plus the audit history it refers to: compact, but needs a correct history index; (c) recompute on demand from history: no extra storage, but results change when history is edited, so it weakens reproducibility unless history is append-only (Q1, P2, P3 support this). The choice is a technical design decision for M3-B, subject to verification.

**Owner approval required before this becomes a rule.**

### 3B.6 OPEN-2 and OPEN-4 — status after M2-R23 analysis (no owner decision recorded)

**OPEN-2 (rejected relationship, `15` §1):** "can a rejected link be resubmitted when new evidence becomes available?" Status unchanged: `[UNRESOLVED]`. The approved principles that bound it are: a rejection is a recorded network result that does not delete the contributor's record (Q15, OQ-21-01); a rejection in one network does not change another (OQ-21-01, OQ-21-16); unsupported reconsideration requests do not reopen decisions automatically, and requests are screened (G5, Q21). Remaining open: whether resubmission requires new evidence or new circumstances; whether a different network may review a revised proposal; whether revision is allowed instead of duplication; the abuse limits. Owner question: OQ-21-18 (see §4A).

**OPEN-4 (multiple accounts, `15` §1):** "how multiple accounts of one person are identified and handled." Status unchanged: `[UNRESOLVED]`. Approved principles that bound it: a Person has a stable ID independent of any Account (Q13, D7); identity matching never relies on name similarity alone, and suspected duplicates are never merged automatically (Q13, D5); reconciliation uses a controlled verification process and preserves relationships, provenance, and audit (D5); account association requires safe verification (Q13), whose method is OQ-21-10. Remaining open: whether one Person may have several accounts, one account several Persons, and the rules for each; account recovery; impersonation controls. Owner question: OQ-21-19 (see §4A).

<!--M2R23-3B6-->






## 3C. M2-R24 product-scope reset and owner decisions (2026-11-02)

**Provenance:** the owner stated these decisions in the M2-R24 task brief in this conversation. No dated message export or verbatim quotation was supplied. Entries are recorded as `OWNER-DIRECT-EVIDENCE` in the sense that the owner stated them in the current conversation (same limit as §3B).

### 3C.1 Product-scope reset (superseding product-scope statement)

The owner stated that the Sovereign Lineage Platform is **primarily a family discovery, relationship-awareness, and family-connection platform.** It is **not** a legal genealogy authority, a court, or an institution that officially proves biological lineage.

- **Supersedes:** the product-scope framing of the earlier documents as a legal-grade lineage-confirmation system. That framing is historical and is not deleted.
- **Preserved unchanged:** P1 (confirmed biological links are the current source of truth for calculation), Q2 (biological relationship source of truth), and M0. The reset changes priority and proportionality of governance and evidence work. It does not change the calculation source of truth.
- **Consequence:** accuracy, privacy, and resistance to fabricated relationships remain required. Architecture and development process must be proportionate to the discovery purpose.

### 3C.2 Owner decisions recorded in M2-R24

- **OQ-21-03 — visibility (Option D).** Status: `OWNER-DIRECT-EVIDENCE`. The system determines eligible relatives from confirmed relationships and network boundaries. Each person controls access to their personal information. Specific people may be granted or denied access. Seeing a relative in another person's network does **not** grant access to all details of that relative's network. **Partly resolved:** the detailed visibility matrix, including in-laws and sibling marriages, still requires conceptual design (remains open as a design item).
- **OQ-21-05 — governance thresholds (Option D).** Status: `OWNER-DIRECT-EVIDENCE`. No numerical approval percentages are set. Eligible participants, evidence weight, objections, abstentions, and non-responses are to be defined by decision type and risk. Numerical thresholds follow the governance design. **Partly resolved** (principle only).
- **OQ-21-07 — notifications (Option D).** Status: `OWNER-DIRECT-EVIDENCE`. Configurable daily limits, batching, and review queues are supported. No numerical limits are selected. Important pending requests remain accessible even when notifications are suppressed or grouped. **Partly resolved** (principle only).
- **OQ-21-08 — bulk approval (Option C).** Status: `OWNER-DIRECT-EVIDENCE`. Bulk approval only for complete, eligible, low-risk items. Sensitive biological relationships, disputed items, and incomplete items are excluded. Every item keeps its own independently recorded decision and audit entry. **Resolved** at principle level.
- **OQ-21-10 — account-to-Person verification (Option B).** Status: `OWNER-DIRECT-EVIDENCE`. OTP verifies control of a phone number, not the real-world identity of a person. Linking an account to an existing Person requires additional reliable verification. The verification method, result, and provenance are recorded. An alternative review path exists when verification cannot be completed. **No final verification method is selected** (requires legal/privacy assessment and technical design). Partly resolved.
- **OQ-21-12 — deceased Persons' privacy (Option C).** Status: `OWNER-DIRECT-EVIDENCE`. Death does not make sensitive information public. Sensitive information remains protected. Access rules for deceased Persons are to be designed. Information about living people appearing in a deceased person's record remains protected. Legal and privacy assessment is required before production. Partly resolved (principle only).
- **OQ-21-18 — reopening a rejected proposal (owner decision, M2-R24 execution brief).** Status: `OWNER-DIRECT-EVIDENCE` as stated in the M2-R24 execution brief. Reopening a rejected proposal requires new evidence or a material new reason. The original rejection is preserved. Not decided here: the reopening procedure, who may request reopening, and abuse limits (see M3 conceptual design, `09` §20).
- **OQ-21-19 — multiple accounts per Person (owner decision, M2-R24 execution brief).** Status: `OWNER-DIRECT-EVIDENCE` as stated in the M2-R24 execution brief. Historical status: OPEN in §3B.6 and §4A through M2-R23 (OPEN-4 / Q6). The earlier register text did not contain this decision; this entry records it as new. Approved rules:
  1. One Person may be associated with multiple accounts over time.
  2. Only one account may be active for that Person at a time.
  3. Old accounts are not automatically deleted.
  4. Account recovery or transfer of association requires reliable verification.
  5. Account association, unlinking, recovery, and transfer events must be audited.
  6. Creating a new account does not automatically create a new Person.
  7. Simultaneous active accounts claiming the same Person identity must be prevented.
  Verification method for rule 4: OQ-21-10 (open; legal and privacy review). Not decided here: the account-recovery procedure itself and the audit schema.

<!--M2R24-3C-END-->

## 3D. Final owner decision baseline — reconciliation record (2026-11-03)

**Provenance rule for this section:** the decisions below were stated by the owner in the current M3 final decision brief. No dated transcript was recovered. Each entry is `RECONSTRUCTED-FROM-OWNER-BRIEF`: the meaning is the owner's, the wording is a reconstruction, and the owner must check it against the original text before it is treated as verbatim. Full analysis: `project-docs-en/m3-review/FINAL-OWNER-DECISION-RECONCILIATION.md` and `-PART2.md`.

Absence of an entry in §§2–3B does not mean the owner did not answer; the answers below are the recorded baseline.

| ID | Decision (meaning) | Provenance | Status |
|---|---|---|---|
| R-01 | Shared-relative discovery is an essential capability (not deferred). | RECONSTRUCTED-FROM-OWNER-BRIEF | Confirmed. Supersedes proposal A-08 (withdrawn). |
| R-02 | Networks are connected through shared Persons; no mandatory primary network; no parent/sub-network hierarchy. | RECONSTRUCTED | Confirmed. |
| R-03 | Cross-network paths are labelled at each transition (connecting Person, relationship type, branch context). | RECONSTRUCTED | Confirmed. |
| R-04 | Useful paths first; remaining paths on request; no valid path silently discarded. | RECONSTRUCTED | Confirmed. |
| R-05 | Incomplete or limit-stopped search is never proof of no relationship. | RECONSTRUCTED | Confirmed. |
| R-06 | Membership is separate from Person existence and connection; leaving keeps record and relationships; return needs the approved membership process. | RECONSTRUCTED | Confirmed. |
| R-07 | Person, Account, and membership are separate concepts. | RECONSTRUCTED | Confirmed (consistent with Q13, OQ-21-19). |
| R-08 | Phone-verification login; no separate mandatory 2FA in current scope. | RECONSTRUCTED | Confirmed. |
| R-09 | Session security: device/session list, login history, approximate location where appropriate, new-device notice, terminate one or all other sessions. | RECONSTRUCTED | Confirmed. |
| R-10 | Blocking, abuse reporting, impersonation reporting, independent appeal, in-app support centre. | RECONSTRUCTED | Confirmed; detail is design. |
| R-11 | Multi-country support from the beginning. | RECONSTRUCTED | Confirmed. |
| R-12 | No separate hierarchical community layer. | RECONSTRUCTED | Confirmed. |
| R-13 | Family subgroups; GEDCOM, Excel, CSV import (preview, duplicate suggestions, no automatic confirmation); personal backups; support centre. | RECONSTRUCTED | Confirmed (feature scope). |
| R-14 | Status colours: green = living active participant; blue = living, not participating or unregistered; white = deceased. Computed display; account and membership stored separately. | RECONSTRUCTED | Confirmed (display rule). |
| R-15 | Documents are for viewing and discussion; not authenticated; not legal proof. | RECONSTRUCTED | Confirmed (consistent with Q5, Q22). |
| R-16 | Rejected proposal reopened only with materially new information (OQ-21-18). | §3C.2 | Confirmed. |
| R-17 | No numerical voting thresholds are set by OQ-21-05. | §3C.2 | Confirmed. |
| R-18 | M0 and 22 fixtures immutable. | P17 | Confirmed. |

**Withdrawn:** proposal A-08 in `M3-AMENDMENTS-2026-11-03.md` (narrowing shared-relative discovery). The amendment file is kept unchanged as history.

**Still open (owner policy):** OQ-21-03 matrix; OQ-21-05 eligibility and procedure; one account with several Persons; authorized audit roles; sensitive accountless-change approval rule; C-R21-06 effective time; critical-notification exemption policy; CG-29 marriage and half-sibling policy.

**Legal or privacy review (not decided):** OQ-21-10 verification method; OQ-21-12 deceased privacy; Q7 audit retention and crypto-erase; deletion rules; login-location basis; country-specific marriage recognition; abuse-appeal procedure.

**Unverified:** Q24–Q96 and any later clarifications not in the brief. Not used as a basis for any design.

<!--M3-FINAL-3D-END-->

## 4. Unresolved matters — explicitly NOT decided


No answer is invented for any item below. They are recorded as `[UNRESOLVED]` and must remain open until direct owner evidence or a separately approved decision closes them.

| ID | Matter | Status / note |
|---|---|---|
| Q4 / OPEN-2 | Whether a finally rejected relationship may be resubmitted with new evidence | `[UNRESOLVED]` — no policy selected |
| Q6 / OPEN-4 | Detection and handling of multiple accounts belonging to the same real person | `[UNRESOLVED]` — distinct from Q10's duplicate person-record behavior |
| OPEN-16 | The specific technical mechanism and enforcement point for preventing biological cycles under concurrent writes | `[UNRESOLVED]` (mechanism) — the invariant (P16, owner-approved) stands; mechanism selection + executable concurrency tests remain engineering work (M3 planning / M8 execution); no mechanism is selected here |
| DR-30 / OPEN-19 | Identity verification beyond OTP: whether required, and who decides | `[UNRESOLVED]` — explicitly preserved by Q10; no identity-verification procedure is approved |
| DR-01, DR-06, DR-07, DR-09, DR-12, DR-13, DR-15, DR-16, DR-17, DR-18, DR-20, DR-21, DR-22, DR-23, DR-24, DR-25, DR-26, DR-27, DR-29, DR-30 | Decisions not covered by Q1–Q12 | `[UNRESOLVED]` / pending, except where engineering-deferred by existing documents |
| OPEN-5, OPEN-6, OPEN-7, OPEN-9…OPEN-20 | Other architecture OPEN items (e.g., KD-01/KD-02 naming and degree definition; key storage; hosting region; minor definitions; export/deletion rights) | `[UNRESOLVED]` — untouched by this register |
| DR-19 remainder | Pseudonymous audit identifier scheme and legal-linked deletion/key-destruction path | `[UNRESOLVED]` — awaits legal review; Q7 decided only its stated scope |
| OPEN-20 / DR-34 (proposal) | Abuse/rate-limit values and mechanism | `[UNRESOLVED]`/`[PROPOSED]` — baseline only |
| DR-32, DR-33, DR-34 | Proposal-only identifiers in `DECISION-REGISTER.md` §7 | `[PROPOSED]` — not decisions |

### 4A. Open matters from M2-R21 (OQ-21-xx)

Full analysis, options, and classification are in `M2-R21-OWNER-DECISION-CONSOLIDATION-AND-READINESS-REPORT.md`. Entries here are not decisions.

| ID | Open matter | Owner or technical | Blocking class |
|---|---|---|---|
| OQ-21-00 | **CLOSED in M2-R22** as a mapping of Q13–Q23 to owner confirmations (§3B). Residual, `UNVERIFIED`: verbatim text and dated provenance of the M2-R20 messages are not recovered | Owner | Closed (mapping); residual is not blocking |
| OQ-21-01 | **CLOSED in M2-R22** (§3B.2, option C): each network has its own acceptance state; provenance kept; no forced decisions across networks. Whether accepted links enter the canonical biological set is NOT part of this closure and is covered by OQ-21-16 | Owner | Closed |
| OQ-21-02 | **CLOSED in M2-R22** (§3B.2, option C): results may differ by network; each uses its adopted set; M0 algorithm unchanged. The M0 wording reading is open as OQ-21-16. The FR-018 / §5.1 rewording is tracked in the M2-R22 amendment (C-R21-03) | Owner + technical | Closed (decision); wording follow-up under OQ-21-16 |
| OQ-21-03 | **PARTLY RESOLVED in M2-R24** (§3C.2, option D): eligibility from confirmed relationships and network boundaries; personal control; specific grants or denials; no automatic access to a relative's whole network. **Open:** the detailed matrix by relationship type and branch, including in-laws and sibling marriages (conceptual design item) | Owner + technical design | Partly resolved; matrix blocks only the visibility feature |
| OQ-21-04 | Whether a non-responding party can block a bilateral association, and the expiry rule (Q14, C-R21-01) | Owner | CAN BE RESOLVED DURING M3 |
| OQ-21-05 | **PARTLY RESOLVED in M2-R24** (§3C.2, option D): principle only; no numerical percentages set; eligibility, evidence weight, objections, abstentions, and non-responses to be defined per decision type and risk. **Open:** the numerical thresholds, after the governance design | Owner | Partly resolved; numbers follow governance design |
| OQ-21-06 | **CLOSED in M2-R22** (§3B.2, option C): each network decides adoption independently; adopting networks use the new relationship; rejecting and unreviewed networks keep their previous adopted relationship; history preserved | Owner | Closed |
| OQ-21-07 | **PARTLY RESOLVED in M2-R24** (§3C.2, option D): configurable daily limits, batching, and review queues; important pending requests stay accessible when suppressed or grouped. **Open:** numerical limit values (no value selected) | Owner | Partly resolved; values deferred |
| OQ-21-08 | **RESOLVED at principle level in M2-R24** (§3C.2, option C): bulk approval only for complete, eligible, low-risk items; sensitive, disputed, and incomplete items excluded; each item keeps its own decision and audit entry. Exact eligibility criteria are a feature-design item | Owner | Resolved (principle); criteria at feature design |
| OQ-21-09 | Reopening: effect on network-specific state and canonical state (Q21) | Owner | CAN BE RESOLVED DURING M3 |
| OQ-21-10 | **PARTLY RESOLVED in M2-R24** (§3C.2, option B): OTP verifies a phone number only; linking an account to an existing Person requires additional reliable verification, with method, result, and provenance recorded, and an alternative review path. **Open:** the verification method itself (legal/privacy assessment and technical design; DR-30 / OPEN-19) | Owner + legal/privacy review | Partly resolved; method REQUIRES LEGAL / PRIVACY REVIEW before production |
| OQ-21-11 | Evidence and provenance data model for accountless and deceased Persons (Q22) | Technical (M3) | CAN BE RESOLVED DURING M3 |
| OQ-21-12 | **PARTLY RESOLVED in M2-R24** (§3C.2, option C): death does not make sensitive information public; sensitive information remains protected; access rules for deceased Persons to be designed; living people in a deceased Person's record remain protected. **Open:** the access-rule design and the legal/privacy assessment before production | Owner + legal/privacy review | Partly resolved; REQUIRES LEGAL / PRIVACY REVIEW before production |
| OQ-21-13 | Shared-connection signals permitted for suggestions without exposing restricted data (Q13, Q14) | Owner + technical | CAN BE DEFERRED TO A LATER PHASE |
| OQ-21-14 | **CLOSED in M2-R22** (§3B.2): seven separate technical layers approved. Residual: storage of historical or alternative lineage narratives is not yet decided (see OQ-21-17) | Owner | Closed (layers); residual under OQ-21-17 |
| OQ-21-15 | Numerical matching thresholds for same-person detection (D13, D5). Deliberately not set by the owner; must remain open until the matching design defines what is compared | Owner + technical design | CAN BE RESOLVED DURING M3 (must be decided before suggestion behaviour is implemented) |
| OQ-21-16 | **CLOSED in M2-R23** (§3B.4, option B, `OWNER-DIRECT-EVIDENCE`): biological parentage adopted independently within each network; M0 unchanged; "biologically confirmed" means adopted under that network's rules. Snapshot mechanism is NOT part of this closure (§3B.5, `AGENT-PROPOSAL`) | Owner | Closed |
| OQ-21-17 | Storage model for historical or alternative lineage narratives as a layer separate from canonical biological data | Owner + technical design | CAN BE RESOLVED DURING M3 |
| OQ-21-18 | **DECIDED (owner, M2-R24; §3C.2):** a rejected proposal may be reopened when new evidence or a material new reason becomes available; the original rejection remains preserved. Source of the decision: M2-R24 brief (conversation) | Owner | Closed |
| OQ-21-19 | **DECIDED (owner, M2-R24; §3C.2):** one Person may be associated with multiple accounts over time; only one account may be active for a Person at a time; recovery and transfer require reliable verification and audit. Source of the decision: M2-R24 brief (conversation) | Owner | Closed (principle); verification method is OQ-21-10 |

Nothing in this register converts a `[PROPOSED]` item, a derived `[INTERPRETATION]`, or an engineering recommendation into an approved owner decision.

---

## 5. Traceability

| Decision | Evidence source (owner, direct) | Resolves / affects | Reconciliation targets |
|---|---|---|---|
| P1–P17 | M1-A, M1-C, M1-E acceptance (session `1793525922711_rqjpo`); M2-R12 evidence matrix | — (principles) | This register §2 |
| Q1 | M2-R14/M2-R15 owner review (this register §3) | DR-02, DR-28; P1–P4 | `06-DECISIONS-REQUIRED`, `09-MASTER-ARCHITECTURE`, `15-UNRESOLVED-CONTRADICTIONS` |
| Q2 | same | DR-02, DR-03, TECH-012/013 | `03/04/06/09/15` |
| Q3 | same | OPEN-1 | `06/09/15` (+ FR-020 semantics) |
| Q5 | same | OPEN-3, FR-018 | `06/09/15` |
| Q7 | same | OPEN-8, DR-19 (partial) | `06/09/15` (+ PRV-009) |
| Q8 | same | OPEN-21, DR-11 | `06/09/15` (+ FR-004) |
| Q9 | same | DR-04, SEC-004 | `06/09/15` (+ SEC-010) |
| Q10 | same | DR-05, SEC-002, PRV-002/006/010, FR-014/016/030, GOV-001/008, identity model | `03/04/05/06/09` |
| Q11 | same | DR-31, CG-43 | `06/09/15` (+ GOV-013); gate pending |
| Q12 | same | registration act | `00/01/07/09/11/13/15/16/README` |
| Q13 | M2-R21 owner brief (see §3A evidence limitation) | Extends Q10B/Q10C; no conflict found | `03` (FR-048 note), `09` §3, `15` (M2-R21) |
| Q14 | same | Bilateral association and branch-limited visibility; potential tension with P6 (C-R21-01) | `03` (FR-014/016/030 note), `09` §3/§7/§9, `15` (M2-R21) |
| Q15 | same | Conflicts with single-network model of P5, Q3, `09` §5.3 (C-R21-02) | `09` §5.3, `15` (M2-R21) |
| Q16 | same | Conflicts with FR-018 and `09` §5.1 single state field (C-R21-03) | `03` (FR-018 note), `09` §5.1, `15` (M2-R21) |
| Q17 | same | Consistent with PRV-007, GOV-006; timing open (C-R21-06, OQ-21-06) | `09` §8.3, §12.1, `15` (M2-R21) |
| Q18 | same | Consistent with GOV-003 | `03` (GOV-003 note), `09` §12.2 |
| Q19 | same | Values deferred (OQ-21-05) | `09` §14 |
| Q20 | same | Notification bypass conflict open (C-R21-05) | `03`, `09` §10, `15` (M2-R21) |
| Q21 | same | Consistent with Q1, Q3, FR-035, FR-046; interaction open (OQ-21-09) | `09` §8 |
| Q22 | same | Consistent with P8, P15, Q5, Q10B | `09` §3.2 |
| Q23 | same | Consistent with GOV-006; safeguards open (OQ-21-08) | `09` §5 |

The authority hierarchy for decision content is: this register (decision text) → owner decision messages (evidence) → other documents (descriptions to be reconciled).

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-11-02 | Register created (M2-R15). Records P1–P17 and owner decisions Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12 with `OWNER-DIRECT-EVIDENCE`; records unresolved matters explicitly. Arabic working draft archived externally (hash above) as historical reference. |
| 2026-11-02 | M2-R24: product-scope reset recorded as a superseding product-scope statement (§3C.1), with P1, Q2, and M0 preserved unchanged. Owner decisions OQ-21-03, 05, 07, 08, 10, 12 recorded (§3C.2) with partial-resolution status where a detailed design remains. OQ-21-18 and OQ-21-19 recorded as owner decisions (§3C.2). Historical rows kept. No M0, fixture, or Arabic source changed. |
| 2026-11-02 | M2-R23: OQ-21-16 recorded as `OWNER-DIRECT-EVIDENCE` (§3B.4, option B); M0 interpretation recorded without modifying M0; calculation-snapshot mechanism recorded as `AGENT-PROPOSAL` (§3B.5); OPEN-2 and OPEN-4 analysed with new owner questions OQ-21-18 and OQ-21-19 (§3B.6). Q11 gate NOT executed: no independent AI or human review artifact found in the workspace or Temp (M2-R23 search). M3 gate per Q11 remains open. No P1–P17, Q1–Q12, M0, or fixture entry changed. |
| 2026-11-02 | M2-R22: owner confirmations supplied in the M2-R22 brief mapped to Q13–Q23 (§3B, OQ-21-00 closed as a mapping, residual `UNVERIFIED`); OQ-21-01, OQ-21-02, OQ-21-06, OQ-21-14 recorded as owner decisions (§3B.2); OQ-21-15…17 opened (§4A); C-R22-01 recorded (§3B.3). No P1–P17, Q1–Q12, or M0 entry changed. |
| 2026-11-03 | M3 final reconciliation: §3D added (R-01…R-18, `RECONSTRUCTED-FROM-OWNER-BRIEF`; no transcript recovered). Proposal A-08 (shared-relative narrowing) withdrawn; H-09 treated as answered (essential). No P1–P17, Q1–Q23, OQ entry, M0, fixture, or Arabic source changed. Q24–Q96 remain UNVERIFIED. Reconciliation: `m3-review/FINAL-OWNER-DECISION-RECONCILIATION*.md`. |

| 2026-11-02 | M2-R21: owner decisions stated in the M2-R21 brief registered as Q13–Q23 (§3A, all `OWNER-APPROVED-CLAIM` pending OQ-21-00) and open matters OQ-21-00…OQ-21-14 (§4A). No P1–P17 or Q1–Q12 entry changed. Evidence limitation recorded: the M2-R20 messages are not in the workspace; the M2-R21 brief is the registered source. Amendment notes added to `03`, `09`, `15`, and `README`. Arabic sources, M0, fixtures, and `CLAUDE.md` unchanged. |