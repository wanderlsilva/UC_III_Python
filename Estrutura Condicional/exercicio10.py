#Equação do 2º Grau ----  ax²+bx+c=0 ----
from math import sqrt
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

#b**2 
#pow(b, 2)

delta = b**2 - 4 * a * c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"x1 = x2 = {x:.2f}")
else:
    x1 = (-b + sqrt(delta)) / (2 *a)
    x2 = (-b - sqrt(delta)) / (2 *a)
    print(f"X1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")