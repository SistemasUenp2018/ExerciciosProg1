print("Estao disponiveis para saque notas de R$50,00 R$20,00 R$10,00 R$5,00 ") #nforma as cedulas disponiveis
valorSaque = int(input("Digite o valor pretendido de saque: ")) #Recebe o valor do saque

notas50 = 0 #Cada cedula tem uma variavel, para melhor controle
notas20 = 0
notas10 = 0
notas05 = 0

if (valorSaque % 5) > 0: #Verifica se o valor desejado eh multiplo de 5, caso nao seja, o saque nao pode ser realizado
    print("Quantia invalida o saque nao sera realizado")
else:
    aux = valorSaque #Variavel auxiliar criada com o objetivo de controlar, qual o valor ainda precisa ser
    #distribuido entre as cedulas disponiveis

    notas50 = aux//50 #A variavel recebe, o valor inteiro da divisao (valor do saque/50)
    aux = aux - notas50*50 #A variavel auxiliar subtrai do valor a ser pago, o valor que ja tem decidido qual cedula utilizar
    notas20 = aux//20  #A variavel recebe, o valor inteiro da divisao (valor do saque/20)
    aux = aux - notas20*20 #A variavel auxiliar subtrai do valor a ser pago, o valor que ja tem decidido qual cedula utilizar
    notas10 = aux //10 #A variavel recebe, o valor inteiro da divisao (valor do saque/20)
    aux = aux - notas10*10 #A variavel auxiliar subtrai do valor a ser pago, o valor que ja tem decidido qual cedula utilizar
    notas05 = aux//5 #A variavel recebe, o valor inteiro da divisao (valor do saque/20)
    aux = aux - notas05*5 #A variavel auxiliar subtrai do valor a ser pago, o valor que ja tem decidido qual cedula utilizar

    print("Serao necessarias") #Imprime as cedulas que serao utilizadas, apenas se o valor de cedulas for maior que 0
    if (notas50>0):
        print("%s notas de 50 reais"% notas50)
    if (notas20 > 0):
        print("%s notas de 20 reais"% notas20)
    if (notas10 > 0):
        print("%s notas de 10 reais"% notas10)
    if (notas05 > 0):
        print("%s notas de 5 reais"% notas05)
