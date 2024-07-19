from src.views.user_view import userView

def index():
    message = '''
        Sistema CRUD de Usuário

        # Cadastrar Pessoa - 1
        # Buscar Pessoa Por Nome - 2
        # Sair - 0
    '''
    user_view = userView()

    while(True):
        print(message)
        command = input('Escolha uma opção: ')
        
        match command:
            case '1':
                user_view.create()
            case '2':
                user_view.list()
            case '0':
                exit()