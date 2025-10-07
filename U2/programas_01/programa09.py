import random

print("Juego Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

jugador = int(input("Seleccione una opción (1, 2 o 3): "))
pc = random.randint(1, 3)

opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

print(f"Tú elegiste: {opciones.get(jugador, 'Opción inválida')}")
print(f"La máquina eligió: {opciones[pc]}")

if jugador not in (1, 2, 3):
    print(" Opción inválida.")
elif jugador == pc:
    print(" Empate.")
elif (jugador == 1 and pc == 3) or (jugador == 2 and pc == 1) or (jugador == 3 and pc == 2):
    print(" Has ganado!")
else:
    print(" Has perdido.")
