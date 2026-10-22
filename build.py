#!/usr/bin/env python3
"""Builds the Boston Travel Agency static site into ./docs
Content lives in content_a.py / content_b.py, photos in images.py."""
import os, html, sys, hashlib
from images import IMG
from content_a import FREEDOM, WATER, FOOD
from content_b import DAYTRIPS, FAMILY, SPORTS
from brand import mark_svg, lockup_svg, favicon_uri
from itins import ITIN_INTRO, PLANS, DAYS, SEASONAL

OUT = sys.argv[1] if len(sys.argv) > 1 else "docs"
TRACK = "pid=P00062445&uid=U00628023&mcid=58086&currency=USD"
# Contact form: free Web3Forms access key (sends submissions to email without showing the address). Empty = form hidden.
FORM_KEY = os.environ.get("WEB3FORMS_KEY", "")
DOMAIN = "bostontravelagency.com"
WIDGET = '<div data-vi-partner-id="U00628023" data-vi-widget-ref="W-c39469a9-bbcb-4bd7-8e22-d23ab3cde61a"></div><script async src="https://www.viator.com/orion/partner/widget.js"></script>'
CATS = [FREEDOM, WATER, FOOD, DAYTRIPS, FAMILY, SPORTS]

CSSV = hashlib.md5(open("styles.css","rb").read()).hexdigest()[:8]
def vlink(path): return f"https://www.viator.com{path}?{TRACK}"
BOSTON_ALL = vlink("/Boston/d678-ttd")
def e(s): return html.escape(s, quote=True)
USED = []
def use(k):
    if k not in USED: USED.append(k)
    return IMG[k]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'

def head(title, desc, path, og_img=None):
    og = f'<meta property="og:image" content="{e(IMG[og_img][0])}">' if og_img else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="https://{DOMAIN}/{path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">{og}
<link rel="icon" href="{favicon_uri()}">
{FONTS}
<link rel="stylesheet" href="/styles.css?v={CSSV}">
</head>
<body>
"""

def nav(active=""):
    links = "".join(f'<a href="/{c["slug"]}/"{" aria-current=page" if c["slug"]==active else ""}>{e(c["nav"])}</a>' for c in CATS)
    return f"""<header class="top"><div class="wrap bar">
<a class="brand" href="/">{mark_svg(42)}<span class="wm"><span class="wm-name">Boston Travel Agency</span><span class="wm-tag">Est. 1965 &middot; North End</span></span></a>
<nav class="links">{links}<a href="/sample-itineraries/" class="cta-sm">Sample Itineraries</a></nav>
</div></header>
"""

def foot():
    return f"""<footer class="foot">
<div class="wrap foot-grid">
<div><div class="brand light">{mark_svg(42, bg="#b2452f", wave="#f6f1e8")}<span class="wm"><span class="wm-name">Boston Travel Agency</span><span class="wm-tag">Est. 1965 &middot; North End</span></span></div>
<p>Family-run since 1965, founded in the heart of Boston's North End. We help visitors and locals find the best of the city, and we plan custom trips anywhere in the world.</p></div>
<div><h4>Explore</h4>{''.join(f'<a href="/{c["slug"]}/">{e(c["title"])}</a>' for c in CATS)}</div>
<div><h4>More</h4><a href="/sample-itineraries/">Sample itineraries</a><a href="/about/">About us</a><a href="/contact/">Contact us</a><a href="/photo-credits/">Photo credits</a></div>
</div>
<div class="wrap fine">
<p>Tour bookings are made and fulfilled by Viator, a Tripadvisor company. Boston Travel Agency may earn a commission when you book through links on this site, at no extra cost to you. Prices, ratings and availability shown are approximate and can change; see Viator for current details. Photos from Wikimedia Commons; see <a href="/photo-credits/">photo credits</a>.</p>
<p>&copy; 2026 Boston Travel Agency. All rights reserved.</p>
</div>
</footer>
</body>
</html>
"""

def credit(k):
    url, src, author, lic, licurl, cap = use(k)
    lic_html = f'<a href="{licurl}" rel="license noopener" target="_blank">{e(lic)}</a>' if licurl else e(lic)
    return f'Photo: <a href="{src}" target="_blank" rel="noopener">{e(author)}</a>, {lic_html}'

def figure(k):
    url, src, author, lic, licurl, cap = use(k)
    return f'<figure class="photo"><img src="{url}" alt="{e(cap)}" loading="lazy"><figcaption>{e(cap)}. <span class="cr">{credit(k)}</span></figcaption></figure>'

def hero(k, eyebrow, h1, lede_html, ctas="", small=False):
    url = use(k)[0]
    return f"""<section class="hero photo-hero{' small' if small else ''}" style="background-image:linear-gradient(180deg,rgba(12,24,48,.30),rgba(12,24,48,.72)),url('{url}')">
