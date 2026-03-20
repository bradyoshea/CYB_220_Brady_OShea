class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is now open")

bradys = Restaurant("Brady's", "Mexican")
mcdonalds = Restaurant("McDonald's", "Fast Food")
olive_garden = Restaurant("Olive Garden", "Italian")

bradys.describe_restaurant()
mcdonalds.describe_restaurant()
olive_garden.describe_restaurant()