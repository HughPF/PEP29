import random

# Tiradas de dados
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)

total_j1 = dado1_j1 + dado2_j1
total_j2 = dado1_j2 + dado2_j2

print(f"Jugador 1: {dado1_j1} + {dado2_j1} = {total_j1}")
print(f"Jugador 2: {dado1_j2} + {dado2_j2} = {total_j2}")

if total_j1 > total_j2:
    print(" Gana Jugador 1")
elif total_j2 > total_j1:
    print(" Gana Jugador 2")
else:
    # Empate en la suma → comparar dado más alto
    max_j1 = max(dado1_j1, dado2_j1)
    max_j2 = max(dado1_j2, dado2_j2)
    if max_j1 > max_j2:
        print(" Gana Jugador 1 por dado más alto")
    elif max_j2 > max_j1:
        print(" Gana Jugador 2 por dado más alto")
    else:
        print(" Empate total")
