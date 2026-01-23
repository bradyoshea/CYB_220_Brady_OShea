pizzas = ["Pepperoni", "Meat Lovers", "Italian Sausage"]
friend_pizzas = pizzas[:]
pizzas.append("Buffalo Chicken")
friend_pizzas.append("Hawaiian")

for pizza in pizzas:
    print(f'I like {pizza} pizza')

for pizza in friend_pizzas:
    print(f"My friend likes {pizza} pizza")