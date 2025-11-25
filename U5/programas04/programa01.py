"""
Programa 01: Lectura de un fichero JSON

Requisitos:
- Abrir el archivo paises.json con json.load()
- Mostrar cada país con el formato:
  Japón está en Asia y tiene 125.7 millones de habitantes.
- Controlar posibles errores con try/except
"""

import json

try:
    with open("paises.json", "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)

    for pais in paises:
        print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except FileNotFoundError:
    print("❌ Error: el archivo paises.json no existe.")
except json.JSONDecodeError:
    print("❌ Error: el archivo contiene JSON inválido.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
