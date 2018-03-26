codigoProduto=0 #Variavel que vai receber o codigo do produto
qtdProduto=0 #Variavel que vai receber a quantidade de produtos

codigoProduto= input("Digite o codigo do produto comprado ")
qtdProduto = input("Digite a quantidade de produtos comprados ")


if codigoProduto <= 5 and codigoProduto > 0: #Se o codigo do produto for maior ou igual a cinco, e maior que zero, faca!
    if codigoProduto == 5: #Se o valor do codigo do produto for igual a 5
        print("O valor total eh ", qtdProduto * 22.60) #Exiba a quantia do produto multiplicado pelo valor informado
    if codigoProduto == 4: #Se o codigo do produto for maior ou igual a quatro, e maior que zero, faca!
        print("O valor total eh ", qtdProduto * 18.90) #Exiba a quantia do produto multiplicado pelo valor informado
    if codigoProduto == 3: #Se o codigo do produto for maior ou igual a tres, e maior que zero, faca!
        print("O valor total eh ", qtdProduto * 5.25) #Exiba a quantia do produto multiplicado pelo valor informado
    if codigoProduto == 2: #Se o codigo do produto for maior ou igual a dois, e maior que zero, faca!
        print("O valor total eh ", qtdProduto * 9.9) #Exiba a quantia do produto multiplicado pelo valor informado
    if codigoProduto == 1: #Se o codigo do produto for maior ou igual a um, e maior que zero, faca!
        print("O valor total eh ", qtdProduto * 5.78) #Exiba a quantia do produto multiplicado pelo valor informado

else:
    print("Produto nao encontrado")