<div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><div class="lede">{lede_html}</div>{ctas}</div>
<p class="hero-credit">{credit(k)}</p>
</section>"""

def stars(r): return f'<span class="rating" aria-label="Rated {r} out of 5">&#9733; {r:.1f}</span>'

def card(t):
    title, path, blurb, dur, price, rating, reviews = t
    rv = f'<span class="muted">({reviews} reviews)</span>' if reviews != "New" else '<span class="muted">(new)</span>'
    return f"""<article class="tour"><h3>{e(title)}</h3><p>{e(blurb)}</p>
<ul class="meta"><li>{stars(rating)} {rv}</li><li>{e(dur)}</li><li>From about ${price}</li></ul>
<a class="btn" href="{vlink(path)}" target="_blank" rel="sponsored noopener">Check dates &amp; book</a></article>"""

def write(path, content):
    if path.endswith(".html"):
        prefix = "../" * path.count("/")
        content = content.replace('href="/"', 'href="%s"' % (prefix or "./")).replace('href="/', 'href="%s' % prefix)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    with open(full, "w") as f: f.write(content)

# ---------- category pages ----------
for c in CATS:
    secs = ""
    for i, s in enumerate(c["sections"]):
        body = "".join(f"<p>{p}</p>" for p in s["paras"])
        img = figure(s["img"]) if s.get("img") else ""
        secs += f'<section class="story{" flip" if i % 2 else ""}"><div class="story-text"><h2>{e(s["h"])}</h2>{body}</div>{img}</section>'
    f = c["feature"]
    feat = "".join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in f["items"])
    tips = "".join(f"<li>{e(t)}</li>" for t in c["tips"])
    intro = "".join(f"<p>{p}</p>" for p in c["intro"])
    page = head(f"{c['title']} | Boston Travel Agency", c["intro"][0][:155], c["slug"] + "/", c["hero"]) + nav(c["slug"]) + \
        hero(c["hero"], e(c["kicker"]), e(c["title"]), intro, '<div class="hero-ctas"><a class="btn big" href="#tours">See our top tours</a></div>', small=True) + f"""
