print('Welcome to Tic Tac Toe!')

while True:

    marks_choice = ['X', 'O']

    # Who starts the game : First player name
    player_first = choose_first()
    print(player_first+" you will start the game !")

    # Second player name
    if player_first == "Player 1":
        player_second = "Player 2"
    else:
        player_second = "Player 1"

    # Players' marks
    player_first_mark = player_input()
    marks_choice.remove(player_first_mark)
    player_second_mark = marks_choice[0]

    # Init the game
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game_on = True
    while not full_board_check(board):
        # Player 1 turn
        display_board(board)
        print(player_first + "'s (" + player_first_mark + ") Turn")
        player_first_choice = player_choice(board)
        if space_check(board, player_first_choice):
            place_marker(board, player_first_mark, player_first_choice)
        if win_check(board, player_first_mark):
            print("Congratulations "+player_first+" !! You won")
            break
        elif not full_board_check(board):
            # No win from Player 1 -> Player 2 turn
            display_board(board)
            print(player_second + "'s (" + player_second_mark + ") Turn")
            player_second_choice = player_choice(board)
            if space_check(board, player_second_choice):
                place_marker(board, player_second_mark, player_second_choice)
            if win_check(board, player_second_mark):
                display_board(board)
                print("Congratulations "+player_second+" !! You won")
                break
        else:
            # Noone won -> Endgame
            display_board(board)
            print("Endgame ! Try again ?")
    # Somebody won or board is full -> Replay ?
    if not replay():
        break
