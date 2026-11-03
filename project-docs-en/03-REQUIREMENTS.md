# Requirements — Sovereign Lineage Platform

**Purpose:** English reconstruction of the extracted requirements, preserving all identifiers and source references.
**Scope:** All 114 requirements extracted from the original specification and planning task, as recorded in `project-docs/analysis/REQUIREMENTS.md`.
**Status:** Draft — reconstructed from `project-docs/analysis/REQUIREMENTS.md` (verified: 114 unique IDs). Not owner-approved.
**Source references:** `project-docs/analysis/REQUIREMENTS.md` (the extraction authority). The original specification "Sovereign Lineage Platform — Version 1.0" and the planning-task text are NOT present in the project (`01-MISSING-EVIDENCE.md` ME-04/ME-05).
**Related documents:** `04-TRACEABILITY-MATRIX.md`, `05-CONFLICTS-AND-GAPS.md`, `02-GLOSSARY.md`.
**Last verified:** 2026-11-01.

## 1. Conventions

- Each requirement has a stable identifier (FR, PRV, SEC, GOV, TECH, DATA, PERF, OPS, TST, SCOPE, PLAN). Identifiers are never renumbered or redefined.
- Citations in parentheses refer to sections of the original specification (§) as recorded in the source.
- "Uncertain": the source notes that the specification did not fix the detail; see `05-CONFLICTS-AND-GAPS.md` and `06-DECISIONS-REQUIRED.md`.
- Counts were verified programmatically against the source: 114 unique IDs (FR-43, PRV-10, SEC-9, GOV-12, TECH-14, DATA-3, PERF-3, OPS-6, TST-5, SCOPE-2, PLAN-7).

## 2. Functional requirements (FR)

| ID | Requirement | Source |
|---|---|---|
| FR-001 | Register users and verify phone numbers by OTP code | §9, §12-1 |
| FR-002 | Create person records | §12-2, §4.1 |
| FR-003 | Separate the person record from the user account | §4.1, Principle 1 of the task text |
| FR-004 | Represent unregistered relatives within limited-permission family records | §4.1, §9, §12-3 |
| FR-005 | Support person states: registered user, unregistered, deceased, incomplete data | §4.1 |
| FR-006 | Record father and mother relationships | §4.2, §12-4 |
| FR-007 | Support full and half siblings (sharing one parent) | §4.2, §13 Phase 2 |
| FR-008 | Support more than one marriage for one person | §13 Phase 2 |
| FR-009 | Represent marriage and in-laws as a relationship type separate from blood kinship | §4.2, §13 Phase 4 |
| FR-010 | Support adoption as an independent relationship type | §4.2 |
| FR-011 | Support breastfeeding (milk kinship) as a relationship type (uncertain: "if decided to support later") | §4.2 |
| FR-012 | Record "family acquaintance without proven lineage" as an independent relationship type | §4.2 |
| FR-013 | Automatic linking: infer relationships from documented relationships without unjustified generalization | §4.3 |
| FR-014 | Suggest people likely related to the user based on specific search elements | §5, §12-5 |
| FR-015 | Show the reason for every suggestion (shared grandfather name similarity, family match, documented common relative, possible path) | §5 |
| FR-016 | User response options: confirm acquaintance, confirm kinship, specify its type, acquaintance without type, reject, report an error | §5 |
| FR-017 | Verification cycle: proposal → first party approval → second party confirmation request → type and path determination → comparison → additional endorsement when missing or conflicting → adoption → audit recording | §6 |
| FR-018 | Relationship states: proposed, awaiting confirmation, confirmed by both parties, supported by independent evidence, disputed, rejected | §6 |
| FR-019 | Handle rejection, dispute, and correction requests with a defined mechanism | §6, §10-9, §13 Phase 3 |
| FR-020 | Prevent a rejected, pending, or disputed relationship from being counted as confirmed kinship | §13 Phase 3, §10-4 |
| FR-021 | Kinship calculation engine between any two registered people however many intermediaries | §7 |
| FR-022 | Determine the nearest common ancestor, the number of generations, and whether the kinship is from the father's or mother's side | §7 |
| FR-023 | Detect more than one kinship path between two people when present | §7 |
| FR-024 | Calculate kinship up to the tenth degree (uncertain: behavior beyond it) | §12-9 |
| FR-025 | Generate a clear Arabic description of the relationship | §7, §12-10 |
| FR-026 | Display the actual kinship path instead of only a degree number | §7 |
| FR-027 | Dictionary of Arabic and Libyan kinship terms accounting for dialects and branches | §7, §13 Phase 4 |
| FR-028 | Interactive kinship network showing the user at center | §8, §12-11 |
| FR-029 | Home page: count of documented relatives, suggestions, confirmation requests, latest links, notifications | §8 |
| FR-030 | Search for a person by name or phone number per privacy rules | §8, §12-12 |
| FR-031 | Show the family path connecting the user to a search result | §8 |
| FR-032 | Classify relatives: father's relatives, mother's relatives, siblings, paternal cousins, maternal cousins, distant relatives, in-laws | §8, §13 Phase 5 |
| FR-033 | Zoom in/out of the network and load it progressively | §8 |
| FR-034 | Notifications and confirmation requests | §12-13, §11 |
| FR-035 | Audit record for significant operations | §12-14, §10-7 |
| FR-036 | User management of privacy and permissions | §12-15, §10-6 |
| FR-037 | Record the modification history of relationships | §13 Phase 2 |
| FR-038 | Prevent impossible relationships and incorrect cycles in lineage | §13 Phase 2 |
| FR-039 | Add ancestors and forebears gradually without requiring a full tree at registration | §9 |
| FR-040 | Registration with minimal data and without complexity | §9 |
| FR-041 | Show the person's displayable data and their relation to the user when clicked | §8 |
| FR-042 | Suggestions screen and verification-requests screen | §13 Phase 5 |
| FR-043 | Profile and relatives list | §13 Phase 5 |

