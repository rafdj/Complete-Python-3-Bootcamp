

print('Welcome to Tic Tac Toe!')

while True:
    
    player_first = choose_first()
    
    if player_first = "Player 1":
        player_second = "Player 2"
    else:
        player_second = "Player 1"
        
    print(player_first+" you can start the game !")
    
    
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    while full_board_check(board):
        print(player_first + "'s Turn")
        
        
        print(player_second + "'s Turn")
    
    if not replay():
        break