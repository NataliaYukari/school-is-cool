def getMedia():
    entrada = input()
    entrada = entrada.split(" ")

    for i in range(0,3):
        entrada[i] = float(entrada[i])

    media = ((entrada[0] * 2) + (entrada[1] * 3) + (entrada[2] * 5))/10
    return media

N = int(input())

for i in range(0, N):
    print(format(getMedia(), '.1f'))