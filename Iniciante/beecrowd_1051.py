salario = float(input())

if 0 <= salario <= 2000:
    print("Isento")

else:
    if 2000 < salario <= 3000:
        reajuste = (salario - 2000) * 0.08
        quota = 0
    
    elif 3000 < salario <= 4500:
        reajuste = (salario - 3000) * 0.18
        quota = (1000 * 0.08)

    elif salario > 4500:
        reajuste = (salario - 4500) * 0.28
        quota = (1000 * 0.08) + (1500 * 0.18)

    imposto = reajuste + quota
    print("R$ " + format(imposto, '.2f'))