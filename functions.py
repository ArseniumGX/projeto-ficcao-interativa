# Arquivo com algumas funções necessárias para a execução ou bom funcionamento do código

def clear(): # Função limpa o terminal 
    import platform
    import os
    if platform.system() == 'Windowns':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        return None

def menu(): # função de exibição do menu de ações
    print('''
    [ 1 ] Comer
    [ 2 ] Tomar um copo d'água
    [ 3 ] Tomar um xaropé
    [ 4 ] Comprar comida
    [ 5 ] Comprar remédio
    [ 6 ] Jogar um jogo
    [ 7 ] Ir dormir
    ''')
