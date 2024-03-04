n = int(input())

a = 1
b = 1
c = 1

for i in range(1, n+1):
    a = i * 1
    b = i * i
    c = i**3
    print(a, b, c)

    a = i
    b += 1
    c += 1
    print(a, b, c)

    

