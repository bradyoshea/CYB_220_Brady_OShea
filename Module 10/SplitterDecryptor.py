ciphertext = input("Enter the text you would like to decrypt: ")

length = len(ciphertext)

splitter = int(input(f"Enter the index number of where the text was originally split\n"))

decryptor = length - splitter

plaintext = ciphertext[decryptor:] + ciphertext[:decryptor]

print(plaintext)

