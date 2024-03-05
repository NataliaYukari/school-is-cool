vetorA = [0] * 100

for i in range(0, 100):
    vetorA[i] = float(input())

    if vetorA[i] <= 10:
        print("A[" + str(i) + "] = " + format(vetorA[i], '.1f'))