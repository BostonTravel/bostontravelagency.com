#!/usr/bin/env python3
"""Builds the Boston Travel Agency static site into ./docs
Content lives in content_a.py / content_b.py, photos in images.py."""
import os, html, sys, hashlib, re
from images import IMG
from content_a import FREEDOM, WATER, FOOD
from content_b import DAYTRIPS, FAMILY, SPORTS
from og import card as og_card
from brand import mark_svg, lockup_svg, favicon_uri, vintage_svg
from itins import ITIN_INTRO, PLANS, DAYS, SEASONAL
from stay import STAY_INTRO, TIERS, PICKER, HOODS, STAY_TIPS
from events import EVENTS_INTRO, upcoming, fmt_range
from selfies import SELFIE_INTRO, TOP, BONUS
from food_guide import EAT_INTRO, CLASSICS, TRENDING, TRENDING_AS_OF
import datetime as dt
# Events are listed from this date forward; BUILD_DATE=YYYY-MM-DD overrides for testing.
TODAY = dt.date.fromisoformat(os.environ["BUILD_DATE"]) if os.environ.get("BUILD_DATE") else dt.date.today()
UPCOMING = upcoming(TODAY)
# KAYAK hotel search link template, filled in once the KAYAK affiliate program approves us. Empty = no links shown.
KAYAK_LINK = os.environ.get('KAYAK_LINK', '')

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
# Inline tour link in body text: [[link text|/tours/...]] -> discreet Viator link
def tl(p): return re.sub(r"\[\[(.+?)\|(/tours/[^\]]+)\]\]", lambda m: f'<a class="tl" href="{vlink(m.group(2))}" target="_blank" rel="sponsored noopener">{m.group(1)}</a>', p)
USED = []
def use(k):
    if k not in USED: USED.append(k)
    return IMG[k]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'

def head(title, desc, path, og_img=None):
    short = title.split(" | ")[0]
    t, _, kick = short.partition(": ")
    slug = (path.strip("/").replace("/", "-") or "home").replace(".html", "")
    ogp = og_card(OUT, slug, t, kick or "Boston Travel Agency")
    og = f'<meta property="og:image" content="https://{DOMAIN}/{ogp}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
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
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
{FONTS}
<link rel="stylesheet" href="/styles.css?v={CSSV}">
</head>
<body>
"""

def nav(active=""):
    links = "".join(f'<a href="/{c["slug"]}/"{" aria-current=page" if c["slug"]==active else ""}>{e(c["nav"])}</a>' for c in CATS)
    return f"""<header class="top"><div class="wrap bar">
<a class="brand" href="/"><img class="logo-vintage" src="/logo.svg" width="88" height="61" alt=""><span class="wm"><span class="wm-name">Boston Travel Agency</span><span class="wm-tag">Est. 1965 &middot; Bespoke Private Travel</span></span></a>
<nav class="links"><a href="/about/"{" aria-current=page" if active=="about" else ""}>About Us</a>{links}<a href="/boston-events/"{" aria-current=page" if active=="boston-events" else ""}>Events</a><a href="/where-to-stay/"{" aria-current=page" if active=="where-to-stay" else ""}>Where to Stay</a><a href="/sample-itineraries/" class="cta-sm">Sample Itineraries</a></nav>
</div></header>
"""

def foot():
    return f"""<footer class="foot">
<div class="wrap foot-grid">
<div><div class="brand light"><img class="logo-vintage" src="/logo-dark.svg" width="88" height="61" alt=""><span class="wm"><span class="wm-name">Boston Travel Agency</span><span class="wm-tag">Est. 1965 &middot; Bespoke Private Travel</span></span></div>
<p>Family-run since 1965 and Boston at heart. Today we're a private travel consultancy planning personalized trips around the world, and this site is where we share our favorite tours, tips and happenings in the city we love.</p></div>
<div><h4>Explore</h4>{''.join(f'<a href="/{c["slug"]}/">{e(c["title"])}</a>' for c in CATS)}</div>
<div><h4>More</h4><a href="/sample-itineraries/">Sample itineraries</a><a href="/boston-events/">Events calendar</a><a href="/what-to-eat-in-boston/">What to eat in Boston</a><a href="/boston-selfie-hunt/">Boston Selfie Hunt</a><a href="/where-to-stay/">Where to stay</a><a href="/about/">About us</a><a href="/contact/">Contact us</a><a href="/photo-credits/">Photo credits</a></div>
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
    if rating is None: rv = '<span class="muted">New on Viator</span>'
    return f"""<article class="tour"><h3>{e(title)}</h3><p>{e(blurb)}</p>
<ul class="meta"><li>{stars(rating) if rating is not None else ""} {rv}</li><li>{e(dur)}</li><li>From about ${price}</li></ul>
<a class="btn" href="{vlink(path)}" target="_blank" rel="sponsored noopener">Check dates &amp; book</a></article>"""

