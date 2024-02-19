def ordem(entrada):
    for i in range(len(entrada)):
        posicao = i

        for j in range(i + 1, len(entrada)):
            if entrada[j] > entrada[posicao]:
                posicao = j

        entrada[i], entrada[posicao] = entrada[posicao], entrada[i]
    return entrada

entrada = input()
entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = float(entrada[i])

entrada = ordem(entrada)

if entrada[0] >= (entrada[1] + entrada[2]):
    print("NAO FORMA TRIANGULO")

else:
    if (entrada[0]**2) == ((entrada[1]**2) + (entrada[2]**2)):
        print("TRIANGULO RETANGULO")
    elif (entrada[0]**2) > ((entrada[1]**2) + (entrada[2]**2)):
        print("TRIANGULO OBTUSANGULO")
    elif ((entrada[0]**2) < ((entrada[1]**2) + (entrada[2]**2))):
        print("TRIANGULO ACUTANGULO")

    if entrada[0] == entrada[1] == entrada[2]:
        print("TRIANGULO EQUILATERO")
    elif (entrada[0] == entrada[1]) or (entrada[1] == entrada[2]) or (entrada[0] == entrada[2]):
        print("TRIANGULO ISOSCELES")