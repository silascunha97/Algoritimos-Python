horas_mes = int(input("Horas trabalhadas no mês: "))
valor_horas = 45 
sal_bruto = horas_mes * valor_horas

#adicionais 
an = sal_bruto*0.5
saude= sal_bruto*0.12

#desconto
inss = sal_bruto*0.11

#salario liquido
sal_liq = sal_bruto + an + saude - inss

print(f"Voce trabahou {horas_mes} horas este mês")
print(f"Seu salario bruto é de R${sal_bruto}.00")
print(f"O adicional norturno é de R${an}")
print(f"o auxílio saude é de R{saude}")
print(f"O desconto de Inss é de R${inss}")
print()
print(f"seu salario liquido será {sal_liq}")