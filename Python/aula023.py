for i in range(3):
    nome = input("Digite o nome do aluno: ")
    p1 = float(input("digite nota da p1"))
    p2 = float(input("digite nota da p2"))
    media = (p1+p2)/2
    
    if media >= 6: 
        condicao = "Aprovado"
    else:
        condicao = "Reprovado"
    print(f"{nome}, sua media é {media} e vc está {condicao}")
    