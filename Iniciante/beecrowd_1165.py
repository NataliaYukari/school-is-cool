t = int(input())

for i in range(0, t):
    numero = int(input())
    soma = 0

    for j in range(1, numero+1):
        if numero%j == 0:
            soma += j

    if soma == numero + 1:
        print(numero, "eh primo")
    else:
        print(numero, "nao eh primo")