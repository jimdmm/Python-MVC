class User:
    def __init__(self, name: str, email: str, phone: str):
        self._name = name
        self._email = email
        self._phone = phone

    def get_name(self)-> str:
        return self._name
    
    def get_email(self)->str:
        return self._email
    
    def get_phone(self)->str:
        return self._phone
    