""""
val =int(input("insira um valor"))
desc =int(input("insira um desconto"))
novoPreco = val*(1 - desc/100)
print("novo preço é igual: R$", novoPreco)

"""
#excercicios 7 lista 2

#produtos

tv = 890
mesa = 500
lqf = 120
descA = 5
descB = 10
da = (1 - descA/100)
db = (1 - descB/100)

#Dois produtos
compra1 = (tv + mesa)*da
compra2 = (tv +lqf)*da
compra3 = (mesa + lqf)*da


# Tres produtos

compra4 = (tv + mesa + lqf)*db

#comprando
print("Comprando a TV e a mesa = ", compra1)
print("Comprando a TV e a liquidificador = ", compra2)
print("Comprando a Mesa e a liquidificador = ", compra3)

