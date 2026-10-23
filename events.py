# Boston events guide. Dates are computed from each event's usual pattern; once organizers
# announce dates, add them under "confirmed" keyed by year: {2027: ("2027-07-23", "2027-07-25")}.
# Events that only have a month (lunar calendar, seasonal) use "month" instead of a rule.
# fixed=True means the date never moves (July 4, Dec 31), so it is shown without "typically".
import datetime as dt

EVENTS_INTRO = [
 "Boston's calendar is packed with traditions, from the Marathon on Patriots' Day to the feasts of the North End and First Night on New Year's Eve. Here are the events we think are worth planning a trip around, listed in order of what's coming up next.",
 "Where organizers have announced dates, we show them. Otherwise we show the date the event usually falls on, so check the official site before you book flights or hotels.",
]

EVENTS = [
 {"slug": "lunar-new-year", "name": "Lunar New Year in Chinatown", "where": "Chinatown",
  "month": 2, "when": "Late January or February, following the lunar calendar",
  "blurb": "Lion dances wind through Chinatown's streets with drums, firecrackers and crowds, usually on the weekend after the new year begins.",
  "tour": None, "link": "https://www.meetboston.com/events/"},
 {"slug": "st-patricks", "name": "St. Patrick's Day Parade", "where": "South Boston",
  "rule": ("sunday_near", 3, 17), "when": "The Sunday closest to March 17",
  "blurb": "One of the biggest St. Patrick's Day parades in the country, marching through Southie with bagpipers, bands and a very festive crowd.",
  "tour": ("Freedom Trail History Pub Crawl", "/tours/Boston/Independence-Pub-Crawl/d678-74233P1"), "link": "https://www.southbostonparade.org/"},
 {"slug": "opening-day", "name": "Red Sox Opening Day at Fenway", "where": "Fenway Park",
  "month": 4, "when": "Late March or early April; see the Red Sox schedule",
  "blurb": "The first home game at the oldest ballpark in the major leagues is a Boston holiday in all but name. Tickets go fast.",
  "tour": ("Tour of Historic Fenway Park", "/tours/Boston/Tour-of-Historic-Fenway-Park-Americas-Most-Beloved-Ballpark/d678-43406P1"), "link": "https://www.mlb.com/redsox/schedule"},
 {"slug": "patriots-day", "name": "Patriots' Day Reenactments", "where": "Lexington and Concord",
  "rule": ("nth_weekday", 4, 0, 3, 1), "fixed": True, "when": "Patriots' Day, the third Monday in April",
  "blurb": "At dawn on Lexington Green, reenactors restage the first shots of the Revolution, followed by battles and parades along the Battle Road to Concord.",
  "tour": ("Private Day Trip to Lexington and Concord", "/tours/Boston/Private-Day-Trip-to-Lexington-and-Concord-from-Boston/d678-400049P5"), "link": "https://www.nps.gov/mima/"},
 {"slug": "marathon", "name": "Boston Marathon", "where": "Hopkinton to Boylston Street",
  "rule": ("nth_weekday", 4, 0, 3, 1), "fixed": True, "when": "Patriots' Day, the third Monday in April", "img": "marathon",
  "blurb": "The world's oldest annual marathon. Watch the finish on Boylston Street or the climb up Heartbreak Hill in Newton. Book hotels early; the city fills up.",
  "tour": None, "link": "https://www.baa.org/"},
 {"slug": "boston-calling", "name": "Boston Calling Music Festival", "where": "Harvard Athletic Complex, Allston",
  "rule": ("memorial_weekend",), "when": "Memorial Day weekend, Friday to Sunday",
  "blurb": "Three days of big-name bands and local favorites across several stages, kicking off Boston's summer.",
  "tour": None, "link": "https://bostoncalling.com/"},
 {"slug": "july-4", "name": "Fourth of July and the Boston Pops Fireworks", "where": "Charles River Esplanade",
  "rule": ("fixed", 7, 4), "fixed": True, "when": "July 4, with Harborfest events in the days around it",
  "blurb": "The Boston Pops play on the Esplanade before fireworks over the Charles. Harborfest fills the waterfront with reenactments and the USS Constitution turnaround cruise.",
  "tour": ("Boston Harbor Sunset Cruise", "/tours/Boston/Northern-Lights-Sunset-Cruise/d678-5985P4"), "link": "https://www.july4th.org/"},
 {"slug": "sand-sculpting", "name": "International Sand Sculpting Festival", "where": "Revere Beach",
  "rule": ("weekend_of", 7, 4), "when": "A weekend in late July", "confirmed": {2027: ("2027-07-23", "2027-07-25")},
  "blurb": "Master sand sculptors from around the world compete on America's first public beach, with food, music and fireworks. Free to attend and a short Blue Line ride from downtown.",
  "tour": None, "link": "https://www.reverebeachpartnership.com/"},
 {"slug": "fishermans-feast", "name": "Fisherman's Feast", "where": "North End",
  "rule": ("weekend_of", 8, 3, 3), "when": "Mid-August, Thursday to Sunday",
  "blurb": "Boston's oldest Italian feast, honoring the Madonna del Soccorso. Don't miss the Flight of the Angel on Sunday, when a child is lowered over North Street.",
  "tour": ("North End Food Tour: Pizza, Pasta and Pastries", "/tours/Boston/North-End-Boston-Food-Tour/d678-91367P3"), "link": "https://www.fishermansfeast.com/"},
 {"slug": "st-anthonys", "name": "Saint Anthony's Feast", "where": "North End",
  "rule": ("last_weekend", 8), "when": "The last full weekend of August",
  "blurb": "The largest Italian religious festival in New England: a 10-hour procession, street food, music and the whole neighborhood out on the sidewalks.",
  "tour": ("North End Food Tour with Wine and Limoncello", "/tours/Boston/Off-The-Eaten-Path-Tours/d678-331804P2"), "link": "https://www.stanthonysfeast.com/"},
 {"slug": "salem-october", "name": "Salem Haunted Happenings", "where": "Salem",
  "month": 10, "when": "All of October",
  "blurb": "A month of Halloween parades, haunted tours and costume events in the Witch City. Take the ferry from Boston and skip the traffic.",
  "tour": ("Salem High-Speed Ferry from Boston", "/tours/Boston/Salem-High-Speed-Ferry/d678-3283SALEM"), "link": "https://www.hauntedhappenings.org/"},
 {"slug": "head-of-the-charles", "name": "Head of the Charles Regatta", "where": "Charles River",
  "rule": ("hocr",), "when": "The weekend of the third Sunday in October", "img": "hocr",
  "blurb": "The world's largest three-day rowing event. Spread a blanket on the riverbank near the Weeks or Eliot bridges and watch thousands of crews race past.",
  "tour": ("Boston Duck Boat Tour with Charles River Splash", "/tours/Boston/Boston-Duck-Boat-Sightseeing-City-Tour-with-Cruise/d678-3037DUCK"), "link": "https://www.hocr.org/"},
 {"slug": "tree-lighting", "name": "Boston Common Tree Lighting", "where": "Boston Common",
  "rule": ("nth_weekday", 12, 3, 1, 1), "when": "Usually the first Thursday in December",
  "blurb": "The city lights the tree sent each year by Nova Scotia as thanks for Boston's help after the 1917 Halifax Explosion.",
  "tour": None, "link": "https://www.boston.gov/"},
 {"slug": "tea-party", "name": "Boston Tea Party Reenactment", "where": "Old South Meeting House and the waterfront",
  "rule": ("fixed", 12, 16), "when": "On or around December 16",
  "blurb": "Join the debate at Old South Meeting House, then follow the 'Sons of Liberty' to the harbor as the tea goes overboard.",
  "tour": ("Boston Tea Party Ships & Museum", "/tours/Boston/Admission-to-Boston-Tea-Party-Ships-and-Museum/d678-5650TEA"), "link": "https://www.revolutionaryspaces.org/"},
 {"slug": "first-night", "name": "First Night Boston", "where": "City Hall Plaza, Copley Square and the waterfront",
  "rule": ("fixed", 12, 31), "fixed": True, "when": "New Year's Eve",
  "blurb": "America's original First Night, running since 1976: a parade, ice sculptures, music across the city and fireworks over Boston Harbor at midnight. Free, and the T is free in the evening.",
  "tour": None, "link": "https://www.firstnightboston.org/"},
]

