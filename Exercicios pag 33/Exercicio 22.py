import random
contador = 0
dado =0
dado1 =0
dado2 =0
dado3 =0
dado4 =0
dado5 =0
dado6 =0


while contador <= 787:
    dado = random.randint(1, 6)

    if dado == 1:
        dado1 +=1
    elif dado == 2:
        dado2 +=1
    elif dado == 3:
        dado3 +=1
    elif dado == 4:
        dado4 +=1
    elif dado == 5:
        dado5 +=1
    elif dado == 6:
        dado6 +=1

    contador+=1

print("o 1 saiu %s vezes, o que equivale a %2.f porcento" % (dado1, (dado1/787)*100))
print("o 2 saiu %s vezes, o que equivale a %2.f porcento" % (dado2, (dado2/787)*100))
print("o 3 saiu %s vezes, o que equivale a %2.f porcento" % (dado3, (dado3/787)*100))
print("o 4 saiu %s vezes, o que equivale a %2.f porcento" % (dado4, (dado4/787)*100))
print("o 5 saiu %s vezes, o que equivale a %2.f porcento" % (dado5, (dado5/787)*100))
print("o 6 saiu %s vezes, o que equivale a %2.f porcento" % (dado6, (dado6/787)*100))