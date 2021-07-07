import os
from platform import system
import sys
from personagem import Personagem
from functions import clear, menu, creditos
from random import choice, randint
from time import sleep, time
from PedraPapelTesoura.Projeto02JokenPo import jokenpo
from rich import print


# Nome do projeto: My Crab


if __name__ == '__main__':
    clear()
    perigo = 0 # variável de controle sobre a vida do personagem
    dia = 0 # inicializador dos dias dentro do do while
    creature = Personagem()
    creature.genero = choice(['Macho', 'Fêmea'])
    creature.fome = True # nasce com fome porque não comeu na barriga
    creature.doente = False # situação aleatória ou random.choice
    creature.felicidade = False 
    creature.remedio = False # sem remedio pra curar de doença
    creature.comida = False # nasce sem comida. Aqui não tem facilidade
    creature.dinheiro = 20.0 # Auxilio Emergencial Covid
    creature.alive = True # Evitar + Whiles True
    contadorNegativo = False


# Incio Código

    os.system('cls')
    print('''
    Bem Vindo(a) ao My Crab! 🦀

    Este é um joguinho inspirado na lógica de bichinho 
    virtual Tamagoshi. Nesse momento, enquanto você lê 
    essa introdução, seu Crab nasceu e é {}...
    
    Divirta-se!\n
    '''.format(creature.genero))

    creature.nome = input('    Dê um nome ao seu Crab: ') or 'Sirigueijo'
    os.system('cls')

    
    while creature.alive: # Controle dos Dias
        creature.sono = False
        contadorSono = 0
        dia += 1
        creature.doente = choice([True, False])


        while True: # Controla as ações do dia do Crab

            if creature.fome  and creature.doente  : 
                creature.felicidade = False

            #Status do Crab
            print(f'''   
            ⏱  Dia: {dia}
            -----=== Situação do do seu bichinho ===-----

                             🦀 {creature.nome} 🦀

            Idade: {creature.idade} dia(s)\t          💰 Moedas: {creature.dinheiro}''')

            if creature.felicidade == True:
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
            
            if creature.fome == True:
                print('             - 🍴 Estou com fome!')
                perigo += 1
                
            else:
                print('             + 🍴 Não estou com fome!')
                

            if creature.sono == True:
                print('             - 💤 Estou com sono!')
                perigo += 1
                
            else:
                print('             + 💤 Não estou com sono!')
                
            if creature.doente == True:
                print('             - 💊 Estou doente!')
                perigo += 5
            else:
                print('             + 💊 Não estou doente!')

            if creature.felicidade == True:
                print('             + ✨ Estou feliz!')
            else:
                print('             - ✨ Estou Triste! Brinca comigo?')
                perigo += 1

           
            menu() # Imprime o Menu 


            # Variável que armazena a ação, verifica se a ação é um valor numérico ou é vazio. 
            action = input('    [ ')
            while not action.isdigit() or action == '':
                action = input('    [ ')
            action = int(action) # Converte a entrada do input para inteiro


            if action == 1: ## Comer
                if creature.comer():
                    os.system('cls')
                    print('\t\t\tHmm, que delícia, estou satisfeito! 🍖🍤')
                    sleep(2)
                else:
                    os.system('cls')
                    print('\t\t\tNão tenho comida!!!🦴🦴🦴')
                    

            elif action == 2: ## Tomar medicamento
                if creature.tomarRemedio():
                    os.system('cls')
                    print('\t\t\tUrghh, que remédio ruim...!')
                else:
                    os.system('cls')
                    print('\t\t\tEu não tenho remédio nenhum...')


            elif action == 3: ## Comprar comida
                if creature.comprar('COMIDA'):
                    os.system('cls')
                    print('\t\t\tVocê gastou 3 moedas 💰💰💰 ...')
                    sleep(1)
                    print('\t\t\t...Enchendo o estoque de comida 🍖🍤🍗...')
                else:
                    os.system('cls')
                    print('\t\t\tVocê não tem dinheiro suficiente para comprar comida!💸')


            elif action == 4: ## Comprar Remédio
                if creature.comprar('REMEDIO'):
                    os.system('cls')
                    print('\t\t\tVocê gastou 7 moedas 💰💰💰💰💰💰💰 ...')
                    sleep(1)
                    print('\t\t\t...Enchendo o estoque de Remédio!!💉💊')
                else:
                    os.system('cls')
                    print('\t\t\tVocê não tem dinheiro suficiente para comprar esse xarope!💸')


            elif action == 5: ## Opção de jogos
                creature.dinheiro += jokenpo(creature.nome)
                creature.felicidade = True
            

            elif action == 6: ## Dormir
                creature.envelhecer()
                creature.dormir()
                os.system('cls')
                print('\t\t\tZzzZzZzZzzZzZzZzzZzZzZzzZzZz')
                sleep(2)
                print('\t\t\tSonhando com as algas...💤💤')
                sleep(2)
                os.system('cls')
                break
            

            else:
                print('\t\t\tAção inválida')

            sleep(3) 
            
            # Controle de sono que evita que exista ações diárias infinitas.
            contadorSono += 1
            if contadorSono == 5 : #Troca estado Crab para SONO ( Aviso )
                creature.sono = True
                print('\t\t\tEstou com muito sono💤... preciso dormir...💤💤')
                sleep(2)
            elif contadorSono == 7 : # Força o Crab a dormir.
                os.system('cls')
                print('\t\t\tNão aguentei...Dormindo...💤')
                sleep(2)
                print('\t\t\tTem tubarões me perseguindo!...💤💤')
                sleep(2)
                creature.envelhecer()
                creature.dormir()
                creature.felicidade = False
                os.system('cls')
                break

            os.system('cls')  

        # Passa o estado do personagem para pior. 
        if perigo < 25:
            continue
        else:
            creature.alive = False

    print('''
          Que triste! Seu Crab morreu! 
            ──▄────▄▄▄▄▄▄▄────▄───
            ─▀▀▄─▄█████████▄─▄▀▀──
            ─────██─▀███▀─██──────
            ───▄─▀████▀████▀─▄────
            ─▀█────██▀█▀██────█▀──
            ''') 

    creditos() # Imprime os créditos do game. 


