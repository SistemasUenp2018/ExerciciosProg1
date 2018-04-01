a = 80000
b = 200000
anos = 0

while a < b :
    a = a*1.03 # A recebe a mais 3%
    b = b*1.015 # B recebe b mais 1.5%
    anos +=1

print("Serao necessarios %s ate anos que a Cidade A alcance a cidade B"% anos)
print("Resultado final cidade a: %.2f "% a)
print("Resultado final cidade b: %.2f"% b)