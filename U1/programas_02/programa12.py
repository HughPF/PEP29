# programa12
# Enunciado: Sabiendo que 1 milla equivale a 1,61 Km, escribe un programa que pida
# un número de millas y un número de Km, y muestre la conversión redondeada a 2 decimales.

millas = float(input("Introduce una cantidad en millas: "))
kms = float(input("Introduce una cantidad en kilómetros: "))

millas_a_km = millas * 1.61
km_a_millas = kms / 1.61

print(f"{millas} millas = {millas_a_km:.2f} km")
print(f"{kms} km = {km_a_millas:.2f} millas")
