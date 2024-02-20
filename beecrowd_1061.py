dia_inicio = input()
hora_inicio = input()
dia_fim = input()
hora_fim = input()

dia_inicio = dia_inicio.split(" ")
hora_inicio = hora_inicio.split(" : ")

dias_i = int(dia_inicio[1]) 
horas_i = (dias_i * 24) + int(hora_inicio[0])
minutos_i = (horas_i * 60) + int(hora_inicio[1])
segundos_i = (minutos_i * 60) + int(hora_inicio[2])

dia_fim = dia_fim.split(" ")
hora_fim = hora_fim.split(" : ")

dias_f = int(dia_fim[1])
horas_f = (dias_f * 24) + int(hora_fim[0])
minutos_f = (horas_f * 60) + int(hora_fim[1])
segundos_f = (minutos_f * 60) + int(hora_fim[2])

total_duracao = segundos_f - segundos_i

dias = total_duracao//86400
resto = total_duracao%86400

horas = resto//3600
resto = total_duracao%3600

minutos = resto//60
segundos = resto%60

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")