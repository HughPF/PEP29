"""
Programa 04: Escribir un objeto Python en una cadena JSON
"""

import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

# Convertir a cadena JSON con indentación y orden alfabético
cadena = json.dumps(pais, indent=2, sort_keys=True, ensure_ascii=False)

print(cadena)
