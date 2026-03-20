try:
    with open("cats.txt") as cats_file:
        cats = cats_file.read()
        print(cats)
except FileNotFoundError:
    print("The file cats.txt was not found")

try:
    with open("dogs.txt") as dogs_file:
        dogs = dogs_file.read()
        print(dogs)
except FileNotFoundError:
    print("The file dogs.txt was not found")