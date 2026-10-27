"""Hand-compiled reference tables: franchise names/locations and venue attributes.

Venue facts (surface history, roof, shape, MLB co-tenancy, approximate football
capacity) are compiled from public stadium histories. Capacities are approximate.
"""

# ---------------------------------------------------------------- franchises
# franchise code -> list of (first_season, last_season, display name, city)
FRANCHISES = {
    "ARI": [(1920, 1921, "Racine Cardinals", "Chicago, IL"), (1922, 1959, "Chicago Cardinals", "Chicago, IL"),
            (1960, 1987, "St. Louis Cardinals", "St. Louis, MO"), (1988, 1993, "Phoenix Cardinals", "Tempe, AZ"),
            (1994, 2099, "Arizona Cardinals", "Glendale/Tempe, AZ")],
    "ATL": [(1966, 2099, "Atlanta Falcons", "Atlanta, GA")],
    "BAL": [(1996, 2099, "Baltimore Ravens", "Baltimore, MD")],
    "BUF": [(1960, 2099, "Buffalo Bills", "Buffalo/Orchard Park, NY")],
    "CAR": [(1995, 2099, "Carolina Panthers", "Charlotte, NC")],
    "CHI": [(1920, 1920, "Decatur Staleys", "Decatur, IL"), (1921, 1921, "Chicago Staleys", "Chicago, IL"),
            (1922, 2099, "Chicago Bears", "Chicago, IL")],
    "CIN": [(1968, 2099, "Cincinnati Bengals", "Cincinnati, OH")],
    "CLE": [(1946, 2099, "Cleveland Browns", "Cleveland, OH")],
    "DAL": [(1960, 2099, "Dallas Cowboys", "Dallas/Irving/Arlington, TX")],
    "DEN": [(1960, 2099, "Denver Broncos", "Denver, CO")],
    "DET": [(1930, 1933, "Portsmouth Spartans", "Portsmouth, OH"), (1934, 2099, "Detroit Lions", "Detroit/Pontiac, MI")],
    "GB":  [(1921, 2099, "Green Bay Packers", "Green Bay, WI")],
    "HOU": [(2002, 2099, "Houston Texans", "Houston, TX")],
    "IND": [(1953, 1983, "Baltimore Colts", "Baltimore, MD"), (1984, 2099, "Indianapolis Colts", "Indianapolis, IN")],
    "JAX": [(1995, 2099, "Jacksonville Jaguars", "Jacksonville, FL")],
    "KC":  [(1960, 1962, "Dallas Texans", "Dallas, TX"), (1963, 2099, "Kansas City Chiefs", "Kansas City, MO")],
    "LV":  [(1960, 1981, "Oakland Raiders", "Oakland, CA"), (1982, 1994, "Los Angeles Raiders", "Los Angeles, CA"),
            (1995, 2019, "Oakland Raiders", "Oakland, CA"), (2020, 2099, "Las Vegas Raiders", "Paradise, NV")],
    "LAC": [(1960, 1960, "Los Angeles Chargers", "Los Angeles, CA"), (1961, 2016, "San Diego Chargers", "San Diego, CA"),
            (2017, 2099, "Los Angeles Chargers", "Carson/Inglewood, CA")],
    "LAR": [(1936, 1945, "Cleveland Rams", "Cleveland, OH"), (1946, 1994, "Los Angeles Rams", "Los Angeles/Anaheim, CA"),
            (1995, 2015, "St. Louis Rams", "St. Louis, MO"), (2016, 2099, "Los Angeles Rams", "Los Angeles/Inglewood, CA")],
    "MIA": [(1966, 2099, "Miami Dolphins", "Miami/Miami Gardens, FL")],
    "MIN": [(1961, 2099, "Minnesota Vikings", "Bloomington/Minneapolis, MN")],
    "NE":  [(1960, 1970, "Boston Patriots", "Boston, MA"), (1971, 2099, "New England Patriots", "Foxborough, MA")],
    "NO":  [(1967, 2099, "New Orleans Saints", "New Orleans, LA")],
    "NYG": [(1925, 2099, "New York Giants", "New York, NY / E. Rutherford, NJ")],
    "NYJ": [(1960, 1962, "New York Titans", "New York, NY"), (1963, 2099, "New York Jets", "New York, NY / E. Rutherford, NJ")],
    "PHI": [(1933, 1942, "Philadelphia Eagles", "Philadelphia, PA"), (1943, 1943, "Phil-Pitt Steagles", "Philadelphia/Pittsburgh, PA"),
            (1944, 2099, "Philadelphia Eagles", "Philadelphia, PA")],
    "PIT": [(1933, 1939, "Pittsburgh Pirates", "Pittsburgh, PA"), (1940, 2099, "Pittsburgh Steelers", "Pittsburgh, PA")],
    "SF":  [(1946, 2099, "San Francisco 49ers", "San Francisco/Santa Clara, CA")],
    "SEA": [(1976, 2099, "Seattle Seahawks", "Seattle, WA")],
    "TB":  [(1976, 2099, "Tampa Bay Buccaneers", "Tampa, FL")],
    "TEN": [(1960, 1996, "Houston Oilers", "Houston, TX"), (1997, 1998, "Tennessee Oilers", "Memphis/Nashville, TN"),
            (1999, 2099, "Tennessee Titans", "Nashville, TN")],
    "WAS": [(1932, 1932, "Boston Braves", "Boston, MA"), (1933, 1936, "Boston Redskins", "Boston, MA"),
            (1937, 2019, "Washington Redskins", "Washington, DC / Landover, MD"),
            (2020, 2021, "Washington Football Team", "Landover, MD"), (2022, 2099, "Washington Commanders", "Landover, MD")],
}
# Pittsburgh 1944 merged with the Cardinals as "Card-Pitt" (538 code CRP)

