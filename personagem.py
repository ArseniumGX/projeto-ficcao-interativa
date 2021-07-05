class Personagem:
    def __init__(self) -> None:
        self.__nome = str()
        self.__genero = str()
        self.__idade = int()
        
        self.__fome = bool()
        self.__sede =  bool()
        self.__doente = bool()
        self.__alive = bool()
        
        self.__felicidade = bool()
        self.__remedio = bool()
        self.__comida = bool()
        self.__dinheiro = float()

    def __str__(self):
        return 'Nome: {}\nGênero: {}\nIdade: {}\nFome: {}\nSede: {}\nDoente: {}\nVivo: {}\nFelicidade: {}\nRemedio: {}\nComida: {}\nDinheiro: {}'.format(self.nome, self.genero, self.idade, self.fome, self.sede, self.doente, self.alive, self.felicidade, self.remedio, self.comida, self.dinheiro)

################ GETTERS AND SETTERS ################
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, value):
        self.__genero = value

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, value):
        self.__idade = value

    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self, value):
        self.__fome = value
    
    @property
    def sede(self):
        return self.__sede
    @sede.setter
    def sede(self, value):
        self.__sede = value

    @property
    def doente(self):
        return self.__doente
    @doente.setter
    def doente(self, value):
        self.__doente = value
    
    @property
    def alive(self):
        return self.__alive
    @alive.setter
    def alive(self, value):
        self.__alive = value

    @property
    def felicidade(self):
        return self.__felicidade
    @felicidade.setter
    def felicidade(self, value):
        self.__felicidade = value

    @property
    def remedio(self):
        return self.__remedio
    @remedio.setter
    def remedio(self, value):
        self.__remedio = value

    @property
    def comida(self):
        return self.__comida
    @comida.setter
    def comida(self, value):
        self.__comida = value

    @property
    def dinheiro(self):
        return self.__dinheiro
    @dinheiro.setter
    def dinheiro(self, value):
        self.__dinheiro = value
#####################################################
    
    
###################### METHODS ######################
    
    def comer(self):
        if self.comida:
            self.fome = False
    
    def beber(self):
        self.sede = False
    
    def tomarRemedio(self):
        if self.remedio:
            self.doente = False
    
    def jogar(self):
        self.felicidade = True
        self.dinheiro += 2.0

    def envelhecer(self):
        self.idade += 1

    def dormir(self):
        return True

    def __seTem(self):
        pass
