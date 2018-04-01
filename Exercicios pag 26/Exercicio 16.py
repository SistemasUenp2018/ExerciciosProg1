idade = int(input("Informe a idade do nadador: "))

if idade <=7:
    print("Infantil A")

elif idade < 11:
    print("Infantil B")
elif idade < 14:
    print("Juvenil A")
elif idade < 18:
    print("Juvenil B")
else:
    print("Adulto")