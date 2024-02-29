numero = 1

while numero != 0:
    entrada = input()
    entrada = entrada.split(" ")
    x = int(entrada[0])
    y = int(entrada[1])

    if (x < 0) and (y > 0):
        print("segundo")
    elif (x > 0) and (y > 0):
        print("primeiro")
    elif (x < 0) and (y < 0):
        print("terceiro")
    elif (x > 0) and (y < 0):
        print("quarto")
    else :
        numero = 0