def write(path, content):
    if path.endswith(".html"):
        prefix = "../" * path.count("/")
        content = content.replace('href="/"', 'href="%s"' % (prefix or "./")).replace('href="/', 'href="%s' % prefix).replace('src="/', 'src="%s' % prefix)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    with open(full, "w") as f: f.write(content)

# ---------- category pages ----------
for c in CATS:
    secs = ""
    for i, s in enumerate(c["sections"]):
        body = "".join(f"<p>{tl(p)}</p>" for p in s["paras"])
        img = figure(s["img"]) if s.get("img") else ""
        secs += f'<section class="story{" flip" if i % 2 else ""}"><div class="story-text"><h2>{e(s["h"])}</h2>{body}</div>{img}</section>'
    f = c["feature"]
    def feat_li(it):
        if len(it) == 3:  # (name, text, photo key): photo card
            a, b, k = it; url, cap = use(k)[0], use(k)[5]
            return f'<li class="dish"><img src="{url}" alt="{e(cap)}" loading="lazy"><div class="dish-body"><strong>{e(a)}</strong><span>{e(b)}</span><small class="cr">{credit(k)}</small></div></li>'
        a, b = it
        return f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>'
    feat = "".join(feat_li(it) for it in f["items"])
    tro, tstrip = "", ""
    if c.get("trophies"):
        T = c["trophies"]; total = sum(len(t["years"]) for t in T["teams"])
        def tcard(t):
            chips = "".join(f"<li>{e(y)}</li>" for y in t["years"])
            return f'<article class="trophy" style="--c1:{t["c1"]};--c2:{t["c2"]}"><header><span class="tro-n">{len(t["years"])}</span><span class="tro-t">{e(t["trophy"])}</span></header><div class="tro-b"><h3>{e(t["name"])}</h3><ul class="tro-y">{chips}</ul><p>{e(t["note"])}</p></div></article>'
        tro = f'<section class="wrap" id="championships"><h2 class="sec">{e(T["h"])}</h2><p class="tro-intro"><strong>{total} world championships</strong> across four teams. {e(T["intro"])}</p><div class="trophies">{"".join(tcard(t) for t in T["teams"])}</div></section>'
        tstrip = '<a class="tro-strip" href="#championships">' + "".join(f'<span style="--c1:{t["c1"]}"><b>{len(t["years"])}</b> {e(t["name"].replace("Boston ","").replace("New England ",""))}</span>' for t in T["teams"]) + f'<em>{total} titles &darr;</em></a>'
    tips = "".join(f"<li>{e(t)}</li>" for t in c["tips"])
    intro = "".join(f"<p>{p}</p>" for p in c["intro"])
    page = head(f"{c['title']} | Boston Travel Agency", c["intro"][0][:155], c["slug"] + "/", c["hero"]) + nav(c["slug"]) + \
        hero(c["hero"], e(c["kicker"]), e(c["title"]), intro, '<div class="hero-ctas"><a class="btn big" href="#tours">See our top tours</a></div>', small=True) + f"""
<div class="wrap">{tstrip}{secs}</div>
<section class="band"><div class="wrap"><h2 class="sec">{e(f['h'])}</h2><ul class="feature">{feat}</ul>{('<p class="feat-note">' + e(f["note"]) + '</p>') if f.get("note") else ""}</div></section>
{tro}
<section class="wrap" id="tours"><h2 class="sec">Our top tours</h2>
<div class="grid">{''.join(card(t) for t in c['tours'])}</div>
<aside class="tips"><h3>Local tips</h3><ul>{tips}</ul></aside>
{'<a class="itin-callout" href="/what-to-eat-in-boston/"><strong>Hungry?</strong> See our guide to what to eat in Boston, from cannoli to the roast beef three-way &rarr;</a>' if c["slug"]=="north-end-food-tours" else ""}
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
itin = head("Sample Boston Itineraries: 2, 3 and 5 Days | Boston Travel Agency", "Day-by-day sample itineraries for 2, 3 and 5 days in Boston, with the best tours and where to eat, from a family-run Boston travel agency est. 1965.", "sample-itineraries/", "statehouse") + nav("") + \
    hero("statehouse", "Plan your visit", "Sample Boston itineraries", "".join(f"<p>{p}</p>" for p in ITIN_INTRO), small=True) + f"""
{anchors}
<section class="wrap"><nav class="tabs" aria-label="Choose an itinerary">{tabs}</nav></section>
<section class="wrap"><aside class="before-go"><strong>Before you go: where to stay.</strong> For a 2 or 3-day trip we suggest the Back Bay or the North End and Waterfront, which put most of these plans within walking distance. <a href="/where-to-stay/">See our neighborhood guide &rarr;</a></aside></section>
<section class="wrap days" id="days"><p class="muted center">Showing the <span id="plan-count">2</span>-day plan. Days build on each other, so a longer trip simply adds days.</p>
{''.join(day_block(d) for d in DAYS)}</section>
<section class="band"><div class="wrap"><h2 class="sec">Make it your own</h2><ul class="feature">{seas}</ul>
<p class="muted small-note">Restaurants are examples we like; hours and menus change, so check before you go. Tour bookings are handled by Viator.</p></div></section>
""" + itin_js + foot()
write("sample-itineraries/index.html", itin)

# ---------- where to stay ----------
def hotel_li(h):
    tier, name, why = h
    return f'<li class="hotel t-{tier.lower()}"><span class="tier">{e(tier)}</span><strong>{e(name)}</strong><span class="muted">{e(why)}</span></li>'
def hood_block(i, h):
    link = f'<a class="compare" href="{KAYAK_LINK.format(q=h["slug"])}" target="_blank" rel="sponsored noopener">Compare {e(h["name"])} hotels and prices &rarr;</a>' if KAYAK_LINK else ""
    return f"""<section class="story{' flip' if i % 2 else ''}" id="{h['slug']}"><div class="story-text"><h2>{e(h['name'])}</h2><p>{e(h['summary'])}</p><p class="muted"><strong>Good to know:</strong> {e(h['good'])}</p>
