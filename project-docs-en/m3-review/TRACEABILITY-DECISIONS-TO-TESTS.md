# Traceability: Owner Decisions to Documents and Future Tests

**Status:** links decisions to documents and to the tests that must exist before a phase is accepted. A test listed here is **planned**; it is NOT VERIFIED until it exists and runs.

| Decision group | Decision IDs | Governing document | Future test (phase) |
|---|---|---|---|
| Biological parentage invariants | DD-08, P14, P15, P16 | `DATABASE-DESIGN-READINESS.md` §4; TD-01 | Concurrency: two fathers, cycle, parallel transfers (P3, P5) |
| Biological source of truth | DD-09, DD-11, P1, Q2 | `TECHNICAL-DECISIONS.md` TD-07 | Edge-isolation: marriage and nursing never enter traversal (P4) |
| M0 correctness | DD-12, DD-13, P17 | `m0-verification-report.md` | 22 fixtures and mutation checks (P4, mandatory regression) |
| Incomplete search | DD-14, DD-30, R-05 | TD-05 | Result state tests: a budget stop never returns absence (P4, P7) |
| Account and Person separation | DD-04, DD-05, R-07, Q13 | `DECISIONS.md` §3A; domain notes | Person without account; no auto-merge on name (P2) |
| One active account | DD-18, OQ-21-19 | TD-02 | Concurrent activation race (P1, P8) |
| Verification of association | DD-19, OQ-21-10 | E-01 | Association refused without verification (P8) |
| Network membership | DD-06, DD-24, R-06 | DATABASE-DESIGN-READINESS Part 1 | Leave keeps record; rejoin restores same Person (P2) |
| Visibility separation | DD-07, DD-20, DD-37 | `FINAL-OWNER-DECISION-RECONCILIATION-PART2.md` §8.1 | Path visible, sensitive field hidden (P6, P7) |
| RLS and isolation | DD-21, P12 | TD-04 | Cross-network, cross-user, owner bypass, pooling reset (P5) |
| Audit | DD-15, DD-22, DD-35 | TD-09, TD-10 | Append-only enforcement; rollback test; sensitive masking (P5) |
| Governance | DD-15, DD-16, DD-17 | `OWNER-DECISION-REGISTER-PART1-DD01-DD20.md` | Rejection kept; resubmission needs new evidence (P3) |
| Correction effective time | DD-33 | TD-11 | Atomic commit; previous value retained (P3) |
| Accountless sensitive changes | DD-34 | `FINAL-OWNER-DECISION-RECONCILIATION-PART2.md` §7 | Creator cannot edit sensitive field alone (P3) |
| Critical notifications | DD-32 | TD-12 | Critical item survives daily limit (P11) |
| Account deletion | DD-25 | E-03 | Shared lineage retained only with basis (P6, after review) |
| Sessions and security | DD-27 | TD-13 | Terminate other sessions; new-device notice (P1) |
| Blocking and abuse | DD-28 | E-05 | Block does not delete relationships (P11) |
| Imports | DD-26, R-13 | TD-15 | No automatic confirmation; duplicates flagged (P10) |
| Search | DD-38, §14.11 | `DECISIONS.md` | Search never renames or merges (P7) |
| Internationalization | DD-29, R-11 | `IMPLEMENTATION-ROADMAP.md` P12 | Phone format and locale tests per country (P12) |

## Status legend

- PLANNED: test listed, not written.
- VERIFIED: test written and run with observed result recorded. None is VERIFIED yet except the M0 regression, which is recorded in `m0-verification-report.md`.
