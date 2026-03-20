from random import choice

lottery_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]
answer = choice(lottery_numbers) + choice(lottery_numbers) + choice(lottery_numbers) + choice(lottery_numbers)
print(f"The winning numbers are {answer}")

counter = 0
my_ticket = []

while answer not in my_ticket:
    my_ticket.append(choice(lottery_numbers) + choice(lottery_numbers) + choice(lottery_numbers) + choice(lottery_numbers))
    counter += 1

print(f"It took {counter} attempts to win")
