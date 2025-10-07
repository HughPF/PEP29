# programa02
# Escribe un que lea por teclado un número comprendido entre 1 y 10.
# No se dejará de pedir el número hasta que se introduzca correctamente.

numero = 0
while numero < 1 or numero > 10:
    numero = int(input("Introduce un número entre 1 y 10: "))

print(f"Número correcto: {numero}")
