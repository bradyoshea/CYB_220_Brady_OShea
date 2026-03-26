import secrets
import string

types = ["lowercase", "uppercase", "digits", "special characters"]

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

lowercase_num = int(input("Enter the number of lowercase letters you want in your password: "))
uppercase_num = int(input("Enter the number of uppercase letters you want in your password: "))
digits_num = int(input("Enter the number of digits you want in your password: "))
special_characters_num = int(input("Enter the number of special characters you want in your password: "))
length = lowercase_num + uppercase_num + digits_num + special_characters_num
password = ""
for i in range(length):
    valid_choice = False
    while valid_choice == False:
        type = secrets.choice(types)
        if type == "lowercase":
            if lowercase_num > 0:
                password += secrets.choice(lowercase)
                lowercase_num -=1
                valid_choice = True
        if type == "uppercase":
            if uppercase_num > 0:
                password += secrets.choice(uppercase)
                uppercase_num -=1
                valid_choice = True
        if type == "digits":
            if digits_num > 0:
                password += secrets.choice(digits)
                digits_num -=1
                valid_choice = True
        if type == "special characters":
            if special_characters_num > 0:
                password += secrets.choice(special_characters)
                special_characters_num -=1
                valid_choice = True

print(f"Your password is: {password}")