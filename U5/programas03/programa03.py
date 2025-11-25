"""
Programa03: Escritura de un CSV con csv.writer()

Debe:
- Crear capitales.csv con columnas: Ciudad, País, Continente.
- Escribir cabecera con writerow() y datos con writerows().
- Capturar errores con os.strerror().
- Mostrar: "Archivo 'capitales.csv' creado correctamente."
"""

import csv
import os

archivo = "capitales.csv"

cabecera = ["Ciudad", "País", "Continente"]
datos = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"]
]

try:
    with open(archivo, "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)

        escritor.writerow(cabecera)
        escritor.writerows(datos)

    print("Archivo 'capitales.csv' creado correctamente.")

except OSError as e:
    print("Error al crear el archivo:", os.strerror(e.errno))
