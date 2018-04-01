mediaSala=0
maiorNota=0
menorNota=100
menorQue=0
nota=0
contador = 0
soma = 0

while nota >= 0:
    nota = int(input("Digite a nota: "))
    if nota>= 0:
        if nota>maiorNota: #Se a nota atual eh maior que maior nota, maiorNota recebe esse valor
            maiorNota=nota
        if nota < menorNota: #Se a nota atual for menor que a menorNota, menorNota recebe esse valor
            menorNota = nota
        if nota < 7: #Se a nota for menor que sete, contador especifico atribui mais um
            menorQue += 1

        soma+=nota #Soma para ser utilizada na media
        contador += 1 #Contador para ser utilizado na media

print("A maior nota foi: ",maiorNota)
print("A menor nota foi: ",menorNota)
if contador >0:
    print("A media da sala foi: ",(soma/contador))
print("A quantia de notas abaixo de sete foi: ",menorQue)