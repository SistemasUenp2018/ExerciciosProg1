import math

cargaHoraria = int(input("Por favor, digite a carga horaria da disciplina: "))
cargaHoraria = (cargaHoraria*60)/50 #Realizando o seguinte calculo
#Dividindo a carga horaria temos a quantidade de minutos necessarios, e dividindo por 50 temos o numero de aulas
cargaHoraria = math.ceil(cargaHoraria) #Arredondando para cima para nao termos aulas pela metade
print("O total de aulas necessarias para o cumprimento desta carga horaria, sao %s aulas"%cargaHoraria)