numero = 1
while numero != 0:
    numero = int(input())

    for i in range (1, numero+1):
        print(i, end= "\n" if i == numero else " ")