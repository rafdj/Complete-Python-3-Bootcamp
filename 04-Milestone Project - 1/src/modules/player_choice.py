def player_choice(board):
    """
        player_choice -> int
        Description: Select the position to fullfill
        Inputs:
            board : list
        Outputs:
            The position to fullfill in the board
    """
    while True:
        position = input("Please select your position : ")
        if position.isnumeric():
            position = int(position)
            if position > 9:
                print("Please select a number between 1 and 9")
            elif space_check(board, position):

                return(position)
                break
