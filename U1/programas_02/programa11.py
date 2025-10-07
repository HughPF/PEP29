# programa11
# Enunciado: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de N segundos.
# Escribe un programa que determine la hora de llegada a la ciudad B.

hh = int(input("Introduce la hora de salida (HH): "))
mm = int(input("Introduce los minutos de salida (MM): "))
ss = int(input("Introduce los segundos de salida (SS): "))
n = int(input("Introduce el tiempo de viaje en segundos (N): "))

# Convertimos todo a segundos
salida_total = hh * 3600 + mm * 60 + ss
llegada_total = salida_total + n

# Convertimos de nuevo a HH:MM:SS en formato de 24h
llegada_hh = (llegada_total // 3600) % 24
llegada_mm = (llegada_total % 3600) // 60
llegada_ss = llegada_total % 60

print(f"Hora de llegada: {llegada_hh:02}:{llegada_mm:02}:{llegada_ss:02}")
