# Arquivo com algumas funções necessárias para a execução ou bom funcionamento do código

def clear(): # Função limpa o terminal 
    from os import system, name
    system('cls') if name == 'nt' else system('clear')


def menu(): # função de exibição do menu de ações
    print('''
    Selecione uma ação: 

    [ 1 ] Comer
    [ 2 ] Tomar um xarope
    [ 3 ] Comprar comida
    [ 4 ] Comprar remédio
    [ 5 ] Jogar um jogo
    [ 6 ] Ir dormir
    ''')


def creditos() :
    import sys
    from time import sleep
    bio = '''
              Obrigado por jogar!

                  Criado por

            Akylles Ferreira Barros
              José Pereira Macedo
        Victor Fernando Moura da Luz Santos


    
    '''
    for c in bio :
        sys.stdout.flush()
        print(c, end= '')
        sleep(0.05)

    input('Tecle ENTER para encerrar o programa.')


def menuJogos(): ## Não implementado
    print('''
    O que deseja jogar? 

    [ 1 ] Jokenpô
    [ 2 ] Jogo 2

    [ 0 ] Voltar
    ''')

    op = str(input('\t .: '))
    while not op.isdigit() or op in '':
        op = str(input('\t\tOpção inválida!\n\t .: '))
    op = int(op)
    
    if op == 1:
        pass
    elif op == 2:
        pass
    if op == 0:
        return None
