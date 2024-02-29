opcao = 1
total = 0
vitoriaInter = 0
vitoriaGremio = 0
empates = 0

while opcao == 1:
    entrada = input()
    entrada = entrada.split(" ")
    inter = int(entrada[0])
    gremio = int(entrada[1])

    if inter > gremio:
        vitoriaInter += 1
    elif gremio > inter:
        vitoriaGremio += 1
    else:
        empates += 1

    total += 1
    opcao = int(input("Novo grenal (1-sim 2-nao)\n"))

print(total, "grenais")
print("Inter:" + str(vitoriaInter))
print("Gremio:" + str(vitoriaGremio))
print("Empates:" + str(empates))

if vitoriaGremio > vitoriaInter:
    print("Gremio venceu mais")
elif vitoriaInter > vitoriaGremio:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")