<ul class="hotels">{''.join(hotel_li(x) for x in h['hotels'])}</ul>{link}</div>{figure(h['img'])}</section>"""
picker = "".join(f'<li><a href="#{next(h["slug"] for h in HOODS if h["name"]==n)}"><strong>{e(w)}</strong><span>Stay in {e(n)} &rarr;</span></a></li>' for w, n in PICKER)
tiers = "".join(f'<li class="t-{t.lower()}"><span class="tier">{e(t)}</span><span>{e(d)}</span></li>' for t, d in TIERS)
stips = "".join(f"<li>{e(t)}</li>" for t in STAY_TIPS)
stay = head("Where to Stay in Boston: Best Neighborhoods and Hotels | Boston Travel Agency", "Our neighborhood guide to where to stay in Boston, with luxury, classic and value hotel picks in the Back Bay, North End, Beacon Hill, Seaport, Cambridge and Fenway.", "where-to-stay/", "rowes") + nav("where-to-stay") + \
    hero("rowes", "Plan your visit", "Where to stay in Boston", "".join(f"<p>{p}</p>" for p in STAY_INTRO), small=True) + f"""
<section class="wrap"><h2 class="sec">Find your neighborhood</h2><ul class="picker">{picker}</ul>
<h2 class="sec">Three ways to stay</h2><ul class="tiers">{tiers}</ul></section>
<div class="wrap">{''.join(hood_block(i, h) for i, h in enumerate(HOODS))}</div>
<section class="wrap"><aside class="tips"><h3>Booking tips</h3><ul>{stips}</ul></aside>
<a class="itin-callout" href="/sample-itineraries/"><strong>Now plan your days.</strong> See our 2, 3 and 5-day Boston itineraries &rarr;</a>
<p class="muted small-note">Hotel picks are our suggestions; rates, renovations and availability change, so check current details before you book.</p></section>
""" + foot()
write("where-to-stay/index.html", stay)


# ---------- events ----------
def ev_when(s, e2, conf, ev):
    if conf is None: return e(ev["when"]), "Typical timing"
    if conf: return fmt_range(s, e2), "Confirmed" if ev.get("confirmed") else "Annual date"
    return "Likely " + fmt_range(s, e2), "Typical timing: " + e(ev["when"])
def ev_card(row, compact=False):
    s, e2, conf, ev = row
    when, note = ev_when(s, e2, conf, ev)
    badge = '<span class="ev-badge">Dates confirmed</span>' if conf and ev.get("confirmed") else ""
    url = use(ev["img"])[0]
    chip = f'<span class="ev-chip"><span class="m">{s.strftime("%b")}</span><span class="d">{s.day if conf is not None else "&middot;"}</span></span>'
    if compact:
        return f"""<a class="ev-mini" data-end="{e2.isoformat()}" href="/boston-events/#{ev['slug']}" style="background-image:linear-gradient(180deg,rgba(10,20,40,.05) 25%,rgba(10,20,40,.85)),url('{url}')">{chip}<span class="h">{e(ev['name'])}</span><span class="w">{when}</span></a>"""
    paras = "".join(f"<p{' class=ev-trip' if p.startswith('Make it part of your trip') else ''}>{e(p)}</p>" for p in ev["story"])
    paras = paras.replace("Make it part of your trip:", "<strong>Make it part of your trip:</strong>")
    tour = f'<a class="btn" href="{vlink(ev["tour"][1])}" target="_blank" rel="sponsored noopener">{e(ev["tour"][0])}</a>' if ev["tour"] else ""
    cal = f'<a class="ev-act" href="/boston-events/cal/{ev["slug"]}.ics" download>&#128197; Add to calendar</a>' if conf is not None else ""
    tour += f'<span class="ev-acts">{cal}<button class="ev-act share" type="button" data-title="{e(ev["name"])}: {when}" data-path="/boston-events/#{ev["slug"]}">&#8599; Share</button></span>'
    off = f'<a class="ev-off" href="{e(ev["link"])}" target="_blank" rel="noopener">Official site &rarr;</a>' if ev.get("link") else ""
    return f"""<article class="ev" data-end="{e2.isoformat()}" id="{ev['slug']}">
