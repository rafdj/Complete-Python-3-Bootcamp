def full_board_check(board):
    """
        full_board_check -> boolean
        Description: Detect if the board is full or not
        Outputs:
            True : if board is full
            False : there is alwas cases available
    """
    return ' ' not in board
