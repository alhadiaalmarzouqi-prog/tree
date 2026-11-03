import os
ROOT = r"C:\Users\test\Desktop\شجرة العائلة"
EN = os.path.join(ROOT, "project-docs-en")
OUT = os.path.join(EN, "verification", "final-scan.txt")
L = []
L.append("project-docs-en top-level:")
for f in sorted(os.listdir(EN)):
    full = os.path.join(EN, f)
    if os.path.isfile(full):
        L.append(f"  {f} | {os.path.getsize(full)}")
L.append("project-docs-en/verification:")
vf = os.path.join(EN, "verification")
for f in sorted(os.listdir(vf)):
    full = os.path.join(vf, f)
    if os.path.isfile(full):
        L.append(f"  {f} | {os.path.getsize(full)}")
a = open(os.path.join(EN, "00-SOURCE-MANIFEST.v1-original.md"), "rb").read()
b = open(os.path.join(EN, "00-SOURCE-MANIFEST.md"), "rb").read()
L.append(f"v1 preserved identical (bytes): {a == b}")
cnt = sum(1 for d, _, fn in os.walk(EN) for _ in fn)
L.append(f"total files in project-docs-en: {cnt}")
open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("\n".join(L))