# programa07
# Pide números hasta introducir un 0. Imprime la suma y media.
# Versión 1: con break
# Versión 2: sin break

# Versión 1
suma = 0
contador = 0
while True:
    num = float(input("Introduce un número (0 para salir): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    print(f"Suma: {suma}, Media: {suma / contador}")
else:
    print("No se introdujeron números.")

# Versión 2
suma = 0
contador = 0
num = None
while num != 0:
    num = float(input("Introduce un número (0 para salir): "))
    if num != 0:
        suma += num
        contador += 1

if contador > 0:
    print(f"Suma: {suma}, Media: {suma / contador}")
else:
    print("No se introdujeron números.")
