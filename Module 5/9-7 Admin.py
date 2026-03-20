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

class Admin(User):
    def __init__(self, first_name, last_name, birth_date, username):
        super().__init__(first_name, last_name, birth_date, username)
        self.privelages = ["can add post", "can delete post", "can edit post", "can ban user"]

    def show_privelages(self):
        for privelage in self.privelages:
            print(privelage)

brady = Admin("Brady", "O'Shea", "7/11/2007", "brady123")
brady.show_privelages()