DEFUNCT = {
    "AKR": "Akron Pros", "CBD": "Canton Bulldogs", "BFF": "Buffalo All-Americans/Bisons", "DAY": "Dayton Triangles",
    "HAM": "Hammond Pros", "RII": "Rock Island Independents", "RCH": "Rochester Jeffersons", "COL": "Columbus Panhandles",
    "CTI": "Cleveland Tigers", "MUN": "Muncie Flyers", "CHT": "Chicago Tigers", "DHR": "Detroit Heralds",
    "TON": "Tonawanda Kardex", "ECG": "Evansville Crimson Giants", "LOU": "Louisville Brecks/Colonels",
    "MNN": "Minneapolis Marines/Red Jackets", "SEN": "Washington Senators", "DTI": "Detroit Tigers", "CCL": "Cincinnati Celts",
    "NG1": "New York Giants (1921)", "OOR": "Oorang Indians", "MIL": "Milwaukee Badgers", "TOL": "Toledo Maroons",
    "RAC": "Racine Legion/Tornadoes", "CIB": "Cleveland Indians/Bulldogs", "DUL": "Duluth Kelleys/Eskimos",
    "SLA": "St. Louis All-Stars", "KEN": "Kenosha Maroons", "FYJ": "Frankford Yellow Jackets", "KCB": "Kansas City Blues/Cowboys",
    "DPN": "Detroit Panthers", "PRV": "Providence Steam Roller", "PTB": "Pottsville Maroons", "LAB": "Los Angeles Buccaneers",
    "BRL": "Brooklyn Lions", "HRT": "Hartford Blues", "NYA": "New York Yankees (1927-28)", "DWL": "Detroit Wolverines",
    "SIS": "Staten Island Stapletons", "TOR": "Orange/Newark Tornadoes", "CLI": "Cleveland Indians (1931)",
    "BKN": "Brooklyn Dodgers/Tigers", "RED": "Cincinnati Reds", "GUN": "St. Louis Gunners", "STG": "Phil-Pitt Steagles",
    "BYK": "Boston Yanks", "CRP": "Card-Pitt", "BBA": "Buffalo Bills (AAFC)", "BDA": "Brooklyn Dodgers (AAFC)",
    "MSA": "Miami Seahawks (AAFC)", "CRA": "Chicago Rockets/Hornets (AAFC)", "NAA": "New York Yankees (AAFC)",
    "LDA": "Los Angeles Dons (AAFC)", "BCL": "Baltimore Colts (1947-50)", "NYY": "New York Bulldogs/Yanks",
    "DTX": "Dallas Texans (1952)",
}

