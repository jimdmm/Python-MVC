from src.repositories.user_repository import UserRepository
from src.models.user import User
class UserService:
    def __init__(self) -> None:
        self.repository = UserRepository()
    
    def create(self, name: str, email: str, phone: str)->None:
        user = User(name, email, phone)
        self.repository.create_user(user)
    
    def list_all(self):
        return self.repository.list_all_users()
        