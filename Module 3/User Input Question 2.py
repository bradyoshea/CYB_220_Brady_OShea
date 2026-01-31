money = input("How much money do you have?\n")
money = int(money)
if money >= 350:
    print("You can afford an i9 processor")
elif money >= 300:
    print("You can afford an i7 processor")
elif money >= 180:
    print("You can afford an i5 processor")
elif money >= 120:
    print("You can afford an i3 processor")
else:
    print("You can't afford any processor")