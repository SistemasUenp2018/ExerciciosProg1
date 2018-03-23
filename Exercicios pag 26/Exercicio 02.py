consumo = int(input("Digite em metros cubicos qual o consumo de agua mensal: ")) #Recebe o consumo
if consumo <=10: #Compara se oonsumo eh menor ou igual a 10
    print(" Seu consumo foi: ",consumo*2.55) #Exibe o consumo com a aliquota correspondente
elif consumo <= 20: #Compara se o consumo eh menor ou igual a 20
    print(" Seu consumo foi: ", consumo * 3.44)  #Exibe o consumo com a aliquota correspondente
else: #Se o consumo nao for menor ou igual a 10 ou 20, entao eh a terceira aliquota a aplicada
    print("Seu consumo foi: ", consumo * 5.25)