<div class="wrap">{secs}</div>
<section class="band"><div class="wrap"><h2 class="sec">{e(f['h'])}</h2><ul class="feature">{feat}</ul></div></section>
<section class="wrap" id="tours"><h2 class="sec">Our top tours</h2>
<div class="grid">{''.join(card(t) for t in c['tours'])}</div>
<aside class="tips"><h3>Local tips</h3><ul>{tips}</ul></aside>
<a class="itin-callout" href="/sample-itineraries/"><strong>Planning your days?</strong> See how these tours fit into our 2, 3 and 5-day Boston itineraries &rarr;</a>
<p class="center"><a class="btn ghost" href="{BOSTON_ALL}" target="_blank" rel="sponsored noopener">Browse every Boston experience on Viator</a></p>
</section>
""" + foot()
    write(f"{c['slug']}/index.html", page)

# ---------- itineraries ----------
def plan_card(p):
    key, label, name, desc = p
    return f'<a class="plan-card" href="/sample-itineraries/#plan-{key}"><span class="pc-days">{label}</span><span class="pc-name">{e(name)}</span><span class="pc-desc">{e(desc)}</span><span class="go">See the plan &rarr;</span></a>'

def tour_chip(t):
    title, path = t
    return f'<a class="tour-chip" href="{vlink(path)}" target="_blank" rel="sponsored noopener"><span class="tc-label">Book this tour</span><span class="tc-title">{e(title)}</span><span class="tc-go">Check dates &amp; prices &rarr;</span></a>'

def day_block(d):
    slots = ""
    for label, text, tours, eats in d["slots"]:
        eat = ""
        if eats:
            eat = '<ul class="eats">' + "".join(f'<li><strong>{e(n)}</strong> <span class="where">{e(w)}</span><br><span class="muted">{e(why)}</span></li>' for n, w, why in eats) + '</ul>'
        chips = "".join(tour_chip(t) for t in tours)
        slots += f'<div class="slot"><div class="slot-label">{e(label)}</div><div class="slot-body"><p>{e(text)}</p>{chips}{eat}</div></div>'
    return f"""<article class="day" data-plans="{d['plans']}" id="day-{d['n']}">
<div class="day-head" style="background-image:linear-gradient(180deg,rgba(10,20,40,.15),rgba(10,20,40,.8)),url('{use(d['img'])[0]}')"><span class="day-n">Day {d['n']}</span><h2>{e(d['title'])}</h2><p>{e(d['summary'])}</p></div>
<div class="day-body">{slots}<p class="day-credit">{credit(d['img'])}</p></div></article>"""

tabs = "".join(f'<a class="tab" href="#plan-{k}" data-plan="{k}"><strong>{lbl}</strong><span>{e(n)}</span></a>' for k, lbl, n, _ in PLANS)
anchors = "".join(f'<span id="plan-{k}" class="anchor"></span>' for k, *_ in PLANS)
seas = "".join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span>' + (f' <a href="{vlink(t[1])}" target="_blank" rel="sponsored noopener">{e(t[0])} &rarr;</a>' if t else '') + '</li>' for a, b, t in SEASONAL)
itin_js = """<script>
(function(){var tabs=document.querySelectorAll('.tab');function show(k){document.querySelectorAll('.day').forEach(function(d){d.hidden=d.dataset.plans.split(' ').indexOf(k)<0});tabs.forEach(function(t){t.classList.toggle('on',t.dataset.plan===k)});var c=document.getElementById('plan-count');if(c)c.textContent=k;}
function fromHash(){var m=location.hash.match(/plan-(\\d)/);show(m?m[1]:'2');}
tabs.forEach(function(t){t.addEventListener('click',function(ev){ev.preventDefault();history.replaceState(null,'','#plan-'+t.dataset.plan);show(t.dataset.plan);document.getElementById('days').scrollIntoView({behavior:'smooth'});});});
window.addEventListener('hashchange',fromHash);fromHash();})();
</script>"""
itin = head("Sample Boston Itineraries: 2, 3 and 5 Days | Boston Travel Agency", "Day-by-day sample itineraries for 2, 3 and 5 days in Boston, with the best tours and where to eat, from a North End travel agency est. 1965.", "sample-itineraries/", "statehouse") + nav("") + \
    hero("statehouse", "Plan your visit", "Sample Boston itineraries", "".join(f"<p>{p}</p>" for p in ITIN_INTRO), small=True) + f"""
{anchors}
<section class="wrap"><nav class="tabs" aria-label="Choose an itinerary">{tabs}</nav></section>
<section class="wrap days" id="days"><p class="muted center">Showing the <span id="plan-count">2</span>-day plan. Days build on each other, so a longer trip simply adds days.</p>
{''.join(day_block(d) for d in DAYS)}</section>
<section class="band"><div class="wrap"><h2 class="sec">Make it your own</h2><ul class="feature">{seas}</ul>
<p class="muted small-note">Restaurants are examples we like; hours and menus change, so check before you go. Tour bookings are handled by Viator.</p></div></section>
""" + itin_js + foot()
write("sample-itineraries/index.html", itin)

# ---------- home ----------
def tile(c):
    url = IMG[c["tile"]][0]; use(c["tile"])
    return f"""<a class="tile" href="/{c['slug']}/" style="background-image:linear-gradient(180deg,rgba(10,20,40,.05) 30%,rgba(10,20,40,.85)),url('{url}')"><span class="k">{e(c['kicker'])}</span><span class="h">{e(c['title'])}</span><span class="go">Explore &rarr;</span></a>"""
picks = [FREEDOM["tours"][0], WATER["tours"][0], FOOD["tours"][0], SPORTS["tours"][0], DAYTRIPS["tours"][0], FAMILY["tours"][1]]
home = head("Boston Travel Agency | The Best Tours & Things to Do in Boston",
            "Hand-picked Boston tours from a family-run North End travel agency, est. 1965: the Freedom Trail, whale watching, food tours, Fenway Park, day trips and more.", "", "hero") + nav() + \
    hero("hero", "Family-run since 1965 &middot; Boston's North End", "The best of Boston,<br>picked by people who live here.",
         "<p>We've sorted through hundreds of Boston tours so you don't have to. Every experience here is highly rated, easy to book, and something we'd send our own family on.</p>",
         '<div class="hero-ctas"><a class="btn big" href="#explore">Explore Boston</a><a class="btn ghost light big" href="/sample-itineraries/">See sample itineraries</a></div>') + f"""
