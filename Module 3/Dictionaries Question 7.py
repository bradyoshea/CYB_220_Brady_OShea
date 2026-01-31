berkeley = {"Goose Creek": 42_619, "Hanahan": 24_885, "Daniel Island": 10_886, "Bonneau": 485, "Moncks Corner": 10_933}
calhoun = {"Cameron": 1_820, "St. Matthews": 9_083, "Elloree": 3_082, "Gaston": 18_936, "North": 3_868}
beaufort = {"Hilton Head": 37_805, "Bluffton": 31_323, "Port Royal": 15_047, "Hardeeville": 9_293, "Burton": 7_132}
dorchester = {"North Charleston": 122_400, "Summerville": 51_262, "Ladson": 16_261, "St, George": 1_935, "Ridgeville": 1_591}
aiken = {"North Augusta": 24_928, "Belvedere": 5_458, "Clearwater": 3_124, "Burnettown": 3_090, "New Ellenton": 2_604}
anderson = {"Anderson": 31_676, "Belton": 4_668, "Williamston": 4_399, "Honea Path": 3_981, "Pendleton": 3_797}

counties = [berkeley, calhoun, beaufort, dorchester, aiken, anderson]

for county in counties:
    for key, value in county.items():
        print(f"In {key.title()}, the current population is {value}.")