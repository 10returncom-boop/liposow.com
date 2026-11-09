import urllib.request, os
from PIL import Image

url = "https://aka.doubaocdn.com/s/K1qJU9BCbZ"
out_dir = r"D:\_325_cloudflarepage_site\liposow.com\agrisky-pro\img"
tmp = os.path.join(out_dir, "_hero_tmp.jpg")
out = os.path.join(out_dir, "hero-terrace.webp")

req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=60) as r, open(tmp, "wb") as f:
    f.write(r.read())

im = Image.open(tmp).convert("RGB")
# 縮到合理寬度（2848 -> 1920）以控制體積
if im.width > 1920:
    h = int(im.height * 1920 / im.width)
    im = im.resize((1920, h), Image.LANCZOS)
im.save(out, "WEBP", quality=80, method=6)
os.remove(tmp)
print("saved", out, im.size, os.path.getsize(out), "bytes")
