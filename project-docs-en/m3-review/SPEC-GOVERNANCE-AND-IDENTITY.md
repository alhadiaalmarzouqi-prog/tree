# Specification: Relationship Governance and Identity Lifecycle

**Status:** design specification. Derived from DD-08, DD-15–DD-19, DD-36, and R-06, R-07. Canonical decisions are in the register; this file does not add decisions.

## 1. Relationship lifecycle (per network)

1. **Proposal** submitted by any eligible contributor, with description and optional evidence.
2. **Under review** in each affected network. Evidence is attached to the proposal and never changes its status by itself (DD-15).
3. **Network decision** per network: accepted, rejected with reason, or pending. Non-response is neither acceptance nor rejection; an expired response period leads to a reminder or extension, not an automatic outcome.
4. **Objection**, if raised, is recorded and evaluated through the network. An objection alone does not suspend an already confirmed relationship (DD-15).
5. **Adopted** relationship in that network's graph. Confirmed status applies only within that network (DD-02, DD-07).
6. **Correction** of an adopted parent is a separate governed proposal. The previous parent stays until the approved correction commits atomically (DD-33).
7. **Rejected** proposals keep the rejection and reason. Resubmission needs materially new information (DD-16).

## 2. Participants

- Eligible participants are identified from the affected branches and network membership.
- Conflicts of interest are declared and excluded from deciding their own relationship.
- A specialist or elder may suggest participants and give input. No single person may establish or change biological lineage (DD-15, Q18).
- Both parties to a relationship participate where applicable; neither holds a unilateral veto (P6).

## 3. Thresholds and procedure

- No fixed percentage or numerical quorum is defined (DD-17). Procedure parameters are configuration values, set by the owner's governance policy when it is approved.
- Decision types are risk-classed: low-risk additions, kinship-affecting additions, parent corrections, and deletions or removals. Each class defines eligibility, abstention handling, non-response handling, and extra review. The exact parameters are an owner-policy dependency (see the register, item C-list in `FINAL-OWNER-DECISION-RECONCILIATION-PART2.md` §9).

## 4. Identity lifecycle

- **Account** created by phone OTP. OTP proves control of the phone number only (DD-19).
- **Person** exists independently of any Account (DD-05). Creating an Account never creates a Person; creating a Person never requires an Account.
- **Account-to-Person association** requires an additional verification whose method, result, time, and source are recorded (DD-19). The method is an external dependency (E-01).
- **One active Account per Person** (DD-18). Old accounts remain on record and are never auto-deleted.
- **Transfer or recovery** requires reliable verification and an audit entry. Concurrent transfers are serialized by the database constraint (TD-02).
- **Suggestions** never create, merge, or associate Persons (DD-05, DD-19).
- **Phone change** never creates a new Person (DD-19).

## 5. Membership

- Membership is separate from Person existence and from Account state (DD-04, R-06).
- Leaving a network removes participation only. The Person record and relationships remain.
- Rejoining requires network approval and restores the same Person (DD-24).
