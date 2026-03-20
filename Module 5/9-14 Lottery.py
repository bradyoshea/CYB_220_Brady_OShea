from random import choice

lottery_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]
answer = choice(lottery_numbers) + choice(lottery_numbers) + choice(lottery_numbers) + choice(lottery_numbers)
print(f"The winning numbers are {answer}")