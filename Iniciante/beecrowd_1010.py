soma = 0
for i in range(0,2):
    entrada = input()
    entrada = entrada.split(" ")

    codigo = int(entrada[0])
    numero = int(entrada[1])
    preco = float(entrada[2])

    soma += numero * preco

print("VALOR A PAGAR: R$", format(soma, '.2f'))
