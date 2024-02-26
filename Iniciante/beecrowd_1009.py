nome = input()
salario_fixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
salario = salario_fixo + comissao

print("TOTAL = R$", format(salario, '.2f'))