<div class="ev-photo" style="background-image:url('{url}')">{chip}</div>
<div class="ev-body"><h3>{e(ev['name'])}</h3><p class="ev-when"><strong>{when}</strong> {badge}<br><span class="muted">{e(ev['where'])} &middot; {note}</span></p>{paras}
<div class="ev-links">{tour}{off}</div><p class="ev-credit">{credit(ev['img'])}</p></div></article>"""
share_js = """<script>(function(){function toast(m){var t=document.createElement('div');t.className='toast';t.textContent=m;document.body.appendChild(t);setTimeout(function(){t.remove()},2200)}
document.querySelectorAll('.share').forEach(function(b){b.addEventListener('click',function(){var u=location.origin+b.dataset.path,d={title:b.dataset.title,text:b.dataset.title,url:u};
if(navigator.share){navigator.share(d).catch(function(){})}else if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){toast('Link copied')})}else{prompt('Copy this link',u)}})})})();</script>"""
hide_past = "<script>(function(){var t=new Date().toISOString().slice(0,10);document.querySelectorAll('[data-end]').forEach(function(x){if(x.dataset.end<t)x.hidden=true});})();</script>"
ev_page = head("Boston Events Calendar: Marathon, Feasts, Head of the Charles and More | Boston Travel Agency",
    "The big annual events in Boston and nearby, with upcoming dates: the Boston Marathon, July 4th, the North End feasts, the Head of the Charles, First Night and more.", "boston-events/", "marathon") + nav("boston-events") + \
    hero("marathon", "Plan around the big days", "Boston events calendar", "".join(f"<p>{p}</p>" for p in EVENTS_INTRO), small=True) + f"""
<section class="wrap"><div class="ev-list">{''.join(ev_card(r) for r in UPCOMING)}</div>
<aside class="tips"><h3>Planning tips</h3><ul><li>Hotels sell out and prices jump on Marathon weekend, Head of the Charles weekend and college graduation weekends in May. Book as early as you can.</li><li>For July 4th and First Night, take the T; streets near the Esplanade and the waterfront close to traffic.</li><li>The North End feasts are free. Go hungry and bring cash for the street vendors.</li></ul></aside>
<p class="muted small-note">Dates marked "likely" follow each event's usual pattern and may change. Always confirm on the official site before you book. Last updated {TODAY.strftime("%B %Y")}.</p>
<a class="itin-callout" href="/sample-itineraries/"><strong>Coming for an event?</strong> Build the rest of your trip with our 2, 3 and 5-day itineraries &rarr;</a></section>
""" + hide_past + share_js + foot()
write("boston-events/index.html", ev_page)
def ics(row):
    s, e2, conf, ev = row
    nxt = (e2 + dt.timedelta(1)).strftime("%Y%m%d")
    desc = (ev["story"][0] + " More: https://" + DOMAIN + "/boston-events/#" + ev["slug"]).replace(",", "\\,").replace(";", "\\;")
    return "\r\n".join(["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Boston Travel Agency//Events//EN", "BEGIN:VEVENT",
        f"UID:{ev['slug']}-{s.year}@{DOMAIN}", f"DTSTAMP:{TODAY.strftime('%Y%m%d')}T000000Z", f"DTSTART;VALUE=DATE:{s.strftime('%Y%m%d')}", f"DTEND;VALUE=DATE:{nxt}",
        f"SUMMARY:{ev['name']}" + ("" if conf else " (typical dates, confirm before booking)"), f"LOCATION:{ev['where'].replace(',', chr(92) + ',')}\\, Boston area",
        f"DESCRIPTION:{desc}", f"URL:https://{DOMAIN}/boston-events/#{ev['slug']}", "END:VEVENT", "END:VCALENDAR", ""])
for r in UPCOMING:
    if r[2] is not None: write(f"boston-events/cal/{r[3]['slug']}.ics", ics(r))


# ---------- what to eat ----------
def eat_card(c):
    url = use(c["img"])[0]
    spots = "".join(f'<li><strong>{e(n)}</strong> <span class="muted">{e(w)}{(" &middot; " + e(x)) if x else ""}</span></li>' for n, w, x in c["spots"])
    spots = f'<ul class="eat-spots">{spots}</ul>' if spots else ""
    tour = f'<div class="ev-links"><a class="btn" href="{vlink(c["tour"][1])}" target="_blank" rel="sponsored noopener">{e(c["tour"][0])}</a></div>' if c["tour"] else ""
    return f"""<article class="ev" id="{c['slug']}"><div class="ev-photo" style="background-image:url('{url}')"></div>
