"""Build responsive images from the band's full-size originals.

Originals live in _build/originals/ (downloaded from lukecombsuk.com/wp-content/uploads,
the band's own site). Outputs go to img/ as WebP at several widths plus one JPEG fallback.
Run:  python3 _build/images.py
"""
from pathlib import Path
from PIL import Image, ImageOps
import json

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_build" / "originals"
OUT = ROOT / "img"
OUT.mkdir(exist_ok=True)

LANDSCAPE = [480, 960, 1920]
PORTRAIT = [360, 720, 1080]
SQUARE = [540, 1080]
manifest = {}

for f in sorted(SRC.glob("*.jpg")):
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    w, h = im.size
    name = f.stem
    widths = SQUARE if abs(w - h) < 10 else (PORTRAIT if h > w else LANDSCAPE)
    widths = [x for x in widths if x <= w] or [w]
    made = []
    for tw in widths:
        th = round(h * tw / w)
        r = im if tw == w else im.resize((tw, th), Image.LANCZOS)
        r.save(OUT / f"{name}-{tw}.webp", "WEBP", quality=78, method=6)
        made.append(tw)
    fb = widths[1] if len(widths) > 1 else widths[0]
    fh = round(h * fb / w)
    (im if fb == w else im.resize((fb, fh), Image.LANCZOS)).save(
        OUT / f"{name}-{fb}.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    manifest[name] = {"w": w, "h": h, "widths": made, "fallback": fb}

# logo / favicon
logo = Image.open(SRC / "lcuk.png").convert("RGBA")
logo.save(OUT / "lcuk-logo.png", optimize=True)
lw, lh = logo.size
logo.save(OUT / "lcuk-logo.webp", "WEBP", quality=90, method=6)
for s in (32, 180, 192):
    c = Image.new("RGBA", (s, s), (12, 10, 8, 255))
    t = logo.copy(); t.thumbnail((int(s * .9), int(s * .9)), Image.LANCZOS)
    c.alpha_composite(t, ((s - t.width) // 2, (s - t.height) // 2))
    c.save(OUT / f"icon-{s}.png", optimize=True)
manifest["lcuk-logo"] = {"w": lw, "h": lh}
(ROOT / "_build" / "images.json").write_text(json.dumps(manifest, indent=1))
print(json.dumps(manifest)[:400])
