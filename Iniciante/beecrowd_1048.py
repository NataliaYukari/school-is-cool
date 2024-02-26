def getReajuste(salario):
    if 0 <= salario <=400:
        reajuste = 0.15
        percent = 15

    elif 400 < salario <= 800:
        reajuste = 0.12
        percent = 12
    elif 800 < salario <= 1200:
        reajuste = 0.10
        percent = 10

    elif 1200 < salario <=2000:
        reajuste = 0.07
        percent = 7

    elif salario > 2000:
        reajuste = 0.04
        percent = 4

    return reajuste, percent

def calculoSalario(salario, reajuste):
    valorGanho = salario * reajuste
    novoSalario = salario + valorGanho

    return novoSalario, valorGanho

salario = float(input())
reajuste, percent = getReajuste(salario)
novoSalario, reajusteGanho = calculoSalario(salario, reajuste)

print("Novo salario:", format(novoSalario, '.2f'))
print("Reajuste ganho:", format(reajusteGanho, '.2f'))
print("Em percentual:", percent, "%")