numero = 1

while numero > 0:
    entrada = input()
    entrada = entrada.split(" ")
    m = int(entrada[0])
    n = int(entrada[1])
    lista = []
    soma = 0

    if (m <= 0) or (n <= 0):
        numero = 0

    else:
        if m > n:
            m,n = n,m

        for i in range(m ,n+1):
            lista.append(i)
            soma += i
        
        print(" ".join(map(str, lista)) + " Sum=" + str(soma))