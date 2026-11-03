# M3-R1 Resolution Matrix (Part B: H-06 to H-10, MEDIUM, LOW, M0 claims)

**Continuation of:** `M3-R1-RESOLUTION-MATRIX.md` (Part A). **Date:** 2026-11-03. **Status vocabulary:** as in Part A.

---

## 1. HIGH findings H-06 to H-10

### H-06 (HIGH): MVP correction path for adopted parentage undefined

- **Proposed resolution:** a correction is recorded as a proposal. The previously adopted parent stays adopted in that network until a network decision is recorded. At most one adopted parent per role exists in any network state.
- **Evidence:** `DECISIONS.md` Q17; OQ-21-06; C-R21-06 (effective time unstated).
- **Status:** BLOCKED by owner for the effective-time wording (C-R21-06).

### H-07 (HIGH): audit old/new values may expose hidden fields

- **Proposed resolution:** audit reads follow the same field-level visibility as current state. Sensitive audit values are stored encrypted under a separately controlled key. Ordinary users see only their own changes, plus controlled exceptions for authorized audit roles.
- **Evidence:** `DECISIONS.md` Q1, Q7, P2; `M3-02` §3.
- **Status:** BLOCKED by owner for the list of authorized audit roles. Legal review of crypto-erase is open (DR-19 remainder).

### H-08 (HIGH): path enumeration has no limit or truncated state

- **Proposed resolution:** a "truncated" result state, distinct from "no recorded kinship". A truncated result is never displayed as absence. The enumeration limit is a configuration value; no number is set here.
- **Evidence:** `08` §F item 3; the reviewer's synthetic benchmark (REPORTED, see §4).
- **Status:** NOT VERIFIED for performance. The limit needs measurement at M7.

### H-09 (HIGH): shared-relative discovery in MVP, but its signal is deferred

- **Proposed resolution:** the first release keeps only same-network, explicitly authorized, displayed relationships. Cross-network shared-relative discovery moves out of the first release until OQ-21-13 and C-01 are settled.
- **Caution:** the owner's brief lists shared-relative discovery as an essential capability. This narrowing is a scope proposal the owner must confirm; it is not a decision taken here.
- **Evidence:** `M3-03` §1.1 versus §2 (OQ-21-13, class E).
- **Status:** BLOCKED by owner confirmation.

### H-10 (HIGH): no marriage or in-law representation in the entity model

- **Proposed resolution:** marriage and affinity form a relationship kind separate from parentage. Each edge is labelled, and mixed paths keep those labels. Design: `DATABASE-DESIGN-READINESS.md` §3. Legal validity rules are NOT assumed.
- **Evidence:** `DECISIONS.md` Q2; FR-008 and FR-009 in `03-REQUIREMENTS.md`; CG-29 open.
- **Status:** the technical separation is proposed. Owner-policy items (marriage validity, polygamy, half-sibling rules, CG-29) are BLOCKED.

---

## 2. MEDIUM findings

| ID | Issue | Resolution | Status |
|---|---|---|---|
| M-01 | "No public access after death" vs per-field wording; "public" undefined. | Proposed definition: visible to any person outside the explicit visibility rules, including unauthenticated users. Default deny applies. | Proposed; needs owner confirmation. |
| M-02 | A notification limit can delay a high-risk correction notice. | Proposed: correction notices are never batched into a daily limit. | BLOCKED: OQ-21-07 / C-R21-05 exemption decision. |
| M-03 | RLS policies depend on undefined inputs (H-01, H-04, OQ-21-03). | Listed as RLS prerequisites in `DATABASE-DESIGN-READINESS-PART2.md` §7. | VERIFIED as listing; inputs remain open. |
| M-04 | Network boundary not connected to RLS. | `network_id` on each network-scoped row, with RLS consulting membership (`DATABASE-DESIGN-READINESS-PART2.md` §7). Test SEC-010 required. | Proposed; test NOT VERIFIED (no database). |
| M-05 | OQ-21-13 and OQ-21-15 wording not read in full by the reviewer. | Re-read: `DECISIONS.md` §4A OQ-21-13 ("CAN BE DEFERRED TO A LATER PHASE") and OQ-21-15 ("CAN BE RESOLVED DURING M3 ... must be decided before suggestion behaviour is implemented"). Both match `M3-03` §2. | VERIFIED. |
| M-06 | Bulk approval and notification rules need an undefined risk classification. | Not invented here. Bulk approval stays out of the first release (`M3-03` §1.2). | BLOCKED for feature design. |

---

## 3. LOW findings

| ID | Issue | Resolution | Status |
|---|---|---|---|
| L-01 | Terminology: "Biological relationship", "AdoptedParentage", "Network-Confirmed Link". | Mapping in `DATABASE-DESIGN-READINESS.md` §2; schema term `adopted_parentage`. | Proposed. |
| L-02 | `M3-04` §5 should say the AI review does not satisfy Q11. | Amendment proposed in `M3-AMENDMENTS-2026-11-03.md`. | Proposed. |
| L-03 | Cross-reference for evidence storage (OQ-21-11). | Cross-reference proposed in the amendment file. | Proposed. |
