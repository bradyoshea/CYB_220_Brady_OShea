class User:
    def __init__(self, first_name, last_name, birth_date, username):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.username}'s name is {self.first_name} {self.last_name} and their date of birth is {self.birth_date}.")

    def greet_user(self):
        print(f"Hello {self.first_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

brady = User("Brady", "O'Shea", "7/11/2007", "brady123")
print(brady.login_attempts)
brady.increment_login_attempts()
print(brady.login_attempts)
brady.increment_login_attempts()
print(brady.login_attempts)
brady.increment_login_attempts()
print(brady.login_attempts)
brady.reset_login_attempts()
print(brady.login_attempts)