import random
n = int(input("with how many cards do you want to play?? (only numbers please): "))

p_j1 = 0
p_j2 = 0

cartas = [[],[]]
for i in range(1, n+1):
    cartas[0].append(i)
    cartas[1].append(i)

random.shuffle(cartas[0])
random.shuffle(cartas[1])

for i in range(len(cartas)):
    print(cartas[i])