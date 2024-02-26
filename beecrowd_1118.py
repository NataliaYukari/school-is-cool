def getCodigo():
    print("novo calculo (1-sim 2-nao)")
    codigo = int(input())

    if 1 < codigo > 2:
        return getCodigo()
    else:
        return codigo, 0, 0

codigo = 1
i = 0
soma = 0
while codigo != 2:
    nota = float(input())

    if 0 < nota <= 10:
        soma += nota
        i += 1

        if i == 2:
            print("media =", format(soma/2, '.2f'))
            codigo, i, soma = getCodigo()

    else:
        print("nota invalida")