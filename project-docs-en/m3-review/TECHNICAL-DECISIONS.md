# Technical Decisions (Engineering Choices, Not Owner Decisions)

**Status:** engineering decisions made to implement the approved owner decisions. Each has a rationale and trade-offs. These are **technical design choices**, recorded separately from owner decisions. Any of them can be revised by engineering review without owner approval, provided the owner decisions are still met.

| ID | Choice | Rationale | Trade-off and limit |
|---|---|---|---|
| TD-01 | Biological invariants (one father, one mother, no cycle) enforced by a partial unique index on `(network_id, child_id, role)` for adopted parentage, plus a transaction-scoped advisory lock per network before any adopted-graph write, plus a recursive cycle check in the same transaction | A row lock on the child is insufficient (a cycle spans rows). The index is the last line of defence; the lock serializes graph writes; the check detects cycles on a stable graph | Per-network lock serializes writes in one network. Acceptable for family-sized graphs. Must be proven by concurrency tests (see `DATABASE-DESIGN-READINESS.md` §4) |
| TD-02 | Single active account per Person enforced by a partial unique index on active links | Database-level guarantee against races, per DD-18 | None beyond the index |
| TD-03 | Account-to-many-Person association modelled as an explicit, constrained table with its own verification state, default OFF | DD-36: not assumed approved. Prevents silent one-account-many-person control | If the owner later approves it, only the constraint changes |
| TD-04 | RLS network isolation through a `network_id` on every network-scoped row, with policies checking active membership; session identity set per transaction by the application | Enforces P12 and DD-21 at the database boundary; keeps application authorization primary | Requires careful policy design; tested in P5 |
| TD-05 | Path computation by recursive traversal over the adopted graph with explicit enumeration budgets; result states `complete`, `paginated`, `truncated` | DD-14, DD-30: incomplete search never reads as absence | Budget values are configuration, measured in P4 |
| TD-06 | Derived all-paths cache not introduced in the first release | Cache adds consistency risk; recursive reference first (M3-01 §8.4 recommendation) | Performance may need the cache later; must pass equivalence tests first |
| TD-07 | Marriage, affinity, nursing, and guardianship stored in a separate edge table, never joined into the biological traversal | DD-09, DD-11, GOV-011 | Mixed-path queries need an explicit join with labels |
| TD-08 | Field-level encryption with a managed key; exact-match lookup via a separate HMAC over normalized values | DD-23; keeps plaintext out of indexes | Normalization rules must be versioned; HMAC key rotation needs a re-index plan |
| TD-09 | Audit table is append-only at the database role level (no UPDATE or DELETE grant to application roles); sensitive values in a separate encrypted column | DD-22, DD-35 | Audit reads require a separate role and logged access path |
| TD-10 | State change and audit row written in one transaction with a forced-failure test | P3, DD-15 | None |
| TD-11 | Corrections applied atomically on approval commit; previous value preserved in history | DD-33, Q17 | Effective time equals commit time |
| TD-12 | Notifications: queue with priority classes; critical class bypasses daily limits and is never dropped; pending items retained | DD-32 | Critical class needs strict classification review (E-05 adjacent) |
| TD-13 | Session handling: opaque server-side session records bound to a device record; revocation by row update | DD-27 | Needs a session store; not a JWT-only design |
| TD-14 | Appeal review assigned to a reviewer who did not take the original action | DD-28 ("independent review") | Requires reviewer pool |
| TD-15 | Import staging area with preview, validation, duplicate candidates; no write to confirmed state until a user commits | DD-26; no auto-confirmation | Staging table retention policy needed |

## Notes

- Every TD item must have its corresponding test listed in the traceability matrix before its phase is accepted.
- TD-01 and TD-04 are high-risk and fall under the independent review gate (`IMPLEMENTATION-ROADMAP.md`).
