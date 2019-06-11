def place_marker(board, marker, position):
    """
        place_marker -> list
        Description: Fullfill board with "X" or "O" @position+1
        Inputs:
            board : list
            marker : str
            position : int
        Outputs:
            Updated board with the position felt by marker
    """
    # Ecrasement volontaire en n'utilisant pas la fonction copy
    updated_board = board
    updated_board[position] = marker

    return updated_board
