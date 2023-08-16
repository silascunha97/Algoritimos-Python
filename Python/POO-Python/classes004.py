class Pessoa:
    def __init__(self, nome, idade, nomeclasse):
        self.nome = nome
        self.idade = idade
        nome.nomeclasse = self.__class__.__name__
        
    def falar(self):
        print(f'{self.nomeclasse} Falando ...')

class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    pass        
    