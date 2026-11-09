# -*- coding: utf-8 -*-
import re, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = glob.glob("*.html")
exist = set(files)
broken = []
pat = re.compile(r'href="([^"#]+\.html)(?:#[^"]*)?"')
for f in files:
    txt = open(f, encoding="utf-8").read()
    for m in pat.finditer(txt):
        t = m.group(1)
        if t.startswith("http"):
            continue  # canonical / 外站連結，非站內相對連結
        if t not in exist and (f, t) not in broken:
            broken.append((f, t))
print("pages:", len(files))
print("broken:", broken if broken else "none")
