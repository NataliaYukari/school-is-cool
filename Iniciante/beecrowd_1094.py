N = int(input())

total = 0
totalC = 0
totalR = 0
totalS = 0

for i in range(0, N):
    casoTeste = input()
    casoTeste = casoTeste.split(" ")
    casoTeste[0] = int(casoTeste[0])

    total += casoTeste[0]

    if casoTeste[1] == "C":
        totalC += casoTeste[0]

    elif casoTeste[1] == "R":
        totalR += casoTeste[0]
    
    else:
        totalS += casoTeste[0]

perC = (totalC * 100)/total
perR = (totalR * 100)/total
perS = (totalS * 100)/total

print("Total:", total, "cobaias")
print("Total de coelhos:", totalC)
print("Total de ratos:", totalR)
print("Total de sapos:", totalS)
print("Percentual de coelhos:", format(perC, '.2f'), "%")
print("Percentual de ratos:", format(perR, '.2f'), "%")
print("Percentual de sapos:", format(perS, '.2f'), "%")