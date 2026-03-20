class User:
    def __init__(self, first_name, last_name, birth_date, username):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.username = username

    def describe_user(self):
        print(f"User {self.username}'s name is {self.first_name} {self.last_name} and their date of birth is {self.birth_date}.")

    def greet_user(self):
        print(f"Hello {self.first_name}.")
