# División entre dos números
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

if b == 0:
    print("⚠️ No se puede dividir entre 0.")
else:
    print(f"✅ El resultado de la división es: {a / b}")
