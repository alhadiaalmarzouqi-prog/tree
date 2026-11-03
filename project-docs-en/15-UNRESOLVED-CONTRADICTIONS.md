# Unresolved Contradictions and Owner Decisions

**Purpose:** Register of all contradictions and decisions that must remain open. Nothing here is resolved or adjudicated by this documentation set.
**Scope:** OPEN-1…OPEN-4 (mission-critical), DR-02/DR-28, D-01…D-10, M1-E, and the documented conflict list.
**Status:** Draft.
**Source references:** `05-CONFLICTS-AND-GAPS.md`, `06-DECISIONS-REQUIRED.md`, `07-DECISION-EVIDENCE-REGISTER.md`, `09-MASTER-ARCHITECTURE.md`.
**Last verified:** 2026-11-01.

## 1. Mission-critical open issues (must remain visible)

### OPEN-1 — Effect of objections on confirmed biological relationships
- **Substance:** does an active objection immediately suspend a network-confirmed link from the biological calculation?
- **Alternatives (presented, not selected):** (a) immediate suspension; (b) the link remains in the calculation until a new network decision.
- **Advantages/risks:** immediate suspension is safer against wrong calculation but can be gamed by objections; keeping the link avoids that but risks counting contested links.
- **Consequences:** directly changes engine inputs (M5 depends on this — see `09-MASTER-ARCHITECTURE.md` §15), and the state/audit model.
- **Status:** OPEN — owner decision required. The architecture does not choose. `[OA-claimed: M1-E §3.1]` (unverifiable).

### OPEN-2 — Reconsideration of rejected relationships
- **Substance:** can a rejected link be resubmitted when new evidence becomes available?
- **Status:** OPEN — owner decision required. The transition Rejected → Awaiting confirmation is **not approved**. The document assumes neither that resubmission is possible nor that new evidence is mandatory or sufficient.

### OPEN-3 — Independent evidence representation
- **Substance:** is "supported by independent evidence" (FR-018) (a) a relationship state, (b) a separate evidence record/attribute, or (c) a hybrid?
- **Status:** OPEN — owner decision required; FR-018's wording is preserved unchanged. The only representable-now option (evidence as bound data, not changing state) is `[P]`.

### OPEN-4 — Multiple accounts belonging to one person
- **Substance:** how multiple accounts of one person are identified and handled is unresolved. No solution is assumed. The only permitted architectural phrasing ("internal person identifier; multiple accounts not counted more than once") is `[P]`, a description, not a solution.
- **Status:** OPEN — owner decision required.

## 2. DR-02 / DR-28 — relationship state and audit history

- **Conflict:** DR-02 makes current confirmed biological links the sole source; DR-28 makes an append-only event log the basis. `DECISION-REGISTER.md` §4: "the two cannot be adopted together as written."
- **What the architecture source claims:** current state is the source and audit is history, labeled OWNER-APPROVED — **unverifiable** (M1-E missing); the same source says the DR-28 rewording awaits editing.
- **Distinction preserved:** (a) current authoritative relationship state; (b) immutable historical audit records; (c) derived ancestor/descendant structures.
- **Status:** CONFLICTED, not resolved. A proposed resolution exists in `DECISION-REGISTER.md` §4 (event log as full source; current table and Closure Table derived in-transaction) but is `[P]` and needs explicit owner approval.

## 3. M1-E — missing decision evidence

- The M1-E report is not in the project; 38 references to it exist. The **70** OWNER-APPROVED labels in the Arabic source corpus (all in `MASTER-ARCHITECTURE.md`, 0 elsewhere in the Arabic sources; re-verified in M2-R9) are claims, not verified approvals; no approval dates found; `DECISIONS.md` was absent — **[superseded M2-R15:** the register now exists at `project-docs-en/DECISIONS.md`].**
- Effect: decision traceability for the entire owned-principles layer is blocked until the owner provides the report or a verifiable equivalent. The report has **not** been manufactured.

## 4. D-01…D-10 — reported contradictions without repository identifiers

