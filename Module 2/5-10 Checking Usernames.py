current_users = ("JOHN", "bob", "Sam", "Adam", "joe")
new_users = ("john", "Brandon", "Adam", "Bill", "kevin")
lower_users = []

for user in current_users:
    lower_users.append(user.lower())

for user in new_users:
    if user.lower() in lower_users:
        print(f"{user}: You need a new username")
    else:
        print(f"{user}: This username is available")