AFL_TEAMS = {"BUF", "DEN", "TEN", "KC", "LAC", "NE", "NYJ", "LV", "MIA", "CIN"}
AAFC_TEAMS = {"BBA", "BDA", "MSA", "CRA", "NAA", "LDA", "BCL", "CLE", "SF"}


def team_name(fr, season):
    for a, b, name, city in FRANCHISES.get(fr, []):
        if a <= season <= b:
            return name, city
    if fr in DEFUNCT:
        return DEFUNCT[fr], ""
    return fr, ""


# ---------------------------------------------------------------- venues
# shape: FB = football-specific stadium, MP = multi-purpose / cookie-cutter,
#        BB = baseball park used for football, CU = college/municipal/soccer, INTL = international/neutral
# roof: outdoors | dome | retractable | partial
# surface: list of (first_season, last_season, 'grass'|'artificial'|'hybrid')
# mlb: (team, first_season, last_season) for MLB co-tenancy
V = {}
def venue(vid, name, city, shape, roof, cap, surface, mlb=None, note=""):
    V[vid] = dict(id=vid, name=name, city=city, shape=shape, roof=roof, cap=cap, surface=surface, mlb=mlb, note=note)

G = lambda a=1900, b=2099: [(a, b, "grass")]
A = lambda a=1900, b=2099: [(a, b, "artificial")]

