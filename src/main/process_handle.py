
from .constructor.introduction_process import introduction_process

def start() -> None:
    while True:
        input = introduction_process()

        match input:
            case 'C': print('cadastrando usuário')
            case 'R': print('buscando o usuário')
            case 'S': exit()
            case _: print('\n Comando não encontrado!! \n\n')