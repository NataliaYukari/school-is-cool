vetor = [0] * 10

numero = int(input())

for i in range(0, 10):
    vetor[i] = numero
    numero = numero * 2

    print("N[" + str(i) + "] =", vetor[i])