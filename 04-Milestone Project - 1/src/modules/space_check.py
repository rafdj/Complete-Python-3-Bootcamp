def space_check(board, position):
    """
        space_check -> boolean
        Description: Check if a position of the board is empty
        Inputs:
            board : list
            position : int
        Outputs:
            True : the position is available
            False : the position is not available
    """
    return board[position] == ' '
