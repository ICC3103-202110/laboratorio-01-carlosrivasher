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

def play(cards,board,n,points1,points2,player):
    while points1+points2 < n:
        r1 = int(input("First card, Choose a row: "))
        c1 = int(input("First card, Choose a column: "))
        while r1<1 or r1>2 or c1<1 or c1>n:
            print("Invalid numbers, please choose again")
            r1 = int(input("First card, Choose a row: "))
            c1 = int(input("First card, Choose a column: "))
        a = cards[r1-1][c1-1]
        print("The card is", a)
        r2 = int(input("Second card, Choose a row: "))
        c2 = int(input("Second card, Choose a column: "))
        while r2<1 or r2>2 or c2<1 or c2>n:
            print("Invalid numbers, please choose again")
            r2 = int(input("Second card, Choose a row: "))
            c2 = int(input("Second card, Choose a column: "))
        b = cards[r2-1][c2-1]
        print("The card is", b)
        if a==b:
            if player==1:
                points1+=1
            elif player==2:
                points2+=1
            board_print(board)
            print("The cards are the same, you won a point, keep playing")
            print("Player 1 points:", points1)
            print("Player 2 points:", points2)
            
        elif a != b:
            player = players(player)
            board_print(board)
            print("You failed, the cards are different")
            print("Player 1 points:", points1)
            print("Player 2 points:", points2)
            print("Player", player,"plays")
    if points1 > points2:
        print("GAME OVER, PLAYER 1 WINS WITH", points1, "POINTS")
    elif points2 > points1:
        print("GAME OVER, PLAYER 2 WINS WITH", points2, "POINTS")
    else:
        print("GAME OVER, DRAW WITH", points1, "POINTS")

n = int(input("with how many cards do you want to play? (with number please): "))
points1 = 0
points2 = 0
player=1

cards = matriz_cards(n)
board = game_board(n)
board_print(cards)
board_print(board)
print("Player 1 begins")

play(cards,board,n,points1,points2,player)