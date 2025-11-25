"""
Programa 03: Cargar objeto desde una cadena JSON
"""

import json

cadena_json = '''
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

# Convertir cadena a objeto Python
paises = json.loads(cadena_json)

# Mostrar tipo obtenido
print("Tipo de dato obtenido:", type(paises))

# Imprimir cada país
for pais in paises:
    print(f"{pais['nombre']} — Moneda: {pais['moneda']}")
