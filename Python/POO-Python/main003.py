"""_summary_
    Encapsulamento:
    public, protected, private.
    _ Protected
    __Private
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
        
    @property
    def __dados(self):
         return self.__dados
             
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]
            
        
bd = BaseDeDados()
bd.inserir_cliente(1, 'Silas')
bd.inserir_cliente(2, 'Victor')
bd.inserir_cliente(3, 'Lara')
bd.inserir_cliente(4, 'Elisete')
bd.inserir_cliente(5, 'Carol')
bd.apaga_cliente(5)

bd.lista_clientes()
print(bd.__dados)