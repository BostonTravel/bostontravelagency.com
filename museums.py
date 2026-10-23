# Boston museums and attractions page, with Boston CityPASS(R) featured.
# CityPASS facts from citypass.com/boston (checked October 2026). Update prices when they change.

CITYPASS_URL = "https://www.anrdoezrs.net/click-101910852-17329798"  # CJ link: PID 101910852 (Boston Travel Guide), ad 17329798
CITYPASS_AS_OF = "October 2026"
CITYPASS = {
    "adult": "$84", "child": "$72", "adult_reg": "$152.95", "child_reg": "$122.30",
    "save": "up to 45%", "days": 9,
}

MUSEUMS_INTRO = [
    "Boston packs world-class museums into a small, walkable city. In a single day you can stand in front of a Rembrandt, watch indoor lightning, walk around a three-story tank of sea turtles and sharks, and still make it to the North End for dinner.",
    "Here are the museums and attractions we send our own friends and family to, starting with the easiest way to save on the big ones.",
]

# Picks for "which 4 should I choose?"
CP_PICKS = [
    ("With kids", "New England Aquarium, Museum of Science, Franklin Park Zoo and the harbor cruise."),
    ("First visit", "New England Aquarium, the harbor cruise, View Boston and the Museum of Fine Arts."),
    ("Rainy day", "Museum of Fine Arts, Museum of Science, Harvard Museum of Natural History and the New England Aquarium."),
]

# In Boston CityPASS: (slug, name, where, image key, paragraphs, viator tour or None)
IN_PASS = [
    ("aquarium", "New England Aquarium", "Central Wharf, on the waterfront", "cp_aquarium",
     ["The heart of the aquarium is the Giant Ocean Tank, a huge round reef tank you circle on a spiral ramp, coming face to face with sea turtles, sharks and schools of tropical fish. Penguins splash around the base, and there is a touch tank where kids can reach in."],
     ("New England Aquarium tickets", "/tours/Boston/New-England-Aquarium/d678-3162AQU")),
    ("museum-of-science", "Museum of Science", "Science Park, on the Charles River", "cp_mos",
     ["Hands-on exhibits on everything from dinosaurs to space, plus the Theater of Electricity, where a giant generator throws real indoor lightning. It straddles the Charles River between Boston and Cambridge, an easy walk from the North End."],
     None),
    ("mfa", "Museum of Fine Arts, Boston", "Huntington Avenue, near Fenway", "cp_mfa",
     ["One of the great art museums in the country, with Egyptian mummies, Impressionist masterpieces, a superb American wing and Paul Revere's own silver Sons of Liberty Bowl. Plan at least half a day."],
     None),
    ("harvard-natural-history", "Harvard Museum of Natural History", "Harvard, Cambridge", "cp_hmnh",
     ["Famous for the Glass Flowers, thousands of astonishingly real plant models made entirely of glass, plus dinosaur fossils, gemstones and towering skeletons. Your ticket also gets you into the Peabody Museum next door, so you can see both in one visit."],
     None),
    ("franklin-park-zoo", "Franklin Park Zoo", "Franklin Park, Dorchester", "cp_zoo",
     ["Gorillas, lions, giraffes and a butterfly garden in Boston's biggest park, about 20 minutes from downtown. CityPASS covers daytime general admission."],
     None),
    ("view-boston", "View Boston", "Top of the Prudential Center, Back Bay", "cp_viewboston",
     ["The observation deck at the top of the Prudential Center has 360-degree views over the Back Bay, Fenway Park, the Charles River and the harbor. Go near sunset for the best light."],
     None),
    ("harbor-cruise", "Boston Harbor City Cruises", "Long Wharf, on the waterfront", "cp_cruise",
     ["A narrated sightseeing cruise around Boston Harbor, with the skyline, the Harbor Islands and USS Constitution along the way. Book your sailing time ahead."],
     None),
]

