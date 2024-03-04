x = int(input())
soma = 0
cont = 0

z = int(input())
while z <= x:
    z = int(input())

while soma <= z:
    i = x + cont
    soma += i
    cont += 1

print(cont)