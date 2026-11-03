# Consolidated Owner-Decision Register, Part 1A: DD-01 to DD-20

**Parent:** `OWNER-DECISION-REGISTER-CONSOLIDATED.md`. **Provenance of every row:** `DIRECTIVE-2026-11-03` (owner statement in the final directive; no transcript recovered).

| ID | Decision | Consistency note |
|---|---|---|
| DD-01 | Family discovery, acquaintance, and kinship exploration platform; not a legal genealogy, civil, religious, or scientific authority; issues no legally binding proof of lineage. | `DECISIONS.md` §3C.1 |
| DD-02 | Confirmed, proposed, disputed, incomplete, and rejected relationships are distinguishable; suggestions never presented as fact; network-accepted relationships are not universal facts. | Q15, OQ-21-16 |
| DD-03 | PostgreSQL system of record; NestJS REST API; Flutter client; modular monolith; no MVP microservices; Redis optional, justified only when needed. | Architecture notes |
| DD-04 | Separate concepts: Account, Person, Network, Relationship, Proposal, Evidence/document, Audit record. | Q13, Q16 |
| DD-05 | Person may exist without Account; deceased and never-registered people are ordinary Person records; no merge on name similarity; identity matching, account verification, Person matching, and relationship confirmation are separate. | Q13, D5 |
| DD-06 | No primary network; a Person may be the intersection of several networks; one consistent identity when the system has sufficient grounds. | R-02, Q15 |
| DD-07 | Visibility in one network grants no access to another; network-accepted relationships do not become globally confirmed; cross-network discovery never bypasses authorization. | OQ-21-01, OQ-21-03 |
| DD-08 | At most one confirmed father and one mother per child; no fictitious unknown parent; no biological cycles; concurrent writes cannot bypass these; changes follow proposal and governance; all changes audited. | P14–P16 |
| DD-09 | The biological graph is the source of truth for biological kinship. Marriage, affinity, adoption, and nursing are distinct and never change biological kinship. | P9, P10, Q2 |
| DD-10 | Marriage is a separate record with optional dates and status; no legal or religious validity judgment; half-siblings represented through a shared confirmed biological parent; no inference of shared parentage from marriage, surname, or label. | Directive §17.8 |
| DD-11 | Adoption is outside MVP. Nursing is a distinct category excluded from biological and inheritance calculations. | P9, P10 |
| DD-12 | M0 and its 22 fixtures are immutable without explicit owner authorization; path information, parent roles, valid junction pairs, and counts preserved. | P17 |
| DD-13 | Shortest-depth closure alone is insufficient. Raw path-count multiplication that includes invalid overlapping pairs is prohibited. | Q2 |
| DD-14 | Distinguish: no relationship in a completed search; search incomplete at a technical boundary; proposed or disputed paths; confirmed paths within a network. An incomplete search is never shown as absence. | R-05 |
| DD-15 | Current state authoritative for ordinary reads; audit append-only; state and audit in one transaction; no Event Sourcing; both parties participate where applicable; no unilateral veto; objections recorded and evaluated through the network; objection alone does not suspend a confirmed relationship; evidence and status separate; creator does not own a Person; sensitive changes need extra controls; no single elder or specialist establishes lineage; audit retained indefinitely subject to law; rejections keep their reasons. | Q1, Q3, Q5, Q8, Q15, Q18, Q22 |
| DD-16 | Rejected proposals resubmitted only with materially new information; earlier decision preserved; resubmission is not an appeal that reverses the decision. | OQ-21-18 |
| DD-17 | No fixed approval percentages or numerical voting thresholds. Governance is risk-based with configurable parameters covering eligibility, conflicts of interest, abstention, non-response, evidence, objections, additional review, and audited final results. | OQ-21-05, R-17 |
| DD-18 | A Person may have several Accounts over time; only one active; old accounts not auto-deleted; recovery and transfer need reliable verification and audit; concurrent transfers protected. | OQ-21-19 |
| DD-19 | OTP verifies phone control, not identity. Linking an existing Person needs an additional verification whose method, result, time, and source are recorded. Uncertain matching never silently creates or merges Persons. Phone change never creates a new Person. Phone is not a mandatory profile field. | OQ-21-10, Q13 |
| DD-20 | Personal fields (phone, workplace, residence, map location, other) are optional where appropriate and protected separately from graph visibility. Per-field visibility; selected individuals, all eligible relatives, or kinship-degree groups where supported; minors and living people in deceased records protected; death does not make sensitive data public. | Q10A, OQ-21-12 |
