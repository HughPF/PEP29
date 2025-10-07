# programa04
# Escribe un programa que use un bucle while y le pida continuamente al usuario que introduzca un número
# hasta que ingrese 45, en cuyo caso se imprime “¡Has dejado el bucle con éxito!”.
# Versión 1: usar break
# Versión 2: sin usar break (condición de salida en el while)

# Versión 1
while True:
    num = int(input("Introduce un número (45 para salir): "))
    if num == 45:
        print("¡Has dejado el bucle con éxito!")
        break

# Versión 2
num = 0
while num != 45:
    num = int(input("Introduce un número (45 para salir): "))
print("¡Has dejado el bucle con éxito!")
