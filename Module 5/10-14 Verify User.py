from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_username(path):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    date_of_birth = input("What is your date of birth? ")
    password = input("What is your password? ")
    user_info = {"username": username, "date_of_birth": date_of_birth, "password": password}
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user."""
    path = Path("username.json")
    user_info = get_stored_username(path)
    if user_info:
        valid_response = "n"
        while valid_response == "n":
            returning_user = input(f"Is {user_info['username']} your username (y/n)? ")
            if returning_user == "y":
                print(f"Username: {user_info['username']}")
                print(f"Date of birth: {user_info['date_of_birth']}")
                print(f"Password: {user_info['password']}")
                break
            elif returning_user == "n":
                user_info = get_new_username(path)
                print(f"We'll remember you when you come back, {user_info['username']}!")
                break
            else:
                print("Please enter y or n")
    else:
        user_info = get_new_username(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")


greet_user()
