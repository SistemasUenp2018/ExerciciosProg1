altura = float(input("Digite por favor a sua altura em metros: "))
genero = input("Digite por favor o seu genero H ou M: ")

if genero == "H" or genero == "h":
    print("Seu peso ideal eh %s caro Senhor"%(72.7*altura-58))

elif genero == "M" or genero == "m":
    print("Seu peso ideal eh %s cara Senhora" % (62.1 * altura - 44.7))

else:
    print("Foi impossivel realizar o calculo com as informacoes fornecidas")