# Pedir un número par y luego uno impar
num = int(input("Introduce un número par (positivo o negativo): "))

if num % 2 != 0:
    print(" El número introducido no es par.")
else:
    num2 = int(input("Introduce un número impar (positivo o negativo): "))
    if num2 % 2 == 0:
        print(" El número introducido no es impar.")
    else:
        print(" Todo correcto.")