<div class="ev-body"><p class="eyebrow dark">{e(c['kicker'])}</p><h3>{e(c['name'])}</h3>{''.join(f"<p>{p}</p>" for p in c['paras'])}{spots}{tour}<p class="ev-credit">{credit(c['img'])}</p></div></article>"""
jump = "".join(f'<a href="#{c["slug"]}">{e(c["name"].split(",")[0])}</a>' for c in CLASSICS)
trend = "".join(f'<li><strong>{e(t["name"])}</strong><span class="where">{e(t["where"])}</span><span>{e(t["what"])}</span></li>' for t in TRENDING)
eat = head("What to Eat in Boston: Cannoli, Lobster Rolls, Roast Beef and More | Boston Travel Agency",
    "The foods you have to try in Boston, from North End cannoli and lobster rolls to the North Shore roast beef three-way, plus what's hot in the Seaport right now.", "what-to-eat-in-boston/", "mikes") + nav("what-to-eat") + \
    hero("lobster", "Eat like a local", "What to eat in Boston", "".join(f"<p>{p}</p>" for p in EAT_INTRO), small=True) + f"""
<section class="wrap"><nav class="eat-jump" aria-label="Jump to">{jump}<a href="#food-tours">Food tours</a><a href="#hot-right-now">Hot right now</a></nav>
<h2 class="sec">The Boston classics</h2><div class="ev-list">{''.join(eat_card(c) for c in CLASSICS)}</div></section>
<section class="band" id="food-tours"><div class="wrap"><h2 class="sec">Taste it all on a food tour</h2><p class="muted big">The easiest way to try cannoli, pizza, arancini and more in one afternoon, with a local guide and the neighborhood's stories.</p><div class="grid">{''.join(card(t) for t in FOOD['tours'])}</div></div></section>
<section class="wrap" id="hot-right-now"><div class="wrap"><h2 class="sec">Hot right now</h2><p class="muted big">The places Boston is buzzing about as of {TRENDING_AS_OF}. Restaurants change quickly, so check hours and book ahead.</p><ul class="feature trend">{trend}</ul></section>
<section class="wrap"><a class="itin-callout" href="/north-end-food-tours/"><strong>Want a guide?</strong> A North End food tour is the easiest way to try cannoli, pizza and more in one afternoon &rarr;</a>
<p class="muted small-note">Restaurants, hours and menus change. These are places we like; check before you go.</p></section>
""" + foot()
write("what-to-eat-in-boston/index.html", eat)


# ---------- selfie hunt ----------
def selfie_card(i, s):
    url = use(s["img"])[0]
    tour = f'<div class="ev-links"><a class="btn ghost" href="{vlink(s["tour"][1])}" target="_blank" rel="sponsored noopener">Make it a tour: {e(s["tour"][0])}</a></div>' if s["tour"] else ""
    return f"""<article class="ev sh" id="{s['slug']}"><div class="ev-photo" style="background-image:url('{url}')"><span class="ev-chip"><span class="m">Stop</span><span class="d">{i}</span></span></div>
