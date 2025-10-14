"""
programa05
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables en Python (globales, no locales y locales).
"""

# Variable global
mensaje_global = "Soy una variable global"

def funcion_externa():
    mensaje_externo = "Soy una variable no local"

    def funcion_interna():
        nonlocal mensaje_externo
        mensaje_local = "Soy una variable local"
        print(mensaje_global)      # Accede a la global
        print(mensaje_externo)     # Accede a la no local
        print(mensaje_local)       # Accede a la local

        mensaje_externo = "He sido modificada desde la función interna"

    funcion_interna()
    print("Después de modificar:", mensaje_externo)

print("== Demostración de ámbitos de variables ==")
funcion_externa()
print("Variable global:", mensaje_global)
