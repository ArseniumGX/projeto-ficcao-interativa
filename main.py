from personagem import Personagem
from functions import clear, menu
from random import choice, randint
from time import sleep
from PedraPapelTesoura.Projeto02JokenPo import jokenpo

# Nome do projeto: My Crab

if __name__ == '__main__':
    clear()
    perigo = 0 # variável de controle sobre a vida do personagem
    dia = 0 # inicializador dos dias dentro do do while
    creature = Personagem()
    creature.genero = choice(['Macho', 'Fêmea'])
    creature.fome = True # nasce com fome pq sim
    creature.sede = True # com sede tbm
    creature.doente = False # situação aleatória ou random.choice
    creature.felicidade = True # Feliz por ter nascido
    creature.remedio = False # sem remedio pra curar de doença
    creature.comida = False # nasce sem comida. aqui não tem facilidade
    creature.dinheiro = 20.0
    creature.alive = True

    print('''
    Bem Vindo(a) ao Creature Simulator!

    Este é um joguinho baseado na lógica de bichinho 
    virtual baseado no lendáriota Tamagoshi. Nesse 
    momento, enquanto você lê essa introdução, seu 
    bichinho virtual nasceu e é {}.
    
    Dê um nome ao bichinho e só vai. Divirta-se!\n
    '''.format(creature.genero))
    creature.nome = input('    Digite um nome: ') or 'Coisa'


    while creature.alive:
        dia += 1
        creature.doente = choice([True, False])

        while True:
            print(f'''
            Dia: {dia}
            -----=== Situação do do seu bichinho ===-----

            Nome do bichinho: {creature.nome}
            Idade: {creature.idade} dia(s)\tMoedas: {creature.dinheiro}
            Status:
            ''')
            if creature.fome == True:
                print('\t\t - Está com fome')
                perigo += 1
            else:
                print('\t\t + Não está fome')

            if creature.sede == True:
                print('\t\t - Está com sede')
                perigo += 1
            else:
                print('\t\t + Não está tem sede')

            if creature.doente == True:
                print('\t\t - Está com doente')
                perigo += 5
            else:
                print('\t\t + Não está doente')

            if creature.felicidade == True:
                print('\t\t - Está feliz')
                perigo += 1
            else:
                print('\t\t + Não está feliz')

            menu()
            action = input('    [ ')
            while not action.isdigit() or action == '':
                action = input('    [ ')
            action = int(action)

            if action == 1: ## Comer
                if creature.comer():
                    print('Comido com sucesso!')
                else:
                    print('Com fome!')
            elif action == 2: ## Tomar água
                if creature.beber():
                    print('Bebido')
            
            elif action == 3: ## Tomar medicamento
                if creature.tomarRemedio():
                    print('\t\t\tMedicamento tomado!')
                else:
                    print('\t\t\tVocê não tem medicamento!')

            elif action == 4: ## Comprar comida
                if creature.comprar('COMIDA'):
                    print('\t\t\tComida comprada!')
                else:
                    print('Você não tem dinheiro suficiente!')

            elif action == 5: ## Comprar Medicina
                if creature.comprar('REMEDIO'):
                    print('Medicina comprada')
                else:
                    print('Você não tem dinheiro suficiente!')

            elif action == 6: ## Opção de jogos
                creature.dinheiro += jokenpo(creature.nome)
                creature.felicidade = True
            
            elif action == 7: ## Dormir
                creature.envelhecer()
                print('\n\n\n\t\t\t', creature.dormir())
                break
            
            else:
                print('\t\t\tAção inválida')
            

        if perigo < 100:
            continue
        else:
            creature.alive = False

print('Qua triste.\nSeu animal morreu! ') # <- temporário
input()