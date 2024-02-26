maior = 0

for i in range(0, 100):
    numero = int(input())
    
    if numero > maior:
        maior = numero
        posicao = i

print(maior)
print(posicao + 1)