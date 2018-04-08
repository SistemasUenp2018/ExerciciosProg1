num1=1
num2=1
soma =0

while num1 < 10:
    if num2%2 == 0:
      soma += num1/num2
    else:
        soma -= num1 / num2
    num1+=1
    num2 = num1**2


print("%.2f"%soma)