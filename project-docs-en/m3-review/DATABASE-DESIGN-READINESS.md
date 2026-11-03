# Database Design Readiness (Part 1 of 2): Design Only, No Schema

**Status: DESIGN PROPOSAL. Not approved. This document creates no tables, SQL, or migrations.**
**Gate:** the Q11 independent AI review, the independent human engineer review, and owner approval must occur before M3-C (physical schema) and before any production migration (`DECISIONS.md` §3 Q11; `M3-03` §4). None of those gates has been passed.
**Date:** 2026-11-03. **Continuation:** `DATABASE-DESIGN-READINESS-PART2.md` (RLS, lifecycle, indexes, test plan).

---

## 1. Source rules this design respects

| Rule | Source |
|---|---|
| Current state is authoritative; audit is append-only; state and audit change in one transaction | Q1, P2, P3 |
| Original parent-child links are the only source of biological lineage; derived structures must be reproducible and keep all M0 path and parent-role information; a shortest-depth closure is insufficient | Q2, P1, M0 |
| At most one adopted father and mother per child, per network state | P14 |
| No fictitious Person for an unknown parent | P15 |
| No biological cycles | P16 |
| Adoption is per network; the M0 algorithm is unchanged | OQ-21-01, OQ-21-02, OQ-21-16 |
| Marriage, nursing, adoption, and guardianship are separate from parentage and excluded from M0 | P9, P10, Q2, GOV-011, GOV-012 |
| Account and Person are separate; one active account per Person; old accounts not deleted | Q13, OQ-21-19 |
| RLS is mandatory from the first build, together with application authorization | Q9, P12 |
| Standard supported cryptography only; keys managed, not embedded | P13, Q10A |

---

## 2. Concept-to-table mapping (proposed; resolves L-01)

| Concept (`M3-01` §2) | Proposed table | Notes |
|---|---|---|
| 1 Person | `persons` | Stable `person_id` independent of accounts. Phone and national ID optional. Sensitive fields encrypted. |
| 2 Proposal | `proposals`, `proposal_evidence` | Contributor and status history. Evidence is never a confirmation by itself (Q5). |
| 3 Account association | `accounts`, `account_person_links` | Association history; one active link (§4). |
| 4 Biological parentage, one network | `adopted_parentage` | One row per (network, child, role) adopted. Term chosen for L-01. |
| 5 Network adoption | `network_decisions` | One network's decision on one proposal. |
| Networks | `family_networks`, `network_memberships` | Membership is not parentage. |
| 6 Derived kinship | `kinship_results` (optional cache, §6) | Never stored as truth. |
| 7 Visibility | `visibility_settings` | Per field and group. Default deny. |
| Audit | `audit_events` | Append-only (Part 2 §8). |
| Marriage and affinity (H-10) | `relationship_edges` with `edge_kind` | Kinds: `marriage`, `affinity`, `nursing`, `legal_guardianship`. Separate from `adopted_parentage`. |

---

## 3. Marriage, affinity, and nursing (H-10)

- **Separate store.** These edges are rows in `relationship_edges`, never in `adopted_parentage`. The M0 engine reads only `adopted_parentage` for a network. Part 2 §10 defines the test.
- **Mixed paths.** A path that crosses a marriage edge carries the edge label at each transition.
- **Nursing** is a distinct `edge_kind` with a distinct visual representation (P10). It never enters biological or inheritance calculation.
- **Marriage lifecycle (technical proposal):** start date, end date, status. Several marriages per person are allowed (FR-008); the table must not preclude this.
- **Not decided (owner policy):** legal validity of a marriage; polygamy and half-sibling models (CG-29); the in-law visibility matrix (OQ-21-03). Marriage does not create biological relationship.

---

## 4. Concurrency controls for biological invariants (H-05)

Invariants: (i) at most one adopted father and one adopted mother per (network, child); (ii) no cycle in a network's adopted graph; (iii) at most one active account per Person; (iv) at most one active Person per account (technical default, see `M3-R1-RESOLUTION-MATRIX.md` H-02).

**A row lock on the child row is NOT sufficient by itself.** (a) A cycle spans several rows (an ancestor chain), so locking one child does not serialize two inserts on different children that together form a loop. (b) Two concurrent inserts for the same child and role can both see "no row" and both succeed if nothing that exists is locked.

Candidate mechanisms (for comparison; none selected):

| Option | Mechanism | Duplicate father or mother | Cycle | Cost and risk |
|---|---|---|---|---|
| A | Partial unique index on `(network_id, child_id, role)` where `state = 'adopted'` | Prevented by the database | Not prevented | Cheap; the last line of defence. |
| B | Transaction-scoped advisory lock keyed by `network_id` before any adopted-graph write | Serialized | Serialized, if the cycle check runs after the lock | Coarse per network; simple. |
| C | `SERIALIZABLE` isolation with retry on serialization failure | Prevented | Prevented | Needs a retry policy under contention. |
| D | Recursive cycle check in the same transaction over the adopted graph | Not applicable | Detected | Cost grows with ancestor depth. |

**Proposed combination to evaluate (not approved): A + B + D.** C is the fallback if B is too coarse.

**Required proof (H-05):** a concurrency test on a real PostgreSQL instance with at least two sessions: (i) two fathers for one child; (ii) a cycle formed by two inserts; (iii) two active accounts for one Person. A test on one connection is not evidence. Status: NOT VERIFIED (no database exists).

**Single active account (OQ-21-19 rule 2):** partial unique index on `account_person_links(person_id)` where `is_active`. The account-side index (one active Person per account) depends on owner answer H-02.
