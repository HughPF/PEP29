"""
Programa 02: Escritura de un fichero JSON

Requisitos:
- Crear capitales.json
- Usar json.dump() con ensure_ascii=False e indent=4
- Mostrar mensaje de éxito
"""

import json

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
]

with open("capitales.json", "w", encoding="utf-8") as fichero:
    json.dump(capitales, fichero, ensure_ascii=False, indent=4)

print("Archivo 'capitales.json' creado correctamente.")
