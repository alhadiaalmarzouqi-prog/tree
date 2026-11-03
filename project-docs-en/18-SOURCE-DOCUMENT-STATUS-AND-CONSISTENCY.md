# 18 — Source Document Status and Consistency

**Purpose:** English-only record of (a) the Arabic/English consistency assessment required by the M2-R16 audit (D-2), (b) the verification of the README register-count figure (M-5), and (c) the governance clarification for reading Arabic source records against the English decision register.
**Status:** Completed by the M2-R17 documentation-correction agent, 2026-11-02. This document records status and classification only; it does not approve, amend, or resolve any owner decision, and it does not modify any Arabic source document.
**Scope:** The Arabic architecture source `project-docs/MASTER-ARCHITECTURE.md` (sections §7.4, §5.4, §3.4, §8.1, §16 item 5 as flagged by the M2-R16 audit, plus the related §13 OPEN table and adjacent statements touched by Q1–Q12); `project-docs-en/DECISIONS.md`; and the reconciled English documents.
**Source references:** `project-docs/MASTER-ARCHITECTURE.md` (Arabic, preserved); `project-docs-en/DECISIONS.md`; `project-docs-en/README.md`; `project-docs-en/03-REQUIREMENTS.md`; `project-docs-en/05-CONFLICTS-AND-GAPS.md`; `project-docs-en/06-DECISIONS-REQUIRED.md`; `project-docs-en/07-DECISION-EVIDENCE-REGISTER.md`; `project-docs-en/09-MASTER-ARCHITECTURE.md`; `project-docs-en/15-UNRESOLVED-CONTRADICTIONS.md`.
**Language:** English. No Arabic source file was created, edited, or moved for this assessment.
**Last verified:** 2026-11-02.

---

## 1. Governance clarification — Arabic sources and the English decision register

The following clarification is recorded here and in `README.md` §7 (M2-R17, 2026-11-02):

1. The original Arabic documents under `project-docs/` are **preserved source records**. They are not modified by the English documentation set and are not edited without explicit owner authorization (`00-SOURCE-MANIFEST.md` §7).
2. `project-docs-en/DECISIONS.md` is the **current decision register** for decisions recorded in the English documentation workflow (created M2-R15, 2026-11-02). Current decision status is determined from the register and the reconciled English documents, subject to the evidence rules in `DECISIONS.md` §1.
3. A statement in an Arabic source reflects the state at the time that source was written. **A historical statement in an Arabic source must not automatically be interpreted as the current project status.** Where a later recorded owner decision (Q1–Q12) supersedes an Arabic statement, the current status is the one recorded in the register and the reconciled English documents.
4. The English documentation preserves **traceability to the Arabic source** (`13-SOURCE-TO-ENGLISH-TRACEABILITY.md`).
5. This clarification does **not** authorize changing the meaning of an Arabic source, does **not** invent missing owner-approval evidence, and does **not** convert proposals into decisions. Where a decision's approval evidence is unavailable, the matter remains unverified/open.

**Canonical source paths.** The project contains exactly one master-architecture source: `project-docs/MASTER-ARCHITECTURE.md` (SHA-256 `AE1DCD6CDC0A4DDCB8D8BAE5DA39653625AC2C841EE721AAD8B96B9D500CC9E8`, 54,332 bytes, 470 physical lines — unchanged, verified 2026-11-02). The path `project-docs/analysis/MASTER-ARCHITECTURE.md` **does not exist** in the project tree; the M2-R16 audit's canonical reference is the root-level `project-docs/MASTER-ARCHITECTURE.md`.

---

## 2. Classification legend

Each Arabic statement below is classified as exactly one of:

