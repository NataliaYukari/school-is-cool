vetorN = [0] * 20
aux = 0
aux2 = 0
fim = 19
for i in range(0, 20):
    vetorN[i] = int(input())

for j in range(0, 10):
    aux = vetorN[j] 
    aux2 = vetorN[fim]
    vetorN[fim] = aux
    vetorN[j] = aux2
    
    fim -= 1

for x in range(0, 20):
    print("N[" + str(x) + "] = " + str(vetorN[x]))