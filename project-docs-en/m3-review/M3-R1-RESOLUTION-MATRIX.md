# M3-R1 Resolution Matrix (Part A: method, verification of §8.1, CRITICAL and H-01 to H-05)

**Date:** 2026-11-03 (environment date). **Reviewed document:** `M3-R1-INDEPENDENT-AI-ARCHITECTURE-REVIEW.md`.
**Continuation:** `M3-R1-RESOLUTION-MATRIX-B.md` (H-06 to H-10, MEDIUM, LOW, M0 claims, open items).
**Severity rule:** original severities are kept. No severity was lowered to obtain approval.
**Status vocabulary:** VERIFIED (checked in this session); REPORTED BUT NOT INDEPENDENTLY VERIFIED; NOT VERIFIED; BLOCKED (needs owner decision, external review, or a test that does not yet exist); NOT APPLICABLE.
**"Proposed"** means an engineering design proposal. It is not an owner decision and is not approved. Owner-policy items are BLOCKED.

---

## 1. Verification of the reviewer's "M3-01 §8.1 not visible" claim

- **Reviewer statement:** `M3-01` §8.1 (about lines 119–134) was not visible and was not assessed (M3-R1 §2.1, §2.3).
- **Check performed:** read `project-docs-en/m3-conceptual/M3-01-DOMAIN-MODEL.md` in full, plus lines 49–133 in a separate read, in this session.
- **Observed:** §8 "Kinship calculation and M0 (unchanged)" starts at line 130; §8.1 "Fixed rules" (lines 132–133) states that M0 §B–§C definitions are not changed by the model and that M0 implementation is out of scope.
- **Result:** VERIFIED. The section exists and has no defect beyond those recorded. The reviewer's limit was a read truncation in its environment, not a missing section.

---

## 2. CRITICAL finding

### C-01 (CRITICAL): cross-network kinship and shared-relative results not scoped to the viewer's boundary

- **Proposed resolution:** a result is computed only from graphs the viewer may read, and names only the viewer-visible portion. "Hidden by authorization" is shown separately from "no kinship", so a hidden path is never displayed as absence. Shared-relative results follow the same rule.
- **Evidence:** `DECISIONS.md` §3C.2 (OQ-21-03, option D: seeing a relative in another network does not grant access to that network's details).
- **Status:** BLOCKED for full closure. The narrow rule is a proposal. The full eligible-portion matrix (OQ-21-03) is an owner-policy item not yet decided. CA cannot be granted without owner confirmation of the proposed rule.

---

## 3. HIGH findings H-01 to H-05

### H-01 (HIGH): network formation, membership, and eligibility undefined

- **Proposed resolution:** a network lifecycle covering creation, membership grant and revocation, and the effect of leaving. Adopted facts remain with the adopting network, with history kept. Leaving a network does not delete the Person record or family relationships.
- **Evidence:** `M3-01` §5; `DECISIONS.md` §3B.2 (OQ-21-01: each network decides independently).
- **Status:** BLOCKED by owner for who may create a network and for eligibility (OQ-21-05).

### H-02 (HIGH): "one account, several Persons" not covered; active-link rule not enforced on the account side

- **Proposed resolution:** an active-association constraint on both sides: at most one active account per Person, and at most one active Person per account (the latter is a technical default that must be confirmed, see below). The many-to-one rule is NOT decided here.
- **Evidence:** `DECISIONS.md` §3B.6 (OPEN-4, "remaining open"); OQ-21-19 rule 2.
- **Status:** BLOCKED by owner for the many-to-one rule. The one-active constraint is a technical requirement with status NOT VERIFIED until a database concurrency test exists.
- **Proposed owner question (not added to DECISIONS.md):** whether one account may be linked to several Persons, and under what rule.

### H-03 (HIGH): account-to-Person linking reachable in MVP without the required verification

- **Proposed resolution:** association with an existing Person is removed from the first release. It is allowed only after OQ-21-10 is closed. Suggestions stay informational only.
- **Evidence:** `DECISIONS.md` §3C.2 (OQ-21-10: OTP proves phone control only); `M3-01` §4.5.
- **Status:** BLOCKED by owner and legal/privacy review (OQ-21-10, DR-30 / OPEN-19). The verification method is not selected.

### H-04 (HIGH): no permission table for accountless records

- **Proposed resolution (design item):** the creator may manage basic fields. Sensitive fields and every relationship change go through network governance. Creation confers no ownership of the Person or their lineage (Q8).
- **Evidence:** `DECISIONS.md` Q8; permission table in `DATABASE-DESIGN-READINESS-PART2.md` §5.
- **Status:** BLOCKED for final. The meaning of "additional authorization" for sensitive changes needs owner confirmation. Field classification is a feature-design item.

### H-05 (HIGH): concurrency enforcement named, not designed

- **Proposed resolution:** candidate mechanisms with trade-offs are in `DATABASE-DESIGN-READINESS.md` §4. No mechanism is treated as proven. A concurrency test is a mandatory artifact.
- **Evidence:** `DECISIONS.md` P14, P16; OPEN-16 (mechanism not selected).
- **Status:** NOT VERIFIED. No database exists, so no concurrency test has run. Any claim that the invariant is enforced is blocked until that test passes.