| Classification | Meaning |
|---|---|
| HISTORICAL | The statement described the state at the time the Arabic source was written; it is accurate for that time and no later decision addresses it. |
| SUPERSEDED | A later, recorded owner decision (Q1–Q12, 2026-11-02) or a documented act (M2-R15 register creation) resolves or changes the matter; the current decision register and its evidence support this conclusion. |
| ACTIVE CONFLICT | The Arabic statement and the current English register both claim authority and cannot both be true today; no recorded decision resolves it. |
| NO CONFLICT | The Arabic statement remains consistent with the current English register and the actual status of the decision/open item. |
| UNVERIFIED | The decision's approval evidence is unavailable; no conclusion about approval is drawn. |

Rule: an Arabic statement is labelled SUPERSEDED only when the current register (`DECISIONS.md` §2–§3) and its recorded evidence support that conclusion. Where approval evidence is unavailable, the matter is labelled UNVERIFIED, never approved.

---

## 3. README register-count verification (M-5)

**Claim audited:** `README.md` §6 (pre-M2-R17) stated: "**73 documented decisions/principle entries are registered** in `DECISIONS.md`".

**What "entries" could mean, and the direct count from `DECISIONS.md` (2026-11-02):**

| Candidate interpretation | Count | Source of count |
|---|---|---|
| Principle rows in `DECISIONS.md` §2 | 17 | `^| P\d+ |` rows (P1–P17) |
| Decided owner-decision blocks (`### Q…`) in §3 | 10 | Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12 headings |
| Q identifiers registered (decided + unresolved) | 12 | the 10 above + Q4 and Q6 (recorded unresolved in §4) |
| Rows in §4 "Unresolved matters" | 9 | data rows of the §4 table |
| Rows in §5 traceability table | 11 | P1–P17, Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12 |
| Any combination of the above | 17, 10, 12, 9, 11, 27, 29, 36, 38, 47, 49, … | no combination yields 73 |

**Method:** line-by-line regex counts over `project-docs-en/DECISIONS.md` (2026-11-02) executed with PowerShell; results reproduced in `M2-R17-VALIDATION-RESULTS.md` (external deliverable).

## 4. Arabic / English consistency findings

Assessment date: 2026-11-02. Arabic source inspected: `project-docs/MASTER-ARCHITECTURE.md` (470 lines). All Arabic statements are preserved; nothing below modifies them.

