from src.controllers.user_controller import UserController

class userView:
    def __init__(self):
        self.user_controller = UserController()

    def create(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")

        self.user_controller.create_user(name, email, phone)

    def list(self):
        self.user_controller.list_all_users()
        
        