## 3. Privacy requirements (PRV)

| ID | Requirement | Source |
|---|---|---|
| PRV-001 | A person who disables visibility does not appear in others' suggestions | §10-1 |
| PRV-002 | Phone numbers are not shown to others | §10-2 |
| PRV-003 | Data of an unregistered person (or one who has not consented to be claimed) is not shown publicly | §10-3, §9 |
| PRV-004 | Pending contracts are not shown as confirmed relationships | §10-4, §16-5 |
| PRV-005 | Minors' data hidden by default (uncertain: definition of minor) | §10-5, §9 |
| PRV-006 | User controls which information is shown about them | §10-6 |
| PRV-007 | A confirmed relationship cannot be directly modified by the user | §10-8 |
| PRV-008 | Correction and dispute requests follow a defined mechanism | §10-9 |
| PRV-009 | Audit-record retention policy balancing audit, privacy, correction, and deletion rights | §10 (last paragraph) |
| PRV-010 | Phone number matching only with data subjects' consent and privacy-preserving means | §5 (item 6) |

## 4. Security requirements (SEC)

| ID | Requirement | Source |
|---|---|---|
| SEC-001 | Prevent unauthorized access between users | §13 Phase 6, Principle 10 of the task text |
| SEC-002 | Encrypt sensitive data | §10-10, §13 Phase 6 |
| SEC-003 | Protect access permissions at the database level | §10-10 |
| SEC-004 | RLS policies on PostgreSQL (uncertain: application timing) | §13 Phase 6 |
| SEC-005 | Sensitive view/modification operations are audited | §10-7 |
| SEC-006 | Access tests between users | §13 Phase 6 |
| SEC-007 | Review data paths and leakage | §13 Phase 6 |
| SEC-008 | Do not link a user account to another person's record merely because data is similar | §16-7 |
| SEC-009 | Protect unregistered persons from disclosure | §16-8 |

## 5. Governance and principles (GOV)

| ID | Requirement | Source |
|---|---|---|
| GOV-001 | No confirmed lineage relationship based only on name similarity | §16-2, §5 |
| GOV-002 | No automatic addition of relatives without a path proving the relationship | §4.3, §16-3 |
| GOV-003 | No family head, tribe chief, or supervisor with single authority over relationships | §6, §16-4, Principle 11 of the task text |
| GOV-004 | Disputed relationships are not shown as facts | §16-5 |
| GOV-005 | Every person has the right to control their data and privacy | §16-6 |
| GOV-006 | Any modification of a documented relationship is recorded and subject to a verification procedure | §16-9 |
| GOV-007 | Future features do not rebuild the kinship engine | §16-10 |
| GOV-008 | Name similarity is used to discover candidates only | §5 |
| GOV-009 | Network spread is automatic, but a relationship shown as confirmed rests on documented links | §4.3 |
| GOV-010 | Mutual agreement of the parties starts a relationship known to both, and is not absolute proof of lineage | §6 |
| GOV-011 | The biological relationship is the basis of the blood-kinship engine and is not mixed with other relationship types | §4.2 |
| GOV-012 | In-laws, adoption, and breastfeeding are calculated and displayed independently | §4.2 |

