def jokenpo(name):
    import os
    from random import randint
    from rich import print
    from time import sleep
    import pygame
    
    contadorvitorias=0
    contadorderrotas=0
    jogadadamaquina=0
    money=0
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
            rodadas=int(input("Gostaria de jogar quantas rodadas? Vence o jogador que atigir o maior numero de pontos ao fim das rodadas:  "))
            for i in range(rodadas):
                print(f"""                  Contador de Pontos
                _____________________________
                [pink]{name} : {contadorvitorias}         Máquina:{contadorderrotas}[/pink]

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
                [pink]{name}:{contadorvitorias}         Máquina:{contadorderrotas}[/pink]

                        Rodada: {i+1}|{rodadas}""")
                print("JO")      
                sleep(0.5)
                print("KEN")
                sleep(0.5)
                print("POOH!!!\n")                     
                if jogada==1:
                    if jogadadamaquina==1:
                        print("Empate!") 
                    elif jogadadamaquina==2:
                        contadorderrotas=contadorderrotas+1
                        print("Você perdeu!") 
                    elif jogadadamaquina==3:
                        print("Você Ganhou!")
                        contadorvitorias=contadorvitorias+1 
                    print(f"""O {name} lança
                            [green]{pedra}[/green]""")
                elif jogada==2:
                    if jogadadamaquina==1:
                        print("Você Ganhou!")
                        contadorvitorias=contadorvitorias+1  
                    elif jogadadamaquina==2:
                        print("Empate!")
                    elif jogadadamaquina==3:
                        contadorderrotas=contadorderrotas+1
                        print("Você perdeu!")
                    print(f"""O {name} lança
                            [green]{papel}[/green]""")
                elif jogada==3:
                    if jogadadamaquina==1:
                        contadorderrotas=contadorderrotas+1
                        print("Você perdeu!")                                 
                    elif jogadadamaquina==2:
                        print("Você Ganhou!")
                        contadorvitorias=contadorvitorias+1 
                    elif jogadadamaquina==3:
                        print("Empate!")
                    print(f"""O {name} lança
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
                money+=4.0
                print(f"""Boaaa {name}, Voce é o grande campeão !!!!
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
            elif contadorvitorias<contadorderrotas:
                print(f"""{name} foi derrotado pela máquina ☹
                [blue]
                ▄██████████████▄▄▄   ▐█▄▄▄▄█▌
                ██████▌ ▄▌ ▄ ▐ ▐▌ ███▌▀▀██▀▀
                ████▄█▌ ▄▌ ▄ ▐ ▐▌ ▀███▄▄█▌
                ▄▄▄▄▄██████████████▀[/blue] """)
                
                       
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
                if contadorvitorias > contadorderrotas:
                    return money
                elif contadorderrotas > contadorvitorias:
                    return 0
                else:
                    return 0
