indus=  int(input("Insira o valor gasto em kWh gasto pela industria"))
casa=  int(input("Insira o valor gasto em kWh gasto pela casa"))
empre= int(input("Insira o valor gasto em kWh gasto pela empresa"))

if casa <= 600 and empre <= 6000 and indus <= 1200:
    casa*0.45 and empre+(1*0.70) and indus <= indus*0.75
    print("Casa recebe o valor de {}kWh para pagar, empresa recebe {}kWh a pagas, e industria recebe {}kWh a pagar." .format(casa, empre, indus))
if casa <= 600 and empre <= 6000 >= indus <= 1200:
    casa*0.45 and empre+(1*0.70) and indus <= indus*0.75
    print("Casa recebe o valor de {}kWh para pagar, empresa recebe {}kWh a pagas, e industria recebe {}kWh a pagar." .format(casa, empre, indus))
if casa <= 600 >= empre >= 6000 >= indus <= indus:
    casa*0.45 and empre+(1*0.70) and indus <= indus*0.75
    print("Casa recebe o valor de {}kWh para pagar, empresa recebe {}kWh a pagas, e industria recebe {}kWh a pagar." .format(casa, empre, indus))
else:
    casa*0.65 and empre+(1*0.70) and indus*0.95
    print("Casa recebe o valor de {}kWh para pagar, empresa recebe {}kWh a pagas, e industria recebe {}kWh a pagar." .format(casa, empre, indus))

