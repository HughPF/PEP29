# programa08
# Juego para adivinar un número entre 1 y 20 con máximo 3 intentos.

import random

numero_secreto = random.randrange(1, 21)
intentos = 3

print("Adivina el número (entre 1 y 20). Tienes 3 intentos.")

for i in range(intentos):
    num = int(input(f"Intento {i+1}: "))
    if num == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    elif num < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    print(f"Has agotado los intentos. El número era {numero_secreto}.")
