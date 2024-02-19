entrada = input()
entrada = entrada.split(" ")

codigo = int(entrada[0])
quantidade = int(entrada[1])

if codigo == 1:
    preco = 4.0
elif codigo == 2:
    preco = 4.5
elif codigo == 3:
    preco = 5.0
elif codigo == 4:
    preco = 2.0
elif codigo == 5:
    preco = 1.5
    
total = float(quantidade * preco)
print("Total: R$", format(total, '.2f'))