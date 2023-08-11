#pega a informacao do salário
salario = float(input("Informe seu salário: "))
base = 1650.0
if salario <= base:
    salario = salario*1.18
else:
    salario = salario*1.12
    
print("Novo salario é R${salario}")