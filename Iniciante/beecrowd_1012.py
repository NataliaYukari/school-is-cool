entrada = input()
entrada = entrada.split(" ")

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

triangulo = (a * c)/2
circulo = 3.14159 * (c**2)
trapezio = ((a + b) * c)/2
quadrado = b * b
retangulo = a * b

print("TRIANGULO:", format(triangulo, '.3f'))
print("CIRCULO:", format(circulo, '.3f'))
print("TRAPEZIO:", format(trapezio, '.3f'))
print("QUADRADO:", format(quadrado, '.3f'))
print("RETANGULO:", format(retangulo, '.3f'))