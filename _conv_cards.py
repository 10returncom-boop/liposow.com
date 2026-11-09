import urllib.request, os
from PIL import Image

out_dir = r"D:\_325_cloudflarepage_site\liposow.com\agrisky-pro\img"

jobs = [
    ("https://aka.doubaocdn.com/s/sczpUvu9V3", "card-tech.webp"),
    ("https://aka.doubaocdn.com/s/6T8BlU9xUA",  "card-agri.webp"),
    ("https://aka.doubaocdn.com/s/yBkLkyJszG",  "card-life.webp"),
    ("https://aka.doubaocdn.com/s/4OEH2Y2pzY",  "card-reg.webp"),
    ("https://aka.doubaocdn.com/s/HNLrJ89BeP",  "card-future.webp"),
    ("https://aka.doubaocdn.com/s/3lZ39GmrKV",  "card-resources.webp"),
]

for url, name in jobs:
    tmp = os.path.join(out_dir, "_tmp.jpg")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(tmp, "wb") as f:
        f.write(r.read())
    im = Image.open(tmp).convert("RGB")
    if im.width > 900:
        h = int(im.height * 900 / im.width)
        im = im.resize((900, h), Image.LANCZOS)
    out = os.path.join(out_dir, name)
    im.save(out, "WEBP", quality=80, method=6)
    print(name, im.size, os.path.getsize(out), "bytes")
    os.remove(tmp)
print("done")