- The mission reports a contradiction register D-01…D-10. The project files contain **zero** occurrences of these identifiers.
- The previously reported contradiction descriptions are **not available in the project**; they cannot be restated from repository evidence and are not discarded silently — this register records their absence explicitly.
- Candidate documented contradictions in the project, listed for owner confirmation of mapping (not asserted as the D-xx content):
  - CG-01 RLS timing (spec §13 vs. privacy principles)
  - CG-02 Closure Table vs. ancestor helper table
  - CG-03 age of majority undefined
  - CG-04 mutual confirmation vs. independent evidence
  - DR-02 vs. DR-28 primary source
  - FR-010 adoption support vs. deferral (MASTER-ARCHITECTURE §16.2)
  - CG-28 dispute mechanism vs. GOV-003 no single authority
  - CG-42 900 vs. 700 line limit
- **No new D-xx identifiers were created.** Any mapping requires the owner’s original register.

## 5. Other documented conflicts (retained)

| ID(s) | Conflict | Status |
|---|---|---|
| CG-28 | no single authority (GOV-003) vs. required dispute mechanism | OPEN (DR-10, DR-26) |
| FR-010 vs. deferral | adoption requested in spec vs. adoption out of MVP scope | OPEN until spec amendment |
| CG-42 | 900-line task text vs. 700-line newer rules | OPEN until owner confirms 700 |
| PLAN-007 | two instruction versions; longer prompt treated as newer authority | OPEN (owner review) |
| PRV-007 vs. correction need | no direct modification vs. required correction mechanism | OPEN (DR-10, DR-28) |
| SEC-004 vs. DR-04 | RLS phase 6 vs. phase 1 | OPEN |
| CG-40 | minimal registration vs. discovery accuracy | OPEN |

## 6. Rule

None of the items above may be silently resolved by a later design document (M3+). Each requires either an explicit owner decision, or the disappearance of the conflict through verifiable evidence. This register is the review gate for that rule.
---

## M2-R15 Amendment — 2026-11-02

Owner decisions Q1–Q12 (see `DECISIONS.md`) resolve the following items; the text above remains historical.

- **OPEN-1 — resolved by Q3.** An active objection does not automatically remove a confirmed biological relationship from kinship calculations; it remains included until the network decides. Record the objection (author, date, evidence); expose the disputed status to authorized viewers; no unilateral invalidation.
- **OPEN-3 — resolved by Q5.** Independent evidence is supporting information stored separately from the confirmation status and linked to the relationship; it does not itself determine confirmation.
- **§2 (DR-02 / DR-28) — resolved by Q1/Q2.** Current confirmed relationships are the source of truth; the audit is an immutable history (not the state source); no full Event Sourcing; full reconstruction not required; derived structures are reproducible and preserve all path/parent-role information required by M0. The proposed resolution recorded in §2 is superseded.
- **§3 — updated.** `DECISIONS.md` now exists at `project-docs-en/DECISIONS.md` (see the inline note). The M1-E reporting gap itself is unchanged.
- **Remaining unresolved (unchanged):** OPEN-2, OPEN-4, OPEN-16 (mechanism), DR-30/OPEN-19, and every item in §5 not otherwise resolved above.

## M2-R21 Amendment — 2026-11-02 — owner decisions Q13–Q23 and conflicts

The owner decisions in the M2-R21 brief are registered in `DECISIONS.md` §3A (Q13–Q23, `OWNER-APPROVED-CLAIM` until OQ-21-00 is closed). The open matters are in `DECISIONS.md` §4A. The items below are conflicts and unresolved points. None is resolved by this amendment.

| ID | Conflict or issue | Relevant sources | Status |
|---|---|---|---|
| C-R21-01 | Bilateral association (Q14) could be read as a participation right that conflicts with P6 "no individual veto". Lineage veto and association veto are different things. | DECISIONS P6, Q14 | Potential. OQ-21-04 |
| C-R21-02 | Network-specific acceptance (Q15) conflicts with the single-network majority model (P5, Q3, `09` §5.3 eligibility and majority). | DECISIONS P5, Q3, Q15; `09` §5.3 | CONFLICTED. Owner decision required (OQ-21-01) |
| C-R21-03 | Layered model (Q16) conflicts with the single state sequence in FR-018 and `09` §5.1. | DECISIONS Q1, Q16; `03` FR-018; `09` §5.1 | CONFLICTED. Owner decision required (OQ-21-02) |
| C-R21-04 | M0 §B.1(3) uses one set of biologically confirmed links. If an accepted branch can make a link count for its own calculation, two results for the same pair would conflict with M0. M0 is not changed. | `08` §B.1, §C.4–C.7; Q2 | CONFLICTED with a viewer-scoped reading. Owner decision required (OQ-21-02) |
| C-R21-05 | Notification limits (Q20) could delay a mandatory high-risk correction notice. | DECISIONS Q17, Q20 | Open. OQ-21-07 |
| C-R21-06 | Correction review (Q17) is consistent with PRV-007 and GOV-006. The effective time of a replacement is not stated in any source. | DECISIONS Q17; `09` §8.3, §12.1 | Not a conflict. Timing open (OQ-21-06) |

