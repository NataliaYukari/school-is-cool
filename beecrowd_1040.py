def calcularMedia(nota):
    media = ((nota[0] * 2) + (nota[1] * 3) + (nota[2] * 4) + nota[3])/ (2 + 3 + 4 + 1)
    return media

entrada = input()
entrada = entrada.split(" ")

for i in range(0, 4):
    entrada[i] = float(entrada[i])

print("Media:", round(calcularMedia(entrada), 1))

if calcularMedia(entrada) >= 7.0:
    print("Aluno aprovado.")
elif calcularMedia(entrada) < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame:", notaExame)

    mediaFinal = (calcularMedia(entrada) + notaExame)/2

    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final:", mediaFinal)