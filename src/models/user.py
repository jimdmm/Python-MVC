class User:
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    def set_name(self, name)-> None:
        self._name = name

    def set_email(self, email)-> None:
        self._email = email

    def set_phone(self, phone)-> None:
        self._phone = phone

    def get_name(self)-> str:
        return self._name
    
    def get_email(self)->str:
        return self._email
    
    def get_phone(self)->str:
        return self._phone
    