venue("ATLFC", "Atlanta-Fulton County Stadium", "Atlanta, GA", "MP", "outdoors", 59000, G(), ("Braves", 1966, 1996), "Circular cookie-cutter")
venue("BALBOA", "Balboa Stadium", "San Diego, CA", "CU", "outdoors", 34000, G())
venue("CLEMUNI", "Cleveland Municipal Stadium", "Cleveland, OH", "MP", "outdoors", 80000, G(), ("Indians", 1932, 1993))
venue("BUSCH", "Busch Memorial Stadium", "St. Louis, MO", "MP", "outdoors", 51000, [(1966, 1969, "grass"), (1970, 1995, "artificial")], ("Cardinals", 1966, 2005), "Circular cookie-cutter")
venue("FENWAY", "Fenway Park", "Boston, MA", "BB", "outdoors", 38000, G(), ("Red Sox", 1912, 2099))
venue("FRANKLIN", "Franklin Field", "Philadelphia, PA", "CU", "outdoors", 60000, [(1900, 1968, "grass"), (1969, 2099, "artificial")])
venue("COTTON", "Cotton Bowl", "Dallas, TX", "CU", "outdoors", 75000, G())
venue("KEZAR", "Kezar Stadium", "San Francisco, CA", "CU", "outdoors", 59000, G())
venue("LACOL", "Los Angeles Memorial Coliseum", "Los Angeles, CA", "CU", "outdoors", 93000, G(), ("Dodgers", 1958, 1961), "College bowl")
venue("KCMUNI", "Kansas City Municipal Stadium", "Kansas City, MO", "BB", "outdoors", 47000, G(), ("A's/Royals", 1955, 1972))
venue("METSTAD", "Metropolitan Stadium", "Bloomington, MN", "BB", "outdoors", 48000, G(), ("Twins", 1961, 1981))
venue("BALMEM", "Memorial Stadium (Baltimore)", "Baltimore, MD", "MP", "outdoors", 60000, G(), ("Orioles", 1954, 1991), "Horseshoe")
venue("LAMBEAU", "Lambeau Field", "Green Bay, WI", "FB", "outdoors", 81000, [(1957, 2006, "grass"), (2007, 2099, "hybrid")], None, "Bowl")
venue("OAKCOL", "Oakland Coliseum", "Oakland, CA", "MP", "outdoors", 56000, G(), ("Athletics", 1968, 2024), "Sunken bowl; dirt infield during A's overlap")
venue("MILCO", "Milwaukee County Stadium", "Milwaukee, WI", "BB", "outdoors", 56000, G(), ("Braves/Brewers", 1953, 2000))
venue("MILEHIGH", "Mile High Stadium", "Denver, CO", "MP", "outdoors", 76000, G(), ("Rockies", 1993, 1994), "Horseshoe w/ movable stand")
venue("RICE", "Rice Stadium", "Houston, TX", "CU", "outdoors", 70000, G())
venue("SHEA", "Shea Stadium", "Queens, NY", "MP", "outdoors", 60000, G(), ("Mets", 1964, 2008))
venue("RFK", "RFK Memorial Stadium", "Washington, DC", "MP", "outdoors", 55000, G(), ("Senators", 1962, 1971), "Circular cookie-cutter")
venue("PITT", "Pitt Stadium", "Pittsburgh, PA", "CU", "outdoors", 56000, [(1900, 1969, "grass"), (1970, 2099, "artificial")])
venue("TIGERDET", "Tiger Stadium", "Detroit, MI", "BB", "outdoors", 54000, G(), ("Tigers", 1912, 1999))
venue("YANKEE", "Yankee Stadium", "Bronx, NY", "BB", "outdoors", 63000, G(), ("Yankees", 1923, 2008))
venue("WRIGLEY", "Wrigley Field", "Chicago, IL", "BB", "outdoors", 46000, G(), ("Cubs", 1916, 2099))
venue("WARMEM", "War Memorial Stadium", "Buffalo, NY", "CU", "outdoors", 46000, G(), None, "Municipal (minor-league baseball)")
venue("ORANGE", "Orange Bowl", "Miami, FL", "CU", "outdoors", 75000, [(1900, 1969, "grass"), (1970, 1975, "artificial"), (1976, 2099, "grass")], None, "Horseshoe")
venue("TULANE", "Tulane Stadium", "New Orleans, LA", "CU", "outdoors", 81000, [(1900, 1970, "grass"), (1971, 2099, "artificial")])
venue("SDSTAD", "San Diego / Jack Murphy / Qualcomm Stadium", "San Diego, CA", "MP", "outdoors", 70000, G(), ("Padres", 1969, 2003), "Enclosed multi-purpose")
venue("ALUMNI", "Alumni Stadium", "Chestnut Hill, MA", "CU", "outdoors", 26000, G())
venue("NIPPERT", "Nippert Stadium", "Cincinnati, OH", "CU", "outdoors", 28000, G())
venue("ASTRO", "Houston Astrodome", "Houston, TX", "MP", "dome", 62000, A(), ("Astros", 1965, 1999), "First domed stadium")
venue("GRANT", "Grant Field", "Atlanta, GA", "CU", "outdoors", 58000, G())
venue("MEMMPLS", "Memorial Stadium (Minneapolis)", "Minneapolis, MN", "CU", "outdoors", 56000, G())
venue("RIVERFRONT", "Riverfront / Cinergy Field", "Cincinnati, OH", "MP", "outdoors", 60000, A(), ("Reds", 1970, 2002), "Circular cookie-cutter")
venue("HARVARD", "Harvard Stadium", "Boston, MA", "CU", "outdoors", 37000, G(), None, "Horseshoe")
venue("VET", "Veterans Stadium", "Philadelphia, PA", "MP", "outdoors", 65000, A(), ("Phillies", 1971, 2003), "Circular cookie-cutter")
venue("THREERIV", "Three Rivers Stadium", "Pittsburgh, PA", "MP", "outdoors", 59000, A(), ("Pirates", 1970, 2000), "Circular cookie-cutter")
venue("ARROWHEAD", "Arrowhead Stadium", "Kansas City, MO", "FB", "outdoors", 76000, [(1972, 1993, "artificial"), (1994, 2099, "grass")], None, "Bowl")
venue("CANDLE", "Candlestick Park", "San Francisco, CA", "MP", "outdoors", 70000, G(), ("Giants", 1960, 1999), "Baseball park enclosed for football")
venue("FOXBORO", "Foxboro / Schaefer / Sullivan Stadium", "Foxborough, MA", "FB", "outdoors", 61000, [(1971, 1990, "artificial"), (1991, 2099, "grass")], None, "Bowl")
venue("SOLDIER", "Soldier Field", "Chicago, IL", "FB", "outdoors", 61500, [(1971, 1987, "artificial"), (1988, 2099, "grass")], None, "Colonnade; rebuilt 2002-03")
venue("TEXAS", "Texas Stadium", "Irving, TX", "FB", "partial", 65000, A(), None, "Hole-in-roof partial dome")
venue("YALE", "Yale Bowl", "New Haven, CT", "CU", "outdoors", 70000, G())
venue("RICHWILSON", "Rich / Ralph Wilson / Highmark Stadium", "Orchard Park, NY", "FB", "outdoors", 71000, A(1973, 2025) + G(2026, 2099), None, "Bowl")
venue("CALMEM", "California Memorial Stadium", "Berkeley, CA", "CU", "outdoors", 63000, G())
venue("SILVER", "Pontiac Silverdome", "Pontiac, MI", "FB", "dome", 80000, A(), None, "Air-supported dome")
venue("GIANTS", "Giants Stadium", "E. Rutherford, NJ", "FB", "outdoors", 80000, [(1976, 1999, "artificial"), (2000, 2002, "grass"), (2003, 2099, "artificial")], None, "Bowl")
venue("SUPERDOME", "Louisiana / Caesars Superdome", "New Orleans, LA", "MP", "dome", 73000, A(), None, "Multi-purpose dome")
venue("KINGDOME", "Seattle Kingdome", "Seattle, WA", "MP", "dome", 66000, A(), ("Mariners", 1977, 1999), "Multi-purpose dome")
venue("TAMPA", "Tampa Stadium", "Tampa, FL", "FB", "outdoors", 74000, G(), None, "Bowl ('Big Sombrero')")
venue("ANAHEIM", "Anaheim Stadium", "Anaheim, CA", "MP", "outdoors", 69000, G(), ("Angels", 1966, 2099), "Baseball park enclosed for football")
venue("METRODOME", "Hubert H. Humphrey Metrodome", "Minneapolis, MN", "MP", "dome", 64000, A(), ("Twins", 1982, 2009), "Air-supported dome")
venue("RCADOME", "Hoosier / RCA Dome", "Indianapolis, IN", "FB", "dome", 57000, A(), None, "Air-supported dome")
venue("JOEROBBIE", "Joe Robbie / Hard Rock Stadium", "Miami Gardens, FL", "FB", "outdoors", 65000, G(), ("Marlins", 1993, 2011), "Football-first; MLB 1993-2011")
venue("SUNDEVIL", "Sun Devil Stadium", "Tempe, AZ", "CU", "outdoors", 73000, G())
venue("GADOME", "Georgia Dome", "Atlanta, GA", "FB", "dome", 71000, A(), None, "Cable-supported dome")
venue("UOPX", "State Farm / U. of Phoenix Stadium", "Glendale, AZ", "FB", "retractable", 63400, G(), None, "Roll-out grass tray")
venue("HUSKY", "Husky Stadium", "Seattle, WA", "CU", "outdoors", 72000, A())
venue("JAXMUNI", "Jacksonville Municipal / EverBank Stadium", "Jacksonville, FL", "FB", "outdoors", 67000, G())
venue("TWADOME", "Trans World / Edward Jones Dome", "St. Louis, MO", "FB", "dome", 66000, A())
venue("CLEMSON", "Memorial Stadium (Clemson)", "Clemson, SC", "CU", "outdoors", 81000, G())
venue("BOFA", "Bank of America Stadium", "Charlotte, NC", "FB", "outdoors", 74000, G(1996, 2020) + A(2021, 2099))
venue("FEDEX", "FedExField / Northwest Stadium", "Landover, MD", "FB", "outdoors", 67000, G())
venue("LIBERTY", "Liberty Bowl Memorial Stadium", "Memphis, TN", "CU", "outdoors", 62000, G())
venue("RJS", "Raymond James Stadium", "Tampa, FL", "FB", "outdoors", 65000, G())
venue("VANDY", "Vanderbilt Stadium", "Nashville, TN", "CU", "outdoors", 41000, [(1900, 1969, "grass"), (1970, 1998, "artificial"), (1999, 2099, "grass")])
venue("MTBANK", "M&T Bank Stadium", "Baltimore, MD", "FB", "outdoors", 71000, G())
venue("CLEBROWNS", "Cleveland Browns / Huntington Bank Field", "Cleveland, OH", "FB", "outdoors", 67000, G())
venue("NISSAN", "Nissan Stadium (Adelphia/LP Field)", "Nashville, TN", "FB", "outdoors", 69000, G())
venue("PAULBROWN", "Paul Brown / Paycor Stadium", "Cincinnati, OH", "FB", "outdoors", 65500, G())
venue("NEWMILE", "Empower Field at Mile High", "Denver, CO", "FB", "outdoors", 76000, G())
venue("HEINZ", "Heinz Field / Acrisure Stadium", "Pittsburgh, PA", "FB", "outdoors", 68400, G())
venue("CHAMPAIGN", "Memorial Stadium (Champaign)", "Champaign, IL", "CU", "outdoors", 70000, A())
venue("NRG", "Reliant / NRG Stadium", "Houston, TX", "FB", "retractable", 72000, G())
venue("FORD", "Ford Field", "Detroit, MI", "FB", "dome", 65000, A())
venue("LUMEN", "Lumen Field", "Seattle, WA", "FB", "outdoors", 68700, A(), None, "Open-air, partial canopy roof")
venue("GILLETTE", "Gillette Stadium", "Foxborough, MA", "FB", "outdoors", 65900, G(2002, 2005) + A(2006, 2099))
venue("LINC", "Lincoln Financial Field", "Philadelphia, PA", "FB", "outdoors", 69800, G())
venue("TIGERLSU", "Tiger Stadium (LSU)", "Baton Rouge, LA", "CU", "outdoors", 92000, G())
venue("ALAMO", "Alamodome", "San Antonio, TX", "MP", "dome", 65000, A())
venue("LUCAS", "Lucas Oil Stadium", "Indianapolis, IN", "FB", "retractable", 67000, A())
venue("ATT", "AT&T Stadium", "Arlington, TX", "FB", "retractable", 80000, A())
venue("METLIFE", "MetLife Stadium", "E. Rutherford, NJ", "FB", "outdoors", 82500, A())
venue("TCF", "TCF Bank Stadium", "Minneapolis, MN", "CU", "outdoors", 50800, A())
venue("LEVIS", "Levi's Stadium", "Santa Clara, CA", "FB", "outdoors", 68500, G())
venue("USBANK", "U.S. Bank Stadium", "Minneapolis, MN", "FB", "dome", 66700, A(), None, "Fixed translucent roof")
venue("STUBHUB", "StubHub Center / Dignity Health Sports Park", "Carson, CA", "CU", "outdoors", 27000, G(), None, "Soccer stadium")
venue("MBS", "Mercedes-Benz Stadium", "Atlanta, GA", "FB", "retractable", 71000, A())
venue("ALLEGIANT", "Allegiant Stadium", "Paradise, NV", "FB", "dome", 65000, G(), None, "Fixed roof; roll-in grass tray")
venue("SOFI", "SoFi Stadium", "Inglewood, CA", "FB", "dome", 70000, A(), None, "Fixed translucent canopy (indoor-outdoor)")
venue("ROGERS", "Rogers Centre", "Toronto, ON", "INTL", "retractable", 54000, A(), ("Blue Jays", 1989, 2099))
venue("INTL", "International / neutral venue", "", "INTL", "outdoors", None, G())

