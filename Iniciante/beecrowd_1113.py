x = 0
y = 1

while x != y:
    entrada = input()
    entrada = entrada.split(" ")
    x = int(entrada[0])
    y = int(entrada[1])

    if x > y:
        print("Decrescente")
    elif x < y: 
        print("Crescente")
