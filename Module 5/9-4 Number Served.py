class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is now open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

bradys = Restaurant("Brady's", "Mexican")
print(bradys.number_served)
bradys.number_served = 1000
print(bradys.number_served)
bradys.set_number_served(2000)
print(bradys.number_served)
bradys.increment_number_served(1000)
print(bradys.number_served)
