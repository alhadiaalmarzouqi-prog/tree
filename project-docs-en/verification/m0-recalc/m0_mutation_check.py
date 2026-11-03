"""
Mutation check for the M0 harness: the harness must REJECT deliberately wrong expectations.
Each mutation changes one expected value in memory only (the fixture file is never written).
Exit code 0 only if every mutation is detected.
"""
import copy
import json
import sys

from m0_core import build_graph
from m0_verify import FIXTURE, check_case

MUTATIONS = [
    ("R off by one (T08)", "T08", lambda c: c["expected"].__setitem__("valid_path_pair_count", 3)),
    ("removed valid pair (ST-01)", "ST-01", lambda c: c["expected"]["valid_path_pairs"].pop()),
    ("wrong a-distance (T03)", "T03", lambda c: c["expected"]["valid_path_pairs"][0].__setitem__("a", 9)),
    ("wrong cousin degree (T08)", "T08", lambda c: c["expected"]["valid_path_pairs"][0].__setitem__("cousin_degree", 2)),
    ("wrong removal (T09)", "T09", lambda c: c["expected"]["valid_path_pairs"][0].__setitem__("removal", 0)),
    ("wrong J (T12)", "T12", lambda c: c["expected"].__setitem__("valid_junction_ancestors", ["Gf"])),
    ("wrong role sequence (T02)", "T02",
     lambda c: c["expected"]["valid_path_pairs"][0]["path_a"].__setitem__("roles", ["MOTHER", "FATHER"])),
]


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    base = json.loads(FIXTURE.read_bytes().decode("utf-8"))["cases"]
    detected = 0
    for name, case_id, mutate in MUTATIONS:
        case = copy.deepcopy(next(c for c in base if c["case_id"] == case_id))
        mutate(case)
        failures, _ = check_case(case, build_graph(case["people"]))
        caught = len(failures) > 0
        detected += caught
        print(f"{'DETECTED' if caught else 'MISSED  '} {name}: {failures[0] if failures else 'no failure raised'}")
    print(f"MUTATIONS_DETECTED {detected}/{len(MUTATIONS)}")
    return 0 if detected == len(MUTATIONS) else 1


if __name__ == "__main__":
    sys.exit(main())
