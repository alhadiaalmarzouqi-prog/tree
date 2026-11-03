# M0 Verification Report (Independent Recalculation)

**Date:** 2026-11-03. **Status:** VERIFIED for the 22 fixtures and the checks listed below. Not a formal proof of M0 for all possible graphs.
**Protected inputs (read only):** `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` (M0, Arabic, protected); `project-docs/reference-fixtures/kinship-reference-cases.json` (22 fixtures, protected); `project-docs-en/08-MATHEMATICAL-REFERENCE.md` (English restatement, read only).
**Harness:** `project-docs-en/verification/m0-recalc/` (Python 3.12.10, standard library only, no installed packages).

---

## 1. Protected-file integrity (observed in this session)

| File | SHA-256 observed | Phase A record | Result |
|---|---|---|---|
| `project-docs/reference-fixtures/kinship-reference-cases.json` | `FF52DF522E07ADFC59EB84F78A5B27D007CF636D67228898DFFEA03E07243A46` (37,807 bytes) | same | MATCH |
| `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` | `B69AD1DF6188EB12FA77A125BFBB299B25AEFBCA1BB265B81F97443F0250DD45` (18,147 bytes) | `B69AD1DF...` in `00-SOURCE-MANIFEST` row 7 and `phase-a-verification-output.txt` | MATCH |
| `project-docs-en/08-MATHEMATICAL-REFERENCE.md` | `315010AF8719615C1BEB53388BBCE954EB2174D2CB3D20E7C6902FED81DB8EBB` | not in Phase A manifest (English restatement, not a protected source) | recorded only; NOT VERIFIED against a baseline |

No protected file was written. The harness opens the fixture in read-only mode.

---

## 2. Reproducible commands

```
cd "project-docs-en/verification/m0-recalc"
set PYTHONIOENCODING=utf-8
python m0_verify.py          > m0-verify-output.txt
python m0_mutation_check.py  > m0-mutation-output.txt
```

- `m0_core.py`: M0 definitions (graph rules B.1, paths C.1, path count C.3, COMMON C.4, valid pairs C.5, J C.6, R C.7, a/b/L C.8–C.9, classification C.10–C.13).
- `m0_verify.py`: loads the fixture, checks its hash, compares every expected output, runs graph-rule self-tests.
- `m0_mutation_check.py`: checks that the harness rejects 7 deliberately wrong expectations.

---

## 3. Observed results

**Fixture verification** (`m0-verify-output.txt`, exit code 0):

- `FIXTURE_SHA256_MATCHES_PHASE_A True`; `CASE_COUNT 22 UNIQUE_IDS 22 EXPECTED_SET_MATCH True`.
- All 22 cases `PASS`; `TOTAL_CHECKS 328`.
- `CASES_WITH_MULTIPLE_PATHS_TO_ONE_ANCESTOR 9/22`.
- Self-tests `PASS`: two-node cycle, self-parent cycle, duplicate ID, unknown parent.

**Mutation check** (`m0-mutation-output.txt`):

- `MUTATIONS_DETECTED 7/7`: R off by one; removed valid pair; wrong a-distance; wrong cousin degree; wrong removal; wrong J; wrong role sequence. Each was caught.

**Harness defects found and fixed during this session (recorded, not hidden):**

1. The first run crashed with `UnicodeEncodeError` on the Windows console because the fixture path contains Arabic. Output was re-routed as UTF-8 (`sys.stdout.reconfigure`). No M0 result was affected: the crash happened before any check ran.
2. The first shell redirect wrote the output with a byte-order mark and an encoding the default shell tool did not capture cleanly. The final outputs were regenerated with `PYTHONIOENCODING=utf-8` and `Out-File -Encoding utf8`; the stored files are the regenerated ones.

---

## 4. Coverage against M0 requirements

| M0 requirement | Checked by harness | Notes |
|---|---|---|
| Common ancestors (COMMON, C.4) | Yes, all 22 | Compared as sets. |
| Valid junction pairs (C.5) | Yes, all 22 | Vertex sets must intersect only at the ancestor. |
| Non-overlapping paths except at ancestor | Yes | Enforced by C.5 check. |
| Valid path-pair count R (C.7) | Yes, all 22 | Count and identity of every pair. |
| Path count per ancestor (C.3) | Indirectly | Every expected pair is matched as a full path; max paths per ancestor reported. |
| Path length a, b, L (C.8–C.9) | Yes | Per pair. |
| Direct line (C.10) | Yes | Via classification and generation distance. |
| Sibling (1,1) (C.11) | Yes | Classification only; sibling_type is NOT verified (not defined in M0). |
| Avuncular (C.12) | Yes | Classification only; the direction and gender part of the name is NOT verified (DR-16). |
| Cousin degree and removal (C.13) | Yes | Derived only where a, b ≥ 2. |
| Parent-role sequences | Yes | Each expected path's node and role sequence is matched exactly. |
| Multiple shared ancestors | Yes | T11, T12, ST-series, DI-05a/b. |
| Overlapping paths and invalid junction pairs | Yes | Excluded candidate pairs are checked for C.5 support. |
| No recorded common ancestor (T14) | Yes | Empty set and R = 0. |
| Acyclic graph (B.1(5)) | Yes | Self-tests reject cycles. |

**NOT VERIFIED (not defined by M0, excluded from pass/fail):** `sibling_type`, `shared_ancestor_lines`, `lineage_side_on_shared_ancestor_path`. These appear in the fixture but M0 does not define them, so they cannot be checked against M0.

---

## 5. Limits of this verification

- The harness is written by this session's agent from the M0 definitions. It is an independent recalculation, not a formal proof and not an independent human check. A human engineer must still re-derive a sample by hand (Q11).
- Verification covers 22 fixtures. It does not prove that M0 covers every possible family graph (`KINSHIP-MATHEMATICAL-REFERENCE.md` §F item 1).
- Per-network application (OQ-21-16) is NOT tested. The harness computes a single static graph.
- Performance is NOT measured. The harness is exhaustive enumeration and is for small fixtures only.
- Arabic and English naming (DR-16, KD-01, KD-02) is NOT verified.

---

## 6. Status

- M0 fixture recalculation: **VERIFIED** (22/22, 328 checks, reproduced).
- M0 mutation sensitivity: **VERIFIED** (7/7).
- Human re-derivation: **NOT PERFORMED** (required by Q11 before production).
- M0 as a regression suite for the future engine: **READY** (the harness is the baseline; it must run unchanged in CI).
