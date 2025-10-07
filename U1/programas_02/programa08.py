# programa08
# Enunciado: Una tienda ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.

total = float(input("Introduce el total de la compra: "))
descuento = total * 0.15
precio_final = total - descuento

print("El precio final con 15% de descuento es:", precio_final)