<div class="ev-body"><h3>{e(s['name'])}</h3><p class="muted">{e(s['where'])}</p><p>{s['tip']}</p>
<label class="got"><input type="checkbox" data-k="{s['slug']}"> <span>Got it!</span></label>{tour}<p class="ev-credit">{credit(s['img'])}</p></div></article>"""
bonus = "".join(f'<li><label class="got"><input type="checkbox" data-k="{k}"> <span><strong>{e(n)}</strong><br><span class="muted">{e(w)}</span></span></label></li>' for k, n, w in BONUS)
sh_js = """<script>(function(){var K='bta-selfie-hunt',d={};try{d=JSON.parse(localStorage.getItem(K)||'{}')}catch(x){}
var bs=document.querySelectorAll('.got input'),n=bs.length;function up(){var c=0;bs.forEach(function(b){if(b.checked)c++;b.closest('.got').classList.toggle('on',b.checked)});
document.getElementById('sh-count').textContent=c+' of '+n;document.getElementById('sh-bar').style.width=(100*c/n)+'%';
document.getElementById('sh-done').hidden=c<10;}
bs.forEach(function(b){b.checked=!!d[b.dataset.k];b.addEventListener('change',function(){d[b.dataset.k]=b.checked;try{localStorage.setItem(K,JSON.stringify(d))}catch(x){}up();});});
document.getElementById('sh-reset').addEventListener('click',function(){d={};try{localStorage.removeItem(K)}catch(x){}bs.forEach(function(b){b.checked=false});up();});up();})();</script>"""
badge_js = """<script>(function(){var btn=document.getElementById('sh-badge');if(!btn)return;
function names(sel){return Array.prototype.map.call(document.querySelectorAll(sel),function(i){return i.dataset.n})}
btn.addEventListener('click',function(){var top=document.querySelectorAll('.sh .got input'),all=document.querySelectorAll('.got input'),t=0,a=0,got=[];
top.forEach(function(i){if(i.checked){t++;got.push(i.closest('.ev-body').querySelector('h3').textContent)}});all.forEach(function(i){if(i.checked)a++});
var W=1080,H=1350,c=document.createElement('canvas');c.width=W;c.height=H;var x=c.getContext('2d');
x.fillStyle='#14284b';x.fillRect(0,0,W,H);x.fillStyle='#b2452f';x.fillRect(0,H-36,W,36);
x.fillStyle='#b2452f';x.beginPath();x.roundRect?x.roundRect(80,80,120,120,28):x.rect(80,80,120,120);x.fill();
x.fillStyle='#f6f1e8';x.font='bold 40px Georgia,serif';x.textAlign='center';x.fillText('BTA',140,158);
x.textAlign='left';x.font='bold 40px Georgia,serif';x.fillText('Boston Travel Agency',230,135);x.fillStyle='#f5c3b3';x.font='600 22px Arial,sans-serif';x.fillText('EST. 1965 \u00b7 BESPOKE PRIVATE TRAVEL',232,175);
var done=t>=10;x.fillStyle='#f5c3b3';x.font='600 34px Arial,sans-serif';x.fillText(done?'I COMPLETED THE':'I\u2019M ON THE',80,330);
x.fillStyle='#fff';x.font='bold 96px Georgia,serif';x.fillText('Boston',80,440);x.fillText('Selfie Hunt',80,550);
x.fillStyle='#b2452f';x.font='bold 150px Georgia,serif';x.fillText(t+'/10',80,720);x.fillStyle='#f6f1e8';x.font='32px Arial,sans-serif';x.fillText('top icons collected'+(a>t?'  +'+(a-t)+' bonus':''),80,775);
x.font='30px Arial,sans-serif';var y=850;got.slice(0,10).forEach(function(n,i){x.fillStyle='#f5c3b3';x.fillText('\u2713',i<5?80:560,y+(i%5)*58);x.fillStyle='#f6f1e8';x.fillText(n.length>27?n.slice(0,26)+'\u2026':n,(i<5?80:560)+44,y+(i%5)*58)});
x.fillStyle='#f6f1e8';x.font='bold 34px Arial,sans-serif';x.textAlign='right';x.fillText('bostontravelagency.com/boston-selfie-hunt',W-80,H-80);
c.toBlob(function(bl){var f=new File([bl],'boston-selfie-hunt.png',{type:'image/png'}),txt=(done?'I completed the Boston Selfie Hunt!':'I\u2019ve collected '+t+' of 10 Boston icons on the Boston Selfie Hunt!')+' '+location.origin+'/boston-selfie-hunt/';
if(navigator.canShare&&navigator.canShare({files:[f]})){navigator.share({files:[f],text:txt,title:'Boston Selfie Hunt'}).catch(function(){})}
else{var l=document.createElement('a');l.href=URL.createObjectURL(bl);l.download='boston-selfie-hunt.png';l.click();}},'image/png');});})();</script>"""
sh = head("The Boston Selfie Hunt: 20 Iconic Photos to Collect | Boston Travel Agency",
    "A free, fun day in Boston: collect the city's 20 most iconic photos, from the Make Way for Ducklings statues to Acorn Street, Faneuil Hall, Fenway and the John Harvard statue.", "boston-selfie-hunt/", "ducklings") + nav("selfie") + \
    hero("acorn", "A free, fun day in Boston", "The Boston Selfie Hunt", "".join(f"<p>{p}</p>" for p in SELFIE_INTRO), small=True) + f"""
