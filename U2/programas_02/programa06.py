# programa06
# Leer un número entre 1 y 10 (repetir hasta correcto).
# Mostrar su tabla de multiplicar.
# Luego preguntar si desea introducir otro número (S/N).

continuar = "S"

while continuar.upper() == "S":
    num = 0
    while num < 1 or num > 10:
        num = int(input("Introduce un número entre 1 y 10: "))

    print(f"\nTabla de multiplicar del {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    continuar = input("\n¿Quieres introducir otro número? (S/N): ")

print("Programa finalizado.")
