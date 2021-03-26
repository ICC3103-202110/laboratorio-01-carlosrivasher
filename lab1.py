import random

def matriz_cards(n):
    cards=[[],[]]
    for i in range(1, n+1):
        cards[0].append(i)
        cards[1].append(i)
    random.shuffle(cards[0])
    random.shuffle(cards[1])
    return cards

def game_board(n):
    board=[[],[]]
    for i in range(1, n+1):
        board[0].append("*")
        board[1].append("*")
    return board

def board_print(a):
    for i in range(len(a)):
        print(a[i])

def players(player):
    if player==1:
        player=2
    else:
        player=1
    return player

n = int(input("with how many cards do you want to play? (with number please): "))
points1 = 0
points2 = 0
player=1

cards = matriz_cards(n)
board = game_board(n)

board_print(board)
print("Player 1 begins")

if points1 > points2:
    print("PLAYER 1 WINS WITH", points1, "POINTS")
elif points2 > points1:
    print("PLAYER 2 WINS WITH", points2, "POINTS")
else:
    print("DRAW WITH", points1, "POINTS")