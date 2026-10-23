# The Boston Selfie Hunt. TOP stops have photos and are listed in walking order; BONUS stops are a checklist.
# Each TOP stop: slug, name, where, img, tip, tour (title, viator path) or None
SELFIE_INTRO = [
 "Don't feel like booking a tour? Here's a fun way to spend a day in Boston, whether you're visiting from far away or have lived here your whole life: collect the city's most iconic photos.",
 "Check off each stop as you snap it, and this page will remember your progress on your phone. The top 10 are listed in walking order, so you can do them all in one full day. Then go for the bonus round.",
]

TOP = [
 {"slug": "ducklings", "name": "Make Way for Ducklings", "where": "Public Garden, near Charles and Beacon Streets", "img": "ducklings",
  "tip": "Sit down next to Mrs. Mallard and her eight ducklings from the classic children's book. Locals dress them up for holidays, so you never know what they'll be wearing. Count them: Jack, Kack, Lack, Mack, Nack, Ouack, Pack and Quack.",
  "tour": None},
 {"slug": "acorn-street", "name": "Acorn Street", "where": "Beacon Hill, between Willow and West Cedar Streets", "img": "acorn",
  "tip": "Often called the most photographed street in America: cobblestones, brick row houses and gas lamps. Go early in the morning for the shot without the crowds, and remember people live here, so keep it quiet.",
  "tour": None},
 {"slug": "faneuil-hall", "name": "Faneuil Hall", "where": "Faneuil Hall Marketplace, downtown", "img": "faneuil",
  "tip": "The \"Cradle of Liberty,\" where colonists met to protest British taxes. Get the Samuel Adams statue out front in your shot, and look up for the golden grasshopper weathervane that has topped the building since 1742. Then wander through Quincy Market next door.",
  "tour": ("Freedom Trail History Small Group Walking Tour", "/tours/Boston/Explore-Revolutionary-Boston-Freedom-Trail-History-Tour/d678-66111P3")},
 {"slug": "paul-revere", "name": "Paul Revere and Old North Church", "where": "Paul Revere Mall, North End", "img": "oldnorth",
  "tip": "Line up Paul Revere on his horse in the foreground with the Old North Church steeple behind him, where the lanterns were hung: one if by land, two if by sea.",
  "tour": ("The Full Revolutionary Story: Small-Group Walking Tour", "/tours/Boston/The-Revolutionary-Story-Tour-An-Epic-Walking-Tour-of-Boston/d678-70284P1")},
 {"slug": "mikes-box", "name": "The Cannoli Box", "where": "Hanover Street, North End", "img": "mikes",
  "tip": "Hold up the famous white box tied with string from Mike's Pastry. Bonus points for a cannoli in the other hand. (A local might tell you to fill the box at Modern Pastry across the street. See our <a href=\"/what-to-eat-in-boston/#cannoli\">cannoli guide</a>.)",
  "tour": ("North End Food Tour: Pizza, Pasta and Pastries", "/tours/Boston/North-End-Boston-Food-Tour/d678-91367P3")},
 {"slug": "uss-constitution", "name": "USS Constitution", "where": "Charlestown Navy Yard", "img": "constitution",
  "tip": "\"Old Ironsides,\" launched in 1797, is the oldest commissioned warship still afloat, and it's free to visit. Walk across the bridge from the North End along the Freedom Trail, or take the water taxi.",
  "tour": ("Historic Sightseeing Harbor Cruise", "/tours/Boston/Boston-Historic-Sightseeing-Cruise/d678-3283SSCRUISE")},
 {"slug": "trinity-reflection", "name": "Trinity Church in the Glass", "where": "Copley Square, Back Bay", "img": "backbay",
  "tip": "Stand in Copley Square and line up 1877 Trinity Church with its reflection in the mirrored glass of the 200 Clarendon tower (the old John Hancock Tower). It's Boston's most famous architecture photo: old and new in one frame.",
  "tour": None},
 {"slug": "marathon-finish", "name": "The Marathon Finish Line", "where": "Boylston Street, in front of the Boston Public Library", "img": "marathon",
  "tip": "The blue and yellow finish line is painted on Boylston Street all year. Strike your best finishing pose, safely from the sidewalk or when the light is red.",
  "tour": None},
 {"slug": "fenway", "name": "Fenway Park", "where": "Jersey Street and Gate B, Fenway", "img": "fenway",
  "tip": "Pose with the Teammates statue of Ted Williams, Bobby Doerr, Johnny Pesky and Dom DiMaggio outside Gate B, or take the ballpark tour and get your photo on top of the Green Monster.",
  "tour": ("Tour of Historic Fenway Park", "/tours/Boston/Tour-of-Historic-Fenway-Park-Americas-Most-Beloved-Ballpark/d678-43406P1")},
 {"slug": "john-harvard", "name": "The John Harvard Statue", "where": "Harvard Yard, Cambridge", "img": "harvard",
  "tip": "Rub his left shoe for luck like millions before you (that's why it shines). Ask your guide why it's called \"the statue of three lies.\" Take the Red Line to Harvard to finish your day in Harvard Square.",
  "tour": ("Harvard University Campus Guided Walking Tour", "/tours/Boston/Harvard-Campus-Walking-Tour/d678-5950P2")},
]

BONUS = [
 ("state-house", "The gold dome of the State House", "From Boston Common, looking up Beacon Hill."),
 ("cheers", "The Cheers bar", "Beacon Street, across from the Public Garden. Where everybody knows your name."),
 ("swan-boats", "The Swan Boats", "Public Garden lagoon, spring through early fall."),
 ("citgo", "The Citgo sign", "Best from Kenmore Square or Commonwealth Avenue, glowing at night."),
 ("tortoise-hare", "The Tortoise and the Hare", "Copley Square, honoring the Marathon."),
 ("bobby-orr", "Bobby Orr's flying \"The Goal\" statue", "Outside TD Garden."),
 ("bpl", "The Boston Public Library", "The courtyard and the grand Bates Hall reading room, both free."),
 ("zakim", "The Zakim Bridge at night", "Lit up blue, best from the North End Park or the Charlestown side."),
 ("tea-party", "The Tea Party Ships", "Congress Street Bridge, Fort Point Channel."),
 ("fan-pier", "The skyline from Fan Pier", "Seaport, especially at sunset."),
]
