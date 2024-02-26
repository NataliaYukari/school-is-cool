entrada = input()
entrada = entrada.split(" ")

horaI = int(entrada[0])
minutoI = int(entrada[1])
horaF = int(entrada[2])
minutoF = int(entrada[3])

totalMinutosI = (horaI * 60) + minutoI
totalMinutosF = (horaF * 60) + minutoF
total = totalMinutosF - totalMinutosI

if total <= 0:
    total = total + 1440

hora = total//60
minuto = total%60

print("O JOGO DUROU", hora, "HORA(S) E", minuto, "MINUTO(S)")
