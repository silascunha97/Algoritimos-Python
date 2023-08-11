indus = int(input("Insira o valor gasto em kWh gasto pela indústria: "))
casa = int(input("Insira o valor gasto em kWh gasto pela casa: "))
empre = int(input("Insira o valor gasto em kWh gasto pela empresa: "))

if casa <= 600 and empre <= 6000 and indus <= 1200:
    casa_pagar = casa * 0.45
    empre_pagar = empre + (empre * 0.70)
    indus_pagar = indus * 0.75
    print("Casa recebe o valor de {} kWh para pagar, empresa recebe {} kWh a pagar, e indústria recebe {} kWh a pagar.".format(casa_pagar, empre_pagar, indus_pagar))
elif casa <= 600 and empre > 6000 and indus <= 1200:
    casa_pagar = casa * 0.45
    empre_pagar = empre * 0.70
    indus_pagar = indus * 0.75
    print("Casa recebe o valor de {} kWh para pagar, empresa recebe {} kWh a pagar, e indústria recebe {} kWh a pagar.".format(casa_pagar, empre_pagar, indus_pagar))
elif casa > 600 and empre <= 6000 and indus > 1200:
    casa_pagar = casa * 0.65
    empre_pagar =  empre * 0.70
    indus_pagar = indus * 0.95
    print("Casa recebe o valor de {} kWh para pagar, empresa recebe {} kWh a pagar, e indústria recebe {} kWh a pagar.".format(casa_pagar, empre_pagar, indus_pagar))
else:
    casa_pagar = casa * 0.65
    empre_pagar = empre * 0.70
    indus_pagar = indus * 0.95
    print("Casa recebe o valor de {} kWh para pagar, empresa recebe {} kWh a pagar, e indústria recebe {} kWh a pagar.".format(casa_pagar, empre_pagar, indus_pagar))
