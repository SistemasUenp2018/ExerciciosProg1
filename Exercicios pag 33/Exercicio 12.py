numero = int(input("Digite o numero, para ver o seu fatorial: "))


def fatorial(n): #Criando a funcao
    if n <= 1: #Se n for menor ou igual a 1, retorne 1
        return 1
    else: #SENAO
       return fatorial(n-1)*n #Uso da recursao, que chama a recursao, ateh que o valor de N seja 1

print(fatorial(numero)) #Imprima o resultado
