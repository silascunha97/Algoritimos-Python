from classes003 import Cliente, Endereco

cliente1 = Cliente('Silas', 26)
cliente1.insere_endereco('Itajaí', 'SC')

cliente2 = Cliente('Luciano', 45)
cliente2.insere_endereco('Rio de Janeiro', 'RJ')

cliente3 = Cliente('Malthus', 23)
cliente3.insere_endereco('Ribeirão Preto', 'SP')
cliente1.lista_enderecos()
print()

