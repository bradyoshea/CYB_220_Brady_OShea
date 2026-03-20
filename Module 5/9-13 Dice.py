import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        print(random.randint(1, self.sides))

six_side = Die()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
six_side.roll()
print()

ten_side = Die(10)
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
ten_side.roll()
print()

twenty_side = Die(20)
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
twenty_side.roll()
print()