<section class="wrap intro-block">
<h2 class="sec">Curated, memorable Boston experiences</h2>
<p>Boston Travel was founded in 1965 in the heart of Boston's North End. What began as a neighborhood agency helping local families discover the world has grown into a deeply rooted, family-run company focused on crafting highly personalized travel experiences. With decades of experience and generations of local insight, our passion for travel is matched only by our love of this incredible city.</p>
<p>While we now specialize in customized private tours and bespoke travel planning, this website features a curated collection of some of the very best tours available in Boston today. Whether you're visiting for the first time or rediscovering its cobblestone streets, we invite you to explore Boston through the lens of those who know and love it best.</p>
</section>
<section class="itin-feature"><div class="wrap">
<p class="eyebrow dark">Plan your visit</p><h2 class="sec">Sample itineraries for 2, 3 and 5 days</h2>
<p class="muted big">Day-by-day plans with the best tours, where to eat and how to pace it, built by locals.</p>
<div class="plan-cards">{''.join(plan_card(p) for p in PLANS)}</div>
</div></section>
<section class="wrap" id="explore"><h2 class="sec">Find your Boston</h2><div class="tiles">{''.join(tile(c) for c in CATS)}</div></section>
<section class="band"><div class="wrap">
<h2 class="sec">Our top picks right now</h2>
<div class="grid">{''.join(card(t) for t in picks)}</div>
</div></section>
<section class="wrap widget-wrap"><h2 class="sec">More Boston favorites</h2><p class="muted">Live from Viator, with current prices and availability.</p>{WIDGET}
<p class="center"><a class="btn ghost" href="{BOSTON_ALL}" target="_blank" rel="sponsored noopener">See all 400+ Boston experiences</a></p></section>
<section class="wrap why">
<div><h3>Hand-picked, not paid placement</h3><p>We only list tours with strong, consistent reviews. If it isn't something we'd recommend to a friend, it isn't here.</p></div>
<div><h3>Book safely with Viator</h3><p>Every tour is booked through Viator, with secure checkout, 24/7 support and free cancellation on most experiences.</p></div>
<div><h3>Local since 1965</h3><p>We're a family-run, IATA-accredited agency from the North End. These are the tours and places we recommend to our own family and friends.</p></div>
</section>
""" + foot()
write("index.html", home)

# ---------- contact ----------
if FORM_KEY:
    form = f"""<form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{FORM_KEY}"><input type="hidden" name="subject" value="New message from bostontravelagency.com">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
