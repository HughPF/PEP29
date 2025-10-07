# Comparar dos números
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

if a < b:
    print(f"El menor es {a} y el mayor es {b}")
elif b < a:
    print(f"El menor es {b} y el mayor es {a}")
else:
    print("Ambos números son iguales.")