D = dt.date
def _nth(y, m, wd, n):  # nth weekday (Mon=0) of month
    d = D(y, m, 1); d += dt.timedelta((wd - d.weekday()) % 7); return d + dt.timedelta(7 * (n - 1))
def _last(y, m, wd):
    d = (D(y, m + 1, 1) if m < 12 else D(y + 1, 1, 1)) - dt.timedelta(1)
    return d - dt.timedelta((d.weekday() - wd) % 7)

def dates_for(ev, y):
    """(start, end, confirmed) for year y, or None for month-only events."""
    if y in ev.get("confirmed", {}):
        s, e = ev["confirmed"][y]; return D.fromisoformat(s), D.fromisoformat(e), True
    r = ev.get("rule")
    if not r: return None
    k = r[0]
    if k == "fixed": d = D(y, r[1], r[2]); return d, d, ev.get("fixed", False)
    if k == "nth_weekday":
        d = _nth(y, r[1], r[2], r[3]); return d, d + dt.timedelta(r[4] - 1), ev.get("fixed", False)
    if k == "sunday_near":
        t = D(y, r[1], r[2]); off = (6 - t.weekday()) % 7
        return (t + dt.timedelta(off) if off <= 3 else t - dt.timedelta(7 - off),) * 2 + (False,)
    if k == "memorial_weekend":
        m = _last(y, 5, 0); return m - dt.timedelta(3), m - dt.timedelta(1), False
    if k == "weekend_of":  # Fri (or r[3] days earlier) to the nth Sunday of the month
        s = _nth(y, r[1], 6, r[2]); return s - dt.timedelta(r[3] if len(r) > 3 else 2), s, False
    if k == "last_weekend":
        s = _last(y, r[1], 6); return s - dt.timedelta(2), s, False
    if k == "hocr":
        s = _nth(y, 10, 6, 3); return s - dt.timedelta(2), s, False
    raise ValueError(k)

def upcoming(today):
    """Every event's next occurrence on or after today, sorted by date."""
    out = []
    for ev in EVENTS:
        for y in (today.year, today.year + 1):
            r = dates_for(ev, y)
            if r is None:
                s = D(y, ev["month"], 1); e = (D(y, ev["month"] + 1, 1) if ev["month"] < 12 else D(y + 1, 1, 1)) - dt.timedelta(1)
                r = (s, e, None)
            if r[1] >= today:
                out.append((r[0], r[1], r[2], ev)); break
    return sorted(out, key=lambda x: x[0])

def fmt_range(s, e):
    if s == e: return s.strftime("%a, %b ") + str(s.day) + f", {s.year}"
    if s.month == e.month: return s.strftime("%b ") + f"{s.day} to {e.day}, {s.year}"
    return s.strftime("%b ") + f"{s.day} to " + e.strftime("%b ") + f"{e.day}, {e.year}"
