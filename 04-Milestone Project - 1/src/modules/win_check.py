def win_check(board, mark):
    """
        win_check -> boolean
        Description: Check alignment of mark to know if it wins
        Inputs:
            board : list
            mark : str
        Outputs:
            True : Player with "mark" has won
            False : Player with "mark" didn't win yet
    """
    board_values = board[1:]

    result = False

    # Diagonal winner
    if mark not in board_values:
        result = False
    elif board_values[0] == board_values[4] == board_values[8] == mark or board_values[2] == board_values[4] == board_values[6] == mark:
        result = True
    else:
        for i in range(0, len(board_values)-2):
            # Horizontal winner
            if board_values[i] == board_values[i+1] == board_values[i+2] == mark and i % 3 == 0:
                return True
                break
            # Vertical winner
            if i < len(board_values)-6:
                if board_values[i] == board_values[i+3] == board_values[i+6] == mark:
                    return True
                    break

    return result
