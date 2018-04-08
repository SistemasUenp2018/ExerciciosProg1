import random
numero = random.randrange(0,100)
entrada = int(input())
contador = 1

while numero!=entrada:
    if numero < entrada:
        print("Entrada é maior que o número aleatório")
    else:
        print("Entrada é menor que o número aleatório")
    entrada = int(input())
    contador+=1
print("Parabéns, foram necessárias %s tentativas"%contador)