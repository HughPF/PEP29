"""
Programa04: Escritura desde diccionarios con csv.DictWriter()

Debe:
- Crear patrimonios.csv
- Usar DictWriter con fieldnames = ["Ciudad", "País", "Lugar emblemático"]
- Escribir cabecera con writeheader()
- Escribir filas con writerows()
- Cambiar delimitador a ;
- Mensaje final: "Archivo 'patrimonios.csv' generado correctamente."
"""

import csv
import os

archivo = "patrimonios.csv"

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    fieldnames = ["Ciudad", "País", "Lugar emblemático"]

    with open(archivo, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")

        escritor.writeheader()
        escritor.writerows(patrimonios)

    print("Archivo 'patrimonios.csv' generado correctamente.")

except OSError as e:
    print("Error:", os.strerror(e.errno))