## 6. Technical requirements (TECH)

| ID | Requirement | Source |
|---|---|---|
| TECH-001 | Unified backend application and single database; no microservices initially | §11 |
| TECH-002 | Backend server: NestJS | §11 |
| TECH-003 | PostgreSQL is the single source of truth in the first phase | §11, §16-1 |
| TECH-004 | Mobile application: Flutter | §11 |
| TECH-005 | Web: Next.js "when needed" (uncertain: criterion for need) | §11 |
| TECH-006 | Search: PostgreSQL Full Text with Fuzzy Matching | §11 |
| TECH-007 | Cache: Redis "when needed" (uncertain: criterion for need) | §11 |
| TECH-008 | Notifications: Firebase Cloud Messaging | §11 |
| TECH-009 | Suitable graph library for Flutter or web | §11 |
| TECH-010 | Deployment: Docker and CI/CD | §11 |
| TECH-011 | Neo4j is not used initially | §11 |
| TECH-012 | Closure Table for storing ancestor and kinship relationships | §11, §13 Phase 4 |
| TECH-013 | Ancestor helper table to speed up kinship queries | §11 |
| TECH-014 | Store father/mother relationships and other relationships clearly and independently | §11 |

## 7. Data requirements (DATA)

| ID | Requirement | Source |
|---|---|---|
| DATA-001 | Proposed registration fields: first name, father's name, grandfather's name, family/surname, mother's name, phone number, sex (uncertain: which is mandatory) | §9 |
| DATA-002 | Optional fields: current city, date of birth (with special minor protection) | §9 |
| DATA-003 | Registration simple and not complex | §9 |

## 8. Performance requirements (PERF)

| ID | Requirement | Source |
|---|---|---|
| PERF-001 | The network does not stall at high person counts (progressive loading) | §8 |
| PERF-002 | Appropriate use for phones and weak networks | §13 Phase 5 |
| PERF-003 | Performance tests before launch | §13 Phase 7 |

## 9. Operational requirements (OPS)

| ID | Requirement | Source |
|---|---|---|
| OPS-001 | Execute the project through phases 0–7 with each phase's defined outputs | §13 |
| OPS-002 | Phase 0 produces: DECISIONS.md file, API specification, golden test cases, privacy rules | §13 Phase 0 |
| OPS-003 | Backups and monitoring before launch | §13 Phase 7 |
| OPS-004 | Final deployment | §13 Phase 7 |
| OPS-005 | Trial on a real family with participants' consent | §13 Phase 7 |
| OPS-006 | Time estimate (55–85 prompts, MVP in 6–10 weeks) is a non-binding planning estimate | §14 |

## 10. Testing requirements (TST)

| ID | Requirement | Source |
|---|---|---|
| TST-001 | Kinship accuracy tests | §13 Phases 4 and 7 |
| TST-002 | Multi-path tests | §13 Phase 7 |
| TST-003 | Verification and conflict tests | §13 Phases 3 and 7 |
| TST-004 | Registration, search, and privacy tests | §13 Phase 7 |
| TST-005 | Golden tests for kinship relationships | §13 Phase 4 |

## 11. Release scope (SCOPE)

| ID | Item | Status |
|---|---|---|
| SCOPE-001 | Deferred features: solidarity funds and money, full chat system, smart groups, voice/video calls, maps and migrations, voting and financial governance, advanced tribes and councils, end-to-end chat encryption | outside first release (§12) |
| SCOPE-002 | Platform future: inter-family networks, messaging, councils, events, history, maps, solidarity funds | outside current planning (§15) |

## 12. Planning-task requirements (PLAN)

| ID | Requirement |
|---|---|
| PLAN-001 | Permanent documentation allowing independent agents to execute phase by phase without relying on the conversation log |
| PLAN-002 | Each phase has an execution file containing: goal, scope, prerequisites, files, database changes, API changes, dependencies, tasks, security, tests, acceptance criteria, deliverables, definition of done, exceptions, transition blockers |
| PLAN-003 | Security requirements applied in every phase, not only phase 6 |
| PLAN-004 | After completing a phase: actual verification, running tests, updating status and log, execution report, and a handoff file for the next phase |
| PLAN-005 | The agent stops after completing its phase and does not start the next automatically |
| PLAN-006 | If a phase cannot be completed, report the blockers accurately without marking the phase complete |
| PLAN-007 | Two copies of the instructions exist in the conversation: the first release note (Plan) and the longer prompt (Master Planning). The conflict between them is undocumented; the longer prompt is considered the newer authority per the task text (related to CG-43) |

## 13. Statistics summary

