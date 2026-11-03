"""Phase A verification (M2-R7A). Read-only with respect to all source files.

Writes only to project-docs-en/verification/phase-a-verification-output.txt.
"""
import hashlib
import json
import os
import re
import sys

ROOT = r"C:\Users\test\Desktop\شجرة العائلة"
OUT_DIR = os.path.join(ROOT, "project-docs-en", "verification")
OUT_FILE = os.path.join(OUT_DIR, "phase-a-verification-output.txt")
MANIFEST = os.path.join(ROOT, "project-docs-en", "00-SOURCE-MANIFEST.md")

SOURCE_FILES = [
    "CLAUDE.md",
    r"project-docs\MASTER-ARCHITECTURE.md",
    r"project-docs\analysis\ANALYSIS-REPORT.md",
    r"project-docs\analysis\CONFLICTS-AND-GAPS.md",
    r"project-docs\analysis\DECISION-REGISTER.md",
    r"project-docs\analysis\DECISIONS-REQUIRED.md",
    r"project-docs\analysis\KINSHIP-MATHEMATICAL-REFERENCE.md",
    r"project-docs\analysis\REQUIREMENTS.md",
    r"project-docs\analysis\TRACEABILITY-MATRIX.md",
    r"project-docs\handoffs\NEXT-AGENT.md",
    r"project-docs\reference-fixtures\kinship-reference-cases.json",
    r"project-docs\standards\AGENT-EXECUTION-RULES.md",
    r"project-docs\standards\CODE-ORGANIZATION-RULES.md",
    r"project-docs\standards\DOCUMENTATION-STANDARDS.md",
]

EXPECTED_IDS = ["T01","T02","T03","T04","T05","T06","T07","T08","T09","T10","T11","T12","T13","T14",
                "DI-05a","DI-05b","ST-01","ST-02","ST-03","ST-04","ST-05","ST-06"]

lines_out = []


def out(s=""):
    lines_out.append(s)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def physical_lines(raw):
    nl = raw.count(b"\n")
    ends = raw.endswith(b"\n")
    return (nl if ends else nl + 1), ends


def task1():
    out("== TASK 1: FULL READING ==")
    fixture = os.path.join(ROOT, r"project-docs\reference-fixtures\kinship-reference-cases.json")
    trace = os.path.join(ROOT, r"project-docs\analysis\TRACEABILITY-MATRIX.md")

    raw = open(fixture, "rb").read()
    text = raw.decode("utf-8-sig")
    n, ends = physical_lines(raw)
    out(f"fixture bytes={len(raw)} physical_lines={n} ends_with_newline={ends} chars_processed={len(text)}")

    data = json.loads(text)
    cases = data["cases"]
    ids = [c["case_id"] for c in cases]
    out(f"fixture JSON parse=OK case_count={len(cases)} unique_ids={len(set(ids))}")
    out("fixture case_ids=" + ",".join(ids))
    missing = [i for i in EXPECTED_IDS if i not in ids]
    extra = [i for i in ids if i not in EXPECTED_IDS]
    out(f"fixture expected_22_present={not missing and not extra} missing={missing} extra={extra}")

    issues = []
    for c in cases:
        for key in ("case_id", "description", "query", "people", "expected"):
            if key not in c:
                issues.append(f"{c.get('case_id')} missing key {key}")
        exp = c.get("expected", {})
        if "valid_path_pair_count" in exp and exp["valid_path_pair_count"] != len(exp.get("valid_path_pairs", [])):
            issues.append(f"{c['case_id']} valid_path_pair_count != len(valid_path_pairs)")
    out(f"fixture structural check={'OK' if not issues else 'ISSUES: ' + '; '.join(issues)}")

    traw = open(trace, "rb").read()
    ttext = traw.decode("utf-8-sig")
    tn, tends = physical_lines(traw)
    out(f"trace-matrix bytes={len(traw)} physical_lines={tn} ends_with_newline={tends} chars_processed={len(ttext)}")
    tids = sorted(set(re.findall(r"\b(?:FR|PRV|SEC|GOV|TECH|DATA|PERF|OPS|TST|SCOPE|PLAN)-\d{3}\b", ttext)))
    out(f"trace-matrix unique requirement IDs referenced={len(tids)}")
    out("")
    return raw, traw



def task2():
    out("== TASK 2: SHA-256 REVERIFICATION ==")
    mtext = open(MANIFEST, "r", encoding="utf-8").read()
    rows = re.findall(r"\| \d+ \| `([^`]+)` \| (\d+) \| (\d+) \| ([A-F0-9]{64}) \|", mtext)
    manifest_map = {r[0]: (r[3], int(r[1])) for r in rows}
    out(f"manifest rows parsed={len(rows)}")
    mismatches = 0
    for rel in SOURCE_FILES:
        p = os.path.join(ROOT, rel)
        ch = sha256_file(p)
        sz = os.path.getsize(p)
        if rel not in manifest_map:
            out(f"NOT_IN_MANIFEST path={rel} current={ch}")
            mismatches += 1
            continue
        mh, msz = manifest_map[rel]
        ok = (mh == ch and msz == sz)
        mismatches += 0 if ok else 1
        out(f"{'MATCH' if ok else 'MISMATCH'} path={rel} manifest={mh} current={ch} "
            f"manifest_bytes={msz} current_bytes={sz}")
    out(f"manifest_only={[k for k in manifest_map if k not in SOURCE_FILES]}")
    out(f"TOTAL mismatches={mismatches}")
    out("")
    return mismatches


def tree_check():
    out("== TREE INVENTORY (outside project-docs-en) ==")
    found = []
    for dp, _dn, fn in os.walk(ROOT):
        if "project-docs-en" in os.path.relpath(dp, ROOT).split(os.sep):
            continue
        for f in fn:
            found.append(os.path.relpath(os.path.join(dp, f), ROOT))
    out(f"file_count={len(found)}")
    for f in sorted(found):
        out("  " + f)
    out(f"unlisted_vs_source_list={[f for f in found if f not in SOURCE_FILES]}")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    task1()
    task2()
    tree_check()
    with open(OUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines_out) + "\n")
    print("\n".join(lines_out))


if __name__ == "__main__":
    sys.exit(main())