### F1 — §7.4 (line 263) — RLS application timing

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §7.4 "Authorization and RLS" (line 263).
- **What the Arabic section says:** RLS application timing is `OPEN — OWNER DECISION REQUIRED`; the specification (SEC-004) ties it to phase 6 while DR-04 proposes phase 1; the owner approved neither specifically; the architecture does not choose.
- **Corresponding English document and section:** `09-MASTER-ARCHITECTURE.md` §7.4 (line 229) original `[OPEN]` tag with the M2-R15 amendment (line 426); `03-REQUIREMENTS.md` §15 SEC-010/SEC-011; `05-CONFLICTS-AND-GAPS.md` M2-R15 amendment (CG-01 resolved); `DECISIONS.md` §3 Q9.
- **Decision / OPEN ID:** Q9 (resolves DR-04, SEC-004, CG-01).
- **Classification:** **SUPERSEDED** — the owner decided Q9 on 2026-11-02: RLS is designed and enabled from the beginning of database design and implementation; application authorization and RLS operate together; `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, table ownership, and application database roles are explicitly examined; no effectiveness claim without executable security tests.
- **Evidence:** `DECISIONS.md` §3 Q9 (recorded `OWNER-DIRECT-EVIDENCE`); 09 M2-R15 amendment §7.4; 03 §15 SEC-010; 05 M2-R15 amendment CG-01.
- **Recommended handling:** Arabic source left untouched (preserved). M3/M4 agents must read the English register and reconciled sections first (per README §7). Annotating the Arabic source requires a separate owner order (see §8 below).
- **Blocks M3:** Yes — as part of the outstanding Arabic/English annotation decision (Q12/OPS-007; M2-R16 audit D-2), pending an owner decision on how the Arabic source is to be annotated. This document does not make that decision.

### F2 — §5.4 (line 184) — OPEN-1 (effect of an active objection on a confirmed link)

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §5.4 (line 184); also §4.3 (line 115), §5.1 (lines 154, 156), §5.2 (line 167), §13 (line 401).
- **What the Arabic section says:** whether an active objection immediately suspends a network-confirmed link from the biological calculation is `OPEN — OWNER DECISION REQUIRED`; the two options are unsettled; the architecture does not choose.
- **Corresponding English document and section:** `09-MASTER-ARCHITECTURE.md` §5.4 (line 160) original `[OPEN]` with the M2-R15 amendment (line 419); `15-UNRESOLVED-CONTRADICTIONS.md` M2-R15 amendment (OPEN-1 resolved); `DECISIONS.md` §3 Q3.
- **Decision / OPEN ID:** OPEN-1 (resolved by Q3).
- **Classification:** **SUPERSEDED** — Q3 (2026-11-02): an active objection does not automatically remove a confirmed biological relationship from kinship calculations; the link remains included until the network decides; objection/author/date/evidence recorded; disputed status exposed to authorized viewers; no unilateral invalidation.
- **Evidence:** `DECISIONS.md` §3 Q3; 09 M2-R15 amendment; 15 M2-R15 amendment; 06 M2-R15 amendment (OPEN-1 resolved).
- **Recommended handling:** Arabic source untouched; agents must read the register (README §7). Roadmap note: the Arabic §15 roadmap (line 440) still lists OPEN-1 among items M3 must not silently resolve; OPEN-1 is now resolved by Q3, so that roadmap reference is historical.
- **Blocks M3:** Yes — only as part of the §8 annotation decision; the roadmap reference must not be read as keeping OPEN-1 open.


### F3 — §5.4 (line 185) and §5.2 (line 170) — OPEN-2 (resubmission of a rejected link)

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §5.4 (line 185); §5.2 (line 170); §13 (line 402).
- **What the Arabic section says:** whether a rejected link may be resubmitted with new evidence is `OPEN — OWNER DECISION REQUIRED`; the Rejected → Awaiting confirmation transition is not approved; the document assumes neither that resubmission is possible nor that new evidence is mandatory or sufficient.
- **Corresponding English document and section:** `DECISIONS.md` §4 (Q4/OPEN-2 `[UNRESOLVED]`); `09-MASTER-ARCHITECTURE.md` §5.4 (line 161) `[OPEN]`; `15-UNRESOLVED-CONTRADICTIONS.md` §1 OPEN-2; 06 M2-R15 amendment (OPEN-2 not resolved).
- **Decision / OPEN ID:** Q4 / OPEN-2.
- **Classification:** **NO CONFLICT** — the register confirms Q4 was not answered; OPEN-2 remains unresolved; the Arabic statement matches the current status.
- **Evidence:** `DECISIONS.md` §4 row "Q4 / OPEN-2 … `[UNRESOLVED]` — no policy selected"; 09 M2-R15 amendment line 421.
- **Recommended handling:** none; the item must remain open until the owner decides.
- **Blocks M3:** No new block from this assessment; OPEN-2 is a pre-existing unresolved owner decision preserved by the register.

### F4 — §5.6 (line 196) — OPEN-3 (meaning of "supported by independent evidence")

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §5.6 (line 196); also §13 (line 403).
- **What the Arabic section says:** the meaning of "supported by independent evidence" in FR-018 is `OPEN — OWNER DECISION REQUIRED`; open questions (a) link-state, (b) supporting information bound to the link, (c) relation to network confirmation; the architecture chooses no answer.
- **Corresponding English document and section:** `09-MASTER-ARCHITECTURE.md` §5.6 (line 171) original `[OPEN]` with the M2-R15 amendment (line 420); `03-REQUIREMENTS.md` §15 (FR-018 amendment); `15-UNRESOLVED-CONTRADICTIONS.md` M2-R15 amendment (OPEN-3 resolved); `DECISIONS.md` §3 Q5.
- **Decision / OPEN ID:** OPEN-3 (resolved by Q5).
- **Classification:** **SUPERSEDED** — Q5 (2026-11-02): independent evidence is supporting information stored separately from the relationship's confirmation status, linked to the relationship, with provenance and metadata preserved; its presence/absence does not itself determine confirmation.
- **Evidence:** `DECISIONS.md` §3 Q5; 09 M2-R15 amendment; 15 M2-R15 amendment; 03 §15 FR-018 note.
- **Recommended handling:** Arabic source untouched; agents must read the register (README §7).
- **Blocks M3:** Yes — only as part of the §8 annotation decision.

---


**Conclusion:** the figure "73" is **not reproducible** from the register by any defined counting method (confirming M2-R16 finding M-5). The figure was corrected in `README.md` §6 to the verified statement: 17 principles (P1–P17) and owner decisions Q1, Q2, Q3, Q5, Q7, Q8, Q9, Q10, Q11, Q12, with Q4 and Q6 recorded as unresolved (17 + 12). No unverified replacement number was introduced.

**README file-count claims re-verified (2026-11-02):** `project-docs-en/` contains **34 files before M2-R17** (24 top-level + 10 `verification/`), and **35 files after M2-R17 adds this document** (`18-SOURCE-DOCUMENT-STATUS-AND-CONSISTENCY.md`). README §1.1 categories after M2-R17: numbered files `00`–`18` = 21 (includes the two manifest variants), numbered content documents `02`–`16` = 15, Phase C content `03`–`16` = 14, `DECISIONS.md` = 1, supporting top-level files = 3, verification artifacts = 10; total 21 + 1 + 3 + 10 = **35**. The M2-R15 claims "15 changed + 1 added" and "16 M2-R15-marked files" remain as recorded in `16-VALIDATION.md` G6.

---

### F5 — §3.4 (line 94) — OPEN-4 (multiple accounts belonging to one person)

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §3.4 "Duplicate identity" (line 94); also §13 (line 404).
- **What the Arabic section says:** how multiple accounts belonging to one person are identified and handled is `OPEN — OWNER DECISION REQUIRED` (M1-E §3 item 4); no solution is assumed; the only permitted architectural phrasing is a `PROPOSED` description, not a solution.
- **Corresponding English document and section:** `DECISIONS.md` §4 (Q6/OPEN-4 `[UNRESOLVED]`); `09-MASTER-ARCHITECTURE.md` M2-R15 amendment line 422; `15-UNRESOLVED-CONTRADICTIONS.md` §1 OPEN-4.
- **Decision / OPEN ID:** Q6 / OPEN-4.
- **Classification:** **NO CONFLICT** — Q6 was not answered; the register explicitly preserves OPEN-4 and distinguishes it from Q10C's duplicate person-record behavior. The Arabic statement matches the current status.
- **Evidence:** `DECISIONS.md` §4 row "Q6 / OPEN-4 … `[UNRESOLVED]` — distinct from Q10's duplicate person-record behavior"; 09 M2-R15 amendment line 422.
- **Recommended handling:** none; the item must remain open until the owner decides.
- **Blocks M3:** No new block from this assessment; OPEN-4 is a pre-existing unresolved owner decision preserved by the register.

### F6 — §8.1 (line 280) — DR-02 / DR-28 state-source conflict

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §8.1 "Source of truth" (line 280).
- **What the Arabic section says:** "DR-02 and DR-28 (approved formulations): current state is the source; the audit is a historical record and not a source of state. This resolves the conflict that existed between them (the proposed DR-28 rewording awaits editing in the source document). `OWNER-APPROVED` (principle), `PROPOSED` (literal wording of the source document)."
- **Corresponding English document and section:** `DECISIONS.md` §3 Q1/Q2; `09-MASTER-ARCHITECTURE.md` §8.1/§8.2 with the M2-R15 amendment (line 427); `06-DECISIONS-REQUIRED.md` M2-R15 amendment (DR-02/DR-28 decided); `15-UNRESOLVED-CONTRADICTIONS.md` §2 M2-R15 amendment.
- **Decision / OPEN ID:** Q1 / Q2 (DR-02, DR-28).
- **Classification:** **NO CONFLICT** at the principle level. The Arabic text itself already records the conflict as resolved at the principle level; the only pending aspect (amending the literal wording of DR-28 in the source document) remains pending by design because Arabic sources are not edited without a separate owner order. Note: the M2-R16 audit's phrase "DR-02 and DR-28 … cannot both be adopted as written" appears in `project-docs/analysis/DECISION-REGISTER.md` §4 (and historically in the English `15` §2), not in `MASTER-ARCHITECTURE.md` §8.1; the register Q1/Q2 supersedes that historical conflict note at the principle level.
- **Evidence:** `DECISIONS.md` §3 Q1/Q2; the Arabic §8.1 text quoted above; 09 M2-R15 amendment; 06 M2-R15 amendment; 15 §2 M2-R15 amendment.
- **Recommended handling:** none beyond README §7 (register-first reading).
- **Blocks M3:** No.

### F7 — §8.4/§8.5 (line 304 area) — OPEN-8 (audit retention)

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §8.4/§8.5 (line 304).
- **What the Arabic section says:** retention duration, deletion rights, key-destruction procedures, and whether destroyed-key encryption suffices as a deletion method are `OPEN — OWNER DECISION REQUIRED` (OPEN-8) after legal review.
- **Corresponding English document and section:** `DECISIONS.md` §3 Q7; `09-MASTER-ARCHITECTURE.md` §8.5 M2-R15 amendment (line 428); `06-DECISIONS-REQUIRED.md` M2-R15 amendment (DR-19 in scope); `15-UNRESOLVED-CONTRADICTIONS.md` §5 CG-31.
- **Decision / OPEN ID:** OPEN-8 / DR-19 (in scope, Q7); DR-19 remainder (pseudonymous audit identifier, legal-linked deletion/key-destruction) stays open.
- **Classification:** **SUPERSEDED in scope** — Q7 (2026-11-02) decided no automatic expiration, application functions must not delete audit records, and permission-controlled access; the legal-review remainder (DR-19 remainder) remains **NO CONFLICT** (still open). This section was not flagged by M2-R16; it is included for completeness because Q7 touches it.
- **Evidence:** `DECISIONS.md` §3 Q7 and §4 "DR-19 remainder"; 09 §8.5 amendment.
- **Recommended handling:** none beyond README §7.
- **Blocks M3:** No new block; the DR-19 legal-review remainder is a pre-existing open item.

### F8 — §16 item 5 (line 457) — statement that `DECISIONS.md` does not exist

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §16 "Consistency notes with the source documents", item 5 (line 457).
- **What the Arabic section says:** "`DECISIONS.md` does not exist. It was not created, and the `OWNER-APPROVED` decisions in this document are not formally registered in it. They must be registered by a separate order."
- **Corresponding English document and section:** `09-MASTER-ARCHITECTURE.md` §16 item 5 (line 409) — inline-marked "superseded by M2-R15"; `01-MISSING-EVIDENCE.md` ME-02 (RESOLVED); `00-SOURCE-MANIFEST.md` §5 row (RESOLVED); `07-DECISION-EVIDENCE-REGISTER.md` §5 (line 76); `15-UNRESOLVED-CONTRADICTIONS.md` §3 (inline note); `17-MIGRATION-REPORT.md` and `PHASE-A-GATE-REPORT.md` carry dated addenda.
- **Decision / OPEN ID:** none — a documented act (M2-R15 register creation, 2026-11-02) under owner order Q12 / the M2-R15 execution authorization.
- **Classification:** **SUPERSEDED (historical)** — the register was created at `project-docs-en/DECISIONS.md` on 2026-11-02 and records P1–P17 and Q1–Q12. The Arabic sentence accurately described the pre-M2-R15 state.
- **Evidence:** `project-docs-en/DECISIONS.md` exists (SHA-256 `84A821DBF101FB5CA909931CC473C31C35E7AF2895825AE587410762564CCE96` before M2-R17; unchanged); 09 §16 item 5; 01 ME-02; 00 §5.
- **Recommended handling:** Arabic source untouched; the sentence is historical and must not be read as current (README §7). The "separate order" the Arabic sentence anticipated is the M2-R15 execution authorization recorded in `DECISIONS.md`.
- **Blocks M3:** Yes — only as part of the §8 annotation decision (the Arabic statement is factually outdated but preserved).

### F9 — §13 OPEN table (lines 401–421) — status rows

- **Arabic source path and section:** `project-docs/MASTER-ARCHITECTURE.md` §13 table.
- **Rows and classifications:**
  - **OPEN-1** (line 401) — **SUPERSEDED** by Q3 (see F2).
  - **OPEN-2** (line 402) — **NO CONFLICT**; still open (see F3).
  - **OPEN-3** (line 403) — **SUPERSEDED** by Q5 (see F4).
  - **OPEN-4** (line 404) — **NO CONFLICT**; still open (see F5).
  - **OPEN-8** (line 408) — **SUPERSEDED in scope** by Q7 (see F7).
  - **OPEN-16** (line 416) — **NO CONFLICT**: the Arabic row says the cycle-prevention mechanism is deferred to database design and concurrency testing; the register records OPEN-16's *mechanism* as `[UNRESOLVED]` while the invariant (P16) stands. The mechanism remains unselected.
  - **OPEN-19** (line 419) — **NO CONFLICT**: identity verification beyond OTP remains `OPEN — OWNER DECISION REQUIRED`; the register preserves DR-30/OPEN-19 as `[UNRESOLVED]`.
  - **OPEN-20** (line 420) — **NO CONFLICT**: abuse/rate-limit values remain open; the register records OPEN-20/DR-34 as `[PROPOSED]` baseline only.
  - **OPEN-21** (line 421) — **SUPERSEDED at principle level** by Q8 (record-owner role limited; no unrestricted ownership; network governance for biological confirmation; no automatic sensitive access). The claim mechanism (DR-12) and field-level permission design remain open.
  - **OPEN-5** (KD-02), **OPEN-6** (KD-01), **OPEN-7** (DR-15/KE-04/KE-05), **OPEN-9…OPEN-15**, **OPEN-17**, **OPEN-18** — **NO CONFLICT**; not decided by Q1–Q12 and preserved open by the register §4.
- **Corresponding English document and section:** `09-MASTER-ARCHITECTURE.md` §13 with the M2-R15 amendment (line 430); `DECISIONS.md` §4.
- **Recommended handling:** none beyond README §7; OPEN-2/4, OPEN-16 (mechanism), OPEN-19/DR-30 must remain open (register §4).
- **Blocks M3:** No new block beyond the pre-existing unresolved decisions and the §8 annotation decision.

---

## 5. Phone optionality — Q10A / FR-001 (M2-R16 finding M-6)

**Question examined:** whether the documents clearly state that phone information is optional and is not a mandatory condition for creating a Person record or an Account.

**Sources compared:**
- `DECISIONS.md` §3 Q10A: "Phone number, workplace, residence, and map location are optional profile information."
- `03-REQUIREMENTS.md` FR-001: "Register users and verify phone numbers by OTP code" (§9, §12-1).
- `03-REQUIREMENTS.md` FR-003/FR-004 and `DECISIONS.md` §3 Q10B (DATA-004/005): Account and Person record are separate entities; a person may have a record without an account.
- Related privacy/identity requirements: SEC-002 (encrypt sensitive data), CG-33/DR-30 (identity verification beyond OTP — unresolved), `DECISIONS.md` §4 DR-30/OPEN-19.

**Determination:**
1. **Account creation:** phone is mandatory for account registration per FR-001 (registration + OTP verification). No approved decision changes this; Q10A addresses *profile* information, not the registration credential.
2. **Person record creation:** no requirement makes a phone number a mandatory condition for creating a Person record. Q10A states phone is optional profile information; FR-004/DATA-005 establish person records without accounts (hence without phone credentials). The documents therefore support that phone is optional for a Person record, and that phone is not a mandatory condition for creating a Person record.
3. The only nuance is terminology: FR-001 uses "phone" as the account-registration credential while Q10A uses "phone" as an optional profile field. The two statements address different entities and are **not in conflict**; the terminology reconciliation (e.g., distinct fields "account phone/OTP channel" vs "profile phone") is M3 design/terminology work, as the M2-R16 audit noted ("not a register error").

**Classification:** **NO CONFLICT** (terminology nuance recorded for M3 design). No owner decision is required for this item, and none is invented here. No authentication method is added, and no phone-verification requirement beyond OTP is asserted (DR-30/OPEN-19 remains open).

---

## 6. Unresolved decisions preserved

This correction did not silently close or redefine any unresolved owner decision. Verified against `project-docs-en/DECISIONS.md` (unchanged by M2-R17, SHA-256 `84A821DBF101FB5CA909931CC473C31C35E7AF2895825AE587410762564CCE96`):

- **Q4 / OPEN-2** — remains `[UNRESOLVED]` (resubmission of rejected relationships).
- **Q6 / OPEN-4** — remains `[UNRESOLVED]` (multiple accounts of one person).
- **OPEN-16** — mechanism remains `[UNRESOLVED]`; the invariant (P16) stands; no mechanism selected.
- **DR-30 / OPEN-19** — remains `[UNRESOLVED]` (identity verification beyond OTP; preserved by Q10).
- DR-19 remainder (pseudonymous audit identifier; legal-linked deletion/key-destruction) — remains `[UNRESOLVED]`.
- DR-32/33/34 — remain `[PROPOSED]`, not decisions.
- All other OPEN-5…OPEN-21 / DR-01…DR-31 items not decided by Q1–Q12 — remain open.
- No technical proposal was converted into an owner-approved decision; no claim is made that an independent AI or human engineering review has occurred (Q11 gate remains pending); no claim is made that the owner has approved the final architecture.

---

## 7. Evidence limitations (unavailable evidence)

- The owner's conversation export (session `1793525922711_rqjpo`), the M2-R12 owner-decision evidence, the M2-R13 briefing, and the archived Arabic draft (`%LOCALAPPDATA%\Temp\m2-r14\DECISIONS.ar-draft-20261102.md`) are **not present on this machine**; the fidelity of the Q1–Q12 register text to the owner's verbatim words therefore remains **UNVERIFIED** (M2-R16 audit CB-1). This document does not claim otherwise.
- The M1-E report remains missing (ME-01); in-repository `OWNER-APPROVED` labels remain claims, not evidence.
- Where a decision's approval evidence is unavailable, the matter is classified **UNVERIFIED**, never approved.

---

## 8. Remaining items before M3 (as recorded by this assessment)

1. **Dual independent review (Q11)** — an independent AI agent that did not prepare the reviewed documentation AND an independent human software engineer; findings compared; material disagreements resolved; owner approval of the outcome. **Not yet executed.**
2. **Owner approval of the final architecture** — not given.
3. **Unresolved owner decisions** — Q4/OPEN-2, Q6/OPEN-4, OPEN-16 (mechanism), DR-30/OPEN-19, and the other preserved open items.
4. **Arabic/English annotation decision** — the owner must decide how the Arabic source `project-docs/MASTER-ARCHITECTURE.md` is annotated for supersession (dated supersession notes pointing to `project-docs-en/DECISIONS.md`, or explicit acceptance that the English register supersedes where the Arabic source is silent). This is the D-2 item from the M2-R16 audit; this document records the findings but does not make that decision.
5. **Evidence supply** — the owner should supply the session export / M2-R12/R13 artifacts or explicitly re-confirm the register text (M2-R16 CB-1).

M3 **remains BLOCKED**. This document does not authorize M3 or any implementation work.

---

*End of M2-R17 consistency document. Prepared 2026-11-02 by the M2-R17 documentation-correction agent.*