<div class="sh-page"></div><div class="sh-progress" role="status"><div class="wrap"><strong>Your hunt:</strong> <span id="sh-count">0 of {len(TOP)+len(BONUS)}</span> collected<div class="sh-track"><div id="sh-bar"></div></div><button id="sh-reset" class="sh-reset" type="button">Reset</button></div></div>
<section class="wrap"><h2 class="sec">The top 10, in walking order</h2><p class="muted big">Start in the Public Garden in the morning and finish in Harvard Square by dinner. Comfortable shoes recommended.</p>
<div class="ev-list">{''.join(selfie_card(i + 1, s) for i, s in enumerate(TOP))}</div>
<div class="sh-share"><p id="sh-done" class="sh-done" hidden><strong>You collected the top 10!</strong> You've officially seen Boston. Share your badge, then try the bonus round.</p>
<button id="sh-badge" class="btn big" type="button">Share my Selfie Hunt badge</button><p class="muted">Creates a picture of your progress to post on Instagram, Facebook or send by text.</p></div></section>
<section class="band"><div class="wrap"><h2 class="sec">The bonus round</h2><ul class="sh-bonus">{bonus}</ul></div></section>
<section class="wrap"><a class="itin-callout" href="/sample-itineraries/"><strong>Staying a few days?</strong> Pair the hunt with our 2, 3 and 5-day itineraries &rarr;</a>
<p class="muted small-note">Your checklist is saved only in this browser on this device. Please be respectful when taking photos on residential streets like Acorn Street.</p></section>
""" + sh_js + badge_js + foot()
write("boston-selfie-hunt/index.html", sh)

# ---------- home ----------
def tile(c):
    url = IMG[c["tile"]][0]; use(c["tile"])
    return f"""<a class="tile" href="/{c['slug']}/" style="background-image:linear-gradient(180deg,rgba(10,20,40,.05) 30%,rgba(10,20,40,.85)),url('{url}')"><span class="k">{e(c['kicker'])}</span><span class="h">{e(c['title'])}</span><span class="go">Explore &rarr;</span></a>"""
picks = [FREEDOM["tours"][0], WATER["tours"][0], FOOD["tours"][0], SPORTS["tours"][0], DAYTRIPS["tours"][0], FAMILY["tours"][1]]
home = head("Boston Travel Agency | The Best Tours & Things to Do in Boston",
            "Hand-picked Boston tours from a family-run Boston travel agency, est. 1965: the Freedom Trail, whale watching, food tours, Fenway Park, day trips and more.", "", "hero") + nav() + \
    hero("hero", "Family-run since 1965 &middot; Bespoke private travel", "The best of Boston,<br>picked by people who live here.",
         "<p>We've sorted through hundreds of Boston tours so you don't have to. Every experience here is highly rated, easy to book, and something we'd send our own family on.</p>",
         '<div class="hero-ctas"><a class="btn big" href="#explore">Explore Boston</a><a class="btn ghost light big" href="/sample-itineraries/">See sample itineraries</a></div>') + f"""
<section class="wrap intro-block">
<h2 class="sec">Curated, memorable Boston experiences</h2>
<p>Boston Travel was founded in 1965 in the heart of Boston's North End. What began as a neighborhood agency helping local families discover the world has grown into a deeply rooted, family-run company focused on crafting highly personalized travel experiences. With decades of experience and generations of local insight, our passion for travel is matched only by our love of this incredible city.</p>
<p>Today we're a private travel consultancy, planning personalized trips around the world with a special love for Italy. This site is a labor of love: our favorite tours, tips, events and places to eat in the city we call home, shared so you can come visit, learn, and love Boston as much as we do.</p>
</section>
<section class="itin-feature"><div class="wrap">
<p class="eyebrow dark">Plan your visit</p><h2 class="sec">Sample itineraries for 2, 3 and 5 days</h2>
<p class="muted big">Day-by-day plans with the best tours, where to eat and how to pace it, built by locals.</p>
<div class="plan-cards">{''.join(plan_card(p) for p in PLANS)}</div>
</div></section>
<section class="wrap"><h2 class="sec">Coming up in Boston</h2><div class="ev-strip">{''.join(ev_card(r, True) for r in UPCOMING[:4])}</div><p class="center"><a class="btn ghost" href="/boston-events/">See the full events calendar</a></p>
<a class="itin-callout" href="/what-to-eat-in-boston/"><strong>What to eat in Boston.</strong> Cannoli, lobster rolls, the North Shore roast beef three-way and what\'s hot right now &rarr;</a>
<a class="itin-callout" href="/boston-selfie-hunt/"><strong>No tour, just a fun day?</strong> Try the Boston Selfie Hunt and collect the city\'s 20 most iconic photos &rarr;</a></section>
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
<div><h3>Local since 1965</h3><p>We're a family-run, IATA-accredited agency founded in Boston in 1965. These are the tours and places we recommend to our own family and friends.</p></div>
</section>
""" + hide_past + foot()
write("index.html", home)

# ---------- contact ----------
if FORM_KEY:
    form = f"""<form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{FORM_KEY}"><input type="hidden" name="subject" value="New message from bostontravelagency.com">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
