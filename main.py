from personagem import Personagem
from functions import clear, menu, creditos, statusMenu
from random import choice, randint
from time import sleep
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


# Incio Código

    clear()
    print('''
    Bem Vindo(a) ao My Crab! 🦀

    Este é um joguinho inspirado na lógica de bichinho 
    virtual Tamagoshi. Nesse momento, enquanto você lê 
    essa introdução, seu Crab nasceu e é {}...
    
    Divirta-se!\n
    '''.format(creature.genero))

    creature.nome = input('    Dê um nome ao seu Crab: ') or 'Sirigueijo'
    clear()

    
    while creature.alive: # Controle dos Dias
        creature.sono = False
        contadorSono = 0
        dia += 1
        

        while True: # Controla as ações do dia do Crab

            if creature.fome and creature.doente: 
                creature.felicidade = False


            #Status do Crab
            statusMenu(dia, creature.nome, creature.idade, creature.dinheiro, creature.felicidade)


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
                contadorSono += 1
                if creature.comer():
                    clear()
                    print('\t\t\tHmm, que delícia, estou satisfeito! 🍖🍤')
                    sleep(2)
                else:
                    clear()
                    print('\t\t\tNão tenho comida!!!🦴🦴🦴')
                    

            elif action == 2: ## Tomar medicamento
                contadorSono += 1
                if creature.tomarRemedio():
                    clear()
                    print('\t\t\tUrghh, que remédio ruim...!')
                else:
                    clear()
                    print('\t\t\tEu não tenho remédio nenhum...')


            elif action == 3: ## Comprar comida
                contadorSono += 1
                if creature.comprar('COMIDA'):
                    clear()
                    print('\t\t\tVocê gastou 3 moedas 💰💰💰 ...')
                    sleep(1)
                    print('\t\t\t...Enchendo o estoque de comida 🍖🍤🍗...')
                else:
                    clear()
                    print('\t\t\tVocê não tem dinheiro suficiente para comprar comida!💸')


            elif action == 4: ## Comprar Remédio
                contadorSono += 1
                if creature.comprar('REMEDIO'):
                    clear()
                    print('\t\t\tVocê gastou 7 moedas 💰💰💰💰💰💰💰 ...')
                    sleep(1)
                    print('\t\t\t...Enchendo o estoque de Remédio!!💉💊')
                else:
                    clear()
                    print('\t\t\tVocê não tem dinheiro suficiente para comprar esse xarope!💸')


            elif action == 5: ## Opção de jogo
                contadorSono += 1
                creature.dinheiro += jokenpo(creature.nome)
                creature.felicidade = True
            

            elif action == 6: ## Dormir
                creature.envelhecer()
                creature.dormir()
                clear()
                print('\t\t\tZzzZzZzZzzZzZzZzzZzZzZzzZzZz')
                sleep(2)
                print('\t\t\tSonhando com as algas...💤💤')
                sleep(2)
                clear()
                break
            

            else:
                print('\t\t\tAção inválida')

            sleep(3)
            
            # Controle de sono que evita que exista ações diárias infinitas.
            if contadorSono == 4 : #Troca estado Crab para SONO ( Aviso )
                creature.sono = True
                print('\t\t\tEstou com muito sono💤... preciso dormir...💤💤')
                sleep(2)
            elif contadorSono == 6 : # Força o Crab a dormir.
                clear()
                print('\t\t\tNão aguentei...Dormindo...💤')
                sleep(2)
                print('\t\t\tTem tubarões me perseguindo!...💤💤')
                sleep(2)
                creature.envelhecer()
                creature.dormir()
                creature.felicidade = False
                clear()
                break

            clear()

        if not creature.doente:
            creature.doente = choice([True, False])
        if creature.felicidade:
            creature.felicidade = choice([True, False])

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
    clear()


