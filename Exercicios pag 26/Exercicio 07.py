n1 = int(input("Digite um numero inteiro: ")) #Recebendo o primeiro numero
n2 = int(input("Digite um numero inteiro: ")) #Recebendo o segundo numero
n3 = int(input("Digite um numero inteiro: ")) #Recebendo o terceiro numero

orden1 = 0 #Variavel que recebera o primeiro numero ordenado
orden2 = 0 #Variavel que recebera o segundo numero ordenado
orden3 = 0 #Variavel que recebera o terceiro numero ordenado


if n1 > n2 and n1 > n3:   #Caso N1 seja maior que N2 E Maior que N3 FACA!
    orden1 = n1   #Como ele seria o maior dos tres numeros, ele vai como primeiro ordenado
    if n2 > n3: #Se N2 for maior que N3, ele sera o segundo maior, entao alocamos ele
        # como segundo ordenado, e o numero que restar eh o ultimo
        orden2 = n2
        orden3 = n3
    else: #SENAO (Se a estrutura de decisao anterior devolver FALSO) significa que o
                   # segundo maior numero eh n3
        orden2 = n3
        orden3 = n2
elif n2 > n1 and n2 > n3: #Caso N2 seja maior que N1 E Maior que N3 FACA!
    orden1 = n2 #Como ele seria o maior dos tres numeros, ele vai como primeiro ordenado
    if n1 > n3:#Se N1 for maior que N3, ele sera o segundo maior, entao alocamos ele
               # como segundo ordenado, e o numero que restar eh o ultimo
        orden2 = n1
        orden3 = n3
    else:#SENAO (Se a estrutura de decisao anterior devolver FALSO) significa que o
                   # segundo maior numero eh n3
        orden2 = n3
        orden3 = n1
elif n3 > n1 and n3 > n2: #Caso N3 seja maior que N1 E Maior que N2 FACA!
    orden1 = n3 #Como ele seria o maior dos tres numeros, ele vai como primeiro ordenado
    if n1> n2:#Se N1 for maior que N2, ele sera o segundo maior, entao alocamos ele
        # como segundo ordenado, e o numero que restar eh o ultimo
        orden2= n1
        orden3 = n2
    else:#SENAO (Se a estrutura de decisao anterior devolver FALSO) significa que o
                   # segundo maior numero eh n2
        orden2 = n2
        orden3 = n1


print("Primeiro (%s) segundo (%s) e terceiro numero (%s) "% (orden1, orden2, orden3)) #Exibindo tudo

