import math

entrada = input()

entrada = entrada.split(" ")

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = (B**2) - (4 * A * C)

if delta <= 0:
    print("Impossivel calcular")
else:
    raiz = math.sqrt(delta)
    if (2 * A == 0) or (raiz < 0):
        print("Impossivel calcular")
    else:
        x = (-B + raiz)/(2 * A)
        x1 = (-B - raiz)/(2 * A)
        print("R1 =", round(x, 5))
        print("R2 =", round(x1, 5))