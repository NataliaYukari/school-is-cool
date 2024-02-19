entrada = int(input())

cont = entrada
impares = 0
while impares < 6:
    if  (cont%2 == 1):
        print(cont)
        impares += 1
    cont += 1