from src.models.user import User
class UserController:
    def __init__(self):
        self.users = []

    def create_user(self, name: str, email: str, phone):
        user = User(name, email, phone)
        self.users.append(user)

    def list_all_users(self):
        if len(self.users) == 0:
            print("Sem usuário cadastrado")
            return

        for user in self.users:
            msg = f"{user.get_name()}, {user.get_email()}, {user.get_phone()}"
            print(msg)