<label>Name<input name="name" required></label><label>Email<input type="email" name="email" required></label>
<label>Message<textarea name="message" rows="6" required></textarea></label>
<button class="btn big" type="submit">Send message</button></form>"""
else:
    form = ''
contact = head("Contact Us | Boston Travel Agency", "How to get help with a tour booked through our Boston guides.", "contact/") + nav() + f"""
<section class="wrap narrow prose"><h1 class="sec">Contact us</h1>
<p>Our private travel planning is reserved for longtime clients and the families they refer, so we aren't able to take new travel-planning requests through this site.</p>
<p>Booked a tour from one of our guides? Viator handles every booking, change and cancellation. Contact them through your confirmation email; their support team is available 24/7.</p>
{form}</section>
""" + foot()
write("contact/index.html", contact)

# ---------- about ----------
about = head("About Us | Boston Travel Agency", "Founded in 1965 in Boston's North End by a family from Italy, Boston Travel Agency shares free guides to the city it calls home.", "about/", "hanover") + nav("about") + \
    hero("hanover", "About us", "Boston at heart.<br>Italy in our blood.", "<p>A family-run travel agency since 1965.</p>", small=True) + f"""
<section class="wrap narrow prose">
<h2 class="sec">From the North End to Italy and back</h2>
<p>Boston Travel Agency was founded in 1965 in Boston's North End by a family who had made the journey from Italy themselves. In those years the neighborhood was home to thousands of Italian immigrants, and the agency became the place they turned to for travel between their two worlds: trips back to Italy for family celebrations, long-awaited visits to the towns they had left, and relatives making their way to Boston for the first time.</p>
<div class="heritage">
<figure><img src="../img/bta-first-office-1960s.jpg" width="980" height="670" loading="lazy" alt="Black and white photo of the original Boston Travel Agency storefront in the North End, with a man in a suit standing in the doorway under the sign"><figcaption><span class="h-yr">1960s</span>Where it all began: our first office in the North End, with &ldquo;Agenzia di Viaggi&rdquo; lettered on the window.</figcaption></figure>
<figure><img src="../img/bta-second-office-1970s.jpg" width="1061" height="692" loading="lazy" alt="Color photo of the second Boston Travel Agency office, a brick storefront with gold lettering on a North End street"><figcaption><span class="h-yr">Late 1970s</span>Our second home, opened right next door.</figcaption></figure>
</div>
<p>Six decades later, we're still family-run, and we still plan travel the same personal way: bespoke, private trips around the world, with Italy closest to our hearts. That work is reserved for our longtime clients and the families they refer, so it isn't something we offer through this website.</p>
<h2 class="sec">Why we made this site</h2>
<p>Because Boston is where our story began, and we never stopped loving it. This is the city where our family planted its roots, and we've spent a lifetime collecting its best walks, bites, traditions and hidden corners.</p>
<p>Boston is also one of the easiest and most rewarding cities in the world to explore on your own. It's compact and walkable, there's history on nearly every corner, the neighborhoods each have their own personality, and the food is worth the trip by itself. You don't need a travel agent to have a wonderful time here. You just need a few good tips from people who know it well.</p>
<p>So consider these guides our gift to anyone who wants to come visit, learn, and love Boston as much as we do. Everything here is free to use. Start with our <a href="/sample-itineraries/">sample itineraries</a>, check the <a href="/boston-events/">events calendar</a>, find out <a href="/what-to-eat-in-boston/">what to eat</a>, or spend a day on the <a href="/boston-selfie-hunt/">Boston Selfie Hunt</a>. When you find a tour you like, you can book it directly and securely through Viator.</p>
<p class="muted">Benvenuti a Boston. We hope you fall for it the way we did.</p>
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
write("logo.svg", vintage_svg("#14284b"))
write("favicon.svg", vintage_svg("#14284b"))
# our own historic photos (photos/ -> docs/img/)
import shutil
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
for fn in sorted(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos"))):
    shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos", fn), os.path.join(OUT, "img", fn))
write("logo-dark.svg", vintage_svg("#f6f1e8"))
write("logo-mark.svg", vintage_svg("#14284b"))
urls = [""] + ["sample-itineraries/", "where-to-stay/", "boston-events/", "what-to-eat-in-boston/", "boston-selfie-hunt/"] + [c["slug"] + "/" for c in CATS] + ["about/", "contact/", "photo-credits/"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>https://{DOMAIN}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
with open("styles.css") as f: write("styles.css", f.read())
print("built", OUT, "pages:", len(CATS) + 8, "photos:", len(USED))
