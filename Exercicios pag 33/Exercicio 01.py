import os

num =0
cont =1

while cont <= 10:
    print("Digite o %s numero"%cont)
    num = num + int(input())
    cont+=1
print("A soma total eh: ",num)