codigo = 0
alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
    codigo = int(input())

    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        codigo = 4
    else:
        codigo = 0

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)

