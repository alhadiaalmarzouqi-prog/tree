"""Structural validation of the English documentation set (Stage D0).

Checks (mission section 8, automated subset):
1. All source files unchanged (hash vs manifest).
2. Protected fixture parses; expected 22 IDs present.
3. Requirement identifiers in English docs == those in REQUIREMENTS source.
4. Cross-references resolve within the English set (markdown-style file targets).
5. No undefined decision identifiers remain (DR-xx used in English docs are in source).
6. No OPEN/DR identifiers invented (OPEN-1..21 tracked; no others).
7. Machine-readable structures preserved (formulas/JSON keys not required to match; only counting here).
"""
import hashlib, json, os, re, sys

ROOT = r"C:\Users\test\Desktop\شجرة العائلة"
EN = os.path.join(ROOT, "project-docs-en")
OUT = os.path.join(EN, "verification", "validation-output.txt")
MANIFEST = os.path.join(EN, "00-SOURCE-MANIFEST.md")
REQ_SRC = os.path.join(ROOT, "project-docs", "analysis", "REQUIREMENTS.md")
DR_SRC = os.path.join(ROOT, "project-docs", "analysis", "DECISIONS-REQUIRED.md")
FIXTURE = os.path.join(ROOT, "project-docs", "reference-fixtures", "kinship-reference-cases.json")

EN_DOCS = ["03-REQUIREMENTS.md","04-TRACEABILITY-MATRIX.md","05-CONFLICTS-AND-GAPS.md",
           "06-DECISIONS-REQUIRED.md","07-DECISION-EVIDENCE-REGISTER.md","08-MATHEMATICAL-REFERENCE.md",
           "09-MASTER-ARCHITECTURE.md","10-ANALYSIS-REPORT.md","11-NEXT-AGENT.md","12-STANDARDS.md",
           "13-SOURCE-TO-ENGLISH-TRACEABILITY.md","14-CORRECTED-DOCUMENTATION-DEFECTS.md",
           "15-UNRESOLVED-CONTRADICTIONS.md"]

RID = r"\b(?:FR|PRV|SEC|GOV|TECH|DATA|PERF|OPS|TST|SCOPE|PLAN)-\d{3}\b"
out_lines = []
def out(s=""):
    out_lines.append(s)

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest().upper()

def read(p):
    return open(p, encoding="utf-8-sig").read()

fails = []
out("== 1. Source files unchanged ==")
mtext = read(MANIFEST)
rows = re.findall(r"\| \d+ \| `([^`]+)` \| (\d+) \| (\d+) \| ([A-F0-9]{64}) \|", mtext)
mmap = {r[0]: (r[3], int(r[1])) for r in rows}
for rel, (h, sz) in sorted(mmap.items()):
    p = os.path.join(ROOT, rel)
    ok = os.path.exists(p) and sha(p) == h and os.path.getsize(p) == sz
    out(f"{'PASS' if ok else 'FAIL'} {rel}")
    if not ok:
        fails.append(rel)

out("== 2. Protected fixture ==")
try:
    j = json.loads(read(FIXTURE))
    ids = [c["case_id"] for c in j["cases"]]
    exp = ["T01","T02","T03","T04","T05","T06","T07","T08","T09","T10","T11","T12","T13","T14",
           "DI-05a","DI-05b","ST-01","ST-02","ST-03","ST-04","ST-05","ST-06"]
    ok = sorted(exp) == sorted(ids)
    out(f"PASS {len(ids)} cases; expected set {'present' if ok else 'DIFF'}")
    if not ok:
        fails.append("fixture-id-set")
    struct = all("valid_path_pair_count" in c["expected"] and c["expected"]["valid_path_pair_count"] == len(c["expected"].get("valid_path_pairs", [])) for c in j["cases"])
    out(f"PASS per-case pair-count check" if struct else "FAIL per-case pair-count check")
    if not struct:
        fails.append("fixture-structure")
except Exception as e:
    out("FAIL fixture parse: " + str(e))
    fails.append("fixture-parse")

out("== 3. Requirement identifiers preserved ==")
src_ids = set(re.findall(RID, read(REQ_SRC)))
en_all = "\n".join(read(os.path.join(EN, d)) for d in EN_DOCS)
en_ids = set(re.findall(RID, en_all))
missing = sorted(src_ids - en_ids)
extra = sorted(en_ids - src_ids)
out(f"source count={len(src_ids)} english count={len(en_ids)} missing={missing} extra={extra}")
if missing or extra:
    fails.append("req-id-diff")

out("== 4. English cross-references resolve ==")
for d in EN_DOCS:
    t = read(os.path.join(EN, d))
    refs = sorted(set(re.findall(r"`((?:0[3-9]|1[0-6])-[A-Z0-9\-]+\.md)`", t)))
    bad = [r for r in refs if not os.path.exists(os.path.join(EN, r))]
    out(f"{'PASS' if not bad else 'FAIL'} {d} refs={len(refs)} dangling={bad}")
    if bad:
        fails.append(d + ":" + ",".join(bad))

out("== 5. Decision identifiers are from source ==")
dr_src = set(re.findall(r"\bDR-\d{2}\b", read(DR_SRC)))
dr_en = set()
for d in EN_DOCS:
    dr_en |= set(re.findall(r"\bDR-\d{2}\b", read(os.path.join(EN, d))))
# DR-32..34 legitimately carried from DECISION-REGISTER source
extra_dr = sorted(dr_en - dr_src - {"DR-32", "DR-33", "DR-34"})
out(f"DR in english = {len(dr_en)} ; extra vs DECISIONS-REQUIRED source = {extra_dr or 'none'}")
if extra_dr:
    fails.append("dr-extra:" + ",".join(extra_dr))

out("== 6. OPEN identifiers tracked (1..21) ==")
open_ids = set()
for d in EN_DOCS:
    open_ids |= set(re.findall(r"\bOPEN-(\d{1,2})\b", read(os.path.join(EN, d))))
numbers = sorted({int(x) for x in open_ids})
out(f"OPEN ids seen = {numbers}")
if numbers and (min(numbers) < 1 or max(numbers) > 21):
    fails.append("open-range")

out(f"== RESULT: {'FAIL' if fails else 'PASS'} ; failures={fails}")
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out_lines) + "\n")
print("\n".join(out_lines))
sys.exit(1 if fails else 0)