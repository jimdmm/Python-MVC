from src.services.user_service import UserService
from src.models.user import User
class UserController:

    def __init__(self) -> None:
        self.service = UserService()
    def create_user(self, name: str, email: str, phone: str)->None:
        self.service.create(name, email, phone)

    def list_all_users(self)-> User:
        return self.service.list_all()

