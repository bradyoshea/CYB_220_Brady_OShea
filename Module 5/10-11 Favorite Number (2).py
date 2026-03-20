import json

filename = "number.json"
with open(filename) as file:
    number = json.load(file)

print(f"I know your favorite number! It's {number}.")