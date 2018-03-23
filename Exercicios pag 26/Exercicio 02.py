consumo = int(input("Digite em metros cubicos qual o consumo de agua mensal: "))

if consumo <=10:
    print(" Seu consumo foi: ",consumo*2.55)
elif consumo <= 20:
    print(" Seu consumo foi: ", consumo * 3.44)
else:
    print("Seu consumo foi: ", consumo * 5.25)
