contador = 0
palabra = input("Escribe una palabra (escribe 'fin' para terminar): ").lower()
while palabra != "fin":
    contador += 1
    palabra = input("Escribe otra palabra (escribe 'fin' para terminar): ").lower()
print("Cantidad de palabras ingresadas:", contador)
