# M3-02 — Privacy, Visibility, Evidence, Audit, and Correction (Conceptual)

**Status:** M3 conceptual design draft. **Not owner-approved.** No table, column, migration, policy, or code is defined here.
**Language:** English.
**Governing decisions:** `DECISIONS.md` Q1–Q3, Q5, Q7, Q9, Q10A, Q13, Q15, Q17, Q21–Q23, OQ-21-03, OQ-21-05, OQ-21-07, OQ-21-08, OQ-21-10, OQ-21-12, OQ-21-18, OQ-21-19, and §3C.
**Companion:** `M3-01-DOMAIN-MODEL.md`.

---

## 1. Privacy and family visibility (concept 7)

### 1.1 Approved rules
- The person controls visibility of each personal field (Q10A, PRV-011). Fields include phone number, workplace, residence, map location, and other optional information.
- Visibility may be granted to selected people, to kinship-group settings, or to nobody (PRV-012). Kinship-group settings are enforced server-side, not only in the interface.
- Sensitive information is encrypted at rest with managed keys. Matching uses a separate keyed lookup, and no plaintext searchable copy is kept (Q10A; DR-05 decided).
- Private information is not exposed in duplicate suggestions unless the viewer is authorized (PRV-013).
- Seeing a relative in another person's network does not grant access to all of that relative's network (OQ-21-03, option D).
- Death does not make sensitive information public. Living people appearing in a deceased person's record remain protected (OQ-21-12, option C).

### 1.2 Open design item (OQ-21-03)
The visibility matrix by relationship type and branch, including in-laws and sibling marriages, is not complete. The conceptual rule is **default deny**: access derives from confirmed relationships plus explicit personal settings. The matrix must be written before the visibility feature is built.

### 1.3 Authorization boundaries
- Application-level authorization is mandatory for every read and write. The client is never trusted (P12; `09` §2.2).
- Row-level security is an additional database layer that works consistently with application authorization (P12, Q9). Its policies are designed in M3-C, not here.
- Access to a person's sensitive fields is a separate permission from knowing that the person exists in a network.

---

## 2. Evidence and provenance (proportionate level)

- Every claim (a Proposal, an adopted parentage, or a Person detail) records its **source** and **contributor** (Q22).
- Evidence types may include family testimony, documents, historical records, knowledgeable relatives, and specialist review (Q22). Each item is recorded with its origin.
- Evidence is supporting information, stored separately from confirmation status. It does not itself determine confirmation (Q5).
- A specialist may recommend and review. A specialist cannot decide biological parentage alone (Q18, Q22).
- Identity verification and biological-parentage verification remain separate (Q22, Q13).
- Evidence weight and governance procedure are shown next to each adopted fact (OQ-21-16). The evidence data model is OQ-21-11, a technical follow-up for M3.

**Proportionality:** discovery does not require legal-grade evidence chains. Each claim needs a source and a contributor. Governance depth scales with the decision's risk (OQ-21-05).

---

## 3. Audit and history (supporting concept 6)

- Audit history is append-only and is not deleted by ordinary application functions (P2, Q7, FR-046).
- Each change records who, when, the change type, the information affected, and the old and new values (Q1).
- Audit is written in the same transaction as the state change it records (P3).
- Current state is the operational source of truth; the audit trail is the immutable history (Q1, P4: no full event sourcing).
- Audit retention is indefinite, subject to legal and privacy review (Q7). The pseudonymous audit identifier and any deletion or key-destruction path are open for legal review.
- Account association, unlinking, recovery, and transfer are audited (OQ-21-19, rule 5).
- History of rejected and reopened proposals is preserved (OQ-21-18, Q21).

---

## 4. Correction and reopening lifecycle

- A correction to an adopted parentage is a separate, stricter workflow (Q17). The previous relationship remains intact while the correction is reviewed.
- Each network independently adopts or keeps the correction (OQ-21-06, OQ-21-16). A network with no completed review does not change automatically.
- No automatic deletion, suspension, or replacement occurs because a correction was proposed (Q17).
- Reopening a rejected proposal requires new evidence or a material new reason. The original rejection is preserved (OQ-21-18).
- Reconsideration requests are screened for seriousness and grounds. An unsupported request does not reopen every decision (G5).
- Objections are recorded and do not automatically change adoption (Q3, G3).

---

## 5. Notifications and review queues

- Notifications go to relevant people only, not to everyone (Q20).
- Configurable daily limits, batching, and review queues are supported (OQ-21-07, option D). No numerical limit is selected.
- Important pending requests stay accessible through the review queue even when notifications are suppressed or grouped (OQ-21-07).
- Confirmed additions and items requiring a decision are separate categories (Q20).
- An expired response period is neither acceptance nor rejection (G4, Q20).
- Bulk approval is permitted only for complete, eligible, low-risk items. Sensitive biological relationships, disputed items, and incomplete items are excluded. Each item keeps its own decision and audit entry (OQ-21-08, option C).
- **Open (feature design):** the eligibility criteria for bulk approval and the numerical limits. Neither blocks conceptual design.

---

## 6. Security boundaries

- Authentication uses OTP for phone control (FR-001; OQ-21-10). OTP alone does not establish the identity of a real-world person.
- Standard, supported cryptography only. Key recovery and backup are documented before production (P13).
- Sensitive data is encrypted. Keys are managed, not embedded in code (Q10A, P13).
- Abuse and rate-limit values are `[PROPOSED]` and owned by engineering (DR-34 / OPEN-20). No value is approved here.
- No unrestricted administrator view of family data. Operator access is limited and audited (`09` §2.1; DR-26 open for operations).

---

## 7. Data integrity and concurrency

- At most one adopted biological father and one adopted biological mother per child, within each network's state (P14).
- No biological cycle within a network's adopted graph (P16). The enforcement mechanism under concurrent writes is an engineering decision (OPEN-16). It must be tested under concurrency before production.
- An unknown parent is absent, not a fictitious Person record (P15).
- At most one active account per Person (OQ-21-19, rule 2). This must be enforced under concurrency, not only by the interface.
- A relationship change in one network does not write to another network's adopted state (OQ-21-01).

---

## 8. Performance considerations (conceptual)

- Path enumeration cost grows with overlapping pedigrees (`08` §F). Path enumeration must have explicit limits.
- A truncated search must never display "no kinship" (`08` §F item 3).
- Per-network calculation is independent, so results may be cached per network and per adopted-input version, once an equivalence test passes (`M3-01` §8.4).
- Discovery suggestions use indexed, authorized fields only. The performance target is an engineering decision.

---

## 9. Items deliberately not designed here

- Physical table and column definitions; RLS policy text (M3-C).
- The verification method for linking an account to an existing Person (OQ-21-10; legal and privacy review).
- Eligible-reviewer rules and numerical thresholds (OQ-21-05).
- The visibility matrix for in-laws and sibling marriages (OQ-21-03).
- The storage choice for the ancestry structure (`M3-01` §8.4; a technical decision for M3-02).


