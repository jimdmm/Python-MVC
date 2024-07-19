class UserRepository:
    def __init__(self):
        self.users = []

    def create_user(self, user)->None:
        self.users.append(user)

    def list_all_users(self)->list:
        return self.users