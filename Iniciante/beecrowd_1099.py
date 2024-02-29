n = int(input())

for i in range(0, n):
    soma = 0
    entrada = input()
    entrada = entrada.split(" ")
    x = int(entrada[0])
    y = int(entrada[1])

    if x > y:
        x,y = y,x

    for j in range (x+1, y):
        if j%2 != 0:
            soma += j

    print(soma)