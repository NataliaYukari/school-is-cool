def fib(n):
        fib = [0, 1]

        termo1 = 0
        termo2 = 1

        for i in range(0, n):
              resultado = termo1 + termo2
              termo1 = termo2
              termo2 = resultado
              fib.append(resultado)
        
        return fib[n]

t = int(input())

for i in range(0, t):
    n = int(input())

    print("Fib(" + str(n) +") = " + str(fib(n)))