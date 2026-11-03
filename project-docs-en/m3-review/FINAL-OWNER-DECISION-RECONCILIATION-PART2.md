# Final Owner Decision Reconciliation (Part 2 of 2)

**Continuation of:** `FINAL-OWNER-DECISION-RECONCILIATION.md` (Part 1). **Date:** 2026-11-03.
**Provenance warning for every R-item:** the wording below is reconstructed from the owner's current brief. No transcript was recovered. Each R-item is `RECONSTRUCTED-FROM-OWNER-BRIEF` and must be checked by the owner against the original text before it is treated as verbatim.

## 4. Reconstructed owner decisions (R-items)

| ID | Decision meaning (reconstructed) | Effect on design |
|---|---|---|
| R-01 | Shared-relative discovery is an essential product capability, not a deferred or optional feature. | Shared-relative discovery stays in scope. Withdraws proposal A-08. Design must be built, scoped by visibility rules (see OQ-21-03 split in §7). |
| R-02 | Family networks are connected. One Person may connect several family networks. There is no mandatory primary network and no hierarchical parent or sub-network model. | Network graph is a set of networks linked by shared Persons. No "root" network. |
| R-03 | A cross-network path shows, at each transition, the connecting Person, the relationship type, and the family-branch context. Origin and destination network context are preserved. | Path presentation requirement. |
| R-04 | Useful paths are shown first. The user may request remaining paths at any time. No valid path is silently discarded from the calculation. | Pagination or progressive exploration is a presentation mechanism only. |
| R-05 | A search stopped by a technical limit is never presented as proof that no relationship exists. The result is labelled incomplete. | Result state `truncated` (see M3-R1 H-08). |
| R-06 | Network membership is separate from Person existence and from network connection. A Person who leaves a network keeps their record and relationships. Returning requires the approved membership process. | Membership is its own entity. Leaving never deletes Person or relationship rows. |
| R-07 | Person, Account, and network membership are separate concepts. | Confirms Q13 and OQ-21-19. |
| R-08 | Login is by phone verification. No separate mandatory 2FA is required in the current scope. | No authenticator-app requirement. |
| R-09 | Required session security: active device and session list; recent login history; approximate location only where appropriate; notification on login from a new device; terminate one session; terminate all other sessions. | Feature requirements. Not optional. |

## 5. Reconstructed owner decisions (continued)

| ID | Decision meaning (reconstructed) | Effect on design |
|---|---|---|
| R-10 | Approved capabilities: blocking another user; abuse reporting; impersonation reporting; independent appeal by the accused account holder; in-app support centre. | Feature requirements. Report handling and appeal workflow details are design items. |
| R-11 | Multi-country support is required from the beginning. | Country-specific phone formats, subdivisions, naming, time zones. |
| R-12 | No separate hierarchical community layer. | No mandatory community entity. |
| R-13 | Approved features: family subgroups (creation and manager appointment separate from lineage governance); GEDCOM, Excel, and CSV import with preview and duplicate suggestions, with no automatic confirmation of imported relationships; personal backups; in-app support centre. | Feature-scope items. Consistent with `DECISIONS.md` §15 of the owner feature list. |
| R-14 | Person status colours are a display rule: green = living, active participant; blue = living, not actively participating or unregistered; white = deceased. | Colours are computed from separate stored facts (Person deceased flag, account state, membership state). They are never a stored status column (Q16, OQ-21-14). |
| R-15 | Attached documents are for viewing and discussion by authorized family members. The platform does not authenticate them and does not declare them legal proof. | Consistent with Q5 and Q22. Source, author, and date are recorded where available. |

## 7. Reassessment of the ten open items from the closure report

Classes: **A** already answered by the owner; **B** technical design for engineering; **C** genuine owner-policy decision still required; **D** legal or privacy question requiring qualified review.

| Item | Class | Determination | Basis |
|---|---|---|---|
| H-09 (shared-relative discovery) | **A** | Answered: essential capability (R-01). Not a scope reduction. | Owner brief |
| OQ-21-05 (thresholds, eligibility) | **C** for eligibility and procedure; **A** for "no arbitrary numerical thresholds" | The owner rejected invented numeric thresholds. Eligible participants and decision procedures per decision type still need owner policy. No number will be proposed. | `DECISIONS.md` §3C.2; R-17 |
| H-02 (one account, several Persons) | **A** for one-active-account on the Person side and for "no automatic merge"; **C** for whether one account may link to several Persons | Approved: one Person may have several accounts over time, only one active (OQ-21-19). The account-side rule for one account and several Persons is not in any record. | `DECISIONS.md` §3C.2; R-07 |
| OQ-21-03 (visibility) | **A** for the principle; split below | Approved principle: eligibility from confirmed relationships and network boundaries; personal control; no whole-network access. Matrix for in-laws and sibling marriages is open (**C**). Relationship-path visibility is distinct from sensitive-field visibility (see §8). | `DECISIONS.md` §3C.2; R-02, R-03 |
| H-07 (audit access) | **B** for role-based design; **C** for which roles are authorized | Design: audit reads are role-based and never expose hidden fields (see §8). The owner must name the authorized audit roles. | Q1, Q7, P2; `DECISIONS.md` §3C |
| H-04 (accountless sensitive changes) | **B** for mechanism design; **C** for the approval rule | Design: creator edits basic fields; sensitive changes need a second, independent authorization. Owner must confirm that rule. | Q8; P6 |
| OQ-21-10 (account verification) | **A** for "phone is not identity"; **D** for the real-world verification method | Answered: OTP proves phone control only (OQ-21-10 option B). The method needs legal and privacy review. | `DECISIONS.md` §3C.2 |
| M-02 (correction notices) | **B** for the design; **C** for the exemption policy | Critical correction notices must not be silently suppressed (owner requirement). The notification class list is design; the exact exemption rule is owner policy. Not decided here. | Owner brief; OQ-21-07; C-R21-05 |
| CG-29 (polygamy, half-siblings) | **B** for technical support; **C** for policy; **D** for legal or cultural assumptions | Technical: several marriages and half-sibling classification are supported by the data model (`marriage` edges; parentage per network). Legal validity, recognized forms, and cultural rules are NOT assumed and need owner policy and qualified review. | Q2; FR-007, FR-008, FR-009 |
| H-06 (correction effective time, C-R21-06) | **C** | Replacement effective time is not stated in any record. Owner decision required. Proposed engineering default: the previous adopted parent stays until a network decision (Q17). | Q17; C-R21-06 |
| H-10 (marriage and affinity) | **B** for technical separation; **C** for marriage-validity policy | Separation from parentage is an engineering requirement (Q2, GOV-011). Validity policy is owner-policy. | Q2; GOV-011, GOV-012 |

