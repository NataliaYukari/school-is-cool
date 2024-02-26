N = int(input())

for i in range(0, N):
    numero = int(input())

    if numero == 0:
        print("NULL")
    else: 
        if numero > 0:
            tipo = "POSITIVE"
        elif numero < 0:
            tipo = "NEGATIVE"

        if (numero % 2 == 0) and (numero != 0):
            sinal = "EVEN"
        else:
            sinal = "ODD"

        print(sinal + " " + tipo)