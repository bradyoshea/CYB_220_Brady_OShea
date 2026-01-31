berkeley = ["Goose Creek", "Hanahan", "Moncks Corner"]
calhoun = ["St. Matthews", "Gaston", "North"]
beaufort = ["Hilton Head", "Bluffton", "Port Royal"]
dorchester = ["North Charleston", "Summerville", "Ladson"]
anderson = ["Anderson", "Belton", "Williamston"]
sc_counties = {"Berkeley": berkeley, "Calhoun": calhoun, "Beaufort": beaufort, "Dorchester": dorchester, "Anderson": anderson}
for key, value in sc_counties.items():
    print(f"In {key}, the largest cities are {value[0]}, {value[1]}, and {value[2]}.")