win = "n"
while win == "n":
    message = input("Let's play rock paper scissors until you beat me (or type 'quit' to quit): ")
    if message == "quit":
        break
    elif message == "rock":
        print("You win!")
        win = "y"
    elif message == "paper":
        print("You lose!")
    elif message == "scissors":
        print("It's a tie!")
    else:
        print("Please select 'rock', 'paper' or 'scissors'")