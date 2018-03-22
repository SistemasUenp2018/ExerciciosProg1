numero = 0 #variavel que vai receber o numero digitado
numero = int(input("Digite um numero inteiro: ")) #recebendo o numero informado no console,
# e atribuindo o seu valor a nossa variavel
print("O numero digitado era: %s, seu antecessor eh: %s, e seu sucessor eh: %s"%(numero,(numero-1),(numero+1))) #mostrando na tela os valores
#o operador %s vai ser substituido pela variavel, ou argumento entre parenteses
#eh importante que haja sempre o mesmo numero de "%s" e argumentos/variaveis
