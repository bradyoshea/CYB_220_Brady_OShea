from users_module import User

class Admin(User):
    def __init__(self, first_name, last_name, birth_date, username):
        super().__init__(first_name, last_name, birth_date, username)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privilege = ["can add post", "can delete post", "can ban user", "can edit post"]

    def show_privileges(self):
        for item in self.privilege:
            print(item)