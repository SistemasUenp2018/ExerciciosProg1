a = 0
cont = 0
while cont < 100: # enquanto o contador for menor que 100
    if (cont%2) > 0: #Se o resto da divisao for maior que zero, quer dizer que o numero nao eh divizivel por 2, ou seja impar
        a+= cont
        cont+=1
    else:
        cont+=1
print("O resultado eh: "a)