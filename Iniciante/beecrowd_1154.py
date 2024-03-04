n = 0
soma = 0
cont = -1

while n >= 0:
    soma += n
    n = int(input())
    cont += 1

print(format(soma/cont, '.2f'))
