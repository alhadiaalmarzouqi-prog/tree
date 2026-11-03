# M3 Amendments (Proposed) — 2026-11-03

**Status: PROPOSED.** These amendments are engineering design proposals that respond to M3-R1. None is an owner decision, and none is approved. They do not edit the original M3 documents; they are the amendment notes that the reviewer requested (M3-R1 §8: "recorded as an amendment note ... not as a silent edit"). Owner approval and the Q11 review are required before any amendment is accepted.

**Protected inputs unchanged:** M0, the 22 fixtures, Arabic sources, `DECISIONS.md` (no approved decision changed).

---

## A-01 — `M3-02` §1: viewer-scoped results (C-01, CRITICAL)

Proposed rule:
1. A kinship result or shared-relative result is computed only from graphs the viewer is entitled to read.
2. The result names only viewer-visible people and relationships.
3. A path that exists but is hidden by authorization is reported as "hidden by authorization", never as "no kinship".
4. A result computed on a network the viewer does not belong to is shown only as permitted by the visibility rules; membership in one network does not grant access to another (OQ-21-03).

Status: proposed. The full eligibility matrix is OQ-21-03 (owner-policy, open).

## A-02 — `M3-01` §5: network lifecycle (H-01)

Proposed lifecycle:
- Creation and membership grant or revocation follow governance rules; the threshold and eligibility rules are OQ-21-05 (open).
- A Person who leaves a network keeps their Person record and relationships.
- Adopted facts remain with the network that adopted them. Leaving does not remove them from other networks.
- Each membership change is audited.

Status: proposed. Owner-policy items: OQ-21-05.

## A-03 — `M3-03` §1.1: association to an existing Person (H-03)

Proposed: "Association of an account with an existing Person" is removed from the first release. Suggestions remain informational. The association flow is allowed only after OQ-21-10 (verification method) is closed, through the alternative review path described in OQ-21-10.

Status: proposed. Owner-policy and legal/privacy items: OQ-21-10, DR-30 / OPEN-19.

## A-04 — `M3-02` §1.3: accountless-record permissions (H-04)

Proposed minimal table (see `DATABASE-DESIGN-READINESS-PART2.md` §5 for the full form):
- Creator: may edit basic, non-sensitive fields of a record they created.
- Sensitive fields: changes require additional authorization (owner to define the mechanism).
- Relationship changes: require network governance; the creator has no unilateral authority (Q8, P6).

Status: proposed. "Additional authorization" needs owner confirmation.

## A-05 — `M3-03` §1.2 and `M3-02` §4: MVP correction rule (H-06)

Proposed: a parentage correction is recorded as a Proposal. It does not change the adopted graph until a network decision is recorded for that network. The previously adopted parent remains until then. At most one adopted parent per role per network state.

Status: proposed. Effective-time wording is open (C-R21-06).

## A-06 — `M3-02` §3: audit visibility (H-07)

Proposed:
- Audit reads follow the same field-level visibility as current state.
- Sensitive audit values are stored encrypted under a separately controlled key.
- Ordinary users see only their own changes, plus controlled exceptions.
- Internal before/after values are visible only to authorized audit roles.

Status: proposed. The authorized audit roles are an owner decision.

## A-07 — `M3-02` §8: truncated result state (H-08)

Proposed: a result can be `complete`, `truncated`, or `no recorded kinship`. A `truncated` result is never shown as absence. The enumeration limit is a configuration value. No numeric limit is proposed here.

Status: proposed. The limit value is measured at M7.

## A-08 — `M3-03` §1.1: shared-relative discovery (H-09)

**WITHDRAWN (2026-11-03).** The owner has confirmed that shared-relative discovery is an essential capability (`DECISIONS.md` §3D, R-01). The narrowing below is not adopted. The text is kept unchanged as history.

Proposed: remove "Discovering shared relatives" from the first-release table and record it as deferred until OQ-21-13 and C-01 are settled. Same-network display of an authorized relationship remains in scope.

Status: proposed scope change. The owner's brief lists shared-relative discovery as essential, so the owner must confirm this narrowing.

## A-09 — `M3-01` §3: marriage and affinity (H-10)

Proposed: marriage and affinity form a relationship kind separate from parentage. They carry their own edge type and never enter the biological calculation (Q2, GOV-011, GOV-012). Mixed paths label each edge. Marriage validity, polygamy, and half-sibling rules are NOT assumed (CG-29, open).

Status: technical separation proposed. Owner-policy items open.

## A-10 — `M3-02` §1: definition of "public" (M-01)

Proposed: "public" means visible to any person outside the explicit visibility rules, including unauthenticated users. Default deny applies.

Status: proposed wording.

## A-11 — `M3-02` §5: correction notices (M-02)

Proposed: correction notices and high-risk decision requests are never batched into a daily limit.

Status: BLOCKED by owner (OQ-21-07 / C-R21-05 exemption).

## A-12 — `M3-03` §3: RLS prerequisites (M-03)

Listed as prerequisites: H-01 (network membership model), H-04 (accountless-record permissions), OQ-21-03 (visibility matrix). Recorded here; the M3-03 text is not edited.

## A-13 — `M3-04` §5: scope of the AI review (L-02)

Proposed note: the AI review in M3-R1 does not satisfy Q11. Q11 requires an independent human software engineer as well.

## A-14 — `M3-02` §2: cross-reference (L-03)

Proposed cross-reference: evidence data model is OQ-21-11 (`DECISIONS.md` §4A).

---

## Summary of items that need the owner

OQ-21-03 (matrix), OQ-21-05 (thresholds and eligibility), OQ-21-07 (exemption), OQ-21-10 (verification), DR-30 / OPEN-19, C-R21-06 (effective time), CG-29 (polygamy and half-siblings), the authorized audit roles (A-06), the "additional authorization" mechanism (A-04), the shared-relative narrowing (A-08), and whether one account may link to several Persons (H-02).
