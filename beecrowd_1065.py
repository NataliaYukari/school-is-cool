cont = 0
for i in range(0,5):
    entrada = int(input())

    if entrada%2 == 0:
        cont += 1

print(cont, "valores pares")