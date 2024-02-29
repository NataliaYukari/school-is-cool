isValido = 0
soma = 0

while isValido != 2:
    nota = float(input())

    if 0 < nota <= 10:
        soma += nota
        isValido += 1

    else:
        print("nota invalida")

print("media =", soma/2)