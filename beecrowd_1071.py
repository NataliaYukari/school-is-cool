X = int(input())
Y = int(input())

if Y < X:
    X, Y = Y, X

soma = int(0)
for i in range(X+1, Y):
    if (i % 2 !=0):
        soma += i

print(soma)