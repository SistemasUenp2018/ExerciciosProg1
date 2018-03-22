nota1 = int(input(" Digite a nota 1: "))
peso1 = (int(input("Digite o peso da nota 1: ")))
nota2 = int(input(" Digite a nota 2: "))
peso2 = (int(input("Digite o peso da nota 2: ")))
nota3 = int(input(" Digite a nota 3: "))
peso3 = (int(input("Digite o peso da nota 3: ")))

media = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3)

print("A media ponderada eh: ",media)