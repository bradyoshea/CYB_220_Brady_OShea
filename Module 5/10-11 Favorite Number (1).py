import json
number = input("What is your favorite number? ")
filename = "number.json"
with open(filename, "w") as file:
    json.dump(number, file)