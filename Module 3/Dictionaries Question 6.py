counties = {
    "Berekely County": "Moncks Corner",
    "Calhoun County": "St. Matthews",
    "Cherokee County": "Gaffney",
    "Clarendon County": "Manning",
    "Aiken County": "Aiken",
    "Anderson County": "Anderson"
}

counties_list = ["Berekely County", "Calhoun County", "Cherokee County",
                 "Clarendon County", "Aiken County", "Anderson County",
                 "Abbeville County", "Allendale County", "Barnwell County", "Dillon County"]

for county in counties_list:
    if county in counties:
        print(f"{county} is in our dictionary, and the capital/seat is {counties[county]}")
    else:
        print(f"{county} is not in our dictionary. We will add this county shortly. Thanks!")
