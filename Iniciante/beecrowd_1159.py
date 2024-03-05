def soma(x):
    soma = 0
    i = 0

    while i < 5:
        if x%2 == 0:
            soma += x
            i += 1
        x += 1
    print(soma) 

x = 1
while x != 0:
    x = int(input())

    if x != 0:
        soma(x)