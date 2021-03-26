import random

def matriz_cards(n):
    cartas=[[],[]]
    for i in range(1, n+1):
        cartas[0].append(i)
        cartas[1].append(i)
    random.shuffle(cartas[0])
    random.shuffle(cartas[1])
    return cartas

n = int(input("¿Cuantos pares de carta desea jugar? (Con numeros por favor): "))
p_j1 = 0
p_j2 = 0

cards = matriz_cards(n)

for i in range(len(cards)):
    print(cards[i])

if p_j1 > p_j2:
    print("PLAYER 1 WINS WITH", p_j1, "POINTS")
elif p_j2 > p_j1:
    print("PLAYER 2 WINS WITH", p_j2, "POINTS")
else:
    print("DRAW WITH", p_j1, "POINTS")