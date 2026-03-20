response = ""
with open("guests.txt", "w") as file:
    while response != "quit":
        response = input("What is your name (enter 'quit' to quit)?\n")
        file.write(response + "\n")
