# M3-03 — MVP Scope, Open-Item Classification, and Roadmap (Conceptual)

**Status:** planning document. **Not owner-approved.** Derived from `DECISIONS.md` (including §3C) and the M3 documents `M3-01` and `M3-02`.
**Language:** English.

---

## 1. Practical MVP (first release)

### 1.1 In scope
| Capability | Basis | Notes |
|---|---|---|
| Registration and login (OTP) | FR-001, OQ-21-10 | OTP proves phone control only |
| Person profiles | FR-002, FR-005, Q13 | Stable Person ID; phone and national ID optional |
| Adding parents, siblings, children, and relatives | FR-004, FR-006, FR-007 | Creates Person records and proposals |
| Suggesting existing Person records | FR-014, FR-048, D5 | Authorized fields only; no name-only matching |
| Preventing unsafe automatic merges | D5, Q13 | Flags only; no automatic merge |
| Sending and reviewing family connection requests | FR-016, FR-017, Q14 | Bilateral association before wider visibility |
| Viewing confirmed family connections | FR-028, OQ-21-16 | Shown as adopted within the network |
| Discovering shared relatives | FR-014, OQ-21-03 | A discovery signal, not a confirmed relationship |
| Understanding kinship relationships | FR-021 to FR-026; M0 | M0 unchanged; path shown |
| Basic privacy settings | Q10A, PRV-011–013 | Per-field; default deny for matrix cases |
| Notifications and review queue | Q20, OQ-21-07 | Batching; important items stay accessible |
| Basic audit visibility | Q1, P2, OQ-21-19 | Own-change history |

### 1.2 Deferred to later releases
| Capability | Reason not in the first release |
|---|---|
| Full correction workflow for confirmed parentage | First release may record corrections as new proposals; full workflow once networks hold confirmed parentage at scale |
| Full reopening workflow for rejected proposals | Basic rejection and notification suffice for first use |
| Specialist and elder participation | Governance thresholds not designed (OQ-21-05); not needed for discovery |
| Historical or alternative lineage narratives | OQ-21-17; not needed for discovery |
| Evidence attachments beyond a source note | OQ-21-11; a source note suffices initially |
| Breastfeeding display category | Deferred (P10) |
| Adoption | Outside the current release (P9) |
| Advanced visibility matrix (in-laws, sibling marriages) | OQ-21-03 design; first release uses default deny |
| Advanced bulk approval | OQ-21-08 criteria; first release uses individual decisions |
| Web client | DR-01; mobile first |

### 1.3 Why deferring these is safe
- Individual decisions per network are safe without numeric thresholds, because each item is reviewed on its own.
- Historical narratives are a separate layer (OQ-21-14). Their absence does not change any calculation.

---

## 2. Open-item classification

Classes: **A** blocks conceptual design; **B** blocks one feature only; **C** must be complete before production; **D** engineering responsibility; **E** optional or later release.

| ID | Plain meaning | Status | Class | Blocks | Provisional design | Must be resolved by |
|---|---|---|---|---|---|---|
| OQ-21-03 | Who sees what in relatives' networks | Principle decided (D); matrix open | B | Visibility feature | Default deny; confirmed relationships plus personal settings | Before visibility feature |
| OQ-21-04 | What if the other person never replies to a link request | Open | B | Association feature | Stays pending; reminder; expiry leads to extension, never to acceptance | Before association feature |
| OQ-21-05 | How many approvals a decision needs | Principle decided; numbers open | B | Governance feature | Individual network decisions in the first release | Before governance feature |
| OQ-21-07 | How many notifications per day | Principle decided; numbers open | B | Notification settings | Configurable; no fixed value; queue always accessible | Before notification feature |
| OQ-21-08 | Which items may be bulk-approved | Principle decided; criteria open | B | Bulk approval | Not offered in the first release | Before bulk feature |
| OQ-21-09 | Effect of reopening on adoption state | Open | B | Reopen workflow | Reopening creates a new review item; adopted state unchanged until a new decision | Before reopen feature |
| OQ-21-10 | How a real-world identity is verified for linking to an existing Person | Principle decided (B); method open | C | Linking to existing Persons | Alternative review path; method, result, provenance recorded | Before production; design before linking feature |
| OQ-21-11 | How evidence and sources are stored | Open | D | Evidence storage | Source and contributor fields only | Before evidence feature |
| OQ-21-12 | Privacy rules for deceased persons | Principle decided (C); design and legal review open | C | Deceased-person records | Protected by default; no public access after death | Before production |
| OQ-21-13 | Shared-connection signals for suggestions | Open | E | Suggestion quality | Authorized, explicit links only | Later release |
| OQ-21-15 | Numeric thresholds for same-person matching | Deliberately not set | D (with review) | Suggestion tuning | Suggest on authorized fields; never auto-merge | Before suggestion feature |
| OQ-21-17 | Storage of historical lineage narratives | Open | E | Narrative layer | Not in the first release | Later release |
| DR-30 / OPEN-19 | Whether extra identity verification is required generally, and who decides | Open | C (legal) | Verification policy | As OQ-21-10 | Before production |
| OPEN-16 | Technical mechanism that prevents biological cycles under concurrent writes | Open (mechanism) | D | Integrity enforcement | Enforced at write; tested under concurrency | Before database build is accepted |

**Decided in M2-R24 (not open):** OQ-21-18 (reopening rule) and OQ-21-19 (account rules). Their remaining details are design items: the reopening procedure (D) and the account recovery procedure (D, with the verification method under C).

**Process gate, not a feature:** the Q11 independent review (§4).

---

## 3. Roadmap (phases, separate from the MVP list)

| Phase | Objective | Exit gate |
|---|---|---|
| M3 conceptual design | `M3-01`, `M3-02`, `M3-03` | Conceptual review package prepared; reviews pending |
| M3-B design verification | Compare storage alternatives against M0 path requirements; define equivalence tests | Equivalence test plan accepted by reviewers |
| M3-C physical schema design (design only) | Tables, keys, RLS, indexes, migration and rollback plan | Independent schema review; owner approval |
| M4 database foundation | Schema and RLS in a test environment; concurrency tests | Tests pass; owner acceptance |
| M5 relationships and adoption | Connections, proposals, per-network adoption, audit | Tests pass |
| M6 discovery and notifications | Suggestions, shared relatives, review queues | Tests pass |
| M7 kinship engine | M0 per network; fixture harness | All 22 fixtures pass unchanged |
| M8 privacy, verification, pilot readiness | Privacy tests; legal and privacy review complete | Owner approves pilot |

A pilot follows M8 only after owner approval. Planning, architecture, implementation, verification, and pilot are separate gates.

---

## 4. Review gates

- The Q11 gate (independent AI review and independent human review, then owner approval) applies before physical schema approval and before production implementation (`DECISIONS.md` §3, Q11).
- Conceptual design may proceed without the human review, as the owner authorized.
- No review is claimed in this document. Review status is in the M2-R24 report.


