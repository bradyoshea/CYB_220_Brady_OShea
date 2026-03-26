plaintext = input("Enter the phrase you would like to encrypt: ")
print()

length = len(plaintext)

ciphertext = [None] * length
positions = []

for character in plaintext:
    indices = [i for i, x in enumerate(ciphertext) if x == None]
    valid_choice = False
    while valid_choice == False:
        print(indices)
        print("Select any of the above values")
        new_position = int(input(f"Where would you like to put the character {character}? "))
        print()
        if new_position in indices:
            ciphertext[new_position] = character
            valid_choice = True
            positions.append(new_position)
        else:
            print("Select a valid position")

ciphertext = "".join(ciphertext)
print(f"Here are the new positions of the characters:\n{positions}")
print("..............................")
print(ciphertext)

decrypted_text = ""
answer = input("Would you like to decrypt? ")
if answer == "yes":
    for position in positions:
        decrypted_text += ciphertext[position]
    print(decrypted_text)


