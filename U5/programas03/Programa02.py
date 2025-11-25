"""
Programa02: Lectura con csv.DictReader()

Debe:
- Mostrar los nombres de las columnas (fieldnames).
- Recorrer filas e imprimir:
  {Ciudad} ({País}) tiene una población aproximada de {Población (millones)} millones.
- Si el archivo no incluye cabecera, definir manualmente los nombres de campo.
"""

import csv

ruta = "ciudades.csv"

try:
    with open(ruta, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        fieldnames = lector.fieldnames

        if fieldnames is None:
            fieldnames = ["Ciudad", "País", "Población (millones)"]
            f.seek(0)
            lector = csv.DictReader(f, fieldnames=fieldnames)
            next(lector)

        print("Columnas del fichero:", fieldnames)
        print()

        for fila in lector:
            print(f"{fila['Ciudad']} ({fila['País']}) tiene una población aproximada de {fila['Población (millones)']} millones.")

except FileNotFoundError:
    print("Error: No se encontró el archivo 'ciudades.csv'.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
