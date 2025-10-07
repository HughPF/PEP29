# programa07
# Enunciado: Escribe un programa que reciba una cantidad de minutos
# y muestre por pantalla a cuántas horas y minutos corresponde.

minutos = int(input("Introduce la cantidad de minutos: "))
horas = minutos // 60
resto_minutos = minutos % 60

print(minutos, "minutos equivalen a", horas, "hora(s) y", resto_minutos, "minuto(s).")
