n = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= n:
    factorial *= contador
    contador += 1
print("El factorial de", n, "es:", factorial)
