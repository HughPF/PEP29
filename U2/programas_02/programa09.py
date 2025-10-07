# programa09
# Versión simplificada del Black Jack.
# La banca obtiene un número aleatorio entre 17 y 21.
# El jugador va sacando cartas (1 a 5) hasta que se pase o decida parar.

import random

banca = random.randint(17, 21)
print(" Bienvenido al mini Black Jack!")
print("(La banca tiene su jugada lista.)")

puntuacion = 0
continuar = "S"

while continuar.upper() == "S":
    carta = random.randint(1, 5)
    puntuacion += carta
    print(f"Has sacado un {carta}. Tu puntuación: {puntuacion}")

    if puntuacion > 21:
        print(" Te has pasado de 21. Pierdes.")
        break
    continuar = input("¿Quieres sacar otra carta? (S/N): ")

if puntuacion <= 21:
    print(f"\nBanca: {banca}")
    if puntuacion > banca:
        print(" ¡Has ganado!")
    else:
        print(" Has perdido.")
