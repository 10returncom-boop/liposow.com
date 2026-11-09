# -*- coding: utf-8 -*-
"""把 _content/part_*.py 的內容合併進 build.py 的「外部內容插入點」。"""
import io, os, glob, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(ROOT, "build.py")
MARKER = "# ==== 外部內容插入點（子代理產出的 part_*.py 內容將整合於此） ====\n"

txt = io.open(BUILD, encoding="utf-8").read()
if MARKER not in txt:
    print("ERROR: marker not found in build.py")
    sys.exit(1)

parts = ""
files = sorted(glob.glob(os.path.join(ROOT, "_content", "part_*.py")))
if not files:
    print("ERROR: no part_*.py files found")
    sys.exit(1)

for f in files:
    s = io.open(f, encoding="utf-8").read()
    # 去掉檔頭 coding 宣告，避免重複
    if s.startswith("# -*- coding: utf-8 -*-"):
        s = s.split("\n", 1)[1]
    parts += "\n" + s.strip() + "\n"

new = txt.replace(MARKER, MARKER + parts, 1)
io.open(BUILD, "w", encoding="utf-8", newline="").write(new)
print("merged %d file(s) into build.py" % len(files))
