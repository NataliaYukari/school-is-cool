import math

t = int(input())

for i in range(0, t):
    ent = input()
    ent = ent.split(" ")
    pa, pb, g1, g2 = int(ent[0]), int(ent[1]), float(ent[2]), float(ent[3])

    anos = 0
    while (pb >= pa) and (anos <= 100):
        pa += math.floor(pa * (g1/100))
        pb += math.floor(pb * (g2/100))
        anos += 1


    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(anos,"anos.")