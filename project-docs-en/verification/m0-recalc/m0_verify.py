"""
Independent M0 verification runner (read-only against the protected fixture).

Usage (from any directory):  python m0_verify.py
Exit code 0 only if the fixture hash matches Phase A, all 22 cases pass, and self-tests pass.

Fields not defined by M0 (sibling_type, shared_ancestor_lines,
lineage_side_on_shared_ancestor_path) are NOT verified and are reported as such.
"""
import hashlib
import json
import sys
from pathlib import Path

from m0_core import GraphError, build_graph, canonical, classify, compute, max_paths_per_ancestor, pair_record

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "project-docs" / "reference-fixtures" / "kinship-reference-cases.json"
PHASE_A_SHA256 = "FF52DF522E07ADFC59EB84F78A5B27D007CF636D67228898DFFEA03E07243A46"
PHASE_A_BYTES = 37807
EXPECTED_IDS = {
    "T01", "T02", "T03", "T04", "T05", "T06", "T07", "T08", "T09", "T10", "T11",
    "T12", "T13", "T14", "ST-01", "ST-02", "ST-03", "ST-04", "ST-05", "ST-06",
    "DI-05a", "DI-05b",
}
NOT_VERIFIED_FIELDS = ("sibling_type", "shared_ancestor_lines", "lineage_side_on_shared_ancestor_path")


def check_sets(exp, res, records, expected_pairs, failures):
    """Compare COMMON, J, R and the set of valid pairs. Returns number of checks run."""
    checks = 3
    if sorted(exp["common_ancestors"]) != res["common"]:
        failures.append(f"COMMON expected {sorted(exp['common_ancestors'])} got {res['common']}")
    if sorted(exp["valid_junction_ancestors"]) != res["junctions"]:
        failures.append(f"J expected {sorted(exp['valid_junction_ancestors'])} got {res['junctions']}")
    if exp["valid_path_pair_count"] != len(records):
        failures.append(f"R expected {exp['valid_path_pair_count']} got {len(records)}")
    checks += 2
    missing = set(expected_pairs) - set(records)
    extra = set(records) - set(expected_pairs)
    if missing:
        failures.append(f"{len(missing)} expected valid pair(s) not produced")
    if extra:
        failures.append(f"{len(extra)} produced valid pair(s) not in fixture")
    return checks


def check_pair_fields(e, r, key, failures):
    """Compare a, b, L and derived classification fields for one matched pair. Returns checks run."""
    checks = 0
    for field in ("a", "b", "L"):
        checks += 1
        if e[field] != r[field]:
            failures.append(f"{key[0]} {field} expected {e[field]} got {r[field]}")
    if "structural_classification" in e:
        checks += 1
        derived = classify(r["a"], r["b"])
        if e["structural_classification"] != derived:
            failures.append(f"{key[0]} class expected {e['structural_classification']} derived {derived}")
    if "generation_distance" in e:
        checks += 1
        if e["generation_distance"] != max(r["a"], r["b"]):
            failures.append(f"{key[0]} generation_distance mismatch")
    if r["a"] >= 2 and r["b"] >= 2:
        for name, derived in (("cousin_degree", min(r["a"], r["b"]) - 1), ("removal", abs(r["a"] - r["b"]))):
            if name in e:
                checks += 1
                if e[name] != derived:
                    failures.append(f"{key[0]} {name} expected {e[name]} derived {derived}")
    return checks


def check_case(case, graph):
    """Return (failures, checks_run) for one fixture case."""
    query = case["query"]
    exp = case["expected"]
    res = compute(graph, query["person_a"], query["person_b"])
    records = {canonical(r): r for r in (pair_record(*v) for v in res["valid"])}
    expected_pairs = {canonical(r): r for r in exp["valid_path_pairs"]}
    failures = []
    checks = check_sets(exp, res, records, expected_pairs, failures)
    for key in sorted(set(expected_pairs) & set(records), key=str):
        checks += check_pair_fields(expected_pairs[key], records[key], key, failures)
    for entry in exp.get("excluded_candidate_pairs", []):
        checks += 1
        anc = entry["ancestor_id"]
        if anc not in res["common"] and res["invalid_count"].get(anc, 0) < 1:
            failures.append(f"excluded candidate at {anc} not supported by C.5")
    return failures, checks



def self_tests():
    results = []

    def expect_error(name, people):
        try:
            build_graph(people)
        except GraphError as exc:
            results.append((name, True, str(exc)))
        else:
            results.append((name, False, "no error raised"))

    expect_error("two-node father cycle is rejected",
                 [{"id": "X", "father_id": "Y", "mother_id": None}, {"id": "Y", "father_id": "X", "mother_id": None}])
    expect_error("self-parent cycle is rejected", [{"id": "X", "father_id": "X", "mother_id": None}])
    expect_error("duplicate person id is rejected",
                 [{"id": "X", "father_id": None, "mother_id": None}, {"id": "X", "father_id": None, "mother_id": None}])
    expect_error("unknown parent reference is rejected", [{"id": "X", "father_id": "NOPE", "mother_id": None}])
    return results


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raw = FIXTURE.read_bytes()
    digest = hashlib.sha256(raw).hexdigest().upper()
    print(f"FIXTURE_PATH {FIXTURE}")
    print(f"FIXTURE_BYTES {len(raw)} (Phase A recorded {PHASE_A_BYTES})")
    print(f"FIXTURE_SHA256 {digest}")
    print(f"FIXTURE_SHA256_MATCHES_PHASE_A {digest == PHASE_A_SHA256}")

    cases = json.loads(raw.decode("utf-8"))["cases"]
    ids = [c["case_id"] for c in cases]
    id_set_ok = set(ids) == EXPECTED_IDS and len(ids) == len(set(ids))
    print(f"CASE_COUNT {len(cases)} UNIQUE_IDS {len(set(ids))} EXPECTED_SET_MATCH {id_set_ok}")

    passed = 0
    total_checks = 0
    multi_path_cases = 0
    nv_seen = set()
    for case in cases:
        graph = build_graph(case["people"])
        failures, checks = check_case(case, graph)
        total_checks += checks
        for field in NOT_VERIFIED_FIELDS:
            if field in json.dumps(case["expected"]):
                nv_seen.add(field)
        q = case["query"]
        depth = max_paths_per_ancestor(graph, q["person_a"], q["person_b"])
        if depth > 1:
            multi_path_cases += 1
        status = "PASS" if not failures else "FAIL"
        if not failures:
            passed += 1
        print(f"CASE {case['case_id']:<7} {status} checks={checks} max_paths_per_ancestor={depth}")
        for msg in failures:
            print(f"    FAILURE: {msg}")

    print(f"TOTAL_CHECKS {total_checks}")
    print(f"CASES_WITH_MULTIPLE_PATHS_TO_ONE_ANCESTOR {multi_path_cases}/{len(cases)}")

    print("SELF_TESTS:")
    self_ok = True
    for name, ok, detail in self_tests():
        self_ok = self_ok and ok
        print(f"  {'PASS' if ok else 'FAIL'} {name} ({detail})")

    print(f"NOT_VERIFIED_M0_FIELDS_PRESENT {sorted(nv_seen)} (not defined by M0; excluded from pass/fail)")
    print(f"SUMMARY: {passed}/{len(cases)} cases pass all M0 checks; self-tests {'pass' if self_ok else 'FAIL'}")
    ok_all = passed == len(cases) and self_ok and digest == PHASE_A_SHA256 and id_set_ok
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