| Category | Count |
|---|---|
| FR | 43 |
| PRV | 10 |
| SEC | 9 |
| GOV | 12 |
| TECH | 14 |
| DATA | 3 |
| PERF | 3 |
| OPS | 6 |
| TST | 5 |
| SCOPE | 2 |
| PLAN | 7 |
| **Total** | **114** |

## 14. Source notes

1. Some principles appear in both the specification and the task text (for example the account/person separation). Duplication is intentional for traceability and does not change the requirement.
2. The source notes that SEC-001 maps to Principle 10 in the task text and GOV-003 to Principle 11; the principle numbering in the task text does not match the PLAN numbering.
3. Requirements marked "uncertain" above retain that status. They are OPEN and addressed in `05-CONFLICTS-AND-GAPS.md` and `06-DECISIONS-REQUIRED.md`.
4. This English document is a reconstruction. The Arabic `REQUIREMENTS.md` remains the authority; identifiers and meaning were preserved, wording was not translated literally.
---

## 15. M2-R15 amendments — owner-decision-derived requirements (2026-11-02)

**Scope note:** the 114 identifiers in sections 2–12 are the Phase-B reconstruction (historical counts; §13). Owner decisions Q1–Q12 (see `DECISIONS.md`) add the decision-derived requirements below. Each is `OWNER-DIRECT-EVIDENCE`; the wording is the requirement form of the owner's decision, not a change of meaning. No existing identifier was renumbered or reused.

### New functional requirements (FR)

| ID | Requirement | Source |
|---|---|---|
| FR-044 | A confirmed biological relationship subject to an active objection remains included in biological kinship calculations until the network reaches a decision through the approved governance process; the objection (author, date, supporting evidence) is recorded and the disputed status is exposed to authorized viewers | Q3 |
| FR-045 | Independent evidence is stored separately from a relationship's confirmation status, linked to the relationship, with provenance and relevant metadata preserved; the presence or absence of independent evidence does not itself determine confirmation | Q5 |
| FR-046 | Audit history has no predefined automatic expiration; ordinary application functions must not delete audit records; access to audit records is permission-controlled | Q7 |
| FR-047 | Permissions for records of people without accounts: the creator manages permitted basic information; creation grants no unrestricted ownership or control over the person or their biological lineage; sensitive changes require additional authorization; biological confirmation and changes follow the approved network governance process; audit history and provenance are maintained; the creator does not automatically receive access to all sensitive personal information | Q8 |
| FR-048 | Duplicate-person detection and resolution: the same real person may be entered independently by multiple relatives and may later create their own account. On add: search plausible existing records; compare authorized information; present a candidate suggestion explained with authorized data; ask the user; link to the existing Person ID on confirmation (first record remains primary); preserve contributor/relationship provenance; allow a separate record when the suggestion is rejected; route ambiguous or conflicting cases to an appropriate review process instead of automatic merging; support a controlled association process when the person creates an account; preserve historical identifiers, source records, relationships, and audit history during any approved reconciliation | Q10C |

### New privacy requirements (PRV)

| ID | Requirement | Source |
|---|---|---|
| PRV-011 | Phone number, workplace, residence, and map location are optional profile information; the person controls the visibility of each field independently and may hide it or authorize selected relatives | Q10A |
| PRV-012 | Visibility policies support configurable kinship-degree groups (e.g., first, second, third degree; all eligible relatives) and are enforced server-side, not merely by UI hiding | Q10A |
| PRV-013 | Private information is not exposed during duplicate-person suggestions unless the viewer is authorized to see it | Q10A |

### New security requirements (SEC)

| ID | Requirement | Source |
|---|---|---|
| SEC-010 | RLS is designed and enabled from the beginning of database design and implementation; application authorization and database RLS operate together; tenant/user isolation and unauthorized direct database access are planned and tested; table ownership, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, and application database roles are explicitly examined | Q9 |
| SEC-011 | RLS is not claimed effective without executable security tests | Q9 |
| SEC-012 | Phone numbers and sensitive personal information are encrypted at rest with secure, independently managed encryption keys | Q10A |
| SEC-013 | A separate keyed HMAC mechanism provides exact phone-number lookup and matching; no plaintext searchable copy is stored | Q10A |

### New governance requirements (GOV)

| ID | Requirement | Source |
|---|---|---|
| GOV-013 | Before M3, the architecture is reviewed by BOTH an independent AI agent that did not prepare the reviewed documentation AND an independent human software engineer; their findings are compared, material disagreements resolved, and the owner approves the outcome | Q11 |
| GOV-014 | Similar names alone must never trigger automatic merging | Q10C |
| GOV-015 | A confirmed person-identity match does not automatically confirm a biological parent-child relationship | Q10C |
| GOV-016 | Different kinship descriptions do not prove that two records represent different real people | Q10C |

