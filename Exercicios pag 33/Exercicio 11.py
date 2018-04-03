#Programa implementado utilizando o recurso de recursao...


contador =0 #Contador/Sentinela da estrutura While
limite = int(input("Digite ateh qual espiral de fibonacci voce deseja ver")) #Recebendo a entrada, que
# definirah a quantidade de numeros da sequencia de fibonacci

def fibonacci(n): #Criacao da funcao
    if n < 2:  #Caso N for menor que 2, retorne N
        return n
    else: #Senao
        return fibonacci(n-1)+fibonacci(n-2) #Retorne a funcao com N-1 somado a N-2 (ou seja a formula de fibonacci)

while contador < limite: #Enquanto o contador for menor ou igual que o valor impostado pelo usuario, faca
    print(fibonacci(contador)) #Imprima a funcao de fibonacci, utilizando o contador como parametro
    contador +=1 #Adicione 1 iteracao a sentinela, para que ele controle o escape do loop, ah
    # nao incrementacao da sentinela acarretara em um loop infinito
