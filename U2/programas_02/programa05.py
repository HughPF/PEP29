# programa05
# Escribe un programa que pida un número y muestre una lista desde 1 hasta ese número.
# Controla que esté entre 1 y 10.

num = 0
while num < 1 or num > 10:
    num = int(input("Introduce un número entre 1 y 10: "))

for i in range(1, num + 1):
    print(i, end=" ")
