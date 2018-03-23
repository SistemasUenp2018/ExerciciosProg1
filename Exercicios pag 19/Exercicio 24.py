valorPizzas = float(input("Digite a quantidade de pizzas: "))
valorPizzas = valorPizzas*23 #calculando o valor total das pizzas
valorCerveja = float(input("Digite a quantidade de cervejas (sem alcool): "))
valorCerveja = valorCerveja * 4 #calculando o valor total das cervejas
pessoas = int(input("Digite em quantas pessoas sera dividida a conta: "))
print("A conta ficou R$%s para cada pessoa" %((valorCerveja+valorPizzas)/pessoas))
#somando o valor final das pizzas e cervejas e exibindo tudo

