# programa06
# Escribe un programa que use varias veces la función print() para:
# - Mostrar las operaciones de los operadores aritméticos de Python entre dos números.
# - Mostrar las operaciones de los operadores lógicos de Python con valores booleanos.
# - Mostrar las operaciones de los operadores de comparación de Python con valores booleanos y/o números.

# Operadores aritméticos entre dos números
a = 10
b = 3
print("Suma:", a, "+", b, "=", a + b)
print("Resta:", a, "-", b, "=", a - b)
print("Multiplicación:", a, "*", b, "=", a * b)
print("División:", a, "/", b, "=", a / b)
print("División entera:", a, "//", b, "=", a // b)
print("Módulo:", a, "%", b, "=", a % b)
print("Potencia:", a, "**", b, "=", a ** b)

print()  # Separador visual

# Operadores lógicos con valores booleanos
x = True
y = False
print("AND:", x, "and", y, "=", x and y)
print("OR:", x, "or", y, "=", x or y)
print("NOT:", "not", x, "=", not x)

print()  # Separador visual

# Operadores de comparación con números y booleanos
print("10 > 3:", a > b)
print("10 < 3:", a < b)
print("10 == 3:", a == b)
print("10 != 3:", a != b)
print("True == 1:", True == 1)
print("False == 0:", False == 0)
print("True != False:", True != False)