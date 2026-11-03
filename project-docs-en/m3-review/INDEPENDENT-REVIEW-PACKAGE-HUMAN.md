# Independent Human Engineering Review Package

**Status: PACKAGE PREPARED. HUMAN REVIEW NOT PERFORMED.** Nothing in this document is a review result, approval, or sign-off.
**Date:** 2026-11-03. **Required by:** Q11 (`DECISIONS.md` §3, Q11) and GOV-013. **Gate:** physical schema, migrations, and production code stay blocked until this review is performed, compared with the AI review, disputes are resolved, and the owner approves the outcome.

---

## 1. Who may review

- A software engineer who did not author the M3 documents or the M0 harness.
- Independence means: no authoring role in M0–M3, and no access to the authoring agent's conclusions before forming an opinion.
- The reviewer must record their name, role, date, documents read, and every command run with its result.

## 2. Shared baseline (identical for the human and AI reviewers)

Both reviewers receive the same baseline. The baseline is `project-docs-en/m3-review/FINAL-OWNER-DECISION-RECONCILIATION.md` and `-PART2.md`, plus `DECISIONS.md` §3D (R-01 to R-18). Every R-item is `RECONSTRUCTED-FROM-OWNER-BRIEF`; the reviewer must treat the wording as reconstructed, not verbatim. Q24–Q96 are UNVERIFIED and must not be assumed.

Reviewers must not receive the authoring agent's conclusions beyond these files.

## 2a. Documents to read (exact paths)

1. `project-docs-en/DECISIONS.md` (all sections, including §3B, §3C, §4A).
2. `project-docs-en/m3-conceptual/M3-01-DOMAIN-MODEL.md`.
3. `project-docs-en/m3-conceptual/M3-02-PRIVACY-AUDIT-SECURITY.md`.
4. `project-docs-en/m3-conceptual/M3-03-MVP-SCOPE-AND-OPEN-ITEMS.md`.
5. `project-docs-en/m3-review/M3-R1-INDEPENDENT-AI-ARCHITECTURE-REVIEW.md`.
6. `project-docs-en/m3-review/M3-AMENDMENTS-2026-11-03.md` (proposed amendments).
7. `project-docs-en/m3-review/M3-R1-RESOLUTION-MATRIX.md` and `M3-R1-RESOLUTION-MATRIX-B.md`.
8. `project-docs-en/m3-review/DATABASE-DESIGN-READINESS.md` and `DATABASE-DESIGN-READINESS-PART2.md`.
9. `project-docs-en/08-MATHEMATICAL-REFERENCE.md` (read only) and `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` (protected M0; read in the Arabic original).
10. `project-docs/reference-fixtures/kinship-reference-cases.json` (protected; read only).
11. `project-docs-en/m0-verification-report.md` and `project-docs-en/verification/m0-recalc/` (harness source).

## 3. Commands the reviewer may run (read-only checks)

```
cd "project-docs-en/verification/m0-recalc"
python m0_verify.py
python m0_mutation_check.py
```

Record the exact output. Do not modify the fixture. Hand-check at least 3 cases from different families (for example T09, T12, ST-06) by drawing the graph and enumerating the paths manually.

## 4. Review questions (answer each: AGREE / AGREE WITH CONCERN / DISAGREE, with section and reason)

1. **Scope.** Does the design serve family discovery and connection, not legal lineage proof (`DECISIONS.md` §3C.1)?
2. **Person and Account.** Is OQ-21-19 applied exactly? Is the one-active rule enforceable on both sides? What is the risk if the many-to-one rule is decided later?
3. **Network adoption.** Can one network adopt and another reject without changing the other? Does any part imply a global biological determination (OQ-21-16)?
4. **M0.** Re-derive three fixtures by hand. Does the harness agree with your hand derivation? Is the claim that a shortest-depth closure is insufficient correct for the fixtures?
5. **Concurrency (H-05).** Is the option set in `DATABASE-DESIGN-READINESS.md` §4 complete? Is the claim that a child-row lock is insufficient correct? Which combination would you choose, and why?
6. **RLS and network boundary (M-03, M-04).** Is `network_id` plus membership-based policies sufficient? What bypass paths (owner, `BYPASSRLS`, pooling) remain?
7. **Audit (H-07, Q1, Q7, P2, P3).** Is the append-only and encrypted-sensitive-value design adequate? What leaks remain?
8. **Marriage and nursing (H-10).** Is the separate edge store safe against accidental inclusion in M0? Is any legal assumption made without authority?
9. **Correction and reopening (H-06, Q17, OQ-21-18).** Does the previous adopted parent stay intact until a network decision?
10. **Privacy and deletion.** Are the account and Person deletion rules consistent with "do not promise permanent retention where law may require deletion"?
11. **Notifications (M-02).** Are correction notices protected from batching?
12. **Open items.** Are any OPEN items described as decided? (Check `DECISIONS.md` §4A.)
13. **Missing requirements.** What is absent for a safe first release?
14. **Performance (H-08).** Is the truncation state sufficient? Is an unbounded enumeration path avoided?

## 5. Open risks and trade-offs the reviewer should weigh

- Recursive enumeration cost grows with pedigree collapse (synthetic benchmark only; not measured in this closure).
- The one-active-account and one-father invariants depend on the concurrency mechanism, which is not yet proven.
- Shared-relative discovery is proposed to be narrowed; the owner must confirm.
- The visibility matrix (OQ-21-03) is open, so visibility behaviour beyond default deny is unspecified.
- Legal review (retention, pseudonymous audit identifiers, crypto-erase, deceased-person privacy) is not performed.

## 6. What the reviewer must return

- The 14 answers above, with the section cited for each.
- The commands run and their results.
- A list of critical findings, with severity.
- A statement of which documents were read in full.

No reviewer output has been received. Until it is received, the status of this review is NOT PERFORMED.