- **Reviewed and found consistent (no conflict):** Q13 with P8, P15, Q5, Q10B, Q10C; Q18 with GOV-003; Q19 (values not set); Q21 with Q1, Q3, FR-035, FR-046; Q22 with P8, P15, Q5; Q23 with GOV-006.
- **Pre-existing, unchanged:** OPEN-2, OPEN-4, OPEN-16, DR-30/OPEN-19.

## M2-R22 Amendment — 2026-11-02 — status of C-R21-01…06 and new conflict C-R22-01

Sources: `DECISIONS.md` §3B (owner confirmations and OQ-21-00 disposition) and §4A. Each row states the status after M2-R22. Status words: **Resolved** = closed by an owner decision; **Partly resolved** = owner decision covers part, residual stated; **Open** = not decided.

| ID | Conflicting requirements | Resolved by M2-R22? | Remaining | Blocks M3? | Minimum needed to close |
|---|---|---|---|---|---|
| C-R21-01 | P6 "no individual veto" vs. Q14 bilateral association | Partly resolved. P6 concerns lineage; Q14 concerns association. D13 requires bilateral confirmation before wider visibility | Non-response rule and expiry (OQ-21-04) | No. Does not change the canonical graph | Owner rule on non-response |
| C-R21-02 | P5, Q3, `09` §5.3 (one majority per link) vs. Q15 and OQ-21-01 (per-network acceptance) | Partly resolved. OQ-21-01 approves independent per-network acceptance. **Not resolved for the canonical biological set** (whether accepted links enter the global calculation input) | Canonical-input rule (OQ-21-16) and rewording of `09` §5.3 | **Yes** (through OQ-21-16) | Owner reading of "biologically confirmed" (OQ-21-16) |
| C-R21-03 | FR-018 and `09` §5.1 one state sequence vs. Q16 seven layers | Partly resolved. OQ-21-14 approves seven separate layers. The FR-018 and §5.1 wording is not yet amended | Amending FR-018 and `09` §5.1 wording; state-ownership table (conceptual, not schema) | Yes, as a documentation prerequisite for M3 | Documentation amendment in M3 planning; no schema decision required now |
| C-R21-04 | M0 §B.1(3) "biologically confirmed" vs. OQ-21-02 per-network results | Partly resolved. OQ-21-02 approves per-network results and states M0 is unchanged. The M0 wording reading is **open** | Reading of "biologically confirmed" (C-R22-01, OQ-21-16) | **Yes** | Owner reading (OQ-21-16) |
| C-R21-05 | Q20 notification limits vs. Q17 high-risk correction notices | Open. Q20 and G-decisions do not state an exemption | High-risk notice exemption (OQ-21-07) | No, not for the schema. Yes for the notification feature | Owner rule on exemption |
| C-R21-06 | Q17 correction vs. effective date | **Resolved** by OQ-21-06 (option C) | None for this item. Residual: the review-state representation is part of M3 design | No | Done. Representation is a design item (TI-22-04) |

**New conflict:**

- **C-R22-01 — M0 §B.1(3) "biologically confirmed" vs. OQ-21-02 per-network results.** M0 §B.1(3) states that biological calculations use only biologically confirmed links. The owner has approved per-network kinship results with M0 unchanged. The wording does not say whether "biologically confirmed" is global or per network. Status: `CONFLICTED` (wording). Blocks M3 through OQ-21-16. Not resolved by changing M0.

**Other items noted in this review:**

