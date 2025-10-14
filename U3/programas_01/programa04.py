"""
programa04
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo valores correctos 
(por ejemplo, el radio no puede ser negativo) y si no es así, que muestre un aviso y vuelva a pedir el valor.
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

def leer_valor_positivo(texto):
    while True:
        try:
            valor = float(input(texto))
            if valor > 0:
                return valor
            else:
                print(" El valor debe ser mayor que 0.")
        except ValueError:
            print(" Entrada no válida. Debes introducir un número.")

def opcion1():
    radio = leer_valor_positivo("Introduce el radio del círculo: ")
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")

def opcion2():
    base = leer_valor_positivo("Introduce la base del triángulo: ")
    altura = leer_valor_positivo("Introduce la altura del triángulo: ")
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")

def opcion3():
    base = leer_valor_positivo("Introduce la base del rectángulo: ")
    altura = leer_valor_positivo("Introduce la altura del rectángulo: ")
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area:.2f}")

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
