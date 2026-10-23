# Branded 1200x630 link-preview cards (Open Graph), drawn with Pillow so they need no outside images.
import os, textwrap
from PIL import Image, ImageDraw, ImageFont
NAVY, BRICK, CREAM, PINK = (20, 40, 75), (178, 69, 47), (246, 241, 232), (245, 195, 179)
F = "/usr/share/fonts/truetype/dejavu/"
def _f(name, size): return ImageFont.truetype(F + name, size)

def _mark(d, x, y, s):
    k = s / 112
    P = lambda a, b: (x + a * k, y + b * k)
    d.rounded_rectangle([P(0, 0), P(112, 112)], radius=24 * k, fill=BRICK)
    d.polygon([P(56, 6), P(60.5, 30), P(51.5, 30)], fill=CREAM)
    d.rectangle([P(50, 30), P(62, 39)], fill=CREAM); d.rectangle([P(47.5, 39), P(64.5, 49)], fill=CREAM)
    f = _f("DejaVuSerif-Bold.ttf", int(30 * k)); d.text(P(56, 70), "BTA", font=f, fill=CREAM, anchor="mm")
    pts = [P(22 + i, 95 + 3.5 * __import__("math").sin(i / 17 * 6.283)) for i in range(0, 69)]
    d.line(pts, fill=CREAM, width=max(2, int(4 * k)))

def card(out_dir, slug, title, kicker="Boston Travel Agency"):
    img = Image.new("RGB", (1200, 630), NAVY); d = ImageDraw.Draw(img)
    d.rectangle([0, 600, 1200, 630], fill=BRICK)
    _mark(d, 70, 64, 104)
    d.text((196, 86), "Boston Travel Agency", font=_f("DejaVuSerif-Bold.ttf", 34), fill=CREAM)
    d.text((198, 132), "EST. 1965 · BESPOKE PRIVATE TRAVEL", font=_f("DejaVuSans-Bold.ttf", 17), fill=PINK)
    size = 76 if len(title) < 26 else 64 if len(title) < 44 else 54
    lines = textwrap.wrap(title, width=int(1500 / size))[:3]
    y = 250
    for ln in lines:
        d.text((70, y), ln, font=_f("DejaVuSerif-Bold.ttf", size), fill=(255, 255, 255)); y += int(size * 1.18)
    d.text((70, y + 18), kicker, font=_f("DejaVuSans.ttf", 30), fill=PINK)
    d.text((1130, 548), "bostontravelagency.com", font=_f("DejaVuSans-Bold.ttf", 24), fill=CREAM, anchor="rs")
    os.makedirs(os.path.join(out_dir, "og"), exist_ok=True)
    img.save(os.path.join(out_dir, "og", slug + ".png"), optimize=True)
    return f"og/{slug}.png"
