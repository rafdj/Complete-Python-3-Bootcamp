def player_input():
    """
        player_input -> str
        Description : Select the caracter used by a player
        Outputs:
            "X" or "O"
    """
    marker = ''
    while marker not in ('X', 'O'):
        marker = input("Please select your marker 'X' or 'O': ").upper()

    return marker
