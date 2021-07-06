#limpar codigo apos fazer o jogo
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;ok
# • Ler a minha escolha (Pedra, papel ou tesoura); ok
# • Decidir de forma aleatória a decisão do computador; ok
# • Mostrar quantas rodadas cada jogador ganhou;ok
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador); ok
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.
def pedra_papel_tesoura_game():
    import os
    from random import randint
    from rich import print
    from time import sleep
    import pygame
    pygame.init()
    contadorvitorias=0
    contadorderrotas=0
    jogadadamaquina=0
    votacao=""
    pedra=("""
                _______
            -----'   ____)
                    (_____)
                    (_____)
                    (____)
            -----.__(___)""")
    papel=("""
                ______
            ----'   ____)_____
                        ______)
                        _______)
                    _______)
            -----.__________)   """)
    tesoura=(""" 
                _______
            -----'   ____)____
                        ______)
                    __________)
                    (____)
            -----.__(___)""")
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
            print("""[green]Olá, bem vindo a jogo do pedra,papel,tesoura :D[/green]
                                            ✂️  ✊  📃 
                """)
            pygame.mixer.music.load('game_theme.wav')
            pygame.mixer.music.play()        
            rodadas=int(input("Gostaria de jogar quantas rodadas? Vence o jogador que atigir o maior numero de pontos ao fim das rodadas:  "))
            pygame.mixer.music.stop()
            for i in range(rodadas):
                print(f"""                  Contador de Pontos
                _____________________________
                [pink]Jogador:{contadorvitorias}         Máquina:{contadorderrotas}[/pink]

                        Rodada: {i+1}|{rodadas}""")      
                print(f""" 
                [1] Pedra 
                [red]{pedra}[/red]""")
                print(f""" 
                [2] Papel
                [blue]{papel}[/blue]""")
                print(f"""  
                [3] Tesoura 
                [yellow]{tesoura}[/yellow]""")
                jogada=int(input("Selecione a sua jogada :"))
                jogadadamaquina= randint(1,3)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""                  Contador de Pontos
                ____________________________
                [pink]Jogador:{contadorvitorias}         Máquina:{contadorderrotas}[/pink]

                        Rodada: {i+1}|{rodadas}""")
                print("JO")      
                sleep(0.5)
                print("KEN")
                sleep(0.5)
                print("POOH!!!\n")                     
                if jogada==1:
                    pygame.mixer.music.load('stone.wav')
                    pygame.mixer.music.play()
                    if jogadadamaquina==1:
                        print("Empate!") 
                    elif jogadadamaquina==2:
                        contadorderrotas=contadorderrotas+1
                        print("Você perdeu!") 
                    elif jogadadamaquina==3:
                        print("Você Ganhou!")
                        contadorvitorias=contadorvitorias+1 
                    print(f"""O Jogador lança
                            [green]{pedra}[/green]""")
                elif jogada==2:
                    pygame.mixer.music.load('paper.wav')
                    pygame.mixer.music.play()
                    if jogadadamaquina==1:
                        print("Você Ganhou!")
                        contadorvitorias=contadorvitorias+1  
                    elif jogadadamaquina==2:
                        print("Empate!")
                    elif jogadadamaquina==3:
                        contadorderrotas=contadorderrotas+1
                        print("Você perdeu!")
                    print(f"""O Jogador lança
                            [green]{papel}[/green]""")
                elif jogada==3:
                    pygame.mixer.music.load('razor.wav')
                    pygame.mixer.music.play()
                    if jogadadamaquina==1:
                        contadorderrotas=contadorderrotas+1
                        print("Você perdeu!")                                 
                    elif jogadadamaquina==2:
                        print("Você Ganhou!")
                        contadorvitorias=contadorvitorias+1 
                    elif jogadadamaquina==3:
                        print("Empate!")
                    print(f"""O Jogador lança
                        [green]{tesoura}[/green]""")                                    
                
                if jogadadamaquina==1: 
                    print(f"""A Maquina lança
                            [red]{pedra}[/red]""")
                elif jogadadamaquina==2:
                    print (f"""A Maquina lança
                            [red]{papel}[/red]""")
                elif jogadadamaquina==3:
                    print(f"""A Maquina lança
                            [red]{tesoura}[/red]""")
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')        
            if contadorvitorias>contadorderrotas: 
                print("""Voce é o grande campeão !!!!
                ⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻
                ⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿
                ⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿
                ⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿
                ⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻
                ⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼    
                ⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰
                ⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿
                ⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿
                ⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
                ⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿
                ⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸
                ⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸
                """)
                pygame.mixer.music.load('stage-clear-8-bit.wav')
                pygame.mixer.music.play()
            elif contadorvitorias<contadorderrotas:
                print("""Você foi derrotado pela maquina 
                [blue]
                ▄██████████████▄▄▄   ▐█▄▄▄▄█▌
                ██████▌ ▄▌ ▄ ▐ ▐▌ ███▌▀▀██▀▀
                ████▄█▌ ▄▌ ▄ ▐ ▐▌ ▀███▄▄█▌
                ▄▄▄▄▄██████████████▀[/blue] """)
                pygame.mixer.music.load('game-lose.wav')
                pygame.mixer.music.play()       
            else:
                print("""O Jogo ficou empatado !
                
                ░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
                ░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
                ░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
                ░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌
                ░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
                ▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌
                █▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
                █▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█
                ▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
                ▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌
                █▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█ """)
                pygame.mixer.music.load('draw-game.wav')
                pygame.mixer.music.play()  
            print(f""" PLACAR FINAL :     
                    A maquina ganhou {contadorderrotas} rodadas
                    Você venceu {contadorvitorias} rodadas
                    Ao todo houve um total de {rodadas-(contadorderrotas+contadorvitorias)} de rodadas empatadas""")
            votacao = str(input("Gostaria jogar novamente? [S/N]: ")).upper().strip()[0]
            os.system('cls' if os.name == 'nt' else 'clear')
            if votacao == 'S':
                contadorvitorias=0
                contadorderrotas=0 
            elif votacao == 'N':
                break
        