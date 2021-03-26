import random

def matriz_cards(n): #creador de tablero de cartas
    cards=[[],[]]
    for i in range(1, n+1):
        cards[0].append(i)
        cards[1].append(i)
    random.shuffle(cards[0])
    random.shuffle(cards[1])
    return cards

def game_board(n): #creador de tablero de juego
    board=[[],[]]
    for i in range(1, n+1):
        board[0].append("*")
        board[1].append("*")
    return board

def board_print(a): #imprime tablero
    for i in range(len(a)):
        print(a[i])

def players(player): #cambio de jugador
    if player==1:
        player=2
    else:
        player=1
    return player

def print_board_replace(cards,board,r1,c1): #mostrar numero en tablero de juego
    card1 = cards[r1-1][c1-1]
    board[r1-1][c1-1] = card1
    return board

def change_board(board,r1,c1,r2,c2): #deja espacios donde estaban las cartas iguales
    if board[r1-1][c1-1] == board[r2-1][c2-1]:
        board[r1-1][c1-1] = " "
        board[r2-1][c2-1] = " "
    board_print(board)
    return board

def clean_board(board): #vuelve a dejar arteriscos donde estaban las cartas distintas
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != " ":
                board[i][j] = "*"
    return board

def play(cards,board,n,points1,points2,player): #juego entero
    while points1+points2 < n:
        r1 = int(input("First card, Choose a row: "))
        c1 = int(input("First card, Choose a column: "))
        while r1<1 or r1>2 or c1<1 or c1>n:
            print("-------------")
            board_print(board)
            print("-------------")
            print("Invalid numbers, please choose again")
            r1 = int(input("First card, Choose a row: "))
            c1 = int(input("First card, Choose a column: "))
        while board[r1-1][c1-1] == " ":
            print("-------------")
            board_print(board)
            print("-------------")
            print("The card has already been chosen, please choose again")
            r1 = int(input("First card, Choose a row: "))
            c1 = int(input("First card, Choose a column: "))
        a = cards[r1-1][c1-1]
        print("The card is", a)
        print("-------------")
        board=print_board_replace(cards,board,r1,c1)
        board_print(board)
        print("-------------")
        r2 = int(input("Second card, Choose a row: "))
        c2 = int(input("Second card, Choose a column: "))
        while r2<1 or r2>2 or c2<1 or c2>n:
            print("-------------")
            board_print(board)
            print("-------------")
            print("INVALID NUMBERS, please choose again")
            print("-------------")
            r2 = int(input("Second card, Choose a row: "))
            c2 = int(input("Second card, Choose a column: "))
        while r1==r2 and c1==c2:
            print("-------------")
            board_print(board)
            print("-------------")
            print("YOU CHOSE THE SAME CARD, please choose again")
            print("-------------")
            r2 = int(input("Second card, Choose a row: "))
            c2 = int(input("Second card, Choose a column: "))
        while board[r2-1][c2-1] == " ":
            print("-------------")
            board_print(board)
            print("-------------")
            print("The card has already been chosen, please choose again")
            r2 = int(input("Second card, Choose a row: "))
            c2 = int(input("Second card, Choose a column: "))
        b = cards[r2-1][c2-1]
        print("The card is", b)
        board = print_board_replace(cards,board,r2,c2)
        print("-------------")
        if a==b:
            if player==1:
                points1+=1
            if player==2:
                points2+=1
            board_print(board)
            print("-------------")
            print("The cards are",a,"and",b,"you won a point,","player",player,"keep playing")
            print("-------------")
            print("Player 1 points:", points1)
            print("Player 2 points:", points2)
            print("-------------")
            board = change_board(board,r1,c1,r2,c2)
            print("-------------")
            
        elif a != b:
            player = players(player)
            board_print(board)
            print("-------------")
            print("You failed, the cards are different")
            print("-------------")
            board = clean_board(board)
            board_print(board)
            print("-------------")
            print("Player 1 points:", points1)
            print("Player 2 points:", points2)
            print("-------------")
            print("Player", player,"plays")
    if points1 > points2: #cuando termina el juego, muestra al ganador o empate
        print("-------------")
        print("GAME OVER, PLAYER 1 WINS WITH", points1, "POINTS")
    elif points2 > points1:
        print("-------------")
        print("GAME OVER, PLAYER 2 WINS WITH", points2, "POINTS")
    else:
        print("-------------")
        print("GAME OVER, DRAW WITH", points1, "POINTS")

n = int(input("with how many cards do you want to play? (with number please): "))
while n <= 1:
    n = int(input("Please select 2 or more cards: "))
points1 = 0 #puntos iniciales jugador 1
points2 = 0 #puntos iniciales jugador 2
player = 1 #para que empiece el jugador 1

cards = matriz_cards(n) #cartas
board = game_board(n) #tablero de juego
board_print(board) #mostrar tablero de juego
print("Player 1 begins")

play(cards,board,n,points1,points2,player) #juego