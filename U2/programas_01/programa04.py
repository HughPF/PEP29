# Nota con calificación
nota = float(input("Introduce una nota entre 0 y 10: "))

match nota:
    case n if 0 <= n < 5:
        print("Insuficiente")
    case n if 5 <= n < 6:
        print("Suficiente")
    case n if 6 <= n < 7:
        print("Bien")
    case n if 7 <= n < 9:
        print("Notable")
    case n if 9 <= n <= 10:
        print("Sobresaliente")
    case _:
        print("⚠️ Nota no válida")
