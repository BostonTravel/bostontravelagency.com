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
  "img": 'skyline', "story": ["Drums boom, cymbals crash and firecrackers pop as bright red and gold lions dance their way down Beach Street, stopping at every shop and restaurant to 'eat' the lettuce hung in the doorways for good luck.", "Boston's Chinatown is one of the oldest in the country, and the Lion Dance Parade is its biggest day of the year. It is loud, joyful and completely free, and kids love following the lions from door to door.", 'Make it part of your trip: come hungry. Dim sum on Lunar New Year morning is a Boston tradition, and Chinatown is a short walk from the Theater District and Boston Common.'],
  "tour": None, "link": "https://www.meetboston.com/events/"},
 {"slug": "st-patricks", "name": "St. Patrick's Day Parade", "where": "South Boston",
  "rule": ("sunday_near", 3, 17), "when": "The Sunday closest to March 17",
  "img": 'faneuil', "story": ['Bagpipes, marching bands, floats and a sea of green fill Broadway in South Boston, with hundreds of thousands of people cheering along the route.', "Few American cities are as proudly Irish as Boston, and the parade also marks Evacuation Day, when George Washington's army drove the British out of Boston on March 17, 1776. It is history and a party rolled into one.", "Make it part of your trip: wear green, take the Red Line to Broadway, and finish the day in one of the city's historic Irish pubs."],
  "tour": ("Freedom Trail History Pub Crawl", "/tours/Boston/Independence-Pub-Crawl/d678-74233P1"), "link": "https://www.southbostonparade.org/"},
 {"slug": "opening-day", "name": "Red Sox Opening Day at Fenway", "where": "Fenway Park",
  "month": 4, "when": "Late March or early April; see the Red Sox schedule",
  "img": 'fenway', "story": ["Red, white and blue bunting hangs from Fenway's grandstands, the whole team lines up along the baselines, and the first pitch at Opening Day feels like the end of a long New England winter.", 'Fenway Park opened in 1912 and is the oldest ballpark in the major leagues. Seeing the Green Monster on Opening Day, with the city buzzing all around Kenmore Square, is something Red Sox fans never forget.', 'Make it part of your trip: tickets are tough, so if you miss out, a Fenway Park tour gets you up on the Green Monster any day of the season.'],
  "tour": ("Tour of Historic Fenway Park", "/tours/Boston/Tour-of-Historic-Fenway-Park-Americas-Most-Beloved-Ballpark/d678-43406P1"), "link": "https://www.mlb.com/redsox/schedule"},
 {"slug": "patriots-day", "name": "Patriots' Day Reenactments", "where": "Lexington and Concord",
  "rule": ("nth_weekday", 4, 0, 3, 1), "fixed": True, "when": "Patriots' Day, the third Monday in April",
  "img": 'concord', "story": ['Before sunrise, hundreds of people gather on Lexington Green to watch minutemen in tricorn hats face down a column of redcoats, just as their ancestors did on April 19, 1775.', 'This is the very spot where the American Revolution began, and the reenactors are passionate about getting every detail right. Standing in the dawn chill as the first musket shots ring out gives you chills of a different kind.', "Make it part of your trip: pair it with the Freedom Trail in Boston, then drive the Battle Road to Concord's Old North Bridge for the afternoon ceremonies."],
  "tour": ("Private Day Trip to Lexington and Concord", "/tours/Boston/Private-Day-Trip-to-Lexington-and-Concord-from-Boston/d678-400049P5"), "link": "https://www.nps.gov/mima/"},
 {"slug": "marathon", "name": "Boston Marathon", "where": "Hopkinton to Boylston Street",
  "rule": ("nth_weekday", 4, 0, 3, 1), "fixed": True, "when": "Patriots' Day, the third Monday in April",
  "img": 'marathon', "story": ['Half a million people line the 26.2 miles from Hopkinton to Boylston Street, ringing cowbells, handing out orange slices and cheering for perfect strangers by name.', "Run every year since 1897, Boston is the world's oldest annual marathon and the one serious runners dream of qualifying for. The roar from the crowd as runners turn onto Boylston for the final stretch is pure Boston.", "Make it part of your trip: watch near the finish line in the Back Bay or at Heartbreak Hill in Newton, and book your hotel months ahead. Marathon Monday is also Patriots' Day, so you can catch the dawn reenactment first."],
  "tour": None, "link": "https://www.baa.org/"},
 {"slug": "boston-calling", "name": "Boston Calling Music Festival", "where": "Harvard Athletic Complex, Allston",
  "rule": ("memorial_weekend",), "when": "Memorial Day weekend, Friday to Sunday",
  "img": 'harvard', "story": ['Three days of headline bands, local favorites, food trucks and summer sunshine on the fields just across the river from Harvard Square.', 'Boston Calling kicks off the summer for the whole city, and it is easy to reach by T, so you can stay downtown and still catch every set.', 'Make it part of your trip: spend the mornings in Cambridge exploring Harvard Yard and Harvard Square, then head to the festival for the afternoon and evening shows.'],
  "tour": None, "link": "https://bostoncalling.com/"},
 {"slug": "july-4", "name": "Fourth of July and the Boston Pops Fireworks", "where": "Charles River Esplanade",
  "rule": ("fixed", 7, 4), "fixed": True, "when": "July 4, with Harborfest events in the days around it",
  "img": 'constitution', "story": ['Hundreds of thousands of people spread blankets on the Esplanade as the Boston Pops play patriotic favorites at the Hatch Shell, finishing with the 1812 Overture, real cannon fire and fireworks bursting over the Charles.', 'In July 1776 the Declaration of Independence was read to Bostonians from the balcony of the Old State House, and the reading is repeated there every Fourth. The whole city celebrates like it. On the morning of the Fourth, USS Constitution sails out for its annual turnaround cruise in the harbor.', 'Make it part of your trip: hear the Declaration read from the Old State House balcony in the morning, then claim a spot on the Esplanade by early afternoon. A harbor cruise is a great way to see the city from the water that week.'],
  "tour": ("Boston Harbor Sunset Cruise", "/tours/Boston/Northern-Lights-Sunset-Cruise/d678-5985P4"), "link": "https://www.july4th.org/"},
 {"slug": "sand-sculpting", "name": "International Sand Sculpting Festival", "where": "Revere Beach",
  "rule": ("weekend_of", 7, 4), "when": "A weekend in late July", "confirmed": {2027: ("2027-07-23", "2027-07-25")},
  "img": 'sandcastle', "story": ["World-class sand sculptors from around the globe turn America's first public beach into an open-air gallery, carving castles, faces and fantastic creatures that seem impossible to make from sand and water alone.", 'It is one of the biggest free events in New England, with fireworks, food vendors, rides and live music along the boardwalk. Watching the artists work, grain by grain, over the three days is half the fun.', "Make it part of your trip: take the Blue Line straight to Revere Beach station in about 20 minutes from downtown, and stay for a swim and a famous Kelly's roast beef sandwich."],
  "tour": None, "link": "https://www.reverebeachpartnership.com/"},
 {"slug": "fishermans-feast", "name": "Fisherman's Feast", "where": "North End",
  "rule": ("weekend_of", 8, 3, 3), "when": "Mid-August, Thursday to Sunday",
  "img": 'fishfeast', "story": ['Strings of lights, Italian music, sizzling sausage and peppers and fresh zeppole fill the narrow streets of the North End for four days in August.', "Started in 1910 by fishermen from Sciacca, Sicily, this is Boston's oldest Italian feast. The highlight is the Flight of the Angel on Sunday, when a young girl dressed as an angel is lowered on ropes above North Street to honor the Madonna. Crowds hold their breath.", 'Make it part of your trip: it is steps from the Paul Revere House and Old North Church, so combine it with a North End food tour or the Freedom Trail.'],
  "tour": ("North End Food Tour: Pizza, Pasta and Pastries", "/tours/Boston/North-End-Boston-Food-Tour/d678-91367P3"), "link": "https://www.fishermansfeast.com/"},
 {"slug": "st-anthonys", "name": "Saint Anthony's Feast", "where": "North End",
  "rule": ("last_weekend", 8), "when": "The last full weekend of August",
  "img": 'mikes', "story": ["The 'Feast of all Feasts' takes over Endicott and Thacher Streets with food stalls, cannoli, strolling singers and a festival crowd that feels like a giant neighborhood block party.", 'On Sunday, the statue of Saint Anthony is carried through the North End for about ten hours, covered in ribbons of dollar bills pinned on by the faithful and followed by marching bands. It is a living piece of Italian-American history you will not find anywhere else.', "Make it part of your trip: go on Sunday for the procession, then grab a cannoli on Hanover Street. The whole neighborhood looks forward to this weekend all year."],
  "tour": ("North End Food Tour with Wine and Limoncello", "/tours/Boston/Off-The-Eaten-Path-Tours/d678-331804P2"), "link": "https://www.stanthonysfeast.com/"},
 {"slug": "salem-october", "name": "Salem Haunted Happenings", "where": "Salem",
  "month": 10, "when": "All of October",
  "img": 'salem', "story": ['In October, the whole city of Salem dresses up: costume parades, candlelit ghost tours, haunted houses, psychics and street performers fill the historic downtown.', 'This is where the 1692 witch trials took place, and Salem tells that story with care at its memorials and museums. Add the colonial seaport, the House of the Seven Gables and fall foliage, and there is no better place to spend a day in October.', 'Make it part of your trip: skip the traffic and parking by taking the ferry from Long Wharf, about 50 minutes across the harbor. Go on a weekday if you can; weekends near Halloween are very busy.'],
  "tour": ("Salem High-Speed Ferry from Boston", "/tours/Boston/Salem-High-Speed-Ferry/d678-3283SALEM"), "link": "https://www.hauntedhappenings.org/"},
 {"slug": "head-of-the-charles", "name": "Head of the Charles Regatta", "where": "Charles River",
  "rule": ("hocr",), "when": "The weekend of the third Sunday in October",
  "img": 'hocr', "story": ['Thousands of rowing crews race up the winding Charles River, three at a time, while spectators line the bridges and riverbanks with coffee, cider donuts and blankets.', "It is the largest three-day rowing event in the world, drawing Olympians, college crews and masters rowers from around the globe, all against a backdrop of fall leaves, Harvard's boathouses and the Boston skyline.", "Make it part of your trip: watch from the Weeks or Eliot Bridges for the best views of the tight turns, and book your hotel early. October is Boston's busiest season."],
  "tour": ("Boston Duck Boat Tour with Charles River Splash", "/tours/Boston/Boston-Duck-Boat-Sightseeing-City-Tour-with-Cruise/d678-3037DUCK"), "link": "https://www.hocr.org/"},
 {"slug": "tree-lighting", "name": "Boston Common Tree Lighting", "where": "Boston Common",
  "rule": ("nth_weekday", 12, 3, 1, 1), "when": "Usually the first Thursday in December",
  "img": 'statehouse', "story": ["Carolers, ice skating on the Frog Pond and thousands of twinkling lights draped through Boston Common, all leading up to the countdown to light the city's official Christmas tree.", "Every year since 1971, Nova Scotia has sent Boston its tree as a thank-you for the city's help after the 1917 Halifax Explosion. It is a warm holiday tradition with a story behind it.", "Make it part of your trip: stroll Beacon Hill's gaslit streets afterward, and see the holiday windows and the tree at Faneuil Hall."],
  "tour": None, "link": "https://www.boston.gov/"},
 {"slug": "tea-party", "name": "Boston Tea Party Reenactment", "where": "Old South Meeting House and the waterfront",
  "rule": ("fixed", 12, 16), "when": "On or around December 16",
  "img": 'revere', "story": ["Join the crowd at Old South Meeting House as colonists in costume argue over the tax on tea, then follow the 'Sons of Liberty' to the waterfront and watch the tea go into the harbor.", 'On December 16, 1773, this protest helped spark the American Revolution. The reenactment happens where it really started, in the same meeting house where Samuel Adams spoke, and audiences are invited to shout along.', 'Make it part of your trip: visit the Boston Tea Party Ships and Museum, where you can toss tea overboard yourself, and walk the Freedom Trail the same week.'],
  "tour": ("Boston Tea Party Ships & Museum", "/tours/Boston/Admission-to-Boston-Tea-Party-Ships-and-Museum/d678-5650TEA"), "link": "https://www.revolutionaryspaces.org/"},
 {"slug": "first-night", "name": "First Night Boston", "where": "City Hall Plaza, Copley Square and the waterfront",
  "rule": ("fixed", 12, 31), "fixed": True, "when": "New Year's Eve",
  "img": 'hero', "story": ['A parade, glowing ice sculptures, live music on stages across the city and two rounds of fireworks, the last at midnight over Boston Harbor.', "Boston started First Night in 1976, and the idea of a citywide, family-friendly New Year's Eve arts celebration has since spread around the world. It is free, and the T is free in the evening, so the whole city comes out.", 'Make it part of your trip: see the ice sculptures by daylight, catch the early fireworks over Boston Common with kids, and head to the waterfront for midnight. Dress warmly.'],
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
