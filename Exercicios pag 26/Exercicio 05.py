precoAlcool=0    #Declarando as variaveis a serem utilizadas
precoGasolina=0
distancia=0

precoAlcool= float(input("Digite o preco do alcool: ")) #Recebendo as entradas de dados
precoGasolina= float(input("Digite o preco da gasolina: "))
distancia = float(input("Insira a distancia a ser percorrida: "))

precoAlcool = precoAlcool*(distancia/10)     #Realizando os calculos, para definir qual o valor em reais gasto com cada combustivel
precoGasolina = precoGasolina*(distancia/15)

print("O preco da viagem com Gasolina eh %s, e o preco utilizando alcool eh %s" % (precoGasolina,precoAlcool))
#Exibindo o dinheiro utilizado nos dois tipos de combustivel

if precoGasolina > precoAlcool: #Se o preco final com gasolina, for maior que o preco final com alcool
    print("Recomendamos o uso de alcool") #Exiba que o alcool eh o recomendado, baseado no valor
else:  #SENAO
    print("Recomendamos o uso de gasolina") #Exiba que o recomendado eh a gasolina