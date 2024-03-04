n = int(input())
termo1 = 0
termo2 = 1
fib = []

if n == 1:
    fib.append(0)
else:
    fib.append(0)
    fib.append(1)

    for i in range(0, n-2):
        resultado = termo1 + termo2
        termo1 = termo2
        termo2 = resultado
        fib.append(resultado)

print(" ".join(map(str, fib)))