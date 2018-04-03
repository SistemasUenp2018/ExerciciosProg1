#Para descobrir se um numero eh divisivel por outro, basta utilizarmos o operador modulo (%),
# que retorna o resto de uma divisao, se o resto for zero, ele eh sim divisivel




numero = int(input("Digite o numero para descobrir se ele eh ou nao primo: "))
contador =numero-1 #Contador recebe o numero digitado menos um, pois sabemos que ele eh divisivel por ele mesmo
primo = 1 #Recebe o valor de um, para começar como positivo, pois ateh que
# provemos o contrario, todos os numeros podem ser primos

while contador > 1: #Enquanto o contador for maior que um, ja que os numeros primos sao diviziveis por um
    if numero%contador == 0: #Se o resto da divisao (do numero impostado, pelo contador) for igual a zero
        primo = 0 #Primo recebe 0, sinalizando como FALSO
    contador-=1 #Contador decrementa um, pois serao testados todos os
    # numeros menores que o numero impostado pelo usuario

if primo==1: #Se o valor for igual a um, significa que os quesitos para que ele
    # seja um numero primo, foram cumpridos
    print("Eh primo")
else:
    print("Nao primo")