- `09` §7.4 RLS timing was marked `[OPEN]`. Q9 approved RLS from the start of database design. The stale statement is marked superseded in `09` (M2-R22). It is documentation-only.
- OPEN-2 (rejected → awaiting resubmission) and OPEN-4 (multiple accounts) are unchanged. See `DECISIONS.md` §4 and the M2-R22 report.

## M2-R23 Amendment — 2026-11-02 — OQ-21-16 and final contradiction status

- **C-R22-01 (M0 §B.1(3) "biologically confirmed") — RESOLVED** by OQ-21-16 option B (`DECISIONS.md` §3B.4, `OWNER-DIRECT-EVIDENCE`). M0 unchanged; the term means "adopted under that network's rules". Residual: the eligible-participant and threshold rules (OQ-21-05) and snapshot mechanism (§3B.5, `AGENT-PROPOSAL`), which do not change the M0 reading.
- **C-R21-04 (M0 vs. network-dependent results) — RESOLVED** by OQ-21-16 with OQ-21-02. Each network applies M0 to its own adopted graph (`09` §19).
- **C-R21-02 (single-network model) — ACCEPTANCE RESOLVED** by OQ-21-01 and OQ-21-16. `09` §5.3 carries an M2-R22 note; `09` §19 states the per-network rule. Documentation consistency is not yet checked across `02` glossary "Network-Confirmed Link" and `03` FR-017/FR-018 wording (see M2-R23 report).
- **C-R21-06 (correction timing) — RESOLVED** by OQ-21-06 (`DECISIONS.md` §3B.2) and consistent with OQ-21-16.
- **C-R21-03 (seven layers vs. single status sequence) — DECISION RESOLVED** by OQ-21-14. Documentation amendment of `03` FR-018 and `09` §5.1 wording remains open (see M2-R23 report, M3 documentation prerequisite).
- **C-R21-01 (bilateral association vs. P6) — PARTLY RESOLVED.** Non-response rule remains open (OQ-21-04, `CAN_BE_DEFERRED`).
- **C-R21-05 (notification limits vs. high-risk notices) — OPEN.** OQ-21-07.
- **OPEN-2 — OPEN, owner question OQ-21-18** (`DECISIONS.md` §3B.6). Unchanged in status.
- **OPEN-4 — OPEN, owner question OQ-21-19** (`DECISIONS.md` §3B.6). Unchanged in status.
- **Q11 independent review — NOT EXECUTED** (`DECISIONS.md` §3 Q11).

## M2-R24 Amendment — 2026-11-02 — product-scope reset and reclassified open items

- **Product-scope reset (`DECISIONS.md` §3C.1):** the platform is primarily a discovery and family-connection platform, not a legal or scientific lineage authority. This supersedes the legal-grade framing of earlier product-scope statements. P1, Q2, and M0 are preserved; the reset changes the proportionality of governance and evidence work, not the calculation source of truth.
- **OPEN-2 — DECIDED (OQ-21-18, §3C.2).** The conflict in `09` §5.2 (Rejected → Awaiting confirmation "not approved") is resolved by the owner decision: a rejected proposal may be reopened on new evidence or a material new reason, with the original rejection preserved. `09` §5.2 is to be amended in M3-A to reflect this. Status changed from OPEN to DECIDED.
- **OPEN-4 — DECIDED in principle (OQ-21-19, §3C.2).** One Person may have several accounts over time, only one active at a time; recovery and transfer need reliable verification and audit. The verification method remains OQ-21-10. Status changed from OPEN to DECIDED in principle.
- **OQ-21-08 — RESOLVED at principle level** (bulk approval, option C).
- **OQ-21-03, OQ-21-05, OQ-21-07, OQ-21-10, OQ-21-12 — PARTLY RESOLVED.** Principles are decided; detailed matrices, numerical values, and the verification method remain open as listed in `DECISIONS.md` §4A.
- **C-R21-05 (notification limits vs. high-risk notices)** is partly addressed: OQ-21-07 now requires that important pending requests remain accessible even when notifications are suppressed or grouped. The numerical limits and the exemption wording remain open.
- **C-R21-01 (bilateral association vs. P6)** remains partly resolved; non-response rule open (OQ-21-04).
- **Q11 independent review** remains NOT EXECUTED (unchanged).