nota1 = float (input("Digite a nota 1: "))
nota2 = float (input("Digite a nota 2: "))
sexo = input("Digite o genero H ou M: ")
media = (nota1+nota2)/2

if media >= 7:
    if sexo == "H" or sexo =="h":
        print("Parabens, aprovado")
    else:
        print("Parabens, aprovada")
else:
    if sexo == "H" or sexo == "h":
        print("Que pena, reprovado")
    else:
        print("Que pena, reprovada")