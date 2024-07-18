def introduction_page():
    message = '''
        Sistema CRUD de Usuário

        # Cadastrar Pessoa - C
        # Buscar Pessoa Por Nome - R
        # Sair - S
    '''

    print(message)
    command = input('Escolha uma opção: ')

    return command