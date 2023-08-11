print("Digite o tipo de instalação conforme a legenda")
print("C - Casa") 
print("I - Industria")
print("E - Empresa")
print("Qual o tipo de instalação")

tipo = input("Qual o tipo de instalação?")

if tipo == "C" or tipo == "c":
    tipo = "Casa"
    kwh = float(input("digite o consumo mensal"))
    if kwh <= 600:
        preco = kwh*0.45
    else:
        preco = kwh*0.65
elif tipo == "I" or tipo == "i":
    tipo = "Industria"
    kwh = float(input("digite o consumo mensal"))
    if kwh <= 1200:
        preco = kwh*0.75
    else:
        preco = kwh*0.95
elif tipo == "E" or tipo == "e":
    tipo = "Industria"
    kwh = float(input("digite o consumo mensal"))
    if kwh <= 6000:
        preco = kwh*0.70
    else:
        preco = kwh*0.80
else:
    print("Insira um opção valida")
    
print("O tipo de instalação {} consome kWh por mês" .format(tipo, kwh))
print("O valor da conta é de R$ {preco}")