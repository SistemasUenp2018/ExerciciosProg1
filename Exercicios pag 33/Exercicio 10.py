inicio = int(input("Digite o numero do inicio "))
fim = int(input("Digite o numero do final "))

if fim > inicio:
    while fim >= inicio:
        print(inicio)
        inicio+=1

else:
    print("O final é menor que o início, não foi possivel executar o algoritmo")