# spreadspoke stadium name (current naming) -> venue id ; used 1966-1998
SPREADSPOKE_MAP = {
    "Atlanta-Fulton County Stadium": "ATLFC", "Balboa Stadium": "BALBOA", "Cleveland Municipal Stadium": "CLEMUNI",
    "Busch Memorial Stadium": "BUSCH", "Fenway Park": "FENWAY", "Franklin Field": "FRANKLIN", "Cotton Bowl": "COTTON",
    "Kezar Stadium": "KEZAR", "Los Angeles Memorial Coliseum": "LACOL", "Kansas City Municipal Stadium": "KCMUNI",
    "Metropolitan Stadium": "METSTAD", "Memorial Stadium (Baltimore)": "BALMEM", "Lambeau Field": "LAMBEAU",
    "Oakland Coliseum": "OAKCOL", "Milwaukee County Stadium": "MILCO", "Mile High Stadium": "MILEHIGH",
    "Rice Stadium": "RICE", "Shea Stadium": "SHEA", "RFK Memorial Stadium": "RFK", "Pitt Stadium": "PITT",
    "Tiger Stadium": "TIGERDET", "Yankee Stadium": "YANKEE", "Wrigley Field": "WRIGLEY", "War Memorial Stadium": "WARMEM",
    "Orange Bowl": "ORANGE", "Tulane Stadium": "TULANE", "San Diego Stadium": "SDSTAD", "Qualcomm Stadium": "SDSTAD",
    "Alumni Stadium": "ALUMNI", "Nippert Stadium": "NIPPERT", "Houston Astrodome": "ASTRO", "Grant Field": "GRANT",
    "Memorial Stadium (Minneapolis)": "MEMMPLS", "Cinergy Field": "RIVERFRONT", "Harvard Stadium": "HARVARD",
    "Veterans Stadium": "VET", "Three Rivers Stadium": "THREERIV", "Arrowhead Stadium": "ARROWHEAD",
    "Candlestick Park": "CANDLE", "Foxboro Stadium": "FOXBORO", "Soldier Field": "SOLDIER", "Texas Stadium": "TEXAS",
    "Yale Bowl": "YALE", "Ralph Wilson Stadium": "RICHWILSON", "California Memorial Stadium": "CALMEM",
    "Pontiac Silverdome": "SILVER", "Giants Stadium": "GIANTS", "Louisiana Superdome": "SUPERDOME",
    "Seattle Kingdome": "KINGDOME", "Houlihan's Stadium": "TAMPA", "Anaheim Stadium": "ANAHEIM",
    "Hubert H. Humphrey Metrodome": "METRODOME", "RCA Dome": "RCADOME", "Sun Life Stadium": "JOEROBBIE",
    "Sun Devil Stadium": "SUNDEVIL", "Georgia Dome": "GADOME", "Husky Stadium": "HUSKY", "EverBank Field": "JAXMUNI",
    "Edward Jones Dome": "TWADOME", "Memorial Stadium (Clemson)": "CLEMSON", "Bank of America Stadium": "BOFA",
    "FedEx Field": "FEDEX", "Liberty Bowl Memorial Stadium": "LIBERTY", "Raymond James Stadium": "RJS",
    "Vanderbilt Stadium": "VANDY", "M&T Bank Stadium": "MTBANK", "Tiger Stadium (LSU)": "TIGERLSU",
}

