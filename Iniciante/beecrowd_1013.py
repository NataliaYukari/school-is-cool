entrada = input()
entrada = entrada.split(" ")

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

if (a - b) > 0:
    abs = a - b
else:
    abs = a - b * -1

maiorAB = (a + b + abs)/2

if maiorAB < c:
    maior = c
else:
    maior = maiorAB

print(round(maior), "eh o maior")