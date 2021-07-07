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


def statusMenu(dia, nome, idade, dinheiro, felicidade):
    from rich import print
    print(f'''   
            ⏱  Dia: {dia}
            -----=== Situação do do seu bichinho ===-----

                             🦀 {nome} 🦀

            Idade: {idade} dia(s)\t          💰 Moedas: {dinheiro}''')

    if felicidade == True:
        print('''[orange1]
                        ░░▄█▀▀▀░█▀█░█▀█░░░▀▀▀█▄
                        ▄███▄▄░░▀▄███▄▀░░░▄▄███▄
                        ▀██▄▄▄▄██▀███▀█▄▄▄▄██▀
                        ░░▄▄▄▄████▄▄▄████▄▄▄▄
                        ░▐▐▀▐▀░▀██████▀░▀▌▀▌▌
                [/orange1]''')
    else :
        print('''[purple]
                        ░░▄█▀▀▀░███░███░░░▀▀▀█▄
                        ▄███▄▄░░▀▄███▄▀░░░▄▄███▄
                        ▀██▄▄▄▄██▀▀▀▀▀█▄▄▄▄██▀
                        ░░▄▄▄▄███▄███▄██▄▄▄▄
                        ░▐▐▀▐▀░▀██████▀░▀▌▀▌▌
                [/purple]''')

        print('''
                                Status  
            ''')