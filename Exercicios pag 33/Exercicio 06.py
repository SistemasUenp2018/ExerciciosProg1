numero = -1
soma = 0
contador = 0
while numero != 0:
    numero = int(input("Digite algum numero, ou 0 para encerrar o loop: "))
    soma+= numero
    contador+=1

soma= soma/(contador-1)
print("A media eh: ",soma)
