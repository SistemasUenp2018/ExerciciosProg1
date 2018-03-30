lista = input("Digite tres numeros inteiros separados por espaco: ") #Lendo tudo numa linha soh
lista = lista.split(" ") #Separando os numeros
a = int(lista[2]) #Recebendo eles em variaveis e convertendo em inteiros
b = int(lista[0])
c = int(lista[1])

print("A:%s B:%s C:%s "% (a,b,c)) #Exibindo tudo