**Note on H-02:** the Account/Person separation and the one-active rule (OQ-21-19) are approved. The only open question is the account-side many-to-one rule. Engineering must not infer it.


## 8. Visibility and audit rules (design derived from confirmed decisions)

**8.1 Path visibility is not sensitive-field visibility.** A user may see that a relationship path exists (for example, the connecting Person and the relationship type) without seeing that Person's phone number, residence, or other sensitive fields. Each is controlled separately:
- Path and relationship visibility: derived from confirmed relationships and network boundaries (OQ-21-03; R-02, R-03).
- Sensitive-field visibility: controlled by the Person's own field settings and group rules (Q10A, PRV-011 to PRV-013).
- Seeing a relative in another network grants no access to that network's details (OQ-21-03).

**8.2 Role-based audit access (H-07).** Proposed roles, for the owner to confirm (C):
- Own-change history: each user sees records of changes they themselves made, with hidden fields masked.
- Network governance view: members see decision and objection history for proposals in their network, with personal fields masked.
- Audit administrator: may see internal before and after values for security and legal investigation only, under logged access. Sensitive values are encrypted under a separate key.
- No ordinary role, including support staff, sees hidden personal values through audit.

**8.3 Critical notifications (M-02).** Owner requirement: critical items must not silently disappear. Design rule: every critical item is kept in the review queue regardless of batching, and a notification is never silently dropped. The exact exemption list is owner policy (C).

## 9. Unresolved and reviewed items

**Genuine owner-policy decisions still required (C):**
1. Visibility matrix for in-laws and sibling marriages (OQ-21-03).
2. Eligible participants and decision procedures per decision type (OQ-21-05); no numerical thresholds will be proposed.
3. One account linked to several Persons (H-02).
4. Authorized audit roles (H-07) and the approval rule for sensitive accountless changes (H-04).
5. Effective time of an adopted correction (C-R21-06 / H-06).
6. Exemption policy for critical notifications (OQ-21-07 / M-02).
7. Marriage-validity policy and polygamy or half-sibling policy (CG-29, H-10).
8. Confirmation of the Q24–Q96 and other owner items recorded as UNVERIFIED, if they are approved decisions.

**Legal or privacy review required (D), before production:**
1. Account-to-Person verification method (OQ-21-10, DR-30 / OPEN-19).
2. Deceased-person privacy rules and access design (OQ-21-12).
3. Audit retention, pseudonymous audit identifiers, and crypto-erase (Q7, DR-19 remainder).
4. Deletion and anonymization rules for accounts and Person records.
5. Session location handling and the legal basis for storing login history.
6. Marriage and relationship recognition in each country served (R-11).
7. Abuse reporting, appeal, and temporary-restriction procedures.

**Technical decisions delegated to engineering (B):** concurrency mechanism for biological invariants (OPEN-16; candidates in `DATABASE-DESIGN-READINESS.md` §4); enumeration limit and truncation measurement (H-08, M7); RLS network-boundary mechanism (M-04); audit storage shape; session and device data model; import preview and duplicate matching logic (no numeric thresholds without owner decision, OQ-21-15).

**UNVERIFIED items (cannot be used as basis for design):** Q24–Q96 text and approval; any "latest clarifications" beyond those in the current brief; the M2-R20 messages (OQ-21-00 residual).

**Note on H-04:** the mechanism for "additional authorization" is a design item. Whatever mechanism is chosen must not allow a single creator to change a sensitive field of a Person they do not control, and must not give the creator ownership of lineage (Q8).

| R-16 | A rejected proposal may be reopened only with materially new information (OQ-21-18). | Consistent with `DECISIONS.md` §3C.2. |
| R-17 | No numerical voting threshold is set by OQ-21-05. | Consistent with `DECISIONS.md` §3C.2 and Q19. |
| R-18 | M0 and all 22 fixtures remain immutable. | Consistent with P17. |

## 6. Superseded and withdrawn items

| Earlier item | Replacement | Status |
|---|---|---|
| Proposal A-08 in `M3-AMENDMENTS-2026-11-03.md` (remove or defer shared-relative discovery) | R-01 | WITHDRAWN. The amendment file is kept unchanged as historical; this withdrawal is recorded here and in `DECISIONS.md` §3D. |
| M3-R1 H-09 "deferred" reading | R-01 | Historical. M3-R1 is not rewritten. |
| M3-R1-RESOLUTION-MATRIX rows that say "BLOCKED by owner confirmation" for H-09 | R-01 | Status updated by an amendment note in the matrix B file, §1. |
| M-02 proposal "correction notices never batched" | Owner requirement that critical notifications must not silently disappear (R-13 family, §15 owner feature list); exact exemption design remains open | Proposal kept as a design requirement, not as an owner decision. |
