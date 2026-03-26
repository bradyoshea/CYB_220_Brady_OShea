plaintext = input("Enter the text you would like encrypt: ")

length = len(plaintext)

message = f"Where would you like the text split?\nEnter a number between 1 and {length-1}\n"

splitter = int(input(message))

ciphertext = plaintext[splitter:] + plaintext[:splitter]

print(ciphertext)