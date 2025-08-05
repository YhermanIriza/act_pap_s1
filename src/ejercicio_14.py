import random
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número (entre 1 y 10): "))
while intento != numero_secreto:
    intento = int(input("Incorrecto. Intenta otra vez: "))
print("¡Felicitaciones! Adivinaste el número:", numero_secreto)
