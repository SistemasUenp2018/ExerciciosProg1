cont=0 #O contador recebe zero
qtd=int(input()) #Recebemos o primeiro numero
soma=qtd #o primeiro numero eh incluido na soma
while qtd > cont: #Enquanto a quantidade for menor que a soma faça
    soma+=int(input()) #Soma recebe ela mesmo, mais o numero impostado pelo usuario
    cont+=1 #Contador recebe ele, e mais um a cada iteração

print(soma)