# Decision Evidence Register

**Purpose:** Central register of every decision identifier and its evidence status. This register records evidence; it does not approve, reject, or create decisions.
**Scope:** DR-01…DR-34 (34 identifiers found in the project), KD-01/KD-02, and the labeled-but-unverifiable OWNER-APPROVED claims citing M1-E.
**Status:** Draft. No decision in this register is owner-approved. The M1-E report is missing (`01-MISSING-EVIDENCE.md` ME-01), so all owner-approval claims are unverified.
**Source references:** `project-docs/analysis/DECISIONS-REQUIRED.md`, `project-docs/analysis/DECISION-REGISTER.md`, `project-docs/MASTER-ARCHITECTURE.md`, `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md`, `project-docs/CLAUDE.md`.
**Related documents:** `06-DECISIONS-REQUIRED.md`, `01-MISSING-EVIDENCE.md`, `15-UNRESOLVED-CONTRADICTIONS.md`.
**Last verified:** 2026-11-01.

## 1. Status classes (mission §7)

| Class | Meaning | Present in this register |
|---|---|---|
| Approved principles | Owner-approved, with traceable evidence | **None verifiable** (M1-E missing; labels are claims only) |
| Technical proposals | Recommendations not approved | DR-01…DR-34 (all) |
| Open owner decisions | Require owner decision | OPEN-1…OPEN-21; all pending DRs |
| Deferred implementation | Explicitly deferred to a later phase; not a design decision | noted per DR |
| Rejected alternatives | Rejected in source (e.g., plain-text phones, direct vote on lineage) | within DR entries |
| Missing evidence | Evidence unavailable | M1-E, approval dates (`DECISIONS.md` was missing only in the pre-M2-R15 state; see §5 below) |

## 2. Decision identifiers found in the project

Found by text search (2026-11-01): DR-01…DR-34 (34 identifiers); KD identifiers (13 mentions of KD-01/KD-02); no PD or NG identifiers found; no D-01…D-10 identifiers found.

## 3. Status of each DR

| ID | Title (short) | Status | Evidence available | Blocks |
|---|---|---|---|---|
| DR-01 | Flutter only vs Flutter+Next.js | PROPOSED / OPEN | full DR text in `DECISIONS-REQUIRED.md` | Yes: 1, 5 |
| DR-02 | Closure Table / CTE / hybrid | PROPOSED / OPEN / CONFLICTED — **decided by Q1/Q2 (M2-R15)** | DR text; conflict with DR-28 in `DECISION-REGISTER.md` §4 | Yes: 0, 2, 4 |
| DR-03 | Closure Table = ancestor helper table? | PROPOSED / OPEN — **decided at principle level by Q2 (M2-R15); physical table choice remains DB design** | DR text | DB design |
| DR-04 | RLS timing | PROPOSED / OPEN — **decided by Q9 (M2-R15): RLS from the beginning of database design/implementation** | DR text; CG-01 | Yes: 0, 1 |
| DR-05 | Phone matching/masking | PROPOSED / OPEN — **decided by Q10A (M2-R15): encrypted at rest + keyed HMAC lookup** | DR text; CG-08, CG-34 | Yes: 1, 3 |
| DR-06 | Age of majority | PROPOSED / OPEN | DR text; legal review missing | Yes: 1 |
| DR-07 | Tenth-degree behavior | PROPOSED / OPEN | DR text; KD-02 open | Yes: 4 |
| DR-08 | Redis criterion | PROPOSED / OPEN (deferred) | DR text; CG-06 | No |
| DR-09 | Minimum for adopting a link | PROPOSED / OPEN | DR text; CG-04, CG-23 | Yes: 3 |
| DR-10 | Dispute resolution | PROPOSED / OPEN | DR text; CG-27, CG-28 | Yes: 3 |
| DR-11 | Unregistered-record ownership | PROPOSED / OPEN — **decided at principle level by Q8 (M2-R15)** | DR text; CG-25 | Yes: 1, 2 |
| DR-12 | Claim mechanism | PROPOSED / OPEN | DR text; CG-26 | Yes: 2 |
| DR-13 | In-law calculation | PROPOSED / OPEN | DR text; CG-17 | Yes: 4 |
| DR-14 | Adoption/breastfeeding/acquaintance | PROPOSED / OPEN | DR text; CG-15, CG-16 | Yes: 2, 4 |
| DR-15 | Multi-path ordering | PROPOSED / OPEN | DR text; CG-18 | Yes: 4 |
| DR-16 | Term dictionary | PROPOSED / OPEN | DR text; CG-20; KD-01 | Yes: 4 |
| DR-17 | Name matching | PROPOSED / OPEN | DR text; CG-21 | Yes: 3 |
| DR-18 | Notifying unregistered people | PROPOSED / OPEN | DR text; CG-36 | No |
| DR-19 | Audit retention / deletion | PROPOSED / OPEN — **decided in scope by Q7 (M2-R15); pseudonym/legal-deletion remainder open** | DR text; CG-31; legal review missing | Yes: 1 |
| DR-20 | Encryption & keys | PROPOSED / OPEN | DR text; CG-10 | Yes: 1 |
| DR-21 | Hosting & data region | PROPOSED / OPEN | DR text; CG-11; legal review missing | Yes: 0, 7 |
| DR-22 | OTP provider | PROPOSED / OPEN | DR text; CG-09 | Yes: 1 |
| DR-23 | UI language | PROPOSED / OPEN | DR text; CG-12 | No (affects 5) |
| DR-24 | Performance targets | PROPOSED / OPEN | DR text; CG-07, CG-37 | No (set before 7) |
| DR-25 | Real-family trial | PROPOSED / OPEN | DR text | Blocks 7 |
| DR-26 | Supervision role | PROPOSED / OPEN | DR text; CG-35 | Yes: 3 |
| DR-27 | Deceased status | PROPOSED / OPEN | DR text; CG-24 | Partially blocks 2 |
| DR-28 | History pattern / polygamy | PROPOSED / OPEN / CONFLICTED — **decided by Q1/Q2 (M2-R15) for the state-source conflict; marriage/polygamy representation portion remains design** | DR text; CG-27, CG-29, CG-30, CG-38; conflict with DR-02 | Yes: 2 |
| DR-29 | Unspecified sex | PROPOSED / OPEN | DR text; CG-19 | No (affects 4) |
| DR-30 | Identity beyond OTP | PROPOSED / OPEN | DR text; CG-33 | No |
| DR-31 | Independent review | PROPOSED / OPEN — **decided as a requirement by Q11 (M2-R15); review gate not yet executed** | DR text; CG-43 | Phase transitions |
| DR-32 | Offline work (proposal only) | PROPOSED (not in DECISIONS-REQUIRED) | `DECISION-REGISTER.md` §7 from CG-13 | — |
| DR-33 | Export/deletion rights (proposal only) | PROPOSED (not in DECISIONS-REQUIRED) | `DECISION-REGISTER.md` §7 from CG-32 | — |
| DR-34 | Abuse/rate limits (proposal only) | PROPOSED (not in DECISIONS-REQUIRED) | `DECISION-REGISTER.md` §7 from CG-34 | — |

