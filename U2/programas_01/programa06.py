# Validar una fecha
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

valida = True

# Comprobar rango básico
if mes < 1 or mes > 12 or dia < 1:
    valida = False
else:
    # Días máximos según mes
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if dia > 31:
            valida = False
    elif mes in (4, 6, 9, 11):
        if dia > 30:
            valida = False
    elif mes == 2:
        # Año bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia > 29:
                valida = False
        else:
            if dia > 28:
                valida = False

if valida:
    print("✅ La fecha es correcta.")
else:
    print("⚠️ La fecha no es válida.")
