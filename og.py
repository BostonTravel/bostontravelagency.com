# Branded 1200x630 link-preview cards (Open Graph), drawn with Pillow so they need no outside images.
import os, textwrap
from PIL import Image, ImageDraw, ImageFont
NAVY, BRICK, CREAM, PINK = (20, 40, 75), (178, 69, 47), (246, 241, 232), (245, 195, 179)
F = "/usr/share/fonts/truetype/dejavu/"
def _f(name, size): return ImageFont.truetype(F + name, size)

_LOGO = None
def _logo(h):
    # the agency's original globe logo, tinted cream for the navy card
    global _LOGO
    if _LOGO is None:
        src = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand", "logo-vintage-black.png")).convert("L")
        alpha = src.point(lambda v: 255 - v)
        alpha = alpha.crop(alpha.getbbox())
        _LOGO = Image.new("RGBA", alpha.size, CREAM + (255,)); _LOGO.putalpha(alpha)
    w = round(_LOGO.width * h / _LOGO.height)
    return _LOGO.resize((w, h), Image.LANCZOS)

def card(out_dir, slug, title, kicker="Boston Travel Agency"):
    img = Image.new("RGB", (1200, 630), NAVY); d = ImageDraw.Draw(img)
    d.rectangle([0, 600, 1200, 630], fill=BRICK)
    lg = _logo(120); img.paste(lg, (64, 50), lg)
    tx = 64 + lg.width + 28
    d.text((tx, 78), "Boston Travel Agency", font=_f("DejaVuSerif-Bold.ttf", 34), fill=CREAM)
    d.text((tx + 2, 124), "EST. 1965 · BESPOKE PRIVATE TRAVEL", font=_f("DejaVuSans-Bold.ttf", 17), fill=PINK)
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
