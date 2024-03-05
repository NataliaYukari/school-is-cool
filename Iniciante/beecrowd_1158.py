n = int(input())

for i in range(0, n):
    entrada = input()
    entrada = entrada.split(" ")
    
    x = int(entrada[0])
    y = int(entrada[1])

    soma = 0 
    j = 0

    while j < y:
        if x%2 != 0:
            soma += x
            print("-",x)
            j += 1
        x += 1

    
    print(soma)