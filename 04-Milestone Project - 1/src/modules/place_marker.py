def place_marker(board, marker, position):
    # Ecrasement volontaire en n'utilisant pas la fonction copy
    updated_board = board
    updated_board[position] = marker

    return updated_board
