tipo = 0
rose = 0
tinto =0
branco =0
cancela = 0

while cancela == 0:
    tipo = input("Insira R, B ou T para informar o tipo do vinho: ")
    if tipo == "R" or tipo == "r":
        rose += 1
    elif tipo == "T" or tipo == "t":
        tinto += 1
    elif tipo == "B" or tipo == "b":
        branco+=1
    elif tipo == "X" or tipo == "x":
        print("As quantidades saio %s garrafas de tinto, %s garrafas de branco, e %s garrafas de rose" % (tinto, branco, rose))
        cancela = 1
    else:
        print("Tipo invalido informar novamente")

