nota1 = int(input(" Digite a nota 1: ")) # Recebe a primeira nota na variavel
peso1 = (int(input("Digite o peso da nota 1: "))) #Recebe o primeiro peso na variavel
nota2 = int(input(" Digite a nota 2: "))
peso2 = (int(input("Digite o peso da nota 2: ")))
nota3 = int(input(" Digite a nota 3: "))
peso3 = (int(input("Digite o peso da nota 3: ")))

    media = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3) #Usa a formula de media ponderada

print("A media ponderada eh: ",media) #exibe na tela
