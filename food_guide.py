# What to Eat in Boston. CLASSICS are timeless; TRENDING is dated and refreshed a few times a year.
# Each item: name, kicker, img (key in images.py), paras (HTML allowed), spots [(name, where, note)], tour (title, viator path) or None
EAT_INTRO = [
 "Boston isn't just lobster and chowder anymore, but the classics are classics for a reason. Here is what we tell friends and family they have to eat while they're in town, from North End cannoli to the North Shore roast beef sandwich locals argue about, plus a few of the places everyone is talking about right now.",
]
TRENDING_AS_OF = "Fall 2026"

CLASSICS = [
 {"slug": "cannoli", "name": "Cannoli in the North End", "kicker": "The great North End rivalry", "img": "mikes",
  "paras": [
   "No trip to Boston is complete without a cannoli, and you'll hear about the great North End rivalry before you even get there.",
   "<strong>Mike's Pastry</strong> on Hanover Street is the famous one. Look for the line out the door and the white boxes tied with string all over the neighborhood. It's lively, crowded and a classic Boston photo, so if you want the selfie with the box, Mike's is your place, and you'll love it.",
   "<strong>Modern Pastry</strong>, just across the street, is the one locals are more likely to name as their favorite. Its cannoli are filled to order, so the shells stay crisp. <strong>Bova's Bakery</strong> on Salem Street is the neighborhood's old-school standby, famous for being open around the clock and perfect for a late-night cannoli after dinner.",
   "Sadly, many of the old-school North End bakeries are gone. Locals still miss <strong>Maria's Pastry Shop</strong> on Cross Street, run for decades by Maria Merola until she retired in 2019, and many of us remember it as the freshest and most authentic of them all. The good news is you won't be disappointed by any of the ones still standing. A local might quietly steer you to Modern, but the best plan is to try a couple and pick a side.",
  ],
  "spots": [("Modern Pastry", "Hanover St., North End", "The locals' pick"), ("Mike's Pastry", "Hanover St., North End", "The famous one, and the photo"), ("Bova's Bakery", "Salem St., North End", "Late-night cannoli")],
  "tour": ("North End Food Tour: Pizza, Pasta and Pastries", "/tours/Boston/North-End-Boston-Food-Tour/d678-91367P3")},
 {"slug": "lobster-roll", "name": "A Lobster Roll", "kicker": "Hot and buttered, or cold with mayo?", "img": "lobster",
  "paras": [
   "Every New Englander has an opinion here. A Connecticut-style roll is warm lobster meat drenched in butter. A Maine-style roll is cold lobster tossed with a little mayo. Both come in a toasted, buttered split-top bun, and both are worth every penny.",
   "Our top three: <strong>Neptune Oyster</strong> in the North End, whose hot buttered roll is legendary and worth the wait for a seat; <strong>Row 34</strong> in Fort Point, a stylish oyster bar with a great roll either way; and <strong>Belle Isle Seafood</strong> in Winthrop, a no-frills seafood shack about ten minutes from Logan. It's the perfect first or last stop of your trip.",
  ],
  "spots": [("Neptune Oyster", "Salem St., North End", "Get it hot with butter"), ("Row 34", "Fort Point", "Oyster bar with a view of the scene"), ("Belle Isle Seafood", "Winthrop, near Logan", "Shack-style, huge portions")],
  "tour": ("Boston Harbor Sunset Cruise", "/tours/Boston/Northern-Lights-Sunset-Cruise/d678-5985P4")},
 {"slug": "roast-beef", "name": "North Shore Roast Beef, \"Three-Way\"", "kicker": "Order it like a local", "img": "sandcastle",
  "paras": [
   "A \"three-way\" is thin-sliced rare roast beef with James River BBQ sauce, mayo and white American cheese on a grilled onion roll. Just say \"large beef, three-way\" and you'll sound like you grew up here.",
   "The legend starts on Revere Beach. Kelly's opened in 1951 as a hot dog stand, and one night a wedding next door was canceled, leaving the owners with spare roast beefs. They sliced them thin and served them on grilled rolls the next day, and what was supposed to last the day sold out in an hour. Kelly's still claims to have invented the sandwich, and the North Shore has been arguing about who makes the best one ever since.",
   "The one locals line up for is <strong>The Modern Butcher</strong> in Danvers, which serves its roast beef only on Saturdays. Lines run down the street, and when it's sold out, that's it for the week.",
   "Our advice: you'll find a roast beef in Boston, but if you want the real thing, head north of the city. The easiest way is a trip to Revere Beach on the Blue Line. Grab a three-way at the original Kelly's on the boulevard, eat it on the seawall, and if you're here in late July, walk over to the <a href=\"/boston-events/#sand-sculpting\">International Sand Sculpting Festival</a>.",
  ],
  "spots": [("Kelly's Roast Beef", "Revere Beach Blvd., Revere", "The original, since 1951"), ("The Modern Butcher", "Maple St., Danvers", "Saturdays only")],
  "tour": None},
 {"slug": "chowder", "name": "New England Clam Chowder", "kicker": "Say it with us: chowdah", "img": "faneuil",
  "paras": [
   "Creamy, briny and full of clams and potatoes, real New England clam chowder is thick enough to stand a spoon in and comes with a pack of oyster crackers on the side. (Locals consider the tomato-based Manhattan version a mistake.)",
   "For history with your bowl, sit at the oyster bar at <strong>Union Oyster House</strong> near Faneuil Hall, which has been serving since 1826 and is often called the oldest restaurant in America.",
  ],
  "spots": [("Union Oyster House", "Union St., near Faneuil Hall", "Open since 1826")],
  "tour": ("Food and History: North End, Freedom Trail and Beacon Hill", "/tours/Boston/From-Food-to-Freedom-Trail-Walking-Tour/d678-5713P108")},
 {"slug": "fried-clams", "name": "Fried Whole-Belly Clams", "kicker": "A North Shore summer ritual", "img": "salem",
  "paras": [
   "Sweet, crunchy, a little messy and nothing like the clam strips you've had elsewhere. Whole-belly clams are the real thing, and the best are eaten at a picnic table near the water.",
   "<strong>Woodman's of Essex</strong>, about an hour north, says it fried the first clam back in 1916. Combine it with a day trip to Salem or Cape Ann.",
  ],
  "spots": [("Woodman's of Essex", "Essex", "Where the fried clam began")],
  "tour": ("Private Day Trip to Salem and Hammond Castle", "/tours/Boston/Private-Day-Trip-to-Salem-and-Hammond-Castle-from-Boston/d678-400049P15")},
 {"slug": "oysters", "name": "Local Oysters", "kicker": "Duxbury, Wellfleet and beyond", "img": "rowes",
  "paras": [
   "Cold New England water makes some of the best oysters in the world: crisp, salty and clean. Ask what's local that day and try a few side by side; oyster lovers can taste the difference between bays.",
   "Raw bars are everywhere, from Neptune Oyster in the North End to the Seaport waterfront in summer.",
  ],
  "spots": [("Neptune Oyster", "North End", ""), ("Row 34", "Fort Point", "")], "tour": None},
 {"slug": "boston-cream-pie", "name": "Boston Cream Pie", "kicker": "It's actually a cake", "img": "statehouse",
  "paras": [
   "Two layers of sponge cake, vanilla custard in the middle and chocolate glaze on top. It's the official dessert of Massachusetts, and yes, it's a cake.",
   "It was invented at the <strong>Omni Parker House</strong> hotel in the 1850s, and you can still order the original in its restaurant, a block from Boston Common on the Freedom Trail.",
  ],
  "spots": [("Omni Parker House", "School St., downtown", "Where it was invented")], "tour": None},
 {"slug": "pizza", "name": "North End and East Boston Pizza", "kicker": "Old-school pies", "img": "hanover",
  "paras": [
   "<strong>Regina Pizzeria</strong> on Thacher Street has been making thin, chewy, slightly charred pies in the North End since 1926. Expect a line and a small, loud, wonderful dining room.",
   "<strong>Santarpio's</strong> in East Boston, near the airport, is a local legend for its pizza and grilled sausage and lamb skewers. No frills, just great food.",
  ],
  "spots": [("Regina Pizzeria", "Thacher St., North End", "Since 1926"), ("Santarpio's", "Chelsea St., East Boston", "Get the lamb skewers too")], "tour": None},
 {"slug": "fenway-frank", "name": "A Fenway Frank", "kicker": "Best eaten under the Green Monster", "img": "fenway",
  "paras": [
   "Is it the best hot dog in the world? Maybe not. Is it the best hot dog you'll eat at the oldest ballpark in the major leagues on a summer night? Absolutely. Add a sausage with peppers and onions from a cart on Lansdowne Street on the way in.",
  ],
  "spots": [], "tour": ("Tour of Historic Fenway Park", "/tours/Boston/Tour-of-Historic-Fenway-Park-Americas-Most-Beloved-Ballpark/d678-43406P1")},
 {"slug": "local-lingo", "name": "A Frappe, a Fluffernutter and a Dunkin'", "kicker": "Speak the language", "img": "backbay",
  "paras": [
   "In Boston, a milkshake with ice cream is a <strong>frappe</strong>. Order a \"milkshake\" and you may get just milk and syrup.",
   "Marshmallow Fluff was invented in Somerville in 1917, and a <strong>Fluffernutter</strong> (Fluff and peanut butter on white bread) is a lunchbox classic for generations of New England kids.",
   "And you will notice the <strong>Dunkin'</strong> on every corner. Locals drink iced coffee all year, even in a snowstorm. Order a \"regular\" and you'll get cream and sugar.",
  ],
  "spots": [], "tour": None},
 {"slug": "baked-beans", "name": "Boston Baked Beans (Sort Of)", "kicker": "Why we're called Beantown", "img": "oldnorth",
  "paras": [
   "Here's a local secret: nobody in Boston goes out for baked beans. The dish, navy beans slow-baked for hours with molasses and salt pork, is the reason Boston got the nickname \"Beantown,\" back when the city was a hub of the molasses and rum trade.",
   "You'll find them on a few historic menus and on souvenir shelves, and they're good. Just don't be surprised when the locals look at you funny if you ask where to get the best ones. Grab a box of Boston Baked Beans candy instead.",
  ],
  "spots": [], "tour": None},
]

TRENDING = [
 {"name": "Maple & Ash", "where": "Seaport Blvd., Seaport", "what": "A splashy Chicago steakhouse known for its fire-roasted seafood towers and a dramatic, moody dining room."},
 {"name": "Mai", "where": "Seaport", "what": "A stylish French-Japanese spot with Labubus in the rafters. Built for photos, but the handrolls and wagyu steak frites hold up."},
 {"name": "Island Creek Raw Bar", "where": "Seaport, seasonal", "what": "The outdoor summer raw bar from the famous Duxbury oyster farm. Oysters, rosé and harbor breezes."},
 {"name": "Cisco Brewers Seaport", "where": "Seaport Blvd., April to October", "what": "Nantucket's beloved brewery runs a giant, dog-friendly beer garden with food trucks and cocktails."},
 {"name": "311 Omakase", "where": "South End", "what": "Boston's first Michelin-starred restaurant: an intimate 10-seat sushi counter. Book well ahead."},
]
