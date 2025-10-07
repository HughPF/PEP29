# programa03
# Escribe un programa que muestre los números pares que hay entre 0 y 10.
# Resuélvelo de 4 formas diferentes:
# 1. for sin continue
# 2. for con continue
# 3. while sin continue
# 4. while con continue

print("1. For sin continue:")
for i in range(0, 11):
    if i % 2 == 0:
        print(i, end=" ")

print("\n2. For con continue:")
for i in range(0, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")

print("\n3. While sin continue:")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print("\n4. While con continue:")
i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")
