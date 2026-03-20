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

brady = User("Brady", "O'Shea", "7/11/2007", "brady123")
john = User("John", "Doe", "2/1/2007", "john123")
brandon = User("Brandon", "Grech", "unknown", "bgrech")

brady.describe_user()
brady.greet_user()
john.describe_user()
john.greet_user()
brandon.describe_user()
brandon.greet_user()