import os
import hashlib

ROOT = r"C:\Users\test\Desktop\شجرة العائلة"
BASE = os.path.join(ROOT, "project-docs-en")
OUT = os.path.join(BASE, "verification", "deliverables-list.txt")

rows = []
for dp, _dn, fn in os.walk(BASE):
    for f in fn:
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ROOT)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest().upper()
        rows.append((rel, os.path.getsize(p), h))

rows.sort()
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(f"count={len(rows)}\n")
    for rel, size, h in rows:
        fh.write(f"{rel} | {size} | {h}\n")
print("count=", len(rows))