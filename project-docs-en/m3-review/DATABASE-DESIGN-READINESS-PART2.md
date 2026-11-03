# Database Design Readiness (Part 2 of 2): RLS, Lifecycle, Path Storage, Tests

**Status: DESIGN PROPOSAL. Not approved. No SQL, migrations, or policies are created here.**
**Continuation of:** `DATABASE-DESIGN-READINESS.md` (Part 1: §1 source rules, §2 mapping, §3 marriage and nursing, §4 concurrency).

---

## 5. Accountless and deceased records (H-04, OQ-21-12)

Proposed permission table. Field classification is a feature-design item.

| Action | Creator of an accountless Person | Eligible network member | Active Person owner | Support staff |
|---|---|---|---|---|
| Create Person | yes, basic fields | via proposal | yes | no |
| Edit basic non-sensitive field | yes, while accountless | per governance | yes | no |
| Edit sensitive field | additional authorization (mechanism: owner decision) | additional authorization | yes | no |
| Change any relationship | no | network governance only | network governance | no |
| Read sensitive field | only if visibility allows | per visibility | per visibility | no |
| Deceased record | sensitive fields stay protected (OQ-21-12) | same | same | no |

Creation confers no ownership of the Person or their lineage (Q8). Support staff never receive unrestricted access to family networks.

---

## 6. Path computation and derived storage (M0, H-08)

- **Canonical source:** `adopted_parentage` rows per network (Q2). Derived data must be reproducible from them.
- **Reference engine:** recursive traversal over the adopted graph, with explicit limits. It is the equivalence reference.
- **Cache (optional, not selected):** an all-paths cache may be added only after an equivalence test against the reference passes on all 22 fixtures and on generated networks. It is rebuilt in the same transaction as the change that invalidates it (`M3-01` §8.4).
- **Truncation (H-08):** each result has state `complete`, `truncated`, or `no recorded kinship`. `truncated` is never shown as absence. The limit is configuration; no number is set.
- **Result metadata (AGENT-PROPOSAL, `DECISIONS.md` §3B.5):** network identifier, adopted-input version, M0 specification version, timestamp.

---

## 7. Row-level security (P12, Q9, M-03, M-04)

- **Layering:** application authorization is mandatory for every read and write. RLS is an additional database boundary. Neither replaces the other (P12, Q9).
- **Network boundary (M-04, design option):** each network-scoped row carries `network_id`. Policies allow access only where the session's authenticated Person has an active membership for that `network_id`. The session identity is set per transaction by the application, never taken from the client.
- **Prerequisites before writing policies (M-03):** H-01 membership model; H-04 permission table (§5); OQ-21-03 visibility matrix. Policies are NOT written until these are approved.
- **Owner and bypass (Q9):** examine table-owner bypass, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, and application roles. The application role must not own the tables or hold `BYPASSRLS`. Status: NOT VERIFIED; no database exists.
- **Connection pooling:** the session identity is reset at every pooled checkout. A test must show that a reused connection cannot inherit the previous user's identity.


---

## 8. Audit model (P2, P3, Q1, Q7, H-07)

- **Append-only:** ordinary application roles may INSERT audit rows only, never UPDATE or DELETE. Enforced at the database-role level and tested.
- **Same transaction:** each state change and its audit row commit together (P3). Test: a forced failure after the state write leaves neither change.
- **Content:** actor, timestamp, change type, affected fields, and old and new values where permitted.
- **Sensitive values (H-07):** a field hidden from a viewer is hidden in audit reads too. Sensitive audit values are encrypted under a separately controlled key. Ordinary users see only their own changes.
- **Retention (Q7):** no automatic expiry; ordinary functions never delete audit rows. Legal review of pseudonymous identifiers and crypto-erase is open (DR-19 remainder).

---

## 9. Lifecycle, deletion, and recovery

- **Account deletion:** removes credentials and the personal data that law requires to be removed. Shared family information is kept only where a legal basis permits, shown under a neutral label such as "former contributor". Relationships are not deleted merely because an account is deleted.
- **Person-record deletion request:** assessed against the requester's rights, other affected persons, and legal duties. Delete or anonymize what must go; retain shared family information only where legally permitted.
- **Membership exit:** the Person record and relationships remain; adopted facts stay with the network that adopted them.
- **Backup and key recovery (P13):** must be documented before production. Key custody, rotation, and recovery are NOT designed here.

---

## 10. Test plan (required artifacts)

| Test | Purpose | Status |
|---|---|---|
| M0 fixture regression (`verification/m0-recalc/m0_verify.py`) | Protects the 22 fixtures | VERIFIED this session: 22/22, 328 checks |
| M0 mutation sensitivity (`m0_mutation_check.py`) | Proves the harness can fail | VERIFIED: 7/7 |
| Engine equivalence: recursive reference versus any cache | Required before a cache | NOT VERIFIED (no engine) |
| Concurrency: two fathers, cycle, two active accounts | H-05 proof | NOT VERIFIED (no database) |
| RLS: cross-user, cross-network, direct DB access, pooled reuse, table owner, `BYPASSRLS` | P12, Q9 | NOT VERIFIED (no database) |
| Audit: same-transaction rollback, append-only enforcement | P2, P3 | NOT VERIFIED (no database) |
| Edge isolation: marriage and nursing edges never reach the engine | GOV-011, GOV-012, P10 | NOT VERIFIED (no engine) |

---

## 11. Items that block physical schema approval

1. The Q11 independent AI review (separate reviewer) and the human engineer review, then owner approval.
2. Owner decisions: OQ-21-03, OQ-21-05, OQ-21-10, H-02, the H-04 "additional authorization" mechanism, H-09 scope confirmation, and CG-29.
3. The concurrency proof (Part 1 §4) and the RLS tests (§10) run against PostgreSQL before any production migration.
