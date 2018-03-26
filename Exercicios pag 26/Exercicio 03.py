codigoProduto=0 #Variavel que vai receber o codigo do produto
qtdProduto=0 #Variavel que vai receber a quantidade de produtos

codigoProduto= input("Digite o codigo do produto comprado ")
qtdProduto = input("Digite a quantidade de produtos comprados ")

if codigoProduto == 1:
    print("O valor total eh ",qtdProduto*5.78)

elif codigoProduto == 2:
    print("O valor total eh ", qtdProduto * 9.9)

elif codigoProduto == 3:
    print("O valor total eh ", qtdProduto * 5.25)

elif codigoProduto == 4:
    print("O valor total eh ", qtdProduto * 18.90)

elif codigoProduto == 5:
    print("O valor total eh ", qtdProduto * 22.60)

else:
    print("Produto nao encontrado")