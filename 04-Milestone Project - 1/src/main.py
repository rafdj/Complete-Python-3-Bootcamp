

print('Welcome to Tic Tac Toe!')

marks_choice = ['X','O']

while True:
    
    # Who starts the game : First player name
    player_first = choose_first()
    print(player_first+" you will start the game !")
    
    # Second player name
    if player_first = "Player 1":
        player_second = "Player 2"
    else:
        player_second = "Player 1"
    
    # Players' marks
    player_first_mark = player_input()
    player_second_mark = marks_choice.remove(player_first_mark)[0]

    # Init the game
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_on = True
    while not full_board_check(board):
        display_board(board)
        print(player_first + "'s Turn")
        player_first_choice = player_choice()
        if space_check(board, player_first_choice):
            place_marker(board, player_first_mark, player_first_choice)
        
        if win_check(board, player_first_mark):
            print("Congratulations !! "+player_first)
        elif not full_board_check(board):
            print(player_second + "'s Turn")
            player_second_choice = player_choice()
            if space_check(board, player_second_choice):
                place_marker(board, player_second_mark, player_second_choice)
    
    if not replay():
        break