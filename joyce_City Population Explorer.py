import json
import csv


print("=" * 58)
print("         WORLD CITY POPULATION EXPLORER")
print("=" * 58)

# ── STEP 1 — CREATE THE DATA FILE ────────────────────────────
# In real AI work, you'd download this. We generate it here.
cities_data = [
    {"city": "Tokyo",        "country": "Japan",         "continent": "Asia",    "population": 13960000},
    {"city": "Delhi",        "country": "India",         "continent": "Asia",    "population": 11034555},
    {"city": "Shanghai",     "country": "China",         "continent": "Asia",    "population": 24183300},
    {"city": "Mumbai",       "country": "India",         "continent": "Asia",    "population": 12442373},
    {"city": "Beijing",      "country": "China",         "continent": "Asia",    "population": 21542000},
    {"city": "Dhaka",        "country": "Bangladesh",    "continent": "Asia",    "population": 8906039},
    {"city": "Karachi",      "country": "Pakistan",      "continent": "Asia",    "population": 14910352},
    {"city": "Osaka",        "country": "Japan",         "continent": "Asia",    "population": 2691185},
    {"city": "New York",     "country": "USA",           "continent": "America", "population": 8336817},
    {"city": "São Paulo",    "country": "Brazil",        "continent": "America", "population": 12325232},
    {"city": "Mexico City",  "country": "Mexico",        "continent": "America", "population": 9209944},
    {"city": "Los Angeles",  "country": "USA",           "continent": "America", "population": 3979576},
    {"city": "Buenos Aires", "country": "Argentina",     "continent": "America", "population": 3075646},
    {"city": "Chicago",      "country": "USA",           "continent": "America", "population": 2693976},
    {"city": "Lagos",        "country": "Nigeria",       "continent": "Africa",  "population": 14862111},
    {"city": "Kinshasa",     "country": "DR Congo",      "continent": "Africa",  "population": 14342439},
    {"city": "Cairo",        "country": "Egypt",         "continent": "Africa",  "population": 10107125},
    {"city": "Johannesburg", "country": "South Africa",  "continent": "Africa",  "population": 5635127},
    {"city": "Nairobi",      "country": "Kenya",         "continent": "Africa",  "population": 4397073},
    {"city": "Abuja",        "country": "Nigeria",       "continent": "Africa",  "population": 3464123},
    {"city": "London",       "country": "UK",            "continent": "Europe",  "population": 9002488},
    {"city": "Moscow",       "country": "Russia",        "continent": "Europe",  "population": 12506468},
    {"city": "Paris",        "country": "France",        "continent": "Europe",  "population": 2161000},
    {"city": "Berlin",       "country": "Germany",       "continent": "Europe",  "population": 3669491},
    {"city": "Madrid",       "country": "Spain",         "continent": "Europe",  "population": 3305408},
    {"city": "Rome",         "country": "Italy",         "continent": "Europe",  "population": 2844552},
    {"city": "Sydney",       "country": "Australia",     "continent": "Oceania", "population": 5312000},
    {"city": "Melbourne",    "country": "Australia",     "continent": "Oceania", "population": 5078193},
    {"city": "Brisbane",     "country": "Australia",     "continent": "Oceania", "population": 2560700},
    {"city": "Auckland",     "country": "New Zealand",   "continent": "Oceania", "population": 1695200},
]

# ── STEP 2 — WRITE TO JSON FILE ──────────────────────────────
# The indent parameter in Python's json.dump() (and json.dumps()) is used to pretty-print JSON data by adding line breaks and spaces.

json_filename = "cities.json"
with open(json_filename, "w") as f:
    json.dump(cities_data, f, indent=2)
print(f"\n💾 Step 1: Written {len(cities_data)} cities to '{json_filename}'")


# ── STEP 3 — READ BACK FROM JSON ─────────────────────────────
with open(json_filename, "r") as f:
    cities = json.load(f)
print(f"📂 Step 2: Loaded {len(cities)} cities from '{json_filename}'")

# ── STEP 4 — EXPLORE THE DATA ────────────────────────────────
print(f"\n📋 SAMPLE RECORD:")
print(f"   {json.dumps(cities[0], indent=6)}")

# ── STEP 5 — CONTINENT BREAKDOWN ─────────────────────────────
print("\n🌍 CITIES PER CONTINENT")
print("-" * 35)
continent_counts = {}
for c in cities:
    cont = c["continent"]
    continent_counts[cont] = continent_counts.get(cont, 0) + 1

for cont, count in sorted(continent_counts.items()):
    bar = "█" * count
    print(f"  {cont:<10}: {bar} ({count})")


# ── STEP 6 — FILTER BY CONTINENT ─────────────────────────────
chosen = "Asia"
print(f"\n🔍 FILTERING: Cities in {chosen}")
print("-" * 45)
asian_cities = [c for c in cities if c["continent"] == chosen]
asian_cities_sorted = sorted(asian_cities, key=lambda x: x["population"], reverse=True)
for c in asian_cities_sorted:
    pop_m = c["population"] / 1_000_000
    print(f"  {c['city']:<15} ({c['country']:<12}): {pop_m:.2f}M")
    
    
# ── STEP 7 — GLOBAL TOP 10 ───────────────────────────────────
print("\n🏆 TOP 10 MOST POPULOUS CITIES (Global)")
print("-" * 50)
top10 = sorted(cities, key=lambda x: x["population"], reverse=True)[:10]
for rank, c in enumerate(top10, 1):
    pop_m = c["population"] / 1_000_000
    bar   = "█" * int(pop_m)
    print(f"  {rank:>2}. {c['city']:<16} {c['continent']:<10}: {bar} {pop_m:.1f}M")


# ── STEP 8 — CONTINENT POPULATION TOTALS ─────────────────────
print("\n📊 TOTAL POPULATION BY CONTINENT")
print("-" * 40)
cont_pop = {}
for c in cities:
    cont = c["continent"]
    cont_pop[cont] = cont_pop.get(cont, 0) + c["population"]

for cont, pop in sorted(cont_pop.items(), key=lambda x: -x[1]):
    pop_m = pop / 1_000_000
    bar   = "█" * int(pop_m / 10)
    print(f"  {cont:<10}: {bar} {pop_m:.1f}M")
    
# ── STEP 9 — WRITE TOP 10 TO CSV ─────────────────────────────
csv_filename = "top10_cities.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["rank", "city", "country", "continent", "population"])
    writer.writeheader()
    for rank, c in enumerate(top10, 1):
        writer.writerow({
            "rank": rank,
            "city": c["city"],
            "country": c["country"],
            "continent": c["continent"],
            "population": c["population"]
        })
print(f"\n💾 Step 3: Top 10 exported to '{csv_filename}'")


# ── VERIFY CSV ───────────────────────────────────────────────
print(f"\n📄 Verifying CSV contents:")
with open(csv_filename, "r") as f:
    for i, line in enumerate(f):
        print(f"  {line.strip()}")
        


# ── SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 58)
most_pop_city = max(cities, key=lambda x: x["population"])
least_pop_city = min(cities, key=lambda x: x["population"])
print(f"  Most populous  : {most_pop_city['city']} ({most_pop_city['population']:,})")
print(f"  Least populous : {least_pop_city['city']} ({least_pop_city['population']:,})")
print(f"  Total cities   : {len(cities)}")
print(f"  Files created  : {json_filename}, {csv_filename}")
print("=" * 58)

print("\n💡 CHALLENGE: Try these...")
print("  1. Find all cities with population > 10 million.")
print("  2. Which country has the most cities in this dataset?")
print("  3. Add 3 more cities of your choice to cities.json and re-run.")
print()