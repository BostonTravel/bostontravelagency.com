# Where to Stay guide. Tiers: Luxury, Classic, Value. KAYAK links added once approved (KAYAK_LINK in build.py).
STAY_INTRO = [
 "Where you stay shapes your whole Boston trip. The city is small enough to walk, but each neighborhood has its own personality, from the brownstones of the Back Bay to the cobblestones of the North End and the glass towers of the Seaport.",
 "Here is our neighborhood-by-neighborhood guide, with hotels we like at three levels: Luxury, Classic and Value. Boston hotel prices swing a lot with the season. Expect the highest rates in September and October, around graduations in May, and during big events like the Marathon in April.",
]

TIERS = [
 ("Luxury", "Five-star service, standout rooms and the best locations. Often $600 or more a night in high season."),
 ("Classic", "Comfortable, well-located hotels with character. Typically $300 to $600 a night."),
 ("Value", "Smart, simpler stays that save money for the rest of the trip. Often under $300 a night."),
]

PICKER = [
 ("First visit to Boston", "Back Bay"),
 ("History and the Freedom Trail", "North End & Waterfront"),
 ("Romance and old-world charm", "Beacon Hill & Downtown"),
 ("Modern hotels and harbor views", "Seaport"),
 ("Harvard, MIT or a college visit", "Cambridge"),
 ("Red Sox games and concerts", "Fenway & Kenmore"),
]

HOODS = [
 {"name": "Back Bay", "slug": "back-bay", "img": "backbay",
  "summary": "Victorian brownstones, Newbury Street shopping and Copley Square. Central, beautiful and easy to walk from, which makes it our top pick for first-time visitors.",
  "good": "Walkable to the Public Garden, the Charles River Esplanade and the Prudential Center. The Green Line and Back Bay Station connect you to the rest of the city.",
  "hotels": [
   ("Luxury", "Mandarin Oriental, Boston", "Polished service and a full spa, connected to the Prudential Center shops."),
   ("Luxury", "Four Seasons One Dalton Street", "Sleek rooms with skyline views in one of the city's tallest towers."),
   ("Classic", "Fairmont Copley Plaza", "A grand 1912 landmark facing Copley Square and Trinity Church."),
   ("Classic", "The Lenox Hotel", "A family-owned Boston favorite steps from the Marathon finish line."),
  ]},
 {"name": "North End & Waterfront", "slug": "north-end-waterfront", "img": "rowes",
  "summary": "Stay in the middle of Boston's history and its best Italian food. You can walk to Faneuil Hall, the Paul Revere House and the harbor in minutes.",
  "good": "The North End itself has few hotels, so most options sit along the waterfront a short walk away. Great for Freedom Trail days and harbor cruises.",
  "hotels": [
   ("Luxury", "Boston Harbor Hotel", "The famous arch at Rowes Wharf, with harbor views and water taxis at the door."),
   ("Classic", "Battery Wharf Hotel", "A quiet waterfront hotel on the edge of the North End."),
   ("Classic", "Boston Marriott Long Wharf", "Right next to the Aquarium and the harbor cruise docks."),
   ("Value", "citizenM Boston North Station", "Compact, stylish rooms by TD Garden, a short walk to the North End."),
  ]},
 {"name": "Beacon Hill & Downtown", "slug": "beacon-hill-downtown", "img": "acorn",
  "summary": "Gas lamps, brick sidewalks and the Public Garden on Beacon Hill, with the historic heart of downtown just beyond. Charming, central and full of character.",
  "good": "Steps from Boston Common, the State House and the start of the Freedom Trail. The Theater District is close by for evenings out.",
  "hotels": [
   ("Luxury", "Four Seasons Hotel Boston", "A longtime favorite overlooking the Public Garden."),
   ("Classic", "Omni Parker House", "Operating since 1855 and the birthplace of the Boston cream pie."),
   ("Classic", "The Liberty", "A dramatic hotel inside the former Charles Street Jail."),
   ("Value", "Moxy Boston Downtown", "A playful, budget-friendly hotel in the Theater District."),
  ]},
 {"name": "Seaport", "slug": "seaport", "img": "skyline",
  "summary": "Boston's newest neighborhood, built on old wharves along the harbor. Modern hotels, rooftop bars and some of the city's best seafood restaurants.",
  "good": "Close to the convention center and the airport, with water views everywhere. It is a bit of a walk to the historic sites, but the Silver Line and water taxis help.",
  "hotels": [
   ("Classic", "Omni Boston Hotel at the Seaport", "A big, modern hotel with a rooftop bar and pool."),
   ("Classic", "The Envoy Hotel", "A boutique hotel known for its harbor-view rooftop bar."),
   ("Value", "YOTEL Boston", "Clever, compact cabins in the heart of the Seaport."),
  ]},
 {"name": "Cambridge", "slug": "cambridge", "img": "harvard",
  "summary": "Across the river, Cambridge is home to Harvard and MIT, with bookstores, cafes and a lively college-town feel. Often a little less expensive than downtown Boston.",
  "good": "The Red Line takes you into Boston in about 10 to 15 minutes. Ideal for college visits and a slightly slower pace.",
  "hotels": [
   ("Classic", "The Charles Hotel", "The classic Harvard Square stay, right on the Charles River."),
   ("Classic", "Hotel Veritas", "A small, intimate boutique hotel near Harvard Yard."),
  ]},
 {"name": "Fenway & Kenmore", "slug": "fenway-kenmore", "img": "fenway",
  "summary": "Stay in the shadow of the Green Monster. Fenway is lively on game nights and close to the Museum of Fine Arts and the Isabella Stewart Gardner Museum.",
  "good": "Kenmore Square has a Green Line stop for quick trips downtown. Prices can jump on game and concert nights, so book early.",
  "hotels": [
   ("Classic", "Hotel Commonwealth", "A comfortable favorite in Kenmore Square, steps from Fenway Park."),
   ("Classic", "The Verb Hotel", "A retro, rock-and-roll themed hotel across from the ballpark."),
   ("Value", "Hotel Buckminster", "A historic, budget-friendly hotel right in Kenmore Square."),
  ]},
]

STAY_TIPS = [
 "Book early for September, October and graduation weekends in May, when rates climb fast.",
 "You probably do not need a car. Most hotels charge $50 or more a night for parking, and the city is easy to walk.",
 "Staying near a T stop (subway station) makes day trips and late nights much easier.",
 "For families, ask about rooms with two queen beds or suites. Many older Boston hotels have small rooms.",
]