# More museums: (slug, name, where, image key or None, paragraphs, viator tour or None)
MORE = [
    ("gardner", "Isabella Stewart Gardner Museum", "The Fenway, a short walk from the MFA", "mu_gardner",
     ["A Venetian-style palace built around a flower-filled courtyard, packed with the art Isabella Stewart Gardner collected and arranged herself. Empty frames still hang where 13 works were stolen in 1990, the biggest unsolved art theft in history.",
      "Fun fact: anyone named Isabella gets in free. Admission is also free every Thursday night from 5 to 9 pm (reserve ahead)."],
     None),
    ("ica", "Institute of Contemporary Art (ICA)", "Seaport, on the waterfront", "mu_ica",
     ["Boston's home for contemporary art, in a glass building that cantilevers out over the harbor. Even if modern art is not your thing, the harbor views from inside are worth the trip."],
     None),
    ("harvard-art-museums", "Harvard Art Museums", "Harvard, Cambridge", "mu_ham",
     ["Three museums under one glass roof: the Fogg, the Busch-Reisinger and the Arthur M. Sackler, with everything from Van Gogh and Picasso to ancient Asian art. It pairs perfectly with Harvard Yard and the natural history museum."],
     None),
    ("tea-party", "Boston Tea Party Ships & Museum", "Fort Point Channel", "ev_teaparty",
     ["Costumed colonists bring December 16, 1773 back to life on replica ships, and you get to throw the tea overboard yourself. One of the most fun history stops in the city, especially with kids."],
     ("Boston Tea Party Ships & Museum tickets", "/tours/Boston/Admission-to-Boston-Tea-Party-Ships-and-Museum/d678-5650TEA")),
    ("childrens-museum", "Boston Children's Museum", "Fort Point Channel, look for the giant milk bottle", "mu_bcm",
     ["Three floors of climbing, building and splashing for young kids, right on the water. You can't miss it: a 40-foot Hood milk bottle stands out front."],
     None),
    ("uss-constitution-museum", "USS Constitution Museum", "Charlestown Navy Yard", "constitution",
     ["Right next to Old Ironsides, the oldest commissioned warship afloat in the world. Touring the ship itself is free; the museum next door is pay what you wish, with hands-on exhibits about life at sea in 1812."],
     None),
    ("jfk-library", "John F. Kennedy Presidential Library and Museum", "Columbia Point, Dorchester", "mu_jfk",
     ["The I. M. Pei building on the harbor tells the story of JFK's life and presidency, from the 1960 campaign to the Cuban Missile Crisis. Allow a couple of hours."],
     None),
    ("african-american-history", "Museum of African American History", "Beacon Hill", "mu_aamh",
     ["Centered on the African Meeting House, built in 1806 and the oldest Black church building still standing in America, where abolitionists including Frederick Douglass spoke. It anchors the Black Heritage Trail on Beacon Hill."],
     None),
    ("mapparium", "The Mapparium", "Mary Baker Eddy Library, Back Bay", "mu_mapp",
     ["A three-story stained-glass globe you walk through on a glass bridge, showing the world as it was mapped in 1935. Whisper at one end and you can hear it clearly at the other. Small, quirky and unforgettable."],
     None),
    ("mit-museum", "MIT Museum", "Kendall Square, Cambridge", "mu_mit",
     ["Robots, holograms, kinetic sculpture and the latest from MIT's labs, in a bright new building in Kendall Square. A great stop for curious teens."],
     None),
]

MUSEUM_TIPS = [
    "Reserve timed tickets ahead for the New England Aquarium and the harbor cruise, especially on summer weekends and school vacations.",
    "The MFA and the Gardner are a 10-minute walk apart, so they pair easily in one day.",
    "Harvard's museums, Harvard Yard and Harvard Square make a perfect half day in Cambridge on the Red Line.",
    "Hours, prices and free days change, so check each museum's site before you go.",
]
