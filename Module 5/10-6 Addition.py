working = "n"
while working == "n":
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")
    try:
        number1 = int(number1)
        number2 = int(number2)
        working = "y"
    except ValueError:(
        print("You did not enter a number"))

print(f"{number1} + {number2} = {number1 + number2}")