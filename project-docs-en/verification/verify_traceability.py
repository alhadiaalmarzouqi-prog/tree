"""Phase A Task 3 + line-count audit (read-only). Writes only to verification/."""
import os
import re

ROOT = r"C:\Users\test\Desktop\شجرة العائلة"
OUT = os.path.join(ROOT, "project-docs-en", "verification", "phase-a-traceability-output.txt")
SRC = [os.path.join(dp, f) for dp, _d, fn in os.walk(ROOT)
       if "project-docs-en" not in os.path.relpath(dp, ROOT).split(os.sep) for f in fn]

lines = []
def out(s=""):
    lines.append(s)

out("== LINE COUNT AUDIT (physical lines) ==")
for p in sorted(SRC):
    raw = open(p, "rb").read()
    nl = raw.count(b"\n")
    phys = nl if raw.endswith(b"\n") or not raw else nl + 1
    out(f"{os.path.relpath(p, ROOT)} bytes={len(raw)} physical_lines={phys}")

out("")
out("== OWNER / EVIDENCE TERM SEARCH (all source files) ==")
texts = {p: open(p, "rb").read().decode("utf-8-sig", errors="replace") for p in SRC}
terms = {
    "M1-E": r"M1-E", "M1-A": r"M1-A", "M1-B": r"M1-B",
    "D-01..D-10 identifier": r"\bD-(0[1-9]|10)\b",
    "PD identifier": r"\bPD-\d+", "NG identifier": r"\bNG-\d+", "KD identifier": r"\bKD-\d+",
    "owner message quote (رسالة المالك)": r"رسالة المالك",
    "owner approval statement (المالك وافق)": r"وافق المالك|وافقَ المالك|موافقة المالك",
    "owner approval date": r"تاريخ الموافقة|approved on|approval date",
    "DECISIONS.md file existence": r"DECISIONS\.md",
}
for name, pat in terms.items():
    hits = []
    for p, t in texts.items():
        for m in re.finditer(pat, t):
            ln = t.count("\n", 0, m.start()) + 1
            hits.append(f"{os.path.relpath(p, ROOT)}:{ln}")
    out(f"{name}: count={len(hits)} sample={hits[:6]}")

out("")
out("== DR / CG IDENTIFIER INVENTORY ==")
all_text = "\n".join(texts.values())
dr = sorted(set(re.findall(r"\bDR-\d{2}\b", all_text)))
cg = sorted(set(re.findall(r"\bCG-\d{2}\b", all_text)))
out(f"DR ids seen={len(dr)} range={dr[0] if dr else None}..{dr[-1] if dr else None}")
out(f"CG ids seen={len(cg)} range={cg[0] if cg else None}..{cg[-1] if cg else None}")

out("")
out("== D-01..D-10 CONTEXT (search for any mention of 'contradiction' register) ==")
out("contradiction-word hits are listed by file in phase-a-traceability-output.txt only as counts:")
for p, t in texts.items():
    c = len(re.findall(r"(تناقض|تعارض|contradiction)", t))
    if c:
        out(f"  {os.path.relpath(p, ROOT)} contradiction-related terms={c}")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines))
