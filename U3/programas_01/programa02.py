"""
programa02
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla los siguientes requisitos:
• Entrada: Tiene 4 parámetros de entrada: nombre, primer apellido, segundo apellido y curso.
  El parámetro curso tendrá en la declaración de la función el valor por defecto “2DAW”.
• Salida: No tiene parámetros de salida.
• Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se haya pasado como parámetro de entrada.
El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar el paso de parámetros de forma nominal (clave=valor).
"""

def saludar(nombre, primer_apellido, segundo_apellido, curso="2DAW"):
    print(f"Hola {nombre} {primer_apellido} {segundo_apellido}, bienvenido/a al curso {curso}.")

# Ejemplos de llamadas
saludar("Laura", "Martínez", "Gómez")  # Usa valor por defecto
saludar("Sergio", "Navarro", "Ruiz", "1DAW")
saludar(nombre="Lucía", primer_apellido="Santos", segundo_apellido="Pérez")
saludar(primer_apellido="Ramírez", nombre="David", segundo_apellido="López", curso="3DAW")
