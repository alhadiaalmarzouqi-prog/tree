# Implementation Roadmap (Foundation-First)

**Status:** planning artifact derived from `DECISIONS.md` and the consolidated register (`OWNER-DECISION-REGISTER-CONSOLIDATED.md`). It does not authorize production work by itself. Each phase lists its own gate.
**Principle (DD-40):** identity, relationship and governance lifecycle, M0 correctness, audit, and RLS come before social features.

## Phase overview

| Phase | Scope | Gate before start | Status |
|---|---|---|---|
| P0 Foundation | Repository layout, NestJS and Flutter skeletons, PostgreSQL local environment, CI runner, lint and test tooling | Owner approves the technology baseline (already in DD-03) | Implemented 2026-11-03. Backend + M0 verified; Flutter/PostgreSQL/CI + `npm audit` detail UNVERIFIED due to environment. See `P0-FOUNDATION-EXECUTION-REPORT.md`. Awaiting owner acceptance of the environment-dependent limitations before P0 is marked COMPLETE |
| P1 Identity | Account registration by phone OTP, sessions, device list, login history, session termination, new-device notice | P0 complete; legal and privacy review of login-history retention (external dependency E-06) | Not started |
| P2 Person and networks | Person records (accountless and deceased allowed), network membership, multi-network intersection, leave and rejoin | P1 complete | Not started |
| P3 Relationship and governance | Proposals, evidence attachment, network decisions, objections, rejection with reasons, audited corrections, atomic effective time | P2 complete; governance parameters configurable (no fixed numbers, DD-17) | Not started |
| P4 M0 engine | Recursive reference engine over the adopted graph; the 22 fixtures and mutation tests as mandatory regression | P3 data model stable; M0 unchanged | Harness exists (see Verification) |
| P5 Audit and RLS | Append-only audit, same-transaction writes, RLS with network isolation, concurrency tests for biological invariants | Must be built with P2–P3 tables, not after | Not started |
| P6 Privacy and account lifecycle | Field-level visibility, account and Person deletion workflows, data export rights, support staff restrictions | Legal and privacy review (E-02, E-03) before production release | Not started |
| P7 Discovery and navigation | Kinship path search (incomplete-state aware), shared-relative discovery, cross-network paths, dashboard | P4, P5, P6 | Not started |
| P8 Identity association | Account-to-Person verification workflow, duplicate suggestions, controlled reconciliation | Verification method decided with legal review (E-01) | Not started |
| P9 Social features | Posts, comments, reactions, subgroups, invitations, favorites, sharing | P5, P6 | Not started |
| P10 Imports, exports, backups | GEDCOM, Excel, CSV import with preview; PDF, image, structured export; personal backups | P3, P5 | Not started |
| P11 Notifications and support | Batched notifications with critical bypass; support tickets; abuse, blocking, impersonation workflow, appeal | P1, P5 | Not started |
| P12 Internationalization | Arabic and English, country phone formats, time zones, locale extensibility | Can run in parallel from P1 onward | Not started |
| P13 Pilot readiness | Security testing, backup recovery drill, incident response, owner approval of pilot | All above; external dependencies closed | Not started |

## Per-phase definition (required for each phase)

Every phase defines: **scope**, **deliverables**, **dependencies**, **acceptance criteria**, **automated tests**, **security and privacy tests**, and **migration and rollback notes** (where a schema change is involved). Phase files are created when the phase starts, not in advance.

## Safety rules across phases

- No feature bypasses tenant, network, or relationship authorization.
- No relationship write bypasses governance.
- No account operation silently creates or merges Person records.
- No sensitive data is public by default.
- No production migration runs without its phase gate. For P3, P5, and P6, the required independent review must be completed and recorded before the migration is promoted to production (see the review gate note; owner directive 2026-11-03).
- The M0 regression suite runs on every change that touches calculation code.

## Independent review gate

**Current rule (owner directive, 2026-11-03):** independent AI review and independent human engineering review are **no longer prerequisites for starting implementation**. They are moved into the implementation lifecycle, per `OWNER-DIRECTIVE-2026-11-03-REVIEW-LIFECYCLE.md`. Reviews must be performed during or after the relevant phase and **completed before passing these high-risk gates**:

- P3 — relationship-governance writes;
- P5 — RLS and concurrency enforcement;
- P6 — privacy and deletion implementation.

A review is not represented as completed until it has actually occurred and left a review record. The directive does not weaken automated tests, security validation, or acceptance criteria.

**Superseded rule (historical record, retained):** the Q11 gate (independent AI review and independent human engineering review, then owner approval of the outcome) was a prerequisite before any implementation of high-risk phases. Its text was: "The Q11 gate (independent AI review and independent human engineering review, then owner approval of the outcome) applies to high-risk phases: P3 (governance and relationship writes), P5 (RLS and concurrency), and P6 (privacy and deletion). It does not block P0, P1 foundations, or P12 internationalization work. The status of this gate is recorded in `IMPLEMENTATION-READINESS-REPORT.md` and must not be treated as satisfied until real review evidence exists." This prerequisite is superseded for the start of implementation by the 2026-11-03 owner directive. The Q11 decision in `DECISIONS.md` §3 and the historical records are not altered by this note.
