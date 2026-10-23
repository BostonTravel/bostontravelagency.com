# Boston Travel Agency logo (original design): BTA monogram, Old North steeple, harbor wave
def mark_svg(size=40, bg="#14284b", fg="#f6f1e8", wave="#c8553d", title=True):
    t = '<title>Boston Travel Agency</title>' if title else ''
    return (f'<svg class="logo-mark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 112 112" width="{size}" height="{size}" role="img" aria-label="Boston Travel Agency">{t}'
        f'<rect width="112" height="112" rx="24" fill="{bg}"/>'
        f'<path d="M56 6 L60.5 30 L51.5 30 Z" fill="{fg}"/><rect x="50" y="30" width="12" height="9" fill="{fg}"/>'
        f'<rect x="47.5" y="39" width="17" height="10" fill="{fg}"/><rect x="54.5" y="41.5" width="3" height="6" rx="1.5" fill="{bg}"/>'
        f'<text x="56" y="83" text-anchor="middle" font-family="Fraunces, Georgia, \'Times New Roman\', serif" font-weight="700" font-size="34" letter-spacing="1" fill="{fg}">BTA</text>'
        f'<path d="M22 95 q8.5 -7 17 0 t17 0 t17 0 t17 0" fill="none" stroke="{wave}" stroke-width="4" stroke-linecap="round"/></svg>')

def lockup_svg(dark=False):
    bg, name, tag, wave = ("#b2452f", "#ffffff", "#f5c3b3", "#f6f1e8") if dark else ("#14284b", "#14284b", "#b2452f", "#c8553d")
    inner = mark_svg(112, bg=bg, wave=wave, title=False).replace('<svg class="logo-mark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 112 112" width="112" height="112" role="img" aria-label="Boston Travel Agency">', '<g transform="translate(4,4)">').replace('</svg>', '</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 120" width="560" height="120">{inner}'
        f'<text x="138" y="62" font-family="Fraunces, Georgia, \'Times New Roman\', serif" font-weight="700" font-size="40" fill="{name}">Boston Travel Agency</text>'
        f'<text x="140" y="92" font-family="Inter, Arial, sans-serif" font-weight="600" font-size="15" letter-spacing="2.5" fill="{tag}">EST. 1965 · BESPOKE PRIVATE TRAVEL</text></svg>')

def favicon_uri():
    import urllib.parse
    return "data:image/svg+xml," + urllib.parse.quote(mark_svg(64, title=False))

# ---------- the agency's original globe logo (used site-wide) ----------
from brand_logo import VIEWBOX, PATH
def vintage_svg(color="#14284b"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VIEWBOX}" role="img" aria-label="Boston Travel Agency">'
            f'<title>Boston Travel Agency</title><path fill="{color}" fill-rule="evenodd" d="{PATH}"/></svg>')
