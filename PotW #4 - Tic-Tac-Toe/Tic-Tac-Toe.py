import random


board = [   [" "]*3, 
            [" "]*3,
            [" "]*3    ]

turn = 1


def introduction():
    tutorial_choice = input("\nWelcome to Tic-Tac-Toe! Would you like a tutorial? (Y/N)\n")
    if tutorial_choice == "Y":
        tutorial()
    elif tutorial_choice == "N":
        players()
    else:
        print("ERROR: INVALID RESPONSE")
        introduction()


def tutorial():
    print("\nThe goal of Tic-Tac-Toe is to get 3 of your marks (X or O) in a row. This can be done horizontally, vertically, or diagonally.")
    print("\nTo place a mark, please enter the corresponding number of the square.\n")

    print("\t       |       |           ")
    print("\t   1   |   2   |   3       ")
    print("\t_______|_______|_______    ")
    print("\t       |       |           ")
    print("\t   4   |   5   |   6       ")
    print("\t_______|_______|_______    ")
    print("\t       |       |           ")
    print("\t   7   |   8   |   9       ")
    print("\t       |       |           ")

    ready_choice = input("\nDo you wish to proceed? (Y/N)\n")
    if ready_choice == "Y":
        players()
    elif ready_choice == "N":
        print(" ")
        exit()
    else:
        print("ERROR: INVALID RESPONSE")
        tutorial()


def players():
    global player1, player2, player_start

    player1 = input("\nWhat is the name of Player 1?\n")
    player2 = input("\nWhat is the name of Player 2?\n")

    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        player_start = player1
    elif coin_flip == 2:
        player_start = player2
    
    player_move()


def player_move():
    global turn, player_current, move

    if turn == 1:
        player_current = player_start

    move = int(input("\n{}, which square would you like to place your mark in?\n".format(player_current)))

    move_result()


def move_result():   
    global turn, player_current, move

    #move == 1
    if move == 1 and player_current == player1 and board[0][0] == " ":
        board[0][0] = "X"
    elif move == 1 and player_current == player2 and board[0][0] == " ":
        board[0][0] = "O"

    #move == 2
    elif move == 2 and player_current == player1 and board[0][1] == " ":
        board[0][1] = "X"
    elif move == 2 and player_current == player2 and board[0][1] == " ":
        board[0][1] = "O"

    #move == 3
    elif move == 3 and player_current == player1 and board[0][2] == " ":
        board[0][2] = "X"
    elif move == 3 and player_current == player2 and board[0][2] == " ":
        board[0][2] = "O"

    #move == 4
    elif move == 4 and player_current == player1 and board[1][0] == " ":
        board[1][0] = "X"
    elif move == 4 and player_current == player2 and board[1][0] == " ":
        board[1][0] = "O"

    #move == 5
    elif move == 5 and player_current == player1 and board[1][1] == " ":
        board[1][1] = "X"
    elif move == 5 and player_current == player2 and board[1][1] == " ":
        board[1][1] = "O"

    #move == 6
    elif move == 6 and player_current == player1 and board[1][2] == " ":
        board[1][2] = "X"
    elif move == 6 and player_current == player2 and board[1][2] == " ":
        board[1][2] = "O"

    #move == 7
    elif move == 7 and player_current == player1 and board[2][0] == " ":
        board[2][0] = "X"
    elif move == 7 and player_current == player2 and board[2][0] == " ":
        board[2][0] = "O"

    #move == 8
    elif move == 8 and player_current == player1 and board[2][1] == " ":
        board[2][1] = "X"
    elif move == 8 and player_current == player2 and board[2][1] == " ":
        board[2][1] = "O"

    #move == 9
    elif move == 9 and player_current == player1 and board[2][2] == " ":
        board[2][2] = "X"
    elif move == 9 and player_current == player2 and board[2][2] == " ":
        board[2][2] = "O"
    else:
        print("ERROR: SQUARE NOT AVAILABLE")
        player_move()

    turn += 1

    if player_current == player1:
        player_current = player2
    elif player_current == player2:
        player_current = player1

    board_update()


def board_update():      
    print("\nX: {} ".format(player1))
    print("O: {}\n ".format(player2))
    
    print("\t        Turn #{}\n         ".format(turn-1))
    print("\t       |       |           ")
    print("\t   {}   |   {}   |   {}    ".format(board[0][0], board[0][1], board[0][2]))
    print("\t_______|_______|_______    ")
    print("\t       |       |           ")
    print("\t   {}   |   {}   |   {}    ".format(board[1][0], board[1][1], board[1][2]))
    print("\t_______|_______|_______    ")
    print("\t       |       |           ")
    print("\t   {}   |   {}   |   {}    ".format(board[2][0], board[2][1], board[2][2]))
    print("\t       |       |           ")

    game_tracker()
    player_move()


def game_tracker():
    #horizontal win cases
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " " and board[0][1] != " " and board[0][2] != " ":
        if board[0][0] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[0][0] == "O":
            print("\n{} wins!\n".format(player2))
        exit()
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " " and board[1][1] != " " and board[1][2] != " ":
        if board[1][0] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[1][0] == "O":
            print("\n{} wins!\n".format(player2))
        exit()
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
        if board[2][0] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[2][0] == "O":
            print("\n{} wins!\n".format(player2))
        exit()

    #vertical win cases
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != " " and board[1][0] != " " and board[2][0] != " ":
        if board[0][0] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[0][0] == "O":
            print("\n{} wins!\n".format(player2))
        exit()
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " " and board[1][1] != " " and board[2][1] != " ":
        if board[0][1] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[0][1] == "O":
            print("\n{} wins!\n".format(player2))
        exit()
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " " and board[1][2] != " " and board[2][2] != " ":
        if board[0][2] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[0][2] == "O":
            print("\n{} wins!\n".format(player2))
        exit()

    #diagonal win cases
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != " " and board[1][1] != " " and board[2][2] != " ":
        if board[0][0] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[0][0] == "O":
            print("\n{} wins!\n".format(player2))
        exit()
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " " and board[1][1] != " " and board[2][0] != " ":
        if board[0][2] == "X":
            print("\n{} wins!\n".format(player1))
        elif board[0][2] == "O":
            print("\n{} wins!\n".format(player2))
        exit()

    #tie case
    elif board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
        print("\nThe game resulted in a tie.\n")
        exit()


introduction()
