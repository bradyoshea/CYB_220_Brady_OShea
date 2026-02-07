def sandwich(*toppings):
    print("User ordered sandwich with the following toppings:")
    for topping in toppings:
        print(topping)
    print()

sandwich("ham", "cheese", "lettuce")
sandwich("cheese")
sandwich("chicken", "cheese", "bacon", "lettuce")