## 4. KD identifiers

| ID | Item | Status |
|---|---|---|
| KD-01 | Kinship degree naming system | OPEN — not decided by mathematics (`KINSHIP-MATHEMATICAL-REFERENCE.md` §A.2; `MASTER-ARCHITECTURE.md` OPEN-6) |
| KD-02 | Definition of "tenth degree" | OPEN — not decided by mathematics (`MASTER-ARCHITECTURE.md` OPEN-5) |

## 5. OWNER-APPROVED labels: claims, not evidence

- The Arabic source corpus contains **70** occurrences of the label `OWNER-APPROVED`, all of them in `MASTER-ARCHITECTURE.md` and none in any other Arabic source file (re-verified in M2-R9); each cites M1-E items. Textual mentions inside this English set are documentation references, not source labels.
- The M1-E report is **MISSING**. No owner approval date, message, or record could be found (search for approval dates: 0 results).
- Per mission restrictions, these labels are recorded here as unverified claims and do not constitute traceable owner approval. Use in the architecture document is marked `[OA-claimed]` accordingly.
- `DECISIONS.md`, where approved decisions are to be registered per `CLAUDE.md`, now exists at `project-docs-en/DECISIONS.md` (created M2-R15, 2026-11-02); the "0 files" count refers to the pre-M2-R15 state.

## 6. Register rules

1. This register is updated only by evidence-backed changes: a new decision, a verifiable owner statement, or a decision status change. No entry may be marked owner-approved without the actual evidence.
2. Proposed identifiers DR-32, DR-33, DR-34 exist only as proposals in `DECISION-REGISTER.md`; their origin is documented there and in this table.
3. The D-01…D-10 identifiers are not in this register because no project file mentions them (see `15-UNRESOLVED-CONTRADICTIONS.md` for how their absence is handled).
---

## M2-R15 Amendment — 2026-11-02

- The register at `project-docs-en/DECISIONS.md` now records P1–P17 and owner decisions Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12 as `OWNER-DIRECT-EVIDENCE` (evidence per the M2-R12 conversation recovery and the M2-R13 briefing).
- Evidence classes preserved: the 17 principles remain `OWNER-DIRECT-EVIDENCE` at conversation level and `OWNER-APPROVED-CLAIM` inside repository files; registering them (Q12) preserves both classes while adding the formal record.
- §3 status table: DR-02, DR-03, DR-04, DR-05, DR-11, DR-19 (in part), DR-28, DR-31 → **decided** by owner Q1–Q12 (2026-11-02); OPEN-1, OPEN-3, OPEN-8 (in scope), OPEN-21 (principle) resolved. All other rows unchanged; none is marked owner-approved without the new evidence class.
- §5 statement on `DECISIONS.md`: updated inline — the register now exists.

---

## M2-R17 note — 2026-11-02

- The §3 status cells for DR-02, DR-03, DR-04, DR-05, DR-11, DR-19, DR-28, and DR-31 now carry inline markers pointing to the deciding owner decisions (Q1–Q12), so the table is unambiguous without reading the M2-R15 amendment below. The historical status wording is preserved; each marker states the current decided status per `project-docs-en/DECISIONS.md`. No row's substantive status was changed.
- §1 "Missing evidence" examples updated: `DECISIONS.md` is no longer missing (created M2-R15, 2026-11-02); the pre-M2-R15 absence is historical only.
- Unresolved items remain unresolved: Q4/OPEN-2, Q6/OPEN-4, OPEN-16 (mechanism), DR-30/OPEN-19, and every other row not marked decided above.
