import json
filename = "number_remembered.json"

try:
    with open(filename) as file:
        number_remembered = json.load(file)
except FileNotFoundError:
    number_remembered = input("What is your favorite number? ")
    with open(filename, "w") as file:
        json.dump(number_remembered, file)
        print(f"I know your favorite number! It's {number_remembered}.")
else:
    print(f"I know your favorite number! It's {number_remembered}.")