### New technical requirements (TECH)

| ID | Requirement | Source |
|---|---|---|
| TECH-015 | Audit records identify who performed each change and when, the change type, the affected information, and the old and new values; current state and its audit record are updated in the same transaction; full historical state reconstruction is not required | Q1 |
| TECH-016 | Original biological parent-child relationships are the sole source of lineage truth; ancestor tables, path data, and other derived structures are not independent sources, are reproducible from the original relationships, and preserve all path and parent-role information required by M0; a conventional Closure Table storing only shortest depth is not assumed sufficient | Q2 |

### New data requirements (DATA)

| ID | Requirement | Source |
|---|---|---|
| DATA-004 | `Account ID` identifies a login account; `Person ID` identifies a person record in the lineage network | Q10B |
| DATA-005 | A person may have a record without an account; a person may be represented by multiple independently created candidate records before duplicate resolution | Q10B |
| DATA-006 | A unique Person ID alone does not prove that two records represent different real people | Q10B |

### New operational requirement (OPS)

| ID | Requirement | Source |
|---|---|---|
| OPS-007 | The project maintains a formal `DECISIONS.md` register recording approved owner decisions with stable identifiers and traceable evidence; affected authoritative documents are updated so they no longer contradict approved decisions; historical documentation and change traceability are preserved; Arabic source and English documentation remain consistent | Q12 |

### Amendments to existing requirements (original rows preserved above)

- **FR-018:** "supported by independent evidence" is supporting information bound to the link (Q5), not a separate confirmation state; the original wording remains historical.
- **FR-020:** read together with Q3 — a link disputed solely because of an active objection on an already-confirmed link remains included in biological calculations until the network decides; non-confirmed states (proposed, awaiting, rejected, unresolved) are not counted.
- **SEC-004:** the timing uncertainty is resolved by SEC-010 (RLS from the beginning of database design/implementation); the "uncertain: timing of application" note is historical.
- **PRV-009 / FR-035:** read with FR-046/Q7 — no automatic expiration; application functions must not delete audit records; access is permission-controlled; legally defined privacy/deletion requirements remain subject to professional legal review.
- **FR-014 / FR-016:** person-suggestion and response behavior now includes the duplicate-person scenario in FR-048 (Q10C).

- **FR-018 (M2-R21, Q16):** the single state sequence in this row conflicts with the separation of relationship layers required by Q16. The wording is not amended until OQ-21-02 is answered (see `15-UNRESOLVED-CONTRADICTIONS.md`, M2-R21 amendment).
- **FR-014, FR-016, FR-048 (M2-R21, Q13, Q14):** identity matching is consistent with Q13. A suggestion is not a confirmed relationship and must not reveal restricted information. Discovery signals remain open (OQ-21-13).
- **FR-020 (M2-R21, Q15, Q16):** whether network-specific acceptance changes the biological inputs of kinship calculation is open (OQ-21-02). Until answered, FR-020 applies as written, with the Q3 reading.
- **FR-018 (M2-R22, OQ-21-14, OQ-21-01):** the seven-layer model separates the link lifecycle from network acceptance and identity association. The FR-018 wording is still not amended. Its single state list remains the historical wording until the M3 documentation amendment (C-R21-03).
- **FR-017 and FR-018 (M2-R23, OQ-21-01, OQ-21-16):** "second party confirmation" and "adoption" describe one network's decision. Each network adopts relationships independently (`DECISIONS.md` §3B.2, §3B.4). FR-017 applies per network. FR-018 as a single six-state list is superseded by the seven-layer model (OQ-21-14); its amendment is still an M3 documentation item.
- **FR-020 (M2-R22, OQ-21-02, OQ-21-16):** kinship results may differ between networks (OQ-21-02). Whether a network-adopted link counts as biologically confirmed under M0 §B.1(3) is OPEN (OQ-21-16). FR-020 is not amended.
- **GOV-003 (M2-R21, Q18):** specialists may suggest participants but have no unilateral authority over parentage. Consistent with this requirement.

**Statistics note:** §13's total of 114 refers to the Phase-B reconstruction. M2-R15 adds 22 decision-derived identifiers above (FR-044…FR-048, PRV-011…PRV-013, SEC-010…SEC-013, GOV-013…GOV-016, TECH-015…TECH-016, DATA-004…DATA-006, OPS-007).