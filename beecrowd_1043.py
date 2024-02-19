def isTriangulo(entrada):
    if (entrada[0] < (entrada[1] + entrada[2])) and (entrada[1] < (entrada[0] + entrada[2])) and (entrada[2] < (entrada[0] + entrada[1])):
        return True

entrada = input()
entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = float(entrada[i])

if isTriangulo(entrada) == True:
    perimetro = entrada[0] + entrada[1] + entrada[2]
    print("Perimetro =", round((perimetro), 1))
else:
    area = ((entrada[0] + entrada[1]) * entrada[2])/2
    print("Area =", round((area), 1))