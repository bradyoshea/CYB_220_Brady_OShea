users = []

if not users:
    print("We need to find some users")
else:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")