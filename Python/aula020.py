a = 374
b = 597
par = 0
impar = 0

while a <= b:
    if a % 2 == 0:
        par += 1
        
    else:
        impar += 1
    a += 1
print("Quantidade de numeros pares: {par}")
print()
print("Quantidade de numeros pares: {impar}")
