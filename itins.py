# Sample itineraries. Each day lists the plans (2, 3, 5) it belongs to.
# Tours: (title, viator path). Eat: (name, neighborhood, why).
ITIN_INTRO = [
 "Boston is compact, walkable and packed with history, which makes it perfect for a short trip. These sample itineraries are the plans we would build for our own friends and family: the essentials in two days, the city plus Cambridge and Fenway in three, and the full experience, with a day trip, in five.",
 "Each day is paced for real people, with time to linger over lunch. Mix and match freely, and swap days around the weather and the season.",
]

PLANS = [
 ("2", "2 Days", "Boston essentials", "The Freedom Trail, the North End, Beacon Hill, the Back Bay and the harbor. The perfect long weekend."),
 ("3", "3 Days", "City, Cambridge & Fenway", "Everything in the 2-day plan, plus Harvard Yard and a behind-the-scenes look at Fenway Park."),
 ("5", "5 Days", "The complete Boston", "Add a food-focused day across the city's neighborhoods and a day trip to Salem, Concord or Plymouth."),
]

DAYS = [
 {"n": 1, "plans": "2 3 5", "title": "Revolutionary Boston & the North End", "img": "oldnorth",
  "summary": "Walk the Freedom Trail, eat your way through Little Italy and end with oysters at America's oldest restaurant.",
  "slots": [
   ("Morning", "Start at Boston Common and join a small-group Freedom Trail tour. In two and a half hours you will see the State House, the Granary Burying Ground, the Old State House, the Boston Massacre site and Faneuil Hall, with a guide who brings the 1770s to life.",
    [("Freedom Trail History Small Group Walking Tour", "/tours/Boston/Explore-Revolutionary-Boston-Freedom-Trail-History-Tour/d678-66111P3")], []),
   ("Lunch", "Follow the red line into the North End, Boston's Little Italy, for lunch.", [],
    [("Pizzeria Regina", "North End", "Brick-oven pizza on Thacher Street since 1926"), ("Giacomo's", "North End", "Tiny, beloved and famous for its pasta. Expect a line.")]),
   ("Afternoon", "Continue on the trail to the Paul Revere House and Old North Church, then walk across the bridge to Charlestown to board the USS Constitution. Take the ferry back downtown for a great view of the skyline. Pick up a cannoli on the way and choose your side in the Mike's vs. Modern debate.", [],
    [("Mike's Pastry or Modern Pastry", "Hanover Street", "The great cannoli rivalry"), ("Caffe Vittoria", "Hanover Street", "Espresso in an old-world cafe")]),
   ("Evening", "Dinner where Bostonians have eaten oysters for two centuries, or at the North End's favorite raw bar.", [],
    [("Union Oyster House", "Near Faneuil Hall", "America's oldest continuously operating restaurant, since 1826"), ("Neptune Oyster", "North End", "Small, buzzy and known for its hot buttered lobster roll")]),
  ]},
 {"n": 2, "plans": "2 3 5", "title": "Beacon Hill, the Back Bay & the Harbor", "img": "acorn",
  "summary": "Gas lamps and brownstones in the morning, a duck boat in the afternoon and a sunset cruise to finish.",
  "slots": [
   ("Morning", "Wander the cobblestone lanes of Beacon Hill (do not miss Acorn Street), then cross into the Public Garden to see the Make Way for Ducklings statues and, in season, ride the Swan Boats.", [],
    [("The Paramount", "Charles Street, Beacon Hill", "A neighborhood breakfast and brunch institution"), ("Tatte Bakery", "Charles Street and around town", "Pastries and coffee in a bright, busy cafe")]),
   ("Midday", "Hop on a duck boat for the city's most famous tour. It rolls past the landmarks, then drives straight into the Charles River.",
    [("Boston Duck Boat Sightseeing Tour", "/tours/Boston/Boston-Duck-Boat-Sightseeing-City-Tour-with-Cruise/d678-3037DUCK")], []),
   ("Afternoon", "Stroll Newbury Street's shops and cafes, then see Copley Square: Trinity Church and the Boston Public Library, whose courtyard is one of the city's hidden gems. For a bird's-eye view, head up to View Boston at the top of the Prudential Center.", [],
    [("Saltie Girl", "Back Bay", "Seafood and an enormous tinned-fish menu"), ("Atlantic Fish Co.", "Boylston Street", "A classic Back Bay seafood room")]),
   ("Evening", "Take a harbor sunset cruise from the waterfront, then have dinner in the Seaport.",
    [("Boston Harbor Sunset Cruise", "/tours/Boston/Northern-Lights-Sunset-Cruise/d678-5985P4")],
    [("Row 34", "Fort Point, Seaport", "Oysters and local beer in a converted warehouse"), ("Legal Harborside", "Seaport", "Three floors of seafood with harbor views")]),
  ]},
 {"n": 3, "plans": "3 5", "title": "Cambridge & Fenway", "img": "fenway",
  "summary": "America's oldest university in the morning and America's oldest ballpark in the afternoon.",
  "slots": [
   ("Morning", "Ride the Red Line to Harvard Square and take a student-led tour of Harvard Yard, then browse the bookstores and cafes around the square. If you have time, walk down Massachusetts Avenue to see MIT.",
    [("Harvard University Campus Guided Walking Tour", "/tours/Boston/Harvard-Campus-Walking-Tour/d678-5950P2")],
    [("Alden & Harlow", "Harvard Square", "Creative small plates in a basement dining room")]),
   ("Afternoon", "Head back across the river to Fenway Park. The tour takes you onto the field level and up on top of the Green Monster.",
    [("Tour of Historic Fenway Park", "/tours/Boston/Tour-of-Historic-Fenway-Park-Americas-Most-Beloved-Ballpark/d678-43406P1")], []),
   ("Evening", "In season, stay for a Red Sox game. Otherwise, catch the Celtics or Bruins at TD Garden, or grab a burger near the park.",
    [("Boston Celtics Game at TD Garden", "/tours/Boston/Boston-Celtics-Basketball-Game-at-TD-Garden/d678-5576124P94"), ("Boston Bruins Game at TD Garden", "/tours/Boston/Boston-Bruins-Ice-Hockey-Game-at-TD-Garden/d678-5576124P109")],
    [("Bleacher Bar", "Lansdowne Street", "A bar built into Fenway's outfield wall, with a window onto the field"), ("Tasty Burger", "Fenway", "A casual local burger favorite")]),
  ]},
 {"n": 4, "plans": "5", "title": "A Taste of Boston", "img": "mikes",
  "summary": "A food tour, a tea party and a night out in the South End, the city's best dining neighborhood.",
  "slots": [
   ("Morning", "Join a food and history tour that combines tastings with the stories of the North End, the Freedom Trail and Beacon Hill.",
    [("Food and History: North End, Freedom Trail and Beacon Hill", "/tours/Boston/From-Food-to-Freedom-Trail-Walking-Tour/d678-5713P108")], []),
   ("Afternoon", "Throw tea into the harbor yourself at the Boston Tea Party Ships & Museum, then wander the Rose Kennedy Greenway or browse the stalls of the Boston Public Market.",
    [("Boston Tea Party Ships & Museum", "/tours/Boston/Admission-to-Boston-Tea-Party-Ships-and-Museum/d678-5650TEA")], []),
   ("Evening", "Have dinner in the South End, Boston's restaurant row, or try dim sum and dumplings in Chinatown. Finish with a Boston cream pie where it was invented.", [],
    [("Toro", "South End", "Lively Spanish tapas"), ("Myers + Chang", "South End", "Playful Asian small plates"), ("Gourmet Dumpling House", "Chinatown", "Soup dumplings and scallion pancakes"), ("Omni Parker House", "Downtown", "Birthplace of the Boston cream pie and Parker House rolls")]),
  ]},
 {"n": 5, "plans": "5", "title": "Day Trip: Salem, Concord or Plymouth", "img": "salem",
  "summary": "Get out of the city for the day. Choose witches and sea captains, the shot heard round the world, or the Pilgrims.",
  "slots": [
   ("Option 1: Salem", "Take the ferry to Salem and explore the witch trials story, the Peabody Essex Museum and the House of the Seven Gables. October is magical, and very busy.",
    [("Salem High-Speed Ferry from Boston", "/tours/Boston/Salem-High-Speed-Ferry/d678-3283SALEM")],
    [("Turner's Seafood at Lyceum Hall", "Salem", "Seafood in a historic hall where Alexander Graham Bell once lectured")]),
   ("Option 2: Lexington & Concord", "Stand on Lexington Green and Concord's Old North Bridge, where the Revolution began on April 19, 1775, then visit Walden Pond and Louisa May Alcott's Orchard House.",
    [("Private Day Trip to Lexington and Concord", "/tours/Boston/Private-Day-Trip-to-Lexington-and-Concord-from-Boston/d678-400049P5")], []),
   ("Option 3: Plymouth", "Board Mayflower II, visit Plimoth Patuxet Museums and see Plymouth Rock, with a stop in Quincy, home of two presidents, on the way.",
    [("Plymouth Day Trip with Quincy, Plimoth Patuxet and Mayflower II", "/tours/Boston/Full-Day-Plymouth-and-Cape-Cod-Tour-from-Boston/d678-5491P4")], []),
   ("Farewell evening", "Back in Boston, toast your trip with a classic Italian dinner in the North End.", [],
    [("Mamma Maria", "North Square, North End", "Upscale Italian in a townhouse facing the Paul Revere House")]),
  ]},
]

SEASONAL = [
 ("Spring through fall", "Swap in a whale watch on Day 2 or Day 4. Boats sail to Stellwagen Bank from the downtown waterfront.", ("Boston Whale Watching Cruise", "/tours/Boston/Boston-Whale-Watching-Cruise/d678-3283BWW")),
 ("October", "Salem's Haunted Happenings and the Head of the Charles Regatta. Book early.", None),
 ("Evenings", "Add a ghost tour by trolley through Boston's old burying grounds.", ("Ghosts & Gravestones Trolley Tour", "/tours/Boston/Boston-Ghosts-and-Gravestones-Tour/d678-5046BOS_GG")),
 ("Late September to mid-October", "Trade the Day 5 trip for a fall foliage day in New Hampshire's White Mountains.", ("New Hampshire Fall Foliage Day Trip", "/tours/Boston/Fall-foliage-tour-in-New-Hampshire/d678-66192P4")),
]