<label>Name<input name="name" required></label><label>Email<input type="email" name="email" required></label>
<label>Travel dates (optional)<input name="dates"></label><label>Message<textarea name="message" rows="6" required></textarea></label>
<button class="btn big" type="submit">Send message</button></form>"""
else:
    form = '<p class="muted">Our contact form is coming soon.</p>'
contact = head("Contact Us | Boston Travel Agency", "Get in touch with Boston Travel Agency.", "contact/") + nav() + f"""
<section class="wrap narrow prose"><h1 class="sec">Contact us</h1>
<p>Have a question about a tour or planning a group trip? Send us a note. For bookings, changes and cancellations on any tour, contact Viator directly through your confirmation email; their support team is available 24/7.</p>
{form}</section>
""" + foot()
write("contact/index.html", contact)

# ---------- about ----------
about = head("About Us | Boston Travel Agency", "Boston Travel was founded in 1965 in the heart of Boston's North End and is still family-run today.", "about/", "hanover") + nav() + \
    hero("hanover", "About us", "Family-run since 1965.", "<p>Founded in the heart of Boston's North End.</p>", small=True) + f"""
<section class="wrap narrow prose">
<p>Boston Travel was founded in 1965 in the heart of Boston's North End. What began as a neighborhood agency helping local families discover the world has grown into a deeply rooted, family-run company focused on crafting highly personalized travel experiences.</p>
<p>With decades of experience and generations of local insight, our passion for travel is matched only by our love of this incredible city. Boston's rich history, cultural legacy and neighborhood charm make it a destination every traveler should experience at least once.</p>
<p>Today we specialize in customized private tours and bespoke travel planning. This website is our curated collection of some of the very best tours available in Boston, all booked securely through Viator. Planning your visit? Start with our <a href="/sample-itineraries/">sample itineraries</a>.</p>
</section>
""" + foot()
write("about/index.html", about)

# ---------- photo credits ----------
rows = "".join(f'<li><img src="{IMG[k][0]}" alt="" loading="lazy"><div><strong>{e(IMG[k][5])}</strong><br>{credit(k)}, via Wikimedia Commons</div></li>' for k in USED)
credits = head("Photo Credits | Boston Travel Agency", "Photo credits and licenses.", "photo-credits/") + nav() + f"""
<section class="wrap narrow prose"><h1 class="sec">Photo credits</h1>
<p>Photos on this site come from Wikimedia Commons and are used under the licenses shown. Thank you to the photographers who share their work. Photos are displayed unaltered except for cropping to fit the page.</p>
<ul class="credits">{rows}</ul></section>
""" + foot()
write("photo-credits/index.html", credits)

# ---------- 404 / misc ----------
write("404.html", head("Page not found | Boston Travel Agency", "Page not found", "404.html") + nav() + """
<section class="hero small"><div class="wrap"><h1>That page wandered off the Freedom Trail.</h1><p class="lede"><a class="btn" href="/">Back to the home page</a></p></div></section>
""" + foot())
if os.environ.get("CUSTOM_DOMAIN") == "1":
    write("CNAME", DOMAIN + "\n")
write(".nojekyll", "")
write("logo.svg", lockup_svg())
write("logo-dark.svg", lockup_svg(dark=True))
write("logo-mark.svg", mark_svg(512, title=False))
urls = [""] + ["sample-itineraries/"] + [c["slug"] + "/" for c in CATS] + ["about/", "contact/", "photo-credits/"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>https://{DOMAIN}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
with open("styles.css") as f: write("styles.css", f.read())
print("built", OUT, "pages:", len(CATS) + 5, "photos:", len(USED))
