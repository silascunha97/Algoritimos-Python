from datetime import datetime
from random import randint

ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

class Pessoa:
    
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        print(ano_atual - self.idade)
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

#p1 = Pessoa.por_ano_nascimento('Silas', 1997)
p1 = Pessoa('Silas', 26)
print(p1)
print('Seu nome é', p1.nome, 'Sua idade é', p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())
