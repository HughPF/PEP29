# programa10
# Versión con varios jugadores del Black Jack simplificado.
# Pide el número de jugadores y evalúa quién gana o pierde frente a la banca.

import random

banca = random.randint(17, 21)
jugadores = int(input("¿Cuántos jugadores van a jugar? "))

for j in range(1, jugadores + 1):
    print(f"\n Jugador {j}:")
    puntuacion = 0
    continuar = "S"

    while continuar.upper() == "S":
        carta = random.randint(1, 5)
        puntuacion += carta
        print(f"Has sacado un {carta}. Puntuación total: {puntuacion}")

        if puntuacion > 21:
            print(" Te has pasado de 21. Pierdes.")
            break
        continuar = input("¿Quieres sacar otra carta? (S/N): ")

    if puntuacion <= 21:
        print(f"Banca: {banca}")
        if puntuacion > banca:
            print(" ¡Has ganado!")
        else:
            print(" Has perdido.")
