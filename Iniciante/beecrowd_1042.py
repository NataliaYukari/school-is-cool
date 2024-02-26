entrada = input()
entrada = entrada.split(" ")
lista = []

def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i])

for i in range(len(entrada)):
    entrada[i] = int(entrada[i])
    lista.append(entrada[i])

for i in range(len(entrada)):
    posicao = i
    for j in range (i + 1, len(entrada)):
        if entrada[j] < entrada[posicao]:
            posicao = j
    
    entrada[i], entrada[posicao] = entrada[posicao], entrada[i]

imprimir(entrada)
print(" ")
imprimir(lista)