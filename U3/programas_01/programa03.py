"""
programa03
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar qué operación desea realizar.
Las operaciones que puede realizar serán calcular el área de un círculo, un triángulo o un rectángulo.
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la opción 4.

Funciones requeridas:
- calcular_area_circulo(radio)
- calcular_area_triangulo(base, altura)
- calcular_area_rectangulo(base, altura)
- mostrar_menu()
- main()
- opcion1(), opcion2(), opcion3()
"""

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def opcion1():
    radio = float(input("Introduce el radio del círculo: "))
    if radio > 0:
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    else:
        print(" El radio debe ser mayor que 0.")

def opcion2():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    else:
        print(" La base y la altura deben ser mayores que 0.")

def opcion3():
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")
    else:
        print(" La base y la altura deben ser mayores que 0.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción (1-4): ")
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            print(" Fin del programa")
            break
        else:
            print(" Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
