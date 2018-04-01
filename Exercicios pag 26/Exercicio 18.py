pesoPeixes = int(input("Por favor, digite em KG o peso dos peixes: "))

if pesoPeixes > 50:
    print("O valor da multa serah R$%.2f"%((pesoPeixes-50)*4))
else:
    print("Tudo certo, sem multa")