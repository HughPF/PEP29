"""
Programa01: Lectura básica con csv.reader()

Crea un fichero llamado ciudades.csv con el siguiente contenido:
Ciudad,País,Población (millones)
Tokio,Japón,37.4
Delhi,India,30.3
Shanghái,China,27.1
São Paulo,Brasil,22.0

El programa debe:
- Leer el fichero usando csv.reader().
- Mostrar frases como:
  La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes.
- Controlar las posibles excepciones.
"""

import csv

try:
    with open("ciudades.csv", "r", encoding="utf-8") as f:
        lector = csv.reader(f)

        # Saltar cabecera
        next(lector)

        for ciudad, pais, poblacion in lector:
            print(f"La ciudad de {ciudad} está en {pais} y tiene {poblacion} millones de habitantes.")

except FileNotFoundError:
    print("Error: El archivo 'ciudades.csv' no se encontró.")
except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
