# programa02
# Enunciado: Escribe un programa que:
# - Cree una variable que almacene el número entero 6.
# - Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto al que apunta la variable.
# - Cree otra variable a la que se asigne la primera variable.
# - Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto al que apunta la variable.
# - Use los operadores de identidad (is / is not) para comprobar que ambas variables apuntan al mismo objeto.
# - Asigne la cadena "Hola" a la primera variable.
# - Muestre el tipo del objeto que contiene la cadena "Hola".
# - Use isinstance() para comprobar los tipos de las dos variables.

a = 6
print("Valor de a:", a, " | Tipo:", type(6), "==", type(a))

b = a
print("Valor de b:", b, " | Tipo:", type(6), "==", type(b))

print("¿a y b apuntan al mismo objeto?", a is b)
print("¿a y b apuntan a objetos distintos?", a is not b)

a = "Hola"
print("Nuevo valor de a:", a, " | Tipo:", type("Hola"), "==", type(a))

print("¿a es int?", isinstance(a, int))
print("¿b es str?", isinstance(b, str))