# nflverse stadium_id -> venue id ; used 1999+
NFLVERSE_MAP = {
    "ATL00": "GADOME", "ATL97": "MBS", "BAL00": "MTBANK", "BOS00": "GILLETTE", "BOS99": "FOXBORO",
    "BRG00": "TIGERLSU", "BUF00": "RICHWILSON", "BUF01": "ROGERS", "CAR00": "BOFA", "CHI98": "SOLDIER",
    "CHI99": "CHAMPAIGN", "CIN00": "PAULBROWN", "CIN99": "RIVERFRONT", "CLE00": "CLEBROWNS", "DAL00": "ATT",
    "DAL99": "TEXAS", "DEN00": "NEWMILE", "DEN99": "MILEHIGH", "DET00": "FORD", "DET99": "SILVER",
    "GNB00": "LAMBEAU", "HOU00": "NRG", "IND00": "LUCAS", "IND99": "RCADOME", "JAX00": "JAXMUNI",
    "KAN00": "ARROWHEAD", "LAX01": "SOFI", "LAX97": "STUBHUB", "LAX99": "LACOL", "MIA00": "JOEROBBIE",
    "MIN00": "METRODOME", "MIN01": "USBANK", "MIN98": "TCF", "NAS00": "NISSAN", "NOR00": "SUPERDOME",
    "NYC00": "GIANTS", "NYC01": "METLIFE", "OAK00": "OAKCOL", "PHI00": "LINC", "PHI99": "VET",
    "PHO00": "UOPX", "PHO99": "SUNDEVIL", "PIT00": "HEINZ", "PIT99": "THREERIV", "SAN00": "ALAMO",
    "SDG00": "SDSTAD", "SEA00": "LUMEN", "SEA98": "KINGDOME", "SEA99": "HUSKY", "SFO00": "CANDLE",
    "SFO01": "LEVIS", "STL00": "TWADOME", "TAM00": "RJS", "VEG00": "ALLEGIANT", "WAS00": "FEDEX",
}

SHAPE_LABEL = {"FB": "Football-specific", "MP": "Multi-purpose / cookie-cutter", "BB": "Baseball park",
               "CU": "College / municipal / soccer", "INTL": "International / neutral", "": "Unknown (pre-1966)"}


def surface_for(vid, season):
    for a, b, s in V[vid]["surface"]:
        if a <= season <= b:
            return s
    return None
