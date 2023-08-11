import numpy as np

a = 1
b = -15
c = 6

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não tem raízes reais.")
else:
    if a == 0:
        print("Coeficiente 'a' não pode ser igual a zero para uma equação quadrática.")
    else:
        x1 = (-b + np.sqrt(delta)) / (2*a)
        x2 = (-b - np.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
