positivos = 0
soma = 0

for i in range(0, 6):
    entrada = float(input())

    if entrada > 0:
        positivos += 1
        soma += entrada

media = soma/positivos
print(positivos, "valores positivos")
print(round((media), 1))