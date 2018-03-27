import math
n1 = float(input("Digita a area a ser pintada ")) #Recebe a area a ser pintada
n1= int(n1//3) #Cada lata da pra 3 metros de area pintada, entao dividindo por 3 descobrimos quantas litros serao necessarias
n1 = n1/18 #Quantidade de latas necessarias
n1= math.ceil(n1) #Arredondando para cima
print("Serao necessarias %.0f latas de tinta, e o preco final serah de R$%.2f"% (n1,n1*80)) #exibe as latas necessarias, e multiplica por 80 que eh o valor unitario da lata