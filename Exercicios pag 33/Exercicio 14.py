num1=99
num2=50
soma =0

while num1 > 0:
    soma += num1/num2
    print("%s/%s " % (num1, num2))
    num1-=2
    num2-=1


print("%.2f"%soma)