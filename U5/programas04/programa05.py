"""
Programa 05: Listado y filtrado de países

Requisitos:
- Leer paises.json
- Pedir continente al usuario
- Mostrar solo los países que pertenecen a ese continente
- Guardar el resultado en un nuevo fichero (paises_filtrados.json)
"""

import json

try:
    with open("paises.json", "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)

    continente = input("Introduce un continente: ").strip()

    filtrados = [p for p in paises if p["continente"].lower() == continente.lower()]

    if filtrados:
        print("\nPaíses encontrados:")
        for p in filtrados:
            print(f"- {p['nombre']}")
    else:
        print("No se encontraron países en ese continente.")

    # Guardar en nuevo JSON
    with open("paises_filtrados.json", "w", encoding="utf-8") as f_out:
        json.dump(filtrados, f_out, ensure_ascii=False, indent=4)

    print("\nArchivo 'paises_filtrados.json' creado correctamente.")

except Exception as e:
    print("❌ Error:", e)
