favorite_places ={
    "grievink": ["dinxperlo", "lintelo"],
    "rutgers": ["de heurne"],
    "veerbeek": ["hoorn"],
}

for name, places in favorite_places.items():
    print(f"\nDe familie {name.title()} woont in:")
    for place in places:
        print(